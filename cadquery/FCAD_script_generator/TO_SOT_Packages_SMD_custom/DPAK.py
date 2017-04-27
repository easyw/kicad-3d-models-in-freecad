import cadquery as cq
from Helpers import show

import sys
sys.path.append('./')

from ribbon import Ribbon

import os
import argparse
import yaml
import pprint
import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
import Draft
import ImportGui



class Dimensions(object):

    def __init__(self, base, variant, cut_pin=False):
        # FROM KLC
        self.fab_line_width_mm = 0.1
        self.silk_line_width_mm = 0.12
        self.courtyard_line_width_mm = 0.05
        self.courtyard_clearance_mm = 0.25
        self.courtyard_precision_mm = 0.01

        # PIN NUMBERING
        self.centre_pin = 1 + variant['pins'] // 2
        self.tab_pin_number= self.centre_pin if (cut_pin) else variant['pins'] + 1

        # NAME
        self.name = self.footprint_name(base['package'], (variant['pins'] - 1) if cut_pin else variant['pins'],
                                        not cut_pin, self.tab_pin_number)
        # PADS
        self.pad_1_centre_x_mm = (variant['pad']['x_mm'] / 2.0) - (base['footprint']['x_mm'] / 2.0)
        self.pad_1_centre_y_mm = -variant['pitch_mm'] * (variant['pins'] - 1) / 2.0
        self.tab_centre_x_mm = (base['footprint']['x_mm'] - base['footprint']['tab']['x_mm']) / 2.0
        self.tab_centre_y_mm = 0.0
        self.split_paste = (base['footprint']['split_paste'] == 'on')

        # FAB OUTLINE
        self.device_offset_x_mm = base['device']['x_mm'] / 2.0  # x coordinate of RHS of device
        self.tab_x_mm = base['device']['tab']['x_mm']
        self.tab_offset_y_mm = base['device']['tab']['y_mm'] / 2.0  # y coordinate of bottom of tab
        self.body_x_mm = base['device']['body']['x_mm']
        self.body_offset_y_mm = base['device']['body']['y_mm'] / 2.0  # y coordinate of bottom of body
        self.corner_mm = 1.0  #  x and y size of chamfered corner on top left of body -- from KLC

        # COURTYARD
        self.biggest_x_mm = base['footprint']['x_mm']
        self.biggest_y_mm = max(base['footprint']['tab']['y_mm'], base['device']['body']['y_mm'],
                                       2.0 * self.pad_1_centre_y_mm + variant['pad']['y_mm'])
        self.courtyard_offset_x_mm = self.round_to(self.courtyard_clearance_mm + self.biggest_x_mm / 2.0,
                                                   self.courtyard_precision_mm)
        self.courtyard_offset_y_mm = self.round_to(self.courtyard_clearance_mm + self.biggest_y_mm / 2.0,
                                                   self.courtyard_precision_mm)
        # SILKSCREEN
        self.label_centre_x_mm = 0
        self.label_centre_y_mm = self.courtyard_offset_y_mm + 1
        self.silk_line_nudge_mm = 0.20  #  amount to shift to stop silkscreen lines overlapping fab lines


    def round_to(self, n, precision):
        correction = 0.5 if n >= 0 else -0.5
        return int(n / precision + correction) * precision


    def footprint_name(self, package, num_pins, add_tab, tab_number):
        tab_suffix = '_TabPin' if add_tab else ''
        pins = str(num_pins)
        tab = str(tab_number) if add_tab else ''
        name = '{p:s}-{ps:s}{ts:s}{tn:s}'.format(p=package, ps=pins, ts=tab_suffix, tn=tab)
        return name


class DPAK(object):

    def __init__(self, config_file):
        self.PACKAGE = None
        self.config = None


    def load_config(self, config_file):
        try:
            devices = yaml.load_all(open(config_file))
        except Exception as fnfe:
            print(fnfe)
            return
        config = None
        for dev in devices:
            if dev['base']['package'] == self.PACKAGE:
                config = dev
                break
        return config


    def build_model(self, base, variant, cut_pin=False, verbose=False):

#												KEY:
#												[Y] = already in config file
#												[A] = add to config file
#												[C] = calculate in Dimensions
#												[K] = constant in Dimensions


        LENGTH = 13.85  # Y axis 								[Y]

        BODY_LENGTH = 9.25  # Y axis 								[Y]
        BODY_WIDTH = 10.0  # X axis 								[Y]
        BODY_HEIGHT = 4.4  #									[A]
        BODY_WAIST = 2.4  # Z axis distance from PCB to bottom of chamfers			[A]

        TAB_HEIGHT = 1.27  # Z axis thickness of tab						[A]

        CHAMFER_1 = 0.5  # horizontal part of top side chamfers					[K]
        CHAMFER_2 = BODY_HEIGHT - BODY_WAIST  # vertical part of top side chamfers		[C]
        CHAMFER_3 = 0.2  # horizontal part of bottom front chamfer				[K]

        TAB_LENGTH = 7.55  #									[A]
        TAB_PROJECT = 1.0  # Y axis distance from end of tab to end of body			[Y]
        TAB_TOP_WIDTH = 10.0  # width of part of tab that is outside body			[Y]
        TAB_BOTTOM_WIDTH = 8.5  # width of part of tab that is underneath body			[A] [b]
        TAB_SMALL = 0.5  # approximation used for tab chamfers and shoulders			[K]
        TAB_LARGE = 1.5  # approximation used for tab chamfers and shoulders			[K]

        # Y axis offset of body centre so that whole device is centred on (0, 0)
        BODY_OFFSET = (LENGTH / 2.0) - (BODY_LENGTH / 2.0) - TAB_PROJECT  #			[C]

        NUM_PINS = 7  #										[Y]
        PIN_PITCH = 1.27  #									[Y]
        PIN_WIDTH = 0.6  #									[Y]
        PIN_THICKNESS = 0.5  #									[A]
        PIN_OFFSET = LENGTH / 2.0  # Y axis offset of end of pin				[K]
        PIN_RADIUS = 0.5  #									[K] [a]
        PIN_FAT_WIDTH = PIN_WIDTH + 0.24  # Extra width of wide part on pins			[K] [a]
        PIN_FAT_LENGTH = 0.75  # Length of wide part on pins					[K] [a]
        PIN_FAT_CUT = 4.6  # Used to produce wide part of pins					[K] [a]

        PIN_PROFILE = [  #									[C] [a]
            ('start', {'position': (-PIN_OFFSET, PIN_THICKNESS / 2.0),
                       'direction': 0.0, 'width': PIN_THICKNESS}),
            ('line', {'length': 2.1 - PIN_RADIUS - PIN_THICKNESS / 2.0}),
            ('arc', {'radius': PIN_RADIUS, 'angle': 90.0}),
            ('line', {'length': 0.5}),
            ('arc', {'radius': PIN_RADIUS, 'angle': -90}),
            ('line', {'length': 3})
        ]

        HOLE_DIAMETER = 2.5  #									[A] [b]
        HOLE_DEPTH = 0.1  #									[K]

        NUDGE = 0.02  #										[K]

#												NOTES:
#												[a] maybe override in class if required?
#												[b] or calculate?




        # calculate dimensions and other attributes specific to this variant
        dim = Dimensions(base, variant, cut_pin)

        body = cq.Workplane("XY").workplane(offset=NUDGE).moveTo(0, BODY_OFFSET)\
            .rect(BODY_WIDTH, BODY_LENGTH).extrude(BODY_HEIGHT)

        body = body\
            .faces(">Z").edges(">Y").chamfer(BODY_HEIGHT - TAB_HEIGHT, CHAMFER_1)\
            .faces(">Z").edges("<Y").chamfer(CHAMFER_1, CHAMFER_2)\
            .faces(">Z").edges("<X").chamfer(CHAMFER_1, CHAMFER_2)\
            .faces(">Z").edges(">X").chamfer(CHAMFER_1, CHAMFER_2)\
            .faces("<Z").edges("<Y").chamfer(BODY_WAIST - NUDGE, CHAMFER_3)

        body = body.faces(">Z").hole(HOLE_DIAMETER, depth=HOLE_DEPTH)

        tab = cq.Workplane("XY")\
            .moveTo(0, BODY_OFFSET + BODY_LENGTH / 2.0 + TAB_PROJECT)\
            .line((TAB_TOP_WIDTH/2.0) - TAB_LARGE, 0)\
            .line(TAB_LARGE, -TAB_SMALL)\
            .line(0, -(TAB_PROJECT - TAB_SMALL))\
            .line(-(TAB_TOP_WIDTH - TAB_BOTTOM_WIDTH)/2.0, 0)\
            .line(0, -(TAB_LENGTH - TAB_PROJECT))\
            .line(-TAB_BOTTOM_WIDTH, 0)\
            .line(0, TAB_LENGTH - TAB_PROJECT)\
            .line(-(TAB_TOP_WIDTH - TAB_BOTTOM_WIDTH)/2.0, 0)\
            .line(0, TAB_PROJECT - TAB_SMALL)\
            .line(TAB_LARGE, TAB_SMALL)\
            .close().extrude(TAB_HEIGHT)

        pin = cq.Workplane("YZ")\
            .workplane(offset=-PIN_WIDTH/2.0 - (NUM_PINS - 1) * PIN_PITCH/2.0)
        pin = Ribbon(pin, PIN_PROFILE).drawRibbon().extrude(PIN_WIDTH)
        pins = pin
        for i in range(0, NUM_PINS):
            pins = pins.union(pin.translate((i * PIN_PITCH, 0, 0)))

        fat_pin = cq.Workplane("YZ")\
            .workplane(offset=-(PIN_FAT_WIDTH)/2.0 - (NUM_PINS - 1) * PIN_PITCH/2.0)
        fat_pin = Ribbon(fat_pin, PIN_PROFILE).drawRibbon().extrude(PIN_FAT_WIDTH)
        fat_pins = fat_pin
        for i in range(0, NUM_PINS):
            fat_pins = fat_pins.union(fat_pin.translate((i * PIN_PITCH, 0, 0)))

        cutter = cq.Workplane("XY").moveTo(0, -PIN_OFFSET)\
            .rect(BODY_WIDTH, PIN_FAT_CUT).extrude(BODY_HEIGHT)
        fat_pins = fat_pins.cut(cutter)

        cutter = cq.Workplane("XY")\
            .moveTo(0, -PIN_OFFSET + PIN_FAT_CUT + PIN_FAT_LENGTH)\
            .rect(BODY_WIDTH, PIN_FAT_CUT).extrude(BODY_HEIGHT)
        fat_pins = fat_pins.cut(cutter)

        pins = pins.union(fat_pins)

        return body, tab, pins


    def build_family(self, verbose=False):
        print('Building {p:s}'.format(p=self.config['base']['description']))
        base = self.config['base']
        for variant in self.config['variants']:
            if 'uncut' in variant['centre_pin']:
                print('uncut: {:d}'.format(variant['pins']))
                (body, tab, pins) = self.build_model(base, variant, verbose=verbose)
                yield (body, tab, pins)
            if 'cut' in variant['centre_pin']:
                print('cut: {:d}'.format(variant['pins']))
                (body, tab, pins) = self.build_model(base, variant, cut_pin=True, verbose=verbose)
                yield (body, tab, pins)

class TO263(DPAK):

    def __init__(self, config_file):
        self.PACKAGE = 'TO-263'
        self.config = self.load_config(config_file)


# opened from within freecad
if "module" in __name__:

    FreeCAD.Console.PrintMessage("Started from CadQuery:")

    from DPAK import DPAK, TO263

    CONFIG = '/home/ray/KiCad Contributing/kicad-3d-models-in-freecad/cadquery/FCAD_script_generator/TO_SOT_Packages_SMD_custom/DPAK_config.yaml'
    package = TO263(CONFIG)
    (body, tab, pins) = package.build_family(verbose=True).next()

    show(body)
    show(tab)
    show(pins)

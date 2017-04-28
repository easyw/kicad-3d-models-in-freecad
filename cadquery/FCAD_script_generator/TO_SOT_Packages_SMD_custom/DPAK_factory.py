import sys

sys.path.append('./')

import cadquery as cq
from Helpers import show
from ribbon import Ribbon

import argparse
import yaml


class Dimensions(object):

    def __init__(self, base, variant, cut_pin=False, tab_linked=False):

        # PIN NUMBERING
        self.number_pins = variant['pins']
        self.centre_pin = 1 + self.number_pins // 2
        self.tab_pin_number= self.centre_pin if (tab_linked or cut_pin) else variant['pins'] + 1

        # NAME
        self.name = self.footprint_name(base['series'], (variant['pins'] - 1) if cut_pin else variant['pins'],
                                        not cut_pin, self.tab_pin_number)
        # 3D
        self.device_x_mm = base['device']['x_mm']
        self.body_x_mm = base['device']['body']['x_mm']
        self.body_y_mm = base['device']['body']['y_mm']
        self.body_z_mm = base['device']['body']['z_mm']
        self.body_waist_z_mm = base['device']['body']['waist_z_mm']
        self.marker_offset_x_mm = base['device']['body']['marker_offset_x_mm']
        self.tab_x_mm = base['device']['tab']['x_mm']
        self.tab_z_mm = base['device']['tab']['z_mm']
        self.chamfer_1 = 0.5  # horizontal part of top side chamfers
        self.chamfer_2 = self.body_z_mm - self.body_waist_z_mm  # vertical part of top side chamfers
        self.chamfer_3 = 0.2  # horizontal part of bottom front chamfer
        self.tab_y_mm = base['device']['tab']['y_mm']
        self.tab_project_x_mm = base['device']['tab']['project_x_mm']

        # TODO improve how these values are calculated?

        self.tab_inner_y_mm = self.tab_y_mm * 0.8
        self.tab_large_mm = self.tab_y_mm * 0.15
        self.tab_small_mm = self.tab_project_x_mm * 0.3

        self.body_centre_x_mm = self.device_x_mm / 2.0 - self.tab_project_x_mm - self.body_x_mm / 2.0

        self.pin_pitch_mm = variant['pitch_mm']
        self.pin_y_mm = variant['pin']['y_mm']
        self.pin_z_mm = variant['pin']['z_mm']
        self.pin_offset_x_mm = self.device_x_mm / 2.0

        # TODO improve calculation? override in specific classes?
        self.pin_radius_mm = 0.5
        self.pin_fat_y_mm = self.pin_y_mm + 0.24
        self.pin_fat_x_mm = 0.75  # Length of wide part on pins                    
        self.pin_fat_cut_mm = 4.6  # Used to produce wide part of pins

        self.pin_profile = [
            ('start', {'position': (-self.pin_offset_x_mm, self.pin_z_mm / 2.0),
                       'direction': 0.0, 'width': self.pin_z_mm}),
            ('line', {'length': 2.1 - self.pin_radius_mm - self.pin_z_mm / 2.0}),
            ('arc', {'radius': self.pin_radius_mm, 'angle': 90.0}),
            ('line', {'length': 0.5}),
            ('arc', {'radius': self.pin_radius_mm, 'angle': -90}),
            ('line', {'length': 3})
        ]

        self.marker_x_mm = base['device']['marker']['x_mm']
        self.marker_z_mm = base['device']['marker']['z_mm']
        self.nudge_mm = 0.02


    def round_to(self, n, precision):
        correction = 0.5 if n >= 0 else -0.5
        return int(n / precision + correction) * precision


    def footprint_name(self, series, num_pins, add_tab, tab_number):
        tab_suffix = '_TabPin' if add_tab else ''
        pins = str(num_pins)
        tab = str(tab_number) if add_tab else ''
        name = '{s:s}-{ps:s}{ts:s}{tn:s}'.format(s=series, ps=pins, ts=tab_suffix, tn=tab)
        return name


class DPAK(object):

    def __init__(self, config_file):
        self.SERIES = None
        self.config = None


    def _load_config(self, config_file):
        try:
            devices = yaml.load_all(open(config_file))
        except Exception as fnfe:
            print(fnfe)
            return
        config = None
        for dev in devices:
            if dev['base']['series'] == self.SERIES:
                config = dev
                break
        return config


    def _build_body(self, dim):

        body = cq.Workplane("XY").workplane(offset=dim.nudge_mm).moveTo(dim.body_centre_x_mm, 0)\
            .rect(dim.body_x_mm, dim.body_y_mm).extrude(dim.body_z_mm)

        body = body\
            .faces(">Z").edges(">X").chamfer(dim.body_z_mm - dim.tab_z_mm, dim.chamfer_1)\
            .faces(">Z").edges("<X").chamfer(dim.chamfer_1, dim.chamfer_2)\
            .faces(">Z").edges(">Y").chamfer(dim.chamfer_1, dim.chamfer_2)\
            .faces(">Z").edges("<Y").chamfer(dim.chamfer_1, dim.chamfer_2)\
            .faces("<Z").edges("<X").chamfer(dim.body_waist_z_mm - dim.nudge_mm, dim.chamfer_3)
        body = body.faces(">Z").workplane().center(dim.marker_offset_x_mm, 0).hole(dim.marker_x_mm, depth=dim.marker_z_mm)
        return body


    def _build_tab(self, dim):

        tab = cq.Workplane("XY")\
            .moveTo(dim.device_x_mm / 2.0, 0)\
            .line(0, -(dim.tab_y_mm/2.0) + dim.tab_large_mm)\
            .line(-dim.tab_small_mm, -dim.tab_large_mm)\
            .line(-(dim.tab_project_x_mm - dim.tab_small_mm), 0)\
            .line(0, (dim.tab_y_mm - dim.tab_inner_y_mm)/2.0)\
            .line(-(dim.tab_x_mm - dim.tab_project_x_mm), 0)\
            .line(0, dim.tab_inner_y_mm)\
            .line(dim.tab_x_mm - dim.tab_project_x_mm, 0)\
            .line(0, (dim.tab_y_mm - dim.tab_inner_y_mm)/2.0)\
            .line(dim.tab_project_x_mm - dim.tab_small_mm, 0)\
            .line(dim.tab_small_mm, -dim.tab_large_mm)\
            .close().extrude(dim.tab_z_mm)
        return tab


    def _build_pins(self, dim, cut_pin):

        pin = cq.Workplane("XZ")\
            .workplane(offset=-(dim.pin_y_mm/2.0 + (dim.number_pins - 1) * dim.pin_pitch_mm/2.0))
        pin = Ribbon(pin, dim.pin_profile).drawRibbon().extrude(dim.pin_y_mm)
        pins = pin
        for i in range(0, dim.number_pins):
            if not (cut_pin and i == dim.centre_pin -1):
                pins = pins.union(pin.translate((0, -i * dim.pin_pitch_mm, 0)))

        fat_pin = cq.Workplane("XZ")\
            .workplane(offset=-(dim.pin_fat_y_mm/2.0 + (dim.number_pins - 1) * dim.pin_pitch_mm/2.0))
        fat_pin = Ribbon(fat_pin, dim.pin_profile).drawRibbon().extrude(dim.pin_fat_y_mm)
        fat_pins = fat_pin
        for i in range(0, dim.number_pins):
            if not (cut_pin and i == dim.centre_pin -1):
                fat_pins = fat_pins.union(fat_pin.translate((0, -i * dim.pin_pitch_mm, 0)))

        cutter = cq.Workplane("XY").moveTo(-dim.pin_offset_x_mm, 0)\
            .rect(dim.pin_fat_cut_mm, dim.body_y_mm).extrude(dim.body_z_mm)

        fat_pins = fat_pins.cut(cutter)

        cutter = cq.Workplane("XY")\
            .moveTo(-dim.pin_offset_x_mm + dim.pin_fat_cut_mm + dim.pin_fat_x_mm, 0)\
            .rect(dim.pin_fat_cut_mm, dim.body_y_mm).extrude(dim.body_z_mm)

        fat_pins = fat_pins.cut(cutter)

        pins = pins.union(fat_pins)

        return pins


    def _assemble_model(self, base, dim, body, tab, pins):
        model = {'__name': dim.name,
                 'body': {'part': body, 'colour': base['device']['body']['colour']},
                 'tab':  {'part': tab,  'colour': base['device']['tab']['colour']},
                 'pins': {'part': pins, 'colour': base['device']['pins']['colour']}
                 }
        return model
 

    def _build_model(self, base, variant, cut_pin=False, tab_linked=False, verbose=False):

        dim = Dimensions(base, variant, cut_pin, tab_linked)
        body = self._build_body(dim)
        tab = self._build_tab(dim)
        pins = self._build_pins(dim, cut_pin)
        model = self._assemble_model(base, dim, body, tab, pins)
        return model


    def build_series(self, verbose=False):
        print('Building series {p:s}'.format(p=self.config['base']['description']))
        base = self.config['base']
        for variant in self.config['variants']:
            if 'uncut' in variant['centre_pin']:
                model = self._build_model(base, variant, verbose=verbose)
                yield model
                model = self._build_model(base, variant, tab_linked=True, verbose=verbose)
                yield model
            if 'cut' in variant['centre_pin']:
                model = self._build_model(base, variant, cut_pin=True, verbose=verbose)
                yield model


class TO252(DPAK):

    def __init__(self, config_file):
        self.SERIES = 'TO-252'
        self.config = self._load_config(config_file)


    def _build_tab(self, dim):  # overrides DPAK._build_tab()

        CUTOUT_Y_MM = dim.tab_y_mm * 0.70
        CUTOUT_RADIUS_MM = 0.08
        tab = cq.Workplane("XY")\
            .moveTo(dim.device_x_mm / 2.0, 0)\
            .line(0, -(dim.tab_y_mm/2.0))\
            .line(-dim.tab_project_x_mm, 0)\
            .line(0, (dim.tab_y_mm - dim.tab_inner_y_mm)/2.0)\
            .line(-(dim.tab_x_mm - dim.tab_project_x_mm), 0)\
            .line(0, dim.tab_inner_y_mm)\
            .line(dim.tab_x_mm - dim.tab_project_x_mm, 0)\
            .line(0, (dim.tab_y_mm - dim.tab_inner_y_mm)/2.0)\
            .line(dim.tab_project_x_mm, 0)\
            .close().extrude(dim.tab_z_mm)\
            .faces(">X").edges("|Z").fillet(CUTOUT_RADIUS_MM / 2.0)
        c1 = cq.Workplane("XY")\
            .moveTo(dim.device_x_mm / 2.0, 0)\
            .rect(CUTOUT_RADIUS_MM * 2.0, CUTOUT_Y_MM)\
            .extrude(dim.tab_z_mm)
        c2 = cq.Workplane("XY")\
            .moveTo(dim.device_x_mm / 2.0, CUTOUT_Y_MM / 2.0)\
            .circle(CUTOUT_RADIUS_MM)\
            .extrude(dim.tab_z_mm+1)
        c3 = cq.Workplane("XY")\
            .moveTo(dim.device_x_mm / 2.0, -CUTOUT_Y_MM / 2.0)\
            .circle(CUTOUT_RADIUS_MM)\
            .extrude(dim.tab_z_mm+1)
        cutter = c1.union(c2).union(c3)
        tab = tab.cut(cutter)
        return tab


class TO263(DPAK):

    def __init__(self, config_file):
        self.SERIES = 'TO-263'
        self.config = self._load_config(config_file)


class TO268(DPAK):

    def __init__(self, config_file):
        self.SERIES = 'TO-268'
        self.config = self._load_config(config_file)


class Factory(object):

    def __init__(self, config_file):
        self.config_file = config_file

    def _parse_command_line(self):
        parser = argparse.ArgumentParser(description='Select which packages to build')
        parser.add_argument('package', nargs=argparse.REMAINDER, help='package type to build (e.g. TO252) (default is all types)')
        args = parser.parse_args()
        return args


    def get_build_list(self):
        args = self._parse_command_line()
        packages = args.package[1:]  # remove program name, which is returned as first argument
        if not packages:
            # print('DEBUG: no packages')
            build_list = [TO252(self.config_file), TO263(self.config_file), TO268(self.config_file)]
        else:
            # print('DEBUG: >>{p:s}<<'.format(p=packages))
            build_list = []
            if 'TO252' in packages:
                build_list.append(TO252(self.config_file))
            if 'TO263' in packages:
                build_list.append(TO263(self.config_file))
            if 'TO268' in packages:
                build_list.append(TO268(self.config_file))
        return build_list


# opened from within freecad
if "module" in __name__:

    FreeCAD.Console.PrintMessage("Started from CadQuery ...")

    from DPAK import *

    CONFIG = '/home/ray/KiCad Contributing/kicad-3d-models-in-freecad/cadquery/FCAD_script_generator/TO_SOT_Packages_SMD_custom/DPAK_config.yaml'
    series = TO252(CONFIG)
    model = series.build_series(verbose=True).next()

    for key in model.keys():
        if key is not '__name':
            show(model[key]['part'])


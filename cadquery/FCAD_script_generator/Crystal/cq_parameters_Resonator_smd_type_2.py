# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
# This is a
# Dimensions are from Microchips Packaging Specification document:
# DS00000049BY. Body drawing is the same as QFP generator#

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are a FreeCAD & cadquery tools                                     *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating QFP/SOIC/SSOP/TSSOP models in STEP AP214  *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Lesser General Public License (LGPL)     *
#*   as published by the Free Software Foundation; either version 2 of      *
#*   the License, or (at your option) any later version.                    *
#*   for detail see the LICENCE text file.                                  *
#*                                                                          *
#*   This program is distributed in the hope that it will be useful,        *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
#*   GNU Library General Public License for more details.                   *
#*                                                                          *
#*   You should have received a copy of the GNU Library General Public      *
#*   License along with this program; if not, write to the Free Software    *
#*   Foundation, Inc.,                                                      *
#*   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           *
#*                                                                          *
#****************************************************************************


import cq_parameters  # modules parameters
from cq_parameters import *

import math
from math import tan, cos, sin, radians, sqrt, atan

import cq_base_model  # modules parameters
from cq_base_model import *

class cq_parameters_Resonator_smd_type_2():

    def __init__(self):
        x = 0


    def get_dest_3D_dir(self, modelName):
        for n in self.all_params:
            if n == modelName:
                return self.all_params[modelName].dest_dir_prefix


    def get_dest_file_name(self, modelName):
        for n in self.all_params:
            if n == modelName:
                return self.all_params[modelName].filename


    def model_exist(self, modelName):
        for n in self.all_params:
            if n == modelName:
                return True
                
        return False
        
        
    def get_list_all(self):
        list = []
        for n in self.all_params:
            list.append(n)
        
        return list

        
    def make_3D_model(self, modelName):
        
        top = self.make_top(self.all_params[modelName])
        case = self.make_case(self.all_params[modelName])
        bottom = self.make_bottom(case, self.all_params[modelName])
        pins = self.make_pins(self.all_params[modelName])
        show(top)
        show(case)
        show(bottom)
        show(pins)
     
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
     
        top_color_key = self.all_params[modelName].top_color_key
        body_color_key = self.all_params[modelName].body_color_key
        bottom_color_key = self.all_params[modelName].bottom_color_key
        pin_color_key = self.all_params[modelName].pin_color_key

        top_color = shaderColors.named_colors[top_color_key].getDiffuseFloat()
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        bottom_color = shaderColors.named_colors[bottom_color_key].getDiffuseFloat()
        pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

        Color_Objects(Gui,objs[0], top_color)
        Color_Objects(Gui,objs[1], body_color)
        Color_Objects(Gui,objs[2], bottom_color)
        Color_Objects(Gui,objs[3], pin_color)

        col_body_top = Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_body = Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_bottom = Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        col_pin = Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
        
        material_substitutions={
            col_body_top[:-1]:top_color_key,
            col_body[:-1]:body_color_key,
            col_bottom[:-1]:bottom_color_key,
            col_pin[:-1]:pin_color_key,
        }
        
        expVRML.say(material_substitutions)
        while len(objs) > 1:
                FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
                del objs
                objs = GetListOfObjects(FreeCAD, doc)

        return material_substitutions
    
    def make_top(self, params):

        type = params.type                  # Model type
        L = params.L                        # Model length
        W = params.W                        # Model length
        H = params.H                        # Model heigth
        A1 = params.A1                      # Bottom distance to PCB
        pc = params.p_cnt                   # Number of pins
        psx = params.p_split_x              # Distance between pins, along length
        psy = params.p_split_y              # Distance between pins, along width
        pl = params.p_length                # pin length
        pw = params.p_width                 # pin width
        rotation = params.rotation          # Rotation if required
        
        FreeCAD.Console.PrintMessage('make_top ...\r\n')

        of = 0.0
        if (type == 1):
            tw = W * 1.0
            tl = L * 1.03
            of = H * 0.75
            hl = H - of
            #
            # 
            #
            top = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0, 0.0).rect(tl, tw).extrude(hl)
            top = top.faces("<X").edges("<Y").fillet(W / 60.0)
            top = top.faces("<X").edges(">Y").fillet(W / 60.0)
            top = top.faces(">X").edges("<Y").fillet(W / 60.0)
            top = top.faces(">X").edges(">Y").fillet(W / 60.0)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - (tl / 2.0), 0.0 - (tw / 2.0)).circle(W / 30.0, False).extrude(of + hl + 0.2)
            top = top.cut(cc)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - (tl / 2.0), (tw / 2.0)).circle(W / 30.0, False).extrude(of + hl + 0.2)
            top = top.cut(cc)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo((tl / 2.0), 0.0 - (tw / 2.0)).circle(W / 30.0, False).extrude(of + hl + 0.2)
            top = top.cut(cc)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo((tl / 2.0), (tw / 2.0)).circle(W / 30.0, False).extrude(of + hl + 0.2)
            top = top.cut(cc)

        top = top.translate((0.0, 0.0, A1 + of - 0.01))  # Move down 0.03 to make sure they join
        
        if (rotation != 0):
            top = top.rotate((0,0,0), (0,0,1), rotation)

        return (top)


    def make_case(self, params):

        type = params.type                  # Model type
        L = params.L                        # Model length
        W = params.W                        # Model length
        H = params.H                        # Model heigth
        A1 = params.A1                      # Bottom distance to PCB
        pc = params.p_cnt                   # Number of pins
        psx = params.p_split_x              # Distance between pins, along length
        psy = params.p_split_y              # Distance between pins, along width
        pl = params.p_length                # pin length
        pw = params.p_width                 # pin width
        rotation = params.rotation          # Rotation if required
        
        FreeCAD.Console.PrintMessage('make_case ...\r\n')

        of = 0.02
        if (type == 1):
            #
            # Make slightly smaller than bottom so it is visible in the corners 
            #
            bh = H * 0.75
            tw = W * 0.99
            td = W - tw
            tl = L - td
            case = cq.Workplane("XY").workplane(offset = of).moveTo(0.0, 0.0).rect(tl, tw).extrude(bh * 0.7)
            
            
        case = case.translate((0.0, 0.0, A1 + of))
            
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_bottom(self, body, params):

        type = params.type                  # Model type
        L = params.L                        # Model length
        W = params.W                        # Model length
        H = params.H                        # Model heigth
        A1 = params.A1                      # Bottom distance to PCB
        pc = params.p_cnt                   # Number of pins
        psx = params.p_split_x              # Distance between pins, along length
        psy = params.p_split_y              # Distance between pins, along width
        pl = params.p_length                # pin length
        pw = params.p_width                 # pin width
        rotation = params.rotation          # Rotation if required
        
        FreeCAD.Console.PrintMessage('make_bottom ...\r\n')

        of = 0.0
        if (type == 1):
            bh = H * 0.75
            #
            # 
            #
            bottom = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0, 0.0).rect(L, W).extrude(bh)
            bottom = bottom.cut(body)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - (L / 2.0), 0.0 - (W / 2.0)).circle(W / 30.0, False).extrude(bh + 0.2)
            bottom = bottom.cut(cc)
            body.cut(cc)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - (L / 2.0), (W / 2.0)).circle(W / 30.0, False).extrude(bh + 0.2)
            bottom = bottom.cut(cc)
            body.cut(cc)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo((L / 2.0), 0.0 - (W / 2.0)).circle(W / 30.0, False).extrude(bh + 0.2)
            bottom = bottom.cut(cc)
            body.cut(cc)

            cc = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo((L / 2.0), (W / 2.0)).circle(W / 30.0, False).extrude(bh + 0.2)
            bottom = bottom.cut(cc)
            body.cut(cc)
            

        bottom = bottom.translate((0.0, 0.0, A1 + of))
        
        if (rotation != 0):
            bottom = bottom.rotate((0,0,0), (0,0,1), rotation)

        return (bottom)

        
        
    
    def make_pins(self, params):

        type = params.type                  # Model type
        L = params.L                        # Model length
        W = params.W                        # Model length
        H = params.H                        # Model heigth
        A1 = params.A1                      # Bottom distance to PCB
        pc = params.p_cnt                   # Number of pins
        psx = params.p_split_x              # Distance between pins, along length
        psy = params.p_split_y              # Distance between pins, along width
        pl = params.p_length                # pin length
        pw = params.p_width                 # pin width
        rotation = params.rotation          # Rotation if required
        
        FreeCAD.Console.PrintMessage('make_pins ...\r\n')

        pins = None
        pil = pl
        if (type == 1):
            pil = pl * 0.95
        
        if (pc == 2):
            pins = cq.Workplane("XY").workplane(offset = 0.0).moveTo((psx / 2.0), 0.0).rect(pil, pw).extrude(0.3)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - (psx / 2.0), 0.0).rect(pil, pw).extrude(0.3)
            pins = pins.union(pin)

        if (pc == 4):
            pins = cq.Workplane("XY").workplane(offset = 0.0).moveTo((psx / 2.0), psy / 2.0).rect(pil, pw).extrude(0.3)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - (psx / 2.0), psy / 2.0).rect(pil, pw).extrude(0.3)
            pins = pins.union(pin)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo((psx / 2.0), 0.0 - (psy / 2.0)).rect(pil, pw).extrude(0.3)
            pins = pins.union(pin)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - (psx / 2.0), 0.0 - (psy / 2.0)).rect(pil, pw).extrude(0.3)
            pins = pins.union(pin)

        pins = pins.translate((0.0, 0.0, A1))
        
        if (rotation != 0):
            pins = pins.rotate((0,0,0), (0,0,1), rotation)

        return (pins)


    ##enabling optional/default values to None
    def namedtuple_with_defaults(typename, field_names, default_values=()):

        T = collections.namedtuple(typename, field_names)
        T.__new__.__defaults__ = (None,) * len(T._fields)
        if isinstance(default_values, collections.Mapping):
            prototype = T(**default_values)
        else:
            prototype = T(*default_values)
        T.__new__.__defaults__ = tuple(prototype)
        return T
        
    Params = namedtuple_with_defaults("Params", [
        'type',		            # Model type
        'filename',		        # File name
        'L',				    # Model length
        'W',			   	    # Model width
        'H',			   	    # Model height
        'A1',			   	    # Bottom-board separation
        
        'p_cnt',                # Number of pins
        'p_split_x',		    # Distance between pins, along length
        'p_split_y',		    # Distance between pins, along width
        'p_length',		        # Pin length
        'p_width',		        # Pin width

        'top_color_key',	    # Top color
        'body_color_key',	    # Body color
        'bottom_color_key',	    # Bottom color
        'pin_color_key',	    # Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])

    all_params = {

        'MicroCrystal_CC1V-T1A': Params(
            #
            # https://www.microcrystal.com/fileadmin/Media/Products/32kHz/Datasheet/CC1V-T1A.pdf
            # 
            type = 1,               # Model type, 1 = top is slightly larger than body, only one stair step
            filename = 'Crystal_SMD_MicroCrystal_CC1V-T1A-2Pin_8.0x3.7mm',   # File name
            L = 8.0,                # Model length
            W = 3.7,                # Model width
            H = 1.75,               # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 2,              # Number of pins
            p_split_x = 6.8,        # Distance between pins, along length
            p_length = 1.2,         # Pin length
            p_width = 3.5,          # Pin width

            top_color_key = 'black body',       # Top color
            body_color_key = 'gold pins',       # Body color
            bottom_color_key = 'black body',    # Bottom color
            pin_color_key = 'gold pins',        # Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'MicroCrystal_CC4V-T1A': Params(
            #
            # http://cdn-reichelt.de/documents/datenblatt/B400/CC4V-T1A.pdf
            # 
            type = 1,               # Model type, 1 = top is slightly larger than body, only one stair step
            filename = 'Crystal_SMD_MicroCrystal_CC4V-T1A-2Pin_5.0x1.9mm',   # File name
            L = 5.0,                # Model length
            W = 1.9,                # Model width
            H = 0.9,                # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 2,              # Number of pins
            p_split_x = 4.1,        # Distance between pins, along length
            p_length = 0.9,         # Pin length
            p_width = 1.7,          # Pin width

            top_color_key = 'black body',       # Top color
            body_color_key = 'gold pins',       # Body color
            bottom_color_key = 'black body',    # Bottom color
            pin_color_key = 'gold pins',        # Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'MicroCrystal_CC5V-T1A': Params(
            #
            # http://cdn-reichelt.de/documents/datenblatt/B400/CC5V-T1A.pdf
            # 
            type = 1,               # Model type, 1 = top is slightly larger than body, only one stair step
            filename = 'Crystal_SMD_MicroCrystal_CC5V-T1A-2Pin_4.1x1.5mm',   # File name
            L = 4.1,                # Model length
            W = 1.5,                # Model width
            H = 0.9,                # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 2,              # Number of pins
            p_split_x = 3.0,        # Distance between pins, along length
            p_length = 1.1,         # Pin length
            p_width = 1.3,          # Pin width

            top_color_key = 'black body',       # Top color
            body_color_key = 'gold pins',       # Body color
            bottom_color_key = 'black body',    # Bottom color
            pin_color_key = 'gold pins',        # Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'MicroCrystal_CC7V-T1A': Params(
            #
            # https://www.microcrystal.com/fileadmin/Media/Products/32kHz/Datasheet/CC7V-T1A.pdf
            # 
            type = 1,               # Model type, 1 = top is slightly larger than body, only one stair step
            filename = 'Crystal_SMD_MicroCrystal_CC7V-T1A-2Pin_3.2x1.5mm',   # File name
            L = 3.2,                # Model length
            W = 1.5,                # Model width
            H = 0.9,                # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 2,              # Number of pins
            p_split_x = 2.2,        # Distance between pins, along length
            p_length = 1.0,         # Pin length
            p_width = 1.3,          # Pin width

            top_color_key = 'black body',       # Top color
            body_color_key = 'gold pins',       # Body color
            bottom_color_key = 'black body',    # Bottom color
            pin_color_key = 'gold pins',        # Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'MicroCrystal_CC8V-T1A': Params(
            #
            # https://www.microcrystal.com/fileadmin/Media/Products/32kHz/Datasheet/CC8V-T1A.pdf
            # 
            type = 1,               # Model type, 1 = top is slightly larger than body, only one stair step
            filename = 'Crystal_SMD_MicroCrystal_CC8V-T1A-2Pin_2.0x1.2mm',   # File name
            L = 2.0,                # Model length
            W = 1.2,                # Model width
            H = 0.67,                # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 2,              # Number of pins
            p_split_x = 1.2,        # Distance between pins, along length
            p_length = 0.8,         # Pin length
            p_width = 1.0,          # Pin width

            top_color_key = 'black body',       # Top color
            body_color_key = 'gold pins',       # Body color
            bottom_color_key = 'black body',    # Bottom color
            pin_color_key = 'gold pins',        # Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'MicroCrystal_CM9V-T1A': Params(
            #
            # https://www.microcrystal.com/fileadmin/Media/Products/32kHz/Datasheet/CM9V-T1A.pdf
            # 
            type = 1,               # Model type, 1 = top is slightly larger than body, only one stair step
            filename = 'Crystal_SMD_MicroCrystal_CM9V-T1A-2Pin_1.6x1.0mm',   # File name
            L = 1.6,                # Model length
            W = 1.0,                # Model width
            H = 0.5,                # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 2,              # Number of pins
            p_split_x = 1.0,        # Distance between pins, along length
            p_length = 0.6,         # Pin length
            p_width = 0.8,          # Pin width

            top_color_key = 'black body',       # Top color
            body_color_key = 'gold pins',       # Body color
            bottom_color_key = 'black body',    # Bottom color
            pin_color_key = 'gold pins',        # Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

    }

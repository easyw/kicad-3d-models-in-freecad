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

class cq_parameters_Resonator_peterman_smd():

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
     
        body_top_color_key = self.all_params[modelName].body_top_color_key
        body_color_key = self.all_params[modelName].body_color_key
        bottom_color_key = self.all_params[modelName].bottom_color_key
        pin_color_key = self.all_params[modelName].pin_color_key

        body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        bottom_color = shaderColors.named_colors[bottom_color_key].getDiffuseFloat()
        pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

        Color_Objects(Gui,objs[0],body_top_color)
        Color_Objects(Gui,objs[1],body_color)
        Color_Objects(Gui,objs[2],bottom_color)
        Color_Objects(Gui,objs[3],pin_color)

        col_body_top = Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_body = Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_bottom = Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        col_pin = Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
        
        material_substitutions={
            col_body_top[:-1]:body_top_color_key,
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

        tw = W * 0.80
        td = W - tw
        tl = L - td
        #
        # 
        #
        top = cq.Workplane("XY").workplane(offset = 0.2).moveTo(0.0, 0.0).rect(tl, tw).extrude(A1 + (H - 0.2))
        top = top.faces("<X").edges("<Y").fillet(W / 18.0)
        top = top.faces("<X").edges(">Y").fillet(W / 18.0)
        top = top.faces(">X").edges("<Y").fillet(W / 18.0)
        top = top.faces(">X").edges(">Y").fillet(W / 18.0)
        
        top = top.translate((0.0, 0.0, A1 + 0.03))
        
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
        
        FreeCAD.Console.PrintMessage('make_top ...\r\n')

        bh = H * 0.5
        bc0 = H * 0.505
        bc1 = H * 0.75
        bc2 = H * 0.995
        #
        # Make slightly smaller than bottom so it is visible in the corners 
        #
        tw = W * 0.99
        td = W - tw
        tl = L - td
        case = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0, 0.0).rect(tl, tw).extrude(bh * 0.7)

        #
        # First step
        #
        tw = W * 0.93
        td = W - tw
        tl = L - td
        case0 = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0, 0.0).rect(tl, tw).extrude(bc0)
        case0 = case0.faces("<X").edges("<Y").fillet(W / 12.0)
        case0 = case0.faces("<X").edges(">Y").fillet(W / 12.0)
        case0 = case0.faces(">X").edges("<Y").fillet(W / 12.0)
        case0 = case0.faces(">X").edges(">Y").fillet(W / 12.0)

        #
        # Second step
        #
        tw = W * 0.90
        td = W - tw
        tl = L - td
        case1 = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0, 0.0).rect(tl, tw).extrude(bc1)
        case1 = case1.faces("<X").edges("<Y").fillet(W / 12.0)
        case1 = case1.faces("<X").edges(">Y").fillet(W / 12.0)
        case1 = case1.faces(">X").edges("<Y").fillet(W / 12.0)
        case1 = case1.faces(">X").edges(">Y").fillet(W / 12.0)

        #
        # Third step
        #
        tw = W * 0.85
        td = W - tw
        tl = L - td
        case2 = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0, 0.0).rect(tl, tw).extrude(bc2)
        case2 = case2.faces("<X").edges("<Y").fillet(W / 12.0)
        case2 = case2.faces("<X").edges(">Y").fillet(W / 12.0)
        case2 = case2.faces(">X").edges("<Y").fillet(W / 12.0)
        case2 = case2.faces(">X").edges(">Y").fillet(W / 12.0)

        case = case.union(case0)
        case = case.union(case1)
        case = case.union(case2)
        
        case = case.faces("|Z").edges("not(<X or >X or <Y or >Y)").fillet(W / 200.0)
        
        
        
        case = case.translate((0.0, 0.0, A1 + 0.03))
        
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

        bh = H * 0.5
        #
        # Make slightly smaller than bottom so it is visible in the corners 
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
        
        bottom = bottom.faces(">Z").fillet(W / 200.0)

        bottom = bottom.translate((0.0, 0.0, A1 + 0.03))
        
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
        if (pc == 2):
            pins = cq.Workplane("XY").workplane(offset = 0.0).moveTo((psx / 2.0), 0.0).rect(pl, pw).extrude(0.3)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - (psx / 2.0), 0.0).rect(pl, pw).extrude(0.3)
            pins = pins.union(pin)

        if (pc == 4):
            pins = cq.Workplane("XY").workplane(offset = 0.0).moveTo((psx / 2.0), psy / 2.0).rect(pl, pw).extrude(0.3)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - (psx / 2.0), psy / 2.0).rect(pl, pw).extrude(0.3)
            pins = pins.union(pin)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo((psx / 2.0), 0.0 - (psy / 2.0)).rect(pl, pw).extrude(0.3)
            pins = pins.union(pin)

            pin = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - (psx / 2.0), 0.0 - (psy / 2.0)).rect(pl, pw).extrude(0.3)
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

        'body_top_color_key',	# Top color
        'body_color_key',	    # Body color
        'bottom_color_key',	    # Bottom color
        'pin_color_key',	    # Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])

    all_params = {

        'SMD_0603-2Pin': Params(
            #
            # https://www.petermann-technik.com/fileadmin/documents/datasheets/Quarz-Crystals/SMD-QUARTZ-CRYSTAL-SMD0603-2.pdf
            # 
            type = 1,               # Model type
            filename = 'Crystal_SMD_0603-2Pin_6.0x3.5mm',   # File name
            L = 6.0,                # Model length
            W = 3.5,                # Model width
            H = 1.1,                # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 2,              # Number of pins
            p_split_x = 4.5,        # Distance between pins, along length
            p_length = 1.5,         # Pin length
            p_width = 2.0,          # Pin width

            body_top_color_key = 'metal aluminum',  # Top color
            body_color_key = 'gold pins',           # Body color
            bottom_color_key = 'black body',        # Bottom color
            pin_color_key = 'metal grey pins',      # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'SMD_0603-4Pin': Params(
            #
            # https://www.petermann-technik.com/fileadmin/documents/datasheets/Quarz-Crystals/SMD-QUARTZ-CRYSTAL-SMD0603-2.pdf
            # 
            type = 1,               # Model type
            filename = 'Crystal_SMD_0603-4Pin_6.0x3.5mm',   # File name
            L = 6.0,                # Model length
            W = 3.5,                # Model width
            H = 1.0,                # Model heigth
            A1 = 0.0,               # Bottom-board separation
            
            p_cnt = 4,              # Number of pins
            p_split_x = 4.4,        # Distance between pins, along length
            p_split_y = 2.4,        # Distance between pins, along width
            p_length = 1.4,         # Pin length
            p_width = 0.9,          # Pin width

            body_top_color_key = 'metal aluminum',  # Top color
            body_color_key = 'gold pins',           # Body color
            bottom_color_key = 'black body',        # Bottom color
            pin_color_key = 'metal grey pins',      # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'Crystal_SMD_2012-2Pin_2.0x1.2mm': Params(
            #
            # https://www.sii.co.jp/en/quartz/files/2013/03/SC-20S_Leaflet_e20151217.pdf
            #
            type = 1,               # Model type
            filename = 'Crystal_SMD_2012-2Pin_2.0x1.2mm',   # File name
            L = 2.05,                # Model length
            W = 1.2,                # Model width
            H = 0.6,                # Model heigth
            A1 = 0.0,               # Bottom-board separation

            p_cnt = 2,              # Number of pins
            p_split_x = 1.5,        # Distance between pins, along length
            p_length = 0.425,         # Pin length
            p_width = 1.0,          # Pin width

            body_top_color_key = 'metal aluminum',  # Top color
            body_color_key = 'gold pins',           # Body color
            bottom_color_key = 'black body',        # Bottom color
            pin_color_key = 'metal grey pins',      # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),


    }
        

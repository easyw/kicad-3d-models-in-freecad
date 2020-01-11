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


import cq_support  # modules parameters
from cq_support import *

import math


class cq_Sanyo_STK4xx():

    def __init__(self):
        x = 0


    def get_dest_3D_dir(self, modelName):
        return self.all_params[modelName].dest_dir_prefix


    def get_modelfilename(self, modelName):
        return self.all_params[modelName].modelName


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
        
        params = self.all_params[modelName]

        if modelName == 'Sanyo_STK4xx_59_2':
            case_top = self.make_top_Sanyo_STK4xx_59_2(params)
            show(case_top)
            case = self.make_case_Sanyo_STK4xx_59_2(params)
            show(case)
            pins = self.make_pins_Sanyo_STK4xx_59_2(params)
            show(pins)

            
        elif modelName == 'Sanyo_STK4xx_78_0':
            case_top = self.make_top_Sanyo_STK4xx_78_0(params)
            show(case_top)
            case = self.make_case_Sanyo_STK4xx_78_0(params)
            show(case)
            pins = self.make_pins_Sanyo_STK4xx_78_0(params)
            show(pins)
            
        npth_pins = self.make_npth_pins(params)
        show(npth_pins)
     
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
     
        body_top_color_key = params.body_top_color_key
        body_color_key = params.body_color_key
        pin_color_key = params.pin_color_key
        npth_pin_color_key = params.npth_pin_color_key

        body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()
        npth_pin_color = shaderColors.named_colors[npth_pin_color_key].getDiffuseFloat()

        Color_Objects(Gui,objs[0],body_top_color)
        Color_Objects(Gui,objs[1],body_color)
        Color_Objects(Gui,objs[2],pin_color)
        Color_Objects(Gui,objs[3],npth_pin_color)

        col_body_top=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_body=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        col_npth_pin=Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
        
        material_substitutions={
            col_body_top[:-1]:body_top_color_key,
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pin_color_key,
            col_npth_pin[:-1]:npth_pin_color_key
        }
        
        expVRML.say(material_substitutions)
        while len(objs) > 1:
                FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
                del objs
                objs = GetListOfObjects(FreeCAD, doc)

        return material_substitutions


    def make_top_Sanyo_STK4xx_59_2(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required


        #
        # Create dummy
        #
        case = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(0.0, 0.0).circle(0.005, False).extrude(0.001)

        return (case)


    def make_case_Sanyo_STK4xx_59_2(self, params):

        L = params.L                        # Body length
        W = params.W                        # Body width
        H = params.H                        # Body height
        BH = params.BH                      # Body hole
        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        smallpad_w = 9.6
        smallpad_l = 0.48
        smallpad_h = 7.37
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        #
        # Hole in body
        #
        for ph in BH:
            case1 = cq.Workplane("ZX").workplane(offset=0.0 - L).moveTo(ph[1], ph[0]).circle(ph[2] / 2.0, False).extrude((2.0 * L))
            case = case.cut(case1)
        #
        # Cut lower part of body
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 1.0).moveTo(0.0, 0.0).rect(4.0, L + 2.0).extrude(H + 2.0)
        case1 = case1.rotate((0,0,0), (0,1,0), 10.0)
        case1 = case1.translate((W / 2 - 0.8, 0.0, 0.0))
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 1.0).moveTo(0.0, 0.0).rect(4.0, L + 2.0).extrude(H + 2.0)
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 - 10.0)
        case1 = case1.translate(( 0.0 - (W / 2 - 0.8), 0.0, 0.0))
        case = case.cut(case1)
        
        
        dx = (7.0 * 2.54)
        case = case.translate((dx, 0.0, A1))

        case = case.faces(">Z").edges("<X").fillet(3.0)
        case = case.faces(">Z").edges(">X").fillet(3.0)
        case = case.faces("<Z").edges(">X").fillet(3.0)
        case = case.faces("<Z").edges("<X").fillet(3.0)
#        case = case.faces(">Y").edges("<X").fillet(2.0)
        case = case.faces(">Y").edges("<Z").fillet(2.0)
        case = case.faces(">Y").edges(">Z").fillet(1.9)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_Sanyo_STK4xx_59_2(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        pin_w = 0.5
        pin_l = 0.5
        pin_h = 7.5 * 1.3

        #
        # Create pin
        #

        tx = 0.0
        pin = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - pin_h)
        for i in range(0, 14):
            tx = tx + 2.54
            pin1 = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(tx, 0.0).rect(pin_w, pin_l).extrude(0.0 - pin_h)
            pin = pin.union(pin1)


        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_top_Sanyo_STK4xx_78_0(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required


        #
        # Create dummy
        #
        case = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(0.0, 0.0).circle(0.005, False).extrude(0.001)

        return (case)


    def make_case_Sanyo_STK4xx_78_0(self, params):

        L = params.L                        # Body length
        W = params.W                        # Body width
        H = params.H                        # Body height
        A1 = params.A1                      # Body PCB seperation
        BH = params.BH                      # Body hole
        rotation = params.rotation          # Rotation if required

        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        #
        # Hole in body
        #
        for ph in BH:
            case1 = cq.Workplane("ZX").workplane(offset=0.0 - L).moveTo(ph[1], ph[0]).circle(ph[2] / 2.0, False).extrude((2.0 * L))
            case = case.cut(case1)
        #
        # Cut lower part of body
        #
        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(0.0 - 3.0, 0.0 - (2.0 * L)).rect(6.0, L * 4.0, centered=False).extrude(0.0 - (H + 2.0))
        case1 = case1.rotate((0,0,0), (0,1,0), 10.0)
        case1 = case1.translate((W / 2 - 0.8, 0.0, 0.0))
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=H * 1.5).moveTo(0.0 + 4.5, 0.0 - (2.0 * L)).rect(6.0, L * 4.0, centered=False).extrude(0.0 - (H + 2.0))
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 - 10.0)
        case1 = case1.translate((W / 2 - 0.8, 0.0, 0.0))
        case = case.cut(case1)
        #
        #
        #
        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(0.0 - 3.0, 0.0 - (2.0 * L)).rect(6.0, L * 4.0, centered=False).extrude(0.0 - (H + 2.0))
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 - 10.0)
        case1 = case1.translate(( 0.0 - (W / 2 - 0.8), 0.0, 0.0))
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=H * 1.5).moveTo(0.0 - 10.5, 0.0 - (2.0 * L)).rect(6.0, L * 4.0, centered=False).extrude(0.0 - (H + 2.0))
        case1 = case1.rotate((0,0,0), (0,1,0), 10.0)
        case1 = case1.translate(( 0.0 - (W / 2 - 0.8), 0.0, 0.0))
        case = case.cut(case1)
        
        
        dx = (7.0 * 2.54)
        case = case.translate((dx, 0.0, A1))

        case = case.faces(">Z").edges("<X").fillet(3.0)
        case = case.faces(">Z").edges(">X").fillet(3.0)
        case = case.faces("<Z").edges(">X").fillet(3.0)
        case = case.faces("<Z").edges("<X").fillet(3.0)
        case = case.faces(">Y").edges("<Z").fillet(2.0)
        case = case.faces(">Y").edges(">Z").fillet(1.9)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_Sanyo_STK4xx_78_0(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        pin_w = 0.5
        pin_l = 0.5
        pin_h = 7.5 * 1.3

        #
        # Create pin
        #

        tx = 0.0
        pin = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - pin_h)
        for i in range(0, 14):
            tx = tx + 2.54
            pin1 = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(tx, 0.0).rect(pin_w, pin_l).extrude(0.0 - pin_h)
            pin = pin.union(pin1)


        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_npth_pins(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        #
        # Create dummy
        #
        case = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(0.0, 0.0).circle(0.005, False).extrude(0.001)

        return (case)


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
        'modelName',            # modelName
        'L',                    # Body length
        'W',                    # Body width
        'H',                    # Body height
        'A1',                   # Body PCB seperation
        'BH',                   # Body hole
        'body_top_color_key',   # Top color
        'body_color_key',       # Body colour
        'pin_color_key',        # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'       # Destination directory
    ])



    all_params = {


        'Sanyo_STK4xx_59_2': Params(
            #
            # http://datasheet.octopart.com/STK430-Sanyo-datasheet-107060.pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Sanyo_STK4xx-15_59.2x8.0mm_P2.54mm',    # modelName
            L =  8.0,                                       # Body length
            W = 59.2,                                       # Body width
            H = 32.0,                                       # Body height
            A1 = 7.5,                                       # Body PCB seperation
            BH = [[-26.0, 20.5, 3.6], [26.0, 20.5, 3.6]],   # Body hole

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),


        'Sanyo_STK4xx_78_0': Params(
            #
            # http://datasheet.octopart.com/STK430-Sanyo-datasheet-107060.pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Sanyo_STK4xx-15_78.0x8.0mm_P2.54mm',    # modelName
            L =  8.0,                                       # Body length
            W = 78.0,                                       # Body width
            H = 44.0,                                       # Body height
            A1 = 7.5,                                       # Body PCB seperation
            BH = [[-35.0, 22.00, 3.6], [35.0, 22.00, 3.6]], # Body hole
            
            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

    }
        
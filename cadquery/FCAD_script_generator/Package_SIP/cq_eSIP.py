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


class cq_eSIP():

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

        if params.modelName == 'PowerIntegrations_eSIP-7C':
            case_top = self.make_top_eSIP_7C(params)
            show(case_top)
            case = self.make_case_eSIP_7C(params)
            show(case)
            pins = self.make_pins_eSIP_7C(params)
            show(pins)

        elif params.modelName == 'PowerIntegrations_eSIP-7F':
            case_top = self.make_top_eSIP_7F(params)
            show(case_top)
            case = self.make_case_eSIP_7F(params)
            show(case)
            pins = self.make_pins_eSIP_7F(params)
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


    def make_top_eSIP_7C(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        smallpad_w = 9.6
        smallpad_l = 0.48
        smallpad_h = 7.37
        #
        large_w = 10.16
        large_l = 1.53
        large_h = 8.19
        #
        metal_w = 6.7
        metal_l = 0.1
        metal_h = 5.04

        case = cq.Workplane("XY").workplane(offset=A1 + (large_h - metal_h) / 2.0).moveTo(0.0, (large_l / 2.0) + smallpad_l ).rect(metal_w, metal_l).extrude(metal_h)
        case = case.translate((0.0 + ((large_w / 2.0) - 1.27), 0.0, 0.0))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_eSIP_7C(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        smallpad_w = 9.6
        smallpad_l = 0.48
        smallpad_h = 7.37
        #
        large_w = 10.16
        large_l = 1.53
        large_h = 8.19
        
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(0.0, 0.0).rect(large_w, large_l).extrude(large_h)
        case = case.faces("<Y").fillet(large_l / 6.0)
        case1 = cq.Workplane("XY").workplane(offset=A1 + (large_h - smallpad_h) / 2.0).moveTo(0.0, (large_l / 2.0) + (smallpad_l / 2.0)).rect(smallpad_w, smallpad_l).extrude(smallpad_h)
        case1 = case1.faces(">Y").chamfer(smallpad_l / 3.0)
        case = case.union(case1)
        case1 = cq.Workplane("XZ").workplane(offset=(large_l / 2.0) - 0.1).moveTo(0.0 - ((smallpad_w / 2.0) - 1.0), A1 + 1.0).circle(0.5, False).extrude(2.0)
        case = case.cut(case1)

        case = case.translate((0.0 + ((large_w / 2.0) - 1.27), 0.0, 0.0))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_eSIP_7C(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        pin_l = 0.345
        pin_w = 0.775
        pin_h = 5.005
        tth = pin_h
        ang = 10.0
        dxd = 3.0
        upph = 1.0
        
        #
        #
        # Create body
        #
        pin  = cq.Workplane("XY").workplane(offset=A1).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - pin_h)
        pin = pin.faces("<Z").edges("#Y").fillet(pin_l / 2.1)
        #
        pin2 = cqsup.make_bend_pin_stand_1(pin_w, pin_l, pin_h, ang, dxd, upph)
        pin2 = pin2.translate((0.0 + 1.27, 0.0, A1))
        pin  = pin.union(pin2)
        #
        pin2 = cqsup.make_bend_pin_stand_1(pin_w, pin_l, pin_h, ang, dxd, upph)
        pin2 = pin2.translate((0.0 + 3.81, 0.0, A1))
        pin  = pin.union(pin2)
        #
        pin2 = cqsup.make_bend_pin_stand_1(pin_w, pin_l, pin_h, ang, dxd, upph)
        pin2 = pin2.translate((0.0 + 7.62, 0.0, A1))
        pin  = pin.union(pin2)

        #
        pin1 = cq.Workplane("XY").workplane(offset=A1).moveTo(0.0 + 2.54, 0.0).rect(pin_w, pin_l).extrude(0.0 - pin_h)
        pin1 = pin1.faces("<Z").edges("#Y").fillet(pin_l / 2.1)
        pin  = pin.union(pin1)
        #
        pin1 = cq.Workplane("XY").workplane(offset=A1).moveTo(0.0 + 5.12, 0.0).rect(pin_w, pin_l).extrude(0.0 - pin_h)
        pin1 = pin1.faces("<Z").edges("#Y").fillet(pin_l / 2.1)
        pin = pin.union(pin1)

        return (pin)
    

    def make_top_eSIP_7F(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        smallpad_w = 7.37
        smallpad_l = 9.6
        smallpad_h = 0.48
        #
        large_w = 8.19
        large_l = 10.16
        large_h = 1.53
        #
        metal_w = 5.04
        metal_l = 6.7
        metal_h = 0.1

        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(metal_w, metal_l).extrude(metal_h)
        case = case.translate((0.0 - 6.24, 0.0 - 3.81, A1 + large_h + smallpad_h - (metal_h / 2.0)))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_eSIP_7F(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        smallpad_w = 7.37
        smallpad_l = 9.6
        smallpad_h = 0.48
        #
        large_w = 8.19
        large_l = 10.16
        large_h = 1.53
        
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(large_w, large_l).extrude(large_h)
        case = case.faces("<Z").fillet(large_h / 6.0)
        case1 = cq.Workplane("XY").workplane(offset=large_h).moveTo(0.0, 0.0).rect(smallpad_w, smallpad_l).extrude(smallpad_h)
        case1 = case1.faces(">Z").chamfer(smallpad_h / 3.0)
        case = case.union(case1)
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((large_w / 2.0) - 1.0), ((large_l / 2.0) - 1.0)).circle(0.5, False).extrude(0.1)
        case = case.cut(case1)

        case = case.translate((0.0 - 6.24, 0.0 - 3.81, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_eSIP_7F(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        #
        large_w = 8.19
        large_l = 10.16
        large_h = 1.53
        #
        pin_l = 0.775
        pin_w = 0.345
        pin_h = 5.005
        tth = pin_h
        ang = 10.0
        dxd = 3.0
        
        pL1 = 3.18
        pL2 = 2.1 + 0.2
        
        #
        # Create dummy
        #
        pin = cq.Workplane("XY").workplane(offset=(large_h / 2.0) + pin_w).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - (pL1 + pin_w))
        pin1 = cq.Workplane("XY").workplane(offset=(large_h / 2.0)).moveTo(0.0 - (pL2 / 2.0), 0.0).rect(pL2, pin_l).extrude(pin_w)
        pin = pin.union(pin1)
        pin = pin.faces(">X").edges(">Z").fillet(pin_w / 2.2)
        pin = pin.translate((0.0, 0.0, A1))
        #
        pin1 = cq.Workplane("XY").workplane(offset=(large_h / 2.0) + pin_w).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - (pL1 + pin_w))
        pin2 = cq.Workplane("XY").workplane(offset=(large_h / 2.0)).moveTo(0.0 - (pL2 / 2.0), 0.0).rect(pL2, pin_l).extrude(pin_w)
        pin1 = pin1.union(pin2)
        pin1 = pin1.faces(">X").edges(">Z").fillet(pin_w / 2.2)
        pin1 = pin1.translate((0.0, 0.0 - 2.54, A1))
        pin = pin.union(pin1)
        #
        pin1 = cq.Workplane("XY").workplane(offset=(large_h / 2.0) + pin_w).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - (pL1 + pin_w))
        pin2 = cq.Workplane("XY").workplane(offset=(large_h / 2.0)).moveTo(0.0 - (pL2 / 2.0), 0.0).rect(pL2, pin_l).extrude(pin_w)
        pin1 = pin1.union(pin2)
        pin1 = pin1.faces(">X").edges(">Z").fillet(pin_w / 2.2)
        pin1 = pin1.translate((0.0, 0.0 - 5.08, A1))
        pin = pin.union(pin1)
        #
        #
        #
        pL2 = 2.1 + 2.14 + 0.2
        #
        pin1 = cq.Workplane("XY").workplane(offset=(large_h / 2.0) + pin_w).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - (pL1 + pin_w))
        pin2 = cq.Workplane("XY").workplane(offset=(large_h / 2.0)).moveTo(0.0 - (pL2 / 2.0), 0.0).rect(pL2, pin_l).extrude(pin_w)
        pin1 = pin1.union(pin2)
        pin1 = pin1.faces(">X").edges(">Z").fillet(pin_w / 2.2)
        pin1 = pin1.translate((2.14, 0.0 - 1.27, A1))
        pin = pin.union(pin1)
        #
        pin1 = cq.Workplane("XY").workplane(offset=(large_h / 2.0) + pin_w).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - (pL1 + pin_w))
        pin2 = cq.Workplane("XY").workplane(offset=(large_h / 2.0)).moveTo(0.0 - (pL2 / 2.0), 0.0).rect(pL2, pin_l).extrude(pin_w)
        pin1 = pin1.union(pin2)
        pin1 = pin1.faces(">X").edges(">Z").fillet(pin_w / 2.2)
        pin1 = pin1.translate((2.14, 0.0 - 3.81, A1))
        pin = pin.union(pin1)
        #
        pin1 = cq.Workplane("XY").workplane(offset=(large_h / 2.0) + pin_w).moveTo(0.0, 0.0).rect(pin_w, pin_l).extrude(0.0 - (pL1 + pin_w))
        pin2 = cq.Workplane("XY").workplane(offset=(large_h / 2.0)).moveTo(0.0 - (pL2 / 2.0), 0.0).rect(pL2, pin_l).extrude(pin_w)
        pin1 = pin1.union(pin2)
        pin1 = pin1.faces(">X").edges(">Z").fillet(pin_w / 2.2)
        pin1 = pin1.translate((2.14, 0.0 - 7.62, A1))
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
        pin = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(0.0, 0.0).circle(0.005, False).extrude(0.001)
        
        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


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
        'A1',                   # Body PCB seperation
        'body_top_color_key',   # Top color
        'body_color_key',       # Body colour
        'pin_color_key',        # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'       # Destination directory
    ])



    all_params = {


        'PowerIntegrations_eSIP-7C': Params(
            #
            # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'PowerIntegrations_eSIP-7C',    # modelName
            A1 = 3.2,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'PowerIntegrations_eSIP-7F': Params(
            #
            # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'PowerIntegrations_eSIP-7F',    # modelName
            A1 = 0.1,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),
    }
        
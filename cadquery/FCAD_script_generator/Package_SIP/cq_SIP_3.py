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


class cq_SIP_3():

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

#        case_top = self.make_top_dummy(params)
#        show(case_top)
        
        if modelName == 'SIP4_Sharp_Angled':
            case = self.make_case_SIP4_Sharp_Angled(params)
            show(case)
            pins = self.make_pins_SIP4_Sharp_Angled(params)
            show(pins)

        elif modelName == 'SIP4_Sharp_Straight':
            case = self.make_case_SIP4_Sharp_Straight(params)
            show(case)
            pins = self.make_pins_SIP4_Sharp_Straight(params)
            show(pins)

        elif modelName == 'SIP-3_P1.30mm':
            case = self.make_case_SIP_3_P1_30mm(params)
            show(case)
            pins = self.make_pins_SIP_3_P1_30mm(params)
            show(pins)

        elif modelName == 'SIP-3_P2.90mm':
            case = self.make_case_SIP_3_P2_90mm(params)
            show(case)
            pins = self.make_pins_SIP_3_P2_90mm(params)
            show(pins)

        elif modelName == 'SIP-8':
            case = self.make_case_SIP_8(params)
            show(case)
            pins = self.make_pins_SIP_8(params)
            show(pins)

        elif modelName == 'SIP-9':
            case = self.make_case_SIP_9(params)
            show(case)
            pins = self.make_pins_SIP_9(params)
            show(pins)

        elif modelName == 'SLA704XM':
            case = self.make_case_SLA704XM(params)
            show(case)
            pins = self.make_pins_SLA704XM(params)
            show(pins)

        elif modelName == 'STK672-040-E':
            case = self.make_case_STK672_040_E(params)
            show(case)
            pins = self.make_pins_STK672_040_E(params)
            show(pins)

        elif modelName == 'STK672-080-E':
            case = self.make_case_STK672_080_E(params)
            show(case)
            pins = self.make_pins_STK672_080_E(params)
            show(pins)

            
            
#        npth_pins = self.make_npth_pins_dummy(params)
#        show(npth_pins)
     
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
     
#        body_top_color_key = params.body_top_color_key
        body_color_key = params.body_color_key
        pin_color_key = params.pin_color_key
#        npth_pin_color_key = params.npth_pin_color_key

#        body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()
#        npth_pin_color = shaderColors.named_colors[npth_pin_color_key].getDiffuseFloat()

#        Color_Objects(Gui,objs[0],body_top_color)
        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],pin_color)
#        Color_Objects(Gui,objs[3],npth_pin_color)

#        col_body_top=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
#        col_npth_pin=Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
        
        material_substitutions={
#            col_body_top[:-1]:body_top_color_key,
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pin_color_key,
 #           col_npth_pin[:-1]:npth_pin_color_key
        }
        
        expVRML.say(material_substitutions)
        while len(objs) > 1:
                FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
                del objs
                objs = GetListOfObjects(FreeCAD, doc)

        return material_substitutions


    def make_npth_pins_dummy(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        #
        # Create dummy
        #
        pin = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(0.0, 0.0).circle(0.005, False).extrude(0.001)
        
        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_top_dummy(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        #
        # Create dummy
        #
        case = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(0.0, 0.0).circle(0.005, False).extrude(0.001)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_SIP4_Sharp_Angled(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 24.6
        W = 18.5
        W1 = 16.4
        H =  5.50
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        case = case.faces(">Y").edges(">Z").chamfer(H - 1.1, 0.4)
        case = case.faces(">Y").edges("<Z").chamfer(1.0, 0.2)

        #
        # Cut top
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - ((W / 2.0) - 0.525), ((L / 2.0) - 2.5)).rect(1.05, 5.0).extrude(H + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo((W / 2.0) - 0.525, ((L / 2.0) - 2.5)).rect(1.05, 5.0).extrude(H + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(5.0, 5.0).extrude(H + 2)
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 - 20.0)
        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(6.0, 6.0).extrude(0.0 - 6.0)
        case1 = case1.cut(case2)
        case1 = case1.translate(((W / 2.0) + 0.525, ((L / 2.0)- 2.5), 1.4))
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(5.0, 5.0).extrude(H + 2)
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 + 20.0)
        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(6.0, 6.0).extrude(0.0 - 6.0)
        case1 = case1.cut(case2)
        case1 = case1.translate((0.0 - ((W / 2.0) + 0.525), ((L / 2.0)- 2.5), 1.4))
        case = case.cut(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0, ((L / 2.0) - 3.2)).circle(3.2 / 2.0, False).extrude(H + 0.2)
        case = case.cut(case1)

        case = case.faces(">Z").fillet(0.2)

        case = case.translate((7.62, 16.8, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_SIP4_Sharp_Angled(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.6
        W = 0.8
        H = 11.2
        
        #
        #
        # Create pins
        #
        pin  = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(0.0 - (H - 4.5))
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 2.25).rect(W, 4.5 + L).extrude(L)
        pin = pin.union(pin1)
        pin = pin.faces(">Z").edges("<Y").fillet(L)
        pin = pin.translate((0.0, 0.0, A1 + 1.7))
        #
        pin2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(0.0 - (H - 4.5))
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 2.25).rect(W, 4.5 + L).extrude(L)
        pin2 = pin2.union(pin1)
        pin2 = pin2.faces(">Z").edges("<Y").fillet(L)
        pin2 = pin2.translate((0.0 + 05.08, 0.0, A1 + 1.7))
        pin = pin.union(pin2)
        #
        pin2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(0.0 - (H - 4.5))
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 2.25).rect(W, 4.5 + L).extrude(L)
        pin2 = pin2.union(pin1)
        pin2 = pin2.faces(">Z").edges("<Y").fillet(L)
        pin2 = pin2.translate((0.0 + 12.70, 0.0, A1 + 1.7))
        pin = pin.union(pin2)
        #
        pin2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(0.0 - (H - 4.5))
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 2.25).rect(W, 4.5 + L).extrude(L)
        pin2 = pin2.union(pin1)
        pin2 = pin2.faces(">Z").edges("<Y").fillet(L)
        pin2 = pin2.translate((0.0 + 15.24, 0.0, A1 + 1.7))
        pin = pin.union(pin2)

        
        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_case_SIP4_Sharp_Straight(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 24.6
        W = 18.5
        W1 = 16.4
        H =  5.50
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        case = case.faces(">Y").edges(">Z").chamfer(H - 1.1, 0.4)
        case = case.faces(">Y").edges("<Z").chamfer(1.0, 0.2)

        #
        # Cut top
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - ((W / 2.0) - 0.525), ((L / 2.0) - 2.5)).rect(1.05, 5.0).extrude(H + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo((W / 2.0) - 0.525, ((L / 2.0) - 2.5)).rect(1.05, 5.0).extrude(H + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(5.0, 5.0).extrude(H + 2)
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 - 20.0)
        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(6.0, 6.0).extrude(0.0 - 6.0)
        case1 = case1.cut(case2)
        case1 = case1.translate(((W / 2.0) + 0.525, ((L / 2.0)- 2.5), 1.4))
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(5.0, 5.0).extrude(H + 2)
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 + 20.0)
        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(6.0, 6.0).extrude(0.0 - 6.0)
        case1 = case1.cut(case2)
        case1 = case1.translate((0.0 - ((W / 2.0) + 0.525), ((L / 2.0)- 2.5), 1.4))
        case = case.cut(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0, ((L / 2.0) - 3.2)).circle(3.2 / 2.0, False).extrude(H + 0.2)
        case = case.cut(case1)

        case = case.faces(">Z").fillet(0.2)

        case = case.rotate((0,0,0), (1,0,0), 90.0)
        case = case.translate((7.62, 1.7, A1 + (L / 2.0)))

        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_SIP4_Sharp_Straight(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.6
        W = 0.8
        H = 11.2
        
        #
        #
        # Create pins
        #
        pin  = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(0.0, 0.0).rect(W, L).extrude(0.0 - (H + 0.1))
        pin1  = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(5.08, 0.0).rect(W, L).extrude(0.0 - (H + 0.1))
        pin = pin.union(pin1)
        pin1  = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(12.70, 0.0).rect(W, L).extrude(0.0 - (H + 0.1))
        pin = pin.union(pin1)
        pin1  = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(15.24, 0.0).rect(W, L).extrude(0.0 - (H + 0.1))
        pin = pin.union(pin1)

        
        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_case_SIP_3_P1_30mm(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 1.60
        W = 4.30
        H = 3.20
        S = 0.84
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        case = case.faces("<Y").edges("<X").chamfer(S, S)
        case = case.faces("<Y").edges(">X").chamfer(S, S)

        case = case.translate((1.3, 0.0 - 0.21, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_SIP_3_P1_30mm(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.41
        W = 0.43
        H = 15.00

        #
        #
        # Create pins
        #
        pin  = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(0.0, 0.0).rect(W, L).extrude(0.0 - (H + 0.1))
        pin1  = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(1.3, 0.0).rect(W, L).extrude(0.0 - (H + 0.1))
        pin = pin.union(pin1)
        pin1  = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(2.6, 0.0).rect(W, L).extrude(0.0 - (H + 0.1))
        pin = pin.union(pin1)


        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_case_SIP_3_P2_90mm(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 1.60
        W = 4.30
        H = 3.20
        S = 0.84
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        case = case.faces("<Y").edges("<X").chamfer(S, S)
        case = case.faces("<Y").edges(">X").chamfer(S, S)

        case = case.translate((2.9,  0.0 - 0.21, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_SIP_3_P2_90mm(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        pin_l = 0.41
        pin_w = 0.43
        pin_h = 14.90
        dxd = 1.6

        #
        #
        # Create pins
        #
        ang = 0.0 - 45.00
        pin  = cqsup.make_bend_pin_stand_2(pin_w, pin_l, pin_h, ang, dxd)
        pin = pin.translate((1.6, 0.0, A1))
        #
        pin1 = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(2.9, 0.0).rect(pin_w, pin_l).extrude(0.0 - (pin_h + 0.1))
        pin  = pin.union(pin1)
        #
        ang = 0.0 - 45.00
        pin1 = cqsup.make_bend_pin_stand_2(pin_w, pin_l, pin_h, ang, dxd)
        pin1 = pin1.rotate((0,0,0), (0,0,1), 180.0)
        pin1 = pin1.translate((4.2, 0.0, A1))
        pin  = pin.union(pin1)


        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_case_SIP_8(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 3.0
        W = 19.0
        H = 6.4
        S = L / 2.2
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        
        case = case.faces(">Z").edges("<Y").chamfer(0.4, S)
        case = case.faces(">Z").edges(">Y").chamfer(S, 0.4)
        case = case.faces("<Z").edges("<Y").chamfer(0.4, S)
        case = case.faces("<Z").edges(">Y").chamfer(S, 0.4)
        case = case.faces(">X").edges("<Y").chamfer(0.4, S)
        case = case.faces(">X").edges(">Y").chamfer(S, 0.4)
        case = case.faces("<X").edges("<Y").chamfer(S, 0.4)
        case = case.faces("<X").edges(">Y").chamfer(S, 0.4)

        case1 = cq.Workplane("XZ").workplane(offset=((L / 2.0) + 0.1)).moveTo(0.0 - ((W / 2.0) - 1.5), 1.5).circle(0.5, False).extrude(0.0 - 0.2)
        case = case.cut(case1)

        case = case.translate((8.89,  0.0, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_SIP_9(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 3.0
        W = 21.54
        H = 6.4
        S = L / 2.2
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        
        case = case.faces(">Z").edges("<Y").chamfer(0.4, S)
        case = case.faces(">Z").edges(">Y").chamfer(S, 0.4)
        case = case.faces("<Z").edges("<Y").chamfer(0.4, S)
        case = case.faces("<Z").edges(">Y").chamfer(S, 0.4)
        case = case.faces(">X").edges("<Y").chamfer(0.4, S)
        case = case.faces(">X").edges(">Y").chamfer(S, 0.4)
        case = case.faces("<X").edges("<Y").chamfer(S, 0.4)
        case = case.faces("<X").edges(">Y").chamfer(S, 0.4)

        case1 = cq.Workplane("XZ").workplane(offset=((L / 2.0) + 0.1)).moveTo(0.0 - ((W / 2.0) - 1.5), 1.5).circle(0.5, False).extrude(0.0 - 0.2)
        case = case.cut(case1)

        case = case.translate(((W / 2.0) - (1.27 / 2.0),  0.0, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_SIP_8(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.2
        W = 0.5
        W1 = 1.2
        H = 4.3
        H1 = 1.3

        #
        #
        # Create pins
        #
        dx = 0.0
        pin = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx + (W / 2.0), 0.0).rect((W1 / 2.0), L).extrude(0.0 - H1)
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W, L).extrude(0.0 - H)
        pin1 = pin1.faces("<Z").edges("<X").chamfer(0.75, 0.1)
        pin1 = pin1.faces("<Z").edges(">X").chamfer(0.1, 0.75)
        pin = pin.union(pin1)

        for i in range(0, 6):
            dx = dx + 2.54
            pin2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W1, L).extrude(0.0 - H1)
            pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W, L).extrude(0.0 - H)
            pin1 = pin1.faces("<Z").edges("<X").chamfer(0.75, 0.1)
            pin1 = pin1.faces("<Z").edges(">X").chamfer(0.1, 0.75)
            pin1 = pin1.union(pin2)
            pin = pin.union(pin1)

        dx = dx + 2.54
        pin2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx - (W / 2.0), 0.0).rect((W1 / 2.0), L).extrude(0.0 - H1)
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W, L).extrude(0.0 - H)
        pin1 = pin1.faces("<Z").edges("<X").chamfer(0.75, 0.1)
        pin1 = pin1.faces("<Z").edges(">X").chamfer(0.1, 0.75)
        pin1 = pin1.union(pin2)
        pin = pin.union(pin1)

        pin = pin.translate((0.0,  0.0, A1))

        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_pins_SIP_9(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.2
        W = 0.5
        W1 = 1.2
        H = 4.3
        H1 = 1.3

        #
        #
        # Create pins
        #
        dx = 0.0
        pin = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx + (W / 2.0), 0.0).rect((W1 / 2.0), L).extrude(0.0 - H1)
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W, L).extrude(0.0 - H)
        pin1 = pin1.faces("<Z").edges("<X").chamfer(0.75, 0.1)
        pin1 = pin1.faces("<Z").edges(">X").chamfer(0.1, 0.75)
        pin = pin.union(pin1)

        for i in range(0, 7):
            dx = dx + 2.54
            pin2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W1, L).extrude(0.0 - H1)
            pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W, L).extrude(0.0 - H)
            pin1 = pin1.faces("<Z").edges("<X").chamfer(0.75, 0.1)
            pin1 = pin1.faces("<Z").edges(">X").chamfer(0.1, 0.75)
            pin1 = pin1.union(pin2)
            pin = pin.union(pin1)

        dx = dx + 2.54
        pin2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx - (W / 2.0), 0.0).rect((W1 / 2.0), L).extrude(0.0 - H1)
        pin1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(dx, 0.0).rect(W, L).extrude(0.0 - H)
        pin1 = pin1.faces("<Z").edges("<X").chamfer(0.75, 0.1)
        pin1 = pin1.faces("<Z").edges(">X").chamfer(0.1, 0.75)
        pin1 = pin1.union(pin2)
        pin = pin.union(pin1)

        pin = pin.translate((0.0,  0.0, A1))

        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_case_SLA704XM(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 4.8
        W = 31.0
        H = 16.0
        #
        D1W = 03.3
        D1H = 13.0
        #
        D2W = 27.4
        D1H = 13.0
        #
        D3W = 28.0
        D1H = 13.0
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        
        #
        # Cut left hole
        #
        case1 = cq.Workplane("XZ").workplane(offset=0.0 - (L / 2.0) - 0.1).moveTo(D1W - (W / 2.0), D1H).circle(3.2 / 2.0, False).extrude(2.0 * L)
        case = case.cut(case1)
        #
        # Cut right hole
        #
        case1 = cq.Workplane("XZ").workplane(offset=0.0 - (L / 2.0) - 0.1).moveTo(D2W - (W / 2.0), D1H).circle(3.2 / 2.0, False).extrude(2.0 * L)
        case = case.cut(case1)
        case1 = cq.Workplane("XZ").workplane(offset=0.0 - (L / 2.0) - 0.1).moveTo(D3W - (W / 2.0), D1H).circle(3.2 / 2.0, False).extrude(2.0 * L)
        case = case.cut(case1)
        case1 = cq.Workplane("XZ").workplane(offset=0.0 - (L / 2.0) - 0.1).moveTo(((D3W - D2W) / 2.0) + D2W - (W / 2.0), D1H).rect(0.6, 3.2).extrude(2.0 * L)
        case = case.cut(case1)
        #
        # Create upper left cut out
        #
        case1 = cq.Workplane("XZ").workplane(offset=0.0).moveTo(0.0, 0.0).rect(7.3, 6.1).extrude(L)
        case1 = case1.faces("<Z").edges(">X").fillet(2)
        case1 = case1.translate((3.3 - (W / 2.0),  (L / 2.0) - 1.7 , 13.0))
        case = case.cut(case1)
        #
        # Create upper right cut out
        #
        case1 = cq.Workplane("XZ").workplane(offset=0.0).moveTo(0.0, 0.0).rect(7.3, 6.1).extrude(L)
        case1 = case1.faces("<Z").edges("<X").fillet(2)
        case1 = case1.translate(((W / 2.0)- 3.3,  (L / 2.0) - 1.7 , 13.0))
        case = case.cut(case1)

        case = case.translate((14.28,  L / 2.0, A1))

        case = case.faces("<Y").fillet(0.2)

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_SLA704XM(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.55
        W = 0.65
        H = 9.7
        ang = 45.0
        dxd = 2.0
        upph = 3.7

        #
        # Create pins
        #
        dx = 0.0
        pin = cqsup.make_bend_pin_stand_1(W, L, H, ang, dxd, upph)
        dx = dx + 3.36

        for i in range(0, 8):
            pin1 = cqsup.make_bend_pin_stand_1(W, L, H, ang, dxd, upph)
            pin1 = pin1.translate((dx,  0.0, 0.0))
            pin = pin.union(pin1)
            dx = dx + 3.36

        dx = 1.68
        for i in range(0, 9):
            pin1 = cqsup.make_bend_pin_stand_1(W, L, H, ang, dxd, upph)
            pin1 = pin1.rotate((0,0,0), (0,0,1), 180.0)
            pin1 = pin1.translate((dx,  0.0, 0.0))
            pin = pin.union(pin1)
            dx = dx + 3.36
            
        
        pin = pin.translate((0.0,  2.0, A1))

        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_case_STK672_040_E(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 9.0
        W = 53.0
        H = 22.0
        #
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)

        case = case.faces("<Y").fillet(0.2)
        case = case.faces(">Y").fillet(0.2)
        #
        # Pin 1 mark
        #
        case1 = cq.Workplane("XZ").workplane(offset=(L / 2.0) - 0.2).moveTo(0.0 - ((W / 2.0) - 2.0), 2.0).circle(0.5, False).extrude(0.2)
        case = case.cut(case1)

        case = case.translate((21.0,  0.0 - 1.6, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_STK672_040_E(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.4
        W = 0.5
        H = 5.0
        ang = 10.0
        dxd = 2.0
        upph = 1.0

        #
        # Create pins
        #
        dx = 0.0
        pin = cqsup.make_bend_pin_stand_1(W, L, H, ang, dxd, upph)
        dx = dx + 2.0

        for i in range(0, 21):
            pin1 = cqsup.make_bend_pin_stand_1(W, L, H, ang, dxd, upph)
            pin1 = pin1.translate((dx,  0.0, 0.0))
            pin = pin.union(pin1)
            dx = dx + 2.0
        
        pin = pin.translate((0.0,  2.0, A1 + 0.4))

        if (rotation != 0):
            pin = pin.rotate((0,0,0), (0,0,1), rotation)

        return (pin)


    def make_case_STK672_080_E(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        L = 8.5
        W = 46.6
        H = 25.6
        #
        #
        # Create body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        #
        # cut left side
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(4.0, L + 0.4).extrude(H)
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 - 20.0)
        case1 = case1.translate((0.0 - ((W / 2.0) - 2.0), 0.0, 0.0 - 2.0))
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(4.0, L + 0.4).extrude(H)
        case1 = case1.rotate((0,0,0), (0,1,0), 20.0)
        case1 = case1.translate((0.0 - ((W / 2.0) + 3.0), 0.0, (H / 2.0)))
        case = case.cut(case1)
        #
        # cut right side
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(4.0, L + 0.4).extrude(H)
        case1 = case1.rotate((0,0,0), (0,1,0), 0.0 - 20.0)
        case1 = case1.translate((((W / 2.0) + 3.0), 0.0, (H / 2.0) + 1.0))
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(4.0, L + 0.4).extrude(H)
        case1 = case1.rotate((0,0,0), (0,1,0), 20.0)
        case1 = case1.translate((((W / 2.0) - 2.0), 0.0, 0.0 - 2.0))
        case = case.cut(case1)

#        case = case.faces("<Y").fillet(0.2)
        case = case.faces(">Y").fillet(1.0)
        #
        # Pin 1 mark
        #
        case1 = cq.Workplane("XZ").workplane(offset=(L / 2.0) - 0.2).moveTo(0.0 - ((W / 2.0) - 6.0), 2.0).circle(0.5, False).extrude(0.2)
        case = case.cut(case1)

        #
        # Holes
        #
        case1 = cq.Workplane("XZ").workplane(offset=(L / 2.0) + 0.2).moveTo(0.0 - ((W / 2.0) - 2.7), 12.7).circle(3.6 / 2.0, False).extrude(0.0 - (L + 0.4))
        case = case.cut(case1)
        case1 = cq.Workplane("XZ").workplane(offset=(L / 2.0) + 0.2).moveTo(((W / 2.0) - 2.7), 12.7).circle(3.6 / 2.0, False).extrude(0.0 - (L + 0.4))
        case = case.cut(case1)

        case = case.translate((14.00,  0.0 - 1.6, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins_STK672_080_E(self, params):

        A1 = params.A1                      # Body PCB seperation
        rotation = params.rotation          # Rotation if required

        cqsup = cq_support()
        L = 0.4
        W = 0.5
        H = 5.0
        ang = 10.0
        dxd = 2.0
        upph = 1.0

        #
        # Create pins
        #
        dx = 0.0
        pin = cqsup.make_bend_pin_stand_1(W, L, H, ang, dxd, upph)
        dx = dx + 2.0

        for i in range(0, 14):
            pin1 = cqsup.make_bend_pin_stand_1(W, L, H, ang, dxd, upph)
            pin1 = pin1.translate((dx,  0.0, 0.0))
            pin = pin.union(pin1)
            dx = dx + 2.0
        
        pin = pin.translate((0.0,  2.0, A1 + 0.4))

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

        'SIP4_Sharp_Angled': Params(
            #
            # 
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'SIP4_Sharp-SSR_P7.62mm_Angled',         # modelName
            A1 = 0.1,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'SIP4_Sharp_Straight': Params(
            #
            # 
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'SIP4_Sharp-SSR_P7.62mm_Straight',         # modelName
            A1 = 7.0,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'SIP-3_P1.30mm': Params(
            #
            # https://www.diodes.com/assets/Package-Files/SIP-3-Bulk-Pack.pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'SIP-3_4.30x1.60mm_P1.30mm',    # modelName
            A1 = 13.4,                                  # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'SIP-3_P2.90mm': Params(
            #
            # https://www.diodes.com/assets/Package-Files/SIP-3-Ammo-Pack.pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'SIP-3_4.30x1.60mm_P2.90mm',    # modelName
            A1 = 13.3,                                  # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'SIP-8': Params(
            #
            # http://www.njr.com/semicon/PDF/package/SIP8_E.pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'SIP-8_19x3mm_P2.54mm',         # modelName
            A1 = 1.3,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'SIP-9': Params(
            #
            # http://www.njr.com/semicon/PDF/package/SIP8_E.pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'SIP-9_21.54x3mm_P2.54mm',      # modelName
            A1 = 1.3,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'SLA704XM': Params(
            #
            # http://www.sumzi.com/upload/files/2007/07/2007073114282034189.PDF
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'SLA704XM',                     # modelName
            A1 = 6.7,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'STK672-040-E': Params(
            #
            # https://www.onsemi.com/pub/Collateral/EN5227-D.PDF
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'STK672-040-E',                 # modelName
            A1 = 1.0,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),

        'STK672-080-E': Params(
            #
            # https://www.onsemi.com/pub/Collateral/EN5227-D.PDF
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'STK672-080-E',                 # modelName
            A1 = 1.0,                                   # Body PCB seperation

            body_top_color_key = 'metal grey pins',     # Top color
            body_color_key = 'black body',              # Body color
            pin_color_key = 'metal grey pins',          # Pin color
            npth_pin_color_key = 'grey body',           # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Package_SIP.3dshapes',   # destination directory
            ),
    }
        
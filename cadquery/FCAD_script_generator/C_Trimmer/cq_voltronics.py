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


import cq_common  # modules parameters
from cq_common import *

import sys
import math


class cq_voltronics():

    def __init__(self):
        x = 0

        
    def get_model_name(self, modelID):
        for n in self.all_params:
            if n == modelID:
                return self.all_params[modelID].modelName
        return 'xxUNKNOWNxxx'

        
    def get_dest_3D_dir(self, modelID):
        for n in self.all_params:
            if n == modelID:
                return self.all_params[modelID].dest_dir_prefix
        return 'Capacitor_SMD.3dshapes'

    def model_exist(self, modelID):
        for n in self.all_params:
            if n == modelID:
                return True
                
        return False
        
        
    def get_list_all(self):
        list = []
        for n in self.all_params:
            list.append(n)
        
        return list

        
    def make_3D_model(self, modelID):
        
        destination_dir = self.get_dest_3D_dir(modelID)
        params = self.all_params[modelID]

        
        if modelID == 'Voltronics_JN':
            case_top = self.make_top_Voltronics_JN(params)
            show(case_top)
            case = self.make_case_Voltronics_JN_JQ(params)
            show(case)
            pins = self.make_pin_Voltronics_JN_JQ(params)
            show(pins)
        elif modelID == 'Voltronics_JQ':
            case_top = self.make_top_Voltronics_JQ(params)
            show(case_top)
            case = self.make_case_Voltronics_JN_JQ(params)
            show(case)
            pins = self.make_pin_Voltronics_JN_JQ(params)
            show(pins)
        elif modelID == 'Voltronics_JR':
            case_top = self.make_top_Voltronics_JR(params)
            show(case_top)
            case = self.make_case_Voltronics_JR(params)
            show(case)
            pins = self.make_pin_Voltronics_JR(params)
            show(pins)
        elif modelID == 'Voltronics_JV':
            case_top = self.make_top_Voltronics_JV(params)
            show(case_top)
            case = self.make_case_Voltronics_JV(params)
            show(case)
            pins = self.make_pin_Voltronics_JV(params)
            show(pins)
        elif modelID == 'Voltronics_JZ':
            case_top = self.make_top_Voltronics_JZ(params)
            show(case_top)
            case = self.make_case_Voltronics_JZ(params)
            show(case)
            pins = self.make_pin_Voltronics_JZ(params)
            show(pins)
        else:
            FreeCAD.Console.PrintMessage('\r\n')
            FreeCAD.Console.PrintMessage('ERROR: Model ID ' + str(modelID) + ' does not exist, exiting')
            FreeCAD.Console.PrintMessage('\r\n')
            sys.exit()
            
            
        npth_pins = self.make_npth_pins_dummy(params)
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


    def make_npth_pins_dummy(self, params):

        A1 = params.A1                      # package height
        rotation = params.rotation          # Rotation if required

        # Dummy
        case = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(0.0, 0.0).circle(0.01, False).extrude(0.01)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_top_Voltronics_JN_JQ(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required
    
        tw = (L - L1) / 2.0
        #
        pts = []
        pts.append((0.0, L1))
        pts.append((0.0 - 0.2, L1))
        pts.append((0.0 - (tw), L1 + tw))
        pts.append((0.0 - (W - (2.0 * tw)), L1 + tw))
        pts.append((0.0 - (W - tw), L1 + tw))
        pts.append((0.0 - (W - 0.1), L1))
        pts.append((0.0 - (W - 0.1), 0.0))
        pts.append((0.0 - (W - tw), 0.0 - tw))
        pts.append((0.0 - (tw), 0.0 - tw))
        pts.append((0.0 - 0.2, 0.0))

        case = cq.Workplane("XY").workplane(offset=0.0).polyline(pts).close().extrude(BH)
        case = case.faces(">Z").fillet(0.05)
        case = case.translate(((W / 2.0), 0.0 - (L1 / 2.0), 0.0))
        
        case1 = cq.Workplane("XY").workplane(offset=BH).moveTo(0.0, 0.0).circle(D / 2.0, False).extrude(H - BH)
        case2 = cq.Workplane("XY").workplane(offset=BH).moveTo(0.0, 0.0).circle((D / 2.0) - ((H - BH) + 0.1), False).extrude(H)
        case1 = case1.cut(case2)
        case1 = case1.faces(">Z").fillet((H - BH) * 0.6)
        case = case.union(case1)

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - 0.1, 0.0).rect(W, L - 0.2).extrude(BH - 0.1)
        case = case.cut(case1)

        return case

    def make_top_Voltronics_JN(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make top
        #
        case = self.make_top_Voltronics_JN_JQ(params)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(SD, SD).extrude(2.0 * H)
        case = case.cut(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)

    def make_top_Voltronics_JQ(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make top
        #
        case = self.make_top_Voltronics_JN_JQ(params)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(SD / 2.0, False).extrude(2.0 * H)
        case = case.cut(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)


    def make_top_Voltronics_JR(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        W2 = params.W2              # Width 2
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        tx = 0.15
        #
        # Make screw
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(SD / 2.0, False).extrude(BH + 0.3)
        case1 = cq.Workplane("XY").workplane(offset=BH + 0.2).moveTo(0.0, 0.0).rect(2.0 * SD, 0.45).extrude(H)
        case = case.cut(case1)
    
        case = case.translate((0.0 - tx, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)


    def make_top_Voltronics_JV(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make top
        #
        case = self.make_top_Voltronics_JN_JQ(params)

        case1 = cq.Workplane("XY").workplane(offset=BH).moveTo((W / 2.0) - 0.15, 0.0).rect(0.3, L1).extrude(H - BH)
        case1 = case1.faces(">Z").fillet(0.14)
        case = case.union(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(SD, SD * 2.0).extrude(2.0 * H)
        case = case.cut(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)


    def make_top_Voltronics_JZ(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        tx = 0.0
        #
        # Make screw
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(SD / 2.0, False).extrude(BH + 0.3)
        case1 = cq.Workplane("XY").workplane(offset=BH + 0.2).moveTo(0.0, 0.0).rect(2.0 * SD, 0.45).extrude(H)
        case = case.cut(case1)
    
        case = case.translate((0.0 - tx, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)


    def make_case_Voltronics_JN_JQ(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        PW = params.PW              # Pad width
        PL = params.PL              # Pad length
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - 0.05, 0.0).rect(W - 0.3, L - 0.2).extrude(BH - 0.1)
        case = case.faces(">Z").fillet(0.05)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_Voltronics_JR(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        W2 = params.W2              # Width 2
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        wx = W - W2
        tx = 0.15
        pts = []
        pts.append((0.0, L))
        pts.append((0.0 - (wx - W1), L))
        pts.append((0.0 - (wx - 0.0), L - W1))
        pts.append((0.0 - (wx - 0.0), W1))
        pts.append((0.0 - (wx - W1), 0.0))

        case = cq.Workplane("XY").workplane(offset=0.0).polyline(pts).close().extrude(BH)
        case = case.faces(">Z").fillet(0.05)
        case = case.translate(((W / 2.0) - W2, 0.0 - (L / 2.0), 0.0))
        
        #
        # Add circle ontop
        #
        case1 = cq.Workplane("XY").workplane(offset=BH).moveTo(0.0 - tx, 0.0).circle(((D / 2.0) - 0.1), False).extrude(H - BH)
        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - tx, 0.0).circle(((D / 2.0) - 0.1) - ((H - BH) / 2.0), False).extrude(H + 0.2)
        case1 = case1.cut(case2)
        case1 = case1.faces(">Z").fillet((H - BH) * 0.2)
        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)


    def make_case_Voltronics_JV(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        PW = params.PW              # Pad width
        PL = params.PL              # Pad length
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - 0.05, 0.0).rect(W - 0.3, L - 0.2).extrude(BH - 0.1)
        case = case.faces(">Z").fillet(0.05)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_Voltronics_JZ(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        tx = 0.0
        #
        pts = []
        # Right side
        pts.append((0.0, (L / 2.0) - (L1 / 2.0)))
        pts.append((0.0 - (L1 / 2.0), (L / 2.0) - (L1 / 2.0)))
        pts.append((0.0 - (L1 / 2.0), (L / 2.0) + (L1 / 2.0)))
        pts.append((0.0, (L / 2.0) + (L1 / 2.0)))
        pts.append((0.0, L))
        # Top side
        pts.append((0.0 - (W - W1), L))
        # Left side
        pts.append((0.0 - (W - 0.0), L - W1))
        pts.append((0.0 - (W - 0.0), (L / 2.0) + (L1 / 2.0)))
        pts.append((0.0 - (W - W1 ), (L / 2.0) + (L1 / 2.0)))
        pts.append((0.0 - (W - W1 ), (L / 2.0) - (L1 / 2.0)))
        pts.append((0.0 - (W - 0.0), (L / 2.0) - (L1 / 2.0)))
        pts.append((0.0 - (W - 0.0), W1))
        pts.append((0.0 - (W - W1), 0.0))
        #
        case = cq.Workplane("XY").workplane(offset=0.0).polyline(pts).close().extrude(BH)
        case = case.faces(">Z").fillet(0.05)
        case = case.translate(((W / 2.0), 0.0 - (L / 2.0), 0.0))
        
        #
        # Add circle ontop
        #
        case1 = cq.Workplane("XY").workplane(offset=BH ).moveTo(0.0, 0.0).circle(((D / 2.0) - 0.1), False).extrude(H - BH)
        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(((D / 2.0) - 0.1) - ((H - BH) / 2.0), False).extrude(H + 0.2)
        case1 = case1.cut(case2)
        case1 = case1.faces(">Z").fillet((H - BH) * 0.2)
        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)


    def make_pin_Voltronics_JN_JQ(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        PW = params.PW              # Pad width
        PL = params.PL              # Pad length
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        A1 = params.A1                      # package height
        rotation = params.rotation          # Rotation if required

        #
        # Make pin
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.1, L - 0.1).extrude(BH - 0.1)
        case = case.translate(((W / 2.0) - 0.15, 0.0, 0.0))

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.1, L - 0.2).extrude(BH - 0.1)
        case1 = case1.translate((0.0 - ((W / 2.0) - 0.05), 0.0, 0.0))
        
        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pin_Voltronics_JV(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        PW = params.PW              # Pad width
        PL = params.PL              # Pad length
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        A1 = params.A1                      # package height
        rotation = params.rotation          # Rotation if required

        #
        # Make pin
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.1, L - 0.1).extrude(BH - 0.1)
        case = case.translate(((W / 2.0) - 0.15, 0.0, 0.0))

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.1, L - 0.2).extrude(BH - 0.1)
        case1 = case1.translate((0.0 - ((W / 2.0) - 0.05), 0.0, 0.0))
        
        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pin_Voltronics_JR(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        W2 = params.W2              # Width 2
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        PW = params.PW              # Pad width
        PL = params.PL              # Pad length
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        tx = 0.15
        #
        # Make pin
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L1).extrude(BH - 0.2)
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - tx, 0.0).circle((L / 2.5), False).extrude(BH + 0.1)
        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pin_Voltronics_JZ(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        PW = params.PW              # Pad width
        PL = params.PL              # Pad length
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make pin
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L1).extrude(BH - 0.2)
        
        case = case.translate((0.0, 0.0, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

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
        'modelName',		    # modelName
        'A1',				    # Body PCB seperation
        'W',				    # Width
        'W1',                   # Width 1
        'W2',                   # Width 2
        'L',				    # Length
        'L1',                   # Length 1
        'H',				    # Height
        'BH',				    # Body height
        'D',				    # Dome diameter
        'SD',				    # Screw size
        'PW',				    # Pad width
        'PL',				    # Pad length
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {


        'Voltronics_JN': Params(
            #
            # http://www.knowlescapacitors.com/getmedia/76b68d57-f62f-4666-a976-d23a42593c78/9341_Voltronics-2014_Final-Proof.aspx
            # 
            modelName = 'C_Trimmer_Voltronics_JN',   # modelName
            W = 01.70,                  # Width
            L = 01.50,                  # Length
            L1 = 01.00,                 # Length 1
            H = 00.90,                  # Height
            BH = 00.80,                 # Body height
            D = 01.50,                  # Dome diameter
            SD = 00.80,                 # Screw size
            A1 = 0.01,                  # Body-board separation

            body_top_color_key  = 'gold pins',          # Top color
            body_color_key      = 'black body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Voltronics_JQ': Params(
            #
            # http://www.knowlescapacitors.com/getmedia/76b68d57-f62f-4666-a976-d23a42593c78/9341_Voltronics-2014_Final-Proof.aspx
            # 
            modelName = 'C_Trimmer_Voltronics_JQ',   # modelName
            W = 02.70,                  # Width
            L = 02.20,                  # Length
            L1 = 01.00,                 # Length 1
            H = 01.00,                  # Height
            BH = 00.80,                 # Body height
            D = 02.20,                  # Dome diameter
            SD = 00.20,                 # Screw size
            A1 = 0.01,                  # Body-board separation

            body_top_color_key  = 'metal aluminum',     # Top color
            body_color_key      = 'black body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Voltronics_JR': Params(
            #
            # http://www.knowlescapacitors.com/getmedia/76b68d57-f62f-4666-a976-d23a42593c78/9341_Voltronics-2014_Final-Proof.aspx
            # 
            modelName = 'C_Trimmer_Voltronics_JR',   # modelName
            W = 03.50,                  # Width
            W1 = 00.70,                 # Width 1
            W2 = 00.40,                 # Width 2
            L = 03.10,                  # Length
            L1 = 01.60,                 # Length 1
            H = 01.15,                  # Height
            BH = 00.50,                 # Body height
            D = 03.10,                  # Dome diameter
            SD = 01.50,                 # Screw size
            A1 = 0.01,                  # Body-board separation

            body_top_color_key  = 'gold pins',          # Top color
            body_color_key      = 'white body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Voltronics_JV': Params(
            #
            # http://www.knowlescapacitors.com/getmedia/76b68d57-f62f-4666-a976-d23a42593c78/9341_Voltronics-2014_Final-Proof.aspx
            # 
            modelName = 'C_Trimmer_Voltronics_JV',   # modelName
            W = 03.20,                  # Width
            L = 02.50,                  # Length
            L1 = 01.00,                 # Length 1
            H = 01.25,                  # Height
            BH = 00.80,                 # Body height
            D = 02.40,                  # Dome diameter
            SD = 00.45,                 # Screw size
            A1 = 0.01,                  # Body-board separation

            body_top_color_key  = 'gold pins',          # Top color
            body_color_key      = 'black body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),
            
        'Voltronics_JZ': Params(
            #
            # http://www.knowlescapacitors.com/getmedia/76b68d57-f62f-4666-a976-d23a42593c78/9341_Voltronics-2014_Final-Proof.aspx
            # 
            modelName = 'C_Trimmer_Voltronics_JZ',   # modelName
            W = 04.50,                  # Width
            W1 = 00.50,                 # Width 1
            L = 03.20,                  # Length
            L1 = 01.00,                 # Length 1
            H = 01.50,                  # Height
            BH = 00.80,                 # Body height
            D = 03.10,                  # Dome diameter
            SD = 01.80,                 # Screw size
            A1 = 0.01,                  # Body-board separation

            body_top_color_key  = 'gold pins',          # Top color
            body_color_key      = 'white body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),
    }

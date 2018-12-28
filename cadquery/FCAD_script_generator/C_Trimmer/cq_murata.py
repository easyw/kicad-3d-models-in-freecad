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


class cq_murata():

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

        
        if modelID == 'Murata_TZB4_A':
            case_top = self.make_top_Murata_TZB4_A(params)
            show(case_top)
            case = self.make_case_Murata_TZB4_A(params)
            show(case)
            pins = self.make_pin_Murata_TZB4_A(params)
            show(pins)
        elif modelID == 'Murata_TZB4_B':
            case_top = self.make_top_Murata_TZB4_B(params)
            show(case_top)
            case = self.make_case_Murata_TZB4_B(params)
            show(case)
            pins = self.make_pin_Murata_TZB4_B(params)
            show(pins)
        elif modelID == 'Murata_TZC3':
            case_top = self.make_top_Murata_TZC3(params)
            show(case_top)
            case = self.make_case_Murata_TZC3(params)
            show(case)
            pins = self.make_pin_Murata_TZC3(params)
            show(pins)
        elif modelID == 'Murata_TZR1':
            case_top = self.make_top_Murata_TZR1(params)
            show(case_top)
            case = self.make_case_Murata_TZR1(params)
            show(case)
            pins = self.make_pin_Murata_TZR1(params)
            show(pins)
        elif modelID == 'Murata_TZW4':
            case_top = self.make_top_Murata_TZW4(params)
            show(case_top)
            case = self.make_case_Murata_TZW4(params)
            show(case)
            pins = self.make_pin_Murata_TZW4(params)
            show(pins)
        elif modelID == 'Murata_TZY2':
            case_top = self.make_top_Murata_TZY2(params)
            show(case_top)
            case = self.make_case_Murata_TZY2(params)
            show(case)
            pins = self.make_pin_Murata_TZY2(params)
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
        case = cq.Workplane("XY").workplane(offset=A1 + 0.2).moveTo(0.0, 0.0).circle(0.01, False).extrude(0.01)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_top_Murata_TZB4_A(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required


        case = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).circle(D / 2.0, False).extrude(0.0 - 0.8)
        case1 = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).circle(SD / 2.0, False).extrude(0.0 - 0.4)
        case = case.cut(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).rect(2.0 * SD, 0.6).extrude(0.0 - 0.4)
        case = case.cut(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).rect(0.6, 2.0 * SD).extrude(0.0 - 0.4)
        case = case.cut(case1)

        case = case.translate((0.0, 0.0, A1 + 0.1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_top_Murata_TZB4_B(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required


        case = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).circle(D / 2.0, False).extrude(0.0 - 0.8)
        case1 = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).circle(SD / 2.0, False).extrude(0.0 - 0.4)
        case = case.cut(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).rect(2.0 * SD, 0.6).extrude(0.0 - 0.4)
        case = case.cut(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=H - 0.2).moveTo(0.0, 0.0).rect(0.6, 2.0 * SD).extrude(0.0 - 0.4)
        case = case.cut(case1)

        case = case.translate((0.0, 0.0, A1 + 0.1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_top_Murata_TZC3(self, params):

        W = params.W                # Width
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required


        case = cq.Workplane("XY").workplane(offset=BH).moveTo(0.0, 0.0).circle((D / 2.0) - 0.1, False).extrude(0.1)

        case1 = cq.Workplane("XY").workplane(offset=BH).moveTo(0.0, 0.0).circle((SD / 2.0) - 0.1, False).extrude(H - BH)
        case = case.union(case1)

        case1 = cq.Workplane("XY").workplane(offset=H + 0.1).moveTo(0.0, 0.0).rect(SD - 0.2, 0.3).extrude(0.0 - 0.3)
        case = case.cut(case1)

        case1 = cq.Workplane("XY").workplane(offset=H + 0.1).moveTo(0.0, 0.0).rect(0.3, SD - 0.2).extrude(0.0 - 0.3)
        case = case.cut(case1)
        
        case = case.faces(">Z").fillet(0.1)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_top_Murata_TZR1(self, params):

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

        case1 = cq.Workplane("XY").workplane(offset=BH + 0.5).moveTo(0.0, 0.0).rect(0.2, SD).extrude(0.0 - 0.8)
        case = case.cut(case1)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_top_Murata_TZW4(self, params):

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
        pts.append((0.0 - (W - (2.0 * tw)), L1 + tw))
        pts.append((0.0 - (W - tw), L1 + tw))
        pts.append((0.0 - (W), L1))
        pts.append((0.0 - (W), 0.0))
        pts.append((0.0 - (W - tw), 0.0 - tw))
        pts.append((0.0 - tw, 0.0 - tw))

        case = cq.Workplane("XY").workplane(offset=0.0).polyline(pts).close().extrude(BH)
        case = case.faces(">Z").fillet(0.05)
        case = case.translate(((W / 2.0), 0.0 - (L1 / 2.0), 0.0))
                
        #
        # Top circle
        #
        case1 = cq.Workplane("XY").workplane(offset=BH).moveTo(0.0, 0.0).circle(D / 2.0, False).extrude(H - BH)
        case2 = cq.Workplane("XY").workplane(offset=BH).moveTo(0.0, 0.0).circle((D / 2.0) - ((H - BH) + 0.1), False).extrude(H)
        case1 = case1.cut(case2)
        case1 = case1.faces(">Z").fillet((H - BH) * 0.4)
        case = case.union(case1)

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L - 0.2).extrude(BH - 0.1)
        case = case.cut(case1)

        case1 = cq.Workplane("XY").workplane(offset=BH + 0.5).moveTo(0.0, 0.0).rect(0.2, SD).extrude(0.0 - 0.8)
        case = case.cut(case1)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_top_Murata_TZY2(self, params):

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
        case1 = case1.faces(">Z").fillet((H - BH) * 0.4)
        case = case.union(case1)

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - 0.1, 0.0).rect(W, L - 0.2).extrude(BH - 0.1)
        case = case.cut(case1)

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(SD, SD * 2.0).extrude(2.0 * H)
        case = case.cut(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
            
        return (case)


    def make_case_Murata_TZB4_A(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W1, L).extrude(H)

        case1 = cq.Workplane("XY").workplane(offset=H + 0.2).moveTo(0.0, 0.0).circle(D / 2.0, False).extrude(0.0 - 0.8)
        case = case.cut(case1)

        case = case.faces(">Z").fillet(0.2)
        case = case.faces("<X").edges(">Y").fillet(0.1)
        case = case.faces("<X").edges("<Y").fillet(0.1)
        case = case.faces(">X").edges(">Y").fillet(0.1)
        case = case.faces(">X").edges("<Y").fillet(0.1)
    
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(W1 / 4.0, 0.0).rect(0.4, L + 0.4).extrude(0.4)
        case = case.cut(case1)

        case = case.translate((0.0, 0.0, A1 + 0.1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_case_Murata_TZB4_B(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W1, L).extrude(H)

        case1 = cq.Workplane("XY").workplane(offset=H + 0.2).moveTo(0.0, 0.0).circle(D / 2.0, False).extrude(0.0 - 0.8)
        case = case.cut(case1)

        case = case.faces(">Z").fillet(0.2)
        case = case.faces("<X").edges(">Y").fillet(0.1)
        case = case.faces("<X").edges("<Y").fillet(0.1)
        case = case.faces(">X").edges(">Y").fillet(0.1)
        case = case.faces(">X").edges("<Y").fillet(0.1)

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(W1 / 4.0, 0.0).rect(0.4, L + 0.4).extrude(0.4)
        case = case.cut(case1)

        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(1.0, 1.2).extrude(1.0)
        case1 = case1.translate(((W1 / 2.0) - 0.5, 0.0, 0.0))
        case = case.cut(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(1.0, 1.2).extrude(1.0)
        case1 = case1.translate((0.0 - ((W1 / 2.0) - 0.5), 0.0, 0.0))
        case = case.cut(case1)
        

        case = case.translate((0.0, 0.0, A1 + 0.1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_case_Murata_TZC3(self, params):

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

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_case_Murata_TZR1(self, params):

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
        # Make body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - 0.05, 0.0).rect(W - 0.3, L - 0.2).extrude(BH - 0.1)
        case = case.faces(">Z").fillet(0.05)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_Murata_TZW4(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W - 0.2, L - 0.2).extrude(BH - 0.1)
        case = case.faces(">Z").fillet(0.05)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case_Murata_TZY2(self, params):

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


    def make_pin_Murata_TZB4_A(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(1.0, 1.2).extrude(1.0)
        case = case.translate(((W / 2.0) - 0.5, 0.0, 0.0))

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(1.0, 1.2).extrude(1.0)
        case1 = case1.translate((0.0 - ((W / 2.0) - 0.5), 0.0, 0.0))

        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_pin_Murata_TZB4_B(self, params):

        W = params.W                # Width
        W1 = params.W1              # Width 1
        L = params.L                # Length
        L1 = params.L1              # Length 1
        H = params.H                # Height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        cqph = cq_parameters_help()
        
        tx = ((W - W1) / 3.0)

        cqph.pin_length = 2.0 * tx
        cqph.pin_width = 1.0
        
        case = cqph._make_gullwing_pin(1.0, tx)
        case = case.rotate((0,0,0), (0,0,1), 0.0 - 90.0)
        case = case.translate((0.0 - ((W1 / 2.0) - (tx + cqph.pin_length) - (cqph.pin_thickness * 2.0) - ((W - W1) / 2.0)), 0.0, 0.0))

        case1 = cqph._make_gullwing_pin(1.0, tx)
        case1 = case1.rotate((0,0,0), (0,0,1), 90.0)
        case1 = case1.translate(((W1 / 2.0) - (tx + cqph.pin_length) - (cqph.pin_thickness * 2.0) - ((W - W1) / 2.0), 0.0, 0.0))

        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_pin_Murata_TZC3(self, params):

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


        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.05, 0.0).rect(W - 0.1, L1 * 0.8).extrude(BH - 0.2)
        
        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_pin_Murata_TZR1(self, params):

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


    def make_pin_Murata_TZW4(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BH = params.BH              # Body height
        D = params.D                # Dome diameter
        SD = params.SD              # Screw diameter
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        #
        # Make pin
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.1, L - 0.2).extrude(BH - 0.1)
        case = case.translate(((W / 2.0) - 0.05, 0.0, 0.0))

        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.1, L - 0.2).extrude(BH - 0.1)
        case1 = case1.translate((0.0 - ((W / 2.0) - 0.05), 0.0, 0.0))
        
        case = case.union(case1)
        
        case = case.translate((0.0, 0.0, A1))
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pin_Murata_TZY2(self, params):

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


        'Murata_TZB4_A': Params(
            #
            # https://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/trimmer/t13e.ashx?la=en-gb
            # 
            modelName = 'C_Trimmer_Murata_TZB4-A',      # modelName
            W = 05.00,                                  # Width
            W1 = 04.50,                                 # Width 1
            L = 04.00,                                  # Length
            H = 03.00,                                  # Height
            D = 03.00,                                  # Dome diameter
            SD = 01.40,                                 # Screw size
            A1 = 0.01,                                  # Body-board separation

            body_top_color_key  = 'metal aluminum',     # Top color
            body_color_key      = 'brown body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Murata_TZB4_B': Params(
            #
            # https://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/trimmer/t13e.ashx?la=en-gb
            # 
            modelName = 'C_Trimmer_Murata_TZB4-B',      # modelName
            W = 07.00,                                  # Width
            W1 = 04.50,                                 # Width 1
            L = 04.00,                                  # Length
            H = 03.00,                                  # Height
            D = 03.00,                                  # Dome diameter
            SD = 01.40,                                 # Screw size
            A1 = 0.01,                                  # Body-board separation

            body_top_color_key  = 'metal aluminum',     # Top color
            body_color_key      = 'brown body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Murata_TZC3': Params(
            #
            # https://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/trimmer/t13e.ashx?la=en-gb
            # 
            modelName = 'C_Trimmer_Murata_TZC3',        # modelName
            W = 04.50,                                  # Width
            W1 = 00.50,                                 # Width 1
            L = 03.20,                                  # Length
            L1 = 01.00,                                 # Length 1
            H = 01.60,                                  # Height
            BH = 00.80,                                 # Body height
            D = 03.20,                                  # Dome diameter
            SD = 02.50,                                 # Screw size
            A1 = 0.01,                                  # Body-board separation

            body_top_color_key  = 'white body',         # Top color
            body_color_key      = 'black body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Murata_TZR1': Params(
            #
            # https://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/trimmer/t13e.ashx?la=en-gb
            # 
            modelName = 'C_Trimmer_Murata_TZR1',        # modelName
            W = 01.70,                                  # Width
            L = 01.50,                                  # Length
            L1 = 00.70,                                 # Length 1
            H = 00.90,                                  # Height
            BH = 00.60,                                 # Body height
            D = 01.40,                                  # Dome diameter
            SD = 00.45,                                 # Screw size
            A1 = 0.01,                                  # Body-board separation

            body_top_color_key  = 'gold pins',          # Top color
            body_color_key      = 'black body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Murata_TZW4': Params(
            #
            # https://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/trimmer/t13e.ashx?la=en-gb
            # 
            modelName = 'C_Trimmer_Murata_TZW4',        # modelName
            W = 05.20,                                  # Width
            L = 04.20,                                  # Length
            L1 = 01.00,                                 # Length 1
            H = 02.60,                                  # Height
            BH = 01.60,                                 # Body height
            D = 04.10,                                  # Dome diameter
            SD = 01.60,                                 # Screw size
            A1 = 0.01,                                  # Body-board separation

            body_top_color_key  = 'metal aluminum',     # Top color
            body_color_key      = 'white body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

        'Murata_TZY2': Params(
            #
            # https://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/trimmer/t13e.ashx?la=en-gb
            # 
            modelName = 'C_Trimmer_Murata_TZY2',        # modelName
            W = 03.20,                                  # Width
            L = 02.50,                                  # Length
            L1 = 01.00,                                 # Length 1
            H = 01.25,                                  # Height
            BH = 00.75,                                 # Body height
            D = 02.40,                                  # Dome diameter
            SD = 00.45,                                 # Screw size
            A1 = 0.01,                                  # Body-board separation

            body_top_color_key  = 'gold pins',     # Top color
            body_color_key      = 'black body',         # Body color
            pin_color_key       = 'metal grey pins',    # Pin color
            npth_pin_color_key  = 'grey body',          # NPTH Pin color
            rotation = 0,                               # Rotation if required
            dest_dir_prefix = 'Capacitor_SMD.3dshapes', # destination directory
            ),

    }

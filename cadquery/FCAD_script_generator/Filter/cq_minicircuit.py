# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
# This is a
#
## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module
#
## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8
#
## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script
#
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

#
# Most of these models are based on 
# http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
#

import cq_common  # modules parameters
from cq_common import *

import sys
import math


class cq_minicircuit():

    def __init__(self):
        self.body_top_color_key  = 'brown body'         # Top color
        self.body_color_key      = 'black body'         # Body color
        self.pin_color_key       = 'metal grey pins'    # Pin color
        self.npth_pin_color_key  = 'black body'         # NPTH Pin color

    def set_colors(self, modelID):
    
        params = self.all_params[modelID]
    
        if params.body_top_color_key != None:
            self.body_top_color_key = params.body_top_color_key
        #
        if params.body_color_key != None:
            self.body_color_key = params.body_color_key
        #
        if params.pin_color_key != None:
            self.pin_color_key = params.pin_color_key
        #
        if params.npth_pin_color_key != None:
            self.npth_pin_color_key = params.npth_pin_color_key
        #


    def get_model_name(self, modelID):
        for n in self.all_params:
            if n == modelID:
                return self.all_params[modelID].modelName
        return 'xxUNKNOWNxxx'


    def get_dest_3D_dir(self, modelID):
        for n in self.all_params:
            if n == modelID:
                if self.all_params[modelID].dest_dir_prefix != None:
                    return self.all_params[modelID].dest_dir_prefix

        return 'Filter.3dshapes'


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


    def set_rotation(self, modelID):

        params = self.all_params[modelID]
        
        self.rotatex = 0.0          # Rotation around x-axis if required
        self.rotatey = 0.0          # Rotation around x-axis if required

        if params.serie == 'FV1206-1':
            self.rotatez = 270.0          # Rotation around x-axis if required
        else:
            self.rotatez = 0.0          # Rotation around x-axis if required


    def set_translate(self, modelID):

        ttdx = 0.0
        ttdy = 0.0
        ttdz = 0.0
        
        self.translate = (ttdx, ttdy, ttdz)


    def make_3D_model(self, modelID):

        destination_dir = self.get_dest_3D_dir(modelID)
        params = self.all_params[modelID]

        FreeCAD.Console.PrintMessage('\r\n')
        FreeCAD.Console.PrintMessage('make_3D_model 1 \r\n')
        self.set_colors(modelID)
        self.set_translate(modelID)
        self.set_rotation(modelID)
        FreeCAD.Console.PrintMessage('make_3D_model 2 \r\n')
        case_top = self.make_top(modelID)
        show(case_top)
        FreeCAD.Console.PrintMessage('make_3D_model 3 \r\n')
        case = self.make_body(modelID)
        show(case)

        FreeCAD.Console.PrintMessage('make_3D_model 4 \r\n')
        pins = self.make_pin(modelID)
        show(pins)

        FreeCAD.Console.PrintMessage('make_3D_model 5 \r\n')
        npth_pins = self.make_npth_pin(modelID)
        show(npth_pins)

        FreeCAD.Console.PrintMessage('make_3D_model 6 \r\n')
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)

        body_top_color_key = self.body_top_color_key
        body_color_key = self.body_color_key
        pin_color_key = self.pin_color_key
        npth_pin_color_key = self.npth_pin_color_key

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


    def make_top(self, modelID):

        params = self.all_params[modelID]
        A = params.A                # Width
        B = params.B                # Length
        C = params.C                # Height
        D = params.D                # Pad 1 width
        E = params.E                # Pad 2 width
        F = params.F                # Pad 2 length
        G = params.G                # Pitch
        L = params.L                # Pad 3 width
        Q = params.Q                # Pad 3 lenght
        serie = params.serie        # Serie


        #
        # Pin 1 marker 
        #
        if serie == 'FV1206-1' or serie == 'FV1206-6':
            case = cq.Workplane("XY").workplane(offset=C - 0.1).moveTo(0.0 - (((A / 2.0) - D) - 0.3), 0.0).rect(0.6, 0.4).extrude(0.1)
        elif serie == 'FV1206-7':
            case = cq.Workplane("XY").workplane(offset=C - 0.1).moveTo(0.0 - ((A / 2.0) - 1.0), 0.0).rect(0.6, 0.4).extrude(0.1)
        else:
            case = cq.Workplane("XY").workplane(offset=C - 0.1).moveTo(0.0 - (((A / 2.0) - D) - 0.1), 0.0).rect(0.6, 0.4).extrude(0.1)
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)
        if self.rotatey > 0.0:
            case = case.rotate((0,0,0), (0,1,0), self.rotatey)
        if self.rotatez > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatez)

        case = case.translate(self.translate)

        return (case)



    def make_body(self, modelID):

        params = self.all_params[modelID]
        A = params.A                # Width
        B = params.B                # Length
        C = params.C                # Height
        D = params.D                # Pad 1 width
        E = params.E                # Pad 2 width
        F = params.F                # Pad 2 length
        G = params.G                # Pitch
        L = params.L                # Pad 3 width
        Q = params.Q                # Pad 3 lenght
        serie = params.serie        # Serie

        if serie == 'FV1206':
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(A - (2.0 * D), B).extrude(C)
            case = case.faces(">Z").edges(">Y").fillet(0.05)
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(A / 2.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(A / 2.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)

        elif serie == 'FV1206-1':
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(A, B).extrude(C)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)
            
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">Y").fillet(0.05)
            case = case.faces(">Z").edges("<X").fillet(0.05)
            case = case.faces(">Z").edges(">X").fillet(0.05)

        elif serie == 'FV1206-4':
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(A, B).extrude(C)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((A / 2.0) - F / 2.0), 0.0).rect(F, Q).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((A / 2.0) - F / 2.0), 0.0).rect(F, Q).extrude(C)
            case = case.cut(case1)
            
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">Y").fillet(0.05)
            case = case.faces(">Z").edges("<X").fillet(0.05)
            case = case.faces(">Z").edges(">X").fillet(0.05)

        elif serie == 'FV1206-6':
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(A, B).extrude(C)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.cut(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.cut(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((A / 2.0) - F / 2.0), 0.0).rect(F, L).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((A / 2.0) - F / 2.0), 0.0).rect(F, L).extrude(C)
            case = case.cut(case1)
            
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">Y").fillet(0.05)
            case = case.faces(">Z").edges("<X").fillet(0.05)
            case = case.faces(">Z").edges(">X").fillet(0.05)

        elif serie == 'FV1206-7':
            
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(A, B).extrude(C)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(E, B).extrude(0.1)
            case = case.cut(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((A / 2.0) - (F / 2.0)), 0.0).rect(F, Q).extrude(C)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((A / 2.0) - (F / 2.0)), 0.0).rect(F, Q).extrude(C)
            case = case.cut(case1)

            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">Y").fillet(0.05)
            case = case.faces(">Z").edges("<X").fillet(0.05)
            case = case.faces(">Z").edges(">X").fillet(0.05)
        #
        # Pin 1 marker 
        #
        if serie == 'FV1206-1' or serie == 'FV1206-6':
            case1 = cq.Workplane("XY").workplane(offset=C - 0.1).moveTo(0.0 - (((A / 2.0) - D) - 0.3), 0.0).rect(0.6, 0.4).extrude(0.1)
            case = case.cut(case1)
        elif serie == 'FV1206-7':
            case1 = cq.Workplane("XY").workplane(offset=C - 0.1).moveTo(0.0 - ((A / 2.0) - 1.0), 0.0).rect(0.6, 0.4).extrude(0.1)
            case = case.cut(case1)
        else:
            case1 = cq.Workplane("XY").workplane(offset=C - 0.1).moveTo(0.0 - (((A / 2.0) - D) - 0.1), 0.0).rect(0.6, 0.4).extrude(0.1)
            case = case.cut(case1)

        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)
        if self.rotatey > 0.0:
            case = case.rotate((0,0,0), (0,1,0), self.rotatey)
        if self.rotatez > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatez)

        case = case.translate(self.translate)

        return (case)


    def make_pin(self, modelID):

        params = self.all_params[modelID]
        A = params.A                # Width
        B = params.B                # Length
        C = params.C                # Height
        D = params.D                # Pad 1 width
        E = params.E                # Pad 2 width
        F = params.F                # Pad 2 length
        G = params.G                # Pitch
        L = params.L                # Pad 3 width
        Q = params.Q                # Pad 3 lenght
        serie = params.serie        # Serie


        if serie == 'FV1206':
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo((A / 2.0) - (D / 2.0), 0.0).rect(D, B).extrude(C)
            case = case.faces(">Z").edges(">Y").fillet(0.05)
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">X").fillet(0.05)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((A / 2.0) - (D / 2.0)), 0.0).rect(D, B).extrude(C)
            case1 = case1.faces(">Z").edges(">Y").fillet(0.05)
            case1 = case1.faces(">Z").edges("<Y").fillet(0.05)
            case1 = case1.faces(">Z").edges("<X").fillet(0.05)
            case = case.union(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case1 = case1.faces(">Z").edges(">Y").fillet(0.05)
            case1 = case1.faces(">Z").edges("<Y").fillet(0.05)
            case = case.union(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case1 = case1.faces(">Z").edges(">Y").fillet(0.05)
            case1 = case1.faces(">Z").edges("<Y").fillet(0.05)
            case = case.union(case1)

        elif serie == 'FV1206-1':
            #
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.union(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.union(case1)
        
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">Y").fillet(0.05)

        elif serie == 'FV1206-4':
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.union(case1)
            #
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">Y").fillet(0.05)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((A / 2.0) - F / 2.0), 0.0).rect(F, Q).extrude(C)
            case1 = case1.faces(">Z").edges(">X").fillet(0.05)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((A / 2.0) - F / 2.0), 0.0).rect(F, Q).extrude(C)
            case1 = case1.faces(">Z").edges("<X").fillet(0.05)
            case = case.union(case1)

        elif serie == 'FV1206-6':
            #
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, (B / 2.0) - (F / 2.0)).rect(E, F).extrude(C)
            case = case.union(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - G, 0.0 - ((B / 2.0) - (F / 2.0))).rect(E, F).extrude(C)
            case = case.union(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((A / 2.0) - F / 2.0), 0.0).rect(F, L).extrude(C)
            case1 = case1.faces(">Z").edges(">X").fillet(0.05)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((A / 2.0) - F / 2.0), 0.0).rect(F, L).extrude(C)
            case1 = case1.faces(">Z").edges("<X").fillet(0.05)
            case = case.union(case1)
            
        
            case = case.faces(">Z").edges("<Y").fillet(0.05)
            case = case.faces(">Z").edges(">Y").fillet(0.05)

        elif serie == 'FV1206-7':
            #
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(E, B).extrude(0.1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((A / 2.0) - (F / 2.0)), 0.0).rect(F, Q).extrude(C)
            case1 = case1.faces(">Z").edges(">X").fillet(0.05)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((A / 2.0) - (F / 2.0)), 0.0).rect(F, Q).extrude(C)
            case1 = case1.faces(">Z").edges("<X").fillet(0.05)
            case = case.union(case1)


        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)
        if self.rotatey > 0.0:
            case = case.rotate((0,0,0), (0,1,0), self.rotatey)
        if self.rotatez > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatez)

        case = case.translate(self.translate)

        return (case)


    def make_npth_pin(self, modelID):

        params = self.all_params[modelID]
        A = params.A                # Width
        B = params.B                # Length
        C = params.C                # Height
        D = params.D                # Pad 1 width
        E = params.E                # Pad 2 width
        F = params.F                # Pad 2 length
        G = params.G                # Pitch
        L = params.L                # Pad 3 width
        Q = params.Q                # Pad 3 lenght
        serie = params.serie        # Serie


        #
        # Make dummy
        #
        case = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0, 0.0).rect(0.01, 0.01).extrude(0.01)
#        case = case.faces("<X").edges("<Y").fillet(0.03)
#        case = case.faces("<X").edges(">Y").fillet(0.03)
#        case = case.faces(">X").edges("<Y").fillet(0.03)
#        case = case.faces(">X").edges(">Y").fillet(0.03)

        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)
        if self.rotatey > 0.0:
            case = case.rotate((0,0,0), (0,1,0), self.rotatey)
        if self.rotatez > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatez)

        case = case.translate(self.translate)

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
        'A',		            # Width
        'B',		            # Length
        'C',		            # Overall height
        'D',		            # pad 1 width
        'E',		            # pad 2 width
        'F',		            # pad 2 length
        'G',		            # pitch
        'L',		            # Pad 3 width
        'Q',		            # Pad 3 lenght
        'serie',		        # Serie
        'npth_pin_color_key',   # NPTH Pin color
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'dest_dir_prefix'	    # Destination directory
    ])


    all_params = {

        'FV1206': Params(
            #
            # https://ww2.minicircuits.com/case_style/FV1206.pdf
            #
            modelName = 'Filter_Mini-Circuits_FV1206',    # Model name
            A = 3.20,               # Width
            B = 1.60,               # Length
            C = 0.94,               # Overall height
            D = 0.51,
            E = 0.81,
            F = 0.23,
            serie = 'FV1206',       # Serie
            ),

        'FV1206-1': Params(
            #
            # https://ww2.minicircuits.com/case_style/FV1206-1.pdf
            #
            modelName = 'Filter_Mini-Circuits_FV1206-1',    # Model name
            A = 3.20,               # Width
            B = 1.60,               # Length
            C = 0.89,               # Overall height
            D = 0.61,
            E = 0.56,
            F = 0.28,
            G = 0.99,
            serie = 'FV1206-1',     # Serie
            ),

        'FV1206-4': Params(
            #
            # https://ww2.minicircuits.com/case_style/FV1206-4.pdf
            #
            modelName = 'Filter_Mini-Circuits_FV1206-4',    # Model name
            A = 3.20,               # Width
            B = 1.60,               # Length
            C = 0.94,               # Overall height
            D = 0.66,
            E = 1.91,
            F = 0.30,
            Q = 0.51,
            serie = 'FV1206-4',     # Serie
            ),

        'FV1206-5': Params(
            #
            # https://ww2.minicircuits.com/case_style/FV1206-5.pdf
            #
            modelName = 'Filter_Mini-Circuits_FV1206-5',    # Model name
            A = 3.20,               # Width
            B = 1.60,               # Length
            C = 1.30,               # Overall height
            D = 0.66,
            E = 1.91,
            F = 0.30, 
            Q = 0.51,
            serie = 'FV1206-4',     # Serie
            ),

        'FV1206-6': Params(
            #
            # https://ww2.minicircuits.com/case_style/FV1206-6.pdf
            #
            modelName = 'Filter_Mini-Circuits_FV1206-6',    # Model name
            A = 3.20,               # Width
            B = 1.60,               # Length
            C = 0.95,               # Overall height
            D = 0.33, 
            E = 0.56, 
            F = 0.30,
            G = 0.99,
            L = 0.50,
            Q = 0.30,
            serie = 'FV1206-6',     # Serie
            ),

        'FV1206-7': Params(
            #
            # https://ww2.minicircuits.com/case_style/FV1206-7.pdf
            #
            modelName = 'Filter_Mini-Circuits_FV1206-7',    # Model name
            A = 3.20,               # Width
            B = 1.60,               # Length
            C = 1.30,               # Overall height
            E = 1.30,
            F = 0.35,
            Q = 0.50,
            serie = 'FV1206-7',     # Serie
            ),
    }

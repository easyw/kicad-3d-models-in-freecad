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


class cq_murata():

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


    def set_rotation(self, params):

        self.rotatex = 0.0          # Rotation around x-axis if required
        self.rotatey = 0.0          # Rotation around x-axis if required
        self.rotatez = 0.0          # Rotation around y-axis if required


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
        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        H1 = params.H1              # Height 1
        serie = params.serie        # Serie


        #
        # Pin 1 marker 
        #
        case = cq.Workplane("XY").workplane(offset=H - 0.1).moveTo(0.0 - (W / 2.0) + (W / 5.0) , 0.0 - (L / 2.0) + (L / 5.0)).circle(0.05, False).extrude(0.1)
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)
        if self.rotatey > 0.0:
            case = case.rotate((0,0,0), (0,1,0), self.rotatey)
        if self.rotatez > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatez)

        case = case.translate(self.translate)

        return (case)



    def make_body(self, modelID):

        FreeCAD.Console.PrintMessage('make_body 1 \r\n')
        params = self.all_params[modelID]
        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        H1 = params.H1              # Height 1
        serie = params.serie        # Serie


        #
        # Make body
        #
        case = cq.Workplane("XY").workplane(offset=H1).moveTo(0.0, 0.0).rect(W, L).extrude(H - H1)
        case = case.faces("<X").edges("<Y").fillet(0.03)
        case = case.faces("<X").edges(">Y").fillet(0.03)
        case = case.faces(">X").edges("<Y").fillet(0.03)
        case = case.faces(">X").edges(">Y").fillet(0.03)
        case = case.faces(">Z").fillet(0.03)
                
        case1 = cq.Workplane("XY").workplane(offset=H - 0.1).moveTo(0.0 - (W / 2.0) + (W / 5.0) , 0.0 - (L / 2.0) + (L / 5.0)).circle(0.05, False).extrude(0.2)
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
        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        H1 = params.H1              # Height 1
        serie = params.serie        # Serie


        if serie == 'SAFEA':
            #
            # Make dummy
            #
            case = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0, 0.0).circle(0.01, 0.01).extrude(0.01)
        elif serie == 'SAFFB':
            case = cq.Workplane("XY").workplane(offset=-0.005).moveTo(-0.385, 0.0).rect(0.18, 0.25).extrude(0.1)
            case1 = cq.Workplane("XY").workplane(offset=-0.005).moveTo(0.0, 0.0 - 0.25).rect(0.18, 0.25).extrude(0.1)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=-0.005).moveTo(0.25, 0.0 - 0.25).rect(0.18, 0.25).extrude(0.1)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=-0.005).moveTo(0.25, 0.25).rect(0.18, 0.25).extrude(0.1)
            case = case.union(case1)
            case1 = cq.Workplane("XY").workplane(offset=-0.005).moveTo(0.0, 0.25).rect(0.18, 0.25).extrude(0.1)
            case = case.union(case1)
        elif serie == 'SAWEN':
            #
            # Make dummy
            #
            case = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0, 0.0).circle(0.01, 0.01).extrude(0.01)
        elif serie == 'SAWFD':
            #
            # Make dummy
            #
            case = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0, 0.0).circle(0.01, 0.01).extrude(0.01)
        else:
            #
            # Make dummy
            #
            case = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0, 0.0).circle(0.01, 0.01).extrude(0.01)
        
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
        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        H1 = params.H1              # Height 1
        serie = params.serie        # Serie


        #
        # Make dummy
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H1)
        case = case.faces("<X").edges("<Y").fillet(0.03)
        case = case.faces("<X").edges(">Y").fillet(0.03)
        case = case.faces(">X").edges("<Y").fillet(0.03)
        case = case.faces(">X").edges(">Y").fillet(0.03)

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
        'W',		            # Width
        'L',		            # Length
        'H',		            # Overall height
        'H1',		            # Height 1
        'serie',		        # Serie
        'npth_pin_color_key',   # NPTH Pin color
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'dest_dir_prefix'	    # Destination directory
    ])


    all_params = {

        #
        # https://www.murata.com/~/media/webrenewal/support/library/catalog/products/filter/rf/p73e.ashx?la=en-gb
        # 
        'SAFEA2G14FF0F00': Params(
            modelName = 'SAFEA2G14FF0F00',    # Model name
            W = 1.35,               # Width
            L = 1.05,               # Length
            H = 0.5,                # Overall height
            H1 = 0.17,              # Height 1
            serie = 'SAFEA',        # Serie
            ),

        'Filter_1109-5_1.1x0.9mm': Params(
            modelName = 'Filter_1109-5_1.1x0.9mm',    # Model name
            W = 1.1,                # Width
            L = 0.9,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAFFB',        # Serie
            ),

        'SAFFB2G14FA0F0A': Params(
            modelName = 'Filter_1109-5_1.1x0.9mm',    # Model name
            W = 1.1,                # Width
            L = 0.9,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAFFB',        # Serie
            ),

        'SAFEA1G96FR0F00': Params(
            modelName = 'SAFEA1G96FR0F00',    # Model name
            W = 1.35,               # Width
            L = 1.05,               # Length
            H = 0.5,                # Overall height
            H1 = 0.17,              # Height 1
            serie = 'SAFEA',        # Serie
            ),

        'SAFFB1G96FN0F0A': Params(
            modelName = 'Filter_1109-5_1.1x0.9mm',    # Model name
            W = 1.1,                # Width
            L = 0.9,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAFFB',        # Serie
            ),

        'SAFEA881MFR0F00': Params(
            modelName = 'SAFEA881MFR0F00',    # Model name
            W = 1.35,               # Width
            L = 1.05,               # Length
            H = 0.5,                # Overall height
            H1 = 0.17,              # Height 1
            serie = 'SAFEA',        # Serie
            ),

        'SAFFB881MFL0F0A': Params(
            modelName = 'Filter_1109-5_1.1x0.9mm',    # Model name
            W = 1.1,                # Width
            L = 0.9,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAFFB',        # Serie
            ),

        'SAFEA942MFR0F00': Params(
            modelName = 'SAFEA942MFR0F00',    # Model name
            W = 1.35,               # Width
            L = 1.05,               # Length
            H = 0.5,                # Overall height
            H1 = 0.17,              # Height 1
            serie = 'SAFEA',        # Serie
            ),

        'SAFFB942MFM0F0A': Params(
            modelName = 'Filter_1109-5_1.1x0.9mm',    # Model name
            W = 1.1,                # Width
            L = 0.9,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAFFB',        # Serie
            ),

        'SAFEA1G58KA0F00': Params(
            modelName = 'SAFEA1G58KA0F00',    # Model name
            W = 1.35,               # Width
            L = 1.05,               # Length
            H = 0.5,                # Overall height
            H1 = 0.17,              # Height 1
            serie = 'SAFEA',        # Serie
            ),

        'SAFEA1G58FB0F00': Params(
            modelName = 'SAFEA1G58FB0F00',    # Model name
            W = 1.35,               # Width
            L = 1.05,               # Length
            H = 0.5,                # Overall height
            H1 = 0.17,              # Height 1
            serie = 'SAFEA',        # Serie
            ),

        'SAFFB1G58KA0F0A': Params(
            modelName = 'Filter_1109-5_1.1x0.9mm',    # Model name
            W = 1.1,                # Width
            L = 0.9,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAFFB',        # Serie
            ),

        'SAFFB1G58FA0F0A': Params(
            modelName = 'SAFFB1G58FA0F0A',    # Model name
            W = 1.1,                # Width
            L = 0.9,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAFFB',        # Serie
            ),

        'SAFEA2G45RA0F00': Params(
            modelName = 'SAFEA2G45RA0F00',    # Model name
            W = 1.35,               # Width
            L = 1.05,               # Length
            H = 0.5,                # Overall height
            H1 = 0.17,              # Height 1
            serie = 'SAFEA',        # Serie
            ),

        'SAWFD881MCM0F0A': Params(
            modelName = 'SAWFD881MCM0F0A',    # Model name
            W = 1.5,               # Width
            L = 1.1,               # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWFD',        # Serie
            ),

        'SAWFD881MCN0F0A': Params(
            modelName = 'SAWFD881MCN0F0A',    # Model name
            W = 1.5,                # Width
            L = 1.1,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWFD',        # Serie
            ),

        'SAWFD1G84CM0F0A': Params(
            modelName = 'SAWFD1G84CM0F0A',    # Model name
            W = 1.5,               # Width
            L = 1.1,               # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWFD',        # Serie
            ),

        'SAWFD1G84CN0F0A': Params(
            modelName = 'SAWFD1G84CN0F0A',    # Model name
            W = 1.5,                # Width
            L = 1.1,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWFD',        # Serie
            ),

        'SAWFD942MCM0F0A': Params(
            modelName = 'SAWFD942MCM0F0A',    # Model name
            W = 1.5,                # Width
            L = 1.1,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWFD',        # Serie
            ),

        'SAWFD942MCN0F0A': Params(
            modelName = 'SAWFD942MCN0F0A',    # Model name
            W = 1.5,                # Width
            L = 1.1,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWFD',        # Serie
            ),

        'SAWEN881MCM0F00': Params(
            modelName = 'SAWEN881MCM0F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),

        'SAWEN881MCN0F00': Params(
            modelName = 'SAWEN881MCN0F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),

        'SAWEN1G84CM0F00': Params(
            modelName = 'SAWEN1G84CM0F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),

        'SAWEN1G84CN0F00': Params(
            modelName = 'SAWEN1G84CN0F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),

        'SAWEN881MCM2F00': Params(
            modelName = 'SAWEN881MCM2F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),

        'SAWEN881MCN2F00': Params(
            modelName = 'SAWEN881MCN2F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),

        'SAWEN942MCM0F00': Params(
            modelName = 'SAWEN942MCM0F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),

        'SAWEN942MCN0F00': Params(
            modelName = 'SAWEN942MCN0F00',    # Model name
            W = 1.8,                # Width
            L = 1.4,                # Length
            H = 0.5,                # Overall height
            H1 = 0.15,              # Height 1
            serie = 'SAWEN',        # Serie
            ),
    }

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


class cq_belfuse():

    def __init__(self):
        self.body_top_color_key  = 'white body'         # Top color
        self.body_color_key      = 'orange body'        # Body color
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

        return 'Fuse.3dshapes'


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
        

    def get_comp_size(self, modelID):


                    # (Fig, A, B, C, D , E, F, G)
        if modelID == '0ZRE0005FF':
            return (1, 8.3, 10.7, 5.1, 2.5, 3.8, 1.6, 0.51)

        if modelID == '0ZRE0008FF':
            return (1, 8.3, 10.7, 5.1, 2.5, 3.8, 1.6, 0.51)

        if modelID == '0ZRE0012FF':
            return (1, 8.3, 10.7, 5.1, 2.5, 3.8, 1.6, 0.51)

        if modelID == '0ZRE0016FF':
            return (1, 9.9, 12.5, 5.1, 2.5, 3.8, 1.6, 0.51)

        if modelID == '0ZRE0025FF':
            return (2, 9.6, 17.4, 5.1, 2.5, 3.8, 1.8, 0.65)

        if modelID == '0ZRE0033FF':
            return (2, 11.4, 16.5, 5.1, 2.5, 3.8, 1.8, 0.65)

        if modelID == '0ZRE0040FF':
            return (2, 11.5, 19.5, 5.1, 2.5, 3.8, 1.8, 0.65)

        if modelID == '0ZRE0055FF':
            return (3, 14.0, 21.7, 5.1, 2.5, 4.1, 1.9, 0.81)

        if modelID == '0ZRE0075FF':
            return (3, 11.5, 23.4, 5.1, 2.5, 4.8, 1.9, 0.81)

        if modelID == '0ZRE0100FF':
            return (4, 18.7, 24.4, 10.2, 2.5, 5.1, 1.9, 0.81)

        if modelID == '0ZRE0125FF':
            return (4, 21.2, 27.4, 10.2, 2.5, 5.3, 1.9, 0.81)

        if modelID == '0ZRE0150FF':
            return (4, 23.4, 30.9, 10.2, 2.5, 5.3, 1.9, 0.81)

        if modelID == '0ZRE0200FF':
            return (3, 24.9, 33.8, 10.2, 2.5, 6.1, 1.9, 0.81)


        FreeCAD.Console.PrintMessage('\r\n')
        FreeCAD.Console.PrintMessage('ERROR: Model ID ' + str(modelID) + ' does not exist, exiting')
        FreeCAD.Console.PrintMessage('\r\n')
        sys.exit()

        return None


    def set_translate(self, modelID):

        Fig, A, B, C, D , E, F, G = self.get_comp_size(modelID)
        
        ttdx = 0.0
        ttdy = 0.0
        ttdz = D - 2.0
        
        self.translate = (ttdx, ttdy, ttdz)


    def make_3D_model(self, modelID):

        destination_dir = self.get_dest_3D_dir(modelID)
        params = self.all_params[modelID]

        self.set_colors(modelID)
        self.set_translate(modelID)
        self.set_rotation(modelID)
        case_top = self.make_top(modelID)
        show(case_top)
        case = self.make_body(modelID)
        show(case)

        pins = self.make_pin(modelID)
        show(pins)

        npth_pins = self.make_npth_pin(modelID)
        show(npth_pins)

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
        Fig, A, B, C, D , E, F, G = self.get_comp_size(modelID)

        #
        # Make dummy
        #
        case = cq.Workplane("XY").workplane(offset=-0.5).moveTo(0.0, 0.0).circle(0.01 , False).extrude(0.01)
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

#        case = case.translate(self.translate)

        return (case)



    def make_body(self, modelID):

        params = self.all_params[modelID]
        Fig, A, B, C, D , E, F, G = self.get_comp_size(modelID)

        
        #
        # Make body
        #
        ttdz = B - A
        F1 = F * 0.6
        if Fig == 1 or Fig == 4:
            case = cq.Workplane("XZ").workplane(offset=(F / 2.0) - (F1 / 2.0)).moveTo(C / 2.0, (A / 2.0) + ttdz).circle((A / 2.0), False).extrude(F1)
            case = case.faces("<Y").fillet(F1 / 2.1)
            case = case.faces(">Y").fillet(F1 / 2.1)
        else:
            case = cq.Workplane("XZ").workplane(offset=(F / 2.0) - (F1 / 2.0)).moveTo(C / 2.0, (A / 2.0) + ttdz).rect(A, A).extrude(F1)
            case = case.faces("<X").edges(">Z").fillet(1.0)
            case = case.faces("<X").edges("<Z").fillet(1.0)
            case = case.faces(">X").edges(">Z").fillet(1.0)
            case = case.faces(">X").edges("<Z").fillet(1.0)
            case = case.faces("<Y").fillet(F1 / 4.0)
            case = case.faces(">Y").fillet(F1 / 4.0)


        #
        # Pin 1
        #
        pinsl = ((A / 2.0) + ttdz) - (A / 4.0)
        ex = C / 2.0
        ey = ((A / 2.0) + ttdz)

        cqrt = cq_parameters_others()
        case1 = cqrt._make_bent_pin(G, pinsl, ex, ey)
        case1 = case1.rotate((0,0,0), (0,0,1), -7.0)
        case = case.union(case1)

        #
        # Pin 2
        #
        cqrt = cq_parameters_others()
        case1 = cqrt._make_bent_pin(G, pinsl, ex, ey)
        case1 = case1.rotate((0,0,0), (0,0,1), -7.0)
        case1 = case1.rotate((0,0,0), (0,0,1), 180)
        case1 = case1.translate((C, 0.0 - F, 0.0))
        case = case.union(case1)
        


#        pin = cqrt._make_angled_pin(pin_height = -4.0, top_length=6.0, style='round')
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

#        case = case.translate(self.translate)

        return (case)


    def make_pin(self, modelID):

        params = self.all_params[modelID]
        Fig, A, B, C, D , E, F, G = self.get_comp_size(modelID)

        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(G / 2.0, False).extrude(0.0 - D)
        case = case.faces("<Z").fillet(G / 2.2)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(C, 0.0 - F).circle(G / 2.0, False).extrude(0.0 - D)
        case1 = case1.faces("<Z").fillet(G / 2.2)
        case = case.union(case1)

        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

#        case = case.translate(self.translate)

        return (case)


    def make_npth_pin(self, modelID):

        params = self.all_params[modelID]
        Fig, A, B, C, D , E, F, G = self.get_comp_size(modelID)

        
        #
        # Make dummy
        #
        case = cq.Workplane("XY").workplane(offset=-0.5).moveTo(0.0, 0.0).circle(0.01 , False).extrude(0.01)
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

#        case = case.translate(self.translate)

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
        'npth_pin_color_key',   # NPTH Pin color
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'dest_dir_prefix'	    # Destination directory
    ])


    all_params = {

        #
        # https://www.belfuse.com/resources/datasheets/circuitprotection/ds-cp-0zre-series.pdf
        # 
        '0ZRE0005FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0005FF_L8.3mm_W3.8mm',    # Model name
            ),

        '0ZRE0008FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0008FF_L8.3mm_W3.8mm',    # Model name
            ),

        '0ZRE0012FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0012FF_L8.3mm_W3.8mm',    # Model name
            ),

        '0ZRE0016FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0016FF_L9.9mm_W3.8mm',    # Model name
            ),

        '0ZRE0025FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0025FF_L9.6mm_W3.8mm',    # Model name
            ),

        '0ZRE0033FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0033FF_L11.4mm_W3.8mm',    # Model name
            ),

        '0ZRE0040FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0040FF_L11.5mm_W3.8mm',    # Model name
            ),

        '0ZRE0055FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0055FF_L14.0mm_W4.1mm',    # Model name
            ),

        '0ZRE0075FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0075FF_L11.5mm_W4.8mm',    # Model name
            ),

        '0ZRE0100FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0100FF_L18.7mm_W5.1mm',    # Model name
            ),

        '0ZRE0125FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0125FF_L21.2mm_W5.3mm',    # Model name
            ),

        '0ZRE0150FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0150FF_L23.4mm_W5.3mm',    # Model name
            ),

        '0ZRE0200FF': Params(
            modelName = 'Fuse_BelFuse_0ZRE_0ZRE0200FF_L24.9mm_W6.1mm',    # Model name
            ),
    }

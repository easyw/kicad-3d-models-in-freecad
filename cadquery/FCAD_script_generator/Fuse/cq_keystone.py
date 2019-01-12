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


class cq_keystone():

    def __init__(self):
        self.body_top_color_key  = 'metal grey pins'    # Top color
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


    def set_translate(self, modelID):

        ttdx = 0.0
        ttdy = 0.0
        ttdz = 0.0
        
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

        #
        # Make dummy
        #
        case = cq.Workplane("XY").workplane(offset=0.5).moveTo(0.0, 0.0).circle(0.01 , False).extrude(0.01)
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return (case)



    def make_body(self, modelID):

        params = self.all_params[modelID]

        W = params.W
        L = params.L
        H = params.H
        pin1 = params.pin1
        
        #
        # Make body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        
        case = case.faces("<X").edges("<Y").fillet(0.2)
        case = case.faces("<X").edges(">Y").fillet(0.2)
        case = case.faces(">X").edges("<Y").fillet(0.2)
        case = case.faces(">X").edges(">Y").fillet(0.2)
        #
        case = case.faces(">Z").fillet(0.2)
        #
        #
        t = L / 6.0
        wd = W / 3.0
        ld = L - (t * 2.0)
        wdx = t + (wd / 2.0)
        wdy = 0.0
        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(wdx, wdy).rect(wd - 0.5, ld).extrude((H / 2.0) + 0.2)
        case = case.cut(case1)
        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(wdx - (wd / 2.0), wdy).rect(0.5, ld - 0.5).extrude((H / 2.0) + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(0.0 - wdx, wdy).rect(wd - 0.5, ld).extrude((H / 2.0) + 0.2)
        case = case.cut(case1)
        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo((0.0 - wdx) + (wd / 2.0), wdy).rect(0.5, ld - 0.5).extrude((H / 2.0) + 0.2)
        case = case.cut(case1)
                          
                          
#        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(0.0 - wdx, wdy).rect((wd - 0.5) - 0.1, ld - 0.1).extrude((H / 2.0))
#        case2 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(0.0 - wdx, wdy).rect((wd - 0.5) - 1.0, ld - 1.0).extrude((H / 2.0))
#        case1 = case1.cut(case2)
#        case = case.union(case1)
        
        #
        #
        dx = pin1[0] + (W / 2.0)
        dy = 0.0 - L / 2.0
        #
        case = case.translate((dx, dy, 0.0))
        case = case.translate((0.0, 0.0 - pin1[1], 0.0))
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return (case)


    def make_pin(self, modelID):

        params = self.all_params[modelID]

        W = params.W
        L = params.L
        H = params.H
        pin1 = params.pin1
        pin = params.pin
        
        
        #
        # Make pins
        #
        case = None
        #
        for p in pin:
            t = p[0]
            x = p[1]
            y = p[2]
            w = p[3]
            l = p[4]
            h = p[5]
            if p[0] == 'rect':
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(x, 0.0 - y).rect(w, l).extrude(0.0 - h)
                case1 = case1.faces("<X").edges("<Z").chamfer(w / 4.0, w / 4.0)
                case1 = case1.faces(">X").edges("<Z").chamfer(w / 4.0, w / 4.0)
        
            if case == None:
                case = case1
            else:
                case = case.union(case1)
        
#            case = case.faces(">X").edges("<Z").chamfer(w / 4.0)
        
        #
        # 
        cqt = cq_parameters_others()
        
        t = L / 6.0
        wd = (W / 3.0)
        ld = (L - (t * 2.0)) / 2.0
        wdx = t + (wd / 2.0)
        case1 = cqt._make_fuse_clip_pin(wd - 0.5, ld, H, 0.4)
        case1 = case1.translate((0.0 - (wdx + (wd / 2.0) - 0.25), (0.0 - (L / 2.0)) + t, 0.0))

        case1 = case1.faces(">X").edges("#Y").fillet(0.4)
        case1 = case1.faces("<X[1]").edges("#Y").fillet(0.3)
        case1 = case1.faces(">X[1]").edges("#Y").fillet(0.3)
        case1 = case1.faces("<X").edges("#Y").fillet(0.4)
        #
        case2 = cqt._make_fuse_clip_pin(wd - 0.5, ld, H, 0.4)
        case2 = case2.faces(">X").edges("#Y").fillet(0.4)
        case2 = case2.faces("<X[1]").edges("#Y").fillet(0.3)
        case2 = case2.faces(">X[1]").edges("#Y").fillet(0.3)
        case2 = case2.faces("<X").edges("#Y").fillet(0.4)
        #
        case2 = case2.rotate((0,0,0), (0,0,1), 180.0)
        case2 = case2.translate((0.0, 2.0 * ld, 0.0))
        case2 = case2.translate(((wdx + (wd / 2.0) - 0.25), (0.0 - (L / 2.0)) + t, 0.0))



        case1 = case1.union(case2)
        #
        dx = pin1[0] + (W / 2.0)
        dy = 0.0 - L / 2.0
        #
        case1 = case1.translate((dx, dy, 0.0))
        case1 = case1.translate((0.0, 0.0 - pin1[1], 0.0))
        
        case = case.union(case1)

        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return (case)


    def make_npth_pin(self, modelID):

        params = self.all_params[modelID]

        #
        # Make dummy
        #
        case = cq.Workplane("XY").workplane(offset=0.5).moveTo(0.0, 0.0).circle(0.01 , False).extrude(0.01)
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

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
        'W',                    # Width
        'L',                    # Length
        'H',                    # Height
        'A1',                   # Body above PCB
        'pin1',                 # pin1 corner
        'pin',                  # pins
        'npth_pin_color_key',   # NPTH Pin color
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'dest_dir_prefix'	    # Destination directory
    ])


    all_params = {

        #
        # http://www.keyelco.com/product-pdf.cfm?p=306
        # 
        'Keystone_3568': Params(
            modelName = 'Fuseholder_Blade_Mini_Keystone_3568',    # Model name
            W = 16.0,                    # Width
            L = 6.73,                    # Length
            H = 7.37,                    # Height
            A1 = 0.0,                   # Body above PCB
            pin1 = [-3.04, -1.67],
            pin = [['rect', 0.0, 0.0, 1.57, 0.4, 2.79], ['rect', 9.92, 0.0, 1.57, 0.4, 2.79], ['rect', 0.0, 3.4, 1.57, 0.4, 2.79], ['rect', 9.92, 3.4, 1.57, 0.4, 2.79]]
            ),
    }

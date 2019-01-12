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


class cq_schurter():

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
        #
        if modelID == 'Schurter_0031-8002':
            case = self.make_body_Schurter_0031_8002(modelID)
            show(case)
            pins = self.make_pin_Schurter_0031_8002(modelID)
            show(pins)

        if modelID == 'Schurter_0031_8201':
            case = self.make_body_Schurter_0031_8201(modelID)
            show(case)
            pins = self.make_pin_Schurter_0031_8201(modelID)
            show(pins)

        if modelID == 'Schurter_FAB_0031_355x':
            case = self.make_body_Schurter_FAB_0031_355x(modelID)
            show(case)
            pins = self.make_pin_Schurter_FAB_0031_355x(modelID)
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


    def make_body_Schurter_0031_8002(self, modelID):

        params = self.all_params[modelID]

        W = params.W
        L = params.L
        H = params.H
        H1 = params.H1
        pin = params.pin
        
        #
        # Make body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        #
        case = case.faces("<Y").edges(">Z").chamfer(H / 2.1, 0.6)
        case = case.faces("<Y").edges("<Z").chamfer(H / 2.1, 0.6)
        #
        case = case.faces(">Y").edges(">Z").chamfer(0.6, H / 2.0)
        case = case.faces(">Y").edges("<Z").chamfer(H / 2.1, 0.6)
        #
        # Add a little top in the middle
        #
        case1 = cq.Workplane("XY").workplane(offset=H).moveTo(0.0, 0.0).circle(8.0 / 2.0, False).extrude(0.4)
        case = case.union(case1)
        #
        # Cut up the hole in the middle
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0, 0.0).circle(3.2 / 2.0, False).extrude(H + 1.0)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=H / 2.0).moveTo(0.0, 0.0).circle(6.3 / 2.0, False).extrude(H + 0.2)
        case = case.cut(case1)
        #
        # Cut up the hole in the ends
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo((W / 2.0) - 2.0, 0.0).rect(4.0, 4.0).extrude(H - 0.8)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - ((W / 2.0) - 2.0), 0.0).rect(4.0, 4.0).extrude(H - 0.8)
        case = case.cut(case1)
        #
        #
        #
        p = pin[1]
        dx = p[1]
        case = case.translate((dx / 2.0, 0.0, 0.0))
        
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return (case)


    def make_body_Schurter_0031_8201(self, modelID):

        params = self.all_params[modelID]

        W = params.W
        L = params.L
        H = params.H
        H1 = params.H1
        pin = params.pin
        
        #
        # Make body
        #
        tdx = (2.0 * W) / 7.0
        tdt = 1.0
        
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(tdt)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((W / 2.0) - (tdx / 2.0)), ((L / 2.0) - (tdt / 2.0))).rect(tdx, tdt).extrude(H)
        case1 = case1.faces(">Z").edges("<X").chamfer(tdx / 5.0, tdx / 5.0)
        case1 = case1.faces(">Z").edges(">X").chamfer(tdx / 5.0, tdx / 5.0)
        case = case.union(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(((W / 2.0) - (tdx / 2.0)), 0.0 - ((L / 2.0) - (tdt / 2.0))).rect(tdx, tdt).extrude(H)
        case1 = case1.faces(">Z").edges("<X").chamfer(tdx / 5.0, tdx / 5.0)
        case1 = case1.faces(">Z").edges(">X").chamfer(tdx / 5.0, tdx / 5.0)
        case = case.union(case1)
        
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((W / 2.0) - (tdx / 2.0)), ((L / 2.0) - (tdt / 2.0))).rect(tdx, tdt).extrude(H)
        case1 = case1.faces(">Z").edges("<X").chamfer(tdx / 5.0, tdx / 5.0)
        case1 = case1.faces(">Z").edges(">X").chamfer(tdx / 5.0, tdx / 5.0)
        case = case.union(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - ((W / 2.0) - (tdx / 2.0)), 0.0 - ((L / 2.0) - (tdt / 2.0))).rect(tdx, tdt).extrude(H)
        case1 = case1.faces(">Z").edges("<X").chamfer(tdx / 5.0, tdx / 5.0)
        case1 = case1.faces(">Z").edges(">X").chamfer(tdx / 5.0, tdx / 5.0)
        case = case.union(case1)
        #
        # Cut up the hole in the middle
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0, 0.0).circle(2.7 / 2.0, False).extrude(H + 1.0)
        case = case.cut(case1)
        #
        case = case.faces("<Y").fillet(0.4)
        case = case.faces(">Y").fillet(0.4)
        #
        p = pin[1]
        dx = p[1]
        case = case.translate((dx / 2.0, 0.0, 0.0))
        
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return (case)


    def make_body_Schurter_FAB_0031_355x(self, modelID):

        params = self.all_params[modelID]

        W = params.W
        L = params.L
        H = params.H
        H1 = params.H1
        pin = params.pin
        
        #
        # Make body
        #
        case = cq.Workplane("YZ").workplane(offset=0.0).moveTo(0.0, H / 2.0).circle(H / 2.0, False).extrude(W)
        #
        #
        case1 = cq.Workplane("YZ").workplane(offset=0.0).moveTo(0.0, L / 2.0).circle(L / 2.0, False).extrude(W - 5.0)
        case2 = cq.Workplane("YZ").workplane(offset=0.0).moveTo(0.0, L / 4.0).rect(L, L / 2.0).extrude(W - 5.0)
        case1 = case1.union(case2)
        case1 = case1.faces("<X").fillet(0.2)
        case1 = case1.faces(">X").fillet(0.2)
        case = case.union(case1)
        #
        case1 = cq.Workplane("YZ").workplane(offset=0.0 - 0.1).moveTo(0.0, H + 2.0).rect(L, 4.0).extrude(W + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("YZ").workplane(offset=W - 2.0).moveTo(0.0, H / 2.0).rect(6.0, 1.8).extrude(3.0)
        case = case.cut(case1)
        #
        #
        #
        case1 = cq.Workplane("YZ").workplane(offset=W - 2.0).moveTo(0.0, H / 2.0).circle((H / 2.0) - 0.4, False).extrude(3.0)
        case2 = cq.Workplane("YZ").workplane(offset=W - 2.0).moveTo(0.0, H / 2.0).circle((H / 2.0) - 0.8, False).extrude(3.0)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        #
#        case = case.faces(">Z").fillet(0.2)
        #
        case = case.translate((0.0 - 0.25, 0.0, 0.0))

        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return (case)


    def make_pin_Schurter_0031_8002(self, modelID):

        params = self.all_params[modelID]
        W = params.W
        L = params.L
        H = params.H
        H1 = params.H1
        pin = params.pin
        fuse = params.fuse
        
        
        #
        # Make pins
        #
        case = None
        qrt = cq_parameters_others()
        fd, fl = fuse
        #
        p = pin[1]
        x = p[1]
        mx = x / 2.0
        mx = mx - (fl / 2.0)
        #
        for p in pin:
            t = p[0]
            x = p[1]
            y = p[2]
            w = p[3]
            l = p[4]
            h = p[5]
            if p[0] == 'rect':
                
                case1 = qrt._make_arrow_pin(w, l, h, 3.5, (h + H) - (2.0 * l), H / 2.0, 'arrow')
                case1 = case1.rotate((0,0,0), (0,0,1), 90.0)
                case1 = case1.translate((x, y, 0.0 - h))

            if case == None:
                case = case1
            else:
                case = case.union(case1)

            case1 = qrt._make_fuse_holder(fd / 2.0, 4.0, 7.0, 3.0, 3.0, 0.3)
            case1 = case1.rotate((0,0,0), (0,0,1), 90.0)
            
            case1 = case1.translate((mx, y, H))
            case = case.union(case1)
            #
            mx = mx + fl
        #
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatex)

        return (case)


    def make_pin_Schurter_0031_8201(self, modelID):

        params = self.all_params[modelID]
        W = params.W
        L = params.L
        H = params.H
        H1 = params.H1
        pin = params.pin
        fuse = params.fuse
        
        
        #
        # Make pins
        #
        case = None
        qrt = cq_parameters_others()
        fd, fl = fuse
        tdx = (2.0 * W) / 7.0
        #
        p = pin[1]
        x = p[1]
        w = p[3]
        l = p[4]
        mx = (tdx / 2.0) - (l / 2.0)
        mx2 = (x - (tdx / 2.0)) + (l / 2.0) 
        #
        for p in pin:
            t = p[0]
            x = p[1]
            y = p[2]
            w = p[3]
            l = p[4]
            h = p[5]
            if p[0] == 'rect':
                
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(x, y).rect(l, w).extrude(0.0 - h)
                case1 = case1.faces("<Z").edges("<Y").chamfer(w / 4.0, w / 4.0)
                case1 = case1.faces("<Z").edges(">Y").chamfer(w / 4.0, w / 4.0)

            if case == None:
                case = case1
            else:
                case = case.union(case1)

            case1 = qrt._make_fuse_holder(fd / 2.0, tdx, H, 5.0, 5.0, 0.3)
            case1 = case1.rotate((0,0,0), (0,0,1), 90.0)
            
            case1 = case1.translate((mx, y, 0.0))
            case = case.union(case1)
            #
            mx = mx2
        #
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatex)

        return (case)


    def make_pin_Schurter_FAB_0031_355x(self, modelID):

        params = self.all_params[modelID]
        W = params.W
        L = params.L
        H = params.H
        H1 = params.H1
        pin = params.pin
        fuse = params.fuse
        
        
        #
        # Make pins
        #
        case = None
        qrt = cq_parameters_others()
        fd, fl = fuse
        #
        p = pin[1]
        x = p[1]
        w = p[3]
        l = p[4]
        #
        for p in pin:
            t = p[0]
            x = p[1]
            y = p[2]
            w = p[3]
            l = p[4]
            h = p[5]
            if p[0] == 'rect':
                
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(x, y).rect(l, w).extrude(0.0 - h)
                case1 = case1.faces("<Z").edges("<Y").chamfer(w / 4.0, w / 4.0)
                case1 = case1.faces("<Z").edges(">Y").chamfer(w / 4.0, w / 4.0)

            if case == None:
                case = case1
            else:
                case = case.union(case1)
        #
        
        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (0,0,1), self.rotatex)

        return (case)


    def make_npth_pin(self, modelID):

        params = self.all_params[modelID]

        npthpin = params.npthpin
        #
        # Make dummy
        #
        case = None

        if npthpin == None:
            case = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).circle(0.001, False).extrude(0.001)
        else:
            for n in npthpin:
                t = n[0]
                x = n[1]
                y = n[2]
                d = n[3]
                d1 = n[4]
                l = n[5]
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(x, y).circle(d / 2.0 , False).extrude(0.0 - l)

                if case == None:
                    case = case1
                else:
                    case = case.union(case1)

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
        'L1',                   # Length 1
        'H',                    # Height
        'H1',                   # Height1
        'A1',                   # Body above PCB
        'pin1',                 # pin1 corner
        'pin',                  # pins
        'fuse',                  # fuse
        'npthpin',              # npthpin
        'npth_pin_color_key',   # NPTH Pin color
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'dest_dir_prefix'	    # Destination directory
    ])


    all_params = {

        #
        # https://www.schurter.com/en/datasheet/typ_OG__Holder__6.3x32.pdf
        # 
        'Schurter_0031-8002': Params(
            modelName = 'Fuseholder_Cylinder-6.3x32mm_Schurter_0031-8002_Horizontal_Open',    # Model name
            W = 41.00,                    # Width
            L = 15.00,                    # Length
            H = 07.5,                     # Height
            fuse = (6.3, 32.0),
            pin = [['rect', 0.0, 0.0, 1.1, 0.3, 4.0], ['rect', 37.5, 0.0, 1.1, 0.3, 4.0]],
            ),

        #
        # https://www.schurter.com/en/datasheet/typ_OGN.pdf
        # 
        'Schurter_0031_8201': Params(
            modelName = 'Fuseholder_Cylinder-5x20mm_Schurter_0031_8201_Horizontal_Open',    # Model name
            W = 22.5,                    # Width
            L = 09.6,                    # Length
            H = 11.5,                    # Height
            fuse = (5.0, 20.0),
            pin = [['rect', 0.0, 0.0, 1.1, 0.3, 4.0], ['rect', 22.5, 0.0, 1.1, 0.3, 4.0]],
            ),

        #
        # https://www.schurter.com/bundles/snceschurter/epim/_ProdPool_/newDS/en/typ_FAB.pdf
        # 
        'Schurter_FAB_0031_355x': Params(
            modelName = 'Fuseholder_Cylinder-5x20mm_Schurter_FAB_0031-355x_Horizontal_Closed',    # Model name
            W = 31.5,                    # Width
            L = 12.00,                   # Length
            H = 10.06,                   # Height
            L1 = 12.0,                   # Length 1
            fuse = (5.0, 20.0),
            pin = [['rect', 0.0, 0.0, 1.1, 0.3, 5.0], ['rect', 10.0, 0.0, 1.1, 0.3, 5.0]],
            ),
    }

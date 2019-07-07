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


import cq_parameters  # modules parameters
from cq_parameters import *

import math
from math import tan, cos, sin, radians, sqrt, atan

import cq_base_model  # modules parameters
from cq_base_model import *

class cq_parameters_Resonator_C26_LF():

    def __init__(self):
        x = 0


    def get_dest_3D_dir(self, modelName):
        for n in self.all_params:
            if n == modelName:
                return self.all_params[modelName].dest_dir_prefix


    def get_dest_file_name(self, modelName):
        for n in self.all_params:
            if n == modelName:
                return self.all_params[modelName].filename


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
        
        case_top = self.make_top(self.all_params[modelName])
        case = self.make_case(self.all_params[modelName])
        pins = self.make_pins(case, self.all_params[modelName])
        show(case_top)
        show(case)
        show(pins)
     
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
     
        body_top_color_key = self.all_params[modelName].body_top_color_key
        body_color_key = self.all_params[modelName].body_color_key
        pin_color_key = self.all_params[modelName].pin_color_key

        body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

        Color_Objects(Gui,objs[0],body_top_color)
        Color_Objects(Gui,objs[1],body_color)
        Color_Objects(Gui,objs[2],pin_color)

        col_body_top=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_body=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        
        material_substitutions={
            col_body_top[:-1]:body_top_color_key,
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pin_color_key,
        }
        
        expVRML.say(material_substitutions)
        while len(objs) > 1:
                FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
                del objs
                objs = GetListOfObjects(FreeCAD, doc)

        return material_substitutions
    
    def make_top(self, params):

        type = params.type                  # body type
        L = params.L                        # top length
        W = params.W                        # top length
        A1 = params.A1                      # Body distance to PCB
        PBD = params.PBD                    # Distance from pin hole to body

        ph = params.p_hole                  # Distance between pin hole
        ps = params.p_split                 # distance between legs
        pl = params.p_length                # pin length
        pd = params.p_diam                  # pin diameter

        rotation = params.rotation          # Rotation if required

        FreeCAD.Console.PrintMessage('make_top ...\r\n')

        tt = 0.1
        tr = 0.15
        lb = L * tr
        
        top = cq.Workplane("XY").workplane(offset = tt).moveTo(0.0, 0.0).circle(W / 2.0, False).extrude(L * (1.0 - tt))
        top = top.faces(">Z").fillet(pd / 1.2)
        
        if (type == 1):
            top = top.rotate((0,0,0), (0,1,0), 90)
            top = top.rotate((0,0,0), (0,0,1), 270)
            top = top.translate((ph / 2.0, 0.0 - (PBD + tt), A1 + (W / 2.0)))
        
        if (type == 2):
            top = top.translate((ph / 2.0, 0.0, A1 + tt))
        
        if (rotation != 0):
            top = top.rotate((0,0,0), (0,0,1), rotation)

        return (top)


    def make_case(self, params):

        type = params.type                  # body type
        L = params.L                        # top length
        W = params.W                        # top length
        A1 = params.A1                      # Body distance to PCB
        PBD = params.PBD                    # Distance from pin hole to body
        
        ph = params.p_hole                  # Distance between pin hole
        ps = params.p_split                 # distance between legs
        pl = params.p_length                # pin length
        pd = params.p_diam                  # pin diameter

        rotation = params.rotation          # Rotation if required

        FreeCAD.Console.PrintMessage('make_case ...\r\n')

        tt = 0.1
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(W / 2.0, False).extrude(3.0 * tt)
        #

        if (type == 1):
            case = case.rotate((0,0,0), (0,1,0), 90)
            case = case.rotate((0,0,0), (0,0,1), 270)
            case = case.translate((ph / 2.0, 0.0 - PBD, A1 + (W / 2.0)))
        
        if (type == 2):
            case = case.translate((ph / 2.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)

    
    def make_pins(self, case, params):

        type = params.type                  # body type
        L = params.L                        # top length
        W = params.W                        # top length
        A1 = params.A1                      # Body distance to PCB
        PBD = params.PBD                    # Distance from pin hole to body
        
        ph = params.p_hole                  # Distance between pin hole
        ps = params.p_split                 # distance between legs
        pl = params.p_length                # pin length
        pd = params.p_diam                  # pin diameter

        rotation = params.rotation          # Rotation if required

        FreeCAD.Console.PrintMessage('make_pins ...\r\n')

        pins = None
        if (type == 1):
            tt = 0.1
            tr = 0.25
            lb = L * tr
            
            zbelow = -3.0 # negative value, length of pins below board level
            #
            r = 0.5
            h = A1 + (W / 1.8)
            arco = (1.0-sqrt(2.0)/2.0)*r # helper factor to create midpoints of profile radii

            aa = math.degrees(math.atan((PBD / 2.0) / (ps / 4.0)))
            
            path = (
                cq.Workplane("XZ")
                .lineTo(0, h - r - zbelow)
                .threePointArc((arco, h - arco - zbelow),(r , h - zbelow))
                .lineTo(3.4, h - zbelow)
                )
            pins = cq.Workplane("XY").circle(pd / 2.0).sweep(path).translate((0, 0, zbelow))
            pins = pins.rotate((0,0,0), (0,0,1), 0.0 - aa)
            pins = pins.faces("<Z").edges().fillet(pd / 4.0)

            
            path = (
                cq.Workplane("XZ")
                .lineTo(0, h - r - zbelow)
                .threePointArc((arco, h - arco - zbelow),(r , h - zbelow))
                .lineTo(3.4, h - zbelow)
                )
            pin = cq.Workplane("XY").circle(pd / 2.0).sweep(path).translate((0, 0, zbelow))
            pin = pin.rotate((0,0,0), (0,0,1), (0.0 - 180.0) + aa)
            pin = pin.translate((ph, 0.0, 0.0))
            pin = pin.faces("<Z").edges().fillet(pd / 4.0)
            
            pins = pins.union(pin)
            
        if (type == 2):
            path = (
                cq.Workplane("XZ")
                .lineTo(0.0, 3.0)
                .lineTo((ph - ps) / 2.0, 3.0 + 1.0)
                .lineTo((ph - ps) / 2.0, 3.0 + 1.0 + A1 + 0.1)
                )
            pins = cq.Workplane("XY").circle(pd / 2.0).sweep(path).translate((0.0, 0.0, 0.0 - 3.0))

#            pins = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(0.0, 0.0).circle(pd / 2.2, False).extrude(0.0 - (3.0 + A1 + 0.1))
#            pins = pins.faces("<Z").edges().fillet(pd / 4.0)
            
            path = (
                cq.Workplane("XZ")
                .lineTo(0.0, 3.0)
                .lineTo(0.0 - ((ph - ps) / 2.0), 3.0 + 1.0)
                .lineTo(0.0 - ((ph - ps) / 2.0), 3.0 + 1.0 + A1 + 0.1)
                )
            pin = cq.Workplane("XY").circle(pd / 2.0).sweep(path).translate((ph, 0.0, 0.0 - 3.0))
            pin = pin.faces("<Z").edges().fillet(pd / 4.0)
            pins = pins.union(pin)
            
            
        if (rotation != 0):
            pins = pins.rotate((0,0,0), (0,0,1), rotation)

        return (pins)


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
        'type',		            # model type
        'filename',		        # file name
        'L',				    # Body length
        'W',			   	    # Body diameter
        'A1',			   	    # Body-board separation

        'PBD',                  # Distance from pin hole to body
        
        'p_hole',		        # Distance between pin hole
        'p_split',		        # Distance between pins
        'p_length',		        # Pin length
        'p_diam',		        # Pin width

        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])

    all_params = {

        'C26-LF_Horizontal': Params(
            #
            #
            # 
            type = 1,
            filename = 'Crystal_C26-LF_D2.1mm_L6.5mm_Horizontal',   # modelName
            L = 6.5,                # Top length
            W = 2.1,                # Top diameter
            A1 = 0.0,               # Body-board separation
            
            PBD = 2.0,              # Distance from pin hole to body
            
            p_hole = 1.9,           # Distance between pin hole
            p_split = 0.7,          # Distance between pins
            p_length = 10.0,        # Pin length
            p_diam = 0.3,           # Pin diameter

            body_top_color_key = 'metal aluminum',  # Top color
            body_color_key = 'brown body',          # Body color
            pin_color_key = 'metal silver',         # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'C26-LF_Horizontal_1EP_1': Params(
            #
            #
            # 
            type = 1,
            filename = 'Crystal_C26-LF_D2.1mm_L6.5mm_Horizontal_1EP_style1',   # modelName
            L = 6.5,                # Top length
            W = 2.1,                # Top diameter
            A1 = 0.0,               # Body-board separation
            
            PBD = 2.0,              # Distance from pin hole to body
            
            p_hole = 1.9,           # Distance between pin hole
            p_split = 0.7,          # Distance between pins
            p_length = 10.0,        # Pin length
            p_diam = 0.3,           # Pin diameter

            body_top_color_key = 'metal aluminum',  # Top color
            body_color_key = 'brown body',          # Body color
            pin_color_key = 'metal silver',         # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'C26-LF_Horizontal_1EP_2': Params(
            #
            #
            # 
            type = 1,
            filename = 'Crystal_C26-LF_D2.1mm_L6.5mm_Horizontal_1EP_style2',   # modelName
            L = 6.5,                # Top length
            W = 2.1,                # Top diameter
            A1 = 0.0,               # Body-board separation
            
            PBD = 2.0,              # Distance from pin hole to body
            
            p_hole = 1.9,           # Distance between pin hole
            p_split = 0.7,          # Distance between pins
            p_length = 10.0,        # Pin length
            p_diam = 0.3,           # Pin diameter

            body_top_color_key = 'metal aluminum',  # Top color
            body_color_key = 'brown body',          # Body color
            pin_color_key = 'metal silver',         # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'C26-LF_Vertical': Params(
            #
            #
            # 
            type = 2,
            filename = 'Crystal_C26-LF_D2.1mm_L6.5mm_Vertical',   # modelName
            L = 6.5,                # Top length
            W = 2.1,                # Top diameter
            A1 = 2.0,               # Body-board separation
            
            PBD = 2.0,              # Distance from pin hole to body
            
            p_hole = 1.9,           # Distance between pin hole
            p_split = 0.7,          # Distance between pins
            p_length = 10.0,        # Pin length
            p_diam = 0.3,           # Pin diameter

            body_top_color_key = 'metal aluminum',  # Top color
            body_color_key = 'brown body',          # Body color
            pin_color_key = 'metal silver',         # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

    }
        
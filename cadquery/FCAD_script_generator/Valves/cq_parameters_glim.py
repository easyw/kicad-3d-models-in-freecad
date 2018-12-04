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

class cq_parameters_glim():

    def __init__(self):
        x = 0

        
    def get_dest_3D_dir(self):
        return 'Valve.3dshapes'

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
        
        FreeCAD.Console.PrintMessage('\r\make_3D_model glim...\r\n')
        
        destination_dir = self.get_dest_3D_dir()
        
        case_top = self.make_case_top(self.all_params[modelName])
        case = self.make_case(self.all_params[modelName])
        pins = self.make_pins(self.all_params[modelName])
        npth_pins = self.make_npth_pins(self.all_params[modelName])
        show(case_top)
        show(case)
        show(pins)
        show(npth_pins)
     
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
     
        body_top_color_key = self.all_params[modelName].body_top_color_key
        body_color_key = self.all_params[modelName].body_color_key
        pin_color_key = self.all_params[modelName].pin_color_key
        npth_pin_color_key = self.all_params[modelName].npth_pin_color_key

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
    
    def make_case_top(self, params):

        D = params.D                # package length
        E = params.E                # body overall width
        H = params.H                # body overall height
        A1 = params.A1              # Body seperation height
        b = params.b                # pin diameter or pad size
        ph = params.ph              # pin length
        rotation = params.rotation  # rotation if required
        pin = params.pin            # pin/pad cordinates
        npthhole = params.npthhole  # NPTH holes
        center = params.center      # Body center

        As = A1
        Es = E
        Ds = D
        Hs = A1+H

        dd = 1.5
        At = As + dd
        Et = Es - (2.0 * dd)
        Dt = Ds - (2.0 * dd)
        Ht = Hs - (2.0 * dd)
        Dt = D - (2.0 * dd)
        fft = Dt / 2.1
        case1 = cq.Workplane("XY").workplane(offset=At).moveTo(center[0], center[1]).rect(Et, Dt).extrude(Ht)
        case1 = case1.faces("<X").edges(">Y").fillet(fft)
        case1 = case1.faces("<X").edges("<Y").fillet(fft)
        case1 = case1.faces(">X").edges(">Y").fillet(fft)
        case1 = case1.faces(">X").edges("<Y").fillet(fft)
        case1 = case1.faces(">Z").fillet(fft)
        case1 = case1.faces("<Z").fillet(fft)
        
        return (case1)


    def make_case(self, params):

        D = params.D                # package length
        E = params.E                # body overall width
        H = params.H                # body overall height
        A1 = params.A1              # package height
        pin = params.pin            # Pins
        rotation = params.rotation  # Rotation if required
        center = params.center      # Body center
        #
        #
        #

        As = A1
        Es = E
        Ds = D
        Hs = A1+H
        ff = Ds / 2.1
        case = cq.Workplane("XY").workplane(offset=As).moveTo(center[0], center[1]).rect(Es, Ds).extrude(Hs)
        case = case.faces("<X").edges(">Y").fillet(ff)
        case = case.faces("<X").edges("<Y").fillet(ff)
        case = case.faces(">X").edges(">Y").fillet(ff)
        case = case.faces(">X").edges("<Y").fillet(ff)
        case = case.faces(">Z").fillet(ff)
        case = case.faces("<Z").fillet(ff)

        
        dd = 0.1
        At = As + dd
        Et = Es - (2.0 * dd)
        Dt = Ds - (2.0 * dd)
        Ht = Hs - (2.0 * dd)
        Dt = D - (2.0 * dd)
        fft = Dt / 2.1
        case1 = cq.Workplane("XY").workplane(offset=At).moveTo(center[0], center[1]).rect(Et, Dt).extrude(Ht)
        case1 = case1.faces("<X").edges(">Y").fillet(fft)
        case1 = case1.faces("<X").edges("<Y").fillet(fft)
        case1 = case1.faces(">X").edges(">Y").fillet(fft)
        case1 = case1.faces(">X").edges("<Y").fillet(fft)
        case1 = case1.faces(">Z").fillet(fft)
        case1 = case1.faces("<Z").fillet(fft)
        
        case = case.cut(case1)
        
        
    #    case = case.faces("<Y").shell(0.1)

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_pins(self, params):

        D = params.D                # package length
        H = params.H                # body overall height
        A1 = params.A1              # Body seperation height
        b = params.b                # pin diameter or pad size
        ph = params.ph              # pin length
        rotation = params.rotation  # rotation if required
        pin = params.pin            # pin/pad cordinates
        npthhole = params.npthhole  # NPTH holes
        center = params.center      # Body center
        
        FreeCAD.Console.PrintMessage('make_pins_ECC \r\n')

        p = pin[0]
        pins = cq.Workplane("XY").workplane(offset=A1 + 1.0 + (H / 2.0)).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0 + (H / 2.0)))
        pins = pins.faces("<Z").fillet(b / 5.0)
        
        for i in range(1, len(pin)):
            p = pin[i]
            pint = cq.Workplane("XY").workplane(offset=A1 + 1.0 + (H / 2.0)).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0 + (H / 2.0)))
            pint = pint.faces("<Z").fillet(b / 5.0)
            pins = pins.union(pint)

        if (rotation != 0):
            pins = pins.rotate((0,0,0), (0,0,1), rotation)

        return (pins)


    def make_npth_pins(self, params):

        D = params.D                # package length
        E = params.E                # body overall width
        H = params.H                # body overall height
        A1 = params.A1              # Body seperation height
        b = params.b                # pin diameter or pad size
        ph = params.ph              # pin length
        rotation = params.rotation  # rotation if required
        pin = params.pin            # pin/pad cordinates
        npthhole = params.npthhole  # NPTH holes
        center = params.center      # Body center

        p = pin[0]
        pins = cq.Workplane("XY").workplane(offset=A1).moveTo(p[0], -p[1]).circle(0.05, False).extrude(0 - (A1 + 0.1))

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
        'modelName',		    # modelName
        'D',				    # Body width/diameter
        'E',			   	    # Body length
        'H',			   	    # Body height
        'A1',				    # Body PCB seperation
        'b',				    # pin width
        'center',               # Body center
        'npthhole',             # NPTH holes
        'ph',                   # Pin length
        'pin',		            # Pins
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {

        'Valve_Glimm': Params(
            #
            # Valve
            # This model have been auto generated based on the foot print file
            # A number of parameters have been fixed or guessed, such as A2
            # 
            # The foot print that uses this 3D model is Valve_Glimm.kicad_mod
            # 
            modelName = 'Valve_Glimm',  # modelName
            D = 5.08,                   # Body width/diameter
            E = 10.16,                  # Body length
            H = 10.00,                  # Body height
            A1 = 0.03,                  # Body-board separation
            b = 0.6,                    # Pin width
            center = (2.54, 0.0),         # Body center
            npthhole = None,            # NPTH hole [(x, y, diameter, length)] or None
            ph = 4.0,                   # Pin length
            pin = [(0.0, 0.0), (5.08, 0.0) ],       # Pins
            body_top_color_key = 'red body',        # Top color
            body_color_key = 'glass_grey',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

    }
        
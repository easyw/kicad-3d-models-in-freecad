#!/usr/bin/python
# -*- coding: utf-8 -*-
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


class cq_parameters_tht_generic_round():

    def __init__(self):
        x = 0

        
    def get_dest_3D_dir(self):
        return 'Buzzer_Beeper.3dshapes'

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

        
        destination_dir = self.get_dest_3D_dir()
        
        case_top = self.make_top(self.all_params[modelName])
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
    
    def make_top(self, params):

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
        x = center[0]
        y = center[1]
        case = cq.Workplane("XY").workplane(offset=A1 + (H / 5.0)).moveTo(x, y).circle(1.0, False).extrude(H - (H / 5.0) - 0.2)
#        case = case.faces("<Z").shell(0.3)

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


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
        x = center[0]
        y = center[1]

        case = cq.Workplane("XY").workplane(offset=A1).moveTo(x, y).circle(D / 2.0, False).extrude(H)
        case = case.faces(">Z").edges(">Y").fillet(D / 8.1)
        case = case.faces("<Z").edges(">Y").fillet(D / 40.0)

        case1 = cq.Workplane("XY").workplane(offset=A1 + (H / 5.0)).moveTo(x, y).circle(1.0, False).extrude(H + (3.0 * (H / 5.0)))
        case = case.cut(case1)
#        case = case.faces("<Z").shell(0.3)

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
        center = params.center      # Body center
        
        p = pin[0]
        pins = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0))
        pins = pins.faces("<Z").fillet(b / 5.0)
        
        for i in range(1, len(pin)):
            p = pin[i]
            pint = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0))
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
        npthhole = params.npthhole  # npth hole
        rotation = params.rotation  # rotation if required
        pin = params.pin            # pin/pad cordinates
        center = params.center      # Body center

        FreeCAD.Console.PrintMessage('make_npth_pins \r\n')

        #
        # Make a dummy one
        #
        p = pin[0]
        pins = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(b / 6.0, False).extrude(0 - 0.1)
        
        if npthhole != None:
            if len(npthhole) > 0:
                p = npthhole[0]
                b = p[2]
                ph = p[3]
                pint = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 0.1))
                pint = pint.faces("<Z").fillet(b / 5.0)
                pins = pins.union(pint)

                for i in range(1, len(npthhole)):
                    p = npthhole[i]
                    b = p[2]
                    ph = p[3]
                    pint = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0))
                    pint = pint.faces("<Z").fillet(b / 5.0)
                    pins = pins.union(pint)


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
        'serie',			    # The component serie
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {

        'Buzzer_12x9.5RM7.6': Params(
            #
            # Valve
            # This model have been auto generated based on the foot print file
            # A number of parameters have been fixed or guessed, such as A2
            # 
            # The foot print that uses this 3D model is Buzzer_12x9.5RM7.6.kicad_mod
            # 
            modelName = 'Buzzer_12x9.5RM7.6',   # modelName
            D = 12.00,                  # Body width/diameter
            H = 09.50,                  # Body height
            A1 = 0.03,                  # Body-board separation
            b = 0.90,                   # Pin diameter
            center = (3.80, 0.00),      # Body center
            npthhole = None,            # NPTH hole [(x, y, length)]
            ph = 3.0,                   # Pin length
            pin = [(0.0, 0.0), (7.60, 0.00)],          # Pins
            body_top_color_key = 'orange body',   # Top color
            body_color_key = 'black body',        # Body color
            pin_color_key = 'metal grey pins',  # Pin color
            npth_pin_color_key = 'grey body',   # NPTH Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = '../Buzzer_Beeper.3dshapes',      # destination directory
            ),

        'Buzzer_15x7.5RM7.6': Params(
            #
            # Valve
            # This model have been auto generated based on the foot print file
            # A number of parameters have been fixed or guessed, such as A2
            # 
            # The foot print that uses this 3D model is Buzzer_15x7.5RM7.6.kicad_mod
            # 
            modelName = 'Buzzer_15x7.5RM7.6',   # modelName
            D = 15.00,                  # Body width/diameter
            H = 07.50,                  # Body height
            A1 = 0.03,                  # Body-board separation
            b = 0.90,                   # Pin diameter
            center = (3.80, 0.00),      # Body center
            npthhole = None,            # NPTH hole [(x, y, length)]
            ph = 3.0,                   # Pin length
            pin = [(0.0, 0.0), (7.60, 0.00)],          # Pins
            body_top_color_key = 'orange body',   # Top color
            body_color_key = 'black body',        # Body color
            pin_color_key = 'metal grey pins',  # Pin color
            npth_pin_color_key = 'grey body',   # NPTH Pin color
            rotation = 0,                       # Rotation if required
            dest_dir_prefix = '../Buzzer_Beeper.3dshapes',      # destination directory
            ),

    }
        
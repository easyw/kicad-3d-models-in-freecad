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

class cq_parameters_tube_CK6418():

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

        W = params.W                        # package length
        E = params.E                        # body width
        H = params.H                        # body overall height
        A1 = params.A1                      # package height
        npth_pin = params.npth_pin          # NPTH holes
        pin_type = params.pin_type          # Pin type
        pin_number = params.pin_number      # Number of pins
        pin_split = params.pin_split        # Pin arc
        rotation = params.rotation          # Rotation if required

        #
        # Calculate center
        # pin 1 always in origo
        #
        origo_x = round (pin_number / 2, 1) * pin_split
        origo_y = 0

        ff = W / 8.0
        
        B = H * 0.95
        #
        case=cq.Workplane("XY").workplane(offset=A1 + B).moveTo(origo_x, 0 - origo_y).circle(W / 8.0, False).extrude(H - B)
        case = case.faces(">Z").edges(">Y").fillet(W / 8.3)

#        case = case.faces("<Z").shell(0.1)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case(self, params):

        W = params.W                        # package length
        E = params.E                        # body width
        H = params.H                        # body overall height
        A1 = params.A1                      # package height
        npth_pin = params.npth_pin          # NPTH holes
        pin_type = params.pin_type          # Pin type
        pin_number = params.pin_number      # Number of pins
        pin_split = params.pin_split        # Pin arc
        rotation = params.rotation          # Rotation if required

        #
        # Calculate center
        # pin 1 always in origo
        #
        origo_x = round (pin_number / 2, 1) * pin_split
        origo_y = 0
        
        ffs = W / 2.2
        B = H * 0.95
        #
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).rect(E, W).extrude(B)
        case = case.faces("<X").edges(">Y").fillet(ffs)
        case = case.faces("<X").edges("<Y").fillet(ffs)
        case = case.faces(">X").edges(">Y").fillet(ffs)
        case = case.faces(">X").edges("<Y").fillet(ffs)
        case = case.faces(">Z").fillet(ffs / 3.0)

        case = case.faces("<Z").shell(0.1)

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)

    
    def make_pins(self, params):

        W = params.W                        # package length
        E = params.E                        # body width
        H = params.H                        # body overall height
        A1 = params.A1                      # package height
        npth_pin = params.npth_pin          # NPTH holes
        pin_type = params.pin_type          # Pin type
        pin_number = params.pin_number      # Number of pins
        pin_split = params.pin_split        # Pin arc
        rotation = params.rotation          # Rotation if required


        origo_x = round (pin_number / 2, 1) * pin_split
        origo_y = 0

        tdx = E / pin_number        
        ty = 0
        tx = (origo_x - (W / 2.0)) + tdx
        
        sx = 0
        sy = 0
        dx = pin_split

        #
        # Pin 1
        pins = cq.Workplane("XY").workplane(offset=0).moveTo(sx, 0 - sy).circle(pin_type[1] / 2.0, False).extrude(0 - pin_type[2])
        pins = pins.faces("<Z").fillet(pin_type[1] / 2.2)
        pins = pins.faces(">Z").fillet(pin_type[1] / 2.2)
        pint = cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).circle(pin_type[1] / 2.0, False).extrude(A1 + 2)
        pint = pint.rotate((0,0,0), (0,1,0), 45)
        pint = pint.translate((sx, 0 - sy, 0 - (pin_type[1] / 2.2)))
        pins = pins.union(pint)
        #
        # Pin 2
        sx = sx + dx
        pint = cq.Workplane("XY").workplane(offset=0).moveTo(sx, 0 - sy).circle(pin_type[1] / 2.0, False).extrude(0 - pin_type[2])
        pint = pint.faces("<Z").fillet(pin_type[1] / 2.2)
        pint = pint.faces(">Z").fillet(pin_type[1] / 2.2)
        pins = pins.union(pint)
        pint = cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).circle(pin_type[1] / 2.0, False).extrude(A1 + 2)
        pint = pint.rotate((0,0,0), (0,1,0), 20)
        pint = pint.translate((sx, 0 - sy, 0 - (pin_type[1] / 2.7)))
        pins = pins.union(pint)
        #
        # Pin 3
        sx = sx + dx
        pint = cq.Workplane("XY").workplane(offset=0 - pin_type[2]).moveTo(sx, 0 - sy).circle(pin_type[1] / 2.0, False).extrude(pin_type[2] + A1)
        pint = pint.faces("<Z").fillet(pin_type[1] / 2.2)
        pins = pins.union(pint)
        #
        # Pin 4
        sx = sx + dx
        pint = cq.Workplane("XY").workplane(offset=0).moveTo(sx, 0 - sy).circle(pin_type[1] / 2.0, False).extrude(0 - pin_type[2])
        pint = pint.faces("<Z").fillet(pin_type[1] / 2.2)
        pint = pint.faces(">Z").fillet(pin_type[1] / 2.2)
        pins = pins.union(pint)
        pint = cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).circle(pin_type[1] / 2.0, False).extrude(A1 + 2)
        pint = pint.rotate((0,0,0), (0,1,0), -20)
        pint = pint.translate((sx, 0 - sy, 0 - (pin_type[1] / 2.7)))
        pins = pins.union(pint)
        #
        # Pin 5
        sx = sx + dx
        pint = cq.Workplane("XY").workplane(offset=0).moveTo(sx, 0 - sy).circle(pin_type[1] / 2.0, False).extrude(0 - pin_type[2])
        pint = pint.faces("<Z").fillet(pin_type[1] / 2.2)
        pint = pint.faces(">Z").fillet(pin_type[1] / 2.2)
        pins = pins.union(pint)
        pint = cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).circle(pin_type[1] / 2.0, False).extrude(A1 + 2)
        pint = pint.rotate((0,0,0), (0,1,0), -45)
        pint = pint.translate((sx, 0 - sy, 0 - (pin_type[1] / 2.7)))
        pins = pins.union(pint)
        
        if (rotation != 0):
            pins = pins.rotate((0,0,0), (0,0,1), rotation)

        return (pins)


    def make_npth_pins(self, params):

        W = params.W                        # package length
        E = params.E                        # body width
        H = params.H                        # body overall height
        A1 = params.A1                      # package height
        npth_pin = params.npth_pin          # NPTH holes
        pin_type = params.pin_type          # Pin type
        pin_number = params.pin_number      # Number of pins
        pin_split = params.pin_split        # Pin arc
        rotation = params.rotation          # Rotation if required

        ffs = W / 2.2
        origo_x = round (pin_number / 2, 1) * pin_split
        origo_y = 0
        
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).rect(E, W).extrude(0.1)
        case = case.faces("<X").edges(">Y").fillet(ffs)
        case = case.faces("<X").edges("<Y").fillet(ffs)
        case = case.faces(">X").edges(">Y").fillet(ffs)
        case = case.faces(">X").edges("<Y").fillet(ffs)

        pins = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo(origo_x, 0 - origo_y).circle((W / 2.0) - 0.5, False).extrude(A1 + 2.0)
        
        pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo((origo_x - (W / 2.0)) + 3.0, 0 - origo_y).circle(0.5, False).extrude((2.0 * H) / 3.0)
        pint = pint.faces(">Z").fillet(0.4)
        pins = pins.union(pint)
        #
        pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo((origo_x + (W / 2.0)) - 3.0, 0 - origo_y).circle(0.5, False).extrude((2.0 * H) / 3.0)
        pint = pint.faces(">Z").fillet(0.4)
        pins = pins.union(pint)
        #
        pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo(origo_x - 1.0, 0 - origo_y).circle(0.5, False).extrude((2.0 * H) / 3.0)
        pint = pint.faces(">Z").fillet(0.4)
        pins = pins.union(pint)
        #
        pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo(origo_x + 1.0, 0 - origo_y).circle(0.5, False).extrude((2.0 * H) / 3.0)
        pint = pint.faces(">Z").fillet(0.4)
        pins = pins.union(pint)
        #
        pint = cq.Workplane("XY").workplane(offset=A1 + (H / 6.0)).moveTo(origo_x, 0 - origo_y).rect(W * 0.8, W / 4.0).extrude(H / 3.0)
        pint = pint.faces(">Z").fillet(W / 20.0)
        pint = pint.faces("<Z").fillet(W / 20.0)
        pins = pins.union(pint)

        case = case.union(pins)
        
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
        'W',				    # Body length
        'E',			   	    # Body width
        'H',			   	    # Body height
        'A1',				    # Body PCB seperation
        'npth_pin',             # NPTH type
        'pin_type',             # Pin type
        'pin_number',           # Number of pins
        'pin_split',		    # Distance between pins
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {

        'Valve_Tube_CK6418': Params(
            #
            # https://frank.pocnet.net/sheets/084/c/CK6418.pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Tube_CK6418',   # modelName
            W = 5.969,                  # Body length
            E = 7.366,                  # Body width
            H = 31.75,                  # Body height
            A1 = 2.0,                   # Body-board separation
            npth_pin = None,            # NPTH hole [(x, y, length)]
            pin_type = ('round', 0.5, 3.0),  # Pin type, diameter, length
            pin_number = 5,             # Number of pins
            pin_split = 2.54,           # Distance between pins

            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'glass_grey',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

    }
        
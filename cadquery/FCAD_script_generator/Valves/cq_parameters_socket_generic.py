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


class cq_parameters_socket_generic():

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

        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        #
        # Calculate center
        # pin 1 always in origo
        #
        alpha_delta = 0 - ((pin_arc * math.pi) / 180.0)
        h = pin_diameter / 2.0
        origo_x = h * math.sin(alpha_delta / 2.0)
        origo_y = h * math.cos(alpha_delta / 2.0)

        case = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(origo_x, 0 - origo_y).circle(0.05, False).extrude(0.1)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case(self, params):

        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        pin_spigot = params.pin_spigot      # Spigot
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        #
        # Calculate center
        # pin 1 always in origo
        #
        alpha_delta = 0 - ((pin_arc * math.pi) / 180.0)
        h = pin_diameter / 2.0
        origo_dx = (h * math.sin(alpha_delta))
        origo_dy = (h * math.cos(alpha_delta))
        
        origo_x = 0 - origo_dx
        origo_y = origo_dy
        
        
        ffs = D / 12.0
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).circle(D / 2.0, False).extrude(H)
        #
        # Cut an arc in each "corners"
        # 
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x + (D / 2.0) + 2.0, 0 - origo_y).circle(3.0, False).extrude(H + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x - (D / 2.0) - 2.0, 0 - origo_y).circle(3.0, False).extrude(H + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - (origo_y + (D / 2.0) + 2.0)).circle(3.0, False).extrude(H + 0.2)
        case = case.cut(case1)
        #
#        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - (origo_y - (D / 2.0) - 2.0)).circle(3.0, False).extrude(H + 0.2)
#        case = case.cut(case1)
        #
        # make ring on the middle of the body
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(D / 2.0 + 2.0, False).extrude((H / 4.0))
        case2 = cq.Workplane("XY").workplane(offset=A1 - 1.0).moveTo(origo_x, 0 - origo_y).circle(D / 2.0 - 1.0, False).extrude(H + 3.0)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 + (4 * (H / 2.0)) / 3).moveTo(origo_x, 0 - origo_y).circle(D / 2.0 + 2.0, False).extrude((H / 4) + 2.0)
        case2 = cq.Workplane("XY").workplane(offset=A1 - 1.0).moveTo(origo_x, 0 - origo_y).circle(D / 2.0 - 1.0, False).extrude(H + 3.0)
        case1 = case1.cut(case2)
        case = case.cut(case1)

        case = case.faces("<Z").edges("<Y").fillet(ffs / 10.0)
        case = case.faces(">Z").edges("<Y").fillet(ffs / 10.0)
        
        alpha = alpha_delta
        for i in range(0, pin_number):
            x1 = (h * math.sin(alpha)) + origo_x
            y1 = (h * math.cos(alpha)) - origo_y
#            FreeCAD.Console.PrintMessage('x1: ' + str(round(x1, 2)) + '\r\n')
#            FreeCAD.Console.PrintMessage('y1: ' + str(round(y1, 2)) + '\r\n')
            pins = cq.Workplane("XY").workplane(offset=A1 + (H / 2.0)).moveTo(x1, y1).circle(pin_type[1], False).extrude(H + 1.0)
            case = case.cut(pins)
            alpha = alpha + alpha_delta

                
        if center_pin != None:
            if center_pin[0] == 'metal':
                pins = cq.Workplane("XY").workplane(offset=A1 + (H / 2.0)).moveTo(origo_x, origo_y).circle(center_pin[1], False).extrude(H + 1.0)
                case = case.cut(pins)
            
        if pin_spigot != None:
            pins = cq.Workplane("XY").workplane(offset=(A1 + H) - 2.0).moveTo(origo_x, origo_y).circle(pin_spigot / 2.0, False).extrude(3.0)
            case = case.cut(pins)
            pins = cq.Workplane("XY").workplane(offset=(A1 + H) - 2.0).moveTo(origo_x - (pin_spigot / 2.0), 0 - origo_y).rect(2.0, 2.0).extrude(3.0)
            case = case.cut(pins)

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

            
            
        return (case)

    
    def make_pins(self, params):


        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        #
        # Calculate center
        # pin 1 always in origo
        #
        alpha_delta = 0 - ((pin_arc * math.pi) / 180.0)
        h = pin_diameter / 2.0
        origo_dx = (h * math.sin(alpha_delta))
        origo_dy = (h * math.cos(alpha_delta))

        origo_x = 0 - origo_dx
        origo_y = origo_dy
        

        alpha = alpha_delta
        if pin_type[0] == 'round':
            x1 = (h * math.sin(alpha)) + origo_x;
            y1 = (h * math.cos(alpha)) - origo_y
            pins = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(0 - (0.1 + pin_type[2]))
            pins = pins.faces("<Z").fillet(pin_type[1] / 5.0)
            alpha = alpha + alpha_delta
            for i in range(1, pin_number):
                x1 = (h * math.sin(alpha)) + origo_x;
                y1 = (h * math.cos(alpha)) - origo_y
                pint = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(0 - (0.1 + pin_type[2]))
                pint = pint.faces("<Z").fillet(pin_type[1] / 5.0)
                pins = pins.union(pint)
                alpha = alpha + alpha_delta
                
        if center_pin != None:
            if center_pin[0] == 'metal':
                pint = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(origo_x, 0 - origo_y).circle(center_pin[1] / 2.0, False).extrude(0 - (0.1 + center_pin[2]))
                pint = pint.faces("<Z").fillet(pin_type[1] / 5.0)
                pins  = pins.union(pint)
                
        
        if (rotation != 0):
            pins = pins.rotate((0,0,0), (0,0,1), rotation)

        return (pins)


    def make_npth_pins(self, params):


        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        b = params.A1                       # Pin width
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        #
        # Calculate center
        # pin 1 always in origo
        #
        alpha_delta = 0 - ((pin_arc * math.pi) / 180.0)
        h = pin_diameter / 2.0
        origo_x = h * math.sin(alpha_delta / 2.0)
        origo_y = h * math.cos(alpha_delta / 2.0)

        case = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(origo_x, 0 - origo_y).circle(0.05, False).extrude(0.1)
        
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
        'D',				    # Body width/diameter
        'socket_H',			    # Body height
        'A1',				    # Body PCB seperation
        'pin_spigot',           # Spigot
        'npth_pin',             # NPTH holes
        'center_pin',           # Center pin
        'pin_type',             # Pin type, length
        'pin_number',           # Number of pins
        'pin',		            # Pins
        'pin_arc',		        # Arch between pins
        'pin_diameter',		    # Diameter of the cricle where pins are located
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {

        'Valve_Socket_Magnoval-B9D-D17.45mm_Pin': Params(
            #
            # https://en.wikipedia.org/wiki/Tube_socket
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket_Magnoval-B9D-D17.45mm_Pin',   # modelName
            D = 30.00,                  # Body width/diameter
            socket_H = 12.00,           # Body height
            A1 = 0.03,                  # Body-board separation
            pin_spigot = None,          # Spigot
            npth_pin = None,            # NPTH hole [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            pin_type = ('round', 1.27, 3.0),  # Pin type, diameter, length
            pin_number = 9,             # Number of pins
            pin_arc = 36.0,             # Arch between pins
            pin_diameter = 17.45,       # Diameter of the circle where pins are located
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Socket_Noval-B9A-D11.89mm_Pin': Params(
            #
            # https://en.wikipedia.org/wiki/Tube_socket
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket_Noval-B9A-D11.89mm_Pin',   # modelName
            D = 25.50,                  # Body width/diameter
            socket_H = 11.00,           # Body height
            A1 = 0.03,                  # Body-board separation
            pin_spigot = None,          # Spigot
            npth_pin = None,            # NPTH hole [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            pin_type = ('round', 1.016, 3.0),  # Pin type, diameter, length
            pin_number = 9,             # Number of pins
            pin_arc = 36.0,             # Arch between pins
            pin_diameter = 11.89,       # Diameter of the circle where pins are located
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Socket_Miniature-B7G-D09.53mm_Pin': Params(
            #
            # https://en.wikipedia.org/wiki/Tube_socket
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket_Miniature-B7G-D09.53mm_Pin',   # modelName
            D = 15.00,                  # Body width/diameter
            socket_H = 8.00,            # Body height
            A1 = 0.03,                  # Body-board separation
            pin_spigot = None,          # Spigot
            npth_pin = None,            # NPTH hole [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            pin_type = ('round', 1.016, 3.0),  # Pin type, diameter, length
            pin_number = 7,             # Number of pins
            pin_arc = 45.0,             # Arch between pins
            pin_diameter = 09.53,       # Diameter of the circle where pins are located
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Socket_Loctal-B9G-D21.00mm_Pin': Params(
            #
            # https://en.wikipedia.org/wiki/Tube_socket
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket-Loctal-B9G-D21.00mm_Pin',   # modelName
            D = 27.00,                  # Body width/diameter
            socket_H = 12.00,           # Body height
            A1 = 0.03,                  # Body-board separation
            pin_spigot = None,          # Spigot
            npth_pin = None,            # NPTH hole [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            pin_type = ('round', 1.3, 3.0),  # Pin type, diameter, length
            pin_number = 9,             # Number of pins
            pin_arc = 40.0,             # Arch between pins
            pin_diameter = 21.00,       # Diameter of the circle where pins are located
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Socket_Loctal-B8G-D17.45mm-Pin': Params(
            #
            # https://en.wikipedia.org/wiki/Tube_socket
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket_Loctal-B8G-D17.45mm-Pin',   # modelName
            D = 29.00,                  # Body width/diameter
            socket_H = 14.50,           # Body height
            A1 = 0.03,                  # Body-board separation
            npth_pin = None,            # NPTH pin [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            pin_type = ('round', 1.30, 3.0),   # Pin type, diameter, length
            pin_number = 8,             # Number of pins
            pin_arc = 45.0,             # Arch between pins
            pin_diameter = 17.45,       # Diameter of the circle where pins are located
            pin_spigot = 6.70,          # Spigot
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Socket_Decar-B10G-D11.89mm_Pin': Params(
            #
            # https://en.wikipedia.org/wiki/Tube_socket
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket_Decar-B10G-D11.89mm_Pin',   # modelName
            D = 17.00,                  # Body width/diameter
            socket_H = 08.00,           # Body height
            A1 = 0.03,                  # Body-board separation
            pin_spigot = None,          # Spigot
            npth_pin = None,            # NPTH pin [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            pin_type = ('round', 1.016, 3.0),   # Pin type, diameter, length
            pin_number = 9,             # Number of pins
            pin_arc = 36.0,             # Arch between pins
            pin_diameter = 11.89,       # Diameter of the circle where pins are located
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Socket_Octal-K8A-D17.45mm_Pin': Params(
            #
            # https://en.wikipedia.org/wiki/Tube_socket
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket_Octal-K8A-D17.45mm_Pin',   # modelName
            D = 29.00,                  # Body width/diameter
            socket_H = 14.50,           # Body height
            A1 = 0.03,                  # Body-board separation
            npth_pin = None,            # NPTH pin [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            pin_type = ('round', 2.36, 3.0),   # Pin type, diameter, length
            pin_number = 8,             # Number of pins
            pin_arc = 45.0,             # Arch between pins
            pin_diameter = 17.45,       # Diameter of the circle where pins are located
            pin_spigot = 7.80,          # Spigot
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),
    }
        
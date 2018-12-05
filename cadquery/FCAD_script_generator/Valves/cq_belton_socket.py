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


class cq_belton_socket():

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
        params = self.all_params[modelName]

        
        if params.serie == 'VT8-PT':
            case_top = self.make_case_top_VT8_PT(params)
            show(case_top)
            case = self.make_case_VT8_PT(params)
            show(case)
            pins = self.make_pins_VT8_PT(params)
            show(pins)
        
        if params.serie == 'VT9-PT':
            case_top = self.make_case_top(params)
            show(case_top)
            case = self.make_case_VT9_PT(params)
            show(case)
            pins = self.make_pins_VT9_PT(params)
            show(pins)
        
        if params.serie == 'VT9-PT-C':
            case_top = self.make_case_top_VT9_PT_C(params)
            show(case_top)
            case = self.make_case_VT9_PT(params)
            show(case)
            pins = self.make_pins_VT9_PT(params)
            show(pins)
            
        npth_pins = self.make_npth_pins(params)
        show(npth_pins)
     
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
     
        body_top_color_key = params.body_top_color_key
        body_color_key = params.body_color_key
        pin_color_key = params.pin_color_key
        npth_pin_color_key = params.npth_pin_color_key

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

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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

        # Dummy
        case = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(origo_x, 0 - origo_y).circle(0.05, False).extrude(0.1)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)
    
    def make_case_top_VT8_PT(self, params):

        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        sadle = params.sadle                # "npth hole 1 x-pos, y-pos, diameter", "npth hole 2 x-pos, y-pos, diameter", width, length of flange, rotation in degree of flange
        sadle_hole = params.sadle_hole      # sadle hole1 x pos, sadle hole1 diameter, sadle hole2 x pos, sadle hole2 diameter 
        sadle_shield = params.sadle_shield  #
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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
        #
        cq_par = cq_parameters_help()
        top = cq_par.create_sadle(origo_x, origo_y, A1, D, sadle, sadle_hole, rotation)
        #

        return (top)
    
    def make_case_top_VT9_PT_C(self, params):

        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        sadle = params.sadle                # "npth hole 1 x-pos, y-pos, diameter", "npth hole 2 x-pos, y-pos, diameter", width, length of flange, rotation in degree of flange
        sadle_hole = params.sadle_hole      # sadle hole1 x pos, sadle hole1 diameter, sadle hole2 x pos, sadle hole2 diameter 
        sadle_shield = params.sadle_shield  #
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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
        #
        cq_par = cq_parameters_help()
        case = cq_par.create_sadle(origo_x, origo_y, A1, D, sadle, sadle_hole, rotation)
        case1 = cq_par.create_sadle_shield(origo_x, origo_y, A1, sadle, sadle_hole, sadle_shield, rotation)
        case = case.union(case1)
        #
        sadle_z = sadle[0]
        sadle_w = sadle[1]
        sadle_r1 = sadle[2] / 2.0
        sadle_x = sadle[3]
        sadle_r2 = sadle[4] / 2.0
        sadle_a = sadle[5]
        sadle_h = 0.2
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 + sadle_z - 6.6).moveTo(sadle_x, 0).circle(1.5, False).extrude(6.6)
        case1 = case1.rotate((0,0,0), (0,0,1), sadle_a)
        case1 = case1.translate((origo_x, 0.0 - origo_y, 0.0))
        case = case.union(case1)
        
        case1 = cq.Workplane("XY").workplane(offset=A1 + sadle_z - 6.6).moveTo(sadle_x, 0).circle(0.5, False).extrude(-3.0)
        case1 = case1.rotate((0,0,0), (0,0,1), sadle_a)
        case1 = case1.translate((origo_x, 0.0 - origo_y, 0.0))
        case = case.union(case1)

        return (case)


    def make_case_VT8_PT(self, params):

        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        pin_top_diameter = params.pin_top_diameter  # Diameter of pin hole on top
        pin_spigot = params.pin_spigot      # Spigot
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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
        
        cq_par = cq_parameters_help()
        case = cq_par.make_body_round(origo_x, origo_y, A1, D, pin_number, pin_type, pin_spigot, pin_top_diameter, H, alpha_delta, rotation)
        
        return (case)


    def make_case_VT9_PT(self, params):

        D = params.D                        # package length
        H = params.socket_H                 # body overall height
        A1 = params.A1                      # package height
        pin_top_diameter = params.pin_top_diameter  # Diameter of pin hole on top
        pin_spigot = params.pin_spigot      # Spigot
        npth_pin = params.npth_pin          # NPTH hole [(x, y, length)]
        center_pin = params.center_pin      # center pin ['type', diameter length)]
        pin_type = params.pin_type          # Pin type, length
        pin_number = params.pin_number      # Number of pins
        pin_arc = params.pin_arc            # Arch between pins
        pin_diameter = params.pin_diameter  # Diameter of the cricle where pins are located
        rotation = params.rotation          # Rotation if required

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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
        
        cq_par = cq_parameters_help()
        case = cq_par.make_body_with_ring_with_cut(origo_x, origo_y, A1, D, pin_number, pin_type, pin_spigot, pin_top_diameter, H, alpha_delta, rotation)
        
        return (case)

    
    def make_pins_VT8_PT(self, params):


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

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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
        
        cq_par = cq_parameters_help()
        pins = cq_par.create_pins(origo_x, origo_y, A1, pin_number, pin_type, center_pin, h, alpha_delta, rotation)
        
        return (pins)

    
    def make_pins_VT9_PT(self, params):


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

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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
        
        cq_par = cq_parameters_help()
        pins = cq_par.create_pins(origo_x, origo_y, A1, pin_number, pin_type, center_pin, h, alpha_delta, rotation)
        
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

        if len(pin_type) > 2:
            A1 = A1 + pin_type[3]
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

        # Dummy
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
        'flange',               # Flange paramters
        'sadle',                # Sadle paramters
        'sadle_hole',           # Sadle hole paramters
        'sadle_shield',         # Sadle shield
        'sadle_pcb_hole',       # Sadle pcb hole
        'pin_top_diameter',     # Diameter of the pin holes ontop
        'pin_spigot',           # Spigot
        'npth_pin',             # NPTH holes
        'center_pin',           # Center pin
        'pin_type',             # Pin type, length
        'pin_number',           # Number of pins
        'pin',		            # Pins
        'pin_arc',		        # Arch between pins
        'pin_diameter',		    # Diameter of the cricle where pins are located
        'serie',		        # The serie of the socket
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {


        'Valve_Noval-B9A_Belton-VT9-PT_Socket': Params(
            #
            # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Noval-B9A_Belton-VT9-PT_Socket',   # modelName
            D = 22.80,                  # Body width/diameter
            socket_H = 08.50,           # Body height
            A1 = 0.03,                  # Body-board separation
            sadle = None,               # Sadle z pos, length, width, xpos r2, diameter r2, rotation
            sadle_hole = None,          # Sadle hole1 x pos, sadle hole1 diameter, sadle hole2 x pos, sadle hole2 diameter 
            sadle_shield = None,        # Sadle shield diameter, height
            sadle_pcb_hole = None,      # Sadle shield diameter, height
            pin_top_diameter = (11.90, 1.016),   # Diameter of the pin holes ontop
            pin_spigot = ('round', 3.5, 6.0),          # Spigot in the middle on the top of the socket
            npth_pin = None,            # NPTH hole [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            #
            pin_type = ('roundtap', 1.8, 0.2, 3.5, 2.6, 3.0, 1.5),  # Pin type, hole diameter, pin thickness upper partlength, upper part width, lower part length, lower part width
            pin_number = 9,             # Number of pins
            pin_arc = 36.0,             # Arch between pins
            pin_diameter = 21.00,       # Diameter of the circle where pins are located
            serie = 'VT9-PT',            # The serie of the socket
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'green body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Noval-B9A_Belton-VT9-PT-C_Socket': Params(
            #
            # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Noval-B9A_Belton-VT9-PT-C_Socket',   # modelName
            D = 23.80,                  # Body width/diameter
            socket_H = 08.50,           # Body height
            A1 = 0.03,                  # Body-board separation
            sadle = [6.6, 35.5, 26.5, 14.25, 8.0, 72.0],  # Sadle z pos, length, width, xpos r2, diameter r2, rotation
            sadle_hole = [(-14.25, 3.3)],               # Sadle hole1 x pos, sadle hole1 diameter, sadle hole2 x pos, sadle hole2 diameter 
            sadle_shield = [23.8, 17.6],                # Sadle shield diameter, height
            sadle_pcb_hole = [('pad', 14.25, 1.3), ('npth', -14.25, 3.3)],  # Sadle shield diameter, height
            #
            pin_top_diameter = (11.90, 1.016),           # Diameter of the pin holes ontop
            pin_spigot = ('round', 3.5, 6.0),   # Spigot in the middle on the top of the socket
            npth_pin = None,                    # NPTH hole [(x, y, length)]
            center_pin = None,                  # Center pin ('type', diameter, length)
            #
            pin_type = ('roundtap', 1.8, 0.2, 3.5, 2.6, 3.0, 1.5),  # Pin type, hole diameter, pin thickness upper partlength, upper part width, lower part length, lower part width
            pin_number = 9,             # Number of pins
            pin_arc = 36.0,             # Arch between pins
            pin_diameter = 21.00,       # Diameter of the circle where pins are located
            serie = 'VT9-PT-C',         # The serie of the socket
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'green body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Octal-K8A_Belton-VT8-PT_Socket': Params(
            #
            # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Octal-K8A_Belton-VT8-PT_Socket',   # modelName
            D = 30.00,                  # Body width/diameter
            socket_H = 14.50,           # Body height
            A1 = 0.03,                  # Body-board separation
            sadle = [13.50, 50.0, 32.00, 20.00, 10.0, 72.0],    # Sadle z pos, length, width, xpos r2, diameter r2, rotation
            sadle_hole = [(-20.00, 3.5), (20.00, 3.5)],         # Sadle hole1 x pos, sadle hole1 diameter, sadle hole2 x pos, sadle hole2 diameter 
            sadle_shield = None,        # Sadle shield diameter, height
            sadle_pcb_hole = [('npth', -20.00, 3.5), ('npth', 20.00, 3.5)],  # Sadle shield diameter, height
            pin_top_diameter = (17.50, 2.36),   # Diameter of the pin holes ontop
            pin_spigot = ('tap', 3.5, 6.0, 2.0),          # Spigot in the middle on the top of the socket
            npth_pin = None,            # NPTH hole [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            #
            pin_type = ('roundtap', 1.6, 0.2, 3.5, 2.6, 17.0, 1.5),  # Pin type, hole diameter, pin thickness upper partlength, upper part width, lower part length, lower part width
            pin_number = 8,             # Number of pins
            pin_arc = 45.0,             # Arch between pins
            pin_diameter = 17.20,       # Diameter of the circle where pins are located
            serie = 'VT8-PT',           # The serie of the socket
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'green body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),

        'Valve_Octal-K8A_Belton-VT8-PTS-B_Socket': Params(
            #
            # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Octal-K8A_Belton-VT8-PTS-B_Socket',   # modelName
            D = 30.00,                  # Body width/diameter
            socket_H = 14.50,           # Body height
            A1 = 0.03,                  # Body-board separation
            sadle = [13.50, 50.0, 32.00, 19.00, 11.0, 72.0],    # Sadle z pos, length, width, xpos r2, diameter r2, rotation
            sadle_hole = [(-19.00, 2.9), (19.00, 2.9)],         # Sadle hole1 x pos, sadle hole1 diameter, sadle hole2 x pos, sadle hole2 diameter 
            sadle_shield = None,        # Sadle shield diameter, height
            sadle_pcb_hole = [('npth', -19.00, 2.9), ('npth', -19.00, 2.9)],  # Sadle shield diameter, height
            pin_top_diameter = (17.50, 2.36),   # Diameter of the pin holes ontop
            pin_spigot = ('tap', 3.5, 6.0, 2.0),          # Spigot in the middle on the top of the socket
            npth_pin = None,            # NPTH hole [(x, y, length)]
            center_pin = None,          # Center pin ('type', diameter, length)
            #
            pin_type = ('roundtap', 1.6, 0.2, 3.5, 2.6, 3.0, 1.5),  # Pin type, hole diameter, pin thickness upper partlength, upper part width, lower part length, lower part width
            pin_number = 8,             # Number of pins
            pin_arc = 45.0,             # Arch between pins
            pin_diameter = 17.20,       # Diameter of the circle where pins are located
            serie = 'VT8-PT',           # The serie of the socket
            
            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'green body',          # Body color
            pin_color_key = 'metal grey pins',      # Pin color
            npth_pin_color_key = 'grey body',       # NPTH Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = '../Valve.3dshapes',  # destination directory
            ),
    }
        
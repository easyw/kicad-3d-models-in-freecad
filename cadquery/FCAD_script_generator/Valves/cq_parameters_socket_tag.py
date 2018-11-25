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


class cq_parameters_socket_tag():

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

        case_top = self.make_case_top(params)
        show(case_top)
        
        if params.serie == 'VT9-PT':
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
        
        
        ffs = D / 70.0
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).circle(D / 2.0, False).extrude(H)
        #
        # Make ring on the middle of the body
        #
        TT = 18.50
        F1 = (H - 2.0) / 2.0
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0 + 6.0, False).extrude(F1 + 0.1)
        case2 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0, False).extrude(F1 + 0.1)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 + F1 + 2.0).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0 + 6.0, False).extrude(H)
        case2 = cq.Workplane("XY").workplane(offset=A1 + F1 + 2.0).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0, False).extrude(H)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        
        #
        # Round bottom
        #
        case = case.faces("<Z").fillet(ffs)
        #
        # Cut the edges of the socket
        #
        tv = 20
        ti = ((D - TT) / 2.0) + 0.2
        ta = 0 - ((tv * math.pi) / 180.0)
        th = (TT / 2.0) + (ti / 2.0)
        tdx = (th * math.sin(ta))
        tdy = (th * math.cos(ta))

        ttx = origo_x + tdx
        tty = origo_y + tdy

        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(0,0).rect(D, ti).extrude(H + 0.2)
        case1 = case1.rotate((0,0,0), (0,0,1), 360 - tv)
        case1 = case1.translate((ttx, 0 - tty, 0))
        case = case.cut(case1)
        #
        tv = tv + 180
        ti = ((D - TT) / 2.0) + 0.2
        ta = 0 - ((tv * math.pi) / 180.0)
        th = (TT / 2.0) + (ti / 2.0)
        tdx = (th * math.sin(ta))
        tdy = (th * math.cos(ta))

        ttx = origo_x + tdx
        tty = origo_y + tdy

        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(0,0).rect(D, ti).extrude(H + 0.2)
        case1 = case1.rotate((0,0,0), (0,0,1), 360 - tv)
        case1 = case1.translate((ttx, 0 - tty, 0))
        case = case.cut(case1)
        
        if pin_spigot != None:
            if pin_spigot[0] == 'round':
                pins = cq.Workplane("XY").workplane(offset=A1 + (H / 4)).moveTo(origo_x, 0 - origo_y).circle(pin_spigot[1] / 2.0, False).extrude(H)
                case = case.cut(pins)
                pins = cq.Workplane("XY").workplane(offset=A1 + ((3 * H) / 4)).moveTo(origo_x, 0 - origo_y).circle(pin_spigot[2] / 2.0, False).extrude(H)
                case = case.cut(pins)

        h = pin_top_diameter / 2.0
        alpha = alpha_delta
        x1 = (h * math.sin(alpha)) + origo_x
        y1 = (h * math.cos(alpha)) - origo_y
        pins = cq.Workplane("XY").workplane(offset=A1 + (H / 2.0)).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(H)
        case = case.cut(pins)
        alpha = alpha + alpha_delta
        for i in range(1, pin_number):
            x1 = (h * math.sin(alpha)) + origo_x
            y1 = (h * math.cos(alpha)) - origo_y
            pint = cq.Workplane("XY").workplane(offset=A1 + (H / 2.0)).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(H)
            case = case.cut(pint)
            alpha = alpha + alpha_delta

        #
        # Round top
        #
        case = case.faces(">Z").fillet(ffs)

        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

            
            
        return (case)

    
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
        
        alpha = alpha_delta
        if pin_type[0] == 'round':
            x1 = (h * math.sin(alpha)) + origo_x
            y1 = (h * math.cos(alpha)) - origo_y
            pins = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(0 - (0.1 + pin_type[2]))
            pins = pins.faces("<Z").fillet(pin_type[1] / 5.0)
            alpha = alpha + alpha_delta
            for i in range(1, pin_number):
                x1 = (h * math.sin(alpha)) + origo_x
                y1 = (h * math.cos(alpha)) - origo_y
                pint = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(0 - (0.1 + pin_type[2]))
                pint = pint.faces("<Z").fillet(pin_type[1] / 5.0)
                pins = pins.union(pint)
                alpha = alpha + alpha_delta
                

        alpha = alpha_delta
        if pin_type[0] == 'roundtap':
            xx = (h * math.sin(alpha)) + origo_x
            yy = (h * math.cos(alpha)) - origo_y

            x1 = (pin_type[4] / 2.0)
            y1 = A1
            #
            x2 = (pin_type[4] / 2.0)
            y2 = A1 - (pin_type[3] - (pin_type[5] / 2.0))
            #
            x3 = (pin_type[6] / 2.0)
            y3 = A1 - (pin_type[3])
            #
            x4 = (pin_type[6] / 2.0)
            y4 = A1 - (pin_type[3] + pin_type[5])
            

            pts = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (0 - x4, y4), (0 - x3, y3), (0 - x2, y2), (0 - x1, y1), (x1, y1)]
            pins = cq.Workplane("XZ").workplane(offset=0 - (pin_type[2] / 2.0)).polyline(pts).close().extrude(pin_type[2])
            pins = pins.faces("<Z").edges("<X").fillet(pin_type[6] / 2.3)
            pins = pins.faces("<Z").edges(">X").fillet(pin_type[6] / 2.3)
            pint = cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0 - (2.0 - (pin_type[2] / 2.0))).rect(pin_type[4], 4.0).extrude(pin_type[2])
            pint = pint.faces(">Y").edges(">Z").fillet(pin_type[2] / 1.5)
            pins = pins.union(pint)
            pins = pins.rotate((0,0,0), (0,0,1), 360 - (alpha * (180.0 / math.pi)))
            pins = pins.translate((xx, yy, 0))

            alpha = alpha + alpha_delta
            for i in range(1, pin_number):
                xx = (h * math.sin(alpha)) + origo_x
                yy = (h * math.cos(alpha)) - origo_y

                pine = cq.Workplane("XZ").workplane(offset=0 - (pin_type[2] / 2.0)).polyline(pts).close().extrude(pin_type[2])
                pine = pine.faces("<Z").edges("<X").fillet(pin_type[6] / 2.3)
                pine = pine.faces("<Z").edges(">X").fillet(pin_type[6] / 2.3)
                pinr = cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0 - (2.0 - (pin_type[2] / 2.0))).rect(pin_type[4], 4.0).extrude(pin_type[2])
                pinr = pinr.faces(">Y").edges(">Z").fillet(pin_type[2] / 1.5)
                pine = pine.union(pint)
                pine = pine.rotate((0,0,0), (0,0,1), 360 - (alpha * (180.0 / math.pi)))
                pine = pine.translate((xx, yy, 0))

                pins = pins.union(pine)
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

        'Valve_Socket_Belton_VT9_PT-B9A-D21.00mm_Tap': Params(
            #
            # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
            # A number of parameters have been fixed or guessed, such as A2
            # 
            modelName = 'Valve_Socket_Belton_VT9_PT-B9A-D21.00mm_Tap',   # modelName
            D = 27.00,                  # Body width/diameter
            socket_H = 08.50,           # Body height
            A1 = 0.03,                  # Body-board separation
            pin_top_diameter = 11.89,   # Diameter of the pin holes ontop
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
    }
        
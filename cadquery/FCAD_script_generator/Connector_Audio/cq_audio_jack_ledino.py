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


import cq_common  # modules parameters
from cq_common import *

import sys
import math


class cq_audio_jack_ledino():

    def __init__(self):
        x = 0

        
    def get_model_name(self, modelID):
        for n in self.all_params:
            if n == modelID:
                return self.all_params[modelID].modelName
        return 'xxUNKNOWNxxx'

        
    def get_dest_3D_dir(self, modelID):
        for n in self.all_params:
            if n == modelID:
                return self.all_params[modelID].dest_dir_prefix
        return 'Capacitor_SMD.3dshapes'

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

        
    def make_3D_model(self, modelID):
        
        destination_dir = self.get_dest_3D_dir(modelID)
        params = self.all_params[modelID]

        
        if modelID == 'Jack_3_5mm_Ledino':
            case_top = self.make_top_Jack_3_5mm_Ledino(params)
            show(case_top)
            case = self.make_case_Jack_3_5mm_Ledino(params)
            show(case)
        else:
            FreeCAD.Console.PrintMessage('\r\n')
            FreeCAD.Console.PrintMessage('ERROR: Model ID ' + str(modelID) + ' does not exist, exiting')
            FreeCAD.Console.PrintMessage('\r\n')
            sys.exit()
            
        pins = self.make_pin(params)
        show(pins)
            
        npth_pins = self.make_npth_pins_dummy(params)
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


    def make_npth_pins_dummy(self, params):

        A1 = params.A1                      # package height
        rotation = params.rotation          # Rotation if required

        # Dummy
        case = cq.Workplane("XY").workplane(offset=A1 + 0.2).moveTo(0.0, 0.0).circle(0.01, False).extrude(0.01)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_top_Jack_3_5mm_Ledino(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z
        AW = params.AW              # Appendix width
        AW1 = params.AW1            # Appendix width 1
        AL = params.AL              # Appendix length
        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        case = cq.Workplane("YZ").workplane(offset=AY).moveTo(AX, AZ).circle(AW1 / 2.0, False).extrude(AL)
        case1 = cq.Workplane("YZ").workplane(offset=AY).moveTo(AX, AZ).circle((AW1 / 2.0) - 0.2, False).extrude(AL)
        case = case.cut(case1)

        case = case.translate((BX, BY, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_case_Jack_3_5mm_Ledino(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z
        AW = params.AW              # Appendix width
        AW1 = params.AW1            # Appendix width 1
        AL = params.AL              # Appendix length
        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        
        case1 = cq.Workplane("YZ").workplane(offset=AY).moveTo(AX, AZ).circle((AW1 / 2.0) - 0.2, False).extrude(W)
        case = case.cut(case1)
        
        case1 = cq.Workplane("YZ").workplane(offset=AY).moveTo(AX, AZ).circle(AW / 2.0, False).extrude(AL)
        case2 = cq.Workplane("YZ").workplane(offset=AY).moveTo(AX, AZ).circle((AW1 / 2.0), False).extrude(AL)
        case1 = case1.cut(case2)
        case1 = case1.faces("<X").edges("<Y").chamfer(0.1)
        
        case = case.union(case1)

        #
        # Pigs ontop
        #
        case1 = cq.Workplane("XY").workplane(offset=H).moveTo(0.0 - ((W / 2.0) - 1.5), 0.0 - ((L / 2.0) - 1.5)).circle(1.2 / 2.0, False).extrude(0.8)
        case1 = case1.faces(">Z").fillet(0.45)
        case = case.union(case1)
        case1 = cq.Workplane("XY").workplane(offset=H).moveTo(0.0 - ((W / 2.0) - 1.5), ((L / 2.0) - 1.5)).circle(1.2 / 2.0, False).extrude(0.8)
        case1 = case1.faces(">Z").fillet(0.45)
        case = case.union(case1)
        case1 = cq.Workplane("XY").workplane(offset=H).moveTo(((W / 2.0) - 1.5), 0.0).circle(1.2 / 2.0, False).extrude(0.8)
        case1 = case1.faces(">Z").fillet(0.45)
        case = case.union(case1)
        
        case = case.translate((BX, BY, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case


    def make_pin(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z
        AW = params.AW              # Appendix width
        AW1 = params.AW1            # Appendix width 1
        AL = params.AL              # Appendix length
        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        case = None
        for n in pin:
            t = n[0]
            x = n[1]
            y = n[2]
            w = n[3]
            l = n[4]
            ld = n[5]
#            pin = [['rect', 0.0, 0.0, 1.5, 0.5, 3.3], ['rect', 2.0, 2.4, 1.5, 0.5, 3.3], ['rect', 2.0, 7.9, 1.5, 0.5, 3.3]],
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(w, l).extrude(0.0 - (ld))
            if w > l:
                case1 = case1.faces("<Z").edges("<X").fillet(w / 2.2)
                case1 = case1.faces("<Z").edges(">X").fillet(w / 2.2)
            else:
                case1 = case1.faces("<Z").edges("<Y").fillet(l / 2.2)
                case1 = case1.faces("<Z").edges(">Y").fillet(l / 2.2)
                
            if t == 'bougl':
                ttf = 2.0
                ttl = 8.0
                case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(2.0 * w, l).extrude(lt)
                case1 = case1.union(case2)
                #
                case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(2.0 * w, l).extrude(lt)
                case3 = cq.Workplane("YZ").workplane(offset=0.0 - w).moveTo(ttf - (l / 2.0), lt).circle(ttf, False).extrude(2.0 * w)
                case4 = cq.Workplane("YZ").workplane(offset=0.0 - w).moveTo(ttf - (l / 2.0), lt).circle(ttf - l, False).extrude(2.0 * w)
                case5 = cq.Workplane("XY").workplane(offset=lt - ttf).moveTo(0.0, 0.0 + ttf).rect(2.0 * w, (2.0 * ttf)).extrude(ttf)
                case3 = case3.cut(case5)
                case3 = case3.cut(case4)
                case2 = case2.union(case3)
                case3 = cq.Workplane("XY").workplane(offset=(lt - ttf)).moveTo(0.0, (2.0 * ttf) - l).rect(2.0 * w, l).extrude(ttf)
                case2 = case2.union(case3)
                case3 = cq.Workplane("XY").workplane(offset=(lt - ttf)).moveTo(0.0, (2.0 * ttf) + (ttl / 2.0) - l).rect(2.0 * w, ttl).extrude(l)
                case2 = case2.union(case3)
                case1 = case1.union(case2)
            elif t == 'bougr':
                ttf = 2.0
                ttl = 8.0
                case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(2.0 * w, l).extrude(lt - ttf)
                case1 = case1.union(case2)
                #
                case2 = cq.Workplane("XY").workplane(offset=(lt - ttf - l)).moveTo(0.0, 0.0 - ((2.0 * ttf) - (l / 2.0))).rect(2.0 * w, ttl).extrude(l)
                case1 = case1.union(case2)
                case1 = case1.faces(">Z").edges(">Y").fillet(l)

            case1 = case1.translate((x, y, 0.0))
                
            if case == None:
                case = case1
            else:
                case = case.union(case1)

        case = case.translate((0.0, 0.0, A1))

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
        'A1',				    # Body PCB seperation

        'W',				    # Width
        'L',				    # Length
        'H',				    # Height
        'BX',				    # Body center X
        'BY',				    # Body center Y
        
        'AX',				    # Appendix X
        'AY',				    # Appendix Y
        'AZ',				    # Appendix Z
        'AW',				    # Appendix width
        'AL',				    # Appendix length
        'AW1',				    # Appendix width 1
        'AL1',				    # Appendix length 1
        'AW2',				    # Appendix width 2
        'AL2',				    # Appendix length 2
        
        'pin',                  # pin
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {

        'Jack_3_5mm_Ledino': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'Jack_3.5mm_Ledino_KB3SPRS_Horizontal', # modelName
            W = 14.30,                                      # Body width
            L = 11.60,                                      # Body length
            H = 06.10,                                      # Body height
            BX = 01.45,                                     # Body center X
            BY = 04.90,                                     # Body center Y
            
            AX = -00.30,                                    # Appendix X
            AY = -10.75,                                    # Appendix Y
            AZ = 03.10,                                     # Appendix Z
            AW = 06.00,                                     # Appendix width
            AW1 = 03.60,                                    # Appendix width 1
            AL = 03.60,                                     # Appendix length

            A1 = 0.01,                                      # Body-board separation

            pin = [['rect', 0.0, 0.0, 1.2, 0.2, 3.2], ['rect', -3.9, 4.6, 0.2, 1.2, 3.2], ['rect', 7.3, 0.5, 0.2, 1.2, 3.2], ['rect', 2.9, 7.1, 1.2, 0.2, 3.2], ['rect', 4.1, 9.8, 1.2, 0.2, 3.2]],
            body_top_color_key  = 'metal aluminum',         # Top color
            body_color_key      = 'black body',             # Body color
            pin_color_key       = 'metal silver',           # Pin color
            npth_pin_color_key  = 'grey body',              # NPTH Pin color
            rotation = 0,                                   # Rotation if required
            dest_dir_prefix = 'Connector_Audio.3dshapes',   # destination directory
            ),
    }

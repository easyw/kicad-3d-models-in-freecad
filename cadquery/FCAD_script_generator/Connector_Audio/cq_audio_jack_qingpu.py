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


class cq_audio_jack_qingpu():

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

        
        if modelID == 'Jack_3_5mm_PJ320D':
            case_top = self.make_top_type(params)
            show(case_top)
            case = self.make_case_type(params)
            show(case)
            pins = self.make_pin(params)
            show(pins)
            npth_pins = self.make_npthpin_type(params)
            show(npth_pins)
        elif modelID == 'Jack_3_5mm_PJ320E':
            case_top = self.make_top_type(params)
            show(case_top)
            case = self.make_case_type(params)
            show(case)
            pins = self.make_pin(params)
            show(pins)
            npth_pins = self.make_npthpin_type(params)
            show(npth_pins)
        elif modelID == 'Jack_3_5mm_PJ31060':
            case_top = self.make_top_type(params)
            show(case_top)
            case = self.make_case_type(params)
            show(case)
            pins = self.make_pin(params)
            show(pins)
            npth_pins = self.make_npthpin_type(params)
            show(npth_pins)
        elif modelID == 'Jack_3_5mm_QingPu_WQP_PJ398SM':
            case_top = self.make_top_type(params)
            show(case_top)
            case = self.make_case_type(params)
            show(case)
            pins = self.make_pin(params)
            show(pins)
            npth_pins = self.make_npthpin_type(params)
            show(npth_pins)
        else:
            FreeCAD.Console.PrintMessage('\r\n')
            FreeCAD.Console.PrintMessage('ERROR: Model ID ' + str(modelID) + ' does not exist, exiting')
            FreeCAD.Console.PrintMessage('\r\n')
            sys.exit()
     
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


    def make_top_type(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        BT = params.BT              # Body type
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z
        AW = params.AW              # Appendix width
        AW1 = params.AW1            # Appendix width 1
        AL = params.AL              # Appendix length
        AL1 = params.AL1            # Appendix length 1
        npthpin = params.npthpin    # npth pin
        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required


        if BT == 1:
            case = cq.Workplane("YZ").workplane(offset=AX - AW).moveTo(AY, AZ).circle(AL1 / 2.0 + 0.2, False).extrude(AW)
            case1 = cq.Workplane("YZ").workplane(offset=AX - AW).moveTo(AY, AZ).circle((AL1 / 2.0), False).extrude(AW)
            case = case.cut(case1)
            
        elif BT == 2:
            #
            # Make circle in front
            #
            case = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle(AL1 / 2.0 + 0.2, False).extrude(AW)
            case1 = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle((AL1 / 2.0), False).extrude(AW)
            case = case.cut(case1)
            
        elif BT == 3:
            #
            # Make circle in front
            #
            case = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle(AL1 / 2.0 + 0.2, False).extrude(AW)
            case1 = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle((AL1 / 2.0), False).extrude(AW)
            case = case.cut(case1)
            #
            # Make shield in front
            #
            case1 = cq.Workplane("XY").workplane(offset=H - 0.1).moveTo(0.0, (L / 2.0) - 2.0).rect(W + 0.1, 3.0).extrude(0.2)
            case2 = cq.Workplane("XY").workplane(offset=0.8 + 0.1).moveTo((W / 2.0) , (L / 2.0) - 2.0).rect(0.2, 3.0).extrude(H - 0.8)
            case1 = case1.union(case2)
            case2 = cq.Workplane("XY").workplane(offset=0.8 + 0.1).moveTo(0.0 - (W / 2.0) , (L / 2.0) - 2.0).rect(0.2, 3.0).extrude(H - 0.8)
            case1 = case1.union(case2)
            case1 = case1.faces(">Z").edges(">X").fillet(0.2)
            case1 = case1.faces(">Z").edges("<X").fillet(0.2)
            #
            case2 = cq.Workplane("XY").workplane(offset=H - 0.3).moveTo(0.0, (L / 2.0)).rect(AW, 1.0).extrude(0.4)
            case2 = case2.faces(">Z").edges(">Y").fillet(0.35)
            case1 = case1.union(case2)
            
            case = case.union(case1)
            
        elif BT == 4:
            case = cq.Workplane("XY").workplane(offset=AZ).moveTo(0.0, 0.0).circle(AW / 2.0, False).extrude(AL)
            case1 = cq.Workplane("XY").workplane(offset=AZ + AL).moveTo(0.0, 0.0).circle(AW / 2.0 - 0.2, False).extrude(AL1)
            case1 = case1.faces(">Z").chamfer(0.6, 0.3)
            case = case.union(case1)
            tx = AZ + AL + 0.2
            while tx < (AZ + AL + AL1 - 1.0):
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(AW / 2.0, False).extrude(0.2)
                case1 = case1.faces(">Z").chamfer(0.09)
                case1 = case1.faces("<Z").chamfer(0.09)
                case1 = case1.rotate((0,0,0), (0,1,0), 5.0)
                case1 = case1.translate((0.0, 0.0, tx))
                case = case.union(case1)
                tx = tx + 0.2

            case1 = cq.Workplane("XY").workplane(offset=AZ + AL + AL1 + 0.1).moveTo(0.0, 0.0).circle(AW1 / 2.0, False).extrude(0.0 - (AZ + AL + AL1 + 0.2))
            case = case.cut(case1)
            
            
            
        case = case.translate((BX, BY, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        return case
    #
    # A casing without fillet top and bottom
    #
    def make_case_type(self, params):
        
        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        BT = params.BT              # Body type
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z
        AW = params.AW              # Appendix width
        AW1 = params.AW1            # Appendix width 1
        AL = params.AL              # Appendix length
        AL1 = params.AL1            # Appendix length 1
        npthpin = params.npthpin    # npth pin
        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required

        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        if BT == 1:
            case = case.faces("<Z").fillet(0.2)
            case = case.faces(">Z").fillet(0.2)
            case1 = cq.Workplane("YZ").workplane(offset=AX - AW).moveTo(AY, AZ).circle(AL / 2.0, False).extrude(AW)
            case2 = cq.Workplane("YZ").workplane(offset=AX - AW).moveTo(AY, AZ).circle((AL1 / 2.0) + 0.2, False).extrude(AW)
            case1 = case1.cut(case2)
        elif BT == 2:
            case = case.faces(">Z").fillet(0.2)
            case1 = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle(AL / 2.0, False).extrude(AW)
            case2 = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle((AL1 / 2.0) + 0.2, False).extrude(AW)
            case1 = case1.cut(case2)
        elif BT == 3:
            case = case.faces(">Z").fillet(0.2)
            case1 = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle(AL / 2.0, False).extrude(AW)
            case2 = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + AW + AY)).moveTo(AX, AZ).circle((AL1 / 2.0) + 0.2, False).extrude(AW)
            case3 = cq.Workplane("XZ").workplane(offset=0.0 - ((L / 2.0) + (AW / 2.0) + AY)).moveTo(AX, AZ + (H / 2.0)).rect(AW, AW / 2.0).extrude(AW / 2.0)
            case1 = case1.cut(case2)
            case1 = case1.cut(case3)
        elif BT == 4:
            case1 = cq.Workplane("XY").workplane(offset=H).moveTo(0.0, 0.0 - (L / 2.0)).rect(1.6, 2.0).extrude(0.0 - (H / 2.0))
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=H).moveTo(0.0, (L / 2.0)).rect(7.0, 1.0).extrude(0.0 - (H / 2.0))
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=AZ + AL + AL1 + 0.1).moveTo(0.0, 0.0).circle(AW1 / 2.0, False).extrude(0.0 - (AZ + AL + AL1 + 0.2))
            case = case.cut(case1)
            #
            # Dummy
            #
            case1 = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(0.0, 0.0).circle(0.001, False).extrude(0.001)
        
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
        AL = params.AL              # Appendix length
        AL1 = params.AL1            # Appendix length 1
        AL = params.AL              # Appendix length
        npthpin = params.npthpin    # npth pin
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
            j = n[5]
            if t == 'smd':
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0, 0).rect(w, l).extrude(j)
                if w > l:
                    if x < 0:
                        case1 = case1.faces("<X").edges("<Y").fillet(l / 2.2)
                        case1 = case1.faces("<X").edges(">Y").fillet(l / 2.2)
                        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo((w / 2.0), 0.0).rect(j, l).extrude(A1 + 1.0)
                        case1 = case1.union(case2)
                    else:
                        case1 = case1.faces(">X").edges("<Y").fillet(l / 2.2)
                        case1 = case1.faces(">X").edges(">Y").fillet(l / 2.2)
                        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - (w / 2.0), 0.0).rect(j, l).extrude(A1 + 1.0)
                        case1 = case1.union(case2)
                else:
                    if y < 0:
                        case1 = case1.faces(">Y").edges("<X").fillet(w / 2.2)
                        case1 = case1.faces(">Y").edges(">X").fillet(w / 2.2)
                        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0,  0.0 - (l / 2.0)).rect(w, j).extrude(A1 + 1.0)
                        case1 = case1.union(case2)
                    else:
                        case1 = case1.faces("<Y").edges("<X").fillet(w / 2.2)
                        case1 = case1.faces("<Y").edges(">X").fillet(w / 2.2)
                        case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0,(l / 2.0)).rect(w, j).extrude(A1 + 1.0)
                        case1 = case1.union(case2)

            elif t == 'rect':
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0, 0).rect(w, l).extrude(0.0 - j)
                if w > l:
                    case1 = case1.faces("<Z").edges("<X").fillet(w / 2.2)
                    case1 = case1.faces("<Z").edges(">X").fillet(w / 2.2)
                else:
                    case1 = case1.faces("<Z").edges("<Y").fillet(l / 2.2)
                    case1 = case1.faces("<Z").edges(">Y").fillet(l / 2.2)
                case1 = case1.translate((0.0, 0.0, A1))
                    
            elif t == 'rect1':
                g = n[6]
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0, 0).rect(w, l).extrude(0.0 - j)
                case1 = case1.rotate((0,0,0), (1,0,0), 5.0)
                if w > l:
                    case1 = case1.faces("<Z").edges("<X").fillet(w / 2.2)
                    case1 = case1.faces("<Z").edges(">X").fillet(w / 2.2)
                else:
                    case1 = case1.faces("<Z").edges("<Y").fillet(l / 2.2)
                    case1 = case1.faces("<Z").edges(">Y").fillet(l / 2.2)
                    
                case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0, 0).rect(w, l).extrude(g)
                case2 = case2.rotate((0,0,0), (1,0,0), 5.0)
                case1 = case1.union(case2)
                case2 = cq.Workplane("XY").workplane(offset=g - 0.22).moveTo(0, -1.58).rect(w, 2.0).extrude(l)
                case1 = case1.union(case2)
                case1 = case1.faces(">Z").edges(">Y").fillet(l / 1.1)
                case1 = case1.translate((0.0, 0.0, A1))
            
            case1 = case1.translate((x, 0.0 - y, 0.0))
                
            if case == None:
                case = case1
            else:
                case = case.union(case1)

        case = case.translate((0.0, 0.0, 0.0))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_npthpin_type(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z
        AL = params.AL              # Appendix length
        AL1 = params.AL1            # Appendix length 1
        AL = params.AL              # Appendix length
        npthpin = params.npthpin    # npth pin
        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required


        if npthpin == None:
            case = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0, 0.0).circle(0.01).extrude(0.01)

        elif len(npthpin) < 1:
            case = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0, 0.0).circle(0.01).extrude(0.01)

        else:
            case = None
            for n in npthpin:
                t = n[0]
                x = n[1]
                y = n[2]
                d = n[3]
                l = n[4]
                case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0, 0).circle(d / 2.0).extrude(0.0 - l)
                case1 = case1.edges("<Z").fillet(d / 2.2)

                case1 = case1.translate((x, 0.0 - y, 0.0))
                    
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
        'BT',				    # Body type
        
        'AX',				    # Appendix X
        'AY',				    # Appendix Y
        'AZ',				    # Appendix Z
        'AW',				    # Appendix width
        'AL',				    # Appendix length
        'AW1',				    # Appendix width 1
        'AL1',				    # Appendix length 1
        'AW2',				    # Appendix width 2
        'AL2',				    # Appendix length 2
        
        'npthpin',              # npth pins
        'pin',                  # pin
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'npth_pin_color_key',   # NPTH Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {

        'Jack_3_5mm_PJ320D': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'Jack_3.5mm_PJ320D_Horizontal',     # modelName
            W = 12.10,                                      # Body width
            L = 06.10,                                      # Body length
            H = 05.00,                                      # Body height
            BX = -00.50,                                    # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 1,                                         # Body type
            
            AX = -06.05,                                    # Appendix X
            AY = 00.0,                                      # Appendix Y
            AZ = 02.50,                                     # Appendix Z
            AW = 02.00,                                     # Appendix width
            AL = 05.60,                                     # Appendix length
            AL1 = 03.6,                                     # Appendix length

            A1 = 0.01,                                      # Body-board separation

            pin = [['smd', -3.175, -3.25, 1.2, 2.5, 0.2], ['smd', -0.175, -3.25, 1.2, 2.5, 0.2], ['smd', 3.825, -3.25, 1.2, 2.5, 0.2], ['smd', 4.925, 3.25, 1.2, 2.5, 0.2]],
            npthpin = [['pin', -4.775, 0.0, 1.5, 2.0], ['pin', 2.225, 0.0, 1.5, 2.0]],
            body_top_color_key  = 'metal aluminum',         # Top color
            body_color_key      = 'red body',               # Body color
            pin_color_key       = 'metal grey pins',        # Pin color
            npth_pin_color_key  = 'red body',               # NPTH Pin color
            rotation = 0,                                   # Rotation if required
            dest_dir_prefix = 'Connector_Audio.3dshapes',   # destination directory
            ),

        'Jack_3_5mm_PJ320E': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'Jack_3.5mm_PJ320E_Horizontal',     # modelName
            W = 07.00,                                      # Body width
            L = 11.20,                                      # Body length
            H = 05.00,                                      # Body height
            BX = 02.70,                                     # Body center X
            BY = 03.60,                                     # Body center Y
            BT = 2,                                         # Body type
            
            AX = -00.40,                                    # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 02.50,                                     # Appendix Z
            AW = 02.80,                                     # Appendix width
            AL = 05.60,                                     # Appendix length
            AL1 = 03.6,                                     # Appendix length

            A1 = 0.01,                                      # Body-board separation

            pin = [['rect', 0.0, 0.0, 0.2, 1.0, 3.0], ['rect', 4.5, 1.5, 0.2, 0.9, 3.0], ['rect', 0.0, -4.0, 0.2, 1.0, 3.0], ['rect', 0.0, -7.0, 0.2, 1.0, 3.0], ['rect', 5.5, -7.0, 0.2, 1.0, 3.0]],
            npthpin = [['pin', 2.3, 1.3, 1.2, 2.0], ['pin', 2.3, -5.7, 1.2, 2.0]],
            body_top_color_key  = 'metal aluminum',         # Top color
            body_color_key      = 'black body',             # Body color
            pin_color_key       = 'metal grey pins',        # Pin color
            npth_pin_color_key  = 'black body',             # NPTH Pin color
            rotation = 0,                                   # Rotation if required
            dest_dir_prefix = 'Connector_Audio.3dshapes',   # destination directory
            ),

        'Jack_3_5mm_PJ31060': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'Jack_3.5mm_PJ31060-I_Horizontal',  # modelName
            W = 06.20,                                      # Body width
            L = 12.00,                                      # Body length
            H = 04.10,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 01.15,                                     # Body center Y
            BT = 3,                                         # Body type
            
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 02.00,                                     # Appendix Z
            AW = 02.00,                                     # Appendix width
            AL = 05.00,                                     # Appendix length
            AL1 = 03.6,                                     # Appendix length

            A1 = 0.50,                                      # Body-board separation

            pin = [['smd', -3.65, 3.45, 2.2, 1.2, 0.2], ['smd', -3.65, -1.65, 2.2, 1.2, 0.2], ['smd', -3.65, -4.35, 2.2, 1.2, 0.2], ['smd', 3.2, -4.35, 3.1, 1.2, 0.2], ['smd', 3.65, 2.15, 2.2, 1.2, 0.2], ['smd', 3.0, 4.35, 3.1, 0.8, 0.2]],
            npthpin = [['pin', 0.0, 3.35, 1.5, 2.0]],
            body_top_color_key  = 'metal aluminum',         # Top color
            body_color_key      = 'red body',               # Body color
            pin_color_key       = 'metal grey pins',        # Pin color
            npth_pin_color_key  = 'red body',               # NPTH Pin color
            rotation = 0,                                   # Rotation if required
            dest_dir_prefix = 'Connector_Audio.3dshapes',   # destination directory
            ),

        'Jack_3_5mm_QingPu_WQP_PJ398SM': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical',  # modelName
            W = 09.00,                                      # Body width
            L = 10.50,                                      # Body length
            H = 09.00,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = -07.23,                                    # Body center Y
            BT = 4,                                         # Body type
            
            AX = 00.00,                                     # Appendix X
            AY = 01.50,                                     # Appendix Y
            AZ = 09.00,                                     # Appendix Z
            AW = 06.00,                                     # Appendix width
            AW1 = 03.60,                                    # Appendix width
            AL = 01.00,                                     # Appendix length
            AL1 = 04.50,                                    # Appendix length

            A1 = 0.00,                                      # Body-board separation

            pin = [['rect1', 0.0, 0.0, 0.8, 0.2, 3.5, 8.0], ['rect', 0.0, 3.1, 0.8, 0.2, 3.5], ['rect', 0.0, 11.41, 0.8, 0.2, 3.5]],
            npthpin = None,
            body_top_color_key  = 'metal aluminum',         # Top color
            body_color_key      = 'black body',             # Body color
            pin_color_key       = 'metal grey pins',        # Pin color
            npth_pin_color_key  = 'red body',               # NPTH Pin color
            rotation = 0,                                   # Rotation if required
            dest_dir_prefix = 'Connector_Audio.3dshapes',   # destination directory
            ),
    }

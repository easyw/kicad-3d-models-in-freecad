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


class cq_coaxial_amphenol():

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

        
        if modelID == 'SMA_Amphenol_132134':
            case_top = self.make_top_SMA_Amphenol_132134(params)
            show(case_top)
            case = self.make_case_SMA_Amphenol_132134(params)
            show(case)
        elif modelID == 'SMA_Amphenol_901_144':
            case_top = self.make_top_SMA_Amphenol_132134(params)
            show(case_top)
            case = self.make_case_SMA_Amphenol_132134(params)
            show(case)
        elif modelID == 'SMA_Amphenol_132134_11':
            case_top = self.make_top_SMA_Amphenol_132134(params)
            show(case_top)
            case = self.make_case_SMA_Amphenol_132134(params)
            show(case)
        elif modelID == 'SMA_Amphenol_132134_14':
            case_top = self.make_top_SMA_Amphenol_132134(params)
            show(case_top)
            case = self.make_case_SMA_Amphenol_132134(params)
            show(case)
        elif modelID == 'SMA_Amphenol_132134_16':
            case_top = self.make_top_SMA_Amphenol_132134(params)
            show(case_top)
            case = self.make_case_SMA_Amphenol_132134(params)
            show(case)
        elif modelID == 'SMA_Amphenol_132289':
            case_top = self.make_top_SMA_Amphenol_132134(params)
            show(case_top)
            case = self.make_case_SMA_Amphenol_132134(params)
            show(case)
        elif modelID == 'SMA_Amphenol_132134_10':
            case_top = self.make_top_SMA_Amphenol_132134(params)
            show(case_top)
            case = self.make_case_SMA_Amphenol_132134(params)
            show(case)
        else:
            FreeCAD.Console.PrintMessage('\r\n')
            FreeCAD.Console.PrintMessage('ERROR: Model ID ' + str(modelID) + ' does not exist, exiting')
            FreeCAD.Console.PrintMessage('\r\n')
            sys.exit()
            
        pins = self.make_pin(params)
        show(pins)
            
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
     
        body_top_color_key = params.body_top_color_key
        body_color_key = params.body_color_key
        pin_color_key = params.pin_color_key

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


    def make_top_SMA_Amphenol_132134(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        BT = params.BT              # Body cut

        AW = params.AW              # Appendix width
        AL = params.AL              # Appendix length
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z

        AW1 = params.AW1            # Appendix width 1
        AL1 = params.AL1            # Appendix length 1
        AX1 = params.AX1            # Appendix center X 1
        AY1 = params.AY1            # Appendix center Y 1
        AZ1 = params.AZ1            # Appendix center Z 1

        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required
        rotationy = params.rotationy    # Rotation if required
        translate = params.translate    # Rotation if required

        case = cq.Workplane("XY").workplane(offset=AZ1).moveTo(AX1, AY1).circle((AW1 / 2.0) - 1.0, False).extrude(AL1)
        #
        # Cut out center pin
        #
        case1 = cq.Workplane("XY").workplane(offset=AZ1).moveTo(AX1, AY1).circle(0.8, False).extrude(AL1)
        case = case.cut(case1)

        case = case.translate((BX, BY, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        if rotationy != None:
            if (rotationy != 0):
                case = case.rotate((0,0,0), (0,1,0), rotationy)

        if translate != None:
            if len(translate) > 2:
                case = case.translate((translate[0], translate[1], translate[2]))
        
        return case


    def make_case_SMA_Amphenol_132134(self, params):

        W = params.W                # Width
        L = params.L                # Length
        H = params.H                # Height
        BX = params.BX              # Body center X
        BY = params.BY              # Body center Y
        BT = params.BT              # Body cut

        AW = params.AW              # Appendix width
        AL = params.AL              # Appendix length
        AX = params.AX              # Appendix center X
        AY = params.AY              # Appendix center Y
        AZ = params.AZ              # Appendix center Z

        AW1 = params.AW1            # Appendix width 1
        AL1 = params.AL1            # Appendix length 1
        AX1 = params.AX1            # Appendix center X 1
        AY1 = params.AY1            # Appendix center Y 1
        AZ1 = params.AZ1            # Appendix center Z 1

        pin = params.pin            # pin
        A1 = params.A1              # package height
        rotation = params.rotation  # Rotation if required
        rotationy = params.rotationy    # Rotation if required
        translate = params.translate    # Rotation if required

        #
        # Main body
        #
        case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(H)
        # cut out under body
        if BT > 0.001:
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W / 2.0, 2.0 * L).extrude(BT)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(2.0 * L, W / 2.0).extrude(BT)
            case = case.cut(case1)
        
        # Base
        case1 = cq.Workplane("XY").workplane(offset=AZ).moveTo(0.0, 0.0).circle((AW / 2.0), False).extrude(AL)
        case = case.union(case1)
        # Top cylinder
        case1 = cq.Workplane("XY").workplane(offset=AZ1).moveTo(0.0, 0.0).circle((AW1 / 2.0) - 0.2, False).extrude(AL1)
        # Add the taps
        tt = AZ1 + 0.4
        while tt < (AZ1 + AL1 - 0.6):
#        while ty < (AY1 + 2.0):
            case2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(AW1 / 1.8, False).extrude(0.2)
            case2 = case2.faces(">Z").chamfer(0.08)
            case2 = case2.faces(">Z").chamfer(0.08)
            case2 = case2.rotate((0,0,0), (0,1,0), 5.0)
            case2 = case2.translate((AX1, AY1, tt))
            case1 = case1.union(case2)
            tt = tt + 0.4
            
        # Cut out hollow
        case2 = cq.Workplane("XY").workplane(offset=AZ1 + 0.2).moveTo(0.0, 0.0).circle((AW1 / 2.0) - 0.4, False).extrude(AL1 + 2.0)
        case1 = case1.cut(case2)
        # Center pin
        case2 = cq.Workplane("XY").workplane(offset=AZ1).moveTo(AX1, AY1).circle(0.8, False).extrude(AL1)
        case3 = cq.Workplane("XY").workplane(offset=AZ1).moveTo(AX1, AY1).circle(0.76, False).extrude(AL1)
        case2 = case2.cut(case3)
        case1 = case1.union(case2)

        case = case.union(case1)

        case = case.translate((BX, BY, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        if rotationy != None:
            if (rotationy != 0):
                case = case.rotate((0,0,0), (0,1,0), rotationy)

        if translate != None:
            if len(translate) > 2:
                case = case.translate((translate[0], translate[1], translate[2]))

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
        rotationy = params.rotationy    # Rotation if required
        translate = params.translate    # Rotation if required

        if pin == None:
            case = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).circle(0.01, False).extrude(0.01)
            
        elif len(pin) < 1:
            case = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).circle(0.01, False).extrude(0.01)

        else:
            case = None
            for n in pin:
                t = n[0]
                x = n[1]
                y = n[2]
                w = n[3]
                l = n[4]
                ld = n[5]
                if t == 'round':
                    case1 = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).circle(w / 2.0, False).extrude(0.0 - (ld + 1.0))
                    case1 = case1.faces("<Z").fillet(w / 2.2)
                elif t == 'rect':
                    case1 = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).rect(w, l).extrude(0.0 - (ld + 1.0))
                    if w > l:
                        case1 = case1.faces("<Z").edges("<X").fillet(w / 2.2)
                        case1 = case1.faces("<Z").edges(">X").fillet(w / 2.2)
                    else:
                        case1 = case1.faces("<Z").edges("<Y").fillet(l / 2.2)
                        case1 = case1.faces("<Z").edges(">Y").fillet(l / 2.2)
                elif t == 'rect1':
                    case1 = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).rect(w, l).extrude(0.0 - (ld + 1.0))
                    if l > w:
                        case1 = case1.faces("<Z").edges(">Y").fillet(l / 2.2)
                    else:
                        case1 = case1.faces("<Z").edges("<Y").fillet(w / 2.2)
                elif t == 'rect2':
                    r = n[6]
                    case1 = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).rect(w, l).extrude(0.0 - (ld + 1.0))
                    case1 = case1.rotate((0,0,0), (0,0,1), r)
                elif t == 'rect4':
                    case1 = cq.Workplane("XY").workplane(offset=1.0).moveTo(0.0, 0.0).rect(w, l).extrude(0.0 - (ld + 1.0))
                elif t == 'smd':
                    case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(w, l).extrude(ld)
                
                case1 = case1.translate((x, y, 0.0))
                    
                if case == None:
                    case = case1
                else:
                    case = case.union(case1)

        case = case.translate((0.0, 0.0, A1))

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)
        
        if rotationy != None:
            if (rotationy != 0):
                case = case.rotate((0,0,0), (0,1,0), rotationy)

        if translate != None:
            if len(translate) > 2:
                case = case.translate((translate[0], translate[1], translate[2]))

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
        'BT',				    # Body cut
        
        'AW',				    # Appendix width
        'AL',				    # Appendix length
        'AX',				    # Appendix X
        'AY',				    # Appendix Y
        'AZ',				    # Appendix Z
        
        'AW1',				    # Appendix width 1
        'AL1',				    # Appendix length 1
        'AX1',				    # Appendix X 1
        'AY1',				    # Appendix Y 1
        'AZ1',				    # Appendix Z 1
        
        'AW2',				    # Appendix width 2
        'AL2',				    # Appendix length 2
        
        'pin',                  # pin
        'npth_pin_color_key',   # NPTH Pin color
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'rotation',	            # Rotation if required
        'rotationy',            # Rotation if required
        'translate',            # Translate if required, even pins
        'dest_dir_prefix'	    # Destination directory
    ])



    all_params = {

        'SMA_Amphenol_132134': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'SMA_Amphenol_132134_Vertical',     # modelName
            W = 07.00,                                      # Body width
            L = 07.00,                                      # Body length
            H = 01.50,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 00.30,                                     # Body cut
            
            AW = 05.50,                                     # Appendix width
            AL = 01.50,                                     # Appendix length
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 01.50,                                     # Appendix Z
            
            AW1 = 05.30,                                    # Appendix width 1
            AL1 = 06.03,                                    # Appendix length 1
            AX1 = 00.00,                                    # Appendix X 1
            AY1 = 00.00,                                    # Appendix Y 1
            AZ1 = 03.00,                                    # Appendix Z 1

            A1 = 0.01,                                      # Body-board separation

            pin = [['round', 0.0, 0.0, 1.27, 1.27, 3.94], ['rect', -2.54, -2.54, 1.02, 1.02, 3.94], ['rect', 2.54, -2.54, 1.02, 1.02, 3.94], ['rect', -2.54, 2.54, 1.02, 1.02, 3.94], ['rect', 2.54, 2.54, 1.02, 1.02, 3.94]],
            body_top_color_key  = 'white body',             # Top color
            body_color_key      = 'gold pins',              # Body color
            pin_color_key       = 'gold pins',              # Pin color
            npth_pin_color_key  = 'metal grey pins',        # NPTH Pin color
            rotation = 0,                                 # Rotation if required
            dest_dir_prefix = 'Connector_Coaxial.3dshapes', # destination directory
            ),

        'SMA_Amphenol_901_144': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'SMA_Amphenol_901-144_Vertical',    # modelName
            W = 06.35,                                      # Body width
            L = 06.35,                                      # Body length
            H = 01.50,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 00.00,                                     # Body cut
            
            AW = 04.50,                                     # Appendix width
            AL = 03.00,                                     # Appendix length
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 01.50,                                     # Appendix Z
            
            AW1 = 05.30,                                    # Appendix width 1
            AL1 = 05.02,                                    # Appendix length 1
            AX1 = 00.00,                                    # Appendix X 1
            AY1 = 00.00,                                    # Appendix Y 1
            AZ1 = 04.50,                                    # Appendix Z 1

            A1 = 0.01,                                      # Body-board separation

            pin = [['round', 0.0, 0.0, 1.27, 1.27, 3.94], ['rect', -2.54, -2.54, 1.02, 1.02, 3.94], ['rect', 2.54, -2.54, 1.02, 1.02, 3.94], ['rect', -2.54, 2.54, 1.02, 1.02, 3.94], ['rect', 2.54, 2.54, 1.02, 1.02, 3.94]],
            body_top_color_key  = 'white body',             # Top color
            body_color_key      = 'gold pins',              # Body color
            pin_color_key       = 'gold pins',              # Pin color
            npth_pin_color_key  = 'metal grey pins',        # NPTH Pin color
            rotation = 0,                                 # Rotation if required
            dest_dir_prefix = 'Connector_Coaxial.3dshapes', # destination directory
            ),

        'SMA_Amphenol_132134_11': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'SMA_Amphenol_132134-11_Vertical',  # modelName
            W = 06.35,                                      # Body width
            L = 06.35,                                      # Body length
            H = 02.50,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 00.60,                                     # Body cut

            AW = 05.00,                                     # Appendix width
            AL = 01.00,                                     # Appendix length
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 02.50,                                     # Appendix Z

            AW1 = 05.30,                                    # Appendix width 1
            AL1 = 06.05,                                    # Appendix length 1
            AX1 = 00.00,                                    # Appendix X 1
            AY1 = 00.00,                                    # Appendix Y 1
            AZ1 = 03.50,                                    # Appendix Z 1

            A1 = 0.01,                                      # Body-board separation

            pin = [['round', 0.0, 0.0, 1.27, 1.27, 2.80], ['rect', -2.54, -2.54, 1.02, 1.02, 2.80], ['rect', 2.54, -2.54, 1.02, 1.02, 2.80], ['rect', -2.54, 2.54, 1.02, 1.02, 2.80], ['rect', 2.54, 2.54, 1.02, 1.02, 2.80]],
            body_top_color_key  = 'white body',             # Top color
            body_color_key      = 'gold pins',              # Body color
            pin_color_key       = 'gold pins',              # Pin color
            npth_pin_color_key  = 'metal grey pins',        # NPTH Pin color
            rotation = 0,                                 # Rotation if required
            dest_dir_prefix = 'Connector_Coaxial.3dshapes', # destination directory
            ),

        'SMA_Amphenol_132134_14': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'SMA_Amphenol_132134-14_Vertical',  # modelName
            W = 07.00,                                      # Body width
            L = 07.00,                                      # Body length
            H = 01.50,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 00.30,                                     # Body cut

            AW = 05.50,                                     # Appendix width
            AL = 02.00,                                     # Appendix length
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 01.50,                                     # Appendix Z

            AW1 = 05.20,                                    # Appendix width 1
            AL1 = 05.85,                                    # Appendix length 1
            AX1 = 00.00,                                    # Appendix X 1
            AY1 = 00.00,                                    # Appendix Y 1
            AZ1 = 03.50,                                    # Appendix Z 1

            A1 = 0.01,                                      # Body-board separation

            pin = [['round', 0.0, 0.0, 0.61, 0.61, 3.94], ['rect', -2.54, -2.54, 1.02, 1.02, 3.94], ['rect', 2.54, -2.54, 1.02, 1.02, 3.94], ['rect', -2.54, 2.54, 1.02, 1.02, 3.94], ['rect', 2.54, 2.54, 1.02, 1.02, 3.94]],
            body_top_color_key  = 'white body',             # Top color
            body_color_key      = 'gold pins',              # Body color
            pin_color_key       = 'gold pins',              # Pin color
            npth_pin_color_key  = 'metal grey pins',        # NPTH Pin color
            rotation = 0,                                 # Rotation if required
            dest_dir_prefix = 'Connector_Coaxial.3dshapes', # destination directory
            ),

        'SMA_Amphenol_132134_16': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'SMA_Amphenol_132134-16_Vertical',  # modelName
            W = 07.00,                                      # Body width
            L = 07.00,                                      # Body length
            H = 01.50,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 00.30,                                     # Body cut

            AW = 05.00,                                     # Appendix width
            AL = 01.50,                                     # Appendix length
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 01.50,                                     # Appendix Z

            AW1 = 05.20,                                    # Appendix width 1
            AL1 = 06.53,                                    # Appendix length 1
            AX1 = 00.00,                                    # Appendix X 1
            AY1 = 00.00,                                    # Appendix Y 1
            AZ1 = 03.00,                                    # Appendix Z 1

            A1 = 0.01,                                      # Body-board separation

            pin = [['round', 0.0, 0.0, 1.27, 1.27, 2.0], ['rect', -2.54, -2.54, 1.02, 1.02, 2.79], ['rect', 2.54, -2.54, 1.02, 1.02, 2.79], ['rect', -2.54, 2.54, 1.02, 1.02, 2.79], ['rect', 2.54, 2.54, 1.02, 1.02, 2.79]],
            body_top_color_key  = 'white body',             # Top color
            body_color_key      = 'gold pins',              # Body color
            pin_color_key       = 'gold pins',              # Pin color
            npth_pin_color_key  = 'metal grey pins',        # NPTH Pin color
            rotation = 0,                                 # Rotation if required
            dest_dir_prefix = 'Connector_Coaxial.3dshapes', # destination directory
            ),

        'SMA_Amphenol_132289': Params(
            #
            # https://www.cui.com/product/resource/sj1-353xng.pdf
            # 
            modelName = 'SMA_Amphenol_132289_EdgeMount',    # modelName
            W = 09.52,                                      # Body width
            L = 09.52,                                      # Body length
            H = 01.50,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 00.00,                                     # Body cut

            AW = 05.00,                                     # Appendix width
            AL = 01.50,                                     # Appendix length
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 01.50,                                     # Appendix Z

            AW1 = 05.30,                                    # Appendix width 1
            AL1 = 09.65,                                    # Appendix length 1
            AX1 = 00.00,                                    # Appendix X 1
            AY1 = 00.00,                                    # Appendix Y 1
            AZ1 = 03.00,                                    # Appendix Z 1

            A1 = 0.01,                                      # Body-board separation

            pin = [['round', 0.0, -0.44, 0.76, 0.76, 2.0], ['rect1', -4.25, -3.835, 1.02, 1.85, 2.79], ['rect1', 4.25, -3.835, 1.02, 1.85, 2.79], ['rect1', -4.25, -0.3, 1.02, 1.02, 2.79], ['rect1', 4.25, -0.3, 1.02, 1.02, 2.79]],
            body_top_color_key  = 'white body',             # Top color
            body_color_key      = 'gold pins',              # Body color
            pin_color_key       = 'gold pins',              # Pin color
            npth_pin_color_key  = 'metal grey pins',        # NPTH Pin color
            
            rotation = 90,                                  # Rotation if required
            rotationy = 90,                                 # Rotation if required
            translate = [2.0, 0.0, 0.8],                    # translation
            
            dest_dir_prefix = 'Connector_Coaxial.3dshapes', # destination directory
            ),

        'SMA_Amphenol_132134_10': Params(
            #
            # http://www.molex.com/pdm_docs/sd/734120110_sd.pdf
            # 
            modelName = 'SMA_Amphenol_132134-10_Vertical',  # modelName
            W = 06.35,                                      # Body width
            L = 06.35,                                      # Body length
            H = 01.02,                                      # Body height
            BX = 00.00,                                     # Body center X
            BY = 00.00,                                     # Body center Y
            BT = 00.00,                                     # Body cut

            AW = 06.00,                                     # Appendix width
            AL = 01.20,                                     # Appendix length
            AX = 00.00,                                     # Appendix X
            AY = 00.00,                                     # Appendix Y
            AZ = 01.02,                                     # Appendix Z

            AW1 = 06.00,                                    # Appendix width 1
            AL1 = 05.35,                                    # Appendix length 1
            AX1 = 00.00,                                    # Appendix X 1
            AY1 = 00.00,                                    # Appendix Y 1
            AZ1 = 02.22,                                    # Appendix Z 1

            A1 = 0.01,                                      # Body-board separation

            pin = [['round', 0.0, 0.0, 1.27, 1.27, 1.27], ['rect4', -2.38, -2.38, 1.59, 1.59, 1.27], ['rect4', 2.38, -2.38, 1.59, 1.59, 1.27], ['rect4', -2.38, 2.38, 1.59, 1.59, 1.27], ['rect4', 2.38, 2.38, 1.59, 1.59, 1.27]],
            body_top_color_key  = 'white body',              # Top color
            body_color_key      = 'gold pins',             # Body color
            pin_color_key       = 'gold pins',              # Pin color
            npth_pin_color_key  = 'metal grey pins',        # NPTH Pin color
            
            rotation = 0,                                  # Rotation if required
            translate = [0.0, 0.0, 1.27],                    # translation

            dest_dir_prefix = 'Connector_Coaxial.3dshapes', # destination directory
            ),
    }

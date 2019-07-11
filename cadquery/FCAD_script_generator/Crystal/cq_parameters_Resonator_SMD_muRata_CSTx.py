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

class cq_parameters_Resonator_SMD_muRata_CSTx():

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
        
        case_top = self.make_case_top(self.all_params[modelName])
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
    
    def make_case_top(self, params):

        W = params.W                        # body length
        E = params.E                        # body width
        H = params.H                        # body height
        A1 = params.A1                      # Body distance to PCB
        
        TW = params.TW                      # top length
        TE = params.TE                      # top width
        TH = params.TH                      # top height

        pin_split = params.pin_split        # top height
        pin_width = params.pin_width        # top height

        rotation = params.rotation          # Rotation if required

        #
        # Calculate center
        # pin 1 always in origo
        #
        origo_x = 0.0
        origo_y = 0.0

        #
        case = None
        if (TW > 0.01):
            ff = TH / 7.0
            case=cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).rect(TW, TE).extrude(H + TH)
            case = case.faces(">Z").fillet(ff)
        else:
            # Make dummy
            case=cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(origo_x, 0 - origo_y).rect(0.1, 0.1).extrude(0.1)
        
        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)


    def make_case(self, params):

        W = params.W                        # body length
        E = params.E                        # body width
        H = params.H                        # body height
        A1 = params.A1                      # Body distance to PCB
        
        TW = params.TW                      # top length
        TE = params.TE                      # top width
        TH = params.TH                      # top height

        pin_split = params.pin_split        # top height
        pin_width = params.pin_width        # top height
        rotation = params.rotation          # Rotation if required

        #
        origo_x = 0.0
        origo_y = 0.0
        #
        case=cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).rect(W, E).extrude(H)

        if (rotation != 0):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case)

    
    def make_pins(self, case, params):

        W = params.W                        # body length
        E = params.E                        # body width
        H = params.H                        # body height
        A1 = params.A1                      # Body distance to PCB
        
        TW = params.TW                      # top length
        TE = params.TE                      # top width
        TH = params.TH                      # top height

        pin_cnt = params.pin_cnt            # Number of pins
        pin_cut = params.pin_cut            # If edge should cut
        pin_split = params.pin_split        # Distance between pins
        pin_width = params.pin_width        # Pin width
        rotation = params.rotation          # Rotation if required

        #
        if (pin_cnt == 2):
            origo_x = 0.0 - (pin_split / 2.0)
            origo_y = 0.0
        else:
            origo_x = 0.0 - pin_split
            origo_y = 0.0
        
        pins = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0.0 - origo_y).rect(pin_width - 0.1, E + 0.05).extrude(H + 0.025)
        case.cut(pins)
        pins = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0.0 - origo_y).rect(pin_width, E + 0.05).extrude(H + 0.025)
        if (pin_cut > 0.01):
            pinc = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, (0.0 - origo_y) - ((E + 0.05) / 2.0)).circle(pin_cut / 2.0, False).extrude(H + 0.1)
            pins.cut(pinc)
            case.cut(pinc)
            pinc = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, (0.0 - origo_y) + ((E + 0.05) / 2.0)).circle(pin_cut / 2.0, False).extrude(H + 0.1)
            pins.cut(pinc)
            case.cut(pinc)
        
        origo_x = origo_x + pin_split
        pin = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0.0 - origo_y).rect(pin_width - 0.1, E + 0.05).extrude(H + 0.025)
        case.cut(pin)
        pin = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0.0 - origo_y).rect(pin_width, E + 0.05).extrude(H + 0.025)
        if (pin_cut > 0.01):
            pinc = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, (0.0 - origo_y) - ((E + 0.05) / 2.0)).circle(pin_cut / 2.0, False).extrude(H + 0.1)
            pin.cut(pinc)
            case.cut(pinc)
            pinc = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, (0.0 - origo_y) + ((E + 0.05) / 2.0)).circle(pin_cut / 2.0, False).extrude(H + 0.1)
            pin.cut(pinc)
            case.cut(pinc)
        pins=pins.union(pin)
        
        if (pin_cnt == 3):
            origo_x = origo_x + pin_split
            pin = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0.0 - origo_y).rect(pin_width - 0.1, E + 0.05).extrude(H + 0.025)
            case.cut(pin)
            pin = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0.0 - origo_y).rect(pin_width, E + 0.05).extrude(H + 0.025)
            if (pin_cut > 0.01):
                pinc = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, (0.0 - origo_y) - ((E + 0.05) / 2.0)).circle(pin_cut / 2.0, False).extrude(H + 0.1)
                pin.cut(pinc)
                case.cut(pinc)
                pinc = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, (0.0 - origo_y) + ((E + 0.05) / 2.0)).circle(pin_cut / 2.0, False).extrude(H + 0.1)
                pin.cut(pinc)
                case.cut(pinc)
            pins=pins.union(pin)
        
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
        'filename',		        # modelName
        'W',				    # Body length
        'E',			   	    # Body width
        'H',			   	    # Body height
        'TW',				    # Top length
        'TE',			   	    # Top width
        'TH',			   	    # Top height
        'A1',				    # Body PCB seperation
        'pin_cnt',  		    # Number of pins
        'pin_cut',  		    # If edge should cut
        'pin_split',		    # Distance between pins
        'pin_width',		    # Pin width
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'rotation',	            # Rotation if required
        'dest_dir_prefix'	    # Destination directory
    ])

    all_params = {

        'Murata_CSTCC8M00G53': Params(
            #
            # http://www.farnell.com/datasheets/19296.pdf?_ga=1.247244932.122297557.1475167906
            # 
            filename = 'Resonator_SMD-3Pin_7.2x3.0mm',   # modelName
            W = 7.2,                  # Body length
            E = 3.0,                  # Body width
            H = 0.5,                  # Body height
            A1 = 0.0,                 # Body-board separation

            TW = 6.6,               # Top length
            TE = 2.1,               # Top width
            TH = 1.05,              # Top height

            pin_cnt = 3,            # Pin count
            pin_cut = 0.45,         # If edge should cut
            pin_split = 2.5,        # Distance between pins
            pin_width = 1.2,        # Pin width

            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'gold pins',            # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'Murata_CDSCB': Params(
            #
            # http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf
            # 
            filename = 'Resonator_SMD_Murata_CDSCB-2Pin_4.5x2.0mm',   # modelName
            W = 4.5,                  # Body length
            E = 2.0,                  # Body width
            H = 0.4,                  # Body height
            A1 = 0.0,                 # Body-board separation

            TW = 4.1,                 # Top length
            TE = 1.4,                 # Top width
            TH = 0.6,                 # Top height

            pin_cnt = 2,            # Pin count
            pin_cut = 0.4,          # If edge should cut
            pin_split = 3.0,          # Distance between pins
            pin_width = 0.8,          # Pin width

            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'gold pins',            # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'Murata_CSTxExxV': Params(
            #
            # https://www.murata.com/en-eu/products/productdata/8801162264606/SPEC-CSTNE16M0VH3C000R0.pdf
            # 
            filename = 'Resonator_SMD_Murata_CSTxExxV-3Pin_3.0x1.1mm',   # modelName
            W = 3.2,                  # Body length
            E = 1.3,                  # Body width
            H = 0.4,                  # Body height
            A1 = 0.0,                 # Body-board separation

            TW = 3.0,                 # Top length
            TE = 1.1,                 # Top width
            TH = 0.5,                 # Top height

            pin_cnt = 3,            # Pin count
            pin_cut = 0.0,          # If edge should cut
            pin_split = 1.2,          # Distance between pins
            pin_width = 0.5,          # Pin width

            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'gold pins',            # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'Murata_SFECV': Params(
            #
            # http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf
            # 
            filename = 'Resonator_SMD_Murata_SFECV-3Pin_6.9x2.9mm',   # modelName
            W = 6.9,                  # Body length
            E = 2.9,                  # Body width
            H = 1.5,                  # Body height
            A1 = 0.0,                 # Body-board separation

            TW = 0.0,               # Top length
            TE = 0.0,               # Top width
            TH = 0.0,               # Top height

            pin_cnt = 3,            # Pin count
            pin_cut = 0.0,          # If edge should cut
            pin_split = 2.85,       # Distance between pins
            pin_width = 1.0,        # Pin width

            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'gold pins',            # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'Murata_SFSKA': Params(
            #
            # http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf
            # 
            filename = 'Resonator_SMD_Murata_SFSKA-3Pin_7.9x3.8mm',   # modelName
            W = 8.5,                  # Body length
            E = 3.8,                  # Body width
            H = 0.5,                  # Body height
            A1 = 0.0,                 # Body-board separation

            TW = 7.9,               # Top length
            TE = 3.0,               # Top width
            TH = 1.3,               # Top height

            pin_cnt = 3,            # Pin count
            pin_cut = 0.6,          # If edge should cut
            pin_split = 2.5,        # Distance between pins
            pin_width = 1.0,        # Pin width

            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'gold pins',            # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

        'Murata_TPSKA': Params(
            #
            # http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf
            # 
            filename = 'Resonator_SMD_Murata_TPSKA-3Pin_7.9x3.8mm',   # modelName
            W = 8.5,                  # Body length
            E = 3.8,                  # Body width
            H = 0.5,                  # Body height
            A1 = 0.0,                 # Body-board separation

            TW = 7.9,               # Top length
            TE = 3.0,               # Top width
            TH = 1.3,               # Top height

            pin_cnt = 3,            # Pin count
            pin_cut = 0.6,          # If edge should cut
            pin_split = 2.5,        # Distance between pins
            pin_width = 1.0,        # Pin width

            body_top_color_key = 'metal silver',    # Top color
            body_color_key = 'white body',          # Body color
            pin_color_key = 'gold pins',            # Pin color
            rotation = 0,                           # Rotation if required
            dest_dir_prefix = 'Crystal.3dshapes',   # destination directory
            ),

    }
        
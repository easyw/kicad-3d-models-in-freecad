#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This script is derived from a script for generating  DIP_parts and Buzzer_Beeper scripts
#
# Dimensions are from data sheets given in the settings of the corresponding KiCad footprint:

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py *b3fs*

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py *b3fs*

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are a FreeCAD & cadquery tools                                     *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating QFP/SOIC/SSOP/TSSOP models in STEP AP214  *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
#*                                                                          *
#*   Copyright (c) 2020                                                     *
#* Mountyrox   https://github.com/mountyrox                                 *
#*                                                                          *
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
import operator

import cadquery as cq
from Helpers import show

import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui

import shaderColors
import exportPartToVRML as expVRML

# Import cad_tools
import cq_cad_tools
# Reload tools
from cq_cad_tools import reload_lib
reload_lib(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, z_RotateObject, Color_Objects, restore_Main_Tools, exportSTEP, saveFCdoc

import cq_parameters  # modules parameters
from cq_parameters import ShapeOfTerminal, ButtonType, partParamsTactSwitches

import collections
from collections import namedtuple


from  cq_base_model import PartBase, Polyline  # modules parameters

from cq_base_tact_switches import cqMakerTactSwitch, TactSwitchSeries, partsTactSwitches




class TactSwitchSeries (TactSwitchSeries):
    r"""A class for holding C&K tactile switch series KMR2x

    .. note:: will be changed to enum when Python version allows it
    """
    KMR2 = 'KMR2'
    r"""KMR2: 12 mm Tact Switch for SMT and THT. 
    """
    


#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*      class cqMakerCuK_Kmr2xTactSwitch (cqMakerTactSwitch)                *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class cqMakerCuK_Kmr2xTactSwitch (cqMakerTactSwitch):
    r"""A class for creating a 3D models from C&K type KMR2. The parameter are defined in the class ``parts_cuk_kmr2``
    :param parameter: namedtuple containing the variable parameter for building the different 3D models.
    :type  parameter: ``partsTactSwitches.Params``

    """
    def __init__(self, parameter):
        cqMakerTactSwitch.__init__(self, parameter)
        
        self.button_oval_width = parameter.button_oval_width if parameter.button_oval_width != None else 2.11                            
        self.button_oval_length = parameter.button_oval_length if parameter.button_oval_length != None else 1.61                             
        #self. = parameter. if parameter. != None else                              

    def _paramsForKMR2 (self):
        r"""set the reqired dimensions for tactile switch serie C&K PTS125S

        """
        self.cover_thickness = 0.1
        self.body_board_distance = 0.0

        self.pad_side_height = 0.6
        self.pad_side_width  = 2.0 * self.cover_thickness
        self.pad_side_length = 0.7

        self.pin_bottom_length = 0.6

        # Dimension of metallic cover plate
        self.cover_side_height =  1.0
        self.offsets = (0.0, 0.0, 0.0)


    # Append the series switcher
    cqMakerTactSwitch._serieSwitcher[TactSwitchSeries.KMR2] = _paramsForKMR2  

    def _padsSideCenter (self):
        r"""generates a body to be placed (central) at the top side of the parts body. These side pads are the fixing elements for the cover clips.

        :rtype: ``solid``
        """
        pad = cq.Workplane("XY", origin=(0.0, self.body_width / 2.0 - self.cover_thickness, self.body_height - self.cover_thickness - self.pad_side_height))\
                    .rect(self.pad_side_length, self.pad_side_width).extrude(self.pad_side_height)\
                    .edges(">Z").edges(">Y").fillet(self.pad_side_width * 0.99)

        return pad.union(pad.mirror("XZ"))

    
    def makePlasticCase (self):
        """ create the plastic body of the tactile switch
        :rtype: ``solid``
        """

        body = cq.Workplane("XY")\
                 .rect(self.body_length, self.body_width - 2.0 * self.pad_side_width).extrude(self.body_height - self.cover_thickness)

        body = body.edges("|Z").fillet(0.2).union(self._padsSideCenter())

        if self.with_gnd_pin:
            pocket = cq.Workplane("YZ")\
                .rect(self.gnd_pin_width * 1.1, 2.0*self.body_height).extrude(self.cover_thickness*2.0)\
                .translate((self.body_length / 2.0 - self.cover_thickness, 0.0, 0.0))
            body = body.cut(pocket)

        return body


    def _coverSideSheetsClosed (self):
        r"""generates a body used as a side clip of the top cover sheet. The shape of the side clip is a closed frame.
        The side clips will be placed at the sides where are no pins.

        :rtype: ``solid``
        """
        ul = self.pad_side_length + 1.4   # upper length of side sheet
        ll = self.pad_side_length + 0.8   # lower length of side sheet
        body = Polyline(cq.Workplane("XZ").workplane(offset=self.body_width / 2.0 - self.pad_side_width - self.cover_thickness))\
            .addMoveTo(-self.pad_side_length / 2.0, self.body_height)\
            .addPoint(-(ul - self.pad_side_length) / 2.0, 0.0)\
            .addPoint((ul-ll) / 2.0, -self.cover_side_height)\
            .addPoint(ll, 0.0)\
            .addPoint((ul-ll) / 2.0, self.cover_side_height)\
            .addPoint(-(ul - self.pad_side_length) / 2.0, 0.0)\
            .addPoint(0.0, -(self.pad_side_height + self.cover_thickness))\
            .addPoint(-self.pad_side_length, 0.0)\
            .make().extrude(2.0*self.cover_thickness).edges(">Z").edges("<Y").fillet(2.0*self.cover_thickness*0.8)

        #body = body.edges("|Z").fillet(0.05)
        body = body.edges("<Z").edges("|Y").fillet(0.2)

        body = body.union(body.mirror("XZ"))

        return body

    def _makeGndPin (self, pin_width = None, pin_thickness = None):
        r"""generates a pin connected to the top metallic cover sheet used as a ground pin.

        :rtype: ``solid``
        """

        if pin_width is None:
            pin_width = self.gnd_pin_width

        if pin_thickness is None:
             pin_thickness = self.cover_thickness

        gndPin = cq.Workplane("YZ")\
            .rect(self.gnd_pin_width, self.body_height).extrude(self.cover_thickness)\
            .translate((self.body_length / 2.0 - self.cover_thickness, 0.0, self.body_height/2.0))\
            .edges(">Z").edges(">X").fillet(self.cover_thickness*0.99)\
            .edges("<Z").edges("|X").fillet(0.2)\


        return gndPin


    def makeCoverPlate (self):
        """ create the outer metal frame of switch
        :rtype: ``solid``
        """
        # body of cover with button hole completely filled
        body = cq.Workplane("XY")\
                    .rect(self.body_length, self.body_width - 6.0 * self.cover_thickness)\
                    .extrude(self.cover_thickness)

        s = cq.StringSyntaxSelector
        #body = body.edges(s(">Z")-s(">Y")-s("<Y")-s("<X")-s(">X")).fillet(self.cover_thickness*0.25)

        body = body.edges("|Z").fillet(0.2)#.cut(self.makeButton(self.button_oval_length + 0.1, self.button_oval_width + 0.1))\
       
        body = body.translate((0.0, 0.0, self.body_height - self.cover_thickness)).union(self._coverSideSheetsClosed())\
            .cut(self.makeButton(self.button_oval_length + 0.1, self.button_oval_width + 0.1))

        if self.with_gnd_pin:
            pocket = cq.Workplane("YZ")\
                .rect(self.gnd_pin_width * 1.6, self.body_height).extrude(self.cover_thickness*2.0)\
                .translate((self.body_length / 2.0 - self.cover_thickness, 0.0, self.body_height))\
                .edges("|Z").fillet(self.cover_thickness*0.99)

            body = body.cut(pocket).union(self._makeGndPin())

        #body = body.edges(">Z").fillet(0.015)

        return body

    def makeButton (self, button_length = None, button_width = None):
        """ create the button of switch, depending on button type 
        :param button_length: length of oval botton (default: button_oval_length as defined in all_parameter)
        :type button_length: ``float``
        :param button_width: width of oval botton (default: button_oval_width as defined in all_parameter)
        :type button_width: ``float``
        :rtype: ``solid``
        """
        if button_length is None:
            button_length = self.button_oval_length

        if button_width is None:
            button_width  = self.button_oval_width

        button_height = self.body_height_with_button - self.body_height + self.cover_thickness
        fw = 0.15

        s = cq.StringSyntaxSelector
        body = Polyline(cq.Workplane("XY"))\
            .addMoveTo(button_length / 2.0, 0.0)\
            .addPoint(-button_length * fw, -button_width / 2.0)\
            .addPoint(-button_length * (1.0 - 2.0 * fw), 0.0)\
            .addPoint(-button_length * fw, button_width / 2.0)\
            .addPoint(+button_length * fw, button_width / 2.0)\
            .addPoint(+button_length * (1.0 - 2.0 * fw), 0.0)\
            .addPoint(+button_length * fw, -button_width / 2.0)\
            .make().extrude(button_height)\
            .edges(s(">X") + s("<X")).fillet(0.4)\
            .edges("|Z").edges("<Y").fillet(0.4)\
            .edges("|Z").edges(">Y").fillet(0.4)\
            .edges(">Z").fillet(0.05)


        #body = body.edges("|Z").fillet(0.2)
       
        body = body.translate((0.0, 0.0, self.body_height - self.cover_thickness))
        return body




        
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class parts_cuk_kmr2 (partsTactSwitches):
    r"""A class for defining parameter of C6K tactile switches type KMR2. 

    """

        
    def getModelVariant (self, modelName):
        r"""returns the parameter namedtuple from ``all_params`` for the given model name
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :rtype: ``namedtuple``
        """
        return cqMakerCuK_Kmr2xTactSwitch (self.all_params[modelName])

    # will be used if Python version allows it
    #try:
    #    # extend the ParamsWithDefault named tuple by 'point'
    #    partsTactSwitches.Params = partsTactSwitches.namedtuple_with_defaults('Params',partsTactSwitches.Params.\
    #        _fields+('button_oval_width', 'button_oval_length'))
    #except:
    #    FreeCAD.Console.PrintMessage('invalid or duplicate field names.\r\n')


    all_params = {

        'SW_Push_1P1T-SH_NO_CK_KMR2xxG': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T-SH_NO_CK_KMR2xxG',  
            body_width = 4.2,		    
            body_length = 2.8,	       
            body_height = 1.4,
            pin_pitch = 1.6,
            distance_pinTip_rows = 4.6,
            pin_width = 0.6,
            pin_thickness = 0.15,
            terminal_shape = ShapeOfTerminal.GW,
            button_oval_width = 2.11,
            button_oval_length = 1.61,
            body_height_with_button = 1.9,
            button_type = ButtonType.FLAT,
            with_gnd_pin = True,
            gnd_pin_width = 1.2,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.KMR2,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_Push_1P1T_NO_CK_KMR2': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T_NO_CK_KMR2',  
            body_width = 4.2,		    
            body_length = 2.8,	       
            body_height = 1.4,
            pin_pitch = 1.6,
            distance_pinTip_rows = 4.6,
            pin_width = 0.6,
            pin_thickness = 0.15,
            terminal_shape = ShapeOfTerminal.GW,
            button_oval_width = 2.11,
            button_oval_length = 1.61,
            body_height_with_button = 1.9,
            button_type = ButtonType.FLAT,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.KMR2,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

    }



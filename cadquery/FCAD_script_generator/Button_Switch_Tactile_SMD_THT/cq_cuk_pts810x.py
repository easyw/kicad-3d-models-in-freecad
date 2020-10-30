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
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   Copyright (c) 2020                                                     *
#* Mountyrox   https://github.com/mountyrox                                 *
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
from cq_cuk_kmr2x import cqMakerCuK_Kmr2xTactSwitch, TactSwitchSeries, parts_cuk_kmr2 




class TactSwitchSeries (TactSwitchSeries):
    r"""A class for holding C&K tactile switch series PTS810x

    .. note:: will be changed to enum when Python version allows it
    """
    PTS810 = 'PTS810'
    r"""PTS810: Microminiature SMT Top Actuated
    """
    


#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*       class cqMakerCuK_PTS810xTactSwitch (cqMakerCuK_Kmr2xTactSwitch)    *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class cqMakerCuK_PTS810xTactSwitch (cqMakerCuK_Kmr2xTactSwitch):
    r"""A class for creating a 3D models from C&K type PTS810. The parameter are defined in the class ``parts_cuk_pts810``
    :param parameter: namedtuple containing the variable parameter for building the different 3D models.
    :type  parameter: ``partsTactSwitches.Params``

    """
    
    def __init__(self, parameter):
        cqMakerCuK_Kmr2xTactSwitch.__init__(self, parameter)
        
        #self. = parameter. if parameter. != None else                              

    def _paramsForPTS810 (self):
        r"""set the reqired dimensions for tactile switch serie C&K PTS810

        """
        self.cover_thickness = 0.15
        self.body_board_distance = 0.0


        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0
        self.pin_bottom_length = 0.6
        self.pin_height = 0.5

        self.cover_offset = 1.3
        self.body_top_chamfer = 1.25
        # Dimension of metallic cover plate
        self.offsets = (0.0, 0.0, 0.0)


    # Append the series switcher
    cqMakerTactSwitch._serieSwitcher[TactSwitchSeries.PTS810] = _paramsForPTS810

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
                 .rect(self.body_length, self.body_width).extrude(self.body_height - self.cover_thickness)

        body = body.edges("|Z").fillet(0.2)

        pocket = cq.Workplane("XY")\
            .rect(self.body_length, self.body_width).extrude(self.body_height)\
            .translate((0.0, 0.0, self.cover_offset))\
            .edges("|Z").chamfer(self.body_top_chamfer)

        body = body.cut(pocket).cut(self.makeCoverPlate()).edges("|Z").fillet(0.05)

        return body




    def makeCoverPlate (self):
        """ create the outer metal frame of switch
        :rtype: ``solid``
        """
        # body of cover with button hole completely filled
        body = cq.Workplane("XY")\
                    .rect(self.body_length, self.body_width)\
                    .extrude(self.cover_thickness)

        s = cq.StringSyntaxSelector

        body = body.edges("|Z").chamfer(0.6)
       
        body = body.translate((0.0, 0.0, self.cover_offset))\
            .cut(self.makeButton(self.button_oval_length + 0.1, self.button_oval_width + 0.1))

        return body

    def makeButton (self, button_length = None, button_width = None):
        """ create the button of switch, depending on button type
        :rtype: ``solid``
        """
        if button_length is None:
            button_length = self.button_oval_length

        if button_width is None:
            button_width  = self.button_oval_width

        button_height = self.body_height_with_button - self.cover_offset
        dl = self.button_oval_width - self.button_oval_length

        s = cq.StringSyntaxSelector
        body = Polyline(cq.Workplane("XY"))\
            .addMoveTo(button_length / 2.0, -dl / 2.0)\
            .addRadiusArc(-button_length, 0.0, button_length/2.0)\
            .addPoint(0.0, dl)\
            .addRadiusArc(button_length, 0.0, button_length/2.0)\
            .make().extrude(button_height)\
            .edges(">Z").fillet(0.1)


        #body = body.edges("|Z").fillet(0.2)
       
        body = body.translate((0.0, 0.0, self.cover_offset))
        return body




        
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*     class parts_cuk_pts810 (parts_cuk_kmr2)                              *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class parts_cuk_pts810 (parts_cuk_kmr2):
    r"""A class for defining parameter of C&K tactile switches type PTS810. 

    """
        
    def getModelVariant (self, modelName):
        r"""returns the parameter namedtuple from ``all_params`` for the given model name
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :rtype: ``namedtuple``
        """
        return cqMakerCuK_PTS810xTactSwitch (self.all_params[modelName])


    all_params = {

        'SW_SPST_PTS810': partsTactSwitches.Params(
            modelName = 'SW_SPST_PTS810',  
            body_width = 4.2,		    
            body_length = 3.2,	       
            body_height = 1.8,
            pin_pitch = 2.15,
            distance_pinTip_rows = 4.6,
            pin_width = 0.55,
            pin_thickness = 0.1,
            terminal_shape = ShapeOfTerminal.JH,
            button_oval_width = 3.0,
            button_oval_length = 2.2,
            body_height_with_button = 2.5,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS810,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


    }



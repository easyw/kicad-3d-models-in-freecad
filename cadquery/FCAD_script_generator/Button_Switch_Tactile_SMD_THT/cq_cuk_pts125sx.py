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


class ButtonType (ButtonType):
    r"""A class for holding type of button of Omron tactile switch series

    .. note:: will be changed to enum when Python version allows it
    """
    RIBS = 'RIBS'
    r"""RIBS: Round actuator with ribs
    """


class TactSwitchSeries (TactSwitchSeries):
    r"""A class for holding C&K tactile switch series PTS125Sx

    .. note:: will be changed to enum when Python version allows it
    """
    PTS125S = 'PTS125S'
    r"""PTS125S: 12 mm Tact Switch for SMT and THT. 
    """
    WS_TATV = 'WS_TATV'
    r"""WS_TATV: 12 mm Tact Switch for THT from Wuerth Electronics. 
    """
    


#*                                                                          *
#*                                                                          *
#*                                                                          *
#*   class cqMakerCuKPTS125SxTactSwitch (cqMakerTactSwitch)                 *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class cqMakerCuKPTS125SxTactSwitch (cqMakerTactSwitch):
    r"""A class for creating a 3D models from C&K type PTS125S and Wuerth TATV. The parameter are defined in the class ``parts_cuk_pts125s``
    :param parameter: namedtuple containing the variable parameter for building the different 3D models.
    :type  parameter: ``partsTactSwitches.Params``

    """
    
    def __init__(self, parameter):
        cqMakerTactSwitch.__init__(self, parameter)
        
        # get all entries of the params list as dictionary
        args = parameter._asdict()
        self.pad_bottom_height = 0.3

        # for projected button type some more dimensions are needed
        self.button_proj_length_top = self.button_dia - 3.2  
        self.button_proj_length_mid = self.button_dia - 4.0 



    def _paramsForPTS125S (self):
        r"""set the reqired dimensions for tactile switch serie C&K PTS125S

        """
        self.cover_width = self.body_width - 2.2    
        self.cover_length = self.body_length - 2.2 

        self.body_board_distance = 0.0
        self.machineEdges = self.__chamferEdges
        self.cover_body_gap = 0.6

        
    def _paramsForWS_TATV (self):
        r"""set the reqired dimensions for tactile switch serie Wuerth WS_TATV

        """
        self.cover_width = self.body_width - 1.0   
        self.cover_length = self.body_length - 1.0
        self.cover_body_gap = 0.01
        
        self.machineEdges = self.__filletEdges
        


    # Append the series switcher
    cqMakerTactSwitch._serieSwitcher[TactSwitchSeries.PTS125S] = _paramsForPTS125S  
    cqMakerTactSwitch._serieSwitcher[TactSwitchSeries.WS_TATV] = _paramsForWS_TATV  

    def calcChamfer (self, width):
        """ returns a value to be used to chamfer edges. The returned value will be calculated from the given width.
       Normally the width is the x or y dimension of the body, if edges parallel to the Z axis will be chamfered.
        
        :param width: width of the body
        :type width: ``float``

        :rtype: ``solid``
        """
        return 0.3 * width - 2.1

    def calcFillet (self, width):
        """ returns a value to be used to fillet edges. The returned value will be calculated from the given width.
       Normally the width is the x or y dimension of the body, if edges parallel to the Z axis will be filleted.
        
        :param width: width of the body
        :type width: ``float``

        :rtype: ``solid``
        """
        return 0.08 * width


    def __padsBottom (self):
        r"""generates a body to be placed as pads at the bottom of the parts body. Four pads will be generated.

        :rtype: ``solid``
        """
        pad = Polyline(cq.Workplane("XY"), origin=(-self.pin_pitch/2.0 - 1.8, self.body_width/2.0 - 0.5))\
                            .addPoint(1.8, 0.0)\
                            .addPoint(0.0, -3.0)\
                            .addPoint(-3.0, 0.0)\
                            .addPoint(0.0, 1.8)\
                            .make().extrude(self.pad_bottom_height)

        pad = pad.union(pad.mirror("XZ"))
        return pad.union(pad.mirror("YZ"))
        
    def __padsTop (self):
        r"""generates a body to be placed as frame at the bottom of the parts body surrounding the metallic cover sheet.

        :rtype: ``solid``
        """
        body = cq.Workplane("XY").workplane(offset=self.body_height_plastic)\
                 .rect(self.body_length, self.body_width).extrude(self.cover_thickness)

        body = self.machineEdges (body, self.body_width)
                 #.edges("|Z").chamfer(self.calcChamfer(self.body_width))

        pw = self.cover_width +  self.cover_body_gap
        pl = self.cover_length +  self.cover_body_gap
        pocket = cq.Workplane("XY").workplane(offset=self.body_height_plastic)\
                 .rect(pl, pw).extrude(self.cover_thickness)

        pocket = self.machineEdges (pocket, pw)
                 #.edges("|Z").chamfer(self.calcChamfer(pw))

        body = body.cut(pocket)

        pocket = cq.Workplane("XY").workplane(offset=self.body_height_plastic)\
                 .rect(1.5, self.body_width).extrude(self.cover_thickness)

        body = body.cut(pocket)

        return body
    
    def __chamferEdges (self, body, width):
        """ chamfer edges |Z of the given body.
        
        :param body: body to be chamfered
        :type body: ``solid``
        :param width: width of the body
        :type width: ``float``

        :rtype: ``solid``
        """
        return body.edges("|Z").chamfer(self.calcChamfer(width))


    def __filletEdges (self, body, width):
        """ fillet edges |Z of the given body.
        
        :param body: body to be filleted
        :type body: ``solid``
        :param width: width of the body
        :type width: ``float``

        :rtype: ``solid``
        """
        return body.edges("|Z").fillet(self.calcFillet(width))

    
    def makePlasticCase (self):
        """ create the plastic body of the tactile switch
        :rtype: ``solid``
        """
        body = cq.Workplane("XY")\
                 .rect(self.body_length, self.body_width).extrude(self.body_height_plastic-self.pad_bottom_height)\
                 .translate((0.0, 0.0, self.pad_bottom_height))

        body = self.machineEdges (body, self.body_width)
                # .edges("|Z").chamfer(self.calcChamfer(self.body_width))
        
        body = body.union(self._mountingPads((self.cover_length / 2.0 * 0.8, self.cover_width / 2.0 * 0.8), 0.65))
        body = body.union(self.__padsBottom())
        body = body.union(self.__padsTop())
        
        if self.has_pegs:
            body = body.union(self._pegs().translate((0.0, 0.0, self.pad_bottom_height)))

        return body


    def __pocketCoverSide (self):
        l = 0.5  # length of pocket
        w = 1.0  # width of pocket
        pocket = cq.Workplane("XY").box(l, w, 2.0 * self.cover_thickness)\
                   .translate (((self.cover_length - l)/2.0, 1.6, 0.0))
        pocket = pocket.union(pocket.mirror("XZ"))
        return pocket.union(pocket.mirror("YZ"))




    def makeCoverPlate (self):
        """ create the outer metal frame of switch
        :rtype: ``solid``
        """
        # body of cover with button hole completely filled
        body = cq.Workplane("XY")\
                    .rect(self.cover_length, self.cover_width).circle(self.button_dia * 0.52)\
                    .extrude(self.cover_thickness)

        body = self.machineEdges (body, self.cover_width)
                    #.edges("|Z").chamfer(self.calcChamfer(self.cover_width))

        if not (self.button_type == ButtonType.FLAT and self.terminal_shape.startswith ('TH')):
            body = body.cut(self.__pocketCoverSide())
       
        body = body.translate((0.0, 0.0, self.body_height - self.cover_thickness))



        return body

    def makeButton (self):
        """ create the button of switch, depending on button type (flat or projected)
        :rtype: ``solid``
        """
        if self.button_type == ButtonType.RIBS:
            # TODO: Button RIBS 
            x = x

        else:
            return cqMakerTactSwitch.makeButton(self)
        
        return body






        
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*   class parts_cuk_pts125s (partsTactSwitches)                            *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class parts_cuk_pts125s (partsTactSwitches):
    r"""A class for defining parameter of C&K tactile switches type PTS125S. 

    """

        
    def getModelVariant (self, modelName):
        r"""returns the parameter namedtuple from ``all_params`` for the given model name
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :rtype: ``namedtuple``
        """
        return cqMakerCuKPTS125SxTactSwitch (self.all_params[modelName]) 


    all_params = {

        'SW_Push_1P1T_NO_CK_PTS125Sx43PSMTR': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T_NO_CK_PTS125Sx43PSMTR',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.3,
            has_pegs = True,
            pegs_radius = 0.75,
            pegs_pitch = 9.0,
            pegs_heigth = 1.5,
            pin_pitch = 5.0,
            distance_pinTip_rows = 15.3,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 7.0,
            body_height_with_button = 4.3,
            button_type = ButtonType.FLAT,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS125S,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_Push_1P1T_NO_CK_PTS125Sx85PSMTR': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T_NO_CK_PTS125Sx85PSMTR',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.3,
            has_pegs = True,
            pegs_radius = 0.75,
            pegs_pitch = 9.0,
            pegs_heigth = 1.5,
            pin_pitch = 5.0,
            distance_pinTip_rows = 15.3,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 7.0,
            body_height_with_button = 8.5,
            button_type = ButtonType.FLAT,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS125S,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_Push_1P1T_NO_CK_PTS125Sx73PSMTR': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T_NO_CK_PTS125Sx73PSMTR',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.3,
            has_pegs = True,
            pegs_radius = 0.75,
            pegs_pitch = 9.0,
            pegs_heigth = 1.5,
            pin_pitch = 5.0,
            distance_pinTip_rows = 15.3,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 7.0,
            body_height_with_button = 7.3,
            button_type = ButtonType.PROJ,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS125S,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_Push_1P1T_NO_CK_PTS125Sx43SMTR': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T_NO_CK_PTS125Sx43SMTR',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.3,
            pin_pitch = 5.0,
            distance_pinTip_rows = 15.3,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 7.0,
            body_height_with_button = 4.3,
            button_type = ButtonType.FLAT,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS125S,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_Push_1P1T_NO_CK_PTS125Sx85SMTR': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T_NO_CK_PTS125Sx85SMTR',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.3,
            pin_pitch = 5.0,
            distance_pinTip_rows = 15.3,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 7.0,
            body_height_with_button = 8.5,
            button_type = ButtonType.FLAT,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS125S,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_Push_1P1T_NO_CK_PTS125Sx73SMTR': partsTactSwitches.Params(
            modelName = 'SW_Push_1P1T_NO_CK_PTS125Sx73SMTR',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.3,
            pin_pitch = 5.0,
            distance_pinTip_rows = 15.3,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 7.0,
            body_height_with_button = 7.3,
            button_type = ButtonType.PROJ,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS125S,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


        'SW_PUSH-12mm': partsTactSwitches.Params(
            modelName = 'SW_PUSH-12mm',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.3,
            pin_pitch = 5.0,
            distance_pinTip_rows = 12.5,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.THL,
            pin_length_below_body = 3.5,
            button_dia = 7.0,
            body_height_with_button = 7.3,
            button_type = ButtonType.PROJ,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.PTS125S,
            destination_dir = 'Button_Switch_THT.3dshapes',    
            ),


        'SW_PUSH-12mm_Wuerth-430476085716': partsTactSwitches.Params(
            modelName = 'SW_PUSH-12mm_Wuerth-430476085716',  
            body_width = 12.0,		    
            body_length = 12.0,	       
            body_height = 3.5,
            pin_pitch = 5.0,
            distance_pinTip_rows = 12.5,
            pin_width = 1.0,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.THL,
            pin_length_below_body = 3.5,
            button_dia = 7.0,
            body_height_with_button = 8.5,
            button_type = ButtonType.FLAT,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.WS_TATV,
            destination_dir = 'Button_Switch_THT.3dshapes',    
            ),

    }



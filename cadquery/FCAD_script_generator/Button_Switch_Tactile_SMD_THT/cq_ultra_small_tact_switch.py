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
    SIDE_D = 'SIDE_D'
    r"""SIDE_D: Side operational button in D shape (Omron 3BU)
    """
    SIDE_T = 'SIDE_T'
    r"""SIDE_T: Side operational button in T shape (Panasonic EVQPU)
    """


class TactSwitchSeries (TactSwitchSeries):
    r"""A class for holding C&K tactile switch series PTS125Sx

    .. note:: will be changed to enum when Python version allows it
    """
    EVQPU = 'EVQPU'
    r"""EVQPU: Small-sized Side-operational SMD from Panasonic
    """
    EVQP7 = 'EVQP7'
    r"""EVQP7: 3.5 mm × 2.9 mm Side-operational SMD from Panasonic
    """
    B3U3 = 'B3U3'
    r"""B3U: Ultra-small Surface-mounting side actuated Tactile from Omron. 
    """
    


#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*   class cqMakerUltraSmallTactSwitch (cqMakerTactSwitch)                  *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class cqMakerUltraSmallTactSwitch (cqMakerTactSwitch):
    r"""A class for creating a 3D models from C&K type PTS125S and Wuerth TATV. The parameter are defined in the class ``parts_cuk_pts125s``
    :param parameter: namedtuple containing the variable parameter for building the different 3D models.
    :type  parameter: ``partsTactSwitches.Params``

    """
    
    def __init__(self, parameter):
        cqMakerTactSwitch.__init__(self, parameter)
        
        self.button_side_width = parameter.button_side_width if parameter.button_side_width != None else 2.6                        
        self.button_side_height = parameter.button_side_height if parameter.button_side_height != None else 1.4                             
        self.body_length_with_button = parameter.body_length_with_button if parameter.body_length_with_button != None else 4.5                             
        #self. = parameter. if parameter. != None else                              
        
        self.pad_bottom_height = 0.3
        self.button_hole_dia = 1.5

        self.bottom_pocket_depth = 0.1
        self.pin_pocket_edge_length =  0.95
        self.pin_pocket_edge_width =  0.4

        # new cover thickness requires new calculation of body_height_plastic and pad_side_length   
        self.cover_thickness = 0.15   
        self.body_height_plastic = self.body_height - self.cover_thickness
        self.pad_side_length =  self.cover_thickness 

        paramFunction = cqMakerTactSwitch._serieSwitcher.get(self.serie, None)
        if paramFunction == None:     # not a valid terminal_shape
            FreeCAD.Console.PrintMessage(str(self.serie) + ' not a valid member of ' + str(TactSwitchSeries))
            self.make_me = False
        else:  # Call the funktion
            paramFunction (self)


    def _paramsForEVQPU (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVQPU

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height = self.body_height - 0.1
        self.pad_side_height = 0.77
        self.pad_side_width = 0.77
        
        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = 0.6
        self.cover_pin_side_sheet_height = 0.8
                
        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0
        self.pin_height = 0.6

        if self.terminal_shape is ShapeOfTerminal.JH:
            self.pin_bottom_length = 0.6
        elif self.terminal_shape is ShapeOfTerminal.GW:
            self.pin_bottom_length = 1.4

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape

    def _paramsForEVQP7 (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVQP7

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height =  1.1
        self.pad_side_height = 0.5
        self.pad_side_width = 0.4
        
        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = 0.7
        self.cover_pin_side_sheet_height = 0.7
                
        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0
        self.pin_height = 0.6

        if self.terminal_shape is ShapeOfTerminal.JH:
            self.pin_bottom_length = 0.6
        elif self.terminal_shape is ShapeOfTerminal.GW:
            self.pin_bottom_length = 1.0

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape
        self.rotation = -90.0

        
    def _paramsForB3U3 (self):
        r"""set the reqired dimensions for tactile switch serie B3U from Omron

        """
        # for SMD parts with a ground terminal an additional offset is necessary, because the center of the footprints is always in the center of all pins
        self.offsets = (0.0, 0.82, 0.0) if self.with_gnd_pin else (0.0, 0.0, 0.0)

        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height =  0.9
        self.pad_side_height = 0.55
        self.pad_side_width = 0.3

        self.pin_pocket_edge_length =  self.cover_thickness
        self.pin_pocket_edge_width =  self.cover_thickness

        self.cover_plate_with_pin_side_sheets = False

        # new cover thickness requires new calculation of body_height_plastic and pad_side_length   
        self.cover_thickness = 0.15   
        self.body_height_plastic = self.body_height - self.cover_thickness
        self.pad_side_length =  self.cover_thickness 
                
        self.pin_bottom_length = 0.8
                
        # J-hook pins with no upper part
        #self.pin_top_length = 0.0
        #self.pin_top_radius = 0.0
        #self.pin_height = 0.6

        if self.terminal_shape is ShapeOfTerminal.JH:
            self.pin_bottom_length = 0.6
        elif self.terminal_shape is ShapeOfTerminal.GW:
            self.pin_bottom_length = 0.8

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape


    # Append the series switcher
    cqMakerTactSwitch._serieSwitcher[TactSwitchSeries.B3U3] = _paramsForB3U3  
    cqMakerTactSwitch._serieSwitcher[TactSwitchSeries.EVQPU] = _paramsForEVQPU  
    cqMakerTactSwitch._serieSwitcher[TactSwitchSeries.EVQP7] = _paramsForEVQP7  





    def __centralSidePads (self):
        r"""generates a body to be placed (central) at the top side of the parts body. These side pads are the fixing elements for the cover clips.

        :rtype: ``solid``
        """
        body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        h = self.body_height + self.cover_side_height / 2.0 - (self.pad_side_height + self.cover_thickness) * 1.5
        body = cq.Workplane("YZ").workplane(offset=body_length_without_pads / 2.0)\
                 .rect(self.body_width - 3.0 * self.pad_side_width, h).extrude(self.cover_thickness)\
                 .translate ((0.0, 0.0, h / 2.0))

        return body.union(body.mirror("YZ"))


    def makePlasticCase (self):
        body = cqMakerTactSwitch.makePlasticCase (self)
        return body.union(self.__centralSidePads())


    def _coverCentralHole(self):
        """ create a body to cut a central square hole into cover
        :rtype: ``solid``
        """
        body = cq.Workplane("XY").rect(1.0, 1.0).extrude(self.cover_thickness)
        return body


    def _coverFilletCentralHole(self, body):
        """ fillet edges of central rectangle hole in cover
        :param body: The body with hole to fillet 
        :type body: ``solid``
        :rtype: ``solid``
        """
        s = cq.StringSyntaxSelector
        body = body.edges(s(">Z")-s(">Y")-s("<Y")-s("<X")-s(">X")).fillet(self.cover_thickness*0.25)
        return body.edges("|Z").fillet(0.1)

    
    def _makeSideBottomD (self):
        # length, width, height of pusher head
        l_ph = 0.5
        w_ph = self.button_side_width
        h_ph = self.button_side_height
        # length, width, height of guide pusher
        l_gp = self.body_length_with_button - self.body_length / 2.0 - l_ph
        w_gp = w_ph - 0.2
        h_gp = h_ph * 0.43
        #.workplane(offset=self.body_height_plastic)\
        body_gp = cq.Workplane("XY")\
                    .rect(l_gp, w_gp).extrude(h_gp)

        pocket = cq.Workplane("XY")\
                    .rect(l_gp, 0.3).extrude(h_gp).translate ((0.0, 0.4, h_gp / 2.0))

        body_gp = body_gp.cut(pocket)
        body_gp = body_gp.cut(pocket.translate ((0.0, -2.0*0.4, 0.0)))
#l_ph * 0.99)\
        body_ph = cq.Workplane("XY")\
                    .rect(l_ph, w_ph).extrude(-h_ph)\
                    .edges(">X").edges("|Z").chamfer(l_ph * 0.90)\
                    .translate (((l_gp + l_ph) /2.0, 0.0, h_gp + self.cover_thickness))

        body = body_gp.union(body_ph).edges().fillet(0.02)

        return body.translate((l_gp/2.0, 0.0, self.body_height_plastic - h_gp))


    
    def _makeSideBottomT (self):
        # length, width, height of pusher head
        l_ph = 0.5
        w_ph = self.button_side_width
        h_ph = self.button_side_height
        # length, width, height of guide pusher
        l_gp = self.body_length_with_button - self.body_length / 2.0 - l_ph
        w_gp = w_ph - 0.2
        h_gp = h_ph * 0.43
        #.workplane(offset=self.body_height_plastic)\
        body_gp = cq.Workplane("XY")\
                    .rect(l_gp, w_gp).extrude(h_gp)

        pocket = cq.Workplane("XY")\
                    .rect(l_gp, 0.3).extrude(h_gp).translate ((0.0, 0.4, h_gp / 2.0))

        body_gp = body_gp.cut(pocket)
        body_gp = body_gp.cut(pocket.translate ((0.0, -2.0*0.4, 0.0)))

        body_ph = cq.Workplane("XY")\
                    .rect(l_ph, w_ph).extrude(-h_ph)\
                    .translate (((l_gp + l_ph) /2.0, 0.0, h_gp + self.cover_thickness))

        body = body_gp.union(body_ph).edges().fillet(0.02)
            

        return body.translate((l_gp/2.0, 0.0, self.body_height_plastic - h_gp))
    

    def makeButton (self):
        """ create the button of switch, depending on button type (flat or projected)
        :rtype: ``solid``
        """
        if self.button_type is ButtonType.SIDE_D:
            # TODO: Button RIBS 
            return self._makeSideBottomD()

        elif self.button_type is ButtonType.SIDE_T:
            return self._makeSideBottomT()
         
        else:
            return cqMakerTactSwitch.makeButton(self)
        
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

class partsUltraSmallTactSwitches (partsTactSwitches):
    r"""A class for defining parameter of ultra small tactile switches type Omron B3U and Panasonic EVQPU & EVQP7. 

    """

        
    def getModelVariant (self, modelName):
        r"""returns the parameter namedtuple from ``all_params`` for the given model name
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :rtype: ``namedtuple``
        """
        return cqMakerUltraSmallTactSwitch (self.all_params[modelName])
    
    # will be used if Python version allows it
    #try:
    #    # extend the ParamsWithDefault named tuple by 'point'
    #    partsTactSwitches.Params = partsTactSwitches.namedtuple_with_defaults('Params',partsTactSwitches.Params.\
    #        _fields+('button_side_width', 'button_side_height', 'body_length_with_button'))
    #except:
    #    FreeCAD.Console.PrintMessage('invalid or duplicate field names.\r\n')



    all_params = {

        'Panasonic_EVQPUJ_EVQPUA': partsTactSwitches.Params(
            modelName = 'Panasonic_EVQPUJ_EVQPUA',  
            body_width = 4.7,		    
            body_length = 3.5,	       
            body_height = 1.65,
            pin_pitch = 1.7,
            distance_pinTip_rows = 6.4,
            pin_width = 0.6,
            pin_thickness = 0.2,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 2.6,
            button_side_height = 1.4,
            body_length_with_button = 4.5,
            button_type = ButtonType.SIDE_T,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.EVQPU,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'Panasonic_EVQPUK_EVQPUB': partsTactSwitches.Params(
            modelName = 'Panasonic_EVQPUK_EVQPUB',  
            body_width = 4.7,		    
            body_length = 3.5,	       
            body_height = 1.65,
            pin_pitch = 1.7,
            distance_pinTip_rows = 5.5,
            pin_width = 0.6,
            pin_thickness = 0.2,
            terminal_shape = ShapeOfTerminal.JH,
            button_side_width = 2.6,
            button_side_height = 1.4,
            body_length_with_button = 4.5,
            button_type = ButtonType.SIDE_T,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.EVQPU,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'Panasonic_EVQPUL_EVQPUC': partsTactSwitches.Params(
            modelName = 'Panasonic_EVQPUL_EVQPUC',  
            body_width = 4.7,		    
            body_length = 3.5,	       
            body_height = 1.65,
            pin_pitch = 1.7,
            distance_pinTip_rows = 6.4,
            pin_width = 0.6,
            pin_thickness = 0.2,
            has_pegs = True,
            pegs_radius = 0.65/2.0,
            pegs_pitch = 2.75,
            pegs_heigth = 0.5,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 2.6,
            button_side_height = 1.4,
            body_length_with_button = 4.5,
            button_type = ButtonType.SIDE_T,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.EVQPU,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'Panasonic_EVQPUM_EVQPUD': partsTactSwitches.Params(
            modelName = 'Panasonic_EVQPUM_EVQPUD',  
            body_width = 4.7,		    
            body_length = 3.5,	       
            body_height = 1.65,
            pin_pitch = 1.7,
            distance_pinTip_rows = 5.5,
            pin_width = 0.6,
            pin_thickness = 0.2,
            has_pegs = True,
            pegs_radius = 0.65/2.0,
            pegs_pitch = 2.75,
            pegs_heigth = 0.5,
            terminal_shape = ShapeOfTerminal.JH,
            button_side_width = 2.6,
            button_side_height = 1.4,
            body_length_with_button = 4.5,
            button_type = ButtonType.SIDE_T,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.EVQPU,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_SPST_EVQP7A': partsTactSwitches.Params(
            modelName = 'SW_SPST_EVQP7A',  
            body_width = 3.5,		    
            body_length = 2.9,	       
            body_height = 1.35,
            pin_pitch = 1.48,
            distance_pinTip_rows = 4.7,
            pin_width = 0.62,
            pin_thickness = 0.2,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 1.7,
            button_side_height = 1.1,
            body_length_with_button = 3.55,
            button_type = ButtonType.SIDE_T,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.EVQP7,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


        'SW_SPST_EVQP7C': partsTactSwitches.Params(
            modelName = 'SW_SPST_EVQP7C',  
            body_width = 3.5,		    
            body_length = 2.9,	       
            body_height = 1.35,
            pin_pitch = 1.48,
            distance_pinTip_rows = 4.7,
            pin_width = 0.62,
            pin_thickness = 0.2,
            has_pegs = True,
            pegs_radius = 0.65/2.0,
            pegs_pitch = 1.8,
            pegs_heigth = 0.5,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 1.7,
            button_side_height = 1.1,
            body_length_with_button = 3.55,
            button_type = ButtonType.SIDE_T,
            with_gnd_pin = False,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.EVQP7,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),



        'SW_SPST_B3U-3000P-B': partsTactSwitches.Params(
            modelName = 'SW_SPST_B3U-3000P-B',  
            body_width = 3.0,		    
            body_length = 2.5,	       
            body_height = 1.2,
            pin_pitch = 0.0,
            distance_pinTip_rows = 4.0,
            pin_width = 1.4,
            pin_thickness = 0.2,
            has_pegs = True,
            pegs_radius = 0.65/2.0,
            pegs_pitch = 0.0,
            pegs_heigth = 0.5,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 1.7,
            button_side_height = 1.2,
            body_length_with_button = 3.2,
            button_type = ButtonType.SIDE_D,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3U3,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


        'SW_SPST_B3U-3000P': partsTactSwitches.Params(
            modelName = 'SW_SPST_B3U-3000P',  
            body_width = 3.0,		    
            body_length = 2.5,	       
            body_height = 1.2,
            pin_pitch = 0.0,
            distance_pinTip_rows = 4.0,
            pin_width = 1.4,
            pin_thickness = 0.2,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 1.7,
            button_side_height = 1.2,
            body_length_with_button = 3.2,
            button_type = ButtonType.SIDE_D,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3U3,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


        'SW_SPST_B3U-3100P-B': partsTactSwitches.Params(
            modelName = 'SW_SPST_B3U-3100P-B',  
            body_width = 3.0,		    
            body_length = 2.5,	       
            body_height = 1.2,
            pin_pitch = 0.0,
            distance_pinTip_rows = 4.0,
            pin_width = 1.4,
            pin_thickness = 0.2,
            has_pegs = True,
            pegs_radius = 0.65/2.0,
            pegs_pitch = 0.0,
            pegs_heigth = 0.5,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 1.7,
            button_side_height = 1.2,
            body_length_with_button = 3.2,
            button_type = ButtonType.SIDE_D,
            with_gnd_pin = True,
            gnd_pin_tip_to_center = 1.9,
            gnd_pin_width = 0.5,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3U3,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


        'SW_SPST_B3U-3100P': partsTactSwitches.Params(
            modelName = 'SW_SPST_B3U-3100P',  
            body_width = 3.0,		    
            body_length = 2.5,	       
            body_height = 1.2,
            pin_pitch = 0.0,
            distance_pinTip_rows = 4.0,
            pin_width = 1.4,
            pin_thickness = 0.2,
            terminal_shape = ShapeOfTerminal.GW,
            button_side_width = 1.7,
            button_side_height = 1.2,
            body_length_with_button = 3.2,
            button_type = ButtonType.SIDE_D,
            with_gnd_pin = True,
            gnd_pin_tip_to_center = 1.9,
            gnd_pin_width = 0.5,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3U3,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


    }



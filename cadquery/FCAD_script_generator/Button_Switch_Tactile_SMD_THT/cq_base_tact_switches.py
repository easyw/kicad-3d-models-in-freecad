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
from cq_parameters import ShapeOfTerminal, ButtonType, partParamsTactSwitches, ButtonRing

import collections
from collections import namedtuple


from  cq_base_model import PartBase, Polyline  # modules parameters

class TactSwitchSeries:
    r"""A class for holding Omron tactile switch series

    .. note:: will be changed to enum when Python version allows it
    """
    # Omron series
    B3F = 'B3F'
    r"""B3F: Through hole-mounting switches
    """
    B3U1 = 'B3U1'
    r"""B3U1: Ultra-small Surface-mounting Tactile
    """
    B3FS = 'B3FS'
    r"""B3FS: 6 × 6-mm Surface-mounting Switches
    """
    B3S = 'B3S'
    r"""B3S: Surface-mounting Switches with a Sealed Structure for High Reliability.
    """
    B3SL = 'B3SL'
    r"""B3S: Surface-mounting Switches with a Sealed Structure
    """
    # C&K
    KSC = 'KSC'
    r"""KSC: Sealed Tact Switch for SMT. Hard and soft actuator.
    """
    KSx0A = 'KSx0A'
    r"""KSx0A: KSA & KSL Series; Sealed Tact Switch
    """
    # Panasonic
    EVPBF = 'EVPBF'
    r"""EVPBF: 6mm Square Middle Travel. SMD Light Touch Switch. 
    """
    EVQP0 = 'EVQP0'
    r"""EVQP0: 6 mm Square Thin Type SMD Light Touch Switches. 
    """
    EVQP2 = 'EVQP2'
    r"""EVQP2: 4.7 mm × 3.5 mm SMD Light Touch Switches 
    """
    EVQPL = 'EVQPL'
    r"""EVQPL: 4.9 mm Square SMD Light Touch Switches 
    """
    # Alps
    SKOG = 'SKOG'
    r"""SKOG: 5.2 mm Square Low-profile (Surface Mount Type)
    """
    SKRK = 'SKRK'
    r"""SKRK: 3.9 × 2.9 mm Compact (Surface Mount Type)
    """


#*                                                                          *
#*                                                                          *
#*                                                                          *
#*   class cqMakerTactSwitch (PartBase, partParamsTactSwitches)             *
#*                                                                          *
#*                                                                          *
#*                                                                          *
#*                                                                          *

class cqMakerTactSwitch (PartBase, partParamsTactSwitches):
    r"""A class for creating a 3D models which parameter are defined in the class ``partsTactSwitches``
    :param parameter: namedtuple containing the variable parameter for building the different 3D models.
    :type  parameter: ``partsTactSwitches.Params``

    """
    
    def __init__(self, parameter):
        PartBase.__init__(self, parameter)
        partParamsTactSwitches.__init__(self, parameter)
        
        # get all entries of the params list as dictionary
        args = parameter._asdict()
            
        self.serie = parameter.serie                                                                                                # The component serie
        self.destination_dir = parameter.destination_dir if parameter.destination_dir != None else  'Button_Switch_SMD.3dshapes' 
        self.button_type = parameter.button_type if parameter.button_type != None else ButtonType.FLAT                              # Type of button from class ButtonType
        self.with_gnd_pin = parameter.with_gnd_pin if parameter.with_gnd_pin != None else False                                     # boolean: True if Ground Terminal is present
        self.cover_color_key = parameter.cover_color_key if parameter.cover_color_key != None else 'metal grey pins' 	            # Cover color
        self.body_color_key = parameter.body_color_key if parameter.body_color_key != None else 'black body'	                    # Body colour
        self.button_color_key = parameter.button_color_key if parameter.button_color_key != None else 'black body'                  # botton color
        self.pin_color_key = parameter.pin_color_key if parameter.pin_color_key != None else 'metal grey pins'	                    # Pin color
        self.gnd_pin_tip_to_center = parameter.gnd_pin_tip_to_center if parameter.gnd_pin_tip_to_center != None else 4.0            # pos of GND pin rel. to center of body, measured to tip of pin
        self.no_gnd_pins = parameter.no_gnd_pins if parameter.no_gnd_pins != None else 1                                            # number of groung pins (1 or 2); default: 1                   
        self.offset_gnd_pin = parameter.offset_gnd_pin if parameter.offset_gnd_pin != None else 0.0                                 # offset of ground pin to middle of housing; default: 0.0                            
        self.gnd_pin_width = parameter.gnd_pin_width if parameter.gnd_pin_width != None else self.pin_width                                 # offset of ground pin to middle of housing; default: 0.0                            
        
        # Default parameter
        self.cover_plate_with_pin_side_sheets = False
        self.pin_gw_angle = 80.0        
        self.edge_fillet = None     # if not None the outer edges of body and cover will be fillet
        self.edge_chamfer = None    # if not None the outer edges of body and cover will be chamfer

        # for SMD parts with a ground terminal an additional offset is necessary, because the center of the footprints is always in the center of all pins
        # The offset will be set to None and must be defined within param function _paramsXXX
        # TODO gnd_pin_tip_to_center is not the right dimension to be used for offset calculation. Check new algorithm with Parts having GW pin and GND Pin
        if self.with_gnd_pin and self.terminal_shape == ShapeOfTerminal.GW:
            self.offsets = None
            #offsY = (self.gnd_pin_tip_to_center - self.pin_pitch / 2.0) / 2.0
            #self.offsets = tuple(map(operator.add, self.offsets, (0.0, offsY, 0.0)))

        # Call of function defining dimensions depending on the serie of terminals
        paramFunction = self._serieSwitcher.get(self.serie, None)
        if paramFunction == None:     # not a valid terminal_shape
            FreeCAD.Console.PrintMessage(str(self.serie) + ' not a valid member of ' + str(TactSwitchSeries))
            self.make_me = False
        else:  # Call the funktion
            paramFunction (self)
        
        
    def _paramsForB3F (self):
        r"""set the reqired dimensions for tactile switch serie Omron B3F

        """
        self.cover_plate_with_side_sheets = False
        self.tht_pin_lower_clamp_angel = 25.0
        self.tht_pin_clamp_extension = 0.5
        self.edge_chamfer = 0.3


    def _paramsForB3FS (self):
        r"""set the reqired dimensions for tactile switch serie Omron B3FS

        """
        self.cover_plate_with_side_sheets = True
        self.cover_side_pocket_width = self.pad_side_width = 2.0
        # side pads and cover side clips
        self.body_side_pads = self._padsSideCenter
        self.cover_side_clips = self._coverSideSheetsClosed

        self.button_proj_hight_bot = 0.5
        self.button_proj_hight_top = 1.8
        self.button_proj_hight_mid = self.button_height - self.button_proj_hight_bot - self.button_proj_hight_top
        self.pin_bottom_length = 0.5


    def _paramsForB3S (self):
        r"""set the reqired dimensions for tactile switch serie Omron B3S

        """
        # for SMD parts with a ground terminal an additional offset is necessary, because the center of the footprints is always in the center of all pins
        self.offsets = (0.0, 0.92, 0.0) if self.with_gnd_pin else (0.0, 0.0, 0.0)

        self.cover_plate_with_side_sheets = True
        self.cover_side_clips_bottom_width = 1.7
        # side pads and cover side clips
        self.body_side_pads = self._padsSideCenter
        self.cover_side_clips = self._coverSideSheetsOpen


    def _paramsForB3SL (self):
        r"""set the reqired dimensions for tactile switch serie Omron B3SL

        """
        self.cover_plate_with_side_sheets = True
        self.cover_side_pocket_width = self.pad_side_width = 3.0
        # side pads and cover side clips
        self.body_side_pads = self._padsSideCenter
        self.cover_side_clips = self._coverSideSheetsClosed

        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0

    def _paramsForB3U1 (self):
        r"""set the reqired dimensions for tactile switch serie B3U-1x from Omron

        """
        # for SMD parts with a ground terminal an additional offset is necessary, because the center of the footprints is always in the center of all pins
        self.offsets = (0.0, 0.82, 0.0) if self.with_gnd_pin else (0.0, 0.0, 0.0)
        
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height =  0.9
        self.pad_side_height = 0.55
        self.pad_side_width = 0.3

        self.pin_pocket_edge_length =  self.cover_thickness
        self.pin_pocket_edge_width =  self.cover_thickness

        # new cover thickness requires new calculation of body_height_plastic and pad_side_length   
        self.cover_thickness = 0.15   
        self.body_height_plastic = self.body_height - self.cover_thickness
        self.pad_side_length =  self.cover_thickness 
                
        self.pin_bottom_length = 0.8

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape
        

    def _paramsForKSC (self):
        r"""set the reqired dimensions for tactile switch serie C&K KSC7

        """
        self.cover_plate_with_side_sheets = True
        self.cover_side_pocket_width = self.pad_side_width = 4.1

        # button has a plate below cover
        self.button_has_base_plate = True;
        self.button_base_height = self.body_height * 0.3
        self.body_height_plastic -= self.button_base_height
        self.pad_side_height -= self.button_base_height

        # side pads and cover side clips
        self.body_side_pads = self._padsSideCenter
        self.cover_side_clips = self._coverSideSheetsClosed

        self.body_board_distance = 0.1


    def _paramsForEVPBF (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVPBF

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height = 1.8
        self.pad_side_height = 0.6
        self.pad_side_width = 1.2 
        
        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = self.pin_pitch - self.pin_width
        self.cover_pin_side_sheet_height = 0.8
        
        self.button_hole_dia = 3.7
        
        # button has a plate below cover
        self.button_has_base_plate = True;
        self.button_base_height = self.cover_pin_side_sheet_height - self.cover_thickness
        self.body_height_plastic -= self.button_base_height

        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape
        
    def _paramsForEVQP0 (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVPQP0

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height = 1.25
        self.pad_side_height = 0.5
        self.pad_side_width = 1.2 
       
        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = self.pin_pitch - self.pin_width
        self.cover_pin_side_sheet_height = 0.5
        
        self.button_hole_dia = 2.5
        
        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape

        
    def _paramsForEVQP2 (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVPQP0

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height = 1.2
        self.pad_side_height = 0.65
        self.pad_side_width = 0.65 
       
        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = (self.pin_pitch - self.pin_width) * 0.9
        self.cover_pin_side_sheet_height = 0.8
        
        self.button_hole_dia = 2.2
        
        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0

        self.pin_pocket_edge_length =  1.2
        self.pin_height = 0.6

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape
        
        
    def _paramsForEVQPL (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVPQP0

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height = 0.45
        self.cover_solid_side_width = 2.5
       
        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = 1.2
        self.cover_pin_side_sheet_height = 0.6
        
        self.button_hole_dia = 3.2
        
        # J-hook pins with no upper part
        self.pin_top_length = 0.0
        self.pin_top_radius = 0.0
        self.pin_height = self.body_height / 2.0

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = None
        self.cover_side_clips = self._coverSideSheetsSolid

        self.rotation = 0.0

    def _paramsForKSx0A (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVPQP0

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height =2.2
               
        self.button_hole_dia = 3.2
        
        self.body_board_distance = 0.0

        self.tht_pin_lower_clamp_angel = 25.0
        self.tht_pin_clamp_extension = 0.5

        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = 3.0
        self.cover_pin_side_sheet_height = 2.0 * self.cover_thickness

        # make special pads and cover clips
        self.cover_side_clips_bottom_width = 2.0
        self.cover_side_pocket_width = self.pad_side_width =4.6
        
        self.button_has_base_plate = True;
        self.button_base_height = self.body_height * 0.3
        self.body_height_plastic -= self.button_base_height
        self.pad_side_height -= self.button_base_height

        # side pads and cover side clips
        self.body_side_pads = self._padsSideCenter
        self.cover_side_clips = self._coverSideSheetsOpen

    def _paramsForSKOG (self):
        r"""set the reqired dimensions for tactile switch serie Panasonic EVPQP0

        """
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height = 0.4
        self.cover_solid_side_width = 2.4
       
        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = 2.4
        self.cover_pin_side_sheet_height = 0.4

        self.body_width -= 2.0 * self.cover_thickness

        self.pin_height = 0.25
        
        self.button_hole_dia = 2.1

        self.edge_chamfer = 1.2
        self.pin_bottom_length = 0.6
        self.pin_gw_angle = 60.0
        
        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = None
        self.cover_side_clips = self._coverSideSheetsSolid
        

    def _paramsForSKRK (self):
        r"""set the reqired dimensions for tactile switch serie SKRK from E-Switch

        """
        # for SMD parts with a ground terminal an additional offset is necessary, because the center of the footprints is always in the center of all pins
        self.offsets = (0.0, 0.82, 0.0) if self.with_gnd_pin else (0.0, 0.0, 0.0)
        
        self.cover_plate_with_side_sheets = True # cover side sheet has T-shape, plate height and pad size has to be defined 
        self.cover_side_height =  1.2
        self.pad_side_height = 0.7
        self.pad_side_width = 0.5

        self.pin_pocket_edge_length =  self.cover_thickness
        self.pin_pocket_edge_width =  self.cover_thickness

        self.cover_plate_with_pin_side_sheets = True
        self.cover_pin_side_sheet_width = 0.5
        self.cover_pin_side_sheet_height = 0.7

        # new cover thickness requires new calculation of body_height_plastic and pad_side_length   
        self.cover_thickness = 0.15   
        self.body_height_plastic = self.body_height - self.cover_thickness
        self.pad_side_length =  self.cover_thickness 
                
        self.pin_bottom_length = 0.8

        self.body_board_distance = 0.0
        # make special pads and cover clips
        self.body_side_pads = self._padSideEdge
        self.cover_side_clips = self._coverSideSheets_T_Shape
        

    _serieSwitcher = {
        TactSwitchSeries.B3F:       _paramsForB3F,
        TactSwitchSeries.B3FS:      _paramsForB3FS,
        TactSwitchSeries.B3S:       _paramsForB3S, 
        TactSwitchSeries.B3SL:      _paramsForB3SL,
        TactSwitchSeries.B3U1:      _paramsForB3U1,
        TactSwitchSeries.KSC:       _paramsForKSC,
        TactSwitchSeries.KSx0A:     _paramsForKSx0A,
        TactSwitchSeries.EVPBF:     _paramsForEVPBF,
        TactSwitchSeries.EVQP0:     _paramsForEVQP0,
        TactSwitchSeries.EVQP2:     _paramsForEVQP2,
        TactSwitchSeries.EVQPL:     _paramsForEVQPL,
        TactSwitchSeries.SKOG:      _paramsForSKOG,
        TactSwitchSeries.SKRK:      _paramsForSKRK,

        }



    def get_dest_3D_dir(self):
        r"""get the destination directory for the 3D model export

        :rtype: string
        """
        return self.destination_dir

    def _padsSideCenter (self):
        r"""generates a body to be placed (central) at the top side of the parts body. These side pads are the fixing elements for the cover clips.

        :rtype: ``solid``
        """
        pad = cq.Workplane("XY", origin=((self.body_length - self.pad_side_length) / 2.0, 0.0, self.body_height_plastic - self.pad_side_height))\
                    .rect(self.pad_side_length, self.pad_side_width).extrude(self.pad_side_height)

        return pad.union(pad.mirror("YZ"))

    def _padSideEdge (self):
        r"""generates a body to be placed (left and right) at the side of the parts body. These side pads are the fixing elements for the cover clips (upside down T-shape).

        :rtype: ``solid``
        """
        pad = cq.Workplane("XY",  origin=((self.body_length - self.pad_side_length) / 2.0, (self.body_width - self.pad_side_width) / 2.0))\
            .workplane(offset=self.body_height_plastic - self.pad_side_height)\
            .rect(self.pad_side_length, self.pad_side_width).extrude(self.pad_side_height)\
            .edges(">Z").edges(">X").fillet(self.cover_thickness*0.99)
        pad = pad.union(pad.mirror("XZ"))
        return pad.union(pad.mirror("YZ"))

    def __pocketEdgePinBottom (self):
        r"""generates a body used to cut deepenings at the bottom of the parts body, where the pins are placed.

        :rtype: ``solid``
        """
        body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        return cq.Workplane("XY")\
                 .rect((body_length_without_pads - self.pin_pocket_edge_length), (self.body_width - self.pin_pocket_edge_width), forConstruction=True) \
                 .vertices().rect(self.pin_pocket_edge_length, self.pin_pocket_edge_width).extrude(self.bottom_pocket_depth)
            
    def _mountingPads (self, pos, r=0.65):
        r"""generates a four cylinders placed at the top of the parts body to fix the cover sheet for covers not having side clips.

        :rtype: ``solid``
        """
        pad = cq.Workplane("XY").workplane(offset=self.body_height_plastic).circle(r)\
                .extrude(2.0 * self.cover_thickness).edges(">Z").fillet(0.05)\
                .translate((pos[0], pos[1], 0.0))

        pad = pad.union(pad.mirror("YZ"))
                
        return pad.union(pad.mirror("XZ"))
    
    def _pegs(self):
        r"""generates one or more cylinders to be placed as reference pegs at the bottom of the parts body.

        :rtype: ``solid``
        """
        peg = cq.Workplane("XY").circle(self.pegs_radius)\
                .extrude(-self.pegs_heigth).edges("<Z").chamfer(self.pegs_radius*0.3)

        peg = peg.translate((self.pegs_pitch / 2.0, 0.0, 0.0))
        peg = peg.union(peg.mirror("YZ"))

        return peg


    def makePlasticCase (self):
        """ create the plastic body of the tactile switch
        :rtype: ``solid``
        """
        body = cq.Workplane("XY")
        if self.cover_plate_with_side_sheets:
            body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
            body = body.rect(body_length_without_pads, self.body_width).extrude(self.body_height_plastic)


            if self.body_side_pads is not None:
                body = body.union(self.body_side_pads())

            # edgeFilter = '<({0:5.2f}, 0.0, 0.0)'.format(-(self.body_length/2.0-0.1))


        else: 
            body = body.rect(self.body_length, self.body_width).extrude(self.body_height_plastic)
                        
            body = body.union(self._mountingPads((self.body_length / 2.0 * 0.7, self.body_width / 2.0 * 0.7), self.body_length * 0.1))


        if self.edge_fillet is not None:
            body = body.edges("|Z").fillet(self.edge_fillet)

        if self.edge_chamfer is not None:
            body = body.edges("|Z").chamfer(self.edge_chamfer)

        body = body.cut(self.__pocketEdgePinBottom())

        if self.has_pegs:
            body = body.union(self._pegs())

        return body



    
    def _coverSideSheetsClosed (self):
        r"""generates a body used as a side clip of the top cover sheet. The shape of the side clip is a closed frame.
        The side clips will be placed at the sides where are no pins.

        :rtype: ``solid``
        """
        body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        body = Polyline(cq.Workplane("YZ").workplane(offset=body_length_without_pads / 2.0))\
            .addMoveTo(-self.cover_side_pocket_width / 2.0, self.body_height)\
            .addPoint(-(self.body_width - self.cover_side_pocket_width) / 2.0, 0.0)\
            .addPoint(0.0, -self.cover_side_height)\
            .addPoint(self.body_width, 0.0)\
            .addPoint(0.0, self.cover_side_height)\
            .addPoint(-(self.body_width - self.cover_side_pocket_width) / 2.0, 0.0)\
            .addPoint(0.0, -(self.cover_side_pocket_heigth + self.cover_thickness))\
            .addPoint(-self.cover_side_pocket_width, 0.0)\
            .make().extrude(self.cover_thickness).edges(">Z").edges(">X").fillet(self.cover_thickness*0.99)

        #body = body.edges("|Z").fillet(0.05)
        body = body.edges("<Z").fillet(0.05)

        body = body.union(body.mirror("YZ"))

        return body

    def _coverSideSheetsOpen (self):
        r"""generates a body used as a side clip of the top cover sheet. The shape of the side clip is a frame, open at the bottom.
        The side clips will be placed at the sides where are no pins.

        :rtype: ``solid``
        """
        body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        body = Polyline(cq.Workplane("YZ").workplane(offset=body_length_without_pads / 2.0))\
            .addMoveTo(-self.cover_side_pocket_width / 2.0, self.body_height)\
            .addPoint(-(self.body_width - self.cover_side_pocket_width) / 2.0, 0.0)\
            .addPoint(0.0, -self.cover_side_height)\
            .addPoint(self.cover_side_clips_bottom_width, 0.0)\
            .addPoint(0.0, self.cover_side_height - self.cover_side_pocket_heigth - self.cover_thickness)\
            .addPoint(-self.cover_side_clips_bottom_width + (self.body_width - self.cover_side_pocket_width) / 2.0, 0.0)\
            .make().extrude(self.cover_thickness).edges(">Z").edges(">X").fillet(self.cover_thickness*0.99)

        #body = body.edges("|Z").fillet(0.05)
        body = body.edges("<Z").fillet(0.05)

        body = body.union(body.mirror("XZ"))
        body = body.union(body.mirror("YZ"))

        return body

    def _coverSideSheets_T_Shape (self):
        r"""generates a body used as a side clip of the top cover sheet. The shape of the side clip is like an upside down T.
        The side clips will be placed at the sides where are no pins.

        :rtype: ``solid``
        """
        body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        h = self.body_height -self.body_height_plastic + self.pad_side_height
        body = Polyline(cq.Workplane("YZ").workplane(offset=body_length_without_pads / 2.0))\
            .addMoveTo(0.0, self.body_height)\
            .addPoint(-(self.body_width / 2.0 - self.pad_side_width), 0.0)\
            .addPoint(0.0, -h)\
            .addPoint(-self.pad_side_width / 2.0, 0.0)\
            .addPoint(0.0, -(self.cover_side_height  - h))\
            .addPoint(self.pad_side_width, 0.0)\
            .addPoint(0.0, (self.cover_side_height  - h) * 1.5)\
            .addPoint((self.body_width - 3.0 * self.pad_side_width) / 2.0, 0.0)\
            .addMirror().make().extrude(self.cover_thickness).edges(">Z").edges(">X").fillet(self.cover_thickness*0.99)\

        #body = body.edges("|Z").fillet(0.05)
        body = body.edges("<Z").fillet(0.05)

        body = body.union(body.mirror("XZ"))
        body = body.union(body.mirror("YZ"))

        return body


    def _coverSideSheetsSolid (self):
        r"""generates a body used as a side clip of the top cover sheet. The shape of the side clip is a rectangle.
        The side clips will be placed at the sides where are no pins.

        :rtype: ``solid``
        """
        body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        body = cq.Workplane("YZ").workplane(offset=body_length_without_pads / 2.0)\
            .box(self.cover_solid_side_width, self.cover_side_height, self.cover_thickness)\
            .edges(">Z").edges(">X").fillet(self.cover_thickness*0.99)\
            .translate((self.cover_thickness / 2.0, 0.0, self.body_height - self.cover_side_height / 2.0))

        body = body.union(body.mirror("YZ"))

        return body

    def __coverPinSideSheets (self):
        r"""generates a body used as a side clip of the top cover sheet. The shape of the side clip is a rectangle.
        The side clips will be placed at the sides where the pins are.

        :rtype: ``solid``
        """
        body = cq.Workplane("XZ").box(self.cover_pin_side_sheet_width, self.cover_pin_side_sheet_height, self.cover_thickness)\
                .translate ((0.0, (self.body_width + self.cover_thickness)/2.0, \
                    self.body_height - (self.cover_pin_side_sheet_height) / 2.0))\
                .edges(">Z").edges(">Y").fillet(self.cover_thickness*0.99).edges(">Y").fillet(0.05)

        return body.union(body.mirror("XZ"))

    def _buttonRingRound (self):
        r"""generates a cylindric body used as a guide ring of the push button, placed on top of the cover sheet.

        :rtype: ``solid``
        """
        body = cq.Workplane("XY").workplane(offset=self.cover_thickness)\
                    .circle(self.button_ring_radius)\
                    .extrude(self.button_ring_heigth).edges(">Z").edges("%CIRCLE").fillet(0.25)

        return body

    def _buttonRingOctagon (self):
        r"""generates a octagone body used as a guide element of the push button, placed on top of the cover sheet.

        :rtype: ``solid``
        """
        body = cq.Workplane("XY").workplane(offset=self.cover_thickness)\
                    .rect(self.button_ring_length, self.button_ring_width)\
                    .extrude(self.button_ring_heigth)\
                    .edges("|Z").chamfer(self.button_ring_width*0.2).edges("|Z").fillet(self.button_ring_width*0.1)
                    #.edges(">Z").edges("%CIRCLE").fillet(0.25)

        return body


    def _makeGndPin (self):
        r"""generates a pin connected to the top metallic cover sheet used as a ground pin.

        :rtype: ``solid``
        """
        if self.terminal_shape.startswith ('TH'):
            # we must change pin thickness, but need to change it back
            pt = self.cover_thickness  # new pin thickness

            # change values
            pt, self.pin_thickness = self.pin_thickness, pt
            self.gnd_pin_width, self.pin_width = self.pin_width, self.gnd_pin_width
                
            # the gnd pin is connected to cover, thus the length must be:
            pl = self.body_height - self.cover_thickness + self.pin_length_below_body + \
                    self.cover_thickness + self.body_board_distance

            top_length = self.gnd_pin_tip_to_center - self.body_length / 2.0 
            gndPin = self._make_angled_pin (pl, top_length, 0.0, 'THT')\
                .rotate ((0,0,0), (1,0,0), -90.0)\
                .rotate ((0,0,0), (0,0,1), -90.0)\
                .translate ((-self.body_length/2.0 + self.cover_thickness , 0.0, self.body_height - self.cover_thickness + self.pin_thickness / 2.0))

            # change back
            pt, self.pin_thickness = self.pin_thickness, pt
            self.gnd_pin_width, self.pin_width = self.pin_width, self.gnd_pin_width

        elif self.terminal_shape is ShapeOfTerminal.GW:
            # we must change some pin dimensions, but need to change them back
            # the gnd pin is connected to cover at position (body_width / 2.0), thus the length must be:
            pl = self.gnd_pin_tip_to_center - self.body_length / 2.0 + self.cover_thickness # (self.pin_bottom_length 
            pt = self.cover_thickness  # new pin thickness

            # change values
            pl, self.pin_length = self.pin_length, pl
            pt, self.pin_thickness = self.pin_thickness, pt
            self.gnd_pin_width, self.pin_width = self.pin_width, self.gnd_pin_width

            # check if bottom length fits to overall GW pin length, if not we must shorten bottom length
            bl = min (self.pin_bottom_length, self.pin_length - 2.0 * self.pin_thickness) # 1 x thickness + 2 x radius (1/2 thickness)
            ri = self.pin_thickness / 2.0
            gndPin = self._make_gullwing_pin (self.body_height - self.cover_thickness + self.body_board_distance, bl, ri, ri)\
                .rotate ((0,0,0), (0,0,1), 90.0).translate ((-self.body_length / 2.0 + self.cover_thickness, 0.0,  -self.body_board_distance))

            # change back
            pl, self.pin_length = self.pin_length, pl
            pt, self.pin_thickness = self.pin_thickness, pt
            self.gnd_pin_width, self.pin_width = self.pin_width, self.gnd_pin_width

        else:
            # we must change some pin dimensions, but need to change them back
            # the gnd pin is connected to cover at position (body_width / 2.0), thus the length must be:
            pt = self.cover_thickness  # new pin thickness

            # change values
            pt, self.pin_thickness = self.pin_thickness, pt
            self.gnd_pin_width, self.pin_width = self.pin_width, self.gnd_pin_width

            top_len = self.gnd_pin_tip_to_center - self.body_length / 2.0 
            gndPin = self._make_Jhook_pin (self.body_height - self.cover_thickness + self.body_board_distance, self.pin_bottom_length/2.0, top_len, 0.01, 0.01)\
                .rotate ((0,0,0), (0,0,1), 90.0).translate ((-(self.gnd_pin_tip_to_center - self.pin_thickness), -self.offset_gnd_pin,  -self.body_board_distance))

            # change back
            pt, self.pin_thickness = self.pin_thickness, pt
            self.gnd_pin_width, self.pin_width = self.pin_width, self.gnd_pin_width

        if self.no_gnd_pins == 2:
            gndPin = gndPin.union(gndPin.rotate((0,0,0), (0,0,1), 180.0))

        return gndPin


    def _coverCentralHole(self):
        """ create a body to cut the central hole for the button into cover
        :rtype: ``solid``
        """
        # even if button ring does not exist, we can extend the height of the cutting cylinder up to cover_thickness+button_ring_heigth
        body = cq.Workplane("XY").circle(self.button_hole_dia / 2.0).extrude(self.cover_thickness + self.button_ring_heigth)
        return body


    def _coverFilletCentralHole(self, body):
        """ fillet edges of central circular hole in cover
        :param body: The body with hole to fillet 
        :type body: ``solid``
        :rtype: ``solid``
        """
        return body.edges("%CIRCLE").fillet(self.cover_thickness*0.25)

    def makeCoverPlate (self):
        """ create the outer metallic frame of switch
        :rtype: ``solid``
        """
        if self.cover_plate_with_side_sheets:
            body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        else:
            body_length_without_pads = self.body_length
        
        body = cq.Workplane("XY")\
                    .rect(body_length_without_pads, self.body_width)\
                    .extrude(self.cover_thickness)

        if self.edge_fillet is not None:
            body = body.edges("|Z").fillet(self.edge_fillet)

        if self.edge_chamfer is not None:
            body = body.edges("|Z").chamfer(self.edge_chamfer)


        if self.button_ring is not ButtonRing.NONE:
            if self.button_ring is ButtonRing.ROUND:
                body = body.union(self._buttonRingRound())
            elif self.button_ring is ButtonRing.OCTA:
                body = body.union(self._buttonRingOctagon())
        
        body = body.cut(self._coverCentralHole())
        body = self._coverFilletCentralHole(body)

        body = body.translate((0.0, 0.0, self.body_height - self.cover_thickness))

        if self.cover_plate_with_side_sheets:
            body = body.union(self.cover_side_clips())

        if self.cover_plate_with_pin_side_sheets:
            body = body.union(self.__coverPinSideSheets())\

        if self.with_gnd_pin:
            body = body.union(self._makeGndPin())
            #body = (self._makeGndPin())

        return body

    def _buttonBasePlate (self):
        """ For some tactile switches the round button has a rectangluar base plate placed below the top metallic cover.
      
        Create a body to be used as a base plate of the button.
        :rtype: ``solid``
        """
        if self.cover_plate_with_side_sheets:
            body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        else:
            body_length_without_pads = self.body_length
            
        body = cq.Workplane("XY").workplane(offset=self.body_height - self.cover_thickness)\
            .rect(body_length_without_pads + 0.01, self.body_width + 0.01).extrude(-self.button_base_height)\
            .edges("|Z").fillet(0.5)

        return body


    def makeButton (self):
        """ create the button of switch, depending on button type
        :rtype: ``solid``
        """
        h = self.button_height if self.button_type == ButtonType.FLAT else self.button_proj_hight_bot
            
        body = cq.Workplane("XY")\
            .workplane(offset=self.body_height - self.cover_thickness).circle(self.button_dia/2.0).extrude(h)
            
        if h > 0.1:
            body = body.edges(">Z").edges("%CIRCLE").fillet(0.1)

        if self.button_has_base_plate:
            body = body.union(self._buttonBasePlate())

        if self.button_type == ButtonType.PROJ:
            proj = cq.Workplane("XY").workplane(offset=self.body_height - self.cover_thickness + h)\
                .rect(self.button_proj_length_mid, self.button_proj_length_mid).extrude(self.button_proj_hight_mid)\
                .edges("|Z").fillet(0.05)
            body = body.union(proj)
            proj = cq.Workplane("XY").workplane(offset=self.body_height - self.cover_thickness + h + self.button_proj_hight_mid)\
                .rect(self.button_proj_length_top, self.button_proj_length_top)\
                .circle(self.button_proj_length_top/3.5)\
                .extrude(self.button_proj_hight_top)\
                .edges("|Z").fillet(0.2).edges(">Z").edges("|X").fillet(0.2)#.edges(">Z").edges("|Y").fillet(0.2)
            body = body.union(proj)


        return body


    def _duplicatePins (self, onePin, noPins=None, pitch=None):
        r"""Duplicates all pins from first pin.

        :param onePin: The first pin of the model
        :type  onePin: ``solid``

        :param codeFormat:
        :type  codeFormat: ``CodeFormat`` default: ``CodeFormat.REAL``
        :return: all pins
        :rtype: ``solid``
        """

        if noPins is None:
            noPins = self.num_pins
        
        if pitch is None:
            pitch = self.pin_pitch

        m = noPins // 2
        pins = [onePin]       
        for i in range (1, noPins):
            nextPin = (onePin.translate((-pitch * (i % m), 0, 0)))
            nextPin = nextPin.rotate ((0,0,0), (0,0,1), 180.0 * (i // m))
            pins.append(nextPin)
        return self._union_all(pins)

    def _makeGwPin (self):
        """ create a gullwing pin
        :rtype: ``solid``
        """
        return self._make_angular_gullwing_pin (self.pin_height, self.pin_bottom_length, self.pin_gw_angle)

    def _makeJhPin (self):
        """ create a J-hook pin
        :rtype: ``solid``
        """
        return self._make_Jhook_pin (self.pin_height, self.pin_bottom_length, self.pin_top_length,  self.pin_top_radius)

    def _makeThPin (self):
        """ create a straight THT pin
        :rtype: ``solid``
        """
        return self._make_angled_pin (self.pin_height, self.pin_top_length)\
            .rotate ((0,0,0), (1,0,0), -90.0)\
            .translate ((0.0, 0.0, self.pin_z_shift))

    def _makeThcPin (self):
        """ create a unsymmetrically bended THT pin
        :rtype: ``solid``
        """
        return self._make_angled_clamping_pin (self.pin_height, self.pin_top_length, self.tht_pin_clamp_extension, self.tht_pin_lower_clamp_angel )\
            .rotate ((0,0,0), (1,0,0), -90.0)\
            .translate ((0.0, 0.0, self.pin_z_shift))

    def _makeThlPin (self):
        """ create a symmetrically bended (lambda shape) THT pin
        :rtype: ``solid``
        """
        return self._make_angled_lambda_pin (self.pin_height, self.pin_top_length, self.tht_pin_clamp_extension)\
            .rotate ((0,0,0), (1,0,0), -90.0)\
            .translate ((0.0, 0.0, self.pin_z_shift))

    _pinStyleSwitcher = {
        ShapeOfTerminal.GW: _makeGwPin,
        ShapeOfTerminal.JH: _makeJhPin,
        ShapeOfTerminal.TH: _makeThPin,
        ShapeOfTerminal.THC: _makeThcPin,
        ShapeOfTerminal.THL: _makeThlPin,
        }


    def make_pins(self):
        r"""Creates all pins of the tactile switch, depending on the ``terminal_shape`` defined in ``parameter``.
        :rtype: ``solid`` of all pins
        """
        # get the function from switcher dictionary making the pin defined by the terminal_shape key
        firstPin = self._pinStyleSwitcher.get(self.terminal_shape)(self)
        allPins = self._duplicatePins (firstPin.translate(self.first_pin_pos))
        

        return (allPins)


    def make_3D_model(self):
        """ create a 3D model of a tactile switch. Four parts will be created: plastic body, metallic cover, button, pins.

        This function will be called from the main_generator script.
        :return: list of the materials used for the 3D model
        :rtype: ``dictionary`` 
        """
        destination_dir = self.get_dest_3D_dir()
        
        # all parts belonging to parts body must be shifted by body_board_distance 
        case = self.makePlasticCase().translate((0.0, 0.0, self.body_board_distance))
        cover = self.makeCoverPlate ().translate((0.0, 0.0, self.body_board_distance))
        button = self.makeButton ().translate((0.0, 0.0, self.body_board_distance))
        pins = self.make_pins()
        show(case)
        show(cover)
        show(button)
        show(pins)
     
        doc = FreeCAD.ActiveDocument
        objs = GetListOfObjects(FreeCAD, doc)

     
        body_color = shaderColors.named_colors[self.body_color_key].getDiffuseFloat()
        cover_color = shaderColors.named_colors[self.cover_color_key].getDiffuseFloat()
        button_color = shaderColors.named_colors[self.button_color_key].getDiffuseFloat()
        pin_color = shaderColors.named_colors[self.pin_color_key].getDiffuseFloat()

        # must be the same order of the above show(..) calls
        Color_Objects(Gui, objs[0], body_color)
        Color_Objects(Gui, objs[1], cover_color)
        Color_Objects(Gui, objs[2], button_color)
        Color_Objects(Gui, objs[3], pin_color)

        col_body = Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_cover = Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_button = Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        col_pin = Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
        
        material_substitutions={
            col_body[:-1]:self.body_color_key,
            col_cover[:-1]:self.cover_color_key,
            col_button[:-1]:self.button_color_key,
            col_pin[:-1]:self.pin_color_key,
        }
        
        expVRML.say(material_substitutions)

        # fuse all parts of model
        while len(objs) > 1:
                FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
                del objs
                objs = GetListOfObjects(FreeCAD, doc)

        #rotate if required
        if (self.rotation != 0):
            z_RotateObject(doc, self.rotation)

        s = objs[0].Shape
        shape = s.copy()
        shape.Placement = s.Placement;
        shape.translate(self.offsets)
        objs[0].Placement = shape.Placement

        return material_substitutions

    
    

#*                                                                          *
#*                                                                          *
#*     class partsTactSwitches                                              *
#*                                                                          *
#*                                                                          *
class partsTactSwitches ():
    r"""A class for defining parameter of a special tactile switch. 

    """

    def model_exist(self, modelName):
        r"""checks if the model with given name exists. i.e. is part of ``all_params``
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :return: True if model exists, otherwise False
        :rtype: ``boolean``
        """
        for n in self.all_params:
            if n == modelName:
                return True
                
        return False
        
        
    def get_param_list_all(self):
        r"""returns a list of all model variants defined in `all_params``
        
        :rtype: ``list``
        """
        list = []
        for n in self.all_params:
            list.append(n)
        
        return list


    def getModelVariant (self, modelName):
        r"""returns the parameter namedtuple from ``all_params`` for the given model name
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :rtype: ``namedtuple``
        """
        return cqMakerTactSwitch (self.all_params[modelName]) 

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
        'modelName',		        # modelName, must correspond to 3D file name defined in KiCad footprint
        'body_width',		        # Body width, default: 6.0
        'body_length',		        # Body length (at the side of pins), default: 6.0
        'body_height',			    # Body height without button, default 3.5
        'cover_thickness',          # Thickness of cover, default 0.3
        'has_pegs',                 # Must be True if switch has reference pegs at the bottom, default: False
        'pegs_radius',              # Radius of the pegs, default: 1.0
        'pegs_pitch',               # Pitch of pegs if more than one, default: 9.0
        'pegs_heigth',              # Height of pegs, default: 1.5
        'pin_pitch',                # pin pitch, default 2.54
        'pin_thickness',            # thickness of pins, default 0.2
        'distance_pinTip_rows',     # distance from tip of pin from row one to row two, default 10.0
        'pin_width',                # pin width, default 0.6
        'pin_length_below_body',    # length of THT pins below body, only necessary for THT pins, dafault 3.5
        'terminal_shape',           # shape of terminal from class ShapeOfTerminal, default ShapeOfTerminal.GW
        'button_dia',               # diameter button, default 3.5
        'body_height_with_button',  # overall height of body incl. button, default 5.0
        'button_type',              # Type of button from class ButtonType, default ButtonType.FLAT
        'button_ring',              # Type of guide ring arround button, NONE if not present; default: ButtonRing.NONE
        'button_ring_radius',       # radius of round button ring, default 2.35
        'button_ring_heigth',       # height of button ring, default 1.6 
        'button_ring_width',        # width of octacon button ring, default 3.7
        'button_ring_length',       # length of octagon button ring, default 3.7 
        'with_gnd_pin',             # boolean: True if Ground Terminal is present, default False 
        'gnd_pin_tip_to_center',    # outer Pin tip (pin center for THT) of GND pin to center of body, default 4.0 
        'no_gnd_pins',              # number of groung pins (1 or 2); default: 1
        'offset_gnd_pin',           # offset of ground pin to middle of housing; default: 0.0
        'gnd_pin_width',            # width of ground pin; default: pin_width
        'serie',			        # The component serie, must be defined, no default value 
        'cover_color_key',	        # Cover color, default 'metal grey pins'
        'body_color_key',	        # Body colour, default 'black body'
        'button_color_key',         # botton color, default 'black body'
        'pin_color_key',	        # Pin color, default 'metal grey pins'
        'destination_dir',	        # Destination directory, default 'Button_Switch_SMD.3dshapes'

        # Python 2.x does not support extension of named tuple using _fields+(). 
        # We must define all field names of derived classe here in this base class. The default valued will be set in the derived classes.

        # fields for cq_cuk_kmr2x and cq_cuk_pts810x:
        'button_oval_width',        # width of side actuated button, default: 2.11
        'button_oval_length',       # length of side actuated button, default: 1.61

        # fields for cq_ultra_small_tact_switch:
        'button_side_width',        # width of side actuated button, default: 2.6
        'button_side_height',       # hight of side actuated button, default: 1.4
        'body_length_with_button',  # length of body incl. side actuated button, default: 4.5
    ])


    all_params = {

        'SW_SPST_B3S-1000': Params(
            modelName = 'SW_SPST_B3S-1000',   
            body_width = 6.0,		    
            body_length = 6.6,	       
            body_height = 3.4,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 9.0,
            pin_width = 0.7,
            pin_thickness = 0.1,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 3.3,
            body_height_with_button = 4.3,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'orange body',        
            pin_color_key = 'gold pins',  
            serie = TactSwitchSeries.B3S,
            destination_dir  = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_SPST_B3S-1100': Params(
            modelName = 'SW_SPST_B3S-1100',   
            body_width = 6.0,		    
            body_length = 6.6,	       
            body_height = 3.4,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 9.0,
            pin_width = 0.7,
            pin_thickness = 0.1,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 3.3,
            body_height_with_button = 4.3,
            button_type = ButtonType.FLAT,
            with_gnd_pin = True,
            gnd_pin_tip_to_center = 4.2,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'gold pins',  
            serie = TactSwitchSeries.B3S,
            destination_dir = 'Button_Switch_SMD.3dshapes',     
            ),

        'SW_SPST_B3SL-1002P': Params(
            modelName = 'SW_SPST_B3SL-1002P',   
            body_width = 6.2,		    
            body_length = 6.5,	       
            body_height = 2.5,			
            pin_pitch = 4.0,
            distance_pinTip_rows = 7.0,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.JH,
            button_dia = 2.5,
            body_height_with_button = 3.4,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'green body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3SL,
            destination_dir  = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_SPST_B3SL-1022P': Params(
            modelName = 'SW_SPST_B3SL-1022P',   
            body_width = 6.2,		    
            body_length = 6.5,	       
            body_height = 2.5,			
            pin_pitch = 4.0,
            distance_pinTip_rows = 7.0,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.JH,
            button_dia = 2.5,
            body_height_with_button = 5.1,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'grey body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3SL,
            destination_dir  = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_SPST_B3U-1100P-B': Params(
            modelName = 'SW_SPST_B3U-1100P-B',   
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
            button_dia = 1.5,
            body_height_with_button = 1.6,
            button_type = ButtonType.FLAT,
            with_gnd_pin = True,
            gnd_pin_tip_to_center = 1.9,
            gnd_pin_width = 0.5,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3U1,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),

        'SW_SPST_B3U-1100P': Params(
            modelName = 'SW_SPST_B3U-1100P',   
            body_width = 3.0,		    
            body_length = 2.5,	       
            body_height = 1.2,
            pin_pitch = 0.0,
            distance_pinTip_rows = 4.0,
            pin_width = 1.4,
            pin_thickness = 0.2,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 1.5,
            body_height_with_button = 1.6,
            button_type = ButtonType.FLAT,
            with_gnd_pin = True,
            gnd_pin_tip_to_center = 1.9,
            gnd_pin_width = 0.5,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3U1,
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


        'SW_SPST_Omron_B3FS-100xP': Params(
            modelName = 'SW_SPST_Omron_B3FS-100xP',   
            body_width = 6.0,		    
            body_length = 6.3,	       
            body_height = 2.6,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 8.0,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 3.0,
            body_height_with_button = 3.1,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3FS,
            destination_dir  = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_SPST_Omron_B3FS-101xP': Params(
            modelName = 'SW_SPST_Omron_B3FS-101xP',   
            body_width = 6.0,		    
            body_length = 6.3,	       
            body_height = 2.6,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 8.0,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 3.0,
            body_height_with_button = 4.3,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3FS,
            destination_dir  = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_SPST_Omron_B3FS-105xP': Params(
            modelName = 'SW_SPST_Omron_B3FS-105xP',   
            body_width = 6.0,		    
            body_length = 6.3,	       
            body_height = 2.6,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 8.0,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 3.0,
            body_height_with_button = 7.3,
            button_type = ButtonType.PROJ,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'yellow body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3FS,
            destination_dir  = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_TH_Tactile_Omron_B3F-10xx': Params(
            modelName = 'SW_TH_Tactile_Omron_B3F-10xx',   
            body_width = 6.0,		    
            body_length = 6.0,	       
            body_height = 3.4,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 6.5,
            pin_width = 0.7,
            pin_thickness = 0.3,
            pin_length_below_body = 3.5,
            terminal_shape = ShapeOfTerminal.THC,
            button_dia = 3.5,
            body_height_with_button = 4.3,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'yellow body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3F,
            destination_dir = 'Button_Switch_THT.3dshapes',      
            ),

        'SW_TH_Tactile_Omron_B3F-11xx': Params(
            modelName = 'SW_TH_Tactile_Omron_B3F-11xx',   
            body_width = 6.0,		    
            body_length = 6.0,	       
            body_height = 3.4,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 6.5,
            pin_width = 0.7,
            pin_thickness = 0.3,
            pin_length_below_body = 3.5,
            terminal_shape = ShapeOfTerminal.THC,
            button_dia = 3.5,
            body_height_with_button = 4.3,
            button_type = ButtonType.FLAT,
            with_gnd_pin = True,
            gnd_pin_tip_to_center = 4.1,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'yellow body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3F,
            destination_dir = 'Button_Switch_THT.3dshapes',      
            ),

        'SW_push_1P1T_NO_CK_KSC6xxJxxx': Params(
            modelName = 'SW_push_1P1T_NO_CK_KSC6xxJxxx',   
            body_width = 6.2,		    
            body_length = 6.2,	       
            body_height = 2.8,			
            pin_pitch = 4.0,
            distance_pinTip_rows = 6.8,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.JH,
            button_dia = 2.9,
            body_height_with_button = 7.6,
            button_type = ButtonType.FLAT,
            button_ring = ButtonRing.ROUND,
            button_ring_radius = 2.35,
            button_ring_heigth = 1.6,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.KSC,
            destination_dir = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_push_1P1T_NO_CK_KSC7xxJxxx': Params(
            modelName = 'SW_push_1P1T_NO_CK_KSC7xxJxxx',   
            body_width = 6.2,		    
            body_length = 6.2,	       
            body_height = 2.8,			
            pin_pitch = 4.0,
            distance_pinTip_rows = 6.8,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.JH,
            button_dia = 3.0,
            body_height_with_button = 4.2,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'blue body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.KSC,
            destination_dir = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_SPST_EVPBF': Params(
           modelName = 'SW_SPST_EVPBF',  
           body_width = 6.0,		    
           body_length = 6.0,	       
           body_height = 2.5,
           cover_thickness = 0.15,
           pin_pitch = 4.0,
           distance_pinTip_rows = 6.6,
           pin_width = 0.8,
           pin_thickness = 0.2,
           terminal_shape = ShapeOfTerminal.JH,
           button_dia = 3.4,
           body_height_with_button = 3.5,
           button_type = ButtonType.FLAT,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'white body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.EVPBF,
           destination_dir = 'Button_Switch_SMD.3dshapes',    
           ),

        'SW_SPST_EVQP0': Params(
           modelName = 'SW_SPST_EVQP0',  
           body_width = 6.2,		    
           body_length = 6.0,	       
           body_height = 1.8,
           cover_thickness = 0.15,
           pin_pitch = 4.0,
           distance_pinTip_rows = 6.6,
           pin_width = 0.8,
           pin_thickness = 0.2,
           terminal_shape = ShapeOfTerminal.JH,
           button_dia = 2.0,
           body_height_with_button = 2.5,
           button_type = ButtonType.FLAT,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'blue body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.EVQP0,
           destination_dir = 'Button_Switch_SMD.3dshapes',    
           ),

        'SW_SPST_EVQP2': Params(
           modelName = 'SW_SPST_EVQP2',  
           body_width = 4.7,		    
           body_length = 3.5,	       
           body_height = 1.65,
           cover_thickness = 0.15,
           pin_pitch = 1.7,
           distance_pinTip_rows = 5.5,
           pin_width = 0.6,
           pin_thickness = 0.2,
           terminal_shape = ShapeOfTerminal.JH,
           button_dia = 1.8,
           body_height_with_button = 2.5,
           button_type = ButtonType.FLAT,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'grey body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.EVQP2,
           destination_dir = 'Button_Switch_SMD.3dshapes',    
           ),

        'SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A08': Params(
           modelName = 'SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A08',  
           body_width = 4.9,		    
           body_length = 4.9,	       
           body_height = 0.8,
           cover_thickness = 0.15,
           pin_pitch = 3.7,
           distance_pinTip_rows = 5.2,
           pin_width = 0.5,
           pin_thickness = 0.2,
           terminal_shape = ShapeOfTerminal.JH,
           button_dia = 3.2,
           body_height_with_button = 0.8,
           button_type = ButtonType.FLAT,
           with_gnd_pin = True,
           gnd_pin_tip_to_center = 4.9/2.0,
           no_gnd_pins = 2,
           offset_gnd_pin = 0.35, 
           gnd_pin_width = 0.3,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'white body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.EVQPL,
           destination_dir = 'Button_Switch_SMD.3dshapes',    
           ),


        'SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A15': Params(
           modelName = 'SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A15',  
           body_width = 4.9,		    
           body_length = 4.9,	       
           body_height = 0.8,
           cover_thickness = 0.15,
           pin_pitch = 3.7,
           distance_pinTip_rows = 5.2,
           pin_width = 0.5,
           pin_thickness = 0.2,
           terminal_shape = ShapeOfTerminal.JH,
           button_dia = 3.2,
           body_height_with_button = 1.5,
           button_type = ButtonType.FLAT,
           button_ring = ButtonRing.OCTA,
           button_ring_width = 3.7,
           button_ring_length = 3.7,
           button_ring_heigth = 0.4,
           with_gnd_pin = True,
           gnd_pin_tip_to_center = 4.9/2.0,
           no_gnd_pins = 2,
           offset_gnd_pin = 0.35, 
           gnd_pin_width = 0.3,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'white body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.EVQPL,
           destination_dir = 'Button_Switch_SMD.3dshapes',    
           ),


        'SW_Tactile_Straight_KSA0Axx1LFTR': Params(
           modelName = 'SW_Tactile_Straight_KSA0Axx1LFTR',  
           body_width = 7.4,		    
           body_length = 7.3,	       
           body_height = 2.6,
           cover_thickness = 0.3,
           pin_pitch = 5.08,
           distance_pinTip_rows = 7.65,
           pin_width = 0.53,
           pin_thickness = 0.3,
           pin_length_below_body = 4.2,
           terminal_shape = ShapeOfTerminal.THC,
           button_dia = 3.0,
           body_height_with_button = 4.7,
           button_type = ButtonType.FLAT,
           button_ring = ButtonRing.ROUND,
           button_ring_radius = 2.4,
           button_ring_heigth = 1.1,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'blue body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.KSx0A,
           destination_dir = 'Button_Switch_THT.3dshapes',    
           ),


        'SW_Tactile_Straight_KSL0Axx1LFTR': Params(
           modelName = 'SW_Tactile_Straight_KSL0Axx1LFTR',  
           body_width = 7.4,		    
           body_length = 7.3,	       
           body_height = 2.6,
           cover_thickness = 0.3,
           pin_pitch = 5.08,
           distance_pinTip_rows = 7.65,
           pin_width = 0.53,
           pin_thickness = 0.3,
           pin_length_below_body = 4.2,
           terminal_shape = ShapeOfTerminal.THC,
           button_dia = 3.0,
           body_height_with_button = 9.9,
           button_type = ButtonType.FLAT,
           button_ring = ButtonRing.ROUND,
           button_ring_radius = 2.4,
           button_ring_heigth = 1.1,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'red body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.KSx0A,
           destination_dir = 'Button_Switch_THT.3dshapes',    
           ),

        'SW_PUSH_6mm_H8.5mm': Params(
            modelName = 'SW_PUSH_6mm_H8.5mm',   
            body_width = 6.0,		    
            body_length = 6.0,	       
            body_height = 3.6,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 6.5,
            pin_width = 0.7,
            pin_thickness = 0.3,
            pin_length_below_body = 3.5,
            terminal_shape = ShapeOfTerminal.THL,
            button_dia = 3.5,
            body_height_with_button = 8.5,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3F,
            destination_dir = 'Button_Switch_THT.3dshapes',      
            ),


        'SW_PUSH_6mm_H9.5mm': Params(
            modelName = 'SW_PUSH_6mm_H9.5mm',   
            body_width = 6.0,		    
            body_length = 6.0,	       
            body_height = 3.45,			
            pin_pitch = 4.5,
            distance_pinTip_rows = 9.0,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 3.5,
            body_height_with_button = 9.5,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3F,
            destination_dir = 'Button_Switch_SMD.3dshapes',      
            ),

        'SW_SPST_SKQG_WithStem': Params(
           modelName = 'SW_SPST_SKQG_WithStem',  
           body_width = 5.2,		    
           body_length = 5.2,	       
           body_height = 0.8,
           cover_thickness = 0.15,
           pin_pitch = 3.7,
           distance_pinTip_rows = 6.4,
           pin_width = 0.5,
           pin_thickness = 0.15,
           terminal_shape = ShapeOfTerminal.GW,
           button_dia = 2.0,
           body_height_with_button = 1.5,
           button_type = ButtonType.FLAT,
           button_ring = ButtonRing.OCTA,
           button_ring_width = 3.7,
           button_ring_length = 3.7,
           button_ring_heigth = 0.4,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'white body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.SKOG,
           destination_dir = 'Button_Switch_SMD.3dshapes',    
           ),


        'SW_SPST_SKQG_WithoutStem': Params(
           modelName = 'SW_SPST_SKQG_WithoutStem',  
           body_width = 5.2,		    
           body_length = 5.2,	       
           body_height = 0.8,
           cover_thickness = 0.15,
           pin_pitch = 3.7,
           distance_pinTip_rows = 6.4,
           pin_width = 0.5,
           pin_thickness = 0.15,
           terminal_shape = ShapeOfTerminal.GW,
           button_dia = 2.0,
           body_height_with_button = 0.7,
           button_type = ButtonType.FLAT,
           cover_color_key = 'metal grey pins',        
           body_color_key = 'black body',        
           button_color_key = 'black body',        
           pin_color_key = 'metal silver',  
           serie = TactSwitchSeries.SKOG,
           destination_dir = 'Button_Switch_SMD.3dshapes',    
           ),


        
        'SW_SPST_TL3305A': Params(
            modelName = 'SW_SPST_TL3305A',   
            body_width = 4.5,		    
            body_length = 4.5,	       
            body_height = 3.0,			
            pin_pitch = 3.0,
            distance_pinTip_rows = 7.5,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 2.5,
            body_height_with_button = 3.8,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3F,   # Tact switch bodys from E-Switch serie TL3305 are similar to Omron B3F, but TL3305 are SMD type
            destination_dir = 'Button_Switch_SMD.3dshapes',      
            ),
        

        'SW_SPST_TL3305B': Params(
            modelName = 'SW_SPST_TL3305B',   
            body_width = 4.5,		    
            body_length = 4.5,	       
            body_height = 3.0,			
            pin_pitch = 3.0,
            distance_pinTip_rows = 7.5,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 2.5,
            body_height_with_button = 5.0,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3F,      # Tact switch bodys from E-Switch serie TL3305 are similar to Omron B3F, but TL3305 are SMD type
            destination_dir = 'Button_Switch_SMD.3dshapes',      
            ),


        'SW_SPST_TL3305C': Params(
            modelName = 'SW_SPST_TL3305C',   
            body_width = 4.5,		    
            body_length = 4.5,	       
            body_height = 3.0,			
            pin_pitch = 3.0,
            distance_pinTip_rows = 7.5,
            pin_width = 0.7,
            pin_thickness = 0.3,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 2.5,
            body_height_with_button = 7.0,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'black body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.B3F,      # Tact switch bodys from E-Switch serie TL3305 are similar to Omron B3F, but TL3305 are SMD type
            destination_dir = 'Button_Switch_SMD.3dshapes',      
            ),


        'SW_Push_SPST_NO_Alps_SKRK': Params(
            modelName = 'SW_Push_SPST_NO_Alps_SKRK',   
            body_width = 3.9,		    
            body_length = 2.9,	       
            body_height = 1.5,
            pin_pitch = 0.0,
            distance_pinTip_rows = 4.8,
            pin_width = 1.4,
            pin_thickness = 0.2,
            terminal_shape = ShapeOfTerminal.GW,
            button_dia = 1.8,
            body_height_with_button = 2.0,
            button_type = ButtonType.FLAT,
            cover_color_key = 'metal grey pins',        
            body_color_key = 'white body',        
            button_color_key = 'black body',        
            pin_color_key = 'metal silver',  
            serie = TactSwitchSeries.SKRK,          
            destination_dir = 'Button_Switch_SMD.3dshapes',    
            ),


    }


                
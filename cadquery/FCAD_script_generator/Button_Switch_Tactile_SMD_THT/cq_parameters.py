#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#

## file of parametric definitions

def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)


import collections
from collections import namedtuple

import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui

import shaderColors
import exportPartToVRML as expVRML

## base parametes & model
import collections
from collections import namedtuple

# Import cad_tools
import cq_cad_tools
# Reload tools
from cq_cad_tools import reload_lib
reload_lib(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

# Sphinx workaround #1
try:
    QtGui
except NameError:
    QtGui = None
#

try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery
    cq = cadquery
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

#checking requirements
checkRequirements(cq)


class ShapeOfTerminal:
    r"""A class for holding constants for Shape of terminal of part

    .. note:: will be changed to enum when Python version allows it
    """
    JH = 'JH'
    r"""JH - J-hook
    """
    GW = 'GW'
    r"""GW - Gull wing
    """
    TH = 'TH'
    r"""TH - Through hole pin
    """
    THC = 'THC'
    r"""THC - angled THT pin with asymetrical clamping bend 
    """
    THL = 'THL'
    r"""THL - angled THT pin with symetrical lambda shaped clamping bend 
    """

class ButtonType:
    r"""A class for holding type of button of Omron tactile switch series

    .. note:: will be changed to enum when Python version allows it
    """
    FLAT = 'FLAT'
    r"""FLAT: Normal round button
    """
    PROJ = 'PROJ'
    r"""PROJ: Projected type (round knob on square shaft)
    """

class ButtonRing:
    r"""A class defining the type of an additional ring around the button.

    .. note:: will be changed to enum when Python version allows it
    """
    NONE = 'NONE'
    r"""NONE: No additional button 
    """
    ROUND = 'ROUND'
    r"""ROUND: Round button ring
    """
    OCTA = 'OCTA'
    r"""OCTA: Octagon button ring
    """


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
#*                                                                          *
#*                                                                          *

class partParamsTactSwitches ():
    r"""Class containing the parameter for building a 3D model of a tactile switch

    :param params: namedtuple containing the variable parameter for building the different 3D models.
    :type  params: ``partsTactSwitches.Params``
    """

    def __init__(self, params):

        # get all entries of the params list as dictionary
        args = params._asdict()
        self.type = params.type if 'type' in args and params.type != None else "SMD"

        # Defining all dimensions needed to build the model.
        # If a dimension is part of the given params list, this value must be used

        # Dimensions of plastic body
        self.body_height = params.body_height if 'body_height' in args and  params.body_height  != None else 3.75
        self.body_length = params.body_length if 'body_length' in args and  params.body_length  != None else 6.6  # side of part where the pins are
        self.body_width = params.body_width if 'body_width' in args and  params.body_width  != None else 6.0
        self.body_height_with_button = params.body_height_with_button if 'body_height_with_button' in args and  params.body_height_with_button  != None else 5.0
        # if no distance of body to board is given with params it is set to None and will be set depending on shape of terminals 
        self.body_board_distance = params.body_board_distance if 'body_board_distance' in args and  params.body_board_distance  != None else None
        # if case has alignment pegs 'has_pegs' must be true
        self.has_pegs = params.has_pegs if 'has_pegs' in args and  params.has_pegs  != None else False
        self.pegs_pitch = params.pegs_pitch if 'pegs_pitch' in args and  params.pegs_pitch  != None else 9.0
        self.pegs_radius = params.pegs_radius if 'pegs_radius' in args and  params.pegs_radius  != None else 1.0
        self.pegs_heigth = params.pegs_heigth if 'pegs_heigth' in args and  params.pegs_heigth  != None else 1.5
        
        # Dimesion of button
        self.button_dia = params.button_dia if 'button_dia' in args and  params.button_dia  != None else 3.5
        self.button_ring = params.button_ring if 'button_ring' in args and  params.button_ring  != None else ButtonRing.NONE
        self.button_ring_radius = params.button_ring_radius if 'button_ring_radius' in args and  params.button_ring_radius  != None else 2.35
        self.button_ring_heigth = params.button_ring_heigth if 'button_ring_heigth' in args and  params.button_ring_heigth  != None else 1.6
        self.button_ring_length = params.button_ring_length if 'button_ring_length' in args and  params.button_ring_length  != None else 3.7
        self.button_ring_width = params.button_ring_width if 'button_ring_width' in args and  params.button_ring_width  != None else 3.7

        # dimension of pins
        self.num_pins = params.num_pins if 'num_pins' in args and  params.num_pins  != None else 4
        self.pin_pitch = params.pin_pitch if 'pin_pitch' in args and  params.pin_pitch  != None else 2.54
        self.pin_width = params.pin_width if 'pin_width' in args and  params.pin_width  != None else 0.6
        self.pin_thickness = params.pin_thickness if 'pin_thickness' in args and  params.pin_thickness  != None else 0.2
        self.distance_pinTip_rows = params.distance_pinTip_rows if 'distance_pinTip_rows' in args and  params.distance_pinTip_rows  != None else 10.0  # distance from tip of pin from row one to row two
        self.num_pin_rows = params.num_pin_rows if 'num_pin_rows' in args and  params.num_pin_rows  != None else 2
        self.top_length = params.top_length if 'top_length' in args and  params.top_length  != None else 0.2         # only used for J-hook and angled THT pin
        self.pin_length_below_body = params.pin_length_below_body if 'pin_length_below_body' in args and  params.pin_length_below_body  != None else 3.5         # only used for THT pin

        # Model variants
        self.terminal_shape = params.terminal_shape if 'terminal_shape' in args and  params.terminal_shape  != None else ShapeOfTerminal.GW
        
        
        # Default dimensions. These dimensions Will normally be defined in the serie specific derived class
        # Dimensions of pockest at bottom of plastic body
        self.bottom_pocket_depth = 0.1
        self.pin_pocket_edge_length =  1.6
        self.pin_pocket_mid_length =  1.2
        self.pin_pocket_edge_width =  1.3

        # Dimension of metallic cover plate
        self.cover_thickness = params.cover_thickness if 'cover_thickness' in args and  params.cover_thickness  != None else 0.3
        self.cover_side_height =  2.1
        self.cover_plate_with_side_sheets = False  # must be true if cover of switch has side clips
        # for side sheets with center pocket:
        self.cover_side_pocket_width = 4.0
        self.cover_side_pocket_heigth = 1.3
        # for solid side sheets:
        self.cover_solid_side_width =  self.body_width / 2.0


        self.button_has_base_plate = False;
#self. = params. if '' in args and  params.  != None else 


        # Dimensions of pockest at top of plastic body
        # self.pocket_turn_inset_top_depth: see derived dimensions
        self.pocket_top_side_width =  0.45
        self.pocket_top_side_depth =  0.45

        # Dimensions of plastic body side pads
        self.pad_side_height =  self.cover_side_pocket_heigth 
        self.pad_side_width =  self.cover_side_pocket_width
         
        # derived dimensions. Some depend on cover thickness. If cover thickness must be changed by a in derived classes,
        # these dimensions have to be adapted to the new thickness. 
        self.button_height = self.body_height_with_button - self.body_height + self.cover_thickness   # the button heigth is measured from below cover to top
        self.body_height_plastic = self.body_height - self.cover_thickness
        self.pad_side_length =  self.cover_thickness 
        # for some switches the lower part of the side clamps are not closed (Omron B3S). For these models the following parameter must be > 0.0
        self.button_hole_dia = self.button_dia * 1.04
        
        # for projected button type some more dimensions are needed
        self.button_proj_length_top = self.button_dia / 1.42  # sqrt (2)
        self.button_proj_length_mid = self.button_proj_length_top / 1.42  # sqrt (2)
        self.button_proj_hight_bot = self.button_height / 4.0
        self.button_proj_hight_mid = self.button_height / 4.0
        self.button_proj_hight_top = self.button_height / 2.0

        # Call of function defining dimensions depending on the shape of terminals
        paramFunction = self._TerminalShapeSwitcher.get(self.terminal_shape, None)
        if paramFunction == None:     # not a valid terminal_shape
            FreeCAD.Console.PrintMessage(str(self.terminal_shape) + ' not a valid member of ' + str(ShapeOfTerminal))
            self.make_me = False
        else:  # Call the funktion
            paramFunction (self)


    def paramsForJh (self):
        r"""set the reqired dimensions for building J-hook pins

        """
        self.pin_bottom_length =  1.0 
        self.pin_height = 1.2
        self.pin_top_length = 1.0
        self.pin_top_radius = self.pin_thickness / 2.0  # inner radius at top of j-hook pin
        if self.body_board_distance is None:
            self.body_board_distance = max (self.pin_thickness  - self.bottom_pocket_depth, 0.0)
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), self.distance_pinTip_rows/2.0 - self.pin_thickness)
        self.rotation = 90.0
        self.offsets = (0.0, 0.0, 0.0)

    def paramsForGw (self):
        r"""set the reqired dimensions for building gullwing pins

        """
        self.pin_bottom_length =  1.3
        self.pin_height = 0.7
        if self.body_board_distance is None:
            self.body_board_distance = 0.0
        # Sice the pins are hidden inside the body, we can make the pin length half the distance pin tip of both rows (distance_pinTip_rows)
        # In this case the y- part of the first pin pos can be 0.0
        self.pin_length = self.distance_pinTip_rows / 2.0         # only used for gullwing
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), 0.0)
        self.rotation = 90.0
        self.offsets = (0.0, 0.0, 0.0)

    def paramsForTh (self):
        r"""set the reqired dimensions for building through hole pins

        """
        self.pin_height = self.pin_length_below_body + 1.1
        if self.body_board_distance is None:
            self.body_board_distance = 0.0
        # Sice the pins are hidden inside the body, we can make the pin top length half the distance pin tip of both rows (distance_pinTip_rows)
        # In this case the y- part of the first pin pos can be 0.0
        self.pin_top_length = self.distance_pinTip_rows / 2.0 - self.pin_thickness  
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), 0.0)
        # THT pins must be shifted upwards 
        self.pin_z_shift = self.pin_height - self.pin_thickness/2.0 - self.pin_length_below_body  
        self.rotation = 90.0
        offsetX = (self.distance_pinTip_rows / 2.0)
        offsetY = (-self.first_pin_pos[0])
        self.offsets = (offsetX, offsetY, 0.0)


    # dictionary assigning the parameter functions for setting the pin dimensions to ShapeOfTerminal keys
    _TerminalShapeSwitcher = {
        ShapeOfTerminal.GW: paramsForGw,
        ShapeOfTerminal.JH: paramsForJh,
        ShapeOfTerminal.TH: paramsForTh,
        ShapeOfTerminal.THC: paramsForTh,
        ShapeOfTerminal.THL: paramsForTh,
        }




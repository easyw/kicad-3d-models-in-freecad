#!/usr/bin/python
# -*- coding: utf8 -*-
#

#****************************************************************************
#*                                                                          *
#* class for generating generic parameters for rotary coded switches        *
#* type Nidec SH7000                                                        *
#*                                                                          *
#* This is part of FreeCAD & cadquery tools                                 *
#* to export generated models in STEP & VRML format.                        *
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
import FreeCAD

from collections import namedtuple
from cq_base_parameters import PartParametersBase, CaseType

### use enums (Phyton 3+)

class CodeFormat:
    r"""A class for holding constants for part Code Format

    .. note:: will be changed to enum when Python version allows it
    """
    REAL = 'REAL'
    r"""REAL - real coded switch
    """
    GRAY = 'GRAY'
    r"""GRAY - gray coded switch
    """

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
    TH = 'THT'
    r"""TH - Through hole pin
    """



# defines all parameter necessary for building the model of the part
class partParams ():
    r"""Class containing the parameter for building a 3D model of a rotary coded switch

    :param params: Member ``Params`` of class ``PartParametersBase->variableParams.Params`` containing the variable parameter for building the different 3D models.

    The values within ``params`` overwrite the corresponding values within the class ``partParams`` 
    :type  params: ``variableParams.Params``
    """

    def __init__(self, params):

        # get all entries of the params list as dictionary
        args = params._asdict()

        # Defining all dimensions needed to build the model.
        # If a dimension is part of the given params list, this value must be used

        # Dimensions of plastic body
        self.body_height = params.body_height if 'body_height' in args else 3.75
        self.body_length = params.body_length if 'body_length' in args else 7.3                 
        self.body_width = params.body_width if 'body_width' in args else 7.1
        self.body_board_distance = params.body_board_distance if 'body_board_distance' in args else 0.1


        # Dimensions of pockest at bottom of plastic body
        self.bottom_center_hole_dia = params.bottom_center_hole_dia if 'bottom_center_hole_dia' in args else 1.2             
        self.bottom_pocket_depth = params.bottom_pocket_depth if 'bottom_pocket_depth' in args else 0.15
        self.pocket_edge_pin_length = params.pocket_edge_pin_length if 'pocket_edge_pin_length' in args else 1.32
        self.pocket_mid_pin_length = params.pocket_mid_pin_length if 'pocket_mid_pin_length' in args else 1.2
        self.pocket_edge_pin_width = params.pocket_edge_pin_width if 'pocket_edge_pin_width' in args else 1.72

        # Dimensions of pockest at top of plastic body
        # self.pocket_turn_inset_top_depth: see derived dimensions
        self.pocket_top_side_width = params.pocket_top_side_width if 'pocket_top_side_width' in args else 0.45
        self.pocket_top_side_depth = params.pocket_top_side_depth if 'pocket_top_side_depth' in args else 0.45

        # Dimensions of plastic body side pads
        self.pad_side_height = params.pad_side_height if 'pad_side_height' in args else 2.45 
        self.pad_side_length = params.pad_side_length if 'pad_side_length' in args else 0.43 
        self.pad_side_width = params.pad_side_width if 'pad_side_width' in args else 1.05

        # Dimension of metallic cover plate
        self.cover_thickness = params.cover_thickness if 'cover_thickness' in args else 0.3
        self.cover_height = params.cover_height if 'cover_height' in args else 2.1
        self.cover_side_pocket_width = params.cover_side_pocket_width if 'cover_side_pocket_width' in args else 3.1
        self.cover_side_pocket_heigth = params.cover_side_pocket_heigth if 'cover_side_pocket_heigth' in args else 1.45
        

        # Dimesion of turn inset
        self.turn_inset_height = params.turn_inset_height if 'turn_inset_height' in args else 1.3
        self.turn_inset_dia = params.turn_inset_dia if 'turn_inset_dia' in args else 3.4
        self.arrowshaft_length = params.arrowshaft_length if 'arrowshaft_length' in args else 1.4
        self.arrowshaft_height = params.arrowshaft_height if 'arrowshaft_height' in args else 0.7
        self.arrowhead_heigth = params.arrowhead_heigth if 'arrowhead_heigth' in args else 0.8
        self.arrowhead_length = params.arrowhead_length if 'arrowhead_length' in args else 1.0
        self.arrow_barb_heigth = params.arrow_barb_heigth if 'arrow_barb_heigth' in args else 0.45
        self.arrow_pocket_depth = params.arrow_pocket_depth if 'arrow_pocket_depth' in args else 1.0

        # Dimension number ring
        self.number_ring_radius = params.number_ring_radius if 'number_ring_radius' in args else 2.5
        self.number_font_size = params.number_font_size if 'number_font_size' in args else 1.0

        # dimension of pins
        self.num_pins = params.num_pins if 'num_pins' in args else 6
        self.pin_pitch = params.pin_pitch if 'pin_pitch' in args else 2.54
        self.pin_width = params.pin_width if 'pin_width' in args else 0.6
        self.pin_thickness = params.pin_thickness if 'pin_thickness' in args else 0.2
        self.distance_pinTip_rows = params.distance_pinTip_rows if 'distance_pinTip_rows' in args else 10.0  # distance from tip of pin from row one to row two
        self.num_pin_rows = params.num_pin_rows if 'num_pin_rows' in args else 2
        self.top_length = params.top_length if 'top_length' in args else 0.2         # only used for J-hook and angled THT pin

        # Model variants
        self.code_format = params.code_format if 'code_format' in args else CodeFormat.REAL
        self.terminal_shape = params.terminal_shape if 'terminal_shape' in args else ShapeOfTerminal.GW
         
        # derived dimensions
        self.body_length_without_pads = self.body_length - 2.0 * self.pad_side_length
        self.first_pin_pos = (self.pin_pitch, (self.body_width - self.pocket_edge_pin_width)/2.0)
        self.pocket_turn_inset_top_depth = self.turn_inset_height - self.cover_thickness


        # Call of function defining dimensions depending on the shape of terminals
        paramFunction = self._shapeSwitcher.get(self.terminal_shape, None)
        if paramFunction == None:     # not a valid terminal_shape
            FreeCAD.Console.PrintMessage(str(self.terminal_shape) + ' not a valid member of ' + str(ShapeOfTerminal))
            self.make_me = False
        else:  # Call the funktion
            paramFunction (self)


    def paramsForJh (self):
        r"""set the reqired dimensions for building J-hook pins

        """
        self.pin_bottom_length =  1.2 
        self.pin_height = 0.96
        self.body_board_distance = self.pin_thickness  - self.bottom_pocket_depth
        self.distance_pinTip_rows = 7.5  # distance from arc of pin from row one to row two
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), self.distance_pinTip_rows/2.0 - self.pin_thickness)
        self.rotation = 90.0
        self.offsets = (0.0, 0.0, 0.0)

    def paramsForGw (self):
        r"""set the reqired dimensions for building gullwing pins

        """
        self.pin_bottom_length =  0.65
        self.pin_height = 0.96
        self.body_board_distance = self.pin_thickness  - self.bottom_pocket_depth
        self.distance_pinTip_rows = 10.0  # distance from tip of pin from row one to row two
        # Sice the pins are hidden inside the body, we can make the pin length half the distance pin tip of both rows (distance_pinTip_rows)
        # In this case the y- part of the first pin pos can be 0.0
        self.pin_length = self.distance_pinTip_rows / 2.0         # only used for gullwing
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), 0.0)
        self.rotation = 90.0
        self.offsets = (0.0, 0.0, 0.0)

    def paramsForTh (self):
        r"""set the reqired dimensions for building through hole pins

        """
        self.pin_height = 4.26
        self.distance_pinTip_rows = 3.0 * self.pin_pitch  # distance from center!!! of pin from row one to row two 3xpitch
        self.body_board_distance = 0.0
        # Sice the pins are hidden inside the body, we can make the pin top length half the distance pin tip of both rows (distance_pinTip_rows)
        # In this case the y- part of the first pin pos can be 0.0
        self.pin_top_length = self.distance_pinTip_rows / 2.0 - self.pin_thickness  
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), 0.0)
        # THT pins must be shifted upwards 
        self.pin_z_shift = self.pin_height + self.pin_thickness - 3.5  # 3.5 is the pin length below body taken from data sheet
        self.rotation = 90.0
        offsetX = (self.distance_pinTip_rows / 2.0)
        offsetY = (-self.first_pin_pos[0])
        self.offsets = (offsetX, offsetY, 0.0)

    # dictionary assigning the parameter functions for setting the pin dimensions to ShapeOfTerminal keys
    _shapeSwitcher = {
        ShapeOfTerminal.GW: paramsForGw,
        ShapeOfTerminal.JH: paramsForJh,
        ShapeOfTerminal.TH: paramsForTh
        }

        
# The param class defines only these parameter which differ from model to model
class variableParams (PartParametersBase):
    r"""Class containing the variable parameter for building the different 3D models of a rotary coded switch

    """


    # must be overridden from PartParametersBase
    # Content of Param will be filled when calling make_params(...)
    Params = namedtuple("Params", [
        'body_height',    # height of plastic body
        'code_format',    # code format of switch: real(=complementary) or gray
        'terminal_shape', # shape of terminal J-hook, gullwing, through hole
        'type'            # type of part: SMD or THT
])

    def __init__(self):
        self.base_params = {
            "7010A"                 : self.make_params(3.75, CodeFormat.REAL, ShapeOfTerminal.JH, CaseType.SMD),
            "7010B"                 : self.make_params(3.75, CodeFormat.REAL, ShapeOfTerminal.GW, CaseType.SMD),
            "7040B"                 : self.make_params(3.75, CodeFormat.GRAY, ShapeOfTerminal.GW, CaseType.SMD),
            "7010C"                 : self.make_params(3.70, CodeFormat.REAL, ShapeOfTerminal.TH, CaseType.THT),
        }

    def getSampleModels(self, model_classes, make_all=True):
        r"""Generate the default model of a model class, defined by the attribute ``default_model``.   
        If no default model is defined, all models will be generated for this model class.

        :param model_classes:
            list of part creator classes inherited from :class:`cq_base_model.PartBase`
        :type  model_classes: ``list of classes``

        :rtype: ``tuple``

        """

        models = {}

        # instantiate generator classes in order to make a dictionary of all default variants
        for i in range(0, len(model_classes)):
            if hasattr (model_classes[i], 'default_model'):
                variant = model_classes[i].default_model
                params =  self.base_params[variant]
                model = model_classes[i](params)
                if model.make_me:
                    models[model.makeModelName(variant)] = self. Model(variant, params, model_classes[i])
            elif make_all:
                models.update (self.getAllModels ([model_classes[i]]))

        return models 


    # overridden from PartParametersBase
    def make_params(self, body_height, code_format, terminal_shape, part_type):
        r"""Fills the tuple ``Params`` with the given values 

        :param body_height: height of plastic body
        :type  body_height: ``float``
        :param code_format: code format of switch: *real(=complementary)* or *gray*
        :type  code_format: ``CodeFormat``
        :param terminal_shape: shape of terminal: *J-hook, gullwing, through hole*
        :type  terminal_shape: ``ShapeOfTerminal``
        :param part_type: type of part: SMD or THT
        :type  part_type: ``CaseType``

        :rtype: ``Params`` returns a new subclass of tuple with named fields. The names are identical to the names of the given parameter.  

        """

        return self.Params(
            body_height = body_height,          # height of plastic body
            code_format = code_format,          # code format of switch: real(=complementary) or gray
            terminal_shape = terminal_shape,    # shape of terminal J-hook, gullwing, through hole
            type = part_type                    # part type: 'THT' or 'SMD'
        )

### EOF ###

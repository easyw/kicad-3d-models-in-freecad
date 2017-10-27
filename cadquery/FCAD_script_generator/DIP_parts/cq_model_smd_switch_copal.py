# -*- coding: utf8 -*-
#!/usr/bin/python
#
   
#****************************************************************************
#*                                                                          *
#* generic class for generating SMD DIP switch models in STEP AP214         *
#*                                                                          *
#* This is part of FreeCAD & cadquery tools                                 *
#* to export generated models in STEP & VRML format.                        *
#*   Copyright (c) 2017                                                     *
#* Terje Io / Io Engineering                                                *
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

## base parametes & model

from cq_base_model import part
from cq_parameters import CASE_THT_TYPE, CASE_SMD_TYPE

## model generators

from cq_model_smd_switch import *

class dip_switch_copal_CHS_B (dip_smd_switch):

    def __init__(self, params):
        dip_smd_switch.__init__(self, params)
        self.rotation = 90

        self.pin_pitch  = 1.27
        self.pin_length = 3.2
        self.pin_thickness = 0.15
        self.pin_width = 0.4
        self.pin_bottom_length = 0.4

        self.body_width = 5.4
        self.body_overall_width = 8.0
        self.body_height = 2.5
        self.body_length = self.num_pins * self.pin_pitch / 2.0 + 1.23
        self.body_board_distance = 0.1

        self.button_width = 0.7
        self.button_length = 0.6
        self.button_base = 2.25
        self.button_heigth = 0.4
        self.button_pocket_dept = 0.5

    def make_modelname(self, genericName):
        return 'SW_DIP_x' + '{:d}'.format(self.num_pins / 2) + '_W7.62mm_Slide_Copal_CHS-B'

    def _make_switchpockets(self):

        # create first pocket

        x0 = self._first_pin_pos()
        z0 = self.body_height - self.button_pocket_dept
        
        pocket = cq.Workplane("XY", origin=(x0, 0.0, z0))\
                   .rect(self.button_width, self.button_base).extrude(self.button_pocket_dept)

        BS = cq.selectors.BoxSelector

        w2 = self.button_base / 2.0
        x2 = self.button_width / 2.0
        
        case = pocket.edges(BS((x0 + x2 + 0.1, -w2 - 0.1, z0-0.1), (x0 - x2 - 0.1, -w2 + 0.1, z0 + 0.1))).chamfer(self.button_pocket_dept - 0.01)
        case = pocket.edges(BS((x0 + x2 + 0.1, w2 - 0.1, z0-0.1), (x0 - x2 - 0.1, w2 + 0.1, z0 + 0.1))).chamfer(self.button_pocket_dept - 0.01)
                   
        return self.make_rest(pocket)

    def make_buttons(self):

        button = cq.Workplane("XY", origin=(self._first_pin_pos(), 0.0, self.body_height - self.button_pocket_dept - 0.1))\
                   .rect(self.button_width, self.button_base).extrude(0.1)\
                   .faces(">Z").center(0, -self.button_base / 2.0 + self.button_length / 2.0 + self.button_pocket_dept)\
                   .rect(self.button_width, self.button_length).extrude(self.button_heigth + 0.1)

        return self.make_rest(button)

class dip_switch_copal_CHS_A (dip_switch_copal_CHS_B):

    def __init__(self, params):
        dip_switch_copal_CHS_B.__init__(self, params)

        self.body_overall_width = 5.6
        self.body_board_distance = self.pin_thickness

        self.pin_bottom_length = (self.body_overall_width - 3.8) / 2.0 - self.pin_thickness

        self.offsets = (0.0, 0.0, self.body_board_distance)

    def make_modelname(self, genericName):
        return 'SW_DIP_x' + '{:d}'.format(self.num_pins / 2) + '_W5.08mm_Slide_Copal_CHS-A'

    def make_pins(self):
    
        # create first pin
        pin = self.make_Jhook_pin((self.body_height + self.body_board_distance) / 2.0, (self.body_overall_width - self.body_width) / 2.0,
                                    self.pin_bottom_length, self.pin_width, self.pin_thickness)
        pin = pin.translate((self._first_pin_pos(), self.body_overall_width / 2.0 - self.pin_thickness, -self.pin_thickness))
        
        pins = self.make_rest(pin)

        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))

### EOF ###

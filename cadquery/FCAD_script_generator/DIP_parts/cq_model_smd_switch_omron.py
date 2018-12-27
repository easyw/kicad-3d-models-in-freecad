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
#* Terje Io https://github.com/terjeio                                      *
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

import cadquery as cq

## model generators

from cq_model_smd_switch import dip_smd_switch_lowprofile

class dip_switch_omron_a6h (dip_smd_switch_lowprofile):

    def __init__(self, params):
        dip_smd_switch_lowprofile.__init__(self, params)
        self.make_me = self.num_pins / 2 in [2, 4, 6, 8, 10]
        self.rotation = 90

        self.pin_pitch  = 1.27
        self.pin_length = 1.1
        self.pin_thickness = 0.15
        self.pin_width = 0.4
        self.pin_bottom_length = 0.6

        self.body_width = 4.5
        self.body_overall_width = 6.7
        self.body_height = 1.45
        self.body_length = self.num_pins * self.pin_pitch / 2.0 + 1.23
        self.body_board_distance = 0.1

        self.button_width = 0.5
        self.button_length = 0.6
        self.button_base = 2.25
        self.button_heigth = 0.4
        self.button_pocket_dept = 0.5

        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), self.pin_rows_distance / 2.0)

    def makeModelName(self, genericName):
        if self.num_pins == 10:
            return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_Omron_A6H-0101_W6.15mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm'
        else:
            return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_Omron_A6H-' + '{:01d}'.format(self.num_pins / 2) + '101_W6.15mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm'

    def _make_switchpockets(self):

        # create first pocket

        x0 = self.first_pin_pos[0]
        z0 = self.body_height - self.button_pocket_dept

        pocket = cq.Workplane("XY", origin=(x0, 0.0, z0))\
                   .rect(self.button_width, self.button_base).extrude(self.button_pocket_dept)

        BS = cq.selectors.BoxSelector

        w2 = self.button_base / 2.0
        x2 = self.button_width / 2.0

        pocket.edges(BS((x0 + x2 + 0.1, -w2 - 0.1, z0-0.1), (x0 - x2 - 0.1, -w2 + 0.1, z0 + 0.1))).chamfer(self.button_pocket_dept - 0.01)
        pocket.edges(BS((x0 + x2 + 0.1, w2 - 0.1, z0-0.1), (x0 - x2 - 0.1, w2 + 0.1, z0 + 0.1))).chamfer(self.button_pocket_dept - 0.01)

        return self._mirror(pocket)

    def _make_cornerpockets(self):
        width = 0.5
        depth = -0.2
        pocket = cq.Workplane("XY", origin=(self.body_length / 2 - 0.5, self.body_width / 2.0 - 0.25, self.body_height))\
                   .rect(width, width).extrude(depth)\
                   .faces(">Z").center(0.0, -width / 2.0).circle(width / 2.0).extrude(depth)

        pockets = pocket.union(pocket.translate((-self.body_length + 1.0, 0, 0)))

        return pockets.union(pockets.rotate((0,0,0), (0,0,1), 180))

    def _make_buttonsrecess(self):
        depth = -0.2
        return cq.Workplane("XY")\
                   .workplane(offset=self.body_height)\
                   .rect(self.body_length - 1.6, self.body_width - self.button_base).extrude(depth)\
                   .faces("<Z").edges().chamfer(-depth-0.01)

    def make_body(self):
        body = super(dip_switch_omron_a6h, self).make_body(0.2, 0.0).cut(self._make_buttonsrecess())\
                                                       .cut(self._make_cornerpockets())

        self.body_edge_upper = self.body_edge_upper + 0.15 # move pin mark a bit

        return body

    def make_buttons(self):

        button = cq.Workplane("XY", origin=(self.first_pin_pos[0], 0.0, self.body_height - self.button_pocket_dept - 0.1))\
                   .rect(self.button_width, self.button_base).extrude(0.1)\
                   .faces(">Z").center(0, -self.button_base / 2.0 + self.button_length / 2.0 + self.button_pocket_dept)\
                   .rect(self.button_width, self.button_length).extrude(self.button_heigth + 0.1)

        return self._mirror(button)

    def make_pins(self):

        # create first pin
        pin = self._make_gullwing_pin(self.body_height / 2.0, self.pin_bottom_length)\
                  .translate((self.first_pin_pos[0], self.body_overall_width / 2.0 - self.pin_length, - self.pin_thickness / 2.0))

        pins = self._mirror(pin)

        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))

class dip_switch_omron_a6s (dip_switch_omron_a6h):

    def __init__(self, params):
        dip_switch_omron_a6h.__init__(self, params)

        self.make_me = self.num_pins / 2 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.pin_pitch  = 2.54
        self.pin_length = 1.8
        self.pin_width = 0.5
        self.pin_bottom_length = 0.7
        
        self.body_width = 6.2
        self.body_overall_width = 9.8
        self.body_height = 3.0
        self.body_length = self.num_pins * self.pin_pitch / 2.0 + 0.94
        self.body_board_distance = 0.1

        self.color_keys[1] = "gold pins"

        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), self.pin_rows_distance / 2.0)
        

    def makeModelName(self, genericName):
        return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_Omron_A6S-' + '{:d}'.format(self.num_pins / 2) + '10x_W8.9mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm'
        
### EOF ###

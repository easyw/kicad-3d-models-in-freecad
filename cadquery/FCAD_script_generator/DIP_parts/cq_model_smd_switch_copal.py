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

class dip_switch_copal_CHS_B (dip_smd_switch_lowprofile):

    def __init__(self, params):
        dip_smd_switch_lowprofile.__init__(self, params)
        self.make_me = self.make_me and self.num_pins / 2 in [1, 2, 4, 6, 8, 10]
        self.rotation = 90

        self.pin_pitch  = 1.27
        self.pin_length = 2.0
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

        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), self.pin_rows_distance / 2.0)

    def makeModelName(self, genericName):
        return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_Copal_CHS-' + '{:02d}'.format(self.num_pins / 2) + 'B_W7.62mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm'

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

class dip_switch_copal_CHS_A (dip_switch_copal_CHS_B):

    def __init__(self, params):
        dip_switch_copal_CHS_B.__init__(self, params)

        self.body_width = 5.4
        self.body_overall_width = 5.6
        self.body_board_distance = self.pin_thickness

        self.pin_bottom_length = 1.0

        self.offsets = (0.0, 0.0, self.body_board_distance)
        
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), self.body_width / 2.0)

    def makeModelName(self, genericName):
        return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_Copal_CHS-' + '{:02d}'.format(self.num_pins / 2) + 'A_W5.08mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm_JPin'

    def make_pins(self):

        # create first pin
        pin = self._make_Jhook_pin((self.body_height + self.body_board_distance) / 2.0, self.pin_bottom_length, self.pin_bottom_length)
        pin = pin.translate((self.first_pin_pos[0], self.body_overall_width / 2.0 - self.pin_thickness, -self.pin_thickness))

        pins = self._mirror(pin)

        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))


class dip_switch_copal_CVS (dip_switch_copal_CHS_B):

    def __init__(self, params):
        dip_switch_copal_CHS_B.__init__(self, params)

        self.make_me = self.num_pins / 2 in [1, 2, 3, 4, 8]
        self.pin_pitch  = 1.00
        self.pin_length = 1.0
        self.pin_thickness = 0.15
        self.pin_width = 0.35
        self.pin_bottom_length = 0.3

        self.body_width = 4.7
        self.body_overall_width = 6.1
        self.body_height = 1.35
        self.body_length = self.num_pins * self.pin_pitch / 2.0 + 1.00
        self.body_board_distance = 0.1

        self.button_width = 0.5
        self.button_length = 0.6
        self.button_base = 2.25
        self.button_heigth = 0.4
        self.button_pocket_dept = 0.5

        self.body_board_distance = self.pin_thickness

        self.offsets = (0.0, 0.0, self.body_board_distance)
        
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), self.body_width / 2.0)

    def makeModelName(self, genericName):
        return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_Copal_CVS-' + '{:02d}'.format(self.num_pins / 2) + 'xB_W5.9mm_P1mm'

        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))
        

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

    def _make_buttonsrecess(self):
        depth = -0.2
        return cq.Workplane("XY")\
                   .workplane(offset=self.body_height)\
                   .rect(self.body_length - 1.6, self.body_width - self.button_base).extrude(depth)\
                   .faces("<Z").edges().chamfer(-depth-0.01)

    def make_body(self):
        body = super(dip_switch_copal_CVS, self).make_body(0.2, 0.0).cut(self._make_buttonsrecess())
        
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


        case = cq.Workplane("XY", origin=(0.0, self.body_width / 2.0 - self.pin_width + 0.1, self.body_height))\
                   .rect(self.body_length, 2.0 * self.pin_width).extrude(self.pin_thickness / 2.0)
                   
                   
        case1 = cq.Workplane("XY", origin=((self.body_length / 2.0) - (self.pin_width / 2.0) , (self.body_width / 2.0) - (self.pin_thickness / 2.0) + 0.1, self.body_height))\
                   .rect(self.pin_width, self.pin_thickness).extrude(0.0 - self.body_height)
        case = case.union(case1)
                   
        case1 = cq.Workplane("XY", origin=((self.body_length / 2.0) - (self.pin_width / 2.0) , (0.0 - ((self.body_width / 2.0) - (self.pin_thickness / 2.0))) - 0.1, self.body_height))\
                   .rect(self.pin_width, self.pin_thickness).extrude(0.0 - self.body_height)
        case = case.union(case1)

        case1 = cq.Workplane("XY", origin=(0.0, (self.body_width / 2.0) - (self.pin_thickness / 2.0) + 0.1, (4.0 * self.body_height) / 5.0))\
                   .rect(self.body_length, self.pin_thickness).extrude(self.body_height / 5.0)
        case = case.union(case1)
           
        case = case.faces("<Y").edges().fillet(self.pin_thickness / 3.0)
        case = case.faces(">Y").edges().fillet(self.pin_thickness / 3.0)
        case = case.faces(">Z").edges("<Y").fillet(self.pin_thickness / 3.0)
        
        pins = pins.union(case)
        
        
        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))
        
        
### EOF ###

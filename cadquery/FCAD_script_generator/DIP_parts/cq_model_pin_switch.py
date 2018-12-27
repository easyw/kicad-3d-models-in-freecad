# -*- coding: utf8 -*-
#!/usr/bin/python
#

#****************************************************************************
#*                                                                          *
#* class for generating DIP switch models in STEP AP214                     *
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

import cadquery as cq
from Helpers import show

## base parametes & model

from cq_base_model import PartBase
from cq_base_parameters import CaseType

## model generator

class dip_switch (PartBase):

    default_model = "DIP-10"

    def __init__(self, params):
        PartBase.__init__(self, params)
        self.make_me = self.num_pins / 2 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#        if self.make_me:
        self.licAuthor = "Terje Io"
        self.licEmail = "https://github.com/terjeio"
        self.destination_dir = "Button_Switch_THT.3dshapes"
        self.footprints_dir = "Button_Switch_THT.pretty"

        self.rotation = 180
        self.pin_rows_distance = 7.62
        self.pin_pitch = 2.54

        self.pin_width = 0.6
        self.pin_thickness = 0.2
        self.pin_length = 3.2

        self.body_width = 9.9
        self.body_height = 5.85
        self.body_length = ((self.num_pins * self.pin_pitch) / 2.0) + 2.18
        self.body_board_distance = 0.0
        self.body_board_pad_height = 0.5

        self.button_width = 1.4
        self.button_length = 1.6
        self.button_base = 3.62
        self.button_heigth = 1.2

        self.color_keys[0] = "blue body" #body
        self.color_keys.append("white body") #buttons
        self.color_keys.append("white body") #buttons

        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), (self.pin_rows_distance / 2.0) - self.pin_thickness)
        self.offsets =  (((self.body_length / 2.0) - 1.8 - self.pin_width, self.pin_rows_distance / 2.0, self.body_board_distance))
#        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), self.pin_rows_distance / 2.0)
#        self.offsets = ((self.first_pin_pos[1], -self.first_pin_pos[0], self.body_board_distance))

    def makeModelName(self, genericName):
        if self.num_pins == 6 or self.num_pins == 16:
            return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_9.78x' + '{:.1f}'.format(self.body_length) + 'mm_W7.62mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm'
        else:
            return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_9.78x' + '{:.2f}'.format(self.body_length) + 'mm_W7.62mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm'

    def _make_switchpockets(self):

        # create first pocket
        pocket = cq.Workplane("XY", origin=(self.first_pin_pos[0], 0.0, 0.0))\
                   .workplane(offset=self.body_height - 1.0)\
                   .rect(self.button_width, self.button_base).extrude(1.0)

        # union and return all pockets
        return self._mirror(pocket)

    def make_body(self):

        body = cq.Workplane(cq.Plane.XY())\
                 .rect(self.body_length, self.body_width).extrude(self.body_height)\
                 .faces(">Z").cut(self._make_switchpockets())

        body.faces("<Z").rect(self.body_length -1.0, self.body_width).cutBlind(self.body_board_pad_height)
        body.faces("<Z").rect(self.body_length, self.body_width - 3.0).cutBlind(self.body_board_pad_height)

        ##ok = Draft.makeShapeString("OK",'C:\windows\fonts\arial.ttf', 5)

        return body

    def make_buttons(self):

        d = 1.7
        o = 0.6
        button_length_2 = self.button_length / 2.0

        # create first button
        button = cq.Workplane("XY", origin=(self.first_pin_pos[0], 0.0, self.body_height - 1.0))\
                   .rect(self.button_width, self.button_base).extrude(0.7)
        button = button.faces(">Z")\
                       .center(0.0, -self.button_base / 2.0 + button_length_2)\
                       .rect(self.button_width, self.button_length)\
                       .extrude(self.button_heigth + 0.7)
        button = button.faces(">Z").workplane(centerOption='CenterOfBoundBox')\
                       .center(0, -(button_length_2 + o)).hole(d, self.button_heigth)
        button = button.faces(">Z").workplane(centerOption='CenterOfBoundBox')\
                       .center(0, button_length_2 + o).hole(d, self.button_heigth)

        return self._mirror(button)

    def make_pins(self):

        l = self.pin_length + self.body_board_pad_height

        #create first pin
        pin = cq.Workplane("XZ", (self.first_pin_pos[0], self.pin_rows_distance / 2.0 + self.pin_thickness / 2.0, self.body_board_pad_height))\
                .moveTo(self.pin_width / 2.0, 0.0)\
                .line(0.0, -(l - self.pin_width))\
                .line(-self.pin_width / 4.0, -self.pin_width)\
                .line(-self.pin_width / 2.0, 0.0)\
                .line(-self.pin_width / 4.0, self.pin_width)\
                .line(0.0, l - self.pin_width)\
                .close().extrude(self.pin_thickness)

        pins = self._mirror(pin)

        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))

    def make_pinmark(self, width):

        h = 0.01
        w = width / 2.0
        w3 = width / 3.0

        return cq.Workplane("XY", origin=(self.first_pin_pos[0], self.body_width / 2.0 - 0.6, self.body_height - h))\
                 .line(-w, -w)\
                 .line(w3, 0.0)\
                 .line(0.0, -w3)\
                 .line(w3, 0.0)\
                 .line(0.0, w3)\
                 .line(w3, 0.0)\
                 .close().extrude(h)

    def make(self):
        show(self.make_body())
        show(self.make_pins())
        show(self.make_buttons())
        show(self.make_pinmark(self.button_width + 0.2))

class dip_switch_low_profile (dip_switch):

    def __init__(self, params):
        dip_switch.__init__(self, params)

        self.make_me = self.num_pins / 2 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        
        self.rotation = 180
        self.pin_rows_distance = 7.62
        self.pin_pitch = 2.54

        self.body_height = 3.8
        self.body_width = 6.7
        self.body_length = ((self.num_pins * self.pin_pitch) / 2.0) + 1.56

        self.button_width = 0.7
        self.button_length = 1.6
        self.button_base = 3.62
        self.button_heigth = 0.5

        self.color_keys[0] = "black body" #body
        self.color_keys.append("white body") #buttons
        self.color_keys.append("white body") #buttons
        
#        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), (self.pin_rows_distance / 2.0) - self.pin_thickness)
#        self.offsets =  ((self.first_pin_pos[1], -self.first_pin_pos[0], self.body_board_distance))
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), (self.pin_rows_distance / 2.0) - self.pin_thickness)
        self.offsets =  (((self.body_length / 2.0) - 1.5 - self.pin_width, self.pin_rows_distance / 2.0, self.body_board_distance))

    def make_body(self, pin_area_height=None, body_angle_top=12.0):
        return self._make_plastic_body(pin_area_height, body_angle_top).cut(self._make_switchpockets())

        body = cq.Workplane(cq.Plane.XY())\
                 .rect(self.body_length, self.body_width).extrude(self.body_height)\
                 .faces(">Z").cut(self._make_switchpockets())

        body.faces("<Z").rect(self.body_length -1.0, self.body_width).cutBlind(self.body_board_pad_height)
        body.faces("<Z").rect(self.body_length, self.body_width - 3.0).cutBlind(self.body_board_pad_height)

        ##ok = Draft.makeShapeString("OK",'C:\windows\fonts\arial.ttf', 5)

        return body

    def make_pins(self):

        l = self.pin_length + self.body_board_pad_height
        pin = self._make_angled_pin(pin_height = l, top_extension=2.0, style='THT')
        pin = pin.rotate((0,0,0), (1,0,0), 0.0 - 90.0)
        pin = pin.translate((self.first_pin_pos[0], 0.0 - self.first_pin_pos[1], (self.body_height / 2.0) + self.body_board_distance))

        pins = self._mirror(pin)

        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))

    def makeModelName(self, genericName):
        if self.num_pins == 2 or self.num_pins == 12 or self.num_pins == 22:
            return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_6.7x' + '{:.1f}'.format(self.body_length) + 'mm_W7.62mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm_LowProfile'
        else:
            return 'SW_DIP_SPSTx' + '{:02d}'.format(self.num_pins / 2) + '_Slide_6.7x' + '{:.2f}'.format(self.body_length) + 'mm_W7.62mm_P' + '{:.2f}'.format(self.pin_pitch) + 'mm_LowProfile'

### EOF ###

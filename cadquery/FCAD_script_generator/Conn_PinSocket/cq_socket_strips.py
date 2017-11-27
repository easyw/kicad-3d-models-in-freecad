# -*- coding: utf8 -*-
#!/usr/bin/python
#

#****************************************************************************
#*                                                                          *
#* class for generating pin socket strip models in STEP AP214               *
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

# 2017-11-25

import cadquery as cq
from Helpers import show

## base parametes & model
import cq_base_model
reload(cq_base_model)
from cq_base_model import PartBase
from cq_base_parameters import PinStyle, CaseType
from parameters import *

## model generator

#
# Dimensions are mainly from footprints, too many variants out in the wild to make any sense of...
#

class socket_strip (PartBase):

#    default_model = "THT-1x1.00mm_Vertical"
#    default_model = "THT-1x1.27mm_Vertical"
#    default_model = "THT-1x2.00mm_Vertical"
#    default_model = "THT-1x2.54mm_Vertical"
#    default_model = "THT-2x1.27mm_Vertical"
    default_model = "THT-2x2.00mm_Vertical"
#    default_model = "THT-2x2.54mm_Vertical"

    def __init__(self, params):
        PartBase.__init__(self, params)
        self.make_me = params.type == CaseType.THT and params.pin_style == PinStyle.STRAIGHT
        self.licAuthor = "Terje Io"
        self.licEmail = "https://github.com/terjeio"
        self.destination_dir = "Conn_PinSocket_{0:03.2f}mm.3dshapes".format(self.pin_pitch)
        self.footprints_dir = "Conn_PinSocket_{0:03.2f}mm.pretty".format(self.pin_pitch)
        self.rotation = 90
        self.pin_style = params.pin_style

        self.pin_width        = params.pin_width
        self.pin_thickness    = params.pin_thickness
        self.pin_length       = params.pin_length + self.pin_thickness
        self.pinsocket_offset = params.pins_offset
        self.body_height      = params.body_height
        self.body_overlength  = params.body_overlength
        self.body_width       = params.body_width
        self.body_offset      = params.body_offset
        self.pin_row_distance = (params.num_pin_rows - 1) * self.pin_pitch
        self.pin_socket_size  = self.pin_width

        self.body_length = self.num_pins * self.pin_pitch / self.num_pin_rows
        self.body_board_distance = self.pin_thickness

        self.color_keys[1] = "gold pins"
        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), self.pin_row_distance / 2.0 - self.pinsocket_offset)

        self.offsets = (-self.first_pin_pos[1] - self.pinsocket_offset * 2.0, -self.first_pin_pos[0], 0)

    def makeModelName(self, genericName):

        return "PinSocket_{0}x{1:02}_P{2:03.2f}mm_{3}{4}".format(self.num_pin_rows, self.num_pins / self.num_pin_rows, self.pin_pitch,
                 "Vertical" if self.pin_style == PinStyle.STRAIGHT else "Horizontal",
                 '' if self.type == CaseType.THT else '_SMD')

    def _make_pinpockets(self):

        rsz = self.pin_socket_size * 2.0
        first_pin_pos = (self.first_pin_pos[0], self.first_pin_pos[1] + self.pinsocket_offset)

        # create first pin pocket
        pocket = cq.Workplane("XY", origin=first_pin_pos + (self.body_height,))\
                   .rect(rsz, rsz).extrude(-rsz / 4.0)\
                   .faces("<Z").edges().chamfer(rsz / 4.0 - 0.001)\
                   .faces("<Z").rect(self.pin_socket_size, self.pin_socket_size).extrude(-self.body_height + rsz)\
                   .faces("<Z").rect(self.pin_socket_size, self.pin_thickness).extrude(-rsz + self.body_board_distance)
         
        pockets = self._mirror(pocket, self.num_pins / self.num_pin_rows)

        if self.num_pin_rows == 2:
            # create opposite pinrow
            pockets = pockets.union(pockets.rotate((0,0,0), (0,0,1), 180))

        return pockets

    def _make_pinsocket(self):

        rsz = self.pin_socket_size * 2.0
        length = self.body_height - rsz
        c = self.pin_socket_size / 12.0

        pinsocket = cq.Workplane("XZ")\
                      .workplane(offset=-self.pin_thickness / 2.0 - self.pinsocket_offset)\
                      .moveTo(-self.pin_socket_size / 2.0, 0.0)\
                      .line(-self.pin_socket_size / 4.0, 0.0)\
                      .line(0.0, length - 0.1)\
                      .line(self.pin_socket_size / 4.0, 0.0)\
                      .line(c, -c)\
                      .line(0.0, -(length - rsz))\
                      .line(self.pin_socket_size -c * 2.0, 0.0)\
                      .line(0.0, length - rsz)\
                      .line(c, c)\
                      .line(self.pin_socket_size / 4.0, 0.0)\
                      .line(0.0, -(length - 0.1))\
                      .close()\
                      .extrude(self.pin_thickness)

        if self.pinsocket_offset > 0.0:
            pinsocket = pinsocket.union(cq.Workplane("XY", origin=(0.0, (self.pinsocket_offset - self.pin_thickness) / 2.0, 0.0))\
                                          .rect(self.pin_width, self.pinsocket_offset).extrude(self.pin_thickness))

        return pinsocket

    def _make_body(self):
 
        length = self.body_length + self.body_overlength
        width  = self.body_width
 
        body = cq.Workplane(cq.Plane.XY())\
                 .rect(length, width).extrude(self.body_height)\
                 .faces(">Y").cut(self._make_pinpockets())

        if self.body_board_distance > 0.0:
            body = body .faces("<Z").rect(length, width - width / 3.0).cutBlind(self.body_board_distance)

        return body

    def _make_pins(self):

        pins = self._mirror(self._make_straight_pin()\
                                .union(self._make_pinsocket())\
                                .translate(self.first_pin_pos + (self.body_board_distance,)), self.num_pins / self.num_pin_rows)

        if self.num_pin_rows == 2:
            # create opposite pinrow
            pins = pins.union(pins.rotate((0,0,0), (0,0,1), 180))

        return pins

    def make(self):        
        show(self._make_body())
        show(self._make_pins())

class angled_socket_strip (socket_strip):

#!    default_model = "THT-1x1.27mm_Horizontal"
#    default_model = "THT-2x1.27mm_Horizontal"
    default_model = "THT-1x2.00mm_Horizontal"
#    default_model = "THT-2x2.00mm_Horizontal"
#    default_model = "THT-1x2.54mm_Horizontal"
    default_model = "THT-2x2.54mm_Horizontal"

    # measurements taken from footprint

    def __init__(self, params):
        socket_strip.__init__(self, params)
        self.make_me = params.type == CaseType.THT and params.pin_style == PinStyle.ANGLED # and not params.pin_pitch == 1.27
        self.rotation = 90
        self.pin_offset = params.pins_offset
        
        tmp = self.body_height
        self.body_height = self.body_width
        self.body_width = tmp
        
        self.offsets = (0.0 if self.num_pin_rows == 1 else -self.pin_pitch / 2.0, -self.first_pin_pos[0], 0)
        self.translate = ((0.0, self.body_offset + self.pin_row_distance / 2.0, self.body_width / 2.0))

    def _make_body(self):
        body = socket_strip._make_body(self)\
                           .rotate((0,0,0), (1,0,0), -90)\
                           .translate(self.translate)
        return body

    def _make_pins(self):

        tl = self.translate[1] - (0.0 if self.num_pin_rows == 1 else self.pin_pitch / 2.0)

        pin = self._make_angled_pin(style = CaseType.THT,
                                    pin_height = self.pin_length + self.pin_pitch / 2.0,
                                    top_length = tl)\
                  .union(self._make_pinsocket())\
                  .translate(self.first_pin_pos + (self.body_board_distance,))
        pins = self._mirror(pin, self.num_pins / self.num_pin_rows)

        if self.num_pin_rows == 2:
            pin = self._make_angled_pin(style=CaseType.THT,
                                       pin_height=self.pin_length + self.pin_pitch * 1.5,
                                       top_length=tl + self.pin_pitch)\
                      .union(self._make_pinsocket())\
                      .translate((self.first_pin_pos[0], -self.first_pin_pos[1], self.body_board_distance))
            pins = pins.union(self._mirror(pin, self.num_pins / self.num_pin_rows))
        return pins.rotate((0,0,0), (1,0,0), -90)\
                   .translate(self.translate)

class smd_socket_strip (socket_strip):

#    default_model = "SMD-2x1.00mm_Vertical"
#    default_model = "SMD-1x1.00mm_Vertical_Right"
#    default_model = "SMD-1x1.00mm_Vertical_Left"
    default_model = "SMD-1x1.27mm_Vertical_Right"
#    default_model = "SMD-1x1.27mm_Vertical_Left"
#    default_model = "SMD-1x2.00mm_Vertical_Right"
#    default_model = "SMD-1x2.00mm_Vertical_Left"
#    default_model = "SMD-1x2.54mm_Vertical_Right"
#    default_model = "SMD-1x2.54mm_Vertical_Left"
#    default_model = "SMD-2x1.27mm_Vertical"
#    default_model = "SMD-2x2.00mm_Vertical"
#    default_model = "SMD-2x2.54mm_Vertical"

    # 1.00mm http://www.mouser.com/ds/2/181/M40-310R-1135950.pdf
    # 2.00mm http://www.mouser.com/ds/2/18/91596-942496.pdf

    # pin horizontal pin length measured from footprints

    def __init__(self, params):
        socket_strip.__init__(self, params)
        self.odd_pins = self.num_pins % 2.0 != 0.0
        self.make_me = params.type == CaseType.SMD and self.num_pins >=2 and (self.num_pin_rows == 1 or not self.odd_pins)
#        self.make_me = self.make_me and (self.pin_pitch != 1.27 or self.num_pin_rows > 1) 
        self.rotation = 90
        self.pin_length = (self.pin_length - self.pin_row_distance) / 2.0 - self.pin_thickness - self.pin_thickness / 4.0
        self.pin1start_right = params.pin1start_right
        self.offsets    = (0, 0, self.pin_thickness * 1.5)

    def makeModelName(self, genericName):
        return socket_strip.makeModelName(self, genericName)\
                + ("" if self.num_pin_rows == 2 else ("_Pin1Right" if self.pin1start_right else "_Pin1Left"))

    def _make_pins(self):

        pin = self._make_angled_pin(top_length=self.body_board_distance)\
                  .union(self._make_pinsocket())\
                  .translate((0.0, 0.0, self.body_board_distance))

        if self.num_pin_rows == 1:
            pin = pin.translate((self.first_pin_pos[0] + (0.0 if not self.pin1start_right else -self.pin_pitch), self.first_pin_pos[1], 0.0))
            if self.odd_pins:
                if self.pin1start_right:
                    odd_pin = pin.rotate((0,0,0), (0,0,1), 180).translate((-self.pin_pitch, 0.0, 0.0))
                else:
                    odd_pin = pin.translate((-self.first_pin_pos[0] * 2.0, 0.0, 0.0))
            pins = self._mirror(pin, self.num_pins / 2, self.pin_pitch * 2.0)
            pinsl = pins.rotate((0,0,0), (0,0,1), 180)
            if self.odd_pins:
                pins = pins.union(odd_pin)
                pinsl = pinsl.translate((self.pin_pitch, 0.0, 0.0))
            pins = pins.union(pinsl)
        else:
            pin = pin.translate(self.first_pin_pos + (0.0,))
            pins = self._mirror(pin)
            pins = pins.union(pins.rotate((0,0,0), (0,0,1), 180))

        return pins

### EOF ###

# -*- coding: utf8 -*-
#!/usr/bin/python
#

#****************************************************************************
#*                                                                          *
#* class for generating turned pin DIP switch models in STEP AP214          *
#*                                                                          *
#* This is part of FreeCAD & cadquery tools                                 *
#* to export generated models in STEP & VRML format.                        *
#*   Copyright (c) 2017                                                     *
#* Terje Io https://github.com/terjeio                                      *
#* Maurice https://launchpad.net/~easyw                                     *
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

from math import sqrt

## base parametes & model

from cq_base_model import PartBase
from cq_base_parameters import CaseType

## model generator

#
# Dimensions and style is from TE Connectivity Specification document:
# http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=1571586&DocType=Customer+Drawing&DocLang=English
#
# NOTE: some are taken from on screen measurements
#

class dip_socket_turned_pin (PartBase):

    default_model = "DIP-10"
    default_model = "DIP-10_SMD"

    def __init__(self, params):
        PartBase.__init__(self, params)
        self.make_me = self.num_pins >= 4
        self.licAuthor = "Terje Io"
        self.licEmail = "https://github.com/terjeio"
        self.destination_dir = "Package_DIP.3dshapes"
        self.footprints_dir = "Package_DIP.pretty"
        self.isTHT = self.type == CaseType.THT
        self.rotation = 270
        self.pin_socket_diameter = 1.524
        self.pin_socket_radius = self.pin_socket_diameter / 2.0
        self.pin_radius = 0.508 / 2.0

        self.body_width = self.pin_rows_distance + 2.54
        self.body_height = 2.667
        self.body_length = self.num_pins * 1.27
        self.body_board_distance = 1.3
        self.body_bottom_pockets =  0 if self.num_pins <= 4\
                                       else (1 if self.num_pins <= 10\
                                                else (3 if self.num_pins > 28 else 2))

        self.first_pin_pos = (self.pin_pitch * (self.num_pins / 4.0 - 0.5), self.pin_rows_distance / 2.0)

        offsetX = (self.first_pin_pos[1] if self.isTHT else 0)
        offsetY = (-self.first_pin_pos[0] if self.isTHT else 0)
        self.offsets = (offsetX, offsetY, self.body_board_distance)

    def makeModelName(self, genericName):
        width = self.pin_rows_distance if self.isTHT else self.pin_rows_distance + 1.27
        return 'DIP-' + '{:d}'.format(self.num_pins) + '_W' + '{:.2f}'.format(width) + \
                ('mm_Socket' if self.isTHT else 'mm_SMDSocket_LongPads')

    def _make_pinpockets(self):

        # create first pocket
        pocket = cq.Workplane("XY", origin=(self.first_pin_pos + (0.0,)))\
                   .circle(self.pin_socket_radius)\
                   .extrude(self.body_height)

        # create other pockets
        pockets = self._mirror(pocket)

        # create other side of the pockets
        return pockets.union(pockets.rotate((0,0,0), (0,0,1), 180))

    def _make_pin_socket (self):
        pin = cq.Workplane("XY")\
                .circle(self.pin_socket_radius).extrude(-self.body_board_distance)\
                .faces("<Z").edges().chamfer(0.3)

        return pin.faces(">Z").workplane()\
                              .circle(self.pin_socket_radius + 0.1).extrude(self.body_height + 0.04).faces(">Z")\
                              .cskHole(self.pin_radius * 2.0, self.pin_socket_diameter, 82, depth=self.body_height)

    def make_body(self):

        tq = 1.1 # package indent depth
        tr = 1.9 # package bridge width
        r = 0.5  # pocket corner radius
        w = tq
        h = self.body_width - 6.0 # top body pocket width
        o = r - r / sqrt(2.0)
        body_length_2 = self.body_length / 2.0

        body = cq.Workplane(cq.Plane.XY())\
                 .rect(self.body_length, self.body_width).extrude(self.body_height)\
                 .faces(">Z").cut(self._make_pinpockets())

        # pin 1 indent
        body = body.faces(">Z").workplane(centerOption='CenterOfBoundBox').center(-body_length_2, -h / 2.0)\
                    .lineTo(w - r, 0.0) \
                    .threePointArc((w - o, o), (w, r)) \
                    .lineTo(w, h-r) \
                    .threePointArc((w - o, h - o), (w - r, h)) \
                    .lineTo(0.0, h) \
                    .close().cutBlind(-self.body_height)

        # reverse indent
        body = body.faces(">Z").workplane(centerOption='CenterOfBoundBox').center(body_length_2, -h / 2.0)\
                    .lineTo(-w + r, 0.0) \
                    .threePointArc((-w + o, o), (-w, r)) \
                    .lineTo(-w, h - r) \
                    .threePointArc((-w + o, h - o), (-w + r, h)) \
                    .lineTo(0.0, h) \
                    .close().cutBlind(-self.body_height / 2.0)

        # top pocket, none if self.body_bottom_pockets = 0, cuts through if self.body_bottom_pockets = 1
        if self.body_bottom_pockets > 0:
            w = (self.body_length - tq - tr * 2.0) / 2.0
            h = self.body_width - (6.0 if self.body_bottom_pockets < 3 else 6.8)

            body = body.faces(">Z").workplane(centerOption='CenterOfBoundBox').center(tq  / 2.0, -h / 2.0)\
                        .lineTo(w - r, 0) \
                        .threePointArc((w - o, o), (w, r)) \
                        .lineTo(w, h - r) \
                        .threePointArc((w - o, h - o), (w - r, h)) \
                        .lineTo(-w + r, h) \
                        .threePointArc((-w + o, h - o), (-w, h - r )) \
                        .lineTo(-w, r) \
                        .threePointArc((-w + o, o), (-w + r, 0.0)) \
                        .close().cutBlind(-self.body_height if self.body_bottom_pockets == 1 else -self.body_height / 2.0)

        # bottom pockets
        if self.body_bottom_pockets > 1:
            w1 = (self.body_length - tq - tr) / self.body_bottom_pockets
            w = (w1 - tr) / 2.0
            offs = -body_length_2 + tq + tr + w
            for i in range(0, self.body_bottom_pockets):
                body = body.faces("<Z").workplane(centerOption='CenterOfBoundBox').center(offs + w1 * i, -h / 2.0)\
                           .lineTo(w - r, 0.0) \
                           .threePointArc((w - o, o), (w, r)) \
                           .lineTo(w, h - r) \
                           .threePointArc((w - o, h - o), (w - r, h)) \
                           .lineTo(-w + r, h) \
                           .threePointArc((-w + o, h - o), (-w, h - r )) \
                           .lineTo(-w, r) \
                           .threePointArc((-w + o, o), (-w + r, 0.0)) \
                           .close().cutBlind(-self.body_height / 2.0)

        q1 = 2.2
        q2 = 3.5 if self.body_bottom_pockets < 3.0 else 3.9

        body = body.faces(">Z").workplane(centerOption='CenterOfBoundBox')\
                               .center(0.0, (-self.body_width + q1) / 2.0 + q2)\
                               .rect(self.body_length, q1).cutBlind(-self.body_height / 2.0)

        return body

    def _make_pin_tht(self):

        # common dimensions
        L = 5.08 - self.body_board_distance # tip to seating plane
        return self._make_pin_socket().faces("<Z").circle(self.pin_radius).extrude(-L).faces("<Z").edges().chamfer(.1)

    def _make_pin_smd(self):

        # common dimensions
        L2 = 0.3
        L = 1.9  # 1.9 tip to seating plane
        r2 = self.pin_radius * 4.0
        s = -L2 - r2
        r = r2 - r2 / sqrt(2.0)

        path = cq.Workplane("YZ")\
                 .lineTo(0.0, -L2)\
                 .threePointArc((r, s + r), (r2, s))\
                 .lineTo(L, s)
        pin = cq.Workplane("XY")\
                .circle(self.pin_radius)\
                .sweep(path).faces(">Y")\
                .chamfer(.1)\
                .translate((0.0, 0.0, -1.3))

        self.offsets = (self.offsets[0], self.offsets[1], self.offsets[2] - s + self.pin_radius)

        return self._make_pin_socket().union(pin)

    def make_pins(self):
        # create first pin
        pin = self._make_pin_tht() if self.isTHT else self._make_pin_smd()

        # create other pins
        pins = self._mirror(pin.translate(self.first_pin_pos + (0.0,)))

        # create other side of the pins
        return pins.union(pins.rotate((0,0,0), (0,0,1), 180))

    def make(self):
        show(self.make_body())
        show(self.make_pins())

## EOF ##

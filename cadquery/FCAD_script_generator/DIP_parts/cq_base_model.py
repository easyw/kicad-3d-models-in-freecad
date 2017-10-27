# -*- coding: utf8 -*-
#!/usr/bin/python
#

#****************************************************************************
#*                                                                          *
#* base class for generating part models in STEP AP214                      *
#*                                                                          *
#* This is part of FreeCAD & cadquery tools                                 *
#* to export generated models in STEP & VRML format.                        *
#*   Copyright (c) 2017                                                     *
#* Terje Io / Io Engineering                                                *
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

#
# parts of this code is based on work by other contributors
#

import cadquery as cq

from math import sqrt, tan, radians

class part:
    #
    destination_dir = "My.3dshapes"
    #
    #############################################
    # Licence information of the generated models
    #############################################
    licAuthor = "kicad StepUp"
    licEmail = "ksu"
    licOrgSys = "kicad StepUp"
    licPreProc = "OCC"
    licOrg = "FreeCAD"   
    #############################################

    def __init__(self):
        # init mandatory base class attributes to some more or less sensible defaults
        self.footprints_dir = None

        self.rotation = 0
        self.make_me = True
        self.pin_pitch = 2.54
        self.pin_thickness = 0.2

        self.body_width = 5.08
        self.body_length = 5.08
        self.body_height = 5.08

        self.offsets = (0.0, 0.0, 0.0)
        self.color_keys = ["black body", "metal grey pins"]

    def union_all(self, objects):
        o = objects[0]
        for i in range(1, len(objects)):
            o = o.union(objects[i])
        return o

    def make_rest(self, obj):
        objs = [obj]        
        for i in range(2, self.num_pins / 2 + 1):
            objs.append(obj.translate((-self.pin_pitch * (i - 1), 0, 0)))

        return self.union_all(objs)   

    def make_plastic_body(self, pin_area_height=None, body_angle_top=12.0, body_angle_bottom=12.0):

        if pin_area_height == None:
            pin_area_height = self.pin_thickness             # top part of body is that much smaller

        the_t = 2.0 * tan(radians(body_angle_top))           # body angle top
        the_b = 2.0 * tan(radians(body_angle_bottom))        # body angle bottom

        A2_t = (self.body_height - pin_area_height) / 2.0    # body top part height
        A2_b = A2_t                                          # body bottom part height
        D_b = self.body_length - the_b * A2_b                # bottom length
        E1_b = self.body_width - the_b * A2_b                # bottom width
        D_t1 = self.body_length - pin_area_height            # top part bottom length
        E1_t1 = self.body_width - pin_area_height            # top part bottom width
        D_t2 = D_t1 - the_t * A2_t                           # top part upper length
        E1_t2 = E1_t1 - the_t * A2_t                         # top part upper width

        self.body_edge_upper = E1_t2 / 2.0 # save for pin mark placement

        return cq.Workplane(cq.Plane.XY())\
                 .rect(D_b, E1_b)\
                 .workplane(offset=A2_b).rect(self.body_length, self.body_width)\
                 .workplane(offset=pin_area_height).rect(self.body_length, self.body_width)\
                 .rect(D_t1, E1_t1)\
                 .workplane(offset=A2_t).rect(D_t2, E1_t2).loft(ruled=True)

    def make_gullwing_pin(self, pin_height, pin_length, bottom_length, pin_width, pin_thickness, r_upper_i=None, r_lower_i=None):

        # r_upper_i - pin upper corner, inner radius
        # r_lower_i - pin lower corner, inner radius
        # bottom_length - pin bottom flat part length (excluding corner arc)

        if r_lower_i == None:
            r_lower_i = pin_thickness / 2.0 if r_upper_i == None else r_upper_i

        if r_upper_i == None:
            r_upper_i = pin_thickness / 2.0
                    
        q = 1.0 - 1.0 / sqrt(2.0)
        r_upper_o = r_upper_i + pin_thickness # pin upper corner, outer radius
        r_lower_o = r_lower_i + pin_thickness # pin lower corner, outer radius
        bottom_length = bottom_length - r_lower_i
        top_length = pin_length - bottom_length - r_upper_i - r_lower_o

        return cq.Workplane("YZ")\
                 .moveTo(0, pin_height)\
                 .line(top_length, 0)\
                 .threePointArc((top_length + r_upper_i / sqrt(2), pin_height - r_upper_i * q),
                                (top_length + r_upper_i, pin_height - r_upper_i))\
                 .line(0, -(pin_height - r_upper_i - r_lower_o))\
                 .threePointArc((top_length + r_upper_i + r_lower_o * q, r_lower_o * q),
                                (top_length + r_upper_i + r_lower_o, 0))\
                 .line(bottom_length, 0)\
                 .line(0, pin_thickness)\
                 .line(-bottom_length, 0)\
                 .threePointArc((top_length + r_upper_i + r_lower_o - r_lower_i / sqrt(2), pin_thickness + r_lower_i * q),
                                (top_length + r_upper_i + r_lower_o - r_upper_i, pin_thickness + r_lower_i))\
                 .lineTo(top_length + r_upper_i + pin_thickness, pin_height - r_upper_i)\
                 .threePointArc((top_length + r_upper_o / sqrt(2), pin_height + pin_thickness - r_upper_o * q),
                                (top_length, pin_height + pin_thickness))\
                 .line(-top_length, 0).close().extrude(pin_width).translate((-pin_width / 2.0, 0, 0))

    def make_Jhook_pin(self, pin_height, pin_length, bottom_length, pin_width, pin_thickness, r_upper_i=None, r_lower_i=None):

        # r_upper_i - pin upper corner, inner radius
        # r_lower_i - pin lower corner, inner radius
        # bottom_length - pin bottom flat part length (excluding corner arc)

        if r_lower_i == None:
            r_lower_i = pin_thickness / 2.0 if r_upper_i == None else r_upper_i

        if r_upper_i == None:
            r_upper_i = pin_thickness / 2.0

        q = 1.0 - 1.0 / sqrt(2.0)
        r_upper_o = r_upper_i + pin_thickness # pin upper corner, outer radius
        r_lower_o = r_lower_i + pin_thickness # pin lower corner, outer radius
        bottom_length = bottom_length - r_lower_i
        top_length = 0.05

        return cq.Workplane("YZ")\
                 .moveTo(-(top_length + r_upper_i), pin_height)\
                 .line(top_length, 0)\
                 .threePointArc((-r_upper_i * q, pin_height - r_upper_i * q),
                                (0.0, pin_height - r_upper_i))\
                 .line(0, -(pin_height - r_upper_i - r_lower_i - pin_thickness))\
                 .threePointArc((-r_lower_i * q, pin_thickness + r_lower_i * q),
                                (-r_lower_i, pin_thickness))\
                 .line(-bottom_length, 0.0)\
                 .line(0, -pin_thickness)\
                 .line(bottom_length, 0)\
                 .threePointArc((r_lower_o / sqrt(2) - r_lower_i, r_lower_o * q),
                                (r_lower_o - r_lower_i, r_lower_o))\
                 .lineTo(r_upper_o - r_upper_i, pin_height - r_upper_i)\
                 .threePointArc((r_upper_o / sqrt(2) - r_upper_i, pin_height + pin_thickness - r_upper_o * q),
                                (-r_upper_i, pin_height + pin_thickness))\
                 .line(-top_length, 0).close().extrude(pin_width).translate((-pin_width / 2.0, 0, 0))

### EOF ###

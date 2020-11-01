#!/usr/bin/python
# -*- coding: utf8 -*-
#

#****************************************************************************
#*                                                                          *
#* base classes for generating part models in STEP AP214                    *
#*                                                                          *
#* This is part of FreeCAD & cadquery tools                                 *
#* to export generated models in STEP & VRML format.                        *
#*   Copyright (c) 2017                                                     *
#* Terje Io https://github.com/terjeio                                      *
#* Maurice https://launchpad.net/~easyw                                     *
#*                                                                          *
#*   Copyright (c) 2020                                                     *
#* Mountyrox   https://github.com/mountyrox                                 *
#*                                                                          *
#*                                                                          *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Lesser General Public License (LGPL)     *
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

# 2020-10-27

#
# parts of this code is based on work by other contributors
#

import cadquery as cq
import FreeCAD

from math import sin, cos, tan, radians, atan2

class Polyline:
    r"""A class for creating a polyline wire (including arcs) using **relative** moves (turtle graphics style)

    Most of the methods returns a reference to the class instance (self) which allows method chaining
    """

    def __init__(self, plane, origin=(0.0, 0.0)):
        self.commands = []
        self.plane = plane
        self.origin = origin
        self.x = 0.0
        self.y = 0.0
        self.addMoveTo(origin[0], origin[1])

    def getCurrentPosition(self):
        r"""get the current position in absolute coordinates

        :rtype: Point
        """
        return (self.x, self.y)


    def addMoveTo(self, x, y):
        r"""add a relative move (offset) from the current coordinate

        .. note:: when issued as the first call after instatiating the class then the origin is moved accordingly

        :param x: x distance from current position
        :type  x: ``float``
        :param y: y distance from current position
        :type  y: ``float``

        :rtype: self
        """
        self.x += x
        self.y += y

        if len(self.commands) == 1:
            self.commands = []
            self.origin = (self.x, self.y)
        self.commands.append((0, self.x, self.y))

        return self

    def addPoint(self, x, y):
        r"""add a straight line to point

        :param x: x distance from current position
        :type  x: ``float``
        :param y: y distance from current position
        :type  y: ``float``

        :rtype: self
        """
        self.x += x
        self.y += y
        self.commands.append((1, self.x, self.y))

        return self

    def addPoints(self, pointList):
        r"""add a list of new points

        :param pointList:
        :type  pointList: list of points

        :rtype: self

        Example where first half is defined by points and then mirrored by adding points in reverse order::

            ow = 0.6
            pw = self.pin_width
            c1 = (ow - pw) / 2.0
            pin = Polyline(cq.Workplane("XY"), origin=(0.0, self.body_width / 2.0))\
                             .addPoints([
                                    (ow / 2.0, 0),
                                    (0.0, -self.body_width),
                                    (-c1, -c1),
                                    (0.0, -(self.pin_length - pw)),
                                    (-pw / 4.0, -pw),
                                    (-pw / 4.0, 0.0),
                               ])\
                             .addMirror().make().extrude(self.pin_thickness)

        .. figure::  ../images/pin.png

           Rendering
        """

        for point in pointList:
            self.addPoint(point[0], point[1])

        return self

    def addArc(self, radius, angle=90, type=0):
        r"""Adds an arc to the polygon wire.
        Hint: If the arc angle is less than 90 degree the connection of the arc to the privious/next polyline segment 
        will not be tangential. To get tangential connections use ``addRadiusArc`` instead.

        :param radius: radius of the arc
        :type  radius: ``float``

        :rtype: ``self``
        """

        o = sin(radians(abs(angle) / 2.0))
        p = 1.0 - 1.0 * o
        f = -1.0 if angle < 0.0 else 1.0

        if type == 0:
            ap1 = self.x + radius * (p if f == 1.0 else o)
            ap2 = self.y + radius * (o if f == 1.0 else p) * f
        else:
            ap1 = self.x + radius * (p if f == -1.0 else o)
            ap2 = self.y + radius * (o if f == -1.0 else p) * f
        self.x += radius
        self.y += radius * f
        self.commands.append((2, self.x, self.y, ap1, ap2))

        return self


    def addRadiusArc(self, x, y, radius):
        r"""Adds an arc to the polygon wire.

        :param  x: the x coordinate of the end point of the arc
        :type   x: ``float``
        :param  y: the y coordinate of the end point of the arc
        :type   y: ``float``
        :param radius: radius of the arc
        :type  radius: ``float``

        :rtype: ``self``
        """
        self.x += x
        self.y += y
        self.commands.append((3, self.x, self.y, radius))

        return self


    def addThreePointArc(self, point1, point2):
        r"""create a three point arc

        The starting point is the current position, end point is *point2*, the arc will be drawn through point1

        :param point1:
        :type  width: ``float``

        :param point2:
        :type  point2: ``point``

        :rtype: self

        Example::

            l = 4
            a = 0.2
            w = 2 - a

            body = Polyline(cq.Workplane("XY"))\
                              .addPoint(0, w)\
                              .addThreePointArc((l / 2, a), (l, 0))\
                              .addPoint(0,- w).make().extrude(1)

        .. figure::  ../images/threepointarc.png

           Rendering

        """
        ap1 = self.x + point1[0]
        ap2 = self.y + point1[1]
        self.x += point2[0]
        self.y += point2[1]
        self.commands.append((2, self.x, self.y, ap1, ap2))

        return self

    def addChamferedRectangle(self, length, width, chamfer):
        r"""create a chamfered rectangle centered at the current point

        :param length:
        :type  length: ``float``

        :param width:
        :type  width: ``float``

        :param chamfer:
        :type  chamfer: ``float``

        :rtype: self

        See :func:`addRoundedRectangle` for an example
        """

        self.addMoveTo(-length / 2.0, -width / 2.0 + chamfer)

        length = length - chamfer * 2.0
        width = width - chamfer * 2.0

        self.addPoint(0.0, width)
        self.addPoint(chamfer, chamfer)
        self.addPoint(length, 0)
        self.addPoint(chamfer, -chamfer)
        self.addPoint(0.0, -width)
        self.addPoint(-chamfer, -chamfer)
        self.addPoint(-length, 0.0)
        self.addPoint(-chamfer, chamfer)

        return self

    def addRoundedRectangle(self, length, width, radius):
        r"""create a rounded rectangle centered at the current point

        :param length:
        :type  length: ``float``

        :param width:
        :type  width: ``float``

        :param cornerRadius:
        :type  cornerRadius: ``float``

        :rtype: self

        Example with a chamfered rectangle cutout::

            l = 4
            w = 2

            cutout = Polyline(cq.Workplane("XY"))\
                        .addChamferedRectangle(l - 0.3, w - 0.3, 0.3).make().extrude(1)

            body = Polyline(cq.Workplane("XY"))\
                        .addRoundedRectangle(l, w, 0.3).make().extrude(1).cut(cutout)

        .. figure::  ../images/roundedrectangle.png

           Rendering
        """

        self.addMoveTo(-length / 2.0, -width / 2.0 + radius)

        length = length - radius * 2.0
        width = width - radius * 2.0

        self.addPoint(0.0, width)
        self.addArc(radius, 90)
        self.addPoint(length, 0)
        self.addArc(radius, -90)
        self.addPoint(0.0, -width)
        self.addArc(-radius, 90)
        self.addPoint(-length, 0.0)
        self.addArc(-radius, -90)

        return self

    def mirror(self, axis="X"):
        r"""mirror the current polyline
        """

        result = []
        tx = -1.0 if axis == "X" else 1.0
        ty = -1.0 if axis != "X" else 1.0

        for point in self.commands:
            result.append((point[0], point[1] * tx, point[2] * ty))

        self.commands = result

        return self

    def addMirror(self, axis="X"):
        r"""add a mirror of the current polyline by reversing its direction. Can only be used for straight lines, 
        not if arcs are added into the polyline.
        """

        x0 = self.origin[0] if axis == "X" else 0.0
        y0 = self.origin[1] if axis != "X" else 0.0
        tx = -1.0 if axis == "X" else 1.0
        ty = -1.0 if axis != "X" else 1.0
        start = 2 #if axis == "X" else 0
        start = 1 if self.commands[0][start] == self.commands[-1][start] else 0

        for point in reversed(self.commands[start:-1]):
            self.commands.append((1, (point[1] - x0) * tx + x0, (point[2] - y0) * ty + y0))

        return self

    def _is_equal (self, point1, point2):
        return point1[0] == point2[0] and point1[1] == point2[1]

    def make(self):
        r""" Closes the polyline and creates a wire in the supplied plane

        :rtype: ``wire``
        """
        plane = self.plane

        for point in self.commands:
            if point[0] == 0:
                plane = plane.moveTo(point[1], point[2])
            elif point[0] == 1:
                plane = plane.lineTo(point[1], point[2])
            elif point[0] == 2:
                plane = plane.threePointArc((point[3], point[4]), (point[1], point[2]))
            elif point[0] == 3:
                plane = plane.radiusArc((point[1], point[2]), point[3]) 

        return plane.wire() if self._is_equal(self.origin, (self.commands[-1])[1:3]) else plane.close().wire()


class PartBase (object):
    """Base class for model creation, to be subclassed

    .. document private functions
    .. automethod:: _union_all
    .. automethod:: _mirror
    .. automethod:: _make_gullwing_pin
    .. automethod:: _make_Jhook_pin
    .. automethod:: _make_straight_pin
    .. automethod:: _make_angled_pin
    .. automethod:: _make_plastic_body
    """
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

    def __init__(self, params):
        # init mandatory base class attributes to some more or less sensible defaults
        self.footprints_dir = None

        self.rotation = 0
        self.make_me = True

        args = params._asdict()
        self.type = params.type if 'type' in args and params.type != None else "SMD"

        self.pin_width = params.pin_width if 'pin_width' in args and  params.pin_width != None else 0.4
        self.pin_thickness = params.pin_thickness if 'pin_thickness' in args and  params.pin_thickness != None else 0.2
        self.pin_length = params.pin_length if 'pin_length' in args and  params.pin_length != None else 3.2
        self.pin_pitch = params.pin_pitch if 'pin_pitch' in args and  params.pin_pitch != None else 2.54
        self.num_pins = params.num_pins if 'num_pins' in args and  params.num_pins != None else 2
        self.num_pin_rows = params.num_pin_rows if 'num_pin_rows' in args and  params.num_pin_rows != None else 2
        self.pin_rows_distance = params.pin_rows_distance if 'pin_rows_distance' in args and  params.pin_rows_distance != None else self.pin_pitch
        self.tht_pin_clamp_extension = params.tht_pin_clamp_extension if 'tht_pin_clamp_extension' in args and  params.tht_pin_clamp_extension != None else 0.45
        self.tht_pin_lower_clamp_angel = params.tht_pin_lower_clamp_angel if 'tht_pin_lower_clamp_angel' in args and  params.tht_pin_lower_clamp_angel != None else 50.0


        self.body_width = params.body_width if 'body_width' in args and  params.body_width != None else 6.0
        self.body_length = params.body_length if 'body_length' in args and  params.body_length != None else 6.0
        self.body_height = params.body_height if 'body_height' in args and  params.body_height != None else 3.5
        self.first_pin_pos = (0.0, 0.0) if self.num_pins is None else (self.pin_pitch * (self.num_pins / 2.0 / self.num_pin_rows - 0.5), self.pin_rows_distance / 2.0)
        self.offsets = (0.0, 0.0, 0.0)

    def say (self, msg):
        FreeCAD.Console.PrintMessage("##: " + str(msg) + '\n')

    def isValidModel (self):
        return self.make_me

    def _union_all(self, objects):
        o = objects[0]
        for i in range(1, len(objects)):
            o = o.union(objects[i])
        return o

    def _mirror(self, obj, pins=None, pitch=None):

        if pins is None:
            pins = self.num_pins // 2

        if pitch is None:
            pitch = self.pin_pitch

        objs = [obj]
        for i in range(2, pins + 1):
            objs.append(obj.translate((-pitch * (i - 1), 0, 0)))

        return self._union_all(objs)

    def _make_plastic_body(self, pin_area_height=None, body_angle_top=12.0, body_angle_bottom=12.0):
        """ create straight pin

        The pin will placed at coordinate 0, 0 and with the base at Z = 0

        :param pin_height: overall pin height
        :type pin_height: ``float``

        :rtype: ``solid``

        .. figure::  ../images/plasticbody.png

           Rendering example

        """

        self.say('\n###: ' + str(pin_area_height) + " " + str( body_angle_top))

        if pin_area_height is None:
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

    def _make_straight_pin(self, pin_height=None, style='Rectangular'):
        """ create straight pin

        The pin will placed at coordinate 0, 0 and with the base at Z = 0

        :param pin_height: overall pin height
        :type pin_height: ``float``

        :rtype: ``solid``

        .. figure::  ../images/straightpin.png

           Rendering example

        """
        if pin_height is None:
            pin_height = self.pin_length + self.body_board_distance

        return Polyline(cq.Workplane("XZ").workplane(offset=-self.pin_thickness / 2.0))\
                          .addPoints([
                                (self.pin_width / 2.0, 0.0),
                                (0.0, -(pin_height - self.pin_width)),
                                (-self.pin_width / 4.0, -self.pin_width),
                                (-self.pin_width / 4.0, 0.0),
                            ]).addMirror().make().extrude(self.pin_thickness)

    def _make_angled_pin(self, pin_height=None, top_length=0.0, top_extension=0.0, style='SMD'):
        """ create angled pin

        The pin will placed with center of top part at coordinate 0, 0 and with the base at Z = 0.
        The top part with length ``top_length`` is oriented downwards Z and the part with length ``pin_height`` points into Y direction.

        :param pin_height: overall pin height, from pin tip to outer surface of top part
        :type pin_height: ``float``

        :rtype: ``solid``

        .. figure::  ../images/angledsmdpin.png

           Rendering example, SMD style

        .. figure::  ../images/angledthtpin.png

           Rendering example, THT style

        """
        if pin_height is None:
            pin_height = self.pin_length

        d = self.pin_width / 10.0
        r_i = self.pin_thickness / 2.0
        r_o = r_i + self.pin_thickness # pin lower corner, outer radius

        if style == 'SMD': # make a horizontal pin
            pin = Polyline(cq.Workplane("XY").workplane(offset=-r_o), origin=(0.0, r_o))\
                             .addMoveTo(-self.pin_width / 2.0, 0.0)\
                             .addPoint(d, self.pin_length - d)\
                             .addThreePointArc((self.pin_width / 2.0 - d, d), (self.pin_width - d * 2.0, 0.0))\
                             .addPoint(d, -self.pin_length + d).make().extrude(self.pin_thickness)

        else: # make a vertical pin
            pin = self._make_straight_pin(pin_height-r_o)\
                      .rotate((0,0,0), (1,0,0), 90)\
                      .translate((0, r_o, - self.pin_thickness))

        # make the arc joining the pin segments
        arc = Polyline(cq.Workplane("YZ").workplane(offset=-self.pin_width / 2.0))\
                         .addArc(r_o, -90, 1)\
                         .addPoint(0, self.pin_thickness)\
                         .addArc(-r_i, -90).make().extrude(self.pin_width)
        
        pin = pin.union(arc).translate((0, -self.pin_thickness / 2, -top_length))

        if(round(top_length, 6) != 0.0):
            pin = pin.union(cq.Workplane("XZ")\
                     .workplane(offset=-self.pin_thickness / 2)\
                     .moveTo(self.pin_width / 2.0, r_o-(top_length + r_o))\
                     .line(0, top_length)\
                     .line(-self.pin_width, 0)\
                     .line(0, -top_length)\
                     .close().extrude(self.pin_thickness))
        elif (round(top_extension, 6) != 0.0):
            pin = pin.union(cq.Workplane("XZ")\
                     .workplane(offset=-self.pin_thickness / 2)\
                     .moveTo(self.pin_width / 2.0, 0.0)\
                     .line(0.0, top_extension)\
                     .line(-self.pin_width, 0.0)\
                     .line(0.0, -top_extension)\
                     .close().extrude(self.pin_thickness))
        
        
        return pin


    def _make_angled_clamping_pin(self, pin_height, top_length=0.0, tht_pin_clamp_extension=0.45, tht_pin_lower_clamp_angel=50.0):
        """ create angled THT pin with asymetrical lambda shaped clamp 

        The pin will placed at coordinate 0, 0 and with the base at Z = 0

        :param pin_height: overall pin height, from pin tip to outer surface of top part
        :type pin_height: ``float``
        :param top_length: top length of pin height, measured from arc to end og top part. Default value: 0.0
        :type top_length: ``float``
        :param tht_pin_clamp_extension: width of clamp. For a straight pin this value would be 0.0 (0.0 is not allowed). Default value: 0.45
        :type tht_pin_clamp_extension: ``float``
        :param tht_pin_lower_clamp_angel: angle between lover clamp leg an straight part of pin tip. Default value: 50 degree
        :type tht_pin_lower_clamp_angel: ``float``

        :rtype: ``solid``

        """

        # the following radii will only be uses to connect top part of pin (pin_length) and lower part of pin (pin_height)
        # the inner angles of the clamp will be done by fillet
        r_i = self.pin_thickness / 2.0
        r_o = r_i + self.pin_thickness 

        # The pin is getting smaller at the tip. The projected length of this tip part is equal to the pin width. 
        # Therefore the part of the pin with constant width is: pin_height - self.pin_width
        # Additionally we have to consider the upper arc:  pin_height_without_tip = pin_height - self.pin_width - 'fraction of arc radius'

        # clamp angle (alpha) to tip of pin.
        alpha = radians (tht_pin_lower_clamp_angel)
        sa = sin(alpha)
        ca = cos(alpha)
        ta = tan(alpha)
        # the straight part of pin below the clamp should be smaller as the clamp angle is smaller, beween 0.3 ... 0.15.
        # We take clamp angle / 175.0 of the height, but not less than pin width (see comment above)
        s = max (tht_pin_lower_clamp_angel / 175.0 * pin_height, self.pin_width)

        # projected height of lower part of clamp is:
        hl = tht_pin_clamp_extension / ta
        # projection height of the upper part of clamp we call hu. The corresponding angle beta has to be calculated. 
        # The height of the pin can be written as: H = s + hl + hu + 'fraction of arc radius'. The fraction of arc radius is: r_o * (1-cos(90-beta)) = r_o * (1-sin(beta)).
        # With (hu = tht_pin_clamp_extension / tan(beta) we get: H = s + hl + tht_pin_clamp_extension / tan(beta) + r_o * (1-sin(beta))
        # This equation could be used to calculate the angle beta, but we must solve a nonlinear equation to the power of four
        # Following approximation can be used: Instead of using the correct fraction of the arc radius we use the complete radius r_o. 
        # This would result in a pin height which is be a little bit too small. To compensate this we inclease the height of the lower tip part (s) by the missing amount. 
        hu = pin_height - r_o - s - hl
        beta = atan2 (tht_pin_clamp_extension, hu)
        sb = sin (beta)
        cb = cos (beta)
        tb = tht_pin_clamp_extension / hu  # tan (beta)

        # This results in a new height, a bit smaller than original height:
        h = s + hl + hu + r_o * (1.0-sb)
        # the correction to s is:
        s += (pin_height - h)
        # Whwn making the pin no arcs will be used for the inner and outer clamp angles.
        # The outer corner of the clamp will be rounded by the last fillet command.
        # When creating the pin, the inner clamp point lies on the bisecting line of angle 180-(alpha+beta).
        # For creating this point we need the tan((alpha+beta)/2). 
        # The length of the inner clamp line is 'pin_thickness*tan((alpha+beta)/2)' shorter than the length of the outer clamp line.
        tbl = tan ((alpha+beta)/2.0)
        dl = self.pin_thickness * tbl
        pin = Polyline(cq.Workplane("YZ").workplane(offset=-self.pin_width / 2.0), origin=(r_o * (1.0-sb), -r_o*cb))\
                            .addPoint(hu, -tht_pin_clamp_extension)\
                            .addPoint(hl, +tht_pin_clamp_extension)\
                            .addPoint(0.0, self.pin_thickness)\
                            .addRadiusArc(-self.pin_thickness * sa, -self.pin_thickness * (1.0 - ca), -self.pin_thickness)\
                            .addPoint(-(hl - dl*ca), -(tht_pin_clamp_extension - dl*sa))\
                            .addPoint(-(hu - dl*cb), +(tht_pin_clamp_extension - dl*sb))\
                            .make().extrude(self.pin_width).edges("<Z").fillet(self.pin_thickness)

        # make pin tip with overall length s
        tip = Polyline(cq.Workplane("XY").workplane(offset=-r_o*cb))\
                          .addMoveTo(0.0, (hl + hu + r_o * (1.0-sb)))\
                          .addPoints([
                                (self.pin_width / 2.0, 0.0),
                                (0.0, (s - self.pin_width)),
                                (-self.pin_width / 4.0, self.pin_width),
                                (-self.pin_width / 4.0, 0.0),
                            ]).addMirror().make().extrude(self.pin_thickness)

        pin = pin.union(tip)

        # make the arc to connect top part of pin
        arc = Polyline(cq.Workplane("YZ").workplane(offset=-self.pin_width / 2.0))\
                         .addRadiusArc(r_o * (1.0-sb), -r_o * cb, -r_o)\
                         .addPoint(self.pin_thickness * sb, self.pin_thickness * cb)\
                         .addRadiusArc(-r_i * (1.0-sb), r_i * cb, r_i).make().extrude(self.pin_width)

        pin = pin.union(arc).translate((0, -self.pin_thickness / 2, -top_length))

        # make the top part of the pin
        if(round(top_length, 6) != 0.0):
            pin = pin.union(cq.Workplane("XZ")\
                     .workplane(offset=-self.pin_thickness / 2)\
                     .moveTo(self.pin_width / 2.0, r_o-(top_length + r_o))\
                     .line(0, top_length)\
                     .line(-self.pin_width, 0)\
                     .line(0, -top_length)\
                     .close().extrude(self.pin_thickness))

        return pin

    def _make_angled_lambda_pin(self, pin_height, top_length=0.0, tht_pin_clamp_extension=0.45):
        """ create angled THT pin with symetrical lambda shaped clamp 

        The pin will placed at coordinate 0, 0 and with the base at Z = 0

        :param pin_height: overall pin height, from pin tip to outer surface of top part
        :type pin_height: ``float``
        :param top_length: top length of pin height, measured from arc to end og top part. Default value: 0.0
        :type top_length: ``float``
        :param tht_pin_clamp_extension: width of clamp. For a straight pin this value would be 0.0 (0.0 is not allowed). Default value: 0.45
        :type tht_pin_clamp_extension: ``float``

        :rtype: ``solid``

        """

        # the following radii will only be uses to connect top part of pin (pin_length) and lower part of pin (pin_height)
        # the inner angles of the clamp 
        r_i = self.pin_thickness / 2.0
        r_o = r_i + self.pin_thickness 
        
        # The pin is getting smaller at the tip. The projected length of this tip part is equal to the pin width. 
        # Therefore the part of the pin with constant height is: pin_height - self.pin_width.
        # Additionally the height is measured from tip to outer surface of top part of pin, we must subtract the outer radius
        pin_height_without_tip = pin_height - self.pin_width - r_o
        # projected heigth of halve the clamp is:
        q = 0.35  # fraction of clamp compared to the pin_height_without_tip. The smaler the value the steeper the clamp   
        d = pin_height_without_tip * q  # 2*d is height of clamp
        
        # clamp angle (alpha):
        alpha = atan2 (tht_pin_clamp_extension, d)
        ca = cos(alpha)
        sa = sin(alpha)
        ta = tht_pin_clamp_extension / d  # tan (alpha)

        s = (pin_height_without_tip - 2.0 * d) / 6.0  # rest of pin hight 5/6 above clamp 1/6 below
        
        # make clamp part of pin. For the inner angles of the clamp no arcs will be used.
        # The same for the outer corner of the clamp, it will be rounded by the last fillet command.
        pin = Polyline(cq.Workplane("YZ").workplane(offset=-self.pin_width / 2.0), origin=(r_o, -r_o))\
                            .addPoint(5.0 * s, 0.0)\
                            .addPoint(d, -tht_pin_clamp_extension)\
                            .addPoint(d, +tht_pin_clamp_extension)\
                            .addPoint(s, 0.0)\
                            .addPoint(0.0, self.pin_thickness)\
                            .addPoint(-s, 0.0)\
                            .addRadiusArc(-self.pin_thickness * sa, -self.pin_thickness * (1.0 - ca), -self.pin_thickness)\
                            .addPoint(-(d - self.pin_thickness * sa), -(tht_pin_clamp_extension - self.pin_thickness * (1.0/ca - ca)))\
                            .addPoint(-(d - self.pin_thickness * sa), +(tht_pin_clamp_extension - self.pin_thickness * (1.0/ca - ca)))\
                            .addRadiusArc(-self.pin_thickness * sa, +self.pin_thickness * (1.0 - ca), -self.pin_thickness)\
                            .addPoint(-5.0 * s, 0.0)\
                            .make().extrude(self.pin_width).edges("<Z").fillet(0.2)

        tip = Polyline(cq.Workplane("XY").workplane(offset=-self.pin_thickness * 1.5))\
                          .addMoveTo(0.0, pin_height_without_tip + r_o)\
                          .addPoints([
                                (self.pin_width / 2.0, 0.0),
                                (-self.pin_width / 4.0, self.pin_width),
                                (-self.pin_width / 4.0, 0.0),
                            ]).addMirror().make().extrude(self.pin_thickness)

        pin = pin.union(tip)

        # make the arc to connect top part of pin
        arc = Polyline(cq.Workplane("YZ").workplane(offset=-self.pin_width / 2.0))\
                         .addArc(r_o, -90, 1)\
                         .addPoint(0, self.pin_thickness)\
                         .addArc(-r_i, -90).make().extrude(self.pin_width)

        pin = pin.union(arc).translate((0, -self.pin_thickness / 2, -top_length))

        # make the top part of the pin
        if(round(top_length, 6) != 0.0):
            pin = pin.union(cq.Workplane("XZ")\
                     .workplane(offset=-self.pin_thickness / 2)\
                     .moveTo(self.pin_width / 2.0, r_o-(top_length + r_o))\
                     .line(0, top_length)\
                     .line(-self.pin_width, 0)\
                     .line(0, -top_length)\
                     .close().extrude(self.pin_thickness))
     
        
        return pin

    def _make_gullwing_pin(self, pin_height, bottom_length, r_upper_i=None, r_lower_i=None):
        """ create gull wing pin

        The pin will placed at coordinate 0, 0 and with the base at Z = 0

        :param pin_height: overall pin height
        :type pin_height: ``float``

        :rtype: ``solid``

        .. figure::  ../images/gullwingpin.png

           Rendering example

        """

        # r_upper_i - pin upper corner, inner radius
        # r_lower_i - pin lower corner, inner radius
        # bottom_length - pin bottom flat part length (excluding corner arc)

        if r_lower_i is None:
            r_lower_i = self.pin_thickness / 2.0 if r_upper_i is None else r_upper_i

        if r_upper_i is None:
            r_upper_i = self.pin_thickness / 2.0

        r_lower_i = max (r_lower_i, 0.0001)
        r_upper_i = max (r_upper_i, 0.0001)
        r_upper_o = r_upper_i + self.pin_thickness # pin upper corner, outer radius
        r_lower_o = r_lower_i + self.pin_thickness # pin lower corner, outer radius
        bottom_length = max (bottom_length - r_lower_i, 0.000001)
        top_length = max (self.pin_length - bottom_length - r_upper_i - r_lower_o, 0.0001)

        return Polyline(cq.Workplane("YZ"), origin=(0, pin_height))\
                          .addPoint(top_length, 0)\
                          .addArc(r_upper_i, -90)\
                          .addPoint(0, -(pin_height - r_upper_i - r_lower_o))\
                          .addArc(r_lower_o, -90, 1)\
                          .addPoint(bottom_length, 0)\
                          .addPoint(0, self.pin_thickness)\
                          .addPoint(-bottom_length, 0)\
                          .addArc(-r_lower_i, -90)\
                          .addPoint(0, pin_height - r_upper_i - r_lower_o)\
                          .addArc(-r_upper_o, -90, 1)\
                          .addPoint(-top_length, 0).make().extrude(self.pin_width).translate((-self.pin_width / 2.0, 0, 0))


    def _make_angular_gullwing_pin(self, pin_height, bottom_length, pin_angle=65.0, r_upper_i=None, r_lower_i=None):
        """ create an angular gull wing pin

        The pin will be placed at coordinate 0, 0 and with the base at Z = 0

        :param pin_height: overall pin height (measured from upper leg bottom to lower leg bottom)
        :type pin_height: ``float``
        :param bottom_length: bottom length of gullwing pin (measured from end of pin to begin of arc)
        :type bottom_length: ``float``
        :param pin_angle: angle between horizontal and mid part of pin (for vertical bent pin angle is 90 deg).
                          Minimum angle is 20 deg, lower angles will be set to default (65 deg)
        :type pin_angle: ``float``
        :rtype: ``solid``
        """

        # r_upper_i - pin upper corner, inner radius
        # r_lower_i - pin lower corner, inner radius
        # bottom_length - pin bottom flat part length (excluding corner arc)

        if r_lower_i is None:
            r_lower_i = self.pin_thickness / 2.0 if r_upper_i is None else r_upper_i

        if r_upper_i is None:
            r_upper_i = self.pin_thickness / 2.0

        if pin_angle <= 20.0:
             pin_angle = 65.0

        ca = cos(radians (pin_angle))
        sa = sin(radians (pin_angle))

        r_upper_o = r_upper_i + self.pin_thickness # pin upper corner, outer radius
        r_lower_o = r_lower_i + self.pin_thickness # pin lower corner, outer radius
        
        # The bottom length given to the function is the lenghth from half the outer bend radius to end of pin.
        # The straight part has to be removed by this half outer bend radius.
        bottom_length = bottom_length - (r_lower_o  * sin(radians (pin_angle/2.0)))
        top_length = self.pin_length - bottom_length - (r_upper_i + r_lower_o) * sa - (pin_height - (r_upper_i + r_lower_o) * (1.0 - ca))/tan(radians (pin_angle))
        if top_length < 0:
            self.say('\n###: Combination of pin length and pin angle not possible. Pin angle will be set to 90 deg')
            top_length = self.pin_length - bottom_length - (r_upper_i + r_lower_o)
            ca = 0.0
            sa = 1.0

        vert_center_length = pin_height - (r_upper_i + r_lower_o) * (1.0 - ca)  # vertical length of middle part of pin
        hor_center_length = self.pin_length - bottom_length - top_length - (r_upper_i + r_lower_o) * sa   # horizontal length of middle part of pin
        

        return Polyline(cq.Workplane("YZ"), origin=(0, pin_height))\
                          .addPoint(top_length, 0)\
                          .addRadiusArc(r_upper_i * sa, -r_upper_i * (1.0 - ca), r_upper_i)\
                          .addPoint(hor_center_length, -vert_center_length)\
                          .addRadiusArc(r_lower_o * sa, -r_lower_o * (1.0 - ca), -r_lower_o)\
                          .addPoint(bottom_length, 0)\
                          .addPoint(0, self.pin_thickness)\
                          .addPoint(-bottom_length, 0)\
                          .addRadiusArc(-r_lower_i * sa, r_lower_i * (1.0 - ca), r_lower_i)\
                          .addPoint(-hor_center_length, vert_center_length)\
                          .addRadiusArc(-r_upper_o * sa, r_upper_o * (1.0 - ca), -r_upper_o)\
                          .addPoint(-top_length, 0).make().extrude(self.pin_width).translate((-self.pin_width / 2.0, 0, 0))



    def _make_Jhook_pin(self, pin_height, bottom_length, top_length = 0.05, r_upper_i=None, r_lower_i=None):
        """ create J-hook pin

        The pin will placed at coordinate 0, 0 and with the base at Z = 0

        :param pin_height: overall pin height
        :type pin_height: ``float``

        :rtype: ``solid``

        .. figure::  ../images/jhookpin.png

           Rendering example

        """

        # r_upper_i - pin upper corner, inner radius
        # r_lower_i - pin lower corner, inner radius
        # bottom_length - pin bottom flat part length (excluding corner arc)

        if r_lower_i is None:
            if r_upper_i is not None and r_upper_i > 0.0:
                r_lower_i = r_upper_i
            else:
                r_lower_i = self.pin_thickness / 2.0 


        if r_upper_i is None:
            r_upper_i = self.pin_thickness / 2.0

        r_upper_o = r_upper_i + self.pin_thickness # pin upper corner, outer radius
        r_lower_o = r_lower_i + self.pin_thickness # pin lower corner, outer radius
        bottom_length = bottom_length - r_lower_i
        
        pl = Polyline(cq.Workplane("YZ"), (-(top_length + r_upper_i), pin_height))
        if top_length > 0.0:
            pl = pl.addPoint(top_length, 0)
        if r_upper_i > 0.0:
            pl = pl.addArc(r_upper_i, -90)

        pl = pl.addPoint(0, -(pin_height - r_upper_i - r_lower_i - self.pin_thickness))\
                          .addArc(-r_lower_i, 90)\
                          .addPoint(-bottom_length, 0)\
                          .addPoint(0, -self.pin_thickness)\
                          .addPoint(bottom_length, 0)\
                          .addArc(r_lower_o, 90, 1)\
                          .addPoint(0, pin_height - r_upper_i - r_lower_i - self.pin_thickness)
                          
        if top_length > 0.0:
            pl = pl.addArc(-r_upper_o, -90, 1).addPoint(-top_length, 0)

        pl = pl.make()
        pl = pl.extrude(self.pin_width)
        pl = pl.translate((-self.pin_width / 2.0, 0, 0))
        return pl

### EOF ###

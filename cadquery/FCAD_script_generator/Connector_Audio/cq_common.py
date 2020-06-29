#!/usr/bin/python
# -*- coding: utf-8 -*-
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

# 2017-11-30

#
# parts of this code is based on work by other contributors
# last copied from cq_base_model.py
#

import collections
from collections import namedtuple

from math import sin, tan, radians

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

from Helpers import show
import Part as FreeCADPart

class Polyline:
    r"""A class for creating a polyline wire (including arcs) using **relative** moves (turtle graphics style)

    :param  plane: the workplane to add the polyline (as a wire)
    :type   plane: ``workplane``
    :param origin: point
    :type  origin: ``point``

    Most of the methods returns a reference to the class instance (self) which allows method chaining
    """

    def __init__(self, plane, origin=(0.0, 0.0)):
        self.commands = []
        self.plane = plane
        self.origin = origin
        self.x = 0
        self.y = 0
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
        r"""add a mirror of the current polyline by reversing its direction
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

        return plane.wire() if self._is_equal(self.origin, (self.commands[-1])[1:3]) else plane.close().wire()

class cq_parameters_help():

    def __init__(self):
        self.pin_thickness = 0.15
        self.pin_length = 1.0
        self.pin_width = 0.4

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

        r_upper_o = r_upper_i + self.pin_thickness # pin upper corner, outer radius
        r_lower_o = r_lower_i + self.pin_thickness # pin lower corner, outer radius
        bottom_length = bottom_length - r_lower_i
        top_length = self.pin_length - bottom_length - r_upper_i - r_lower_o

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
            r_lower_i = self.pin_thickness / 2.0 if r_upper_i is None else r_upper_i

        if r_upper_i is None:
            r_upper_i = self.pin_thickness / 2.0

        r_upper_o = r_upper_i + self.pin_thickness # pin upper corner, outer radius
        r_lower_o = r_lower_i + self.pin_thickness # pin lower corner, outer radius
        bottom_length = bottom_length - r_lower_i
        

        return Polyline(cq.Workplane("YZ"), (-(top_length + r_upper_i), pin_height))\
                          .addPoint(top_length, 0)\
                          .addArc(r_upper_i, -90)\
                          .addPoint(0, -(pin_height - r_upper_i - r_lower_i - self.pin_thickness))\
                          .addArc(-r_lower_i, 90)\
                          .addPoint(-bottom_length, 0)\
                          .addPoint(0, -self.pin_thickness)\
                          .addPoint(bottom_length, 0)\
                          .addArc(r_lower_o, 90, 1)\
                          .addPoint(0, pin_height - r_upper_i - r_lower_i - self.pin_thickness)\
                          .addArc(-r_upper_o, -90, 1)\
                          .addPoint(-top_length, 0).make().extrude(self.pin_width).translate((-self.pin_width / 2.0, 0, 0))

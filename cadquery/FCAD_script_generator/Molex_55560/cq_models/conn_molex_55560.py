# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script to generate connector models

## requirements
## freecad (v1.5 and v1.6 have been tested)
## cadquery FreeCAD plugin (v0.3.0 and v0.2.0 have been tested)
##   https://github.com/jmwright/cadquery-freecad-module

## This script can be run from within the cadquery module of freecad.
## To generate VRML/ STEP files for, use export_conn_jst_xh
## script of the parrent directory.

#* This is a cadquery script for the generation of MCAD Models.             *
#*                                                                          *
#*   Copyright (c) 2016                                                     *
#* Rene Poeschl https://github.com/poeschlr                                 *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU General Public License (GPL)             *
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
#* The models generated with this script add the following exception:       *
#*   As a special exception, if you create a design which uses this symbol, *
#*   and embed this symbol or unaltered portions of this symbol into the    *
#*   design, this symbol does not by itself cause the resulting design to   *
#*   be covered by the GNU General Public License. This exception does not  *
#*   however invalidate any other reasons why the design itself might be    *
#*   covered by the GNU General Public License. If you modify this symbol,  *
#*   you may extend this exception to your version of the symbol, but you   *
#*   are not obligated to do so. If you do not wish to do so, delete this   *
#*   exception statement from your version.                                 *
#****************************************************************************

__title__ = "model description for Molex SlimStack 55560 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for Molex SlimStack 55560 series connectors using cadquery'

___ver___ = "0.1 21/04/2017"


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
from conn_molex_55560_params import *

from ribbon import Ribbon

def generate_pin(params, calc_dim):
    pin_group_width = calc_dim.pin_group_width
    pin_width = seriesParams.pin_width
    pin_thickness = seriesParams.pin_thickness
    pin_pitch = params.pin_pitch
    body_width = seriesParams.body_width
    # hole_length = seriesParams.hole_length
    # hole_offset = seriesParams.hole_offset
    # slot_height = seriesParams.slot_height
    MIN_RAD = 0.08
    p_list = [
        ('start', {'position': ((-body_width/2 - 0.735, pin_thickness/2.0)), 'direction': 0.0, 'width':pin_thickness}),
        ('line', {'length': 0.735}),
        ('arc', {'radius': MIN_RAD, 'angle': 60.0}),
        ('line', {'length': 0.05}),
        ('arc', {'radius': MIN_RAD, 'angle': -60.0}),
        ('line', {'length': 0.4})
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-pin_width/2.0 - pin_group_width/2.0), p_list)
    pin = ribbon.drawRibbon().extrude(pin_width)
    return pin


def generate_pins(params, calc_dim):
    num_pins=params.num_pins
    pin_pitch=params.pin_pitch
    pin_A = generate_pin(params, calc_dim)
    pin_B = pin_A.mirror("XZ")
    pin_pair = pin_A.union(pin_B)
    pins = pin_pair
    for i in range(0, num_pins / 2):
        pins = pins.union(pin_pair.translate((i*pin_pitch,0,0)))
    return pins


"""
def generate_contact(params, calc_dim):
    pin_group_width = calc_dim.pin_group_width
    pin_width = seriesParams.pin_width
    pin_thickness = seriesParams.pin_thickness
    pin_pitch = params.pin_pitch
    body_width = seriesParams.body_width
    hole_length = seriesParams.hole_length
    hole_offset = seriesParams.hole_offset
    slot_height = seriesParams.slot_height
    MIN_RAD = 0.08
    c1_list = [
        ('start', {'position': ((-body_width/2 - 0.5, pin_thickness/2.0)), 'direction': 0.0, 'width':pin_thickness}),
        ('line', {'length': 0.5}),
        ('arc', {'radius': MIN_RAD, 'angle': 60.0}),
        ('line', {'length': 0.05}),
        ('arc', {'radius': MIN_RAD, 'angle': -60.0}),
        ('line', {'length': 0.6}),
        ('arc', {'radius': MIN_RAD, 'angle': -45.0}),
        ('arc', {'radius': MIN_RAD, 'angle': 45.0}),
        ('line', {'length': 0.73}),
        ('arc', {'radius': 0.15, 'angle': 95.0}),
        ('line', {'length': 0.49}),
        ('arc', {'radius': 0.1, 'angle': 85.0})
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-pin_width/2.0 - pin_group_width/2.0), c1_list)
    contact1 = ribbon.drawRibbon().extrude(pin_width)
    c2_list = [
        ('start', {'position': ((-hole_offset-hole_length/2.0+pin_thickness/2.0, slot_height-MIN_RAD-pin_thickness/2.0)), 'direction': 90.0, 'width':pin_thickness}),
        ('arc', {'radius': MIN_RAD, 'angle': -90.0}),
        ('line', {'length': hole_length-2.0*MIN_RAD-pin_thickness}),
        ('arc', {'radius': MIN_RAD, 'angle': -90.0}),
        ('line', {'length': slot_height - 0.45}),
        ('arc', {'radius': MIN_RAD, 'angle': 90.0}),
        ('line', {'length': 0.2}),
        ('arc', {'radius': 0.15, 'angle': 90.0}),
        ('line', {'length': 0.35}),
        ('arc', {'radius': 0.1, 'angle': -90.0})
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-pin_width/2.0 - pin_group_width/2.0), c2_list)
    contact2 = ribbon.drawRibbon().extrude(pin_width)
    contact1 = contact1.union(contact2)
    return contact1


def generate_contacts(params, calc_dim):
    num_pins=params.num_pins
    pin_pitch=params.pin_pitch
    contact1 = generate_contact(params, calc_dim)
    contact2=contact1.mirror("XZ")
    contact_pair = contact1.union(contact2)
    contacts = contact_pair
    for i in range(0, num_pins / 2):
        contacts = contacts.union(contact_pair.translate((i*pin_pitch,0,0)))
    return contacts

"""

def my_rarray(self, xSpacing, ySpacing, xCount, yCount, center=True):
        """
        Local version of rarray() function to fix bug in handling of pitch values below 1.0

        Creates an array of points and pushes them onto the stack.
        If you want to position the array at another point, create another workplane
        that is shifted to the position you would like to use as a reference

        :param xSpacing: spacing between points in the x direction ( must be > 0)
        :param ySpacing: spacing between points in the y direction ( must be > 0)
        :param xCount: number of points ( > 0 )
        :param yCount: number of points ( > 0 )
        :param center: if true, the array will be centered at the center of the workplane. if
            false, the lower left corner will be at the center of the work plane
        """

        if xSpacing <= 0 or ySpacing <= 0 or xCount < 1 or yCount < 1:
            raise ValueError("Spacing and count must be > 0 ")

        lpoints = []  # coordinates relative to bottom left point
        for x in range(xCount):
            for y in range(yCount):
                lpoints.append((xSpacing * x, ySpacing * y))

        #shift points down and left relative to origin if requested
        if center:
            xc = xSpacing*(xCount-1) * 0.5
            yc = ySpacing*(yCount-1) * 0.5
            cpoints = []
            for p in lpoints:
                cpoints.append((p[0] - xc, p[1] - yc))
            lpoints = list(cpoints)

        return self.pushPoints(lpoints)


def generate_body(params, calc_dim):

    body_length = calc_dim.length
    body_width = seriesParams.body_width
    body_height = seriesParams.body_height
    body_fillet_radius = seriesParams.body_fillet_radius
    body_chamfer = seriesParams.body_chamfer
    pin_housing_height = seriesParams.pin_housing_height

    pin_inside_distance = seriesParams.pin_inside_distance
    num_pins = params.num_pins
    pin_pitch = params.pin_pitch

    pocket_inside_distance = seriesParams.pocket_inside_distance
    pocket_width = seriesParams.pocket_width
    pocket_base_thickness = seriesParams.pocket_base_thickness
    pocket_fillet_radius = seriesParams.pocket_fillet_radius

    contact_thickness = seriesParams.contact_thickness
    contact_slot_width = seriesParams.contact_slot_width
    top_slot_offset = seriesParams.top_slot_offset

    lock_positions = params.lock_positions
    pin_group_width = calc_dim.pin_group_width


    # body
    body_A = cq.Workplane("XY")\
        .rect(body_length, body_width).extrude(body_height)\
        .edges("|Z").fillet(body_fillet_radius)
    body_A = body_A.faces("<Y").workplane().center(0, -body_height/2.0).rect(body_length-2*pocket_inside_distance,pin_housing_height*2.0).cutBlind(-body_fillet_radius)
    body_A = body_A.faces(">Y").workplane().center(0, -body_height/2.0).rect(body_length-2*pocket_inside_distance,pin_housing_height*2.0).cutBlind(-body_fillet_radius)
    body_A = body_A.faces(">Z").chamfer(body_chamfer)

    body_B = cq.Workplane("XY")\
        .rect(body_length-0.4, body_width-0.4).extrude(body_height)
    body_A = body_A.cut(body_B)

    pocket = cq.Workplane("XY").workplane(offset=body_height)\
        .rect(body_length - 2.0 * pocket_inside_distance, pocket_width)\
        .extrude(-(body_height - pocket_base_thickness)).edges("|Z").fillet(pocket_fillet_radius)
    body_B = body_B.cut(pocket)

    body_B = body_B.faces(">Z").edges("not(<X or >X or <Y or >Y)").fillet(body_chamfer)
    body = body_A.union(body_B)

    # cut slots for contacts
    body = body.faces(">Z").workplane().center(0, top_slot_offset)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 1)\
        .center(0, -2 * top_slot_offset)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 1)\
       .cutBlind(-contact_thickness)

    body = body.faces(">Z").workplane().center(0, pocket_width / 2.0)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 2 * contact_thickness)\
        .center(0, -pocket_width)
    body = my_rarray(body, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 2 * contact_thickness)\
       .cutBlind(-body_height + pocket_base_thickness)

   # cut overall side housing
    cutter_A = cq.Workplane("YZ").workplane(offset=(body_length - 2.0 * pocket_inside_distance) / 2.0).center(body_width / 2.0 - 0.2, body_height)\
        .line(0.05, -0.1).line(0,-0.1).line(0.05, -0.1).line(0,-0.3).line(0.06,-0.06)\
        .line(1,0).line(0, body_height).close().extrude(-(body_length - 2.0 * pocket_inside_distance))
    cutter_B = cutter_A.mirror("XZ")
    body = body.cut(cutter_A.union(cutter_B))

    # cut lock housings in all positions
    cutter = cq.Workplane("XY").workplane(offset=0.49).center(0, body_width / 2.0)
    cutter = my_rarray(cutter, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 0.25)\
        .center(0, -body_width)
    cutter = my_rarray(cutter, pin_pitch, 1, (num_pins/2), 1).rect(contact_slot_width, 0.25)\
       .extrude(0.25)
    body = body.cut(cutter)

    # overcut to remove selected lock housings
    overcut = []
    if 'all' in lock_positions:
        # no need to overcut any lock housings
        pass
    else:
        if 'none' in lock_positions:
            # need to overcut all lock housings
            overcut = range(1, 1 + num_pins / 2)
        else:
            # need to overcut the housings not in lock_positions
            overcut = [i for i in range(1, 1 + num_pins / 2) if i not in lock_positions]
        cut = cq.Workplane("XY").workplane(offset=0.49).center(-pin_group_width / 2.0, body_width / 2.0)\
            .rect(contact_slot_width, 0.25)\
            .center(0, -body_width)\
            .rect(contact_slot_width, 0.25)\
            .extrude(3)
        for i in overcut:
            cutter = cutter.union(cut.translate(((i-1)*pin_pitch,0,0)))
        body = body.cut(cutter)

    return body


def generate_part(part_key):
    params = all_params[part_key]
    calc_dim = dimensions(params)
    body = generate_body(params, calc_dim)
    pins = generate_pins(params, calc_dim)
    # contacts = generate_contacts(params, calc_dim)
    return (body, pins)


# opened from within freecad
if "module" in __name__:
    # part_to_build = 'molex_55560_2x08'
    # part_to_build = 'molex_55560_2x10'
    # part_to_build = 'molex_55560_2x11'
    # part_to_build = 'molex_55560_2x12'
    # part_to_build = 'molex_55560_2x15'
    part_to_build = 'molex_55560_2x17'
    # part_to_build = 'molex_55560_2x20'
    # part_to_build = 'molex_55560_2x23'
    # part_to_build = 'molex_55560_2x25'
    # part_to_build = 'molex_55560_2x30'
    # part_to_build = 'molex_55560_2x40'

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 part_to_build + "\n")
    (body, pins) = generate_part(part_to_build)
    
    show(body)
    show(pins)
    # show(contacts)

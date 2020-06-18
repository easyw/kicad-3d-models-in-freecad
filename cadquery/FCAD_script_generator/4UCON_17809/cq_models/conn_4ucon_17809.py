#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CadQuery script to generate connector models

## requirements
## freecad (v1.5 and v1.6 have been tested)
## cadquery FreeCAD plugin (v0.3.0 and v0.2.0 have been tested)
##   https://github.com/jmwright/cadquery-freecad-module

## This script can be run from within the cadquery module of freecad.
## To generate VRML/ STEP files for, use export_conn_jst_xh
## script of the parent directory.

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

__title__ = "model description for 4UCON 17809 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for 4UCON 17809 series connectors using cadquery'

___ver___ = "0.3 18/06/2020"


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
from conn_4ucon_17809_params import *

from ribbon import Ribbon


def generate_straight_pin(params, pin_1_side):
    foot_height = seriesParams.foot_height
    pin_width=seriesParams.pin_width
    pin_depth=seriesParams.pin_depth
    pin_height=seriesParams.pin_height
    pin_inside_distance=seriesParams.pin_inside_distance
    pin_thickness = seriesParams.pin_thickness
    chamfer_long = seriesParams.pin_chamfer_long
    chamfer_short = seriesParams.pin_chamfer_short
    sign = 1 if pin_1_side else -1
    pin=cq.Workplane("YZ").workplane(offset=-pin_width/2.0)\
        .moveTo(0, foot_height)\
        .line(sign*pin_thickness/2,0)\
        .line(sign*1.27,-foot_height)\
        .line(0, -2.54)\
        .line(sign*-pin_thickness,0)\
        .line(0, 2.54)\
        .line(sign*-1.27, foot_height)\
        .line(0,1)\
        .close()\
        .extrude(pin_width).edges("|X").fillet(0.07)
    return pin


def generate_2_pin_group(params, pin_1_side):
    pin_pitch=params.pin_pitch
    pin_y_pitch=params.pin_y_pitch
    num_pins=params.num_pins
    pin_a = generate_straight_pin(params, pin_1_side).translate((0, -pin_y_pitch/2, 0))
    pin_b = pin_a.translate((0, -2 * pin_y_pitch, 0))
    pin_group = pin_a.union(pin_b)
    return pin_group


def generate_pins(params):
    pin_pitch=params.pin_pitch
    num_pins=params.num_pins
    pins = generate_2_pin_group(params, pin_1_side=True)
    for i in range(1, num_pins // 2):
        pins = pins.union(generate_2_pin_group(params, i % 2 == 0).translate((i*pin_pitch,0,0)))
    return pins


def generate_2_contact_group(params):
    pin_y_pitch=params.pin_y_pitch
    foot_height = seriesParams.foot_height
    pin_thickness = seriesParams.pin_thickness
    pin_width=seriesParams.pin_width
    y_offset = -(2*pin_y_pitch)
    c_list = [
        ('start', {'position': (pin_y_pitch, foot_height), 'direction': 90.0, 'width':pin_thickness}),
        ('line', {'length': 4.5}),
        ('arc', {'radius': 0.2, 'angle': 35.0}),
        ('line', {'length': 3}),
        ('arc', {'radius': 2.0, 'angle': -70.0}),
        ('line', {'length': 2}),
        ('arc', {'radius': 0.2, 'angle': 35.0}),
        ('line', {'length': 2.8}),
    ]
    ribbon = Ribbon(cq.Workplane("YZ").workplane(offset=-pin_width/2.0), c_list)
    contact1 = ribbon.drawRibbon().extrude(pin_width)
    contact2 = contact1.mirror("XZ")
    contact1 = contact1.union(contact2).translate((0,-3*pin_y_pitch/2.0,0))
    return contact1


def generate_contacts(params):
    num_pins=params.num_pins
    pin_pitch=params.pin_pitch
    pair = generate_2_contact_group(params)
    contacts = pair
    for i in range(0, num_pins // 2):
        contacts = contacts.union(pair.translate((i*pin_pitch,0,0)))
    return contacts


def generate_body(params, calc_dim):
    pin_inside_distance = seriesParams.pin_inside_distance
    pin_width = seriesParams.pin_width
    num_pins = params.num_pins
    pin_pitch = params.pin_pitch
    pin_y_pitch=params.pin_y_pitch

    body_length = calc_dim.length
    body_width = seriesParams.body_width
    body_height = seriesParams.body_height
    body_fillet_radius = seriesParams.body_fillet_radius

    marker_x_inside = seriesParams.marker_x_inside
    marker_y_inside = seriesParams.marker_y_inside
    marker_size = seriesParams.marker_size
    marker_depth = seriesParams.marker_depth

    foot_height = seriesParams.foot_height
    foot_width = seriesParams.foot_width
    foot_length = seriesParams.foot_length
    foot_inside_distance = seriesParams.foot_inside_distance

    slot_length = calc_dim.slot_length
    slot_outside_pin = seriesParams.slot_outside_pin
    slot_width = seriesParams.slot_width
    slot_depth = seriesParams.slot_depth
    slot_chamfer = seriesParams.slot_chamfer

    hole_width = seriesParams.hole_width
    hole_length = seriesParams.hole_length
    hole_offset = seriesParams.hole_offset
    hole_depth = seriesParams.hole_depth

    top_void_depth = seriesParams.top_void_depth
    top_void_width = seriesParams.top_void_width
    bottom_void_width = calc_dim.bottom_void_width

    recess_depth = seriesParams.recess_depth
    recess_large_width = seriesParams.recess_large_width
    recess_small_width = seriesParams.recess_small_width
    recess_height = seriesParams.recess_height

    x_offset = (((num_pins // 2) - 1)*pin_pitch)/2.0
    y_offset = -(1.5*pin_y_pitch)

    # body
    body = cq.Workplane("XY").workplane(offset=foot_height).moveTo(x_offset, y_offset)\
        .rect(body_length, body_width).extrude(body_height)\
        .edges("|Z").fillet(body_fillet_radius).edges(">Z").fillet(body_fillet_radius)

    # pin 1 marker
    body = body.faces(">Z").workplane().moveTo(-(body_length/2)+marker_x_inside, (body_width/2)-marker_y_inside)\
        .line(-marker_size,-marker_size/2).line(0, marker_size).close().cutBlind(-marker_depth)

    # foot
    foot = cq.Workplane("YZ").workplane(offset=(body_length/2)-foot_inside_distance)\
        .moveTo(y_offset - foot_length/2, 0)\
        .line(foot_length*0.2,0)\
        .line(0,foot_height/2)\
        .line(foot_length*0.6,0)\
        .line(0,-foot_height/2)\
        .line(foot_length*0.2,0)\
        .line(0,foot_height)\
        .line(-foot_length,0)\
        .close()\
        .extrude(-foot_width)

    foot_mirror = foot.mirror("YZ")

    foot = foot.union(foot_mirror).translate((x_offset, 0, 0))

    body = body.union(foot)

    # slot
    body = body.faces(">Z").workplane().rect(slot_length, slot_width).cutBlind(-slot_depth)

    chamfer = cq.Workplane("XY").workplane(offset=foot_height+body_height).moveTo(x_offset, y_offset) \
    .rect(slot_length+2*slot_chamfer, slot_width+2*slot_chamfer) \
    .workplane(offset=-slot_chamfer).rect(slot_length, slot_width) \
    .loft(combine=True)

    body = body.cut(chamfer)

    # contact holes
    body = body.faces(">Z").workplane().center(0, hole_offset)\
        .rarray(pin_pitch, 1, (num_pins//2), 1).rect(hole_width, hole_length)\
        .center(0, -2*hole_offset)\
        .rarray(pin_pitch, 1, (num_pins//2), 1).rect(hole_width, hole_length)\
        .cutBlind(-2)

    # internal void
    body = body.faces(">Z").workplane(offset=-hole_depth)\
        .rarray(pin_pitch, 1, (num_pins//2), 1).rect(hole_width, top_void_width)\
        .cutBlind(-(top_void_depth-hole_depth))

    body = body.faces(">Z").workplane(offset=-top_void_depth)\
        .rarray(pin_pitch, 1, (num_pins//2), 1).rect(hole_width, bottom_void_width)\
        .cutBlind(-(body_height-top_void_depth))

    # body end recesses
    body = body.faces(">Z").workplane().center(body_length/2.0-recess_depth/2.0, 0)\
        .rect(recess_depth, recess_small_width).cutBlind(-recess_height)

    recess = cq.Workplane("XY").workplane(offset=foot_height+body_height).center(x_offset-body_length/2.0+recess_depth/2.0, y_offset)\
        .rect(recess_depth, recess_large_width).extrude(-recess_height).edges(">X").edges("|Z").fillet(0.3)

    body = body.cut(recess)

    return body


def generate_part(part_key):
    params = all_params[part_key]
    calc_dim = dimensions(params)
    pins = generate_pins(params)
    body = generate_body(params, calc_dim)
    contacts = generate_contacts(params)
    return (pins, body, contacts)


# opened from within freecad
if "module" in __name__:
    part_to_build = 'ucon_17809_02x10_1.27mm'

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 part_to_build + "\n")
    (pins, body, contacts) = generate_part(part_to_build)

    show(pins)
    show(body)
    show(contacts)



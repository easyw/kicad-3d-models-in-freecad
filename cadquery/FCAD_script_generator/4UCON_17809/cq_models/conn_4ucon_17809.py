# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning JST XH Connectors

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

__title__ = "model description for 4UCON 17809 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for 4UCON 17809 series connectors using cadquery'

___ver___ = "0.1 13/04/2017"


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
# from cq_helpers import *
from conn_4ucon_17809_params import *


def generate_straight_pin(params):
    pin_width=seriesParams.pin_width
    pin_depth=seriesParams.pin_depth
    pin_height=seriesParams.pin_height
    pin_inside_distance=seriesParams.pin_inside_distance
    chamfer_long = seriesParams.pin_chamfer_long
    chamfer_short = seriesParams.pin_chamfer_short

    pin=cq.Workplane("YZ").workplane(offset=-pin_width/2.0)\
        .moveTo(-pin_width/2.0, -pin_depth)\
        .rect(pin_width, pin_height, False)\
        .extrude(pin_width)

    pin = pin.faces(">Z").edges(">X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces(">Z").edges("<X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces(">Z").edges(">Y").chamfer(chamfer_long,chamfer_short)
    pin = pin.faces(">Z").edges("<Y").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges(">X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges("<X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges(">Y").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges("<Y").chamfer(chamfer_short,chamfer_long)
    return pin

def generate_4_pin_group(params):
    pin_pitch=params.pin_pitch
    pin_y_pitch=params.pin_y_pitch
    num_pins=params.num_pins
    pin0 = generate_straight_pin(params)
    pin1 = pin0.translate(( 0, -pin_y_pitch, 0))
    pin2 = pin0.translate(( pin_pitch, -pin_y_pitch/2, 0))
    pin3 = pin0.translate(( pin_pitch, -3 * pin_y_pitch/2, 0))
    pin_group = pin0.union(pin1.union(pin2.union(pin3)))
    return pin_group

"""
    pin1 = pin0
    pin2 = pin0.translate(( pin_pitch,         -pin_y_pitch / 2,     0)))
    pin3 = pin0.translate(( pin_pitch,         -pin_y_pitch / 2,     0)))
"""

def generate_pins(params):
    pin_pitch=params.pin_pitch
    num_pins=params.num_pins
    pins = generate_4_pin_group(params)
    return pins

"""
    for i in range(0, num_pins / 4):
        pins = pins.union(pin.translate(((i * pin_pitch) / 2, 0, 0)))
"""


def generate_body(params ,calc_dim, with_details=False):
    pin_inside_distance = seriesParams.pin_inside_distance
    pin_width = seriesParams.pin_width
    num_pins = params.num_pins
    pin_pitch = params.pin_pitch
    pin_y_pitch=params.pin_y_pitch

    body_length = calc_dim.length
    body_width = seriesParams.body_width
    body_height = seriesParams.body_height
    body_fillet_radius = seriesParams.body_fillet_radius

    foot_height = seriesParams.foot_height
    foot_width = seriesParams.foot_width
    foot_length = seriesParams.foot_length
    foot_inside_distance = seriesParams.foot_inside_distance

    body_channel_depth = seriesParams.body_channel_depth
    body_channel_width = seriesParams.body_channel_width
    body_cutout_length = seriesParams.body_cutout_length
    body_cutout_width = seriesParams.body_cutout_width

    ramp_chamfer_x = seriesParams.ramp_chamfer_x
    ramp_chamfer_y = seriesParams.ramp_chamfer_y
    ramp_height = calc_dim.ramp_height
    ramp_width = calc_dim.ramp_width 
    ramp_offset = calc_dim.ramp_offset

    x_offset = (((num_pins / 2) - 1)*pin_pitch)/2.0
    y_offset = -(3*pin_y_pitch/4)

    body = cq.Workplane("XY").workplane(offset=foot_height).moveTo(x_offset, y_offset)\
        .rect(body_length, body_width).extrude(body_height)\
        .edges("|Z").fillet(body_fillet_radius).edges(">Z").fillet(body_fillet_radius)

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

    return body, None

"""
    body = body.faces("<Z").workplane().rarray(pin_pitch, 1, num_pins, 1)\
        .rect(body_channel_width, body_width).cutBlind(-body_channel_depth)

    body = body.faces(">Z").workplane().moveTo(((num_pins-1)*pin_pitch)/2.0, 0).rarray(pin_pitch, 1, num_pins-1, 1)\
        .rect(body_cutout_width, body_cutout_length).cutThruAll(False)

    ramp = cq.Workplane("YZ").workplane(offset=ramp_offset).moveTo(-body_width/2.0, body_height)\
        .line(0,ramp_height)\
        .line(1.0,0)\
        .line(0,-3.8)\
        .line(0.5,-0.9)\
        .line(0,-1.0)\
        .line(-0.5,-0.5)\
        .line(0,-1.7)\
        .threePointArc((-body_width/2.0 + 1 + (0.6 * (1-0.707)), body_height + (1 - 0.707)* 0.6), (-body_width/2.0 + 1 + 0.6, body_height))\
        .close().extrude(ramp_width).faces(">X").edges(">Z").chamfer(ramp_chamfer_x, ramp_chamfer_y)

    ramp_mirror = ramp.mirror("YZ")

    ramp = ramp.union(ramp_mirror).translate(((num_pins - 1) * pin_pitch / 2.0, 0, 0))
    
    body = body.union(ramp)
 """


def generate_part(part_key, with_plug=False):
    params = all_params[part_key]
    calc_dim = dimensions(params)
    pins = generate_pins(params)
    body, insert = generate_body(params, calc_dim, not with_plug)
    return (pins, body)


# opened from within freecad
if "module" in __name__:
    part_to_build = '17809_02x40_1.27mm'

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 part_to_build + "\n")
    (pins, body) = generate_part(part_to_build, True)

    show(pins)
    show(body)


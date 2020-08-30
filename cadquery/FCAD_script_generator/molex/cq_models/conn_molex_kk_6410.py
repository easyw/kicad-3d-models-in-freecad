# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning Molex KK 6410 Connectors

## requirements
## freecad (v1.5 and v1.6 have been tested)
## cadquery FreeCAD plugin (v0.3.0 and v0.2.0 have been tested)
##   https://github.com/jmwright/cadquery-freecad-module

## This script can be run from within the cadquery module of freecad.
## To generate VRML/ STEP files for, use launch-cq-molex
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

__title__ = "model description for Molex KK 6410 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for Molex KK 6410 series connectors using cadquery'

___ver___ = "0.3 04/12/2017"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Ray Benitez"
    STR_licEmail = "hackscribble@outlook.com"
    STR_licOrgSys = ""
    STR_licPreProc = ""

    LIST_license = ["",]
    ############################################################################


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD

class series_params():
    series = "KK-254"
    manufacturer = 'Molex'
    mpn_format_string = 'AE-6410-{pincount:02d}A'
    orientation = 'V'
    datasheet = 'http://www.molex.com/pdm_docs/sd/022272021_sd.pdf'
    pinrange = range(2, 17)
    mount_pin = ''

    number_of_rows = 1

    body_color_key = "white body"
    pins_color_key = "metal grey pins"
    color_keys = [
        body_color_key,
        pins_color_key
    ]
    obj_suffixes = [
        '__body',
        '__pins'
    ]

    pitch = 2.54

    pin_width = 0.64
    pin_chamfer_long = 0.25
    pin_chamfer_short = 0.25
    pin_height = 14.22				# DIMENSION C
    pin_depth = 3.56				# DIMENSION F depth below bottom surface of base
    pin_inside_distance = 1.27			# Distance between centre of end pin and end of body

    body_width = 5.8
    body_height = 3.17
    body_channel_depth = 0.6
    body_channel_width = 1.5
    body_cutout_length = 1.2
    body_cutout_width = 0.6

    ramp_split_breakpoint = 6			# Above this number of pins, the tab is split into two parts
    ramp_chamfer_x = 0.3
    ramp_chamfer_y = 0.7


calcDim = namedtuple( 'calcDim', ['length', 'ramp_height', 'ramp_width', 'ramp_offset'])


def dimensions(num_pins):
    length = (num_pins-1) * series_params.pitch + 2 * series_params.pin_inside_distance
    ramp_height = 11.7 - series_params.body_height
    if num_pins > series_params.ramp_split_breakpoint:
        ramp_width = series_params.pitch * 2
        ramp_offset = series_params.pitch * (num_pins -5) / 2
    else:
        ramp_width = (num_pins - 1) * series_params.pitch / 2
        ramp_offset = 0
    return calcDim(length = length, ramp_height = ramp_height, ramp_width = ramp_width, ramp_offset = ramp_offset)

def generate_straight_pin():
    pin_width=series_params.pin_width
    pin_depth=series_params.pin_depth
    pin_height=series_params.pin_height
    pin_inside_distance=series_params.pin_inside_distance
    chamfer_long = series_params.pin_chamfer_long
    chamfer_short = series_params.pin_chamfer_short

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


def generate_pins(num_pins):
    pitch=series_params.pitch
    pin=generate_straight_pin()
    pins = pin
    for i in range(0, num_pins):
        pins = pins.union(pin.translate((i * pitch, 0, 0)))
    return pins


def generate_body(num_pins ,calc_dim):
    pin_inside_distance = series_params.pin_inside_distance
    pin_width = series_params.pin_width
    pitch = series_params.pitch

    body_len = calc_dim.length
    body_width = series_params.body_width
    body_height = series_params.body_height

    body_channel_depth = series_params.body_channel_depth
    body_channel_width = series_params.body_channel_width
    body_cutout_length = series_params.body_cutout_length
    body_cutout_width = series_params.body_cutout_width

    # ramp_split_breakpoint = series_params.ramp_split_breakpoint
    ramp_chamfer_x = series_params.ramp_chamfer_x
    ramp_chamfer_y = series_params.ramp_chamfer_y
    ramp_height = calc_dim.ramp_height
    ramp_width = calc_dim.ramp_width
    ramp_offset = calc_dim.ramp_offset

    body = cq.Workplane("XY").moveTo(((num_pins-1)*pitch)/2.0, 0).rect(body_len, body_width).extrude(body_height)#.edges("|Z").fillet(0.05)

    body = body.faces("<Z").workplane().rarray(pitch, 1, num_pins, 1)\
        .rect(body_channel_width, body_width).cutBlind(-body_channel_depth)

    body = body.faces(">Z").workplane().moveTo(((num_pins-1)*pitch)/2.0, 0).rarray(pitch, 1, num_pins-1, 1)\
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

    ramp = ramp.union(ramp_mirror).translate(((num_pins - 1) * pitch / 2.0, 0, 0))

    body = body.union(ramp)

    return body, None


def generate_part(num_pins):
    calc_dim = dimensions(num_pins)
    pins = generate_pins(num_pins)
    body, insert = generate_body(num_pins, calc_dim)
    return (body, pins)


# opened from within freecad
if "module" in __name__:
    part_to_build = 16

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 str(part_to_build) + "pin variant\n")
    (body, pins) = generate_part(part_to_build)

    show(pins)
    show(body)

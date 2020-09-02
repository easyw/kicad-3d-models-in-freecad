# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning Molex KK 41791 Connectors

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

__title__ = "model description for Molex KK-396 41791 series connectors"
__author__ = "Franck78"
__Comment__ = 'model description for Molex KK-396 41791 series connectors using cadquery'

___ver___ = "1.0 08/30/2020"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Franck Bourdonnec"
    STR_licEmail = "fbourdonnec@chez.com"
    STR_licOrgSys = ""
    STR_licPreProc = ""

    LIST_license = ["",]
    ############################################################################


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD

class series_params():
    series = "KK-396"
    manufacturer = 'Molex'
    #mpn_format_string = '26604{pincount:02d}0'
    mpn_format_string = 'A-41791-{pincount:04d}'# old pn-name
    orientation = 'V'
    datasheet = 'https://www.molex.com/pdm_docs/sd/009652028_sd.pdf'
    pinrange = range(2,19)
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

    pitch = 3.96

    pin_width = 1.14
    pin_chamfer_long = 0.3
    pin_chamfer_short = 0.1
    pin_height = 18.29                          # The standart pin, other length available
    pin_depth = 3.6                             # Depth below bottom surface of base
    pin_inside_distance = (7.77-3.96)/2         # Distance between centre of end pin and end of body (A-B)/2
    pin_xpos = 5.11                             # Pin and groove not exactly body centered


    body_width = 6.88                           # The base
    body_height = 3.3
    body_channel_depth = 0.76
    body_channel_width = 5.35

    full_width = 10.01                          # base+ramp
    ramp_height = 11.33                         # Full height
    ramp_notches_pos = (
        [],         # 0 number of pin
        [],         # 1
        [],         # 2
        [],         # 3
        [],         # 4
        [],         # 5
        [],         # 6
        [4],        # 7
        [4],        # 8
        [5],        # 9
        [5],        # 10
        [6],        # 11
        [4,8],      # 12
        [4,9],      # 13
        [5,9],      # 14
        [5,10],     # 15
        [5,11],     # 16
        [6,11],     # 17
        [6,12]      # 18
    )
    # all other mesures from Molex drawing

calcDim = namedtuple( 'calcDim', ['length'])


def dimensions(num_pins):
    length = (num_pins-1) * series_params.pitch + 2 * series_params.pin_inside_distance
    return calcDim(length = length)

def generate_straight_pin():
    pin_width=series_params.pin_width
    pin_depth=series_params.pin_depth
    pin_height=series_params.pin_height
    pin_xpos=series_params.pin_xpos
    chamfer_long = series_params.pin_chamfer_long
    chamfer_short = series_params.pin_chamfer_short

    pin=cq.Workplane("YZ").workplane(offset=series_params.pin_inside_distance - pin_width/2)\
        .moveTo(pin_xpos-pin_width/2.0, -pin_depth)\
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

    body_len = calc_dim.length
    full_width = series_params.full_width
    body_width = series_params.body_width
    body_height = series_params.body_height

    body_channel_depth = series_params.body_channel_depth
    body_channel_width = series_params.body_channel_width
    body_channel_xpos = series_params.pin_xpos

    ramp_height = series_params.ramp_height
    pitch = series_params.pitch

    # Point's coordinates are mesured on the drawing model from Molex
    # 0,0 is bottom left of the _| shape (side view)
    #body = cq.Workplane("YZ")\
    #    .moveTo(0, 0)\
    #    .vLine(1.28)\
    #    .hLine(0.52)\
    #    .vLine(1.53)\
    #    .threePointArc((0.27, 1.92), (0.19, 2.42) )\
    #    .lineTo(0, 2.42)\
    #    .lineTo(0, body_height)\
    #    .hLine(body_width)\
    #    .lineTo(8.01, 2.17)                               /*first big curve beginning*/\
    #    .threePointArc((8.78, 2.0), (9.24, 2.68))\
    #    .lineTo(9.24, 4.98)\
    #    .threePointArc((9.11, 5.64), (8.70, 6.28))\
    #    .lineTo(8.03, 6.94)\
    #    .threePointArc((7.52, 8.06), (7.81, 9.18))\
    #    .lineTo(9.24, ramp_height)\
    #    .lineTo(full_width, ramp_height)                  /* top right corner */\
    #    .lineTo(full_width, 1.91)\
    #    .threePointArc((9.45, 0.58),(8.01,0))             /*bottom right arc*/\
    #    .lineTo(body_channel_xpos+body_channel_width/2,0)\
    #    .vLine(body_channel_depth)\
    #    .hLine(-body_channel_width)\
    #    .vLine(-body_channel_depth)\
    #    .close()\
    #    .extrude(body_len)


    body = cq.Workplane("YZ")\
        .moveTo(0, 0)\
        .vLine(1.28)\
        .hLine(0.52)\
        .lineTo(0.52, 1.53)\
        .threePointArc((0.27, 1.92), (0.19, 2.42) )\
        .lineTo(0, 2.42)\
        .lineTo(0, body_height)\
        .hLine(body_width)\
        .lineTo(8.01, 2.17)\
        .threePointArc((8.78, 2.0), (9.24, 2.68))\
        .lineTo(9.24, 4.98)\
        .threePointArc((9.11, 5.64),(8.70, 6.28))\
        .lineTo(8.03, 6.94)\
        .threePointArc((7.52, 8.06), (7.81, 9.18))\
        .lineTo(9.24, ramp_height)\
        .lineTo(full_width, ramp_height)\
        .lineTo(full_width, 1.91)\
        .threePointArc((9.45, 0.58), (8.01, 0))\
        .lineTo(body_width, 0)\
        .vLine(body_channel_depth)\
        .hLine(-body_channel_width)\
        .vLine(-body_channel_depth)\
        .close()\
        .extrude(body_len)

    # Cuts under the base
    cuts_width = 2/3*pitch         #good approx for th width
    body = body.faces("<Z").workplane(offset=1).rarray(pitch, 1, num_pins, 1)\
        .rect(cuts_width, full_width).cutBlind(-body_channel_depth-1)

    # Cut the ramp full height
    plane = body.faces(">Y").workplane()
    cuts_width = 1/3*pitch * 1.2   # *1.2 ensures a little larger than space between cuts under the base
    for np in series_params.ramp_notches_pos[num_pins]:
        body = plane.moveTo(body_len/2 - np*pitch, 0 ).rect(cuts_width, body_height+ramp_height).cutBlind(-(full_width-body_width))

    body = plane.moveTo(+body_len/2, 0).rect(2.5*cuts_width, body_height+ramp_height).cutBlind(-(full_width-body_width))
    body = plane.moveTo(-body_len/2, 0).rect(2.5*cuts_width, body_height+ramp_height).cutBlind(-(full_width-body_width))

    # Carve a '1' near pin 1
    yrel = -3                 # x,y offset just for treePointArc. I would like to build the sketch, move it, carve it.
    xrel = body_len/2 - pin_inside_distance - pin_width/2
    plane = body.faces("Z").workplane()\
         .moveTo(xrel+0.9, yrel)\
         .hLine(0.4)\
         .vLine(3.35)\
         .hLine(-0.4)\
         .threePointArc((xrel+0.65, yrel+2.81), (xrel, yrel+2.5))\
         .vLine(-0.4)\
         .hLine(0.9)\
         .close()\
         .cutBlind(-0.7)


    return body, None


def generate_part(num_pins):
    calc_dim = dimensions(num_pins)
    pins = generate_pins(num_pins)
    body, insert = generate_body(num_pins, calc_dim)

    # adjust for matching KiCad expectation
    body = body.rotate((0, 0, 0),(0, 0, 1), 180).translate(cq.Vector(calc_dim.length-series_params.pin_inside_distance,series_params.pin_xpos,0))
    pins = pins.rotate((0, 0, 0),(0, 0, 1), 180).translate(cq.Vector(calc_dim.length-series_params.pin_inside_distance,series_params.pin_xpos,0))

    return (body, pins)


# opened from within freecad
if "module" in __name__:
    part_to_build = 16

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 str(part_to_build) + "pin variant\n")
    (body, pins) = generate_part(part_to_build)

    show(pins)
    show(body)

# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning Molex KK 5273 Connectors

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

__title__ = "model description for Molex KK 5273 (SPOX) series connectors"
__author__ = "Franck78"
__Comment__ = 'model description for Molex KK 5273 (SPOX) series connectors using cadquery'

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
    #mpn_format_string = '09652{pincount:02d}8'
    mpn_format_string = '5273-{pincount:02d}A'# KiCad have this footprints (ranging 2..18). Use this for testing
    orientation = 'V'
    datasheet = 'https://www.molex.com/pdm_docs/sd/009652028_sd.pdf'
    pinrange = range(2, 13)			# Molex now sells only 2..8 channels
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
    pin_height = 17.45
    pin_depth = 3.6				# Depth below bottom surface of base
    pin_inside_distance = (7.16-3.96)/2		# Distance between centre of end pin and end of body
    pin_xpos = 5.6                              # Pin and groove not exactly body centered

    body_width = 10.2
    body_height = 3.2
    body_channel_depth = 1/2 * pin_width
    body_channel_width = 1.8
    body_channel_chamfer = 0.7


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
    body_width = series_params.body_width
    body_height = series_params.body_height

    body_channel_depth = series_params.body_channel_depth
    body_channel_width = series_params.body_channel_width
    body_channel_xpos = series_params.pin_xpos
    body_channel_chamfer = series_params.body_channel_chamfer

    # Point's coordinates are mesured on the drawing model from Molex
    # 0,0 is bottom left of the _| shape (side view)
    body = cq.Workplane("YZ")\
        .moveTo(0, 0)\
        .vLine(body_height)\
        .hLine(6.8)\
        .lineTo(7.4, 2.3)\
        .threePointArc((8.5, 2.0), (9.2, 2.9))\
        .lineTo(9.2, 4.9)\
        .threePointArc((9.16, 5.2), (9.02, 5.49))\
        .lineTo(7.62, 7.5)\
        .threePointArc((7.26, 8.64), (7.85, 10.06))\
        .lineTo(10.06, 12.26)\
        .lineTo(10.75, 11.56)\
        .lineTo(8.56, 9.35)\
        .threePointArc((8.26, 8.64), (8.45, 8.06))\
        .lineTo(9.84, 6.08)\
        .threePointArc((10.12, 5.51), (body_width, 4.9))\
        .lineTo(body_width, 2.0)\
        .threePointArc((9.68, 0.63), (8.2, 0.0))\
        .lineTo(body_channel_xpos+body_channel_width/2+body_channel_chamfer, 0)\
        .line(-body_channel_chamfer, body_channel_depth)\
        .hLine(-body_channel_width)\
        .line(-body_channel_chamfer, -body_channel_depth)\
        .close()\
        .extrude(body_len)

    # carve a small notch on the right side
    notche_width=series_params.pitch-pin_width
    body = body.faces("<Y").workplane().moveTo(body_len/2-series_params.pitch/2-pin_inside_distance , 0).rect(notche_width,body_height).cutBlind(-0.3)

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

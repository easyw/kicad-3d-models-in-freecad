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

__title__ = "model description for Molex Picoflex 90325 series connectors"
__author__ = "hackscribble"
__Comment__ = 'model description for Picoflex 90325 series connectors using cadquery'

___ver___ = "0.1 2017-08-09"


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
from conn_molex_90325_params import *


def generate_straight_pin(params, num):
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

    pin = pin.faces("<Z").edges(">X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges("<X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges(">Y").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges("<Y").chamfer(chamfer_short,chamfer_long)

    if num == 0:
        pinTop=cq.Workplane("YZ").workplane(offset=-pin_width/2.0)\
            .moveTo(-2.54, 0)\
            .rect(2.54, 3.4, False)\
            .extrude(pin_width)
    else:
        pinTop=cq.Workplane("YZ").workplane(offset=-pin_width/2.0)\
            .moveTo(0, 0)\
            .rect(2.54, 3.4, False)\
            .extrude(pin_width)

    pinTop = pinTop.faces(">Z").edges(">X").chamfer(chamfer_short,  2*chamfer_long)
    pinTop = pinTop.faces(">Z").edges("<X").chamfer(chamfer_short,  2*chamfer_long)
    pinTop = pinTop.faces(">Z").edges(">Y").chamfer(2*chamfer_long,   chamfer_short)
    pinTop = pinTop.faces(">Z").edges("<Y").chamfer(chamfer_short,  2*chamfer_long)

    pin = pin.union(pinTop)


    return pin


def generate_pins(params):
    pin_pitch=params.pin_pitch
    num_pins=params.num_pins
    pinL=generate_straight_pin(params, 0)
    pinH=generate_straight_pin(params, 1)
    pins = pinL

    for i in range(0, num_pins):
        if (i % 2) == 0:
            pins = pins.union(pinL.translate((i * pin_pitch, 0, 0)))
        else:
            pins = pins.union(pinH.translate((i * pin_pitch, -2.54, 0)))
    return pins


def generate_body(params ,calc_dim, with_details=False):
    pin_inside_distance = seriesParams.pin_inside_distance
    pin_width = seriesParams.pin_width
    num_pins = params.num_pins
    pin_pitch = params.pin_pitch

    #
    # Main body block
    #
    body_block_x = -3.77
    body_block_y = 0
    body_block_width = 5.0
    body_block_height = 1.5
    body_block_lenght = ((params.num_pins - 1) * params.pin_pitch) + 5.05
	
    body_block=cq.Workplane("YZ").workplane(offset=-2.525)\
        .moveTo(body_block_x, body_block_y)\
        .rect(body_block_width, body_block_height, False)\
        .extrude(body_block_lenght)

#    body_block = body_block.faces(">X").edges(">Y").chamfer(seriesParams.pin_chamfer_short / 2.0,seriesParams.pin_chamfer_short / 2.0)
    body_block = body_block.faces(">X").edges("<Y").chamfer(seriesParams.pin_chamfer_short / 2.0,seriesParams.pin_chamfer_short / 2.0)
    body_block = body_block.faces("<X").edges("<Y").chamfer(seriesParams.pin_chamfer_short / 2.0,seriesParams.pin_chamfer_short / 2.0)
#    body_block = body_block.faces("<X").edges(">Y").chamfer(seriesParams.pin_chamfer_short / 2.0,seriesParams.pin_chamfer_short / 2.0)

    #
    # Remove the cutout in main block
    #
    body_offset = -1.525
    for i in range(0, num_pins):
        body_width = 0.5
        body_height = body_block_height / 3.0
        body_lenght = 1.0
	
        if (body_offset + 3.0) < body_block_lenght:

            body = cq.Workplane("YZ").workplane(offset=body_offset)\
                .moveTo(0.75, 0.0)\
                .rect(body_width, body_height, False)\
                .extrude(body_lenght)
 
            body_block = body_block.cut(body)

            body = cq.Workplane("YZ").workplane(offset=body_offset)\
                .moveTo(0.75, 1.0)\
                .rect(body_width, body_height, False)\
                .extrude(body_lenght)
 
            body_block = body_block.cut(body)

            body = cq.Workplane("YZ").workplane(offset=body_offset)\
                .moveTo(-3.8, 0.0)\
                .rect(body_width, body_height, False)\
                .extrude(body_lenght)
 
            body_block = body_block.cut(body)

            body = cq.Workplane("YZ").workplane(offset=body_offset)\
                .moveTo(-3.8, 1.0)\
                .rect(body_width, body_height, False)\
                .extrude(body_lenght)
 
            body_block = body_block.cut(body)

            body_offset = body_offset + (2 * body_lenght)



    #
    # Add larger top pig
    #
    body_x = -2.77
    body_y = 0.0
    body_width = 3.0
    body_height = seriesParams.pig_height
    body_lenght = 1.0
	
    body = cq.Workplane("YZ").workplane(offset=-2.525 + body_block_lenght - 1.0)\
        .moveTo(body_x, body_y)\
        .rect(body_width, body_height, False)\
        .extrude(body_lenght)

    body = body.faces(">Z").edges(">Y").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
    body = body.faces(">Z").edges("<Y").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
    body = body.faces(">Z").edges("<X").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
 
    body_block = body_block.union(body)

    #
    # Add smaller top pig
    #	
    body_x = -0.77
    body_y = 0.0
    body_width = 2.0
    body_height = seriesParams.pig_height
    body_lenght = 1.0
	
    body = cq.Workplane("YZ").workplane(offset=-2.525)\
        .moveTo(body_x, body_y)\
        .rect(body_width, body_height, False)\
        .extrude(body_lenght)

    body = body.faces(">Z").edges(">Y").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
    body = body.faces(">Z").edges("<Y").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
    body = body.faces(">Z").edges(">X").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
    body = body.faces("<X").edges(">Y").chamfer(seriesParams.pin_chamfer_short / 2.0,seriesParams.pin_chamfer_short / 2.0)
 
    body_block = body_block.union(body)
		
    #
    # Add bottom pig at smaller top pig
    #	
    body_x = -1.8
    body_y = 1.48
    body_height = seriesParams.pig_depth + 0.3

    body = cq.Workplane("XY").workplane(offset=0.3)\
        .moveTo(body_x, body_y)\
        .circle(0.75).extrude(-body_height,False)
 
    body = body.faces("<Z").edges(">X").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
    body_block = body_block.union(body)
 
		
    #
    # Add bottom pig at larger top pig
    #	
    body_x = ((params.num_pins - 1) * params.pin_pitch) + 1.8
    body_y = 1.48
    body_height = seriesParams.pig_depth + 0.3
	
    body = cq.Workplane("XY").workplane(offset=0.3)\
        .moveTo(body_x, body_y)\
        .circle(0.75).extrude(-body_height,False)
 
    body = body.faces("<Z").edges(">X").chamfer(seriesParams.pin_chamfer_short,seriesParams.pin_chamfer_short)
    body_block = body_block.union(body)

    return body_block, None


def generate_part(part_key, with_plug=False):
    params = all_params[part_key]
    calc_dim = dimensions(params)
    pins = generate_pins(params)
    body, insert = generate_body(params, calc_dim, not with_plug)
    return (pins, body)


# opened from within freecad
if "module" in __name__:
    part_to_build = "Molex_Picoflex_90325_04"

    FreeCAD.Console.PrintMessage("Started from CadQuery: building " +
                                 part_to_build + "\n")
    (pins, body) = generate_part(part_to_build, True)

    show(pins)
    show(body)


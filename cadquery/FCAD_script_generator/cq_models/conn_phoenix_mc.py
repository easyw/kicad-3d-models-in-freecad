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

__title__ = "model description for Phoenix Series MSTB Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for Phoenix Series MSTB Connectors using cadquery'

___ver___ = "1.0 20/07/2016"

import sys
import os
from conn_phoenix_global_params import *
from conn_phoenix_mc_params import *

import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
from cq_helpers import *

def generate_straight_pin(params):
    pin_width=seriesParams.pin_width
    pin_depth=seriesParams.pin_depth
    body_height=seriesParams.body_height
    pin_inside_distance=seriesParams.pin_inside_distance
    chamfer_long = seriesParams.pin_chamfer_long
    chamfer_short = seriesParams.pin_chamfer_short


    pin=cq.Workplane("YZ").workplane(offset=-pin_width/2.0)\
        .moveTo(-pin_width/2.0, -pin_depth)\
        .rect(pin_width, pin_depth+body_height-pin_inside_distance, False)\
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

def generate_angled_pin(params):
    pin_width=seriesParams.pin_width
    pin_depth=seriesParams.pin_depth
    body_height=seriesParams.body_height
    pin_inside_distance=seriesParams.pin_inside_distance
    chamfer_long = seriesParams.pin_chamfer_long
    chamfer_short = seriesParams.pin_chamfer_short
    pin_from_bottom = seriesParams.pin_from_front_bottom
    pin_bend_radius = seriesParams.pin_bend_radius
    pin_angled_from_back = seriesParams.pin_angled_from_back


    outher_r=pin_width+pin_bend_radius

    pin_points=[(pin_width/2.0, -pin_depth)]
    add_p_to_chain(pin_points, (-pin_width,0))
    add_p_to_chain(pin_points, (0,pin_depth+pin_from_bottom-pin_width/2.0-pin_bend_radius))
    add_p_to_chain(pin_points, (-pin_bend_radius, pin_bend_radius))
    pa1=get_third_arc_point1(pin_points[2], pin_points[3])
    pin_points.append((-(body_height-pin_inside_distance-pin_angled_from_back), pin_points[3][1]))
    add_p_to_chain(pin_points, (0, pin_width))
    pin_points.append((-pin_width/2.0-pin_bend_radius,pin_points[5][1]))
    add_p_to_chain(pin_points, (outher_r,-outher_r))
    pa2=get_third_arc_point2(pin_points[6], pin_points[7])

    pin=cq.Workplane("YZ").workplane(offset=-pin_width/2.0)\
        .moveTo(*pin_points[0])\
        .lineTo(*pin_points[1]).lineTo(*pin_points[2])\
        .threePointArc(pa1,pin_points[3])\
        .lineTo(*pin_points[4]).lineTo(*pin_points[5])\
        .lineTo(*pin_points[6])\
        .threePointArc(pa2,pin_points[7])\
        .close().extrude(pin_width)
    pin = pin.faces("<Y").edges(">X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Y").edges("<X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Y").edges(">Z").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Y").edges("<Z").chamfer(chamfer_short,chamfer_long)

    pin = pin.faces("<Z").edges(">X").chamfer(chamfer_long, chamfer_short)
    pin = pin.faces("<Z").edges("<X").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges(">Y").chamfer(chamfer_short,chamfer_long)
    pin = pin.faces("<Z").edges("<Y").chamfer(chamfer_short,chamfer_long)
    return pin

def generate_pins(params):
    pin_pitch=params.pin_pitch
    num_pins=params.num_pins

    if params.angled:
        pin=generate_angled_pin(params)
    else:
        pin=generate_straight_pin(params)

    pins = pin
    for i in range(0,num_pins):
        pins = pins.union(pin.translate((i*pin_pitch,0,0)))

    return pins

def generate_body(params, calc_dim):
    body, insert = generate_straight_body(params, calc_dim)
    if not params.angled:
        return body, insert

    front_side = seriesParams.pin_from_front_bottom
    pin_angled_from_back = seriesParams.pin_angled_from_back

    body = body.rotate((0,-front_side,0),(1,0,0),90)
    body = body.translate((0,front_side+pin_angled_from_back,0))
    if insert is not None:
        insert = insert.rotate((0,-front_side,0),(1,0,0),90)
        insert = insert.translate((0,front_side+pin_angled_from_back,0))
    return body, insert

def generate_straight_body(params ,calc_dim):
    flange_main_dif=seriesParams.body_width-seriesParams.body_flange_width
    body = cq.Workplane("XY")\
        .moveTo(calc_dim.left_to_pin, -seriesParams.body_width-params.back_to_pin)
        # back is the side which faces up for the angled version.
        # We use this becaus we want to be consistent with the footprint generation script.
    body = body.hLine(calc_dim.length).vLine(seriesParams.body_flange_width)\
        .hLine(-seriesParams.flange_lenght).vLine(flange_main_dif)\
        .hLine(2*seriesParams.flange_lenght-calc_dim.length)\
        .vLine(-flange_main_dif).hLine(-seriesParams.flange_lenght)\
        .close().extrude(seriesParams.body_height)

    single_cutout = cq.Workplane("XY")\
        .workplane(offset=seriesParams.body_height-seriesParams.plug_cutout_depth)\
        .moveTo(-seriesParams.plug_cut_len/2.0, seriesParams.plug_cutout_front)\
        .vLine(seriesParams.plug_cut_width)\
        .hLineTo(-seriesParams.plug_seperator_distance/2.0)\
        .vLineTo(seriesParams.plug_cutout_back-seriesParams.plug_trapezoid_width)\
        .hLineTo(-seriesParams.plug_trapezoid_short/2.0)\
        .lineTo(-seriesParams.plug_trapezoid_long/2.0,seriesParams.plug_cutout_back)\
        .hLine(seriesParams.plug_trapezoid_long)\
        .lineTo(seriesParams.plug_trapezoid_short/2.0,seriesParams.plug_cutout_back-seriesParams.plug_trapezoid_width)\
        .hLineTo(seriesParams.plug_seperator_distance/2.0)\
        .vLineTo(seriesParams.plug_cutout_front+seriesParams.plug_cut_width)\
        .hLineTo(seriesParams.plug_cut_len/2.0).vLine(-seriesParams.plug_cut_width)\
        .hLineTo(seriesParams.plug_arc_len/2.0)\
        .threePointArc((0,seriesParams.plug_arc_mid_y),(-seriesParams.plug_arc_len/2.0,seriesParams.plug_cutout_front))\
        .close().extrude(seriesParams.plug_cutout_depth)
    plug_cutouts = single_cutout
    for i in range(0, params.num_pins):
        plug_cutouts = plug_cutouts.union(single_cutout.translate((i*params.pin_pitch,0,0)))
    body=body.cut(plug_cutouts)
    insert = None
    # if params.flanged:
    #     thread_insert = cq.Workplane("XY").workplane(offset=body_height)\
    #         .moveTo(-mount_hole_to_pin, 0)\
    #         .circle(thread_insert_r)\
    #         .moveTo(mount_hole_to_pin+(num_pins-1)*pin_pitch, 0)\
    #         .circle(thread_insert_r)\
    #         .extrude(-thread_depth)
    #     body = body.cut(thread_insert)
    #     insert = cq.Workplane("XY").workplane(offset=body_height)\
    #         .moveTo(-mount_hole_to_pin, 0)\
    #         .circle(thread_insert_r).circle(thread_r)\
    #         .moveTo(mount_hole_to_pin+(num_pins-1)*pin_pitch, 0)\
    #         .circle(thread_insert_r).circle(thread_r)\
    #         .extrude(-thread_depth-0.1)

    return body, insert

def generate_mount_screw(params, calc_dim):
    if not params.mount_hole:
        return None

    num_pins = params.num_pins
    pin_pitch = params.pin_pitch
    pcb_thickness = seriesParams.pcb_thickness
    head_radius = seriesParams.mount_screw_head_radius
    head_heigth = seriesParams.mount_screw_head_heigth
    head_fillet = seriesParams.mount_screw_fillet
    slot_width = seriesParams.mount_screw_slot_width
    slot_depth = seriesParams.mount_screw_slot_depth
    mount_hole_to_pin = params.mount_hole_to_pin
    thread_r = seriesParams.thread_r
    mount_hole_y=calc_dim.mount_hole_y

    screw = cq.Workplane("XY").workplane(offset=-pcb_thickness)\
        .moveTo(-mount_hole_to_pin, -mount_hole_y)\
        .circle(head_radius)\
        .extrude(-head_heigth)
    screw = screw.faces(">Z").workplane()\
        .circle(thread_r).extrude(pcb_thickness+0.1)
    screw = screw.faces("<Z").edges().fillet(head_fillet)
    screw = screw.faces("<Z").workplane()\
        .rect(head_radius*2,slot_width).cutBlind(-slot_depth)

    screw = screw.union(screw.translate((2*mount_hole_to_pin+(num_pins-1)*pin_pitch,0,0)))
    return screw

def generate_part(part_key):
    params = all_params[part_key]
    calc_dim = dimensions(params)
    pins = generate_pins(params)
    body, insert = generate_body(params, calc_dim)
    mount_screw = None #generate_mount_screw(params, calc_dim)
    return (pins, body, insert, mount_screw)


#opend from within freecad
if "module" in __name__ :
    part_to_build = "MCV_01x04_GF_3.5mm_MH"

    FreeCAD.Console.PrintMessage("Started from cadquery: Building " +part_to_build+"\n")
    (pins, body, insert, mount_screw) = generate_part(part_to_build)
    show(pins)
    show(body)
    if insert is not None:
        show(insert)
    #if mount_screw is not None:
    #    show(mount_screw)

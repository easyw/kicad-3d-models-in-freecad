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

___ver___ = "1.1 18/04/2016"


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
from cq_helpers import *
from conn_phoenix_mstb_params import *


def generate_straight_pin(params):
    pin_width=globalParams.pin_width
    pin_depth=globalParams.pin_depth
    body_height=globalParams.body_height
    pin_inside_distance=globalParams.pin_inside_distance
    chamfer_long = globalParams.pin_chamfer_long
    chamfer_short = globalParams.pin_chamfer_short


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
    pin_width=globalParams.pin_width
    pin_depth=globalParams.pin_depth
    body_height=globalParams.body_height
    pin_inside_distance=globalParams.pin_inside_distance
    chamfer_long = globalParams.pin_chamfer_long
    chamfer_short = globalParams.pin_chamfer_short
    pin_from_bottom = globalParams.pin_from_front_bottom
    pin_bend_radius = globalParams.pin_bend_radius
    pin_angled_from_back = globalParams.pin_angled_from_back


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

    front_side = globalParams.pin_from_front_bottom
    pin_angled_from_back = globalParams.pin_angled_from_back

    body = body.rotate((0,-front_side,0),(1,0,0),90)
    body = body.translate((0,front_side+pin_angled_from_back,0))
    if insert is not None:
        insert = insert.rotate((0,-front_side,0),(1,0,0),90)
        insert = insert.translate((0,front_side+pin_angled_from_back,0))
    return body, insert

def generate_straight_body(params ,calc_dim):
    num_pins = params.num_pins
    pin_pitch = params.pin_pitch
    mount_hole_to_pin = params.mount_hole_to_pin

    body_len = calc_dim.lenght
    body_width = globalParams.body_width
    body_height = globalParams.body_height
    front_side = globalParams.pin_from_front_bottom
    left_side = -params.side_to_pin

    cutout_len = calc_dim.cutout_len

    lock_prod = globalParams.body_lock_prodrudion
    lock_h = globalParams.body_lock_height
    lock_chamf_h = globalParams.body_lock_chamfer_h
    lock_chamf_d = globalParams.body_lock_chamfer_d
    lock_cutout_t_l = globalParams.body_lock_cutout_top_l
    lock_cutout_b_l = globalParams.body_lock_cutout_bottom_l


    plug_width = globalParams.plug_width
    plug_arc_width = globalParams.plug_arc_width
    plug_arc_len = globalParams.plug_arc_len
    plug_front = globalParams.plug_front
    plug_left_side = calc_dim.plug_left_side
    plug_len = calc_dim.cutout_len
    plug_depth = globalParams.plug_depth

    thread_insert_r = globalParams.thread_insert_r
    thread_depth = globalParams.thread_depth
    thread_r = globalParams.thread_r

    start_point = (-(front_side+lock_prod-body_width),0)
    side_profile = [(front_side,0)]
    add_p_to_chain(side_profile, (0,body_height))
    add_p_to_chain(side_profile, (-body_width+lock_chamf_d, 0))
    add_p_to_chain(side_profile, (-lock_chamf_d, -lock_chamf_h))
    add_p_to_chain(side_profile, (0, -lock_h+lock_chamf_h))
    add_p_to_chain(side_profile, (lock_prod,0))

    side_profile=mirror(side_profile)
    body = cq.Workplane("YZ").workplane(offset=left_side)\
        .moveTo(*start_point).polyline(side_profile).close()\
        .extrude(body_len)

    plug_cutout = cq.Workplane("XY").workplane(offset=body_height)\
        .moveTo(plug_left_side,-plug_front)\
        .rect(plug_len, plug_width, False).extrude(-plug_depth)
    body = body.cut(plug_cutout)

    midpoint_y=-(plug_arc_width-plug_width)-plug_front
    plug_cutout = cq.Workplane("XY").workplane(offset=body_height)\
        .moveTo(-plug_arc_len/2.0,-plug_front)\
        .threePointArc((0,midpoint_y),(plug_arc_len/2.0,-plug_front))\
        .close().extrude(-plug_depth)

    plug_cutouts = plug_cutout
    for i in range(0,num_pins):
        plug_cutouts = plug_cutouts.union(plug_cutout.translate((i*pin_pitch,0,0)))
    body = body.cut(plug_cutouts)
    back_width = body_width-plug_width-(front_side-plug_front)
    lock_cutout = cq.Workplane("XZ").workplane(offset=-body_width+front_side)\
        .moveTo(-lock_cutout_t_l/2.0,body_height).hLine(lock_cutout_t_l)\
        .line(-(lock_cutout_t_l-lock_cutout_b_l)/2.0, -lock_chamf_h)\
        .hLine(-lock_cutout_b_l).close()\
        .extrude(back_width)

    lock_cutouts = lock_cutout
    for i in range(0,num_pins):
        lock_cutouts = lock_cutouts.union(lock_cutout.translate((i*pin_pitch,0,0)))

    if params.flanged:
        lock_cutouts = lock_cutouts.union(lock_cutout.translate((-mount_hole_to_pin,0,0)))
        lock_cutouts = lock_cutouts.union(lock_cutout.translate((mount_hole_to_pin+(num_pins-1)*pin_pitch,0,0)))
    body = body.cut(lock_cutouts)

    insert = None
    if params.flanged:
        thread_insert = cq.Workplane("XY").workplane(offset=body_height)\
            .moveTo(-mount_hole_to_pin, 0)\
            .circle(thread_insert_r)\
            .moveTo(mount_hole_to_pin+(num_pins-1)*pin_pitch, 0)\
            .circle(thread_insert_r)\
            .extrude(-thread_depth)
        body = body.cut(thread_insert)
        insert = cq.Workplane("XY").workplane(offset=body_height)\
            .moveTo(-mount_hole_to_pin, 0)\
            .circle(thread_insert_r).circle(thread_r)\
            .moveTo(mount_hole_to_pin+(num_pins-1)*pin_pitch, 0)\
            .circle(thread_insert_r).circle(thread_r)\
            .extrude(-thread_depth-0.1)

    return body, insert

def generate_mount_screw(params, calc_dim):
    if not params.mount_hole:
        return None

    num_pins = params.num_pins
    pin_pitch = params.pin_pitch
    pcb_thickness = globalParams.pcb_thickness
    head_radius = globalParams.mount_screw_head_radius
    head_heigth = globalParams.mount_screw_head_heigth
    head_fillet = globalParams.mount_screw_fillet
    slot_width = globalParams.mount_screw_slot_width
    slot_depth = globalParams.mount_screw_slot_depth
    mount_hole_to_pin = params.mount_hole_to_pin
    thread_r = globalParams.thread_r
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
    mount_screw = generate_mount_screw(params, calc_dim)
    return (pins, body, insert, mount_screw)


#opend from within freecad
if "module" in __name__ :
    part_to_build = "MSTB_01x02_5.00mm_MH"

    FreeCAD.Console.PrintMessage("Started from cadquery: Building " +part_to_build+"\n")
    (pins, body, insert, mount_screw) = generate_part(part_to_build)
    show(pins)
    show(body)
    if insert is not None:
        show(insert)
    if mount_screw is not None:
        show(mount_screw)

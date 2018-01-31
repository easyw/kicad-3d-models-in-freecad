# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning JST XH Connectors

## requirements
## freecad (v1.5 and v1.6 have been tested)
## cadquery FreeCAD plugin (v0.3.0 and v0.2.0 have been tested)
##   https://github.com/jmwright/cadquery-freecad-module

## This script can be run from within the cadquery module of freecad.
## To generate VRML/ STEP files for, use launch-cq-phoenix-export
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

__title__ = "model description for Phoenix Series MSTB Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for Phoenix Series MSTB Connectors using cadquery'

___ver___ = "1.1 03/12/2017"

import sys
import os
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


def generate_angled_pin(params, calc_dim):
    pin_width=seriesParams.pin_width
    pin_depth=seriesParams.pin_depth
    body_height=seriesParams.body_height
    pin_inside_distance=seriesParams.pin_inside_distance
    chamfer_long = seriesParams.pin_chamfer_long
    chamfer_short = seriesParams.pin_chamfer_short
    pin_from_bottom = -calc_dim.body_front_y
    pin_bend_radius = seriesParams.pin_bend_radius
    pin_angled_from_back = -params.angled_back_to_pin


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


def generate_pins(params, calc_dim):
    pin_pitch=params.pin_pitch
    num_pins=params.num_pins

    if params.angled:
        pin=generate_angled_pin(params, calc_dim)
    else:
        pin=generate_straight_pin(params)

    pins = pin
    for i in range(0,num_pins):
        pins = pins.union(pin.translate((i*pin_pitch,0,0)))

    return pins


def generate_body(params, calc_dim, with_details=True):
    body, insert = generate_straight_body(params, calc_dim, with_details)
    if not params.angled:
        return body, insert

    front_side = calc_dim.body_front_y
    pin_angled_from_back = params.angled_back_to_pin

    rotation_origin=(0,front_side,0)
    translation_vector=(0,-front_side-pin_angled_from_back,0)

    body = body.rotate(rotation_origin,(1,0,0),90)
    body = body.translate(translation_vector)
    if insert is not None:
        insert = insert.rotate(rotation_origin,(1,0,0),90)
        insert = insert.translate(translation_vector)
    return body, insert


def generate_main_body_flanged(params, calc_dim):
    flange_main_dif=seriesParams.body_width-seriesParams.body_flange_width

    body = cq.Workplane("XY")\
        .moveTo(calc_dim.left_to_pin, calc_dim.body_front_y)\
        .hLine(calc_dim.length).vLine(seriesParams.body_flange_width)\
        .hLine(-seriesParams.flange_lenght).vLine(flange_main_dif)\
        .hLine(2*seriesParams.flange_lenght-calc_dim.length)\
        .vLine(-flange_main_dif).hLine(-seriesParams.flange_lenght)\
        .close().extrude(seriesParams.body_height)

    BS = cq.selectors.BoxSelector
    p1 = (calc_dim.left_to_pin-0.01,
          -seriesParams.body_width-params.back_to_pin-0.01,
          0.1)
    p2 = (calc_dim.length,
          calc_dim.body_front_y+seriesParams.body_flange_width+0.01,
          seriesParams.body_height-0.1)
    body = body.edges(BS(p1, p2)).fillet(seriesParams.body_roundover_r)

    return body


def generate_main_body(params, calc_dim):
    body = cq.Workplane("XY")\
        .moveTo(calc_dim.left_to_pin, calc_dim.body_front_y)\
        .hLine(calc_dim.length).vLine(seriesParams.body_width)\
        .hLine(-calc_dim.length)\
        .close().extrude(seriesParams.body_height)

    return body

def generate_scoreline(params, calc_dim):
    wp_offset = (-params.side_to_pin + seriesParams.flange_lenght) if params.flanged else (-params.side_to_pin)
    sc_len=(calc_dim.length-2*seriesParams.flange_lenght) if params.flanged else (calc_dim.length)

    arc_p1=(-params.back_to_pin,seriesParams.scoreline_from_bottom-seriesParams.scoreline_width/2.0)
    arc_p2=v_add(arc_p1,(seriesParams.scoreline_width/2.0, seriesParams.scoreline_width/2.0))
    arc_p3=v_add(arc_p1,(0, seriesParams.scoreline_width))
    scline = cq.Workplane("YZ").workplane(offset=wp_offset)\
        .moveTo(*arc_p1)\
        .hLine(seriesParams.scoreline_width/2.0).vLine(seriesParams.scoreline_width)\
        .hLine(-seriesParams.scoreline_width/2.0)\
        .close().extrude(sc_len)
        #.lineTo(*arc_p2).lineTo(*arc_p3).close().extrude(sc_len)
    return scline

def generate_straight_body(params, calc_dim, with_details):
    if params.flanged:
        body = generate_main_body_flanged(params, calc_dim)
    else:
        body = generate_main_body(params, calc_dim)

    body = body.union(generate_scoreline(params, calc_dim))
    if with_details:
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
    if params.flanged and with_details:
        thread_insert = cq.Workplane("XY").workplane(offset=seriesParams.body_height)\
            .moveTo(-params.mount_hole_to_pin, 0)\
            .circle(seriesParams.thread_insert_r)\
            .moveTo(params.mount_hole_to_pin+(params.num_pins-1)*params.pin_pitch, 0)\
            .circle(seriesParams.thread_insert_r)\
            .extrude(-seriesParams.thread_depth)
        body = body.cut(thread_insert)
        insert = cq.Workplane("XY").workplane(offset=seriesParams.body_height)\
            .moveTo(-params.mount_hole_to_pin, 0)\
            .circle(seriesParams.thread_insert_r)\
            .moveTo(params.mount_hole_to_pin+(params.num_pins-1)*params.pin_pitch, 0)\
            .circle(seriesParams.thread_insert_r)\
            .extrude(-seriesParams.thread_depth-0.1)\
            .moveTo(-params.mount_hole_to_pin, 0)\
            .circle(seriesParams.thread_r)\
            .moveTo(params.mount_hole_to_pin+(params.num_pins-1)*params.pin_pitch, 0)\
            .circle(seriesParams.thread_r)\
            .cutThruAll()

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

class plug_params():
    body_width = 11.1
    flange_width = 5.6
    flange_height = 6.9
    y_max_wire_side = -6.4
    y_max_screw_side = 4.7


def generate_plug(params, calc_dim):
    plug, plug_screws = generate_plug_staight(params, calc_dim)

    if not params.angled:
        return plug, plug_screws

    front_side = calc_dim.body_front_y
    pin_angled_from_back = params.angled_back_to_pin

    rotation_origin=(0, front_side,0)
    translation_vector=(0, -front_side-pin_angled_from_back,0)

    plug = plug.rotate(rotation_origin,(1,0,0),90)
    plug = plug.translate(translation_vector)
    if plug_screws is not None:
        plug_screws = plug_screws.rotate(rotation_origin,(1,0,0),90)
        plug_screws = plug_screws.translate(translation_vector)
    return plug, plug_screws

def generate_plug_staight(params, calc_dim):
    plug_bottom = seriesParams.body_height
    plug_main_side_to_0 = 4.2/2
    if params.pin_pitch == 3.81:
        plug_main_side_to_0 = 4.6/2
    if params.pin_pitch == 5.08:
        plug_main_side_to_0 = 2.54

    plug_main_body_len = plug_main_side_to_0*2 + (params.num_pins-1)*params.pin_pitch

    psvp = [(plug_params.flange_width/2.0, plug_bottom)]
    add_p_to_chain(psvp, (-8.1, 0))
    add_p_to_chain(psvp, (-0.3, 0.3))
    arc_psv_1 = get_third_arc_point2(psvp[1], psvp[2])
    add_p_to_chain(psvp, (0, 0.6))
    add_p_to_chain(psvp, (-0.8, 0))
    add_p_to_chain(psvp, (0, 8))
    add_p_to_chain(psvp, (5.7, 0))
    add_p_to_chain(psvp, (0, 0.3))
    add_p_to_chain(psvp, (0.3, 0.3))
    arc_psv_2 = get_third_arc_point1(psvp[7], psvp[8])
    add_p_to_chain(psvp, (0.2, 0))
    add_p_to_chain(psvp, (0.5, -0.5))
    arc_psv_3 = get_third_arc_point2(psvp[9], psvp[10])
    add_p_to_chain(psvp, (0, -0.7))
    add_p_to_chain(psvp, (3.8, -1.0))
    add_p_to_chain(psvp, (0, 0.2))
    add_p_to_chain(psvp, (0.3, 0))
    add_p_to_chain(psvp, (0.3, -0.3))
    arc_psv_4 = get_third_arc_point2(psvp[14], psvp[15])
    add_p_to_chain(psvp, (0, -5.8))
    add_p_to_chain(psvp, (-0.5, -0.5))
    arc_psv_5 = get_third_arc_point1(psvp[16], psvp[17])
    add_p_to_chain(psvp, (-1.4, 0))

    plug_body = cq.Workplane("YZ").workplane(offset=-plug_main_side_to_0)\
        .moveTo(*psvp[0]).lineTo(*psvp[1])\
        .threePointArc(arc_psv_1, psvp[2])\
        .lineTo(*psvp[3]).lineTo(*psvp[4])\
        .lineTo(*psvp[5]).lineTo(*psvp[6])\
        .lineTo(*psvp[7]).threePointArc(arc_psv_2, psvp[8])\
        .lineTo(*psvp[9]).threePointArc(arc_psv_3, psvp[10])\
        .lineTo(*psvp[11]).lineTo(*psvp[12]).lineTo(*psvp[13])\
        .lineTo(*psvp[14]).threePointArc(arc_psv_4, psvp[15])\
        .lineTo(*psvp[16]).threePointArc(arc_psv_5, psvp[17])\
        .lineTo(*psvp[18]).close().extrude(plug_main_body_len)

    if params.flanged:
        flange_radius = 1
        flange = cq.Workplane("XY").workplane(offset=plug_bottom)\
            .moveTo(calc_dim.left_to_pin, -plug_params.flange_width/2)\
            .hLine(calc_dim.length).vLine(plug_params.flange_width)\
            .hLine(-calc_dim.length)\
            .close().extrude(plug_params.flange_height)#\
            #.edges("|Z").fillet(flange_radius)

        flange_screw_cutouts = cq.Workplane("XY")\
            .workplane(offset=seriesParams.body_height+plug_params.flange_height)\
            .moveTo(-params.mount_hole_to_pin, 0)\
            .circle(2)\
            .moveTo(params.mount_hole_to_pin+(params.num_pins-1)*params.pin_pitch, 0)\
            .circle(2)\
            .extrude(-plug_params.flange_height+1.5)
        flange = flange.cut(flange_screw_cutouts)

        plug_body = plug_body.union(flange)

        BS = cq.selectors.BoxSelector
        p1 = (calc_dim.left_to_pin-0.01,
              -seriesParams.body_width-params.back_to_pin-0.01,
              plug_bottom+1)
        p2 = (calc_dim.length,
              calc_dim.body_front_y+seriesParams.body_flange_width+0.01,
              plug_bottom+plug_params.flange_height-0.1)
        plug_body = plug_body.edges(BS(p1, p2)).fillet(seriesParams.body_roundover_r)

    first_hole_pos = (params.num_pins-1)*params.pin_pitch/2.0

    single_screwhole_cutout = plug_body.faces(">Y").workplane()\
        .moveTo(first_hole_pos, -0.7).circle(1.45).extrude(-2, False)

    single_screw = plug_body.faces(">Y").workplane(offset=-2)\
        .moveTo(first_hole_pos, -0.7).circle(1.4).extrude(1, False)\
        .faces(">Y").workplane().rect(2*1.4, 0.4).cutBlind(-0.3)

    wcu_top_width = 2.7
    wcu_top_len = 4.8
    wcu_top_arc_center_width = 3
    wcu_top_y0 = 0.7

    wcu_bottom_len = 2.75
    wcu_bottom_width = 1.72

    wire_input_single_cutout = cq.Workplane("XY").workplane(offset=8.9+plug_bottom)\
        .moveTo(wcu_top_width/2.0, -wcu_top_y0)\
        .threePointArc((wcu_top_arc_center_width/2.0, -wcu_top_y0-wcu_top_len/2.0),
                       (wcu_top_width/2.0, -wcu_top_y0-wcu_top_len))\
        .hLine(-wcu_top_width)\
        .threePointArc((-wcu_top_arc_center_width/2.0, -wcu_top_y0-wcu_top_len/2.0),
                       (-wcu_top_width/2.0, -wcu_top_y0))\
        .close()\
        .workplane(offset=-1.5).rect(wcu_bottom_width, wcu_bottom_len).loft()\
        .faces("<Z").rect(wcu_bottom_width, wcu_bottom_len).extrude(-1.5)
        #.close().extrude(2)

    screwhole_cutouts = single_screwhole_cutout
    screws = single_screw
    wire_input_cutouts = wire_input_single_cutout
    for i in range(0, params.num_pins):
        screwhole_cutouts = screwhole_cutouts.union(
            single_screwhole_cutout.translate((i*params.pin_pitch, 0, 0))
            )
        screws = screws.union(
            single_screw.translate((i*params.pin_pitch, 0, 0))
            )
        wire_input_cutouts = wire_input_cutouts.union(
            wire_input_single_cutout.translate((i*params.pin_pitch, 0, 0))
            )

    plug_body = plug_body.cut(screwhole_cutouts)
    plug_body = plug_body.cut(wire_input_cutouts)

    if params.flanged:
        flange_screw = cq.Workplane("XY")\
            .workplane(offset=seriesParams.body_height+1.5)\
            .moveTo(-params.mount_hole_to_pin, 0)\
            .circle(1.95).extrude(1.5)\
            .faces(">Z").workplane().rect(0.4,2*2).cutBlind(-0.5)
        flange_screw_distance = 2*params.mount_hole_to_pin+(params.num_pins-1)*params.pin_pitch

        screws=screws.union(flange_screw)
        screws=screws.union(flange_screw.translate((flange_screw_distance, 0, 0)))
    return plug_body, screws


def generate_part(part_key, with_plug=False):
    params = all_params[part_key]
    calc_dim = dimensions(params)
    pins = generate_pins(params, calc_dim)
    body, insert = generate_body(params, calc_dim,
                                 with_details=(not with_plug))
    mount_screw = generate_mount_screw(params, calc_dim)
    if with_plug:
        plug, plug_screws = generate_plug(params, calc_dim)
    else:
        plug = None
        plug_screws = None
    return (pins, body, insert, mount_screw, plug, plug_screws)


# opend from within freecad
if "module" in __name__:
    part_to_build = "MCV_01x04_GF_3.5mm_MH"
    #part_to_build = "MCV_01x04_G_3.5mm"
    #part_to_build = "MC_01x04_G_3.5mm"
    #part_to_build = "MC_01x04_GF_3.5mm_MH"
    with_plug = True

    FreeCAD.Console.PrintMessage("Started from cadquery: Building " +
                                 part_to_build + "\n")
    (pins, body, insert, mount_screw, plug, plug_screws) = generate_part(part_to_build, with_plug)
    show(pins)
    show(body)
    if insert is not None:
        show(insert)
    if mount_screw is not None:
        show(mount_screw)
    if plug is not None:
        show(plug)
    if plug_screws is not None:
        show(plug_screws)

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

___ver___ = "1.2 03/12/2017"


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
from cq_helpers import *
from conn_phoenix_mstb_params import *


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

def generate_body(params, calc_dim, with_details=False):
    body, insert = generate_straight_body(params, calc_dim, with_details)
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

def generate_straight_body(params ,calc_dim, with_details):
    num_pins = params.num_pins
    pin_pitch = params.pin_pitch
    mount_hole_to_pin = params.mount_hole_to_pin

    body_len = calc_dim.lenght
    body_width = seriesParams.body_width
    body_height = seriesParams.body_height
    front_side = seriesParams.pin_from_front_bottom
    left_side = -params.side_to_pin

    cutout_len = calc_dim.cutout_len

    lock_prod = seriesParams.body_lock_prodrudion
    lock_h = seriesParams.body_lock_height
    lock_chamf_h = seriesParams.body_lock_chamfer_h
    lock_chamf_d = seriesParams.body_lock_chamfer_d
    lock_cutout_t_l = seriesParams.body_lock_cutout_top_l
    lock_cutout_b_l = seriesParams.body_lock_cutout_bottom_l


    plug_width = seriesParams.plug_width
    plug_arc_width = seriesParams.plug_arc_width
    plug_arc_len = seriesParams.plug_arc_len
    plug_front = seriesParams.plug_front
    plug_left_side = calc_dim.plug_left_side
    plug_len = calc_dim.cutout_len
    plug_depth = seriesParams.plug_depth

    thread_insert_r = seriesParams.thread_insert_r
    thread_depth = seriesParams.thread_depth
    thread_r = seriesParams.thread_r

    start_point = (-(front_side+lock_prod-body_width), 0)
    side_profile = [(front_side, 0)]
    add_p_to_chain(side_profile, (0, body_height))
    add_p_to_chain(side_profile, (-body_width+lock_chamf_d, 0))
    add_p_to_chain(side_profile, (-lock_chamf_d, -lock_chamf_h))
    add_p_to_chain(side_profile, (0, -lock_h+lock_chamf_h))
    add_p_to_chain(side_profile, (lock_prod, 0))

    side_profile = mirror(side_profile)
    body = cq.Workplane("YZ").workplane(offset=left_side)\
        .moveTo(*start_point).polyline(side_profile).close()\
        .extrude(body_len)

    if with_details:
        plug_cutout = cq.Workplane("XY").workplane(offset=body_height)\
            .moveTo(plug_left_side, -plug_front)\
            .rect(plug_len, plug_width, False).extrude(-plug_depth)
        body = body.cut(plug_cutout)

        midpoint_y = -(plug_arc_width-plug_width)-plug_front

        plug_cutout = cq.Workplane("XY").workplane(offset=body_height)\
            .moveTo(-plug_arc_len/2.0, -plug_front)\
            .threePointArc((0,midpoint_y), (plug_arc_len/2.0, -plug_front))\
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
    if params.flanged and with_details:
        thread_insert = cq.Workplane("XY").workplane(offset=body_height)\
            .moveTo(-mount_hole_to_pin, 0)\
            .circle(thread_insert_r)\
            .moveTo(mount_hole_to_pin+(num_pins-1)*pin_pitch, 0)\
            .circle(thread_insert_r)\
            .extrude(-thread_depth)
        body = body.cut(thread_insert)
        insert = cq.Workplane("XY").workplane(offset=body_height)\
            .moveTo(-mount_hole_to_pin, 0)\
            .circle(thread_insert_r)\
            .moveTo(mount_hole_to_pin+(num_pins-1)*pin_pitch, 0)\
            .circle(thread_insert_r)\
            .extrude(-thread_depth-0.1)\
            .moveTo(-mount_hole_to_pin, 0)\
            .circle(thread_r)\
            .moveTo(mount_hole_to_pin+(num_pins-1)*pin_pitch, 0)\
            .circle(thread_r)\
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
    mount_hole_y = calc_dim.mount_hole_y

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


def generate_plug_straight(params, calc_dim):
    psv_to_0 = 2.5
    if params.pin_pitch == 5.08:
        psv_to_0 = 2.54
    elif params.pin_pitch == 7.5:
        psv_to_0 = 2.75
    elif params.pin_pitch == 7.62:
        psv_to_0 = 2.81

    plg_main_with = 2*psv_to_0+(params.num_pins-1)*params.pin_pitch

    #Plug Side View Points
    psvp = [(-2.9, seriesParams.body_height)]    # 0
    add_p_to_chain(psvp, (5.8, 0))               # 1
    add_p_to_chain(psvp, (0.85, 0.5))            # 2
    add_p_to_chain(psvp, (3.4, 0))               # 3
    add_p_to_chain(psvp, (1.35, 0.4))            # 4
    add_p_to_chain(psvp, (2.15, 0))              # 5
    add_p_to_chain(psvp, (0.6, 0.6))             # 6
    arc1_psv = get_third_arc_point2(psvp[5], psvp[6])
    add_p_to_chain(psvp, (0, 7.4))               # 7
    add_p_to_chain(psvp, (-0.2, 0.2))            # 8
    arc2_psv = get_third_arc_point1(psvp[7], psvp[8])
    add_p_to_chain(psvp, (-0.55, 0.02))          # 9
    add_p_to_chain(psvp, (-0.2, -0.35))          # 10
    add_p_to_chain(psvp, (-4.65, 0.83))          # 11
    add_p_to_chain(psvp, (0, 0.1))               # 12
    add_p_to_chain(psvp, (-0.2, 0.2))            # 13
    arc3_psv = get_third_arc_point1(psvp[12], psvp[13])
    add_p_to_chain(psvp, (-9.2, 0))              # 14
    add_p_to_chain(psvp, (0, -9))                # 15
    add_p_to_chain(psvp, (0.85, 0))              # 16

    plug_body = cq.Workplane("YZ").workplane(offset=-psv_to_0)\
        .moveTo(*psvp[0]).lineTo(*psvp[1])\
        .lineTo(*psvp[2]).lineTo(*psvp[3])\
        .lineTo(*psvp[4]).lineTo(*psvp[5])\
        .threePointArc(arc1_psv, psvp[6])\
        .lineTo(*psvp[7]).threePointArc(arc2_psv, psvp[8])\
        .lineTo(*psvp[9]).lineTo(*psvp[10])\
        .lineTo(*psvp[11]).lineTo(*psvp[12])\
        .threePointArc(arc3_psv, psvp[13])\
        .lineTo(*psvp[14]).lineTo(*psvp[15]).lineTo(*psvp[16])\
        .close().extrude(plg_main_with)
    if not params.flanged:
        # plug lock points
        plug_lock_width=1.6

        plp = [psvp[1]]
        add_p_to_chain(plp, (1.125, 0))
        add_p_to_chain(plp, (0.2, 0.2))
        arc1_pl = get_third_arc_point2(plp[1], plp[2])
        add_p_to_chain(plp, (0.6, 0))
        arc2_pl = v_add(plp[2], (0.3, 0.3))
        add_p_to_chain(plp, (0, -3.2))
        add_p_to_chain(plp, (-0.45, -0.45))
        add_p_to_chain(plp, (0.7, -1.1))
        add_p_to_chain(plp, (1.1, 1.15))
        add_p_to_chain(plp, (0.3, 3.68))
        add_p_to_chain(plp, (0.3, 0.3))
        add_p_to_chain(plp, (0, 0.1))
        add_p_to_chain(plp, (-4.3, 0))
        arc3_pl = get_third_arc_point1(plp[8], plp[9])

        pl_wp_offset = params.pin_pitch/2.0
        plug_lock = cq.Workplane("YZ").workplane(offset=pl_wp_offset)\
            .moveTo(*plp[0]).lineTo(*plp[1])\
            .threePointArc(arc1_pl, plp[2])\
            .threePointArc(arc2_pl, plp[3])\
            .lineTo(*plp[4]).lineTo(*plp[5])\
            .lineTo(*plp[6]).lineTo(*plp[7])\
            .lineTo(*plp[8])\
            .threePointArc(arc3_pl, plp[9])\
            .lineTo(*plp[10]).lineTo(*plp[11])\
            .close().extrude(-plug_lock_width)

        BS = cq.selectors.BoxSelector
        plug_lock = plug_lock.edges(
                BS(
                    (pl_wp_offset-0.1, 0, 0),
                    (pl_wp_offset-plug_lock_width+0.1, 11,
                     seriesParams.body_height))
            ).fillet(0.3)

        plug_body = plug_body.union(plug_lock)
        if params.num_pins>2:
            plug_body = plug_body.union(plug_lock.translate(((params.num_pins-2)*params.pin_pitch+plug_lock_width,0,0)))

    single_screw_cutout = plug_body.faces(">Y").workplane()\
        .moveTo((params.num_pins-1)*params.pin_pitch/2, -0.7)\
        .circle(1.9).extrude(-2,False)
    screw_cutouts = single_screw_cutout

    single_screw = plug_body.faces(">Y").workplane(offset=-2)\
        .moveTo((params.num_pins-1)*params.pin_pitch/2, -0.7)\
        .circle(1.9).extrude(1,False)\
            .faces(">Y").workplane().rect(2*2,0.4).cutBlind(-0.3)
    screws = single_screw
    for i in range(params.num_pins):
        #temp=single_screw.translate((i*params.pin_pitch, 0, 0))
        screws = screws.union(single_screw.translate((i*params.pin_pitch, 0, 0)))


    for i in range(params.num_pins):
        plug_body = plug_body.cut(single_screw_cutout.translate((i*params.pin_pitch, 0, 0)))

    if params.flanged:
        plug_flange = cq.Workplane("XY").workplane(offset=seriesParams.body_height)\
            .moveTo(calc_dim.lenght/2-params.side_to_pin)\
            .rect(calc_dim.lenght, 5.8).extrude(7.7)#\
            #.edges("|Z").fillet(1)
        mh_distance = 2*params.mount_hole_to_pin+(params.num_pins-1)*params.pin_pitch
        plug_flange = plug_flange.faces(">Z").workplane()\
            .moveTo(mh_distance/2.0).circle(2).cutBlind(-6)\
            .moveTo(-mh_distance/2.0).circle(2).cutBlind(-6)

        plug_mount_screw = plug_flange.faces(">Z").workplane(offset=-6)\
            .moveTo(mh_distance/2.0).circle(1.95).extrude(2, False)\
            .faces(">Z").workplane().rect(2*2, 0.4).cutBlind(-0.3)

        screws = screws.union(plug_mount_screw)
        screws = screws.union(plug_mount_screw.translate((-mh_distance, 0, 0)))
        plug_body = plug_body.union(plug_flange)

        BS = cq.selectors.BoxSelector
        x1 = -params.side_to_pin-0.01
        p1 = (x1,
              -5.8/2-0.01,
              seriesParams.body_height+1)
        p2 = (x1+calc_dim.lenght+0.2,
              5.8/2+0.01,
              seriesParams.body_height+7.7-0.1)
        plug_body = plug_body.edges(BS(p1, p2)).fillet(seriesParams.body_roundover_r)

    wire_cutout = plug_body.faces(">Z").workplane()\
        .moveTo(-(params.num_pins-1)*params.pin_pitch/2.0, 0.8).rect(3.5, 6.7)\
        .workplane(offset=-2).moveTo(0, 0.9).rect(3, 3.2).loft(combine=False)\
        .faces("<Z").workplane().rect(3, 3.2).extrude(2)
    for i in range(params.num_pins):
        plug_body = plug_body.cut(wire_cutout.translate((i*params.pin_pitch, 0, 0)))

    return plug_body, screws


def generate_plug(params, calc_dim):
    plug, plug_screws = generate_plug_straight(params, calc_dim)
    if not params.angled:
        return plug, plug_screws

    front_side = seriesParams.pin_from_front_bottom
    pin_angled_from_back = seriesParams.pin_angled_from_back

    plug = plug.rotate((0,-front_side,0),(1,0,0),90)
    plug = plug.translate((0,front_side+pin_angled_from_back,0))
    plug_screws = plug_screws.rotate((0,-front_side,0),(1,0,0),90)
    plug_screws = plug_screws.translate((0,front_side+pin_angled_from_back,0))

    return plug, plug_screws

def generate_part(part_key, with_plug=False):
    params = all_params[part_key]
    calc_dim = dimensions(params)
    pins = generate_pins(params)
    body, insert = generate_body(params, calc_dim, not with_plug)
    mount_screw = generate_mount_screw(params, calc_dim)

    plug, plug_screws = (None, None)
    if with_plug:
        plug, plug_screws = generate_plug(params, calc_dim)
    return (pins, body, insert, mount_screw, plug, plug_screws)


#opend from within freecad
if "module" in __name__ :
    #part_to_build = "MSTBVA_01x02_G_5.00mm"
    #part_to_build = 'MSTBA_01x02_G_5.00mm'
    #part_to_build = 'MSTB_01x02_GF_5.00mm'
    #part_to_build = 'MSTB_01x02_GF_5.00mm_MH'
    part_to_build = 'MSTBV_01x02_GF_5.00mm_MH'

    With_plug = False

    FreeCAD.Console.PrintMessage("Started from cadquery: Building " +part_to_build+"\n")
    (pins, body, insert, mount_screw, plug, plug_screws) = generate_part(part_to_build, With_plug)
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

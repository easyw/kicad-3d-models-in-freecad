# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning Molex PicoBlade 53261 Connectors

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

__title__ = "model description for Molex 53398 Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for Molex 53398 Connectors using cadquery'

___ver___ = "1.0 10/04/2016"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Rene Poeschl"
    STR_licEmail = "poeschlr@gmail.com"
    STR_licOrgSys = ""
    STR_licPreProc = ""

    LIST_license = ["",]
    ############################################################################

import sys

# DIRTY HACK TO ALLOW CENTRALICED HELPER SCRIPTS. (freecad cadquery does copy the file to /tmp and we can therefore not use relative paths for importing)

if "module" in __name__ :
    for path in sys.path:
        if 'molex/cq_models':
            p1 = path.replace('molex/cq_models','_tools')
    if not p1 in sys.path:
        sys.path.append(p1)
else:
    sys.path.append('../_tools')

from cq_helpers import *

import cadquery as cq
from math import sqrt
from Helpers import show
from collections import namedtuple
import FreeCAD

#global parameter
mounting_pad_size_y = 3.0
# y dimensions for pad given relative to mounting pad edge
rel_pad_y_outside_edge = 5.2
rel_pad_y_inside_edge = 3.6

# amount to shift y position of center for pick-and-place (positive -> shift whole footprint up)
center_shift_y = 0.6
y_origin_from_mountpad = -rel_pad_y_outside_edge/2 + mounting_pad_size_y/2 + center_shift_y
print(y_origin_from_mountpad)

mount_pin_back_to_body_back = 1
mount_pin_lenght = 1.7
mount_pin_width = 2.2
mount_pin_thickness = 0.25
mount_pin_bend_radius = 0.1 #estimated
mount_pin_height = 1.6 #Measured
mount_pin_top_len = 0.8 #Measured
mount_pin_fillet = 0.3

mount_holder_len = 1.5
mount_holder_width = 2.8
mount_holder_top_z = 2.3 #Measured
mount_holder_chamfer = 0.5 #Measured (+/-0.1 at least)
mount_back = y_origin_from_mountpad + mount_pin_width/2

body_height = 3.4
body_cutout_h = 2.4
body_bottom_width = 0.6
body_top_width = body_height-body_cutout_h-body_bottom_width
body_side_width = 0.6
body_width = 4.2
body_main_z = 0.1 #estimated
#body_center_y =
body_support_width = 0.5
body_cutout_depth = 3
body_top_cutout1_depth = 1 #Measured (+/-0.1 at least)
body_top_cutout2_depth = 0.8 #Measured (+/-0.1 at least)
body_front_chamfer=0.2 #estimated
body_back_y = mount_back + mount_pin_back_to_body_back
body_center_y = body_back_y - body_width/2

pin_width = 0.32
pin_pitch = 1.25
pin_protrution = 1
pin_contact_len = 0.4
pin_back_height = 0.5
pin_back_top = 1.375
pin_back_pocket = 0.3 #estimated
pin_radius = 0.2 # estimated
pin_tip_y = body_back_y + pin_protrution
pin_tip_chamfer = 0.2

contact_hight = 0.6 #Measured (+/-0.1 at least)
contact_to_bottom = 0.725-contact_hight/2+body_bottom_width
contact_front_tip = 3.8 #Measured (+/-0.1 at least)
contact_chamfer_height = 0.1 #estimated
contact_chamfer_width = 0.05 #estimated
contact_chamfer_depth = 0.5 #estimated

back_cutout_center_to_side = 2 #Measured
back_cutout_b_height = 1.15
back_cutout_b_width = 1.15
back_cutout_t_height = 1.45
back_cutout_t_width = 0.3 #Measured (+/-0.1 at least)

top_cutout_width = 0.5
top_cutout_len = 0.5
top_cutout_depth = 0.4

Params = namedtuple("Params",[
    'num_pins',
    'body_length',
    'body_front_cutout_len'
])

class series_params():
    series = "PicoBlade"
    manufacturer = 'Molex'
    mpn_format_string = '53261-{pins_per_row:02d}71'
    orientation = 'H'
    number_of_rows = 1
    datasheet = 'http://www.molex.com/pdm_docs/sd/532610271_sd.pdf'
    pinrange = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]
    mount_pin = '-1MP'

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

    pitch = pin_pitch

def make_params(num_pins):
    bl=3+(num_pins-1)*pin_pitch
    return Params(
        num_pins=num_pins,
        body_length=bl,
        body_front_cutout_len=bl-1.9
    )


def generate_pins(params):
    num_pins = params.num_pins
    body_len = params.body_length

    first_pin_wp_offset = (num_pins-1)/2.0*pin_pitch-pin_width/2.0

    pin_points=[(pin_tip_y,pin_tip_chamfer)]
    add_p_to_chain(pin_points, (0,pin_back_height-pin_tip_chamfer))
    add_p_to_chain(pin_points, (-pin_back_pocket,0))
    add_p_to_chain(pin_points, (0,pin_back_top-pin_back_height))
    add_p_to_chain(pin_points, (-pin_protrution+pin_back_pocket,0))
    pin_points.append((pin_points[4][0],contact_to_bottom+contact_hight))
    add_p_to_chain(pin_points, (-contact_front_tip,0))
    add_p_to_chain(pin_points, (0,-contact_hight))
    pin_points.append((pin_tip_y-2*pin_tip_chamfer-pin_radius-pin_contact_len,pin_points[7][1]))
    add_p_to_chain(pin_points, (pin_radius,-pin_radius))
    pr1=get_third_arc_point2(pin_points[8],pin_points[9])
    pin_points.append((pin_points[9][0],pin_tip_chamfer))
    add_p_to_chain(pin_points, (pin_tip_chamfer,-pin_tip_chamfer))
    add_p_to_chain(pin_points, (pin_contact_len,0))

    pin = cq.Workplane("YZ").workplane(offset=first_pin_wp_offset)\
        .moveTo(*pin_points[0])\
        .lineTo(*pin_points[1]).lineTo(*pin_points[2])\
        .lineTo(*pin_points[3]).lineTo(*pin_points[4])\
        .lineTo(*pin_points[5]).lineTo(*pin_points[6])\
        .lineTo(*pin_points[7]).lineTo(*pin_points[8])\
        .threePointArc(pr1,pin_points[9])\
        .lineTo(*pin_points[10]).lineTo(*pin_points[11])\
        .lineTo(*pin_points[12])\
        .close().extrude(pin_width)

    pin = pin.faces("<Y").edges(">Z")\
        .chamfer(contact_chamfer_depth, contact_chamfer_height)
    pin = pin.faces("<Y").edges("<Z")\
        .chamfer(contact_chamfer_height, contact_chamfer_depth)
    pin = pin.faces("<Y").edges(">X")\
        .chamfer(contact_chamfer_width, contact_chamfer_depth)
    pin = pin.faces("<Y").edges("<X")\
        .chamfer(contact_chamfer_width, contact_chamfer_depth)

    pins = pin
    for i in range(0,num_pins):
        pins = pins.union(pin.translate((-i*pin_pitch,0,0)))

    outher_bend_radius = mount_pin_bend_radius+mount_pin_thickness
    mount_pin_tip_x = body_len/2+mount_pin_lenght
    mount_pin_points = [(mount_pin_tip_x,0)]
    arc_points=[]
    add_p_to_chain(mount_pin_points, (0, mount_pin_thickness))
    add_p_to_chain(mount_pin_points,
                   (-mount_pin_lenght + mount_pin_thickness + mount_pin_bend_radius, 0))
    add_p_to_chain(mount_pin_points, (-mount_pin_bend_radius, mount_pin_bend_radius))
    arc_points.append(get_third_arc_point2(mount_pin_points[2], mount_pin_points[3]))
    add_p_to_chain(mount_pin_points, (0, mount_pin_height-2*(mount_pin_thickness+mount_pin_bend_radius)))
    add_p_to_chain(mount_pin_points, (mount_pin_bend_radius,mount_pin_bend_radius))
    arc_points.append(get_third_arc_point1(mount_pin_points[4],mount_pin_points[5]))
    add_p_to_chain(mount_pin_points, (mount_pin_top_len-mount_pin_bend_radius-mount_pin_thickness, 0))
    add_p_to_chain(mount_pin_points, (0,mount_pin_thickness))
    add_p_to_chain(mount_pin_points, (-mount_pin_top_len+mount_pin_bend_radius+mount_pin_thickness, 0))
    add_p_to_chain(mount_pin_points, (-outher_bend_radius,-outher_bend_radius))
    arc_points.append(get_third_arc_point2(mount_pin_points[8],mount_pin_points[9]))
    add_p_to_chain(mount_pin_points, (0, -mount_pin_height+2*(mount_pin_thickness+mount_pin_bend_radius)))
    add_p_to_chain(mount_pin_points, (outher_bend_radius,-outher_bend_radius))
    arc_points.append(get_third_arc_point1(mount_pin_points[10],mount_pin_points[11]))

    mount_pin1 = cq.Workplane("XZ").workplane(offset=-mount_back)\
        .moveTo(*mount_pin_points[0]).lineTo(*mount_pin_points[1])\
        .lineTo(*mount_pin_points[2]).threePointArc(arc_points[0],mount_pin_points[3])\
        .lineTo(*mount_pin_points[4]).threePointArc(arc_points[1],mount_pin_points[5])\
        .lineTo(*mount_pin_points[6]).lineTo(*mount_pin_points[7])\
        .lineTo(*mount_pin_points[8]).threePointArc(arc_points[2],mount_pin_points[9])\
        .lineTo(*mount_pin_points[10]).threePointArc(arc_points[3],mount_pin_points[11])\
        .close().extrude(mount_pin_width)

    #mount_pin1 = mount_pin1.faces(">X").edges("|Z").fillet(mount_pin_fillet)
    mount_pin1 = mount_pin1.faces(">Y").edges(">X")\
        .chamfer(mount_pin_fillet, mount_pin_fillet)
    mount_pin1 = mount_pin1.faces("<Y").edges(">X")\
        .chamfer(mount_pin_fillet, mount_pin_fillet)

    mount_pin_points=mirror(mount_pin_points)
    arc_points=mirror(arc_points)

    mount_pin2 = cq.Workplane("XZ").workplane(offset=-mount_back)\
        .moveTo(*mount_pin_points[0]).lineTo(*mount_pin_points[1])\
        .lineTo(*mount_pin_points[2]).threePointArc(arc_points[0],mount_pin_points[3])\
        .lineTo(*mount_pin_points[4]).threePointArc(arc_points[1],mount_pin_points[5])\
        .lineTo(*mount_pin_points[6]).lineTo(*mount_pin_points[7])\
        .lineTo(*mount_pin_points[8]).threePointArc(arc_points[2],mount_pin_points[9])\
        .lineTo(*mount_pin_points[10]).threePointArc(arc_points[3],mount_pin_points[11])\
        .close().extrude(mount_pin_width)
    #mount_pin2 = mount_pin2.faces("<X").edges("|Z").fillet(mount_pin_fillet)
    mount_pin2 = mount_pin2.faces(">Y").edges("<X")\
        .chamfer(mount_pin_fillet, mount_pin_fillet)
    mount_pin2 = mount_pin2.faces("<Y").edges("<X")\
        .chamfer(mount_pin_fillet, mount_pin_fillet)

    pins = pins.union(mount_pin1)
    pins = pins.union(mount_pin2)
    return pins



def generate_body(params):
    body_len = params.body_length
    body_front_cutout_len = params.body_front_cutout_len
    num_pins = params.num_pins
    first_pin_center_x = (num_pins-1)/2.0*pin_pitch

    body = cq.Workplane("XY").workplane()\
        .moveTo(0, body_center_y).rect(body_len, body_width)\
            .extrude(body_height)
    body = body.faces("<Z").workplane()\
        .rect(body_len-2*body_support_width,body_width)\
        .cutBlind(-body_main_z)

    front_face = -body_center_y+body_width/2
    cutout = cq.Workplane("XZ").workplane(offset=front_face)\
        .moveTo(0,body_height-body_cutout_depth/2.0+(body_top_width-body_bottom_width)/2.0)\
        .rect(body_len-2*body_side_width, body_cutout_h)\
        .extrude(-body_cutout_depth)
    body=body.cut(cutout)

    cutout = cq.Workplane("XZ").workplane(offset=front_face)\
        .moveTo(0, body_height-body_top_width/2.0)\
        .rect(body_len,body_top_width)\
        .extrude(-body_top_cutout1_depth)\
        .faces(">Y").workplane().rect(body_front_cutout_len,body_top_width)\
        .extrude(body_top_cutout2_depth)
    body=body.cut(cutout)


    BS = cq.selectors.BoxSelector
    body = body.edges(BS(
        (-body_len/2.0+body_side_width/2.0,
         -front_face-0.1,
         body_height),
        (body_len/2.0-body_side_width/2.0,
         -front_face+0.1,
         (body_bottom_width-body_main_z)/2),True))\
         .chamfer(body_front_chamfer)



    back_cutout_center_x = 0
    if num_pins > 3:
        back_cutout_center_x = body_len/2-back_cutout_center_to_side

    back_cutout = cq.Workplane("XY").workplane(body_main_z)\
        .moveTo(back_cutout_center_x-back_cutout_t_width/2,-front_face)\
        .hLine(back_cutout_t_width).vLine(back_cutout_t_height)\
        .hLine((back_cutout_b_width-back_cutout_t_width)/2.0)\
        .vLine(back_cutout_b_height).hLine(-back_cutout_b_width)\
        .vLine(-back_cutout_b_height)\
        .hLine((back_cutout_b_width-back_cutout_t_width)/2.0)\
        .close().extrude(body_bottom_width-body_main_z)

    if num_pins > 3:
        back_cutout = back_cutout.union(back_cutout.translate((-body_len+2*back_cutout_center_to_side,0,0)))
    body = body.cut(back_cutout)

    sp=(body_len/2.0,mount_pin_thickness)
    poly_points=[v_add(sp,(mount_holder_len-mount_holder_chamfer,0))]
    add_p_to_chain(poly_points,(mount_holder_chamfer,mount_holder_chamfer))
    add_p_to_chain(poly_points, (0,mount_holder_top_z-mount_holder_chamfer-mount_pin_thickness))
    add_p_to_chain(poly_points, (-mount_holder_len+mount_holder_chamfer,0))
    add_p_to_chain(poly_points, (-mount_holder_chamfer,mount_holder_chamfer))
    mount_holder1 = cq.Workplane("XZ").workplane(-mount_back)\
        .moveTo(*sp)\
        .polyline(poly_points).close().extrude(mount_holder_width)

    poly_points=mirror(poly_points)
    mount_holder2 = cq.Workplane("XZ").workplane(-mount_back)\
        .moveTo(-sp[0],sp[1])\
        .polyline(poly_points).close().extrude(mount_holder_width)


    poly_points=[v_add(sp,(mount_pin_thickness,0))]
    add_p_to_chain(poly_points, (0,mount_pin_height-mount_pin_bend_radius-mount_pin_thickness-mount_pin_thickness))
    add_p_to_chain(poly_points,(mount_pin_bend_radius,mount_pin_bend_radius))
    add_p_to_chain(poly_points, (mount_pin_top_len-mount_pin_bend_radius-mount_pin_thickness,0))
    add_p_to_chain(poly_points, (0, mount_pin_thickness))
    add_p_to_chain(poly_points, (-mount_pin_top_len,0))
    mount_holder1_cutout = cq.Workplane("XZ").workplane(-mount_back)\
       .moveTo(*sp).polyline(poly_points).close().extrude(mount_pin_width)

    poly_points=mirror(poly_points)
    mount_holder2_cutout = cq.Workplane("XZ").workplane(-mount_back)\
        .moveTo(-sp[0],sp[1])\
        .polyline(poly_points).close().extrude(mount_pin_width)


    body = body.union(mount_holder1)
    body = body.union(mount_holder2)
    body = body.cut(mount_holder1_cutout)
    body = body.cut(mount_holder2_cutout)
    first_cutout_x = (num_pins-1)/2.0*pin_pitch+pin_pitch
    top_cutout = cq.Workplane("XY").workplane(offset=body_height)\
        .moveTo(first_cutout_x, -front_face+body_width-top_cutout_width/2.0)\
        .rect(top_cutout_len,top_cutout_width).extrude(-top_cutout_depth)
    top_cutouts = top_cutout
    for i in range(0,num_pins+2):
        top_cutouts=top_cutouts.union(top_cutout.translate((-i*pin_pitch,0,0)))
    body = body.cut(top_cutouts)
    return body


def generate_part(pincount):
    params = make_params(pincount)
    pins = generate_pins(params)
    body = generate_body(params)
    # pins = pins.translate((0, y_origin_from_mountpad, 0))
    # body = body.translate((0, y_origin_from_mountpad, 0))
    return (body, pins)


#opend from within freecad
if "module" in __name__ :
    part_to_build = 17
    #part_to_build = 4
    FreeCAD.Console.PrintMessage("Started from cadquery: Building " +str(part_to_build)+"\n")
    (body, pins) = generate_part(part_to_build)
    show(pins)
    show(body)

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

__title__ = "model description for Molex 53398 Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for Molex 53398 Connectors using cadquery'

___ver___ = "1.0 10/04/2016"


import cadquery as cq
from math import sqrt
from Helpers import show
from collections import namedtuple
import FreeCAD

#global parameter
pin_width = 0.32
pin_pitch = 1.25
pin_protrution = 0.5
pin_contact_len = 0.6
pin_front_height = 0.45
pin_slope_len = 0.3 #estimated
pin_back_z = 0.3 #Measured
pin_len = 3.9 #Measured
center_pin_pad_y = 2.75
pin_center_offset = 0.05 # estimated
pin_tip_y = center_pin_pad_y + pin_center_offset + pin_contact_len/2.0
pin_tip_chamfer = 0.1


contact_to_front = 2.175
contact_len = 0.6 #Measured (+/-0.1 at least)
contact_top_z = 3.9 #Measured (+/-0.1 at least)
contact_chamfer_len = 0.1 #estimated
contact_chamfer_width = 0.05 #estimated
contact_chamfer_depth = 0.5 #estimated

body_width = 3.7
body_back_width = 0.4
body_side_width = 0.6
body_main_z = 0.3 #Measured
body_pin_cutout_depth = 0.5 #Measured
body_pin_cutout_len = 0.9 #Measured
body_front_plastic_protution = 0.2 # estimated
body_center_y = -pin_tip_y+pin_protrution+body_width/2
body_support_width = 0.5
body_cutout_depth = 3
body_front_cutout_depth = 1 #Measured (+/-0.1 at least)
body_top_chamfer=0.2 #estimated

body_cutout_width = 2.4

connector_height = 4.7

mount_pin_prodrution = 1.7
mount_pin_lenght = 1.48
mount_pin_width = 2.2
mount_pin_thickness = 0.25
mount_pin_bend_radius = 0.1 #estimated
mount_pin_height = 1.6 #Measured
mount_pin_top_len = 0.8 #Measured
mount_pin_fillet = 0.3

back_cutout_center_to_side = 2 #Measured
back_cutout_b_height = 1.15
back_cutout_b_width = 1.15
back_cutout_t_height = 1.45
back_cutout_t_width = 0.3 #Measured (+/-0.1 at least)

mount_holder_len = 1.75
mount_holder_width = 2.8
mount_holder_top_z = 2.65 #Measured
mount_holder_chamfer = 0.5 #Measured (+/-0.1 at least)

def v_add(p1, p2):
    return (p1[0]+p2[0],p1[1]+p2[1])

def v_sub(p1, p2):
    return (p1[0]-p2[0],p1[1]-p2[1])
#v_add(pcs2, (-body_cutout_radius*(1-1/sqrt(2)), -1/sqrt(2)*body_cutout_radius))
def get_third_arc_point1(starting_point, end_point):
    px = v_sub(end_point, starting_point)
    #FreeCAD.Console.PrintMessage("("+str(px[0])+","+str(px[1])+")")
    return v_add((px[0]*(1-1/sqrt(2)),px[1]*(1/sqrt(2))),starting_point)

def get_third_arc_point2(starting_point, end_point):
    px = v_sub(end_point, starting_point)
    #FreeCAD.Console.PrintMessage("("+str(px[0])+","+str(px[1])+")")
    return v_add((px[0]*(1/sqrt(2)),px[1]*(1-1/sqrt(2))),starting_point)

def add_p_to_chain(chain, rel_point):
    chain.append(v_add(chain[len(chain)-1], rel_point))

def mirror(chain):
    result = []
    for point in chain:
        result.append((point[0]*-1,point[1]))
    return result

def poline(points, plane):
    sp = points.pop()
    plane=plane.moveTo(sp[0],sp[1])
    plane=plane.polyline(points)
    return plane

Params = namedtuple("Params",[
    'file_name',
    'num_pins',
    'model_name',
    'body_length',
    'body_front_cutout_len'
])

def make_params(num_pins, name):
    bl=3+(num_pins-1)*pin_pitch
    return Params(
        num_pins=num_pins,
        model_name=name,
        body_length=bl,
        file_name="Molex_PicoBlade_53398-"+ ('%02d' % num_pins) +"71_" + ('%02d' % num_pins) + "x" + ('%.2f' % pin_pitch) +"mm_Straight",
        body_front_cutout_len=bl-1.9
    )

all_params = {
    "0271" : make_params( 2, 'Molex_53398_0271'),
    "0371" : make_params( 3, 'Molex_53398_0371'),
    "0471" : make_params( 4, 'Molex_53398_0471'),
    "0571" : make_params( 5, 'Molex_53398_0571'),
    "0671" : make_params( 6, 'Molex_53398_0671'),
    "0771" : make_params( 7, 'Molex_53398_0771'),
    "0871" : make_params( 8, 'Molex_53398_0871'),
    "0971" : make_params( 9, 'Molex_53398_0971'),
    "1071" : make_params(10, 'Molex_53398_1071'),
    "1171" : make_params(11, 'Molex_53398_1171'),
    "1271" : make_params(12, 'Molex_53398_1271'),
    "1371" : make_params(13, 'Molex_53398_1371'),
    "1471" : make_params(14, 'Molex_53398_1471'),
    "1571" : make_params(15, 'Molex_53398_1571')
}

def union_all(objects):
    o = objects[0]
    for i in range(1,len(objects)):
        o = o.union(objects[i])
    return o


def generate_pins(params):
    num_pins = params.num_pins
    body_len = params.body_length

    first_pin_wp_offset = (num_pins-1)/2.0*pin_pitch-pin_width/2.0

    pin = cq.Workplane("YZ").workplane(offset=first_pin_wp_offset)\
        .moveTo(pin_tip_y,0)\
        .vLine(pin_front_height).hLine(-pin_protrution)\
        .line(-pin_slope_len,body_main_z+body_pin_cutout_depth-pin_front_height)\
        .hLine(-contact_to_front+pin_slope_len).vLineTo(contact_top_z)\
        .hLine(-contact_len).vLineTo(body_main_z+body_pin_cutout_depth)\
        .hLineTo(-pin_len+pin_tip_y).vLineTo(pin_back_z)\
        .hLineTo(pin_tip_y-pin_contact_len-pin_slope_len)\
        .lineTo(center_pin_pad_y-pin_contact_len/2,0)\
        .close().extrude(pin_width)

    pin = pin.faces(">Z").edges("<Y")\
        .chamfer(contact_chamfer_len, contact_chamfer_depth)
    pin = pin.faces(">Z").edges(">Y")\
        .chamfer(contact_chamfer_len, contact_chamfer_depth)
    pin = pin.faces(">Z").edges(">X")\
        .chamfer(contact_chamfer_width, contact_chamfer_depth)
    pin = pin.faces(">Z").edges("<X")\
        .chamfer(contact_chamfer_width, contact_chamfer_depth)
    pin = pin.faces(">Y").edges("|X")\
        .chamfer(pin_tip_chamfer)
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

    mount_pin1 = cq.Workplane("XZ").workplane(offset=-mount_pin_width/2)\
        .moveTo(*mount_pin_points[0]).lineTo(*mount_pin_points[1])\
        .lineTo(*mount_pin_points[2]).threePointArc(arc_points[0],mount_pin_points[3])\
        .lineTo(*mount_pin_points[4]).threePointArc(arc_points[1],mount_pin_points[5])\
        .lineTo(*mount_pin_points[6]).lineTo(*mount_pin_points[7])\
        .lineTo(*mount_pin_points[8]).threePointArc(arc_points[2],mount_pin_points[9])\
        .lineTo(*mount_pin_points[10]).threePointArc(arc_points[3],mount_pin_points[11])\
        .close().extrude(mount_pin_width)

    mount_pin1 = mount_pin1.faces(">X").edges("|Z").fillet(mount_pin_fillet)

    mount_pin_points=mirror(mount_pin_points)
    arc_points=mirror(arc_points)

    mount_pin2 = cq.Workplane("XZ").workplane(offset=-mount_pin_width/2)\
        .moveTo(*mount_pin_points[0]).lineTo(*mount_pin_points[1])\
        .lineTo(*mount_pin_points[2]).threePointArc(arc_points[0],mount_pin_points[3])\
        .lineTo(*mount_pin_points[4]).threePointArc(arc_points[1],mount_pin_points[5])\
        .lineTo(*mount_pin_points[6]).lineTo(*mount_pin_points[7])\
        .lineTo(*mount_pin_points[8]).threePointArc(arc_points[2],mount_pin_points[9])\
        .lineTo(*mount_pin_points[10]).threePointArc(arc_points[3],mount_pin_points[11])\
        .close().extrude(mount_pin_width)
    mount_pin2 = mount_pin2.faces("<X").edges("|Z").fillet(mount_pin_fillet)

    pins = pins.union(mount_pin1)
    pins = pins.union(mount_pin2)
    return pins



def generate_body(params):
    body_len = params.body_length
    body_front_cutout_len = params.body_front_cutout_len
    num_pins = params.num_pins
    first_pin_center_x = (num_pins-1)/2.0*pin_pitch

    body = cq.Workplane("XY").workplane()\
        .moveTo(0, -body_center_y).rect(body_len, body_width)\
            .extrude(connector_height)
    body = body.faces("<Z").workplane()\
        .rect(body_len-2*body_support_width,body_width)\
        .cutBlind(-body_main_z)
    pin_cutout = cq.Workplane("XY").workplane(offset=body_main_z)\
        .moveTo(first_pin_center_x,-body_center_y)\
        .rect(body_pin_cutout_len,body_width)\
        .extrude(body_pin_cutout_depth)
    pin_cutouts = pin_cutout
    for i in range(0,num_pins):
        pin_cutouts=pin_cutouts.union(pin_cutout.translate((-i*pin_pitch,0,0)))
    body = body.cut(pin_cutouts)

    front_thicknes = body_width-body_cutout_width-body_back_width-body_front_plastic_protution
    body = body.faces(">Z").workplane()\
        .moveTo(-body_len/2.0+body_side_width, -body_width/2.0+body_back_width)\
        .hLine(body_len-2*body_side_width)\
        .vLine(body_cutout_width).hLineTo(body_front_cutout_len/2.0)\
        .vLineTo(body_width/2-body_front_plastic_protution)\
        .hLineTo(body_len/2.0).vLineTo(body_width/2.0).hLine(-body_len)\
        .vLine(-body_front_plastic_protution)\
        .hLineTo(-body_front_cutout_len/2.0)\
        .vLine(-front_thicknes).hLineTo(-body_len/2.0+body_side_width)\
        .close().cutBlind(-body_cutout_depth)

    body_front_cutout = cq.Workplane("XY").workplane(offset=connector_height)\
        .moveTo(0,-body_center_y+body_width/2.0-body_front_plastic_protution-front_thicknes/2.0)\
        .rect(body_len,front_thicknes).extrude(-body_front_cutout_depth)
    body = body.cut(body_front_cutout)

    BS = cq.selectors.BoxSelector
    body = body.edges(BS(
        (-body_len/2.0+body_side_width/2.0,
         -body_center_y+body_width/2.0,
         connector_height-0.3),
        (body_len/2.0-body_side_width/2.0,
         -body_center_y-body_width/2.0+body_back_width/2.0,
         connector_height+1),True))\
         .chamfer(body_top_chamfer)

    back_y = body_center_y+body_width/2

    back_cutout_center_x = 0
    if num_pins > 3:
        back_cutout_center_x = body_len/2-back_cutout_center_to_side

    back_cutout = cq.Workplane("XZ").workplane(back_y)\
        .moveTo(back_cutout_center_x-back_cutout_t_width/2,connector_height)\
        .hLine(back_cutout_t_width).vLine(-back_cutout_t_height)\
        .hLine((back_cutout_b_width-back_cutout_t_width)/2.0)\
        .vLine(-back_cutout_b_height).hLine(-back_cutout_b_width)\
        .vLine(back_cutout_b_height)\
        .hLine((back_cutout_b_width-back_cutout_t_width)/2.0)\
        .close().extrude(-body_back_width)

    if num_pins > 3:
        back_cutout = back_cutout.union(back_cutout.translate((-body_len+2*back_cutout_center_to_side,0,0)))
    body = body.cut(back_cutout)

    sp=(body_len/2.0,body_main_z)
    poly_points=[v_add(sp,(mount_holder_len-mount_holder_chamfer,0))]
    add_p_to_chain(poly_points,(mount_holder_chamfer,mount_holder_chamfer))
    add_p_to_chain(poly_points, (0,mount_holder_top_z-mount_holder_chamfer-body_main_z))
    add_p_to_chain(poly_points, (-mount_holder_len,0))
    mount_holder1 = cq.Workplane("XZ").workplane(back_y)\
        .moveTo(*sp)\
        .polyline(poly_points).close().extrude(-mount_holder_width)

    poly_points=mirror(poly_points)
    mount_holder2 = cq.Workplane("XZ").workplane(back_y)\
        .moveTo(-sp[0],sp[1])\
        .polyline(poly_points).close().extrude(-mount_holder_width)


    poly_points=[v_add(sp,(mount_pin_thickness,0))]
    add_p_to_chain(poly_points, (0,mount_pin_height-mount_pin_bend_radius-mount_pin_thickness-body_main_z))
    add_p_to_chain(poly_points,(mount_pin_bend_radius,mount_pin_bend_radius))
    add_p_to_chain(poly_points, (mount_pin_top_len-mount_pin_bend_radius-mount_pin_thickness,0))
    add_p_to_chain(poly_points, (0, mount_pin_thickness))
    add_p_to_chain(poly_points, (-mount_pin_top_len,0))
    mount_holder1_cutout = cq.Workplane("XZ").workplane(back_y)\
       .moveTo(*sp).polyline(poly_points).close().extrude(-mount_pin_width)

    poly_points=mirror(poly_points)
    mount_holder2_cutout = cq.Workplane("XZ").workplane(back_y)\
        .moveTo(-sp[0],sp[1])\
        .polyline(poly_points).close().extrude(-mount_pin_width)


    body = body.union(mount_holder1)
    body = body.union(mount_holder2)
    body = body.cut(mount_holder1_cutout)
    body = body.cut(mount_holder2_cutout)
    return body


def generate_part(part_key):
    pins = generate_pins(all_params[part_key])
    body = generate_body(all_params[part_key])
    return (pins, body)


#opend from within freecad
if "module" in __name__ :
    #part_to_build = "0271"
    part_to_build = "0471"
    FreeCAD.Console.PrintMessage("Started from cadquery: Building " +part_to_build+"\n")
    (pins, body) = generate_part(part_to_build)
    show(pins)
    show(body)

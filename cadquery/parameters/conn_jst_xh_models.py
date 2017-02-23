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

__title__ = "model description for JST-XH Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for JST-XH Connectors using cadquery'

___ver___ = "1.1 10/04/2016"


import cadquery as cq
from math import sqrt
from Helpers import show
from collections import namedtuple
import FreeCAD

#global parameter
pin_width = 0.64
pin_depth = 3.4
pin_inner_lenght = 6.5
pin_lock_h1 = 1.9
pin_lock_h2 = 2.5
pin_lock_d = 0.3
pin_fillet = 0.2
pin_bend_radius = 0.05
pin_pitch = 2.5
body_corner_x = -2.45
body_corner_y = -2.35


def v_add(p1, p2):
    return (p1[0]+p2[0],p1[1]+p2[1])

def v_sub(p1, p2):
    return (p1[0]-p2[0],p1[1]-p2[1])
#v_add(pcs2, (-body_cutout_radius*(1-1/sqrt(2)), -1/sqrt(2)*body_cutout_radius))
def get_third_arc_point(starting_point, end_point):
    px = v_sub(end_point, starting_point)
    #FreeCAD.Console.PrintMessage("("+str(px[0])+","+str(px[1])+")")
    return v_add((px[0]*(1-1/sqrt(2)),px[1]*(1/sqrt(2))),starting_point)

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
    'angled',
    'num_pins',
    'model_name',
    'pin_angle_distance',
    'pin_angle_length',
    'body_width',
    'body_height',
    'body_length',
    'zdistance'
])

def make_params_angled(num_pins, name, file_name):
    return Params(
        angled=True,
        num_pins=num_pins,
        model_name=name,
        pin_angle_distance=9.2-7,
        pin_angle_length=9.2,
        body_width=5.75,
        body_height=7.0,
        body_length=2*2.45+(num_pins-1)*pin_pitch,
        zdistance=6.1-5.75,
        file_name=file_name
    )
def make_params_angled_short(num_pins, name, file_name):
    return Params(
        angled=True,
        num_pins=num_pins,
        model_name=name,
        pin_angle_distance=7.6-7,
        pin_angle_length=7.6,
        body_width=5.75,
        body_height=7.0,
        body_length=2*2.45+(num_pins-1)*pin_pitch,
        zdistance=6.1-5.75,
        file_name=file_name
    )
def make_params_straight(num_pins, name, file_name):
    return Params(
        angled=False,
        num_pins=num_pins,
        model_name=name,
        pin_angle_distance=0,
        pin_angle_length=0,
        body_width=5.75,
        body_height=7.0,
        body_length=2*2.45+(num_pins-1)*pin_pitch,
        zdistance=6.1-5.75,
        file_name=file_name
    )

all_params = {
    "B02B_XH_A" : make_params_straight( 2, 'B02B_XH_A', 'JST_XH_B02B-XH-A_02x2.50mm_Straight'),
    "B03B_XH_A" : make_params_straight( 3, 'B03B_XH_A', 'JST_XH_B03B-XH-A_03x2.50mm_Straight'),
    "B04B_XH_A" : make_params_straight( 4, 'B04B_XH_A', 'JST_XH_B04B-XH-A_04x2.50mm_Straight'),
    "B05B_XH_A" : make_params_straight( 5, 'B05B_XH_A', 'JST_XH_B05B-XH-A_05x2.50mm_Straight'),
    "B06B_XH_A" : make_params_straight( 6, 'B06B_XH_A', 'JST_XH_B06B-XH-A_06x2.50mm_Straight'),
    "B07B_XH_A" : make_params_straight( 7, 'B07B_XH_A', 'JST_XH_B07B-XH-A_07x2.50mm_Straight'),
    "B08B_XH_A" : make_params_straight( 8, 'B08B_XH_A', 'JST_XH_B08B-XH-A_08x2.50mm_Straight'),
    "B09B_XH_A" : make_params_straight( 9, 'B09B_XH_A', 'JST_XH_B09B-XH-A_09x2.50mm_Straight'),
    "B10B_XH_A" : make_params_straight(10, 'B10B_XH_A', 'JST_XH_B10B-XH-A_10x2.50mm_Straight'),
    "B11B_XH_A" : make_params_straight(11, 'B11B_XH_A', 'JST_XH_B11B-XH-A_11x2.50mm_Straight'),
    "B12B_XH_A" : make_params_straight(12, 'B12B_XH_A', 'JST_XH_B12B-XH-A_12x2.50mm_Straight'),
    "B13B_XH_A" : make_params_straight(13, 'B13B_XH_A', 'JST_XH_B13B-XH-A_13x2.50mm_Straight'),
    "B14B_XH_A" : make_params_straight(14, 'B14B_XH_A', 'JST_XH_B14B-XH-A_14x2.50mm_Straight'),
    "B15B_XH_A" : make_params_straight(15, 'B15B_XH_A', 'JST_XH_B15B-XH-A_15x2.50mm_Straight'),
    "B16B_XH_A" : make_params_straight(16, 'B16B_XH_A', 'JST_XH_B16B-XH-A_16x2.50mm_Straight'),
    "B20B_XH_A" : make_params_straight(20, 'B20B_XH_A', 'JST_XH_B20B-XH-A_20x2.50mm_Straight'),
    "S02B_XH_A" : make_params_angled( 2, 'S02B_XH_A', 'JST_XH_S02B-XH-A_02x2.50mm_Angled'),
    "S03B_XH_A" : make_params_angled( 3, 'S03B_XH_A', 'JST_XH_S03B-XH-A_03x2.50mm_Angled'),
    "S04B_XH_A" : make_params_angled( 4, 'S04B_XH_A', 'JST_XH_S04B-XH-A_04x2.50mm_Angled'),
    "S05B_XH_A" : make_params_angled( 5, 'S05B_XH_A', 'JST_XH_S05B-XH-A_05x2.50mm_Angled'),
    "S06B_XH_A" : make_params_angled( 6, 'S06B_XH_A', 'JST_XH_S06B-XH-A_06x2.50mm_Angled'),
    "S07B_XH_A" : make_params_angled( 7, 'S07B_XH_A', 'JST_XH_S07B-XH-A_07x2.50mm_Angled'),
    "S08B_XH_A" : make_params_angled( 8, 'S08B_XH_A', 'JST_XH_S08B-XH-A_08x2.50mm_Angled'),
    "S09B_XH_A" : make_params_angled( 9, 'S09B_XH_A', 'JST_XH_S09B-XH-A_09x2.50mm_Angled'),
    "S10B_XH_A" : make_params_angled(10, 'S10B_XH_A', 'JST_XH_S10B-XH-A_10x2.50mm_Angled'),
    "S11B_XH_A" : make_params_angled(11, 'S11B_XH_A', 'JST_XH_S11B-XH-A_11x2.50mm_Angled'),
    "S12B_XH_A" : make_params_angled(12, 'S12B_XH_A', 'JST_XH_S12B-XH-A_12x2.50mm_Angled'),
    "S13B_XH_A" : make_params_angled(13, 'S13B_XH_A', 'JST_XH_S13B-XH-A_13x2.50mm_Angled'),
    "S14B_XH_A" : make_params_angled(14, 'S14B_XH_A', 'JST_XH_S14B-XH-A_14x2.50mm_Angled'),
    "S15B_XH_A" : make_params_angled(15, 'S15B_XH_A', 'JST_XH_S15B-XH-A_15x2.50mm_Angled'),
    "S16B_XH_A" : make_params_angled(16, 'S16B_XH_A', 'JST_XH_S16B-XH-A_16x2.50mm_Angled'),
    "S03B_XH_A_1" : make_params_angled_short( 3, 'S03B_XH_A_1', 'JST_XH_S03B-XH-A-1_03x2.50mm_Angled_compact'),
    "S04B_XH_A_1" : make_params_angled_short( 4, 'S04B_XH_A_1', 'JST_XH_S04B-XH-A-1_04x2.50mm_Angled_compact'),
    "S05B_XH_A_1" : make_params_angled_short( 5, 'S05B_XH_A_1', 'JST_XH_S05B-XH-A-1_05x2.50mm_Angled_compact'),
    "S06B_XH_A_1" : make_params_angled_short( 6, 'S06B_XH_A_1', 'JST_XH_S06B-XH-A-1_06x2.50mm_Angled_compact'),
    "S07B_XH_A_1" : make_params_angled_short( 7, 'S07B_XH_A_1', 'JST_XH_S07B-XH-A-1_07x2.50mm_Angled_compact'),
    "S08B_XH_A_1" : make_params_angled_short( 8, 'S08B_XH_A_1', 'JST_XH_S08B-XH-A-1_08x2.50mm_Angled_compact'),
    "S09B_XH_A_1" : make_params_angled_short( 9, 'S09B_XH_A_1', 'JST_XH_S09B-XH-A-1_09x2.50mm_Angled_compact'),
    "S10B_XH_A_1" : make_params_angled_short(10, 'S10B_XH_A_1', 'JST_XH_S10B-XH-A-1_10x2.50mm_Angled_compact'),
    "S11B_XH_A_1" : make_params_angled_short(11, 'S11B_XH_A_1', 'JST_XH_S11B-XH-A-1_11x2.50mm_Angled_compact'),
    "S12B_XH_A_1" : make_params_angled_short(12, 'S12B_XH_A_1', 'JST_XH_S12B-XH-A-1_12x2.50mm_Angled_compact'),
    "S13B_XH_A_1" : make_params_angled_short(13, 'S13B_XH_A_1', 'JST_XH_S13B-XH-A-1_13x2.50mm_Angled_compact'),
    "S14B_XH_A_1" : make_params_angled_short(14, 'S14B_XH_A_1', 'JST_XH_S14B-XH-A-1_14x2.50mm_Angled_compact'),
    "S15B_XH_A_1" : make_params_angled_short(15, 'S15B_XH_A_1', 'JST_XH_S15B-XH-A-1_15x2.50mm_Angled_compact')
}

def union_all(objects):
    o = objects[0]
    for i in range(1,len(objects)):
        o = o.union(objects[i])
    return o


def generate_pins(params):
    if params.angled:
        return generate_angled_pins(params)
    return generate_straight_pins(params)

def generate_straight_pins(params):
    num_pins = params.num_pins

    pl = [
        (pin_width/2, -pin_depth),
        (pin_width/2-pin_lock_d, pin_lock_h1-pin_depth),
        (pin_width/2, pin_lock_h2-pin_depth),
        (pin_width/2, pin_inner_lenght),
        (-pin_width/2, pin_inner_lenght),
        (-pin_width/2, pin_lock_h2-pin_depth),
        (-pin_width/2-pin_lock_d, pin_lock_h1-pin_depth)
        ]

    locked_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
        .move(-pin_width/2, -pin_depth)\
        .polyline(pl).close().extrude(pin_width)
    locked_pin = locked_pin.faces("|Z").edges().chamfer(pin_fillet)

    pins = locked_pin.union(locked_pin.translate(((num_pins-1)*pin_pitch,0,0)))

    pli = [
        (pin_width/2, -pin_depth),
        (pin_width/2, pin_inner_lenght),
        (-pin_width/2, pin_inner_lenght),
        ]
    normal_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
        .move(-pin_width/2, -pin_depth)\
        .polyline(pli).close().extrude(pin_width)
    normal_pin = normal_pin.faces("|Z").edges().chamfer(pin_fillet)

    for i in range(1,num_pins-1):
        pins = pins.union(normal_pin.translate((i*pin_pitch,0,0)))
    return pins

def generate_angled_pins(params):
    num_pins = params.num_pins
    pin_angle_length = params.pin_angle_length
    zdistance = params.zdistance
    body_width = params.body_width

    pin_z_distance = body_width + body_corner_y + zdistance

    pl = [
        (pin_width/2, -pin_depth),
        (pin_width/2+pin_lock_d, pin_lock_h1-pin_depth),
        (pin_width/2, pin_lock_h2-pin_depth),
        (pin_width/2, pin_z_distance-pin_width/2),
        (pin_angle_length-0.5, pin_z_distance-pin_width/2),
        (pin_angle_length-0.5, pin_z_distance+pin_width/2),
        (-pin_width/2, pin_z_distance+pin_width/2),
        (-pin_width/2, pin_lock_h2-pin_depth),
        (-pin_width/2+pin_lock_d, pin_lock_h1-pin_depth)
        ]

    locked_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
        .move(-pin_width/2, -pin_depth)\
        .polyline(pl).close().extrude(pin_width)
    locked_pin = locked_pin.faces("<Z").edges().chamfer(pin_fillet)
    locked_pin = locked_pin.faces(">Y").edges().chamfer(pin_fillet)
    BS = cq.selectors.BoxSelector
    p1 = (-0.01, pin_width/2-0.01, pin_z_distance-pin_width/2-0.01)
    p2 = (0.01, pin_width/2+0.01, pin_z_distance-pin_width/2+0.01)
    locked_pin = locked_pin.edges(BS(p1, p2)).fillet(pin_bend_radius)
    locked_pin = locked_pin.faces(">Z").edges("<Y")\
        .fillet(pin_bend_radius+pin_width)

    pins = locked_pin.union(locked_pin.translate(((num_pins-1)*pin_pitch,0,0)))

    pli = [
        (pin_width/2, -pin_depth),
        (pin_width/2, pin_z_distance-pin_width/2),
        (pin_angle_length-0.5, pin_z_distance-pin_width/2),
        (pin_angle_length-0.5, pin_z_distance+pin_width/2),
        (-pin_width/2, pin_z_distance+pin_width/2),
        ]
    normal_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
        .move(-pin_width/2, -pin_depth)\
        .polyline(pli).close().extrude(pin_width)
    normal_pin = normal_pin.faces("<Z").edges().chamfer(pin_fillet)
    normal_pin = normal_pin.faces(">Y").edges().chamfer(pin_fillet)
    normal_pin = normal_pin.edges(BS(p1, p2)).fillet(pin_bend_radius)
    normal_pin = normal_pin.faces(">Z").edges("<Y")\
        .fillet(pin_bend_radius+pin_width)


    for i in range(1,num_pins-1):
        pins = pins.union(normal_pin.translate((i*pin_pitch,0,0)))
    return pins

def generate_angled_body(params):
    body_width = params.body_width
    body_height = params.body_height
    body_lenght = params.body_length
    zdistance = params.zdistance
    d = params.pin_angle_distance

    body_fin_lenght = 11.5-body_height
    body_fin_width = 0.5
    body_fin_height = 5
    body_fin_back_height = 2.5

    body = generate_straight_body(params)
    body = body.rotate((0,body_width+body_corner_y,0),(1,0,0),-90)
    body = body.translate((0,-(body_width+body_corner_y)+d,zdistance))

    fin = cq.Workplane("YZ").workplane(offset=body_corner_x)\
        .moveTo(d,zdistance).vLine(body_fin_height)\
        .line(-body_fin_lenght,-body_fin_height+body_fin_back_height)\
        .vLineTo(0).hLine(body_fin_lenght+body_height)\
        .vLine(zdistance).close().extrude(body_fin_width)
    body=body.union(fin)
    body=body.union(fin.translate((body_lenght-body_fin_width,0,0)))

    return body.union(fin)

def generate_body(params):
    if not params.angled:
        return generate_straight_body(params)
    return generate_angled_body(params)

def generate_straight_body(params):
    num_pins = params.num_pins
    body_width = params.body_width
    body_height = params.body_height
    body_length = params.body_length
    body_plug_depth = 5.15

    body_front_width = 0.85
    body_side_width = 0.85
    body_back_width = 0.75

    body_cutout_radius = 0.5
    body_side_cutout_depth = 3.35
    body_side_cutout_width = 1
    body_front_cutout_depth = 3.9

    body_off_center_y = (body_front_width-body_back_width)/2

    body = cq.Workplane("XY").workplane()\
        .move(body_corner_x, body_corner_y)\
        .rect(body_length, body_width, centered=False)\
        .extrude(body_height)
    body = body.faces(">Z").workplane().move(0,body_off_center_y)\
        .rect(body_length-2*body_side_width, body_width-body_front_width-body_back_width)\
        .cutBlind(-body_plug_depth)

    pcs1 = (body_width/2-body_front_width, body_height/2)
    pcs2 = v_add(pcs1, (0, -body_side_cutout_depth+body_cutout_radius))
    pcs3 = v_add(pcs2, (-body_cutout_radius, -body_cutout_radius))
    pcsam = get_third_arc_point(pcs2, pcs3)

    body = body.faces("<X").workplane()\
        .moveTo(pcs1[0], pcs1[1])\
        .lineTo(pcs2[0], pcs2[1])\
        .threePointArc(pcsam, pcs3)\
        .line(-body_side_cutout_width+body_cutout_radius, 0)\
        .line(0, body_side_cutout_depth).close()\
        .cutThruAll()

    if(num_pins>2):
        f_cutout_distance = body_length-6.9
        body_front_cutout_width = 1.5
    else:
        f_cutout_distance = 0
        body_front_cutout_width = 3.5/2

    p_cutout_f=[(f_cutout_distance/2, body_height/2)]
    add_p_to_chain(p_cutout_f, (0, -body_front_cutout_depth))
    add_p_to_chain(p_cutout_f, (body_front_cutout_width, 0))
    add_p_to_chain(p_cutout_f, (0, 2.5))
    add_p_to_chain(p_cutout_f, (-0.25, 0.25))
    add_p_to_chain(p_cutout_f, (0.25, 0.25))
    p_cutout_f.append(v_add(p_cutout_f[0],(body_front_cutout_width,0)))

    p_cutout_f2 = mirror(p_cutout_f)
    cutout1 = body.faces("<Y").workplane()
    cutout1 = poline(p_cutout_f,cutout1)
    cutout1 = cutout1.close().extrude(-1,False)\
        .faces("<Z").edges(">X").fillet(1.5*body_cutout_radius)

    cutout2 = body.faces("<Y").workplane()
    cutout2 = poline(p_cutout_f2,cutout2)
    cutout2 = cutout2.close().extrude(-1,False)\
        .faces("<Z").edges("<X").fillet(1.5*body_cutout_radius)

    body = body.cut(cutout1.union(cutout2))
    BS = cq.selectors.BoxSelector
    body = body.edges(BS((body_corner_x+body_side_width/2+0.05,
                          0,
                          body_height-0.1),
                          (body_corner_x+body_length-body_side_width/2-0.05,
                          body_width/2,
                          body_height+0.1))).chamfer(0.2)
    bottom_cutout_width = 1.5
    bottom_cutout_depth = 1
    bottom_cutout_platou_len = 1
    bottom_cutout_platou_depth = 0.3
    bottom_cutout = cq.Workplane("YZ").workplane(offset=-bottom_cutout_width/2)\
        .moveTo(body_corner_y, 0).vLine(bottom_cutout_depth)\
        .lineTo(-bottom_cutout_platou_len/2.0,
              bottom_cutout_platou_depth)\
        .line(bottom_cutout_platou_len,0)\
        .lineTo((body_width+body_corner_y), bottom_cutout_depth)\
        .vLineTo(0).close().extrude(bottom_cutout_width)

    for i in range(0,num_pins):
        body = body.cut(bottom_cutout.translate((i*pin_pitch,0,0)))

    return body
    #return bottom_cutout

def generate_part(part_key):
    pins = generate_pins(all_params[part_key])
    body = generate_body(all_params[part_key])
    body_lenght=all_params[part_key].body_length
    #made an error, need to rotate it by 180 degree
    center_x=body_corner_x+body_lenght/2
    pins = pins.rotate((center_x,0,0),(0,0,1),180)
    body = body.rotate((center_x,0,0),(0,0,1),180)
    return (pins, body)


#opend from within freecad
if "module" in __name__ :
    part_to_build = "S02B_XH_A"
    #part_to_build = "B02B_XH_A"
    FreeCAD.Console.PrintMessage("Started from cadquery: Building " +part_to_build+"\n")
    (pins, body) = generate_part(part_to_build)
    show(pins)
    show(body)

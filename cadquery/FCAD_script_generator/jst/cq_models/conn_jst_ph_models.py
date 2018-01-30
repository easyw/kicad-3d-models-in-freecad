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

__title__ = "model description for JST-PH Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for JST-PH Connectors using cadquery. Datasheet: http://www.jst-mfg.com/product/pdf/eng/ePH.pdf'

___ver___ = "1.0 02/03/2017"
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
        if 'jst/cq_models' in path:
            p1 = path.replace('jst/cq_models','_tools')
    if not p1 in sys.path:
        sys.path.append(p1)
else:
    sys.path.append('../_tools')

from cq_helpers import *


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
from conn_jst_ph_params import *

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
    body_length = params.body_length
    zdistance = params.zdistance
    d = params.pin_angle_distance

    body_fin_lenght = 1.6
    body_fin_width = 1
    body_fin_height = 3.8
    body_fin_back_height = 2.9

    body = generate_straight_body(params)

    cutout2 = cq.Workplane("XZ").workplane(offset=-body_corner_y)\
        .moveTo(body_corner_x+body_front_cutout_from_side,
                body_height-body_front_cutout_from_top)\
        .vLineTo(0)\
        .hLine(body_front_cutout_width)\
        .vLineTo(body_height-body_front_cutout_from_top)\
        .close().extrude(-body_front_width,False)
    body = body.cut(cutout2)

    cutout3 = cq.Workplane("XZ").workplane(offset=-body_corner_y)\
        .moveTo(body_corner_x+body_length-body_front_cutout_from_side,
              body_height-body_front_cutout_from_top)\
        .vLineTo(0)\
        .hLine(-body_front_cutout_width)\
        .vLineTo(body_height-body_front_cutout_from_top)\
        .close().extrude(-body_front_width,False)
    body = body.cut(cutout3)

    body = body.rotate((0,body_width+body_corner_y,0),(1,0,0),-90)
    body = body.translate((0,-(body_width+body_corner_y)+d,zdistance))

    fin = cq.Workplane("YZ").workplane(offset=body_corner_x)\
        .moveTo(d,zdistance).vLine(body_fin_height)\
        .line(-body_fin_lenght,-body_fin_height+body_fin_back_height)\
        .vLineTo(0).hLine(body_fin_lenght+body_height)\
        .vLine(zdistance).close().extrude(body_fin_width)
    body=body.union(fin)
    body=body.union(fin.translate((body_length-body_fin_width,0,0)))

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
    body_plug_depth = 4.2

    body_side_cutout_depth = 2
    body_side_cutout_width = 0.8
    body_side_cutout_from_front = 1.5

    body_off_center_y = (body_front_width-body_back_width)/2

    body = cq.Workplane("XY").workplane()\
        .move(body_corner_x, body_corner_y)\
        .rect(body_length, body_width, centered=False)\
        .extrude(body_height)
    body = body.faces(">Z").workplane().move(0,body_off_center_y)\
        .rect(body_length-2*body_side_width, body_width-body_front_width-body_back_width)\
        .cutBlind(-body_plug_depth)

    pcs1 = (body_width/2-body_side_cutout_from_front, body_height/2)
    pcs2 = v_add(pcs1, (0, -body_side_cutout_depth+body_side_cutout_width/2))
    pcs3 = v_add(pcs2, (-body_side_cutout_width, -0))
    #pcsam = get_third_arc_point(pcs2, pcs3)
    pcsam = v_add(pcs2, (-body_side_cutout_width/2, -body_side_cutout_width/2))

    body = body.faces("<X").workplane()\
        .moveTo(pcs1[0], pcs1[1])\
        .lineTo(pcs2[0], pcs2[1])\
        .threePointArc(pcsam, pcs3)\
        .line(0, body_side_cutout_depth-body_side_cutout_width/2).close()\
        .cutThruAll()

    cutout1 = body.faces("<Y").workplane()\
        .move(-body_length/2+body_front_main_cutout_to_side,body_height/2)\
        .vLine(-body_front_main_cutout_depth)\
        .hLineTo(body_length/2-body_front_main_cutout_to_side)\
        .vLine(body_front_main_cutout_depth)\
        .close().extrude(-1,False)
    body = body.cut(cutout1)

    cutout2 = cq.Workplane("XZ").workplane(offset=-body_corner_y)\
        .moveTo(body_corner_x+body_front_cutout_from_side,
                body_height-body_front_cutout_from_top)\
        .vLine(-body_front_cutout_height)\
        .hLine(body_front_cutout_width)\
        .vLine(body_front_cutout_height)\
        .close().extrude(-1,False)
    body = body.cut(cutout2)

    cutout3 = cq.Workplane("XZ").workplane(offset=-body_corner_y)\
        .moveTo(body_corner_x+body_length-body_front_cutout_from_side,
              body_height-body_front_cutout_from_top)\
        .vLine(-body_front_cutout_height)\
        .hLine(-body_front_cutout_width)\
        .vLine(body_front_cutout_height)\
        .close().extrude(-1,False)
    body = body.cut(cutout3)

    bottom_cutout_width = 1.5
    bottom_cutout_depth = 0.2
    bottom_cutout_platou_len = 1
    bottom_cutout_platou_depth = 0.1
    bottom_cutout = cq.Workplane("YZ").workplane(offset=-bottom_cutout_width/2)\
        .moveTo(body_corner_y, 0).vLine(bottom_cutout_depth)\
        .lineTo(-bottom_cutout_platou_len/2.0,
              bottom_cutout_platou_depth)\
        .line(bottom_cutout_platou_len,0)\
        .lineTo((body_width+body_corner_y), bottom_cutout_depth)\
        .vLineTo(0).close().extrude(bottom_cutout_width)

    for i in range(0,num_pins):
        body = body.cut(bottom_cutout.translate((i*pin_pitch,0,0)))

    body_back_prodrucion_from_top = 2.3
    body_back_prodrucion_width = 0.4
    body_back_prodrucion_depth = 0.3

    body_back_prodrucion = cq.Workplane("XY")\
        .workplane(offset=body_height-body_plug_depth)\
        .moveTo(pin_pitch/2.0,
                body_corner_y + body_width -
                body_back_width - body_back_prodrucion_depth/2.0)\
        .rect(body_back_prodrucion_width, body_back_prodrucion_depth)\
        .extrude(body_plug_depth - body_back_prodrucion_from_top)
    for i in range(num_pins-1):
        body = body.union(body_back_prodrucion.translate((i*pin_pitch,0,0)))

    body_pin1_prodrucion_depth = 0.05
    body_pin1_prodrucion_width = 0.5
    body_pin1_prodrucion = cq.Workplane("XY")\
        .workplane(offset = body_height-body_front_cutout_from_top)\
        .moveTo(body_corner_x + body_length -
                body_front_cutout_width - body_pin1_prodrucion_width/2.0,
                body_corner_y - body_pin1_prodrucion_depth/2.0)\
                .rect(body_pin1_prodrucion_width, body_pin1_prodrucion_depth)\
                .extrude(body_front_cutout_from_top)
    body = body.union(body_pin1_prodrucion)

    return body
    #return bottom_cutout

def generate_part(params):
    pins = generate_pins(params)
    body = generate_body(params)
    body_lenght=params.body_length
    #made an error, need to rotate it by 180 degree
    center_x=body_corner_x+body_lenght/2
    pins = pins.rotate((center_x,0,0),(0,0,1),180)
    body = body.rotate((center_x,0,0),(0,0,1),180)
    return (body, pins)


#opend from within freecad
if "module" in __name__ :
    #params=series_params.variant_params['top_entry']['param_generator'](3)
    params=series_params.variant_params['side_entry']['param_generator'](3)

    (body, pins) = generate_part(params)
    show(pins)
    show(body)

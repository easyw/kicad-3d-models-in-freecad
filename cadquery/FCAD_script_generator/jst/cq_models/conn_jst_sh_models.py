#  -*- coding: utf8 -*-
# !/usr/bin/python
# 
#  CadQuery script returning JST SH Connectors

# # This script can be run from within the cadquery module of freecad.
# # To generate VRML/ STEP files for, use export_conn_jst_sh
# # script of the parent directory.

# * This is a cadquery script for the generation of MCAD Models.             *
# *                                                                          *
# *   Copyright (c) 2016                                                     *
# * Rene Poeschl https://github.com/poeschlr                                 *
# * All trademarks within this guide belong to their legitimate owners.      *
# *                                                                          *
# *   This program is free software; you can redistribute it and/or modify   *
# *   it under the terms of the GNU General Public License (GPL)             *
# *   as published by the Free Software Foundation; either version 2 of      *
# *   the License, or (at your option) any later version.                    *
# *   for detail see the LICENCE text file.                                  *
# *                                                                          *
# *   This program is distributed in the hope that it will be useful,        *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
# *   GNU Library General Public License for more details.                   *
# *                                                                          *
# *   You should have received a copy of the GNU Library General Public      *
# *   License along with this program; if not, write to the Free Software    *
# *   Foundation, Inc.,                                                      *
# *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           *
# *                                                                          *
# * The models generated with this script add the following exception:       *
# *   As a special exception, if you create a design which uses this symbol, *
# *   and embed this symbol or unaltered portions of this symbol into the    *
# *   design, this symbol does not by itself cause the resulting design to   *
# *   be covered by the GNU General Public License. This exception does not  *
# *   however invalidate any other reasons why the design itself might be    *
# *   covered by the GNU General Public License. If you modify this symbol,  *
# *   you may extend this exception to your version of the symbol, but you   *
# *   are not obligated to do so. If you do not wish to do so, delete this   *
# *   exception statement from your version.                                 *
# ****************************************************************************

__title__ = "model description for JST-SH Connectors"
__author__ = "benjinne"
__Comment__ = 'model description for JST-SH Connectors using cadquery'
___ver___ = "1.0 3/01/2025"


class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Frank Severinsen"
    STR_licEmail = "Frank.Severinsen@gmail.com"
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
from conn_jst_sh_params import *


def generate_pins(params):
    if params.angled:
        return generate_angled_pins(params)
    return generate_straight_pins(params)

def generate_straight_pins(params):
    num_pins = params.num_pins
    pin_distance = (num_pins-1)*pin_pitch

    mount_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
    	.move(0.3,0.02).vLine(0.6).hLine(1.0).vLine(0.65)\
        .hLine(0.5).vLine(-1.25)\
        .close().extrude(pin_width)

    signal_pin = cq.Workplane("YZ").workplane(-pin_distance/2 -pin_width/2)\
    	.move(0.5,1.32).line(0.130,1.75).hLine(0.35).vLine(-1.75)\
        .close().extrude(pin_width)

    signal_pcb_pin = cq.Workplane("YZ").workplane(-pin_distance/2 -pin_width/2)\
    	.move(-1.8,0).vLine(0.2).hLine(0.7).vLine(-0.13).hLine(0.1).vLine(-0.07)\
        .close().extrude(pin_width)
    
    pins = signal_pin.union(signal_pcb_pin)

    for i in range(num_pins):
        pins = pins.union(signal_pin.translate((i*pin_pitch,0,0)))
        pins = pins.union(signal_pcb_pin.translate((i*pin_pitch,0,0)))

    pins = pins.union(mount_pin.translate((-pin_distance/2-1.1,0,0)))
    pins = pins.union(mount_pin.translate((pin_distance/2+1.1,0,0)))
    return pins

def generate_angled_pins(params):
    num_pins = params.num_pins
    pin_distance = (num_pins-1)*pin_pitch

    mount_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
    	.move(-2.475,0.01).vLine(1.25).hLine(0.5).vLine(-0.65)\
        .hLine(1.0).vLine(-0.6)\
        .close().extrude(pin_width)

    signal_pin = cq.Workplane("YZ").workplane(-pin_distance/2 -pin_width/2)\
    	.move(-1.225,1.79).vLine(0.35).hLine(1.75).vLine(-0.48)\
        .close().extrude(pin_width)

    signal_pcb_pin = cq.Workplane("YZ").workplane(-pin_distance/2 -pin_width/2)\
    	.move(1.675,0).vLine(0.06).hLine(0.1).vLine(0.14).hLine(0.7).vLine(-0.2)\
        .close().extrude(pin_width)
    
    pins = signal_pin.union(signal_pcb_pin)

    for i in range(num_pins):
        pins = pins.union(signal_pin.translate((i*pin_pitch,0,0)))
        pins = pins.union(signal_pcb_pin.translate((i*pin_pitch,0,0)))

    pins = pins.union(mount_pin.translate((-pin_distance/2-1.1,0,0)))
    pins = pins.union(mount_pin.translate((pin_distance/2+1.1,0,0)))
    return pins

def generate_angled_body(params):
    body_off_center_y = 0.0
    body = generate_straight_body(params)
    body = body.rotate((0,0,0),(1,0,0),90)
    body = body.translate((0,body_off_center_y+1.775,1.09))
    return body

def generate_body(params):
    if not params.angled:
        return generate_straight_body(params)
    return generate_angled_body(params)

def generate_straight_body(params):
    num_pins = params.num_pins
    body_width = params.body_width
    body_height = params.body_height
    body_length = params.body_length

    top_L_side_cut_depth = 0.5
    bottom_L_side_cut_depth = 0.5

    front_box_y_offset = 0.4
    front_box_width = body_length - (0.8*2)
    front_box_depth = 3.0
    front_notch_depth = 2.4

    body_off_center_y = 0.35

    body = cq.Workplane("XY").workplane()\
        .box(body_length, body_width, body_height,centered=(True, True, False))
    R_top_side_L_cut = cq.Workplane("YZ").workplane(-body_length/2).move(-body_width/2, body_height)\
        .hLine(1.2).vLine(-0.5).hLine(-0.65).vLine(-1.0).hLine(-0.55).close()\
        .extrude(top_L_side_cut_depth)
    L_top_side_L_cut = R_top_side_L_cut.translate((body_length-top_L_side_cut_depth,0 ,0))
    top_side_L_cut = R_top_side_L_cut.union(L_top_side_L_cut)

    R_bottom_side_L_cut = cq.Workplane("YZ").workplane(-body_length/2).move(body_width/2, 0)\
        .hLine(-1.5).vLine(0.55).hLine(1.0).vLine(0.65).line(0.5,0.289).close()\
        .extrude(bottom_L_side_cut_depth)
    L_bottom_side_L_cut = R_bottom_side_L_cut.translate((body_length-bottom_L_side_cut_depth,0 ,0))
    bottom_side_L_cut =R_bottom_side_L_cut.union(L_bottom_side_L_cut)

    top_box_cut = cq.Workplane("XY").workplane(body_height)\
        .move(front_box_width/2, -body_width/2+front_box_y_offset)\
        .vLine(2.1).hLine(-front_box_width).vLine(-2.1)\
        .close().extrude(-front_box_depth)
    
    top_notch_cut = cq.Workplane("XY").workplane(body_height)\
        .move(front_box_width/2+.35, -body_width/2+front_box_y_offset+1.0)\
        .vLine(0.6).hLine(-.35-front_box_width-.35).vLine(-0.6)\
        .close().extrude(-front_notch_depth)

    body = body.cut(top_side_L_cut)
    body = body.cut(bottom_side_L_cut)
    body = body.cut(top_box_cut)
    body = body.cut(top_notch_cut)
    body = body.translate((0,body_off_center_y,0))
    return body
    #return bottom_cutout

def generate_part(params):
    pins = generate_pins(params)
    body = generate_body(params)
    body = body.translate((0,0,body_off_center_z))
    return (body, pins)


#opened from within freecad
if "module" in __name__ :
    params=series_params.variant_params['side_entry']['param_generator'](6)
    #params=series_params.variant_params['side_entry']['param_generator'](3)
    (body, pins) = generate_part(params)
    body = body.translate((0,0,body_off_center_z))
    show_object(pins)
    show_object(body)

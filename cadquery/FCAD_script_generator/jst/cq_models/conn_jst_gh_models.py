#  -*- coding: utf8 -*-
# !/usr/bin/python
# 
#  CadQuery script returning JST GH Connectors

# # requirements
# # freecad (v1.5 and v1.6 have been tested)
# # cadquery FreeCAD plugin (v0.3.0 and v0.2.0 have been tested)
# #   https://github.com/jmwright/cadquery-freecad-module 

# # This script can be run from within the cadquery module of freecad.
# # To generate VRML/ STEP files for, use export_conn_jst_gh
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

__title__ = "model description for JST-GH Connectors"
__author__ = "Shack"
__Comment__ = 'model description for JST-GH Connectors using cadquery'

___ver___ = "1.0 15/07/2018"


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
from Helpers import show
from collections import namedtuple
import FreeCAD
from conn_jst_gh_params import *


def generate_pins(params):
    if params.angled:
        return generate_angled_pins(params)
    return generate_straight_pins(params)

def generate_straight_pins(params):
    num_pins = params.num_pins
    body_width = params.body_width
    pin_distance = (num_pins-1)*pin_pitch
    mount_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
    	.move(2.475,0).vLine(2.05).hLine(-2.2).vLine(-0.54).hLine(1.55)\
    	.vLine(-0.71).hLine(-2.06).vLine(-0.43).hLine(0.49)\
    	.vLine(-0.37).close().extrude(pin_width)

    signal_pin = cq.Workplane("YZ").workplane(-pin_distance/2 -pin_width/2)\
    	.move(-2.4754,0).vLine(0.3).hLine(0.7).vLine(0.35).hLine(0.67).vLine(2.8)\
        .hLine(0.17).line(0.16,-0.4).vLine(-2.4).hLine(0.74).vLine(2.55)\
        .hLine(-0.07).line(0.4,0.4).vLine(-3.35).hLine(-2.44+0.67).vLine(-0.25).close()\
    	.extrude(pin_width)
    pins = signal_pin

    for i in range(num_pins):
        pins = pins.union(signal_pin.translate((i*pin_pitch,0,0)))

    pins = pins.union(mount_pin.translate((-pin_distance/2-1.85,0,0)))
    pins = pins.union(mount_pin.translate((pin_distance/2+1.85,0,0)))
    return pins

def generate_angled_pins(params):
    num_pins = params.num_pins
    body_width = params.body_width
    pin_distance = (num_pins-1)*pin_pitch
    mount_pin = cq.Workplane("YZ").workplane(-pin_width/2)\
        .move(-2.475,0).vLine(2.05).hLine(2.2).vLine(-0.54).hLine(-1.55)\
        .vLine(-0.71).hLine(2.06).vLine(-0.43).hLine(-0.49)\
        .vLine(-0.37).close().extrude(pin_width)

    signal_pin = cq.Workplane("YZ").workplane(-pin_distance/2 -pin_width/2)\
        .move(2.4754,0).vLine(0.3).hLine(-0.7).vLine(0.35).hLine(-0.67).vLine(1.4196)\
        .hLine(-3.35).line(0.4,-0.4).vLine(0.07).hLine(2.55).vLine(-0.74).hLine(-2.4)\
        .line(-0.4,-0.16).vLine(-0.17).hLine(2.8).vLine(-0.67).close().extrude(pin_width)

    pins = signal_pin

    for i in range(num_pins):
        pins = pins.union(signal_pin.translate((i*pin_pitch,0,0)))

    pins = pins.union(mount_pin.translate((-(num_pins-1)*pin_pitch/2-1.85,0,0)))
    pins = pins.union(mount_pin.translate(((num_pins-1)*pin_pitch/2+1.85,0,0)))
    return pins

def generate_angled_body(params):
    num_pins = params.num_pins
    body_width = params.body_width
    body_height = params.body_height
    body_length = params.body_length
    body_off_center_y = 0.0
    d = params.pin_angle_distance
    body = generate_straight_body(params)
    body = body.rotate((0,0,0),(1,0,0),90)
    body = body.translate((0,body_off_center_y+1.58,1.62))
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
    
    top_L_side_cut_width = 1.95
    top_L_side_cut_height = 2.25
    top_L_side_cut_short_width = 0.60
    top_L_side_cut_short_height = 0.65
    top_L_side_cut_depth = 0.5

    bottom_L_side_cut_width = 2.25
    bottom_L_side_cut_height = 1.9
    bottom_L_side_cut_short_width = 0.65
    bottom_L_side_cut_short_height = 0.60
    bottom_L_side_cut_depth = 0.5

    front_U_width = body_length - 2*1
    front_U_height = 2.05
    front_U_y_offset = 0.6
    front_U_short_width = 0.5
    front_U_short_height = 0.5
    front_U_depth = 2.6
    front_U_pin_nobs_width = 0.5
    front_U_pin_nobs_wall_width = (front_U_pin_nobs_width-pin_width)/2
    front_U_pin_nobs_height = 0.2

    lock_hole_depth = 1.4
    lock_hole_y_offset = 1.02

    lock_tab_depth = 0.4
    lock_tab_y_offset = 0.32
    lock_tab_height = 1
    lock_tab_z_offset = 2.25

    body_front_width = 0.85
    body_side_width = 0.85
    body_back_width = 0.75

    body_cutout_radius = 0.5
    body_side_cutout_depth = 3.35
    body_side_cutout_width = 1
    body_front_cutout_depth = 3.9

    body_off_center_y = 0.35

    body_top_square_hole_width = 1.1
    body_top_square_hole_height = 0.6
    body_top_square_hole_depth = 1
    body_top_square_hole_x_offset = 0.35
    body_top_square_hole_y_offset = 0.35
    
    body_top_L_hole_width = 0.8
    body_top_L_hole_height = 0.9
    body_top_L_hole_depth = 1

    body = cq.Workplane("XY").workplane()\
        .box(body_length, body_width, body_height,centered=(True, True, False))
    R_top_side_L_cut = cq.Workplane("YZ").workplane(-body_length/2).move(-body_width/2, body_height)\
        .hLine(top_L_side_cut_width).vLine(-top_L_side_cut_short_height)\
        .hLine(-(top_L_side_cut_width-top_L_side_cut_short_width))\
        .vLine(-(top_L_side_cut_height-top_L_side_cut_short_height))\
        .hLine(-top_L_side_cut_short_width).close()\
        .extrude(top_L_side_cut_depth)
    L_top_side_L_cut = R_top_side_L_cut.translate((body_length-top_L_side_cut_depth,0 ,0))
    top_side_L_cut = R_top_side_L_cut.union(L_top_side_L_cut)

    R_bottom_side_L_cut = cq.Workplane("YZ").workplane(-body_length/2).move(body_width/2, 0)\
        .hLine(-bottom_L_side_cut_width).vLine(bottom_L_side_cut_short_height)\
        .hLine((bottom_L_side_cut_width-bottom_L_side_cut_short_width))\
        .vLine((bottom_L_side_cut_height-bottom_L_side_cut_short_height))\
        .hLine(bottom_L_side_cut_short_width).close()\
        .extrude(bottom_L_side_cut_depth)
    L_bottom_side_L_cut = R_bottom_side_L_cut.translate((body_length-bottom_L_side_cut_depth,0 ,0))
    

    bottom_side_L_cut =R_bottom_side_L_cut.union(L_bottom_side_L_cut)


    front_U_cut = cq.Workplane("XY").workplane(body_height)\
        .move(front_U_width/2, -body_width/2+front_U_y_offset)\
        .vLine(front_U_height).hLine(-front_U_short_width).vLine(-front_U_short_height)\
        .hLine(-(front_U_width-2*front_U_short_width-(num_pins-1)*pin_pitch-front_U_pin_nobs_width)/2)
    for x in range(0, num_pins):
        front_U_cut = front_U_cut.vLine(-front_U_pin_nobs_height).hLine(-front_U_pin_nobs_wall_width)\
            .vLine(front_U_pin_nobs_height).hLine(-pin_width).vLine(-front_U_pin_nobs_height)\
            .hLine(-front_U_pin_nobs_wall_width).vLine(front_U_pin_nobs_height)
        if x != num_pins-1:
            front_U_cut = front_U_cut.hLine(-(pin_pitch-front_U_pin_nobs_width))
    front_U_cut = front_U_cut.hLine(-(front_U_width-2*front_U_short_width-(num_pins-1)*pin_pitch-front_U_pin_nobs_width)/2)\
        .vLine(front_U_short_height).hLine(-front_U_short_width)\
        .vLine(-front_U_height).close().extrude(-front_U_depth)

    lowerbar = cq.Workplane("YZ").workplane(-body_length/2).move(-body_width/2, 0)\
        .hLine(0.95).vLine(0.5).hLine(-0.75).vLine(0.15).hLine(-0.2).close().extrude(body_length)

    lock_hole = cq.Workplane("XY").workplane()\
        .box(lock_hole_width[num_pins], lock_hole_depth, body_height,centered=(True, True, False))\
        .translate((0, lock_hole_y_offset, 0))

    lock_tab = cq.Workplane("YZ").workplane(-lock_tab_width[num_pins]/2).move(lock_tab_y_offset, lock_tab_z_offset)\
        .hLine(lock_tab_depth).line(-lock_tab_depth, lock_tab_height).close().extrude(lock_tab_width[num_pins])

    body_top_square_hole_template = cq.Workplane("XY").workplane()\
        .box(body_top_square_hole_width, body_top_square_hole_height, body_top_square_hole_depth,centered=(True, True, False))\
        .translate((-(body_length-body_top_square_hole_width)/2+body_top_square_hole_x_offset,\
        (body_width-body_top_square_hole_height)/2-body_top_square_hole_y_offset, body_height-body_top_square_hole_depth))
    
    body_top_square_hole = body_top_square_hole_template.union(body_top_square_hole_template\
        .translate((body_length-body_top_square_hole_width-body_top_square_hole_x_offset*2,0,0)))

    if 10 <= num_pins <= 15:
        body_top_square_hole = body_top_square_hole.union(body_top_square_hole_template\
            .translate((-body_top_square_hole_width-body_top_square_hole_x_offset,0,0)))
        body_top_square_hole = body_top_square_hole.union(body_top_square_hole_template\
            .translate(((-body_length+body_top_square_hole_width*2+body_top_square_hole_x_offset*3),0,0)))

    body = body.cut(lock_hole)
    body = body.union(lock_tab)
    body = body.cut(lowerbar)
    body = body.cut(front_U_cut)
    body = body.cut(top_side_L_cut)
    body = body.cut(bottom_side_L_cut)
    body = body.cut(body_top_square_hole)
    body = body.translate((0,body_off_center_y,0))
    return body
    #return bottom_cutout

def generate_part(params):
    pins = generate_pins(params)
    body = generate_body(params)
    body_length=params.body_length
    body = body.translate((0,0,body_off_center_z))
    #made an error, need to rotate it by 180 degree
    center_x=body_corner_x+body_length/2
    # pins = pins.rotate((center_x,0,0),(0,0,1),180)
    # body = body.rotate((center_x,0,0),(0,0,1),180)
    return (body, pins)


#opend from within freecad
if "module" in __name__ :
    params=series_params.variant_params['side_entry']['param_generator'](6)
    #params=series_params.variant_params['side_entry']['param_generator'](3)

    (body, pins) = generate_part(params)
    body = body.translate((0,0,body_off_center_z))
    show(pins)
    show(body)

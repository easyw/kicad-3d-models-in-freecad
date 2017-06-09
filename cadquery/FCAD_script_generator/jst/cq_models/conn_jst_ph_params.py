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

__title__ = "model description for JST-PH Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for JST-PH Connectors using cadquery. Datasheet: http://www.jst-mfg.com/product/pdf/eng/ePH.pdf'

___ver___ = "1.0 02/03/2017"

from collections import namedtuple
from math import sqrt


#global parameter
pin_width = 0.5
pin_depth = 3.4
pin_inner_lenght = 5
pin_lock_h1 = 1.9
pin_lock_h2 = 2.5
pin_lock_d = 0.3
pin_fillet = 0.2
pin_bend_radius = 0.05
pin_pitch = 2.0
body_corner_x = -1.95
body_corner_y = -1.7

body_front_width = 0.6
body_side_width = 0.5
body_back_width = 0.5

body_front_main_cutout_depth = 3.9
body_front_main_cutout_to_side = 2.5
body_front_cutout_height = 1.8
body_front_cutout_from_top = 1.8
body_front_cutout_width = 1.0
body_front_cutout_from_side = 0.55


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

def make_params_angled(num_pins, name):
    return Params(
        angled=True,
        num_pins=num_pins,
        model_name=name,
        pin_angle_distance=6.25-6.0,
        pin_angle_length=6.25,
        body_width=4.5,
        body_height=6.0,
        body_length=2*1.95+(num_pins-1)*pin_pitch,
        zdistance=4.8-4.5,
        file_name="JST_PH_B{num_pins:02d}B-PH-K_{num_pins:02d}x{pin_pitch:.2f}mm_Straight".format(num_pins=num_pins, pin_pitch=pin_pitch)
    )
def make_params_straight(num_pins, name):
    return Params(
        angled=False,
        num_pins=num_pins,
        model_name=name,
        pin_angle_distance=0,
        pin_angle_length=0,
        body_width=4.5,
        body_height=6.0,
        body_length=2*1.95+(num_pins-1)*pin_pitch,
        zdistance=6.1-5.75,
        file_name="JST_PH_B{num_pins:02d}B-PH-K_{num_pins:02d}x{pin_pitch:.2f}mm_Straight".format(num_pins=num_pins, pin_pitch=pin_pitch)
    )

params_straight = {
    "B02B_PH_K" : make_params_straight( 2, 'B02B_PH_K'),
    "B03B_PH_K" : make_params_straight( 3, 'B03B_PH_K'),
    "B04B_PH_K" : make_params_straight( 4, 'B04B_PH_K'),
    "B05B_PH_K" : make_params_straight( 5, 'B05B_PH_K'),
    "B06B_PH_K" : make_params_straight( 6, 'B06B_PH_K'),
    "B07B_PH_K" : make_params_straight( 7, 'B07B_PH_K'),
    "B08B_PH_K" : make_params_straight( 8, 'B08B_PH_K'),
    "B09B_PH_K" : make_params_straight( 9, 'B09B_PH_K'),
    "B10B_PH_K" : make_params_straight(10, 'B10B_PH_K'),
    "B11B_PH_K" : make_params_straight(11, 'B11B_PH_K'),
    "B12B_PH_K" : make_params_straight(12, 'B12B_PH_K'),
    "B13B_PH_K" : make_params_straight(13, 'B13B_PH_K'),
    "B14B_PH_K" : make_params_straight(14, 'B14B_PH_K'),
    "B15B_PH_K" : make_params_straight(15, 'B15B_PH_K'),
    "B16B_PH_K" : make_params_straight(16, 'B16B_PH_K'),
    "B20B_PH_K" : make_params_straight(20, 'B20B_PH_K')
}

params_angled = {
    "S02B_PH_K" : make_params_angled( 2, 'S02B_PH_K'),
    "S03B_PH_K" : make_params_angled( 3, 'S03B_PH_K'),
    "S04B_PH_K" : make_params_angled( 4, 'S04B_PH_K'),
    "S05B_PH_K" : make_params_angled( 5, 'S05B_PH_K'),
    "S06B_PH_K" : make_params_angled( 6, 'S06B_PH_K'),
    "S07B_PH_K" : make_params_angled( 7, 'S07B_PH_K'),
    "S08B_PH_K" : make_params_angled( 8, 'S08B_PH_K'),
    "S09B_PH_K" : make_params_angled( 9, 'S09B_PH_K'),
    "S10B_PH_K" : make_params_angled(10, 'S10B_PH_K'),
    "S11B_PH_K" : make_params_angled(11, 'S11B_PH_K'),
    "S12B_PH_K" : make_params_angled(12, 'S12B_PH_K'),
    "S13B_PH_K" : make_params_angled(13, 'S13B_PH_K'),
    "S14B_PH_K" : make_params_angled(14, 'S14B_PH_K'),
    "S15B_PH_K" : make_params_angled(15, 'S15B_PH_K'),
    "S16B_PH_K" : make_params_angled(16, 'S16B_PH_K')
}

# -*- coding: utf8 -*-
#!/usr/bin/python
#
# CadQuery script returning JST GH Connectors

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

__title__ = "model description for JST-GH Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for JST-GH Connectors using cadquery'
    
___ver___ = "1.1 10/04/2016"

from collections import namedtuple
from math import sqrt
from itertools import chain

#global parameter
body_off_center_z = 0.15
pin_width = 0.2
pin_depth = 3.4
pin_inner_lenght = 6.5
pin_lock_h1 = 1.9
pin_lock_h2 = 2.5
pin_lock_d = 0.3
pin_fillet = 0.2
pin_bend_radius = 0.05
pin_pitch = 1.25
body_corner_x = -2.45
body_corner_y = -2.35
lock_hole_width = (0, 0, 2.05, 3.0, 4.45, 4.45, 6.65, 6.65, 6.65, 6.65, 8.6, 8.6, 8.6, 8.6, 8.6, 8.6)
lock_tab_width = (0, 0, 0.95, 1.25, 2.45, 2.50, 4.45, 4.45, 4.45, 4.45, 6.1, 6.1, 6.1, 6.1, 6.1, 6.1)


Params = namedtuple("Params",[
    'angled',
    'num_pins',
    'pin_angle_distance',
    'pin_angle_length',
    'body_width',
    'body_height',
    'body_length'
])

def make_params_angled(num_pins):
    return Params(
        angled=True,
        num_pins=num_pins,
        pin_angle_distance=9.2-7,
        pin_angle_length=9.2,
        body_width=4.25,
        body_height=4.05,
        body_length=4.5+((num_pins-1)*pin_pitch)
    )
def make_params_straight(num_pins):
    return Params(
        angled=False,
        num_pins=num_pins,
        pin_angle_distance=0,
        pin_angle_length=0,
        body_width=4.25,
        body_height=4.05,
        body_length=4.5+((num_pins-1)*pin_pitch)

    )

class series_params():
    series = "GH"
    manufacturer = 'JST'
    number_of_rows = 1

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

    variant_params = {
        'top_entry':{
            'mpn_format_string': 'BM{pincount:02}B-GHS-TBT',
            'orientation': 'V',
            'datasheet': 'http://www.jst-mfg.com/product/pdf/eng/eGH.pdf',
            'param_generator': make_params_straight,
            'pinrange': range(2,15),
            'mount_pin': '-1MP'
        },
        # 'top_entry_boss':{
        #     'mpn_format_string': 'B{pincount:02}B-XH-AM',
        #     'orientation': 'V',
        #     'datasheet': 'http://www.jst-mfg.com/product/pdf/eng/eXH.pdf',
        #     'param_generator': make_params_straight_boss,
        #     'pinrange': range(1,13),
        #     'mount_pin': ''
        # },
        'side_entry':{
            'mpn_format_string': 'SM{pincount:02}B-GHS-TB',
            'orientation': 'H',
            'datasheet': 'http://www.jst-mfg.com/product/pdf/eng/eGH.pdf',
            'param_generator': make_params_angled,
            'pinrange': range(2, 15),
            'mount_pin': '-1MP'
        }
    }

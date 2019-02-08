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

__title__ = "model description for JST-EH Connectors"
__author__ = "poeschlr"
__Comment__ = 'model description for JST-EH Connectors using cadquery'

___ver___ = "1.1 04/01/2016"


from math import sqrt
from collections import namedtuple

#global parameter
pin_width = 0.64
pin_depth = 3.2
pin_inner_lenght = 5.1
pin_lock_h1 = 1.9
pin_lock_h2 = 2.5
pin_lock_d = 0.3
pin_fillet = 0.2
pin_bend_radius = 0.05
pin_pitch = 2.5

Body_width = 3.8
Body_width_difference_between_angled_and_straight = 4.2-3.8
Body_height = 6

body_side_to_pin = 2.5
body_back_to_pin = 1.6

body_corner_x = -body_side_to_pin
body_corner_y = -Body_width+body_back_to_pin

Params = namedtuple("Params",[
    'angled',
    'num_pins',
    'pin_angle_distance',
    'pin_angle_length',
    'body_width',
    'body_height',
    'body_length',
    'zdistance'
])

def make_params_angled(num_pins):
    return Params(
        angled=True,
        num_pins=num_pins,
        pin_angle_distance=6.7-6,
        pin_angle_length=6.7-0.5,
        body_width=Body_width,
        body_height=Body_height,
        body_length=2*body_side_to_pin+(num_pins-1)*pin_pitch,
        zdistance=Body_width_difference_between_angled_and_straight
    )

def make_params_straight(num_pins):
    return Params(
        angled=False,
        num_pins=num_pins,
        pin_angle_distance=0,
        pin_angle_length=0,
        body_width=Body_width,
        body_height=Body_height,
        body_length=2*body_side_to_pin+(num_pins-1)*pin_pitch,
        zdistance=Body_width_difference_between_angled_and_straight
    )

class series_params():
    series = "EH"
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
            'mpn_format_string': 'B{pincount:d}B-EH-A',
            'orientation': 'V',
            'datasheet': 'http://www.jst-mfg.com/product/pdf/eng/eEH.pdf',
            'param_generator': make_params_straight,
            'pinrange': range(2, 16),
            'mount_pin': ''
        },
        'side_entry':{
            'mpn_format_string': 'S{pincount:d}B-EH',
            'orientation': 'H',
            'datasheet': 'http://www.jst-mfg.com/product/pdf/eng/eEH.pdf',
            'param_generator': make_params_angled,
            'pinrange': range(2, 16),
            'mount_pin': ''
        }
    }

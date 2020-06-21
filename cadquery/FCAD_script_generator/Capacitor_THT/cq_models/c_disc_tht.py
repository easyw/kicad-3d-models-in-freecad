#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is derived from a cadquery script for generating QFP models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py L35_D12.5_p05

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are a FreeCAD & cadquery tools                                     *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating QFP/SOIC/SSOP/TSSOP models in STEP AP214  *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Lesser General Public License (LGPL)     *
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
#****************************************************************************

__title__ = "make Radial Caps 3D models"
__author__ = "maurice and hyOzd and Frank"
__Comment__ = 'make C axial Caps 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.2 10/02/2017"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "kicad StepUp"
    STR_licEmail = "ksu"
    STR_licOrgSys = "kicad StepUp"
    STR_licPreProc = "OCC"
    STR_licOrg = "FreeCAD"

    LIST_license = ["",]
    ############################################################################


import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt, sin

from c_disc_tht_param import *

class series_params():
    fp_name_format = "disc_fp_name"
    name_prefix = "C"

    pin_1_on_origin = True

    body_color_key = "orange body"
    pins_color_key = "metal grey pins"

    color_keys = [
        body_color_key,
        pins_color_key,
    ]
    obj_suffixes = [
        '__pins',
        '__body'
    ]

def getName(params, configuration):
    format_fn = configuration[series_params.fp_name_format]
    prefix = configuration['prefix'][series_params.name_prefix]
    suffix = params.suffix


    return format_fn.format(width=params.W, diameter=params.L, pitch=params.F,
            prefix=prefix, suffix=suffix)

#all_params = all_params_c_disc_th_cap
all_params = kicad_naming_params_c_disc_th_cap

def generate_part(params):
    L = params.L    # body length
    W = params.W    # body width
    d = params.d     # lead diameter
    F = params.F     # lead separation (center to center)
    ll = params.ll   # lead length
    bs = params.bs   # board separation
    rot = params.rotation


    bend_offset_y = (sin(radians(60.0))*d)/sin(radians(90.0))
    bend_offset_z = (sin(radians(30.0))*d)/sin(radians(90.0))
    # draw the leads
    lead1 = cq.Workplane("XY").workplane(offset=-ll).center(-F/2,0).circle(d/2).extrude(ll+L/4-d+bs)
    lead1 = lead1.union(cq.Workplane("XY").workplane(offset=L/4-d+bs).center(-F/2,0).circle(d/2).center(-F/2+d/2,0).revolve(30,(-F/2+d/2+d,d)).transformed((-30,0,0),(-(-F/2+d/2),d-bend_offset_y,bend_offset_z)).circle(d/2).extrude(L/2))
    lead1 = lead1.rotate((-F/2,0,0), (0,0,1), -90)
    lead2 = lead1.rotate((-F/2,0,0), (0,0,1), 180).translate((F,0,0))
    leads = lead1.union(lead2)

    h = W/2
    c = L
    #calculate point
    R = (h/2) + ((c*c)/(8*h))
    print(R)
    point2 = (sqrt((R * R) - (L/4 * L/4))) - (R-h)

    #draw the body0
    body = cq.Workplane("XY").workplane(offset=L/2+bs).moveTo(0, W/2).threePointArc((-L/4, point2),(-L/2, 0),forConstruction=False).threePointArc((-L/4, -point2),(0, -W/2),forConstruction=False).close().revolve()
    leads = leads.cut(body)
    #show(leads)

    if series_params.pin_1_on_origin:
        body = body.translate((F/2,0,0))
        leads = leads.translate((F/2,0,0))

    return (body, leads) #body, pins

if "module" in __name__:

    variant = "C_Disc_D12.0mm_W4.4mm_P7.75mm"
    body, pins= generate_part(all_params[variant]) #body, base, mark, pins, top


    show(body)
    show(pins)

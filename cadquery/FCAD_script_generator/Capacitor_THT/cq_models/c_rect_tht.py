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
__author__ = "maurice and hyOzd"
__Comment__ = 'make Rect Caps 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.2 10/02/2017"

# thanks to Frank Severinsen Shack for including vrml materials

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
from math import tan, radians, sqrt

from c_rect_tht_param import *

class series_params():
    fp_name_format = "rect_fp_name"
    name_prefix = "C"
    orientation = "H"

    pin_1_on_origin = True

    # colors are found in the params file

    obj_suffixes = [
        '__pins',
        '__body'
    ]

def getName(params, configuration):
    format_fn = configuration[series_params.fp_name_format]
    prefix = configuration['prefix'][series_params.name_prefix]
    suffix = params.suffix


    return format_fn.format(length=params.L, width=params.W, pitch=params.F,
            prefix=prefix, suffix=suffix)

#all_params = all_params_rect_th_cap
all_params = kicad_naming_params_rect_th_cap

def generate_part(params):
    series = params.series # Series
    H = params.H    # body height
    L = params.L    # body length
    W = params.W    # body width
    d = params.d     # lead diameter
    F = params.F     # lead separation (center to center)
    ll = params.ll   # lead length
    bs = params.bs   # board separation
    ef = W/10       # top and bottom edges fillet
    pt = 0.02 # pin thickness (only for MKT)
    pb = F/20
    rot = params.rotation
    if series == 'MKS':
        body = cq.Workplane("XY").box(L, W, H)
        body = body.translate((0,0,H/2)).rotate((0,0,0), (0,0,1), 0). \
            edges("|Z").fillet(ef).edges(">Z").fillet(ef)
        # draw the leads
        leads = cq.Workplane("XY").workplane(offset=bs).\
            center(-F/2,0).circle(d/2).extrude(-(ll)).\
            center(F,0).circle(d/2).extrude(-(ll)).translate((0,0,0.1)) #need overlap for fusion

    elif series == 'MKT':
        body = cq.Workplane("XY").box(F-2*pb, W-2*pt, H-2*pt)
        #translate the object
        body=body.translate((0,0,H/2)).rotate((0,0,0), (0,0,1), 0)

        pin1 = cq.Workplane("XY").box(pb, W, H)
        pin1=pin1.translate((-F/2+pb/2,0,H/2)).rotate((0,0,0), (0,0,1), 0)
        pin2 = cq.Workplane("XY").box(pb, W, H)
        pin2=pin2.translate((F/2-pb/2,0,H/2)).rotate((0,0,0), (0,0,1), 0)
        pins = pin1.union(pin2)

        leads=cq.Workplane("XY").workplane(offset=H-0.6).\
            center(-F/2,0).circle(d/2).extrude(-(ll+H-0.6)).\
            center(F,0).circle(d/2).extrude(-(ll+H-0.6)).translate((0,0,0.1)) #need overlap for fusion
        leads=leads.union(pins)


    if series_params.pin_1_on_origin:
        body = body.translate((F/2,0,0))
        leads = leads.translate((F/2,0,0))
    
    #show(body)
    #show(leads)
    #stop
    return (body, leads) #body, pins

if "module" in __name__:

    variant = "C_Rect_L13.0mm_W3.0mm_P10.00mm_FKS3_FKP3_MKS4"
    body, pins= generate_part(all_params[variant]) #body, base, mark, pins, top


    show(body)
    show(pins)

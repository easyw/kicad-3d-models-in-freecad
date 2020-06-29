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
__Comment__ = 'make Radial Caps 3D models exported to STEP and VRML for Kicad StepUP script'

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

from cp_axial_tht_param import *

class series_params():
    fp_name_format = "axial_fp_name"
    name_prefix = "CP"
    orientation = "H"

    pin_1_on_origin = True

    body_color_key = "blue body"
    mark_vg_color_key = "black body"
    mark_bg_color_key = "metal grey pins"
    pins_color_key = "metal grey pins"
    endcaps_color_key = "metal grey pins"

    color_keys = [
        body_color_key,
        mark_vg_color_key,
        mark_bg_color_key,
        pins_color_key,
        endcaps_color_key
    ]
    obj_suffixes = [
        '__body',
        '__mark_vg',
        '__mark_bg',
        '__pins',
        '__endcaps'
    ]

def getName(params, configuration):
    format_fn = configuration[series_params.fp_name_format]
    prefix = configuration['prefix'][series_params.name_prefix]
    orientation = configuration['orientation_options'][series_params.orientation]


    return format_fn.format(length=params.L, diameter=params.D, pitch=params.F,
            prefix=prefix, orientation=orientation)

#all_params = all_params_radial_th_cap
all_params = kicad_naming_params_axial_th_cap

def generate_part(params):

    L = params.L    # overall height
    D = params.D    # body diameter
    d = params.d     # lead diameter
    F = params.F     # lead separation (center to center)
    ll = params.ll   # lead length
    bs = params.bs   # board separation
    rot = params.rotation

    bt = 1.        # flat part before belt
    if D > 4:
        bd = 0.2       # depth of the belt
    else:
        bd = 0.15       # depth of the belt
    bh = 1.        # height of the belt
    bf = 0.3       # belt fillet

    tc = 0.2       # cut thickness for the bottom&top
    dc = D*0.7     # diameter of the bottom&top cut
    ts = 0.1       # thickness of the slots at the top in the shape of (+)
    ws = 0.1       # width of the slots

    ef = 0.2       # top and bottom edges fillet

    bpt = 0.1        # bottom plastic thickness (not visual)
    tmt = ts*2       # top metallic part thickness (not visual)

    # TODO: calculate width of the cathode marker bar from the body size
    ciba = 45.  # angle of the cathode identification bar

    # TODO: calculate marker sizes according to the body size
    mmb_h = D*0.4       # lenght of the (-) marker on the cathode bar
    mmb_w = mmb_h/4      # rough width of the marker

    ef_s2 = ef/sqrt(2)
    ef_x = ef-ef/sqrt(2)
    #move(0, tc+bpt).\
    #line(dc/2.-off, 0).\
    #line(0, -(tc+bpt+off)).\
    #line(D/2.-dc/2.-ef, 0).\
    #threePointArc((D/2.-(ef_x)+off, bs+(ef_x)+off), (D/2.+off, bs+ef)).\
    #line(0, bt).\
    #threePointArc((D/2.-bd, bs+bt+bh/2.), (D/2., bs+bt+bh)).\
    #lineTo(D/2., L+bs-ef).\
    #threePointArc((D/2.-(ef_x), L+bs-(ef_x)), (D/2.-ef, L+bs)).\
    #lineTo(dc/2., L+bs).\
    #line(0, -(tc+tmt)).\
    #line(-dc/2., 0).\
    #close()

    def bodyp(off=0):
        tpa_off=off/sqrt(2)
        return cq.Workplane("XZ").move(0, bs)\
               .move(0, tc+bpt)\
               .line(dc/2.-off, 0)\
               .line(0, -(tc+bpt+off))\
               .hLineTo(D/2.-ef, 0)\
               .threePointArc((D/2.-(ef_x)+tpa_off, bs+(ef_x)-tpa_off),(D/2.+off, bs+ef))\
               .line(0, bt)\
               .threePointArc((D/2.-bd+off, bs+bt+bh/2.), (D/2.+off, bs+bt+bh))\
               .lineTo(D/2.+off, L+bs-ef)\
               .threePointArc((D/2.-(ef_x)+tpa_off, L+bs-(ef_x)+tpa_off), (D/2.-ef, L+bs+off))\
               .hLineTo(dc/2)\
               .vLine(-(tc+tmt))\
               .hLineTo(0)\
               .close()

    body = bodyp().revolve(360-ciba, (0,0,0), (0,1,0))
    bar = bodyp(0.01).revolve(ciba, (0,0,0), (0,1,0))

    #show(body)
    #show(bar)
    # # fillet the belt edges
    BS = cq.selectors.BoxSelector
    # note that edges are selected from their centers
    b_r = D/2.-bd # inner radius of the belt

    try:
        #body = body.edges(BS((-0.5,-0.5, bs+bt-0.01), (0.5, 0.5, bs+bt+bh+0.01))).\
            #fillet(bf)
        pos=D/10
        body = body.edges(BS((-pos,-pos, bs+bt-0.2), (pos, pos, bs+bt+bh+0.01))).\
            fillet(bf)
    except:
        #stop
        print("")
        print("not filleting")
        #show(body)
        #show(bar)
        #raise
        pass

    #b_r = D/2.-bd # inner radius of the belt
    bar = bar.edges(BS((b_r/sqrt(2), 0, bs+bt-0.01),(b_r, -b_r/sqrt(2), bs+bt+bh+0.01))).\
          fillet(bf)

    body = body.rotate((0,0,0), (0,0,1), 180-ciba/2)
    bar = bar.rotate((0,0,0), (0,0,1), 180+ciba/2)


    # draw the metal at the bottom
    bottom = cq.Workplane("XY").workplane(offset=bs+tc).\
             circle(dc/2).extrude(bpt)
    # draw the metallic part at the top
    top = cq.Workplane("XY").workplane(offset=bs+L-tc-ts).\
         circle(dc/2).extrude(tmt)
    top = top.union(bottom)
    # draw end knobs
    topknob = cq.Workplane("XY").workplane(offset=bs+tc).\
        circle(D/8).extrude(-D/30)
    bottomknob = cq.Workplane("XY").workplane(offset=bs+L-tc-ts+tmt).\
         circle(D/8).extrude(D/30)
    top = top.union(topknob).union(bottomknob)

    # draw the (-) marks on the bar
    n = int(L/(2*mmb_h)) # number of (-) marks to draw
    points = []
    first_z = (L-(2*n-1)*mmb_h)/2
    for i in range(n):
        points.append((0, (i+0.25)*2*mmb_h+first_z))
    mmb = cq.Workplane("YZ", (-D/2,0,bs)).pushPoints(points).\
          box(mmb_w, mmb_h, 2).\
          edges("|X").fillet(mmb_w/2.-0.01)

    #mmb = mmb.cut(mmb.translate((0,0,0)).cut(bar))
    mmb = mmb.cut(mmb.cut(bar).translate((-0.005,0,0)))
    bar = bar.cut(mmb)

    # draw the leads
    lead1 = cq.Workplane("XY").workplane(offset=-ll).center(-F/2,0).circle(d/2).extrude(ll+D/2-d+bs)
    lead1 = lead1.union(cq.Workplane("XY").workplane(offset=D/2-d+bs).center(-F/2,0).circle(d/2).center(-F/2+d/2,0).revolve(90,(-F/2+d/2+d,d)))
    lead1 = lead1.rotate((-F/2,0,0), (0,0,1), -90)
    lead2 = lead1.rotate((-F/2,0,0), (0,0,1), 180).translate((F,0,0))
    Hlead = cq.Workplane("YZ").workplane(offset=-F/2+d).center(0,D/2+bs).circle(d/2).extrude(F-d*2)
    leads = lead1.union(lead2).union(Hlead)

    angle = 90
    #convert vertical model to horizontal
    body = body.rotate((0,0,0), (0,1,0), angle).translate((-L/2,0,D/2))
    mmb = mmb.rotate((0,0,0), (0,1,0), angle).translate((-L/2,0,D/2))
    bar = bar.rotate((0,0,0), (0,1,0), angle).translate((-L/2,0,D/2))
    top = top.rotate((0,0,0), (0,1,0), angle).translate((-L/2,0,D/2))

    if series_params.pin_1_on_origin:
        body = body.translate((F/2,0,0))
        mmb = mmb.translate((F/2,0,0))
        bar = bar.translate((F/2,0,0))
        top = top.translate((F/2,0,0))
        leads = leads.translate((F/2,0,0))

    angle = rot

    body = body.rotate((0,0,0), (0,0,1), angle)
    mmb = mmb.rotate((0,0,0), (0,0,1), angle)
    bar = bar.rotate((0,0,0), (0,0,1), angle)
    top = top.rotate((0,0,0), (0,0,1), angle)
    leads = leads.rotate((0,0,0), (0,0,1), angle)

    #show(body)
    #show(mmb)
    #show(bar)
    #show(leads)
    #show(top)
    #stop
    return (body, mmb, bar, leads, top) #body, base, mark, pins, top

if "module" in __name__:

    variant = "CP_Axial_L10.0mm_D6.0mm_P15.00mm_Horizontal"
    body, mmb, bar, leads, top= generate_part(all_params[variant]) #body, base, mark, pins, top

    show(body)
    show(mmb)
    show(bar)
    show(leads)
    show(top)

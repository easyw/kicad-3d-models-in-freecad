# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
# This is a
# Dimensions are from Microchips Packaging Specification document:
# DS00000049BY. Body drawing is the same as QFP generator#

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8

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

__title__ = "make DIP ICs 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make DIP ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.3 14/08/2015"

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "black body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
marking_color_key = "light brown label"
marking_color = shaderColors.named_colors[marking_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
from Gui.Command import *


outdir=os.path.dirname(os.path.realpath(__file__)+"/../_3Dmodels")
scriptdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)
sys.path.append(scriptdir)
if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

# Licence information of the generated models.
#################################################################################################
STR_licAuthor = "kicad StepUp"
STR_licEmail = "ksu"
STR_licOrgSys = "kicad StepUp"
STR_licPreProc = "OCC"
STR_licOrg = "FreeCAD"   

LIST_license = ["",]
#################################################################################################

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

try:
    # Gui.SendMsgToActiveView("Run")
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"

# case_color = (0.1, 0.1, 0.1)
# pins_color = (0.9, 0.9, 0.9)
#case_color = (50, 50, 50)
#pins_color = (230, 230, 230)
destination_dir="/DIP_packages"
# rotation = 0


Params = namedtuple("Params", [
    'D',    # package length
    'E1',   # package width
    'E',    # package shoulder-to-shoulder width
    'A1',   # package board seperation
    'A2',   # package height

    'b1',   # pin width
    'b',    # pin tip width
    'e',    # pin center to center distance (pitch)

    'npins',  # number of pins
    'modelName', #modelName
    'rotation' #rotation if required
])

def make_params(D, npins, modelName, rotation):
    """Since most DIL packages share the same parameters this is a
    convenience function to generate a Params structure.
    """
    return Params(
        D = D,      # package length
        E1 = 6.35,  # package width
        E = 7.874,  # shoulder to shoulder width (includes pins)
        A1 = 0.38,  # base to seating plane
        A2 = 3.3,   # package height

        b1 = 1.524, # upper lead width
        b = 0.457,  # lower lead width
        e = 2.54,   # pin to pin distance

        npins = npins,  # total number of pins
        modelName = modelName,  # Model Name
        rotation = rotation    # rotation if required
    )

def make_paramso(D, npins, modelName, rotation):
    """Wider version of make_params() 10.16 for opto-couplers """
    return Params(
        D = D,      # package length
        E1 = 6.35, #10.16+0.254-1.24,  # package width
        E = 10.16+0.254,  # shoulder to shoulder width (includes pins)
        A1 = 0.38,  # base to seating plane
        A2 = 3.3,   # package height

        b1 = 1.524, # upper lead width
        b = 0.457,  # lower lead width
        e = 2.54,   # pin to pin distance

        npins = npins,  # total number of pins
        modelName = modelName,  # Model Name
        rotation = rotation    # rotation if required
    )
    
def make_paramsm(D, npins, modelName, rotation):
    """Wider version of make_params() 10.16 for opto-couplers """
    return Params(
        D = D,      # package length
        E1 = 10.16+0.254-1.24,  # package width
        E = 10.16+0.254,  # shoulder to shoulder width (includes pins)
        A1 = 0.38,  # base to seating plane
        A2 = 3.3,   # package height

        b1 = 1.524, # upper lead width
        b = 0.457,  # lower lead width
        e = 2.54,   # pin to pin distance

        npins = npins,  # total number of pins
        modelName = modelName,  # Model Name
        rotation = rotation    # rotation if required
    )

def make_paramsw(D, npins, modelName, rotation):
    """Wider version of make_params()"""
    return Params(
        D = D,      # package length
        E1 = mm(0.53),  # package width
        E = mm(0.61),  # shoulder to shoulder width (includes pins)
        A1 = 0.38,  # base to seating plane
        A2 = 3.3,   # package height

        b1 = 1.524, # upper lead width
        b = 0.457,  # lower lead width
        e = 2.54,   # pin to pin distance

        npins = npins,  # total number of pins
        modelName = modelName,  # Model Name
        rotation = rotation    # rotation if required
    )

def mm(inch):
    """Convenience function to convert inches to mm"""
    return inch*25.4

all_params = {
    "DIP-8_W7.62mm" : Params(
        D = 9.27,   # package length
        E1 = 6.35,  # package width
        E = 7.874,  # shoulder to shoulder width (includes pins)
        A1 = 0.38,  # base to seating plane
        A2 = 3.3,   # package height

        b1 = 1.524, # upper lead width
        b = 0.457,  # lower lead width
        e = 2.54,   # pin to pin distance

        npins = 8,  # total number of pins
        modelName = 'DIP-8_W7.62mm',  # Model Name
        rotation = 90    # rotation if required
    ),

    "DIP-4_W7.62mm" : make_params(4.93, 4, 'DIP-4_W7.62mm', 90),
    "DIP-4_W10.16mm" : make_paramso(4.93, 4, 'DIP-4_W10.16mm', 90),
    "DIP-6_W7.62mm" : make_params(7.05, 6, 'DIP-6_W7.62mm', 90),
    "DIP-6_W10.16mm" : make_paramso(7.05, 6, 'DIP-6_W10.16mm', 90),
    "DIP-8_W10.16mm" : make_paramso(9.27, 8, 'DIP-8_W10.16mm', 90),
    "DIP-14_W7.62mm" : make_params(19.05, 14, 'DIP-14_W7.62mm', 90),
    "DIP-16_W7.62mm" : make_params(mm(0.755), 16, 'DIP-16_W7.62mm', 90),
    "DIP-18_W7.62mm" : make_params(mm(0.9), 18, 'DIP-18_W7.62mm', 90),
    "DIP-20_W7.62mm" : make_params(mm(1.03), 20, 'DIP-20_W7.62mm', 90),
    "DIP-22_W7.62mm" : make_params(mm(1.1), 22, 'DIP-22_W7.62mm', 90),
    "DIP-24_W7.62mm" : make_params(mm(1.25), 24, 'DIP-24_W7.62mm', 90),
    "DIP-22_W10.16mm" : make_paramsm(mm(1.1), 22, 'DIP-22_W10.16mm', 90),
    "DIP-24_W10.16mm" : make_paramsm(mm(1.25), 24, 'DIP-24_W10.16mm', 90),
    "DIP-28_W7.62mm" : make_params(mm(1.4), 28, 'DIP-28_W7.62mm', 90),
    "DIP-24_W15.24mm" : make_paramsw(mm(1.25), 24, 'DIP-24_W15.24mm', 90),
    "DIP-28_W15.24mm" : make_paramsw(mm(1.4), 28, 'DIP-28_W15.24mm', 90),
    "DIP-32_W15.24mm" : make_paramsw(mm(1.63), 32, 'DIP-32_W15.24mm', 90),
    "DIP-40_W15.24mm" : make_paramsw(mm(2), 40, 'DIP-40_W15.24mm', 90),
    "DIP-48_W15.24mm" : make_paramsw(mm(2.42), 48, 'DIP-48_W15.24mm', 90),
    "DIP-64_W15.24mm" : make_paramsw(mm(3.26), 64, 'DIP-64_W15.24mm', 90),

    # 64-Lead Shrink Plastic Dual In-Line (SP) 750mil Body
    "DIP-64_W22.86mm" : Params(
        D = mm(2.27),   # package length
        E1 = mm(0.670),  # package width
        E = mm(0.760),  # shoulder to shoulder width (includes pins)
        A1 = mm(0.02),  # base to seating plane
        A2 = mm(0.150),   # package height

        b1 = mm(0.040), # upper lead width
        b = mm(0.018),  # lower lead width
        e = mm(0.070),   # pin to pin distance

        npins = 64,  # total number of pins
        modelName = 'DIP-64_W22.86mm',  # Model Name
        rotation = 0    # rotation if required
    ),
}

#all_params_base = {  #kicad naming
#    "DIP08" : Params(
#        D = 9.27,   # package length
#        E1 = 6.35,  # package width
#        E = 7.874,  # shoulder to shoulder width (includes pins)
#        A1 = 0.38,  # base to seating plane
#        A2 = 3.3,   # package height
#
#        b1 = 1.524, # upper lead width
#        b = 0.457,  # lower lead width
#        e = 2.54,   # pin to pin distance
#
#        npins = 8,  # total number of pins
#        modelName = 'dip_8_300',  # Model Name
#        rotation = 180    # rotation if required
#    ),
#
#    "DIP06" : make_params(7.05, 6, 'dip_6_300', 180),
#    "DIP14" : make_params(19.05, 14, 'dip_14_300', 180),
#    "DIP16" : make_params(mm(0.755), 16, 'dip_16_300', 180),
#    "DIP18" : make_params(mm(0.9), 18, 'dip_18_300', 180),
#    "DIP20" : make_params(mm(1.03), 20, 'dip_20_300', 180),
#    "DIP22" : make_params(mm(1.1), 22, 'dip_22_300', 180),
#    "DIP24" : make_params(mm(1.25), 24, 'dip_24_300', 180),
#    "DIP28" : make_params(mm(1.4), 28, 'dip_28_300', 180),
#    "DIP22-6" : make_paramsw(mm(1.1), 22, 'dip_22_600', 180),
#    "DIP24-6" : make_paramsw(mm(1.25), 24, 'dip_24_600', 180),
#    "DIP28-6" : make_paramsw(mm(1.4), 28, 'dip_28_600', 180),
#    "DIP32-6" : make_paramsw(mm(1.63), 32, 'dip_32_600', 180),
#    "DIP40-6" : make_paramsw(mm(2), 40, 'dip_40_600', 180),
#    "DIP48-6" : make_paramsw(mm(2.42), 48, 'dip_48_600', 180),
#    "DIP52-6" : make_paramsw(mm(2.6), 52, 'dip_52_600', 180),
#
#    # 64-Lead Shrink Plastic Dual In-Line (SP) 750mil Body
#    "DIP64-75" : Params(
#        D = mm(2.27),   # package length
#        E1 = mm(0.670),  # package width
#        E = mm(0.760),  # shoulder to shoulder width (includes pins)
#        A1 = mm(0.02),  # base to seating plane
#        A2 = mm(0.150),   # package height
#
#        b1 = mm(0.040), # upper lead width
#        b = mm(0.018),  # lower lead width
#        e = mm(0.070),   # pin to pin distance
#
#        npins = 64,  # total number of pins
#        modelName = 'dip_64_75',  # Model Name
#        rotation = 90    # rotation if required
#    ),
#}

def make_dip(params):
    # dimensions for PDIP-8
    D = params.D    # package length
    E1 = params.E1  # package width
    E = params.E    # package shoulder-to-shoulder width
    A1 = params.A1  # package board seperation
    A2 = params.A2  # package height

    b1 = params.b1  # pin width
    b = params.b    # pin width
    e = params.e    # pin center to center distance (pitch)

    npins = params.npins  # number of pins

    modelName = params.modelName
    
    # common dimensions
    L = 3.3 # tip to seating plane
    c = 0.254 # lead thickness

    fp_r = 0.8      # first pin indicator radius
    fp_d = 0.2      # first pin indicator depth
    fp_t = 0.4      # first pin indicator distance from edge
    ef = 0.0 # 0.05,      # fillet of edges  Note: bigger bytes model with fillet and possible geometry errorsy TBD

    ti_r = 0.75     # top indicator radius
    ti_d = 0.5      # top indicator depth
   
    
    the = 12.0      # body angle in degrees
    tb_s = 0.15     # top part of body is that much smaller

    # calculated dimensions
    A = A1 + A2

    A2_t = (A2-c)/2.# body top part height
    A2_b = A2_t     # body bottom part height
    D_b = D-2*tan(radians(the))*A2_b # bottom length
    E1_b = E1-2*tan(radians(the))*A2_b # bottom width
    D_t1 = D-tb_s # top part bottom length
    E1_t1 = E1-tb_s # top part bottom width
    D_t2 = D_t1-2*tan(radians(the))*A2_t # top part upper length
    E1_t2 = E1_t1-2*tan(radians(the))*A2_t # top part upper width

    case = cq.Workplane(cq.Plane.XY()).workplane(offset=A1).rect(D_b, E1_b). \
           workplane(offset=A2_b).rect(D, E1).workplane(offset=c).rect(D,E1). \
           rect(D_t1,E1_t1).workplane(offset=A2_t).rect(D_t2,E1_t2). \
           loft(ruled=True)

    # draw top indicator
    case = case.faces(">Z").center(D_b/2., 0).hole(ti_r*2, ti_d)

    # draw 1st pin (side pin shape)
    x = e*(npins/4.-0.5) # center x position of first pin
    ty = (A2+c)/2.+A1 # top point (max z) of pin

    # draw the side part of the pin
    pin = cq.Workplane("XZ", (x, E/2., 0)).\
          moveTo(+b/2., ty).line(0, -(L+ty-b)).line(-b/4.,-b).line(-b/2.,0).\
          line(-b/4.,b).line(0,L-b).line(-(b1-b)/2.,0).line(0,ty).close().extrude(c)

    # draw the top part of the pin
    pin = pin.faces(">Z").workplane().center(-(b1+b)/4.,c/2.).\
          rect((b1+b)/2.,-E/2.,centered=False).extrude(-c)

    # fillet the corners
    def fillet_corner(pina):
        BS = cq.selectors.BoxSelector
        return pina.edges(BS((1000, E/2.-c-0.001, ty-c-0.001), (-1000, E/2.-c+0.001, ty-c+0.001))).\
            fillet(c/2.).\
            edges(BS((1000, E/2.-0.001, ty-0.001), (-1000, E/2.+0.001, ty+0.001))).\
            fillet(1.5*c)

    def chamfer_corner(pina):
        BS = cq.selectors.BoxSelector
        return pina.edges(BS((1000, E/2.-c-0.001, ty-c-0.001), (-1000, E/2.-c+0.001, ty-c+0.001))).\
            chamfer(c/0.18).\
            edges(BS((1000, E/2.-0.001, ty-0.001), (-1000, E/2.+0.001, ty+0.001))).\
            chamfer(6.*c)

    if "W10.16mm" in ModelName and "DIP-22" not in ModelName and "DIP-24" not in ModelName:
        pin = chamfer_corner(pin)
    else:
        pin = fillet_corner(pin)
        
    if npins/2>2:
        # draw the 2nd pin (regular pin shape)
        x = e*(npins/4.-0.5-1) # center x position of 2nd pin
        pin2 = cq.Workplane("XZ", (x, E/2., 0)).\
            moveTo(b1/2., ty).line(0, -ty).line(-(b1-b)/2.,0).line(0,-L+b).\
            line(-b/4.,-b).line(-b/2.,0).line(-b/4.,b).line(0,L-b).\
            line(-(b1-b)/2.,0).line(0,ty).\
            close().extrude(c)
    
        # draw the top part of the pin
        pin2 = pin2.faces(">Z").workplane().center(0,-E/4.).rect(b1,-E/2.).extrude(-c)
        #pin2 = fillet_corner(pin2)
        if "W10.16mm" in ModelName and "DIP-22" not in ModelName and "DIP-24" not in ModelName:
            pin2 = chamfer_corner(pin2)
        else:
            pin2 = fillet_corner(pin2)

        # create other pins (except last one)
        pins = [pin, pin2]
        for i in range(2,npins/2-1):
            pin_i = pin2.translate((-e*(i-1),0,0))
            pins.append(pin_i)
    else:
        pins = [pin,]
    # create last pin (mirrored 1st pin)
    x = -e*(npins/4.-0.5)
    pinl = cq.Workplane("XZ", (x, E/2., 0)).\
           moveTo(-b/2., ty).line(0, -(L+ty-b)).line(b/4.,-b).line(b/2.,0).\
           line(b/4.,b).line(0,L-b).line((b1-b)/2.,0).line(0,ty).close().\
           extrude(c).\
           faces(">Z").workplane().center(-(b1+b)/4.,c/2.).\
           rect((b1+b)/2.,-E/2.,centered=False).extrude(-c)
    #pinl = fillet_corner(pinl)
    if "W10.16mm" in ModelName and "DIP-22" not in ModelName and "DIP-24" not in ModelName: #this has to be reworked :)
        pinl = chamfer_corner(pinl)
    else:
        pinl = fillet_corner(pinl)

    pins.append(pinl)

    def union_all(objects):
        o = objects[0]
        for i in range(1,len(objects)):
            o = o.union(objects[i])
        return o

    # union all pins
    pins = union_all(pins)

    # create other side of the pins (mirror would be better but there
    # is no solid mirror API)
    pins = pins.union(pins.rotate((0,0,0), (0,0,1), 180))

    # finishing touches
    BS = cq.selectors.BoxSelector
    if ef!=0:
        case = case.edges(BS((D_t2/2.+0.1, E1_t2/2., 0), (D/2.+0.1, E1/2.+0.1, A2))).fillet(ef)
        case = case.edges(BS((-D_t2/2., E1_t2/2., 0), (-D/2.-0.1, E1/2.+0.1, A2))).fillet(ef)
        case = case.edges(BS((-D_t2/2., -E1_t2/2., 0), (-D/2.-0.1, -E1/2.-0.1, A2))).fillet(ef)
        case = case.edges(BS((D_t2/2., -E1_t2/2., 0), (D/2.+0.1, -E1/2.-0.1, A2))).fillet(ef)
        case = case.edges(BS((D/2.,E1/2.,A-ti_d-0.001), (-D/2.,-E1/2.,A+0.1))).fillet(ef)
    ## else:
    ##     case = case.edges(BS((D_t2/2.+0.1, E1_t2/2., 0), (D/2.+0.1, E1/2.+0.1, A2)))
    ##     case = case.edges(BS((-D_t2/2., E1_t2/2., 0), (-D/2.-0.1, E1/2.+0.1, A2)))
    ##     case = case.edges(BS((-D_t2/2., -E1_t2/2., 0), (-D/2.-0.1, -E1/2.-0.1, A2)))
    ##     case = case.edges(BS((D_t2/2., -E1_t2/2., 0), (D/2.+0.1, -E1/2.-0.1, A2)))
    ##     case = case.edges(BS((D/2.,E1/2.,A-ti_d-0.001), (-D/2.,-E1/2.,A+0.1)))

    # add first pin indicator
    ## maui case = case.faces(">Z").workplane().center(D_t2/2.-fp_r-fp_t,E1_t2/2.-fp_r-fp_t).\
    ## maui        hole(fp_r*2, fp_d)

    # extract pins from the case
    case = case.cut(pins)
    #mvX = (npins*e/4+e/2)
    #mvY = (E-c)/2
    #case = case.translate ((-mvX,-mvY,0))
    #pins = pins.translate ((-mvX,-mvY,0))
    
    return (case, pins)

## def shapeToMesh(shape, color):
##     mesh_data = shape.tessellate(1)
##     return Mesh(points = mesh_data[0],
##                 faces = mesh_data[1],
##                 color = color)

def make_one(variant, filename):
    """Generates an X3D file for given variant. Variants parameters must
    be entered into `all_params` data structure.
    """
    print("Generating DIL package model for %s variant..." % variant)
    case, pins = make_dip(all_params[variant])
##     exportX3D([shapeToMesh(case.toFreecad(), case_color),
##                shapeToMesh(pins.toFreecad(), pins_color)],
##               filename)
    print("Done generating DIL %s variant." % variant)

def run():
    ## # get variant names from command line

    return
    ## if len(sys.argv) < 2:
    ##     print("No variant name is given!")
    ##     return
    ##
    ## if sys.argv[1] == "all":
    ##     variants = all_params.keys()
    ## else:
    ##     variants = sys.argv[1:]
    ##
    ## outdir = os.path.abspath("./generated_dip/")
    ## if not os.path.exists(outdir):
    ##     os.makedirs(outdir)
    ##
    ## for variant in variants:
    ##     if not variant in all_params:
    ##         print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
    ##         continue
    ##     make_one(variant, outdir + ("/%s.x3d" % variant))

# when run from freecad-cadquery
if __name__ == "temp.module":

    ModelName=""
    ## Newdoc = FreeCAD.newDocument('mydip')
    ## App.setActiveDocument(ModelName)
    ## Gui.ActiveDocument=Gui.getDocument(ModelName)
    ## case, pins = make_dip(all_params["DIP08"])
    ## color_attr=case_color+(0,)
    ## show(case, color_attr)
    ## #FreeCAD.Console.PrintMessage(pins_color)
    ## color_attr=pins_color+(0,)
    ## #FreeCAD.Console.PrintMessage(color_attr)
    ## show(pins, color_attr)
    ##
    ## show(case, (80, 80, 80, 0))
    ## show(pins)

#import step_license as L
import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    full_path=os.path.realpath(__file__)
    expVRML.say(full_path)
    scriptdir=os.path.dirname(os.path.realpath(__file__))
    expVRML.say(scriptdir)
    sub_path = full_path.split(scriptdir)
    expVRML.say(sub_path)
    sub_dir_name =full_path.split(os.sep)[-2]
    expVRML.say(sub_dir_name)
    sub_path = full_path.split(sub_dir_name)[0]
    expVRML.say(sub_path)
    models_dir=sub_path+"_3Dmodels"
    #expVRML.say(models_dir)
    #stop

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building DIP-8_W7.62mm')
        model_to_build='DIP-8_W7.62mm'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]
    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        #ModelName = all_params[variant].modelName
        #Newdoc = FreeCAD.newDocument(ModelName)
        #App.setActiveDocument(ModelName)
        #Gui.ActiveDocument=Gui.getDocument(ModelName)
        #case, pins = make_dip(all_params[variant])

        ModelName = all_params[variant].modelName
        CheckedModelName = ModelName.replace('.', '')
        CheckedModelName = CheckedModelName.replace('-', '_')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        #case, pins, pinmark = make_qfn(all_params[variant])
        case, pins = make_dip(all_params[variant])

        # color_attr=case_color+(0,)
        # show(case, color_attr)
        # #FreeCAD.Console.PrintMessage(pins_color)
        # color_attr=pins_color+(0,)
        # #FreeCAD.Console.PrintMessage(color_attr)
        # show(pins, color_attr)
        #doc = FreeCAD.ActiveDocument
        #objs=GetListOfObjects(FreeCAD, doc)

        show(case)
        show(pins)
        #show(pinmark)
        #stop
        
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)

        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],pins_color)
        #Color_Objects(Gui,objs[2],marking_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        #col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        material_substitutions={
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pins_color_key
            #col_mark[:-1]:marking_color_key
        }
        expVRML.say(material_substitutions)

        FuseObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[1].Name)
        doc.Label=ModelName
        del objs
        #objs=GetListOfObjects(FreeCAD, doc)
        #FuseObjs_wColors(FreeCAD, FreeCADGui,
        #                doc.Name, objs[0].Name, objs[1].Name)
        #doc.Label=ModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label=ModelName
        restore_Main_Tools()

        # objs=GetListOfObjects(FreeCAD, doc)
        # objs[0].Label=ModelName
        # restore_Main_Tools()
        #rotate if required
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
            z_RotateObject(doc, rot)
        npins=all_params[variant].npins
        e=all_params[variant].e
        E=all_params[variant].E
        c= 0.254 # lead thickness
        mvY = (npins*e/4-e/2)
        mvX = (E-c)/2
        s = objs[0].Shape
        shape=s.copy()
        shape.Placement=s.Placement;
        shape.translate((+mvX,-mvY,0))
        objs[0].Placement=shape.Placement
        #case = case.translate ((-mvX,-mvY,0))
        #pins = pins.translate ((-mvX,-mvY,0))
        # out_dir=destination_dir
        # if not os.path.exists(out_dir):
        #     os.makedirs(out_dir)
        # #out_dir="./generated_qfp/"
        # # export STEP model
        # exportSTEP(doc,ModelName,out_dir)
        script_dir=os.path.dirname(os.path.realpath(__file__))
        #models_dir=script_dir+"/../_3Dmodels"
        expVRML.say(models_dir)
        out_dir=models_dir+destination_dir
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        #out_dir="./generated_qfp/"
        # export STEP model
        exportSTEP(doc, ModelName, out_dir)
        if LIST_license[0]=="":
            LIST_license=Lic.LIST_int_license
            LIST_license.append("")
        Lic.addLicenseToStep(out_dir+'/', ModelName+".step", LIST_license,\
                           STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

        # scale and export Vrml model
        scale=1/2.54
        #exportVRML(doc,ModelName,scale,out_dir)
        objs=GetListOfObjects(FreeCAD, doc)
        expVRML.say("######################################################################")
        expVRML.say(objs)
        expVRML.say("######################################################################")
        export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
        export_file_name=out_dir+os.sep+ModelName+'.wrl'
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
        #expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
        #scale=0.3937001
        #exportVRML(doc,ModelName,scale,out_dir)
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()

        #FreeCADGui.ActiveDocument.activeObject.BoundingBox = True


        ## run()

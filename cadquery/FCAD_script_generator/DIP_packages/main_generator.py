#!/usr/bin/python
# -*- coding: utf8 -*-
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
__author__ = "maurice, hyOzd, Stefan"
__Comment__ = 'make DIP ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.3 14/08/2015"

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import datetime
import copy
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
#from Gui.Command import *


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


#################################################################################################

# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements
# Sphinx workaround #1
try:
    QtGui
except NameError:
    QtGui = None

try:
    # Gui.SendMsgToActiveView("Run")
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery
    cq = cadquery
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

# Sphinx workaround #2
try:
    cq
    checkRequirements(cq)
except NameError:
    cq = None
#

def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        importlib.reload (lib)


# Import cad_tools
import cq_cad_tools
# Reload tools
reload_lib(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements, runGeometryCheck

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print("CQ 030 doesn't open example file")


import cq_parameters  # modules parameters
from cq_parameters import *


# case_color = (0.1, 0.1, 0.1)
# pins_color = (0.9, 0.9, 0.9)
#case_color = (50, 50, 50)
#pins_color = (230, 230, 230)
destination_dir="/DIP_packages"
# rotation = 0


CASE_THT_TYPE = 'tht'
CASE_SMD_TYPE = 'smd'
CASE_THTSMD_TYPE = 'thtsmd'
_TYPES = [CASE_THT_TYPE, CASE_SMD_TYPE ]


CORNER_CHAMFER_TYPE = 'chamfer'
CORNER_FILLET_TYPE = 'fillet'
_CORNER = [CORNER_CHAMFER_TYPE, CORNER_FILLET_TYPE]

def make_case(params, type, modelName):

    D = params.D    # package length
    E1 = params.E1  # package width
    E = params.E    # package shoulder-to-shoulder width
    A1 = params.A1  # package board seperation
    A2 = params.A2  # package height

    b1 = params.b1  # pin width
    b = params.b    # pin width
    e = params.e    # pin center to center distance (pitch)

    npins = params.npins  # number of pins

    corner = params.corner
    excludepins = params.excludepins

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

    if (params.type == CASE_SMD_TYPE):
        mvX = (npins*e/4+e/2)
        mvX = (((npins / 2.) - 1.) / 2) * e
        mvY = (E-c)/2
        case = case.translate ((mvX,mvY,0))

    return (case)


def make_pins_tht(params, type, modelName):

    D = params.D    # package length
    E1 = params.E1  # package width
    E = params.E    # package shoulder-to-shoulder width
    A1 = params.A1  # package board seperation
    A2 = params.A2  # package height

    b1 = params.b1  # pin width
    b = params.b    # pin width
    e = params.e    # pin center to center distance (pitch)

    npins = params.npins  # number of pins

    corner = params.corner
    excludepins = params.excludepins

    # common dimensions
    L = 3.3 # tip to seating plane
    c = 0.254 # lead thickness


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

    if (corner == CORNER_CHAMFER_TYPE):
        pin = chamfer_corner(pin)
    else:
        pin = fillet_corner(pin)

    pinsL = [pin]
    pinsR = [pin.translate((0,0,0))]

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
        if (corner == CORNER_CHAMFER_TYPE):
            pin2 = chamfer_corner(pin2)
        else:
            pin2 = fillet_corner(pin2)

        # create other pins (except last one)
        pinsL.append(pin2)
        pinsR.append(pin2.translate((0,0,0)))
        for i in range(2,npins//2-1):
            pin_i = pin2.translate((-e*(i-1),0,0))
            pinsL.append(pin_i)
            pinsR.append(pin_i.translate((0,0,0)))

    # create last pin (mirrored 1st pin)
    x = -e*(npins/4.-0.5)
    pinl = cq.Workplane("XZ", (x, E/2., 0)).\
           moveTo(-b/2., ty).line(0, -(L+ty-b)).line(b/4.,-b).line(b/2.,0).\
           line(b/4.,b).line(0,L-b).line((b1-b)/2.,0).line(0,ty).close().\
           extrude(c).\
           faces(">Z").workplane().center(-(b1+b)/4.,c/2.).\
           rect((b1+b)/2.,-E/2.,centered=False).extrude(-c)
    #pinl = fillet_corner(pinl)
    if (corner == CORNER_CHAMFER_TYPE):
        pinl = chamfer_corner(pinl)
    else:
        pinl = fillet_corner(pinl)

    pinsL.append(pinl)
    pinsR.append(pinl.translate((0,0,0)))

#    FreeCAD.Console.PrintMessage("\r\n\r\n")
#    ttts = "pins = " + str(len(pins)) + "\r\n"
#    FreeCAD.Console.PrintMessage(ttts)
#    ttts = "pins2 = " + str(len(pins2)) + "\r\n"
#    FreeCAD.Console.PrintMessage(ttts)
#    FreeCAD.Console.PrintMessage("\r\n\r\n")

    def union_all(objects):
        o = objects[0]
        for i in range(1,len(objects)):
            o = o.union(objects[i])
        return o

    FreeCAD.Console.PrintMessage('\r\n')
    pinsLNew = []
    pinsRNew = []
    AddPinLeft = True
    AddPinRight = True
    tts = "len(pinsL) " + str(len(pinsL)) + "\r\n"
    FreeCAD.Console.PrintMessage(tts)
    tts = "len(pinsR) " + str(len(pinsR)) + "\r\n"
    FreeCAD.Console.PrintMessage(tts)
    for ei in excludepins:
        tts = "excludepins " + str(ei) + "\r\n"
        FreeCAD.Console.PrintMessage(tts)
    for i in range(0, npins//2):
        AddPinLeft = True
        for ei in excludepins:
            if ((i + 1) == ei):
                AddPinLeft = False
        if (AddPinLeft):
            tts = "Adding to pinsLNew " + str(i) + "\r\n"
            FreeCAD.Console.PrintMessage(tts)
            pinsLNew.append(pinsL[i])

    for i in range(npins//2, npins):
        AddPinRight = True
        for ei in excludepins:
            if ((i + 1) == ei):
                AddPinRight = False
        if (AddPinRight):
            tts = "Adding to pinsRNew " + str(i - (npins/2)) + "\r\n"
            FreeCAD.Console.PrintMessage(tts)
            pinsRNew.append(pinsR[i - (npins//2)])

    # union all pins
    pinsLT = union_all(pinsLNew)
    pinsRT = union_all(pinsRNew)

    # create other side of the pins (mirror would be better but there
    # is no solid mirror API)
    pinsT = pinsLT.union(pinsRT.rotate((0,0,0), (0,0,1), 180))

    #mvX = (npins*e/4+e/2)
    #mvY = (E-c)/2
    #pins = pins.translate ((-mvX,-mvY,0))

    return (pinsT)


def make_pins_smd(params, type, modelName):

    D = params.D    # package length
    E1 = params.E1  # package width
    E = params.E    # package shoulder-to-shoulder width
    A1 = params.A1  # package board seperation
    A2 = params.A2  # package height

    b1 = params.b1  # pin width
    b = params.b    # pin width
    e = params.e    # pin center to center distance (pitch)

    npins = params.npins  # number of pins

    corner = params.corner
    excludepins = params.excludepins

    # common dimensions
    L = 3.3 # tip to seating plane
    c = 0.254 # lead thickness

    # fillet the corners
    def fillet_corner(pina):
        BS = cq.selectors.BoxSelector
        return pina.\
            edges(BS((1000, E/2.-c-0.001,   ty-c-0.001), (-1000, E/2.-c+0.001, ty-c+0.001))).fillet(c/2.).\
            edges(BS((1000, E/2.-c-0.001,       -0.001), (-1000, E/2.-c+0.001,     +0.001))).fillet(1.5*c).\
            edges(BS((1000, E/2.-0.001,       ty-0.001), (-1000, E/2.+0.001,     ty+0.001))).fillet(1.5*c).\
            edges(BS((1000, E/2.-0.001,        c-0.001), (-1000, E/2.+0.001,     c+0.001))).fillet(c/2.)

    def chamfer_corner(pina):
        BS = cq.selectors.BoxSelector
        return pina.\
            edges(BS((1000, E/2.-c-0.001, ty-c-0.001), (-1000, E/2.-c+0.001, ty-c+0.001))).chamfer(c/0.18).\
            edges(BS((1000, E/2.-0.001, ty-0.001), (-1000, E/2.+0.001, ty+0.001))).chamfer(6.*c)


    # draw 1st pin
    x = e*(npins/4.-0.5) # center x position of first pin
    ty = (A2+c)/2.+A1 # top point (max z) of pin

    # draw the side part of the pin
    pin = cq.Workplane("XZ", (x, E/2., 0)). \
        moveTo(-b, 0). \
        lineTo(-b, ty). \
        lineTo(b, ty). \
        lineTo(b, 0). \
        close().extrude(c)

    # draw the top part of the pin
    pin = pin.faces(">Z").workplane().\
        moveTo(-b, 0). \
        lineTo(-b, -E/2.). \
        lineTo(b, -E/2.). \
        lineTo(b, 0). \
        close().extrude(-c)

    # Draw the bottom part of the pin
    pin = pin.faces("<Z").workplane().center(0, -b + c/2.).rect(2*b, 2 * b).extrude(-c)

    if (corner == CORNER_CHAMFER_TYPE):
        pin = chamfer_corner(pin)
    else:
        pin = fillet_corner(pin)

    pinsL = [pin]
    pinsR = [pin.translate((0,0,0))]
#
#
#
    if npins/2>2:
        # draw the 2nd pin (regular pin shape)
        x = e*(npins/4.-0.5-1) # center x position of 2nd pin
        pin2 = cq.Workplane("XZ", (x, E/2., 0)). \
            moveTo(-b, 0). \
            lineTo(-b, ty). \
            lineTo(b, ty). \
            lineTo(b, 0). \
            close().extrude(c)

        # draw the top part of the pin
        pin2 = pin2.faces(">Z").workplane().center(0, -(4. * b) + c/2.).rect(2*b, 8 * b).extrude(-c)

        # Draw the bottom part of the pin
        pin2 = pin2.faces("<Z").workplane().center(0, -b + c/2.).rect(2*b, 2 * b).extrude(-c)

        if (corner == CORNER_CHAMFER_TYPE):
            pin2 = chamfer_corner(pin2)
        else:
            pin2 = fillet_corner(pin2)

        # create other pins (except last one)
        pinsL.append(pin2)
        pinsR.append(pin2.translate((0,0,0)))
        for i in range(2,npins//2-1):
            pin_i = pin2.translate((-e*(i-1),0,0))
            pinsL.append(pin_i)
            pinsR.append(pin_i.translate((0,0,0)))


    # create last pin (mirrored 1st pin)
    x = -e*(npins/4.-0.5)
    pinl = cq.Workplane("XZ", (x, E/2., 0)). \
        moveTo(-b, 0). \
        lineTo(-b, ty). \
        lineTo(b, ty). \
        lineTo(b, 0). \
        close().extrude(c)
    # draw the top part of the pin
    pinl = pinl.faces(">Z").workplane().center(0, -(4. * b) + c/2.).rect(2*b, 8 * b).extrude(-c)

    # Draw the bottom part of the pin
    pinl = pinl.faces("<Z").workplane().center(0, -b + c/2.).rect(2*b, 2 * b).extrude(-c)
    if (corner == CORNER_CHAMFER_TYPE):
        pinl = chamfer_corner(pinl)
    else:
        pinl = fillet_corner(pinl)

    pinsL.append(pinl)
    pinsR.append(pinl.translate((0,0,0)))


    def union_all(objects):
        o = objects[0]
        for i in range(1,len(objects)):
            o = o.union(objects[i])
        return o


    FreeCAD.Console.PrintMessage('\r\n')
    pinsLNew = []
    pinsRNew = []
    AddPinLeft = True
    AddPinRight = True
    tts = "len(pinsL) " + str(len(pinsL)) + "\r\n"
    FreeCAD.Console.PrintMessage(tts)
    tts = "len(pinsR) " + str(len(pinsR)) + "\r\n"
    FreeCAD.Console.PrintMessage(tts)
    for ei in excludepins:
        tts = "excludepins " + str(ei) + "\r\n"
        FreeCAD.Console.PrintMessage(tts)
    for i in range(0, npins//2):
        AddPinLeft = True
        for ei in excludepins:
            if ((i + 1) == ei):
                AddPinLeft = False
        if (AddPinLeft):
            tts = "Adding to pinsLNew " + str(i) + "\r\n"
            FreeCAD.Console.PrintMessage(tts)
            pinsLNew.append(pinsL[i])

    for i in range(npins//2, npins):
        AddPinRight = True
        for ei in excludepins:
            if ((i + 1) == ei):
                AddPinRight = False
        if (AddPinRight):
            tts = "Adding to pinsRNew " + str(i - (npins/2)) + "\r\n"
            FreeCAD.Console.PrintMessage(tts)
            pinsRNew.append(pinsR[i - (npins//2)])

    # union all pins
    pinsLT = union_all(pinsLNew)
    pinsRT = union_all(pinsRNew)

    # create other side of the pins (mirror would be better but there
    # is no solid mirror API)
    pinsT = pinsLT.union(pinsRT.rotate((0,0,0), (0,0,1), 180))

    mvX = (((npins / 2.) - 1.) / 2) * e
    mvY = (E-c)/2
    pinsT = pinsT.translate ((mvX,mvY,0))

    return (pinsT)


def make_one(variant, filename, type):
    """Generates an X3D file for given variant. Variants parameters must
    be entered into `all_params` data structure.
    """
    print("Generating DIL package model for %s variant..." % variant)
    case, pins = make_dip(all_params[variant], TYPE_THT)
##     exportX3D([shapeToMesh(case.toFreecad(), case_color),
##                shapeToMesh(pins.toFreecad(), pins_color)],
##               filename)
    print("Done generating DIL %s variant." % variant)


def make_3D_model(models_dir, variant):

    LIST_license = ["",]
    modelName = all_params[variant].modelName

    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)

    case = make_case(all_params[variant], type, modelName)

    if (all_params[variant].type == CASE_THT_TYPE):
        pins = make_pins_tht(all_params[variant], type, modelName)

    if (all_params[variant].type == CASE_SMD_TYPE):
        pins = make_pins_smd(all_params[variant], type, modelName)


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
    doc.Label = CheckedmodelName
    del objs
    #objs=GetListOfObjects(FreeCAD, doc)
    #FuseObjs_wColors(FreeCAD, FreeCADGui,
    #                doc.Name, objs[0].Name, objs[1].Name)
    #doc.Label=modelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = CheckedmodelName
    restore_Main_Tools()

    # objs=GetListOfObjects(FreeCAD, doc)
    # objs[0].Label=modelName
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
    # exportSTEP(doc,modelName,out_dir)
    script_dir=os.path.dirname(os.path.realpath(__file__))
    #models_dir=script_dir+"/../_3Dmodels"
    expVRML.say(models_dir)
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    #out_dir="./generated_qfp/"
    # export STEP model
    exportSTEP(doc, modelName, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', modelName+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,modelName,scale,out_dir)
    objs=GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir+os.sep+modelName+'.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    #expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
    #scale=0.3937001
    #exportVRML(doc,modelName,scale,out_dir)
    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, modelName,out_dir)
    #display BBox
    Gui.activateWorkbench("PartWorkbench")
    Gui.SendMsgToActiveView("ViewFit")
    Gui.activeDocument().activeView().viewAxometric()

    #FreeCADGui.ActiveDocument.activeObject.BoundingBox = True


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

    modelName=""
    ## Newdoc = FreeCAD.newDocument('mydip')
    ## App.setActiveDocument(modelName)
    ## Gui.ActiveDocument=Gui.getDocument(modelName)
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

    buildAllSMD = 0

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building DIP-8_W7.62mm')
        model_to_build='DIP-8_W7.62mm'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()

    if model_to_build == "allsmd":
        variants = all_params.keys()
        buildAllSMD = 1
    else:
        variants = [model_to_build]


    if (buildAllSMD == 1):
        for variant in variants:
            if (all_params[variant].type == CASE_SMD_TYPE):
                FreeCAD.Console.PrintMessage('\r\n'+variant)
                make_3D_model(models_dir, variant)

    else:
        for variant in variants:
            FreeCAD.Console.PrintMessage('\r\n'+variant)
            if not variant in all_params:
                print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
                continue

            make_3D_model(models_dir, variant)

        ## run()

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#

## file of parametric definitions

import collections
from collections import namedtuple

import math

import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui

import shaderColors
import exportPartToVRML as expVRML

## base parametes & model
import collections
from collections import namedtuple

# Import cad_tools
import cq_cad_tools
# Reload tools
from cq_cad_tools import reload_lib
reload_lib(cq_cad_tools)

# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

# Sphinx workaround #1
try:
    QtGui
except NameError:
    QtGui = None
#

try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
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

#checking requirements
checkRequirements(cq)


def make_modelfileName_Common(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name
    
    return modelname

    
def get_body_offset(params):

    A2 = params.A2

    BH = 0.0
    if A2 != None:
        BH = A2
        
    return BH
    

def get_battery_size(params):

    cellsize = params.cellsize          # Battery type

    #
    # https://en.wikipedia.org/wiki/List_of_battery_sizes
    #
        
    if cellsize == 'A':
        return 17.00, 50.00

    if cellsize == 'AA':
        return 14.50, 50.50

    if cellsize == 'AAA':
        return 10.50, 44.50

    if cellsize == 'AAAA':
        return 08.30, 42.50
        
    if cellsize == 'B':
        return 21.5, 60.00
        
    if cellsize == 'C':
        return 14.50, 50.50

    if cellsize == 'D':
        return 34.20, 61.50

    if cellsize == '18650':
        return 18.00, 65.00

    if cellsize == 'CR1216':
        return 12.50, 1.6

    if cellsize == 'CR1220':
        return 12.00, 5.0

    if cellsize == 'CR2025':
        return 20.00, 2.5

    if cellsize == 'CR2450':
        return 24.5, 5.0

    return 0.0, 0.0

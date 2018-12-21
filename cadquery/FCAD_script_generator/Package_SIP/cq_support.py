
# -*- coding: utf8 -*-
#!/usr/bin/python
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
reload(cq_cad_tools)
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

try:
    close_CQ_Example(FreeCAD, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"


class cq_support():

    def __init__(self):
        x = 0

    def make_bend_pin_stand_1(self, pin_w, pin_l, pin_h, ang, dxd, upph):
    
        #
        dx = math.cos(math.radians(ang))
        dy = math.sin(math.radians(ang))
        dtl = (dxd * 0.98) / dx
        ttddh = dtl * dy
        pin2 = cq.Workplane("YZ").workplane(offset=0.0 - (pin_w / 2.0)). \
        moveTo(0.0 - (0.0 - (pin_l / 2.0)), 0.0). \
        lineTo(0.0 - (0.0 - (pin_l / 2.0)), 0.0 - upph). \
        lineTo(0.0 - (dxd - (pin_l / 2.0)), 0.0 - (upph + ttddh)). \
        lineTo(0.0 - (dxd - (pin_l / 2.0)), 0.0 - pin_h). \
        lineTo(0.0 - (dxd + (pin_l / 2.0)), 0.0 - pin_h). \
        lineTo(0.0 - (dxd + (pin_l / 2.0)), 0.0 - (upph + ttddh) + (pin_l / math.sqrt(2))). \
        lineTo(0.0 - (0.0 + (pin_l / 2.0)), 0.0 - (upph - (pin_l / math.sqrt(2)))). \
        lineTo(0.0 - (0.0 + (pin_l / 2.0)), 0.0). \
        close(). \
        extrude(pin_w)
        pin2 = pin2.faces("+Y").edges("#Z").fillet(pin_l / 2.1)
        pin2 = pin2.faces("<Y").edges(">Z").fillet(pin_l)
        pin2 = pin2.faces("<Y").edges("<Z").fillet(pin_l / 2.1)
        pin2 = pin2.faces(">Z").edges("<Y").fillet(pin_l / 2.1)
    
        return pin2


    def make_bend_pin_stand_2(self, pin_w, pin_l, pin_h, ang, dxd):
    
        #
        dx = math.cos(math.degrees(ang))
        dy = math.sin(math.degrees(ang))
        dtl = (dxd * 0.98) / dy
        ttddh = dtl * dx
        pin2 = cq.Workplane("XZ").workplane(offset=0.0 - (pin_w / 2.0)). \
        moveTo(0.0 - (0.0 - (pin_l / 2.0)), 0.0). \
        lineTo(0.0 - (0.0 - (pin_l / 2.0)), 0.0 - 1.0). \
        lineTo(0.0 - (dxd - (pin_l / 2.0)), 0.0 - (1.0 + ttddh)). \
        lineTo(0.0 - (dxd - (pin_l / 2.0)), 0.0 - pin_h). \
        lineTo(0.0 - (dxd + (pin_l / 2.0)), 0.0 - pin_h). \
        lineTo(0.0 - (dxd + (pin_l / 2.0)), 0.0 - (1.0 + ttddh) + (pin_l / math.sqrt(2))). \
        lineTo(0.0 - (0.0 + (pin_l / 2.0)), 0.0 - (1.0 - (pin_l / math.sqrt(2)))). \
        lineTo(0.0 - (0.0 + (pin_l / 2.0)), 0.0). \
        close(). \
        extrude(pin_w)
#        pin2 = pin2.faces("+Y").edges("#Z").fillet(pin_l / 2.1)
#        pin2 = pin2.faces("<Y").edges(">Z").fillet(pin_l)
#        pin2 = pin2.faces("<Y").edges("<Z").fillet(pin_l / 2.1)
#        pin2 = pin2.faces(">Z").edges("<Y").fillet(pin_l / 2.1)
    
        return pin2
     
        
        
        
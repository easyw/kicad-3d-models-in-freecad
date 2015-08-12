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

## to run the script just do: freecad make_gwexport_fc.py modelName
## e.g. c:\freecad\bin\freecad make_gw_export_fc.py SOIC_8

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

__title__ = "make chip capacitors 3D models"
__author__ = "maurice"
__Comment__ = 'make chip capacitos 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3 12/08/2015"

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
from Gui.Command import *

outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

close_CQ_Example(App, Gui)

# from export_x3d import exportX3D, Mesh
import cadquery as cq
from Helpers import show
# maui end


import cq_params_chip_res  # modules parameters
from cq_params_chip_res import *

def make_chip(params):
    # dimensions for chip capacitors
    L = params.L    # package length
    W = params.W    # package width
    T = params.T    # package height

    pb = params.pb  # pin band
    pt = params.pt  # pin thickness

    ef = params.ef  # fillet of edges
    modelName = params.modelName  # Model Name
    rotation = params.rotation   # rotation

    # Create a 3D box based on the dimension variables above and fillet it
    case = cq.Workplane("XY").box(L-4*pt, W, T-4*pt)
    # case.edges("|X").fillet(ef)
    # body.edges("|Z").fillet(ef)
    # translate the object
    case=case.translate((0,0,T/2)).rotate((0,0,0), (0,0,1), 0)
    top = cq.Workplane("XY").box(L-2*pb, W, 2*pt)
    top = top.edges("|X").fillet(ef)
    top=top.translate((0,0,T-pt)).rotate((0,0,0), (0,0,1), 0)


    # Create a 3D box based on the dimension variables above and fillet it
    pin1 = cq.Workplane("XY").box(pb, W, T)
    pin1.edges("|Y").fillet(ef)
    pin1=pin1.translate((-L/2+pb/2,0,T/2)).rotate((0,0,0), (0,0,1), 0)
    pin2 = cq.Workplane("XY").box(pb, W, T)
    pin2.edges("|Y").fillet(ef)
    pin2=pin2.translate((L/2-pb/2,0,T/2)).rotate((0,0,0), (0,0,1), 0)
    pins = pin1.union(pin2)
    #body_copy.ShapeColor=result.ShapeColor

    # extract case from pins
    # case = case.cut(pins)
    pins = pins.cut(case)

    return (case, top, pins)


# The dimensions of the box. These can be modified rather than changing the
# object's code directly.


# when run from freecad-cadquery
if __name__ == "temp.module":

    ModelName=""


# when run from command line
if __name__ == "__main__":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building c_1206_h106')
        model_to_build='1206_h106'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()
        FreeCAD.Console.PrintMessage(variants)
        FreeCAD.Console.PrintMessage('\r\n')
    else:
        variants = [model_to_build]
    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        Newdoc = FreeCAD.newDocument(ModelName)
        App.setActiveDocument(ModelName)
        Gui.ActiveDocument=Gui.getDocument(ModelName)
        case, top, pins = make_chip(all_params[variant])
        color_attr=case_color+(0,)
        show(case, color_attr)
        #FreeCAD.Console.PrintMessage(pins_color)

        color_attr=top_color+(0,)
        show(top, color_attr)

        color_attr=pins_color+(0,)
        #FreeCAD.Console.PrintMessage(color_attr)
        show(pins, color_attr)
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[1].Name)
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
        objs[1].Label="Fusion2"
        FuseObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[1].Name)
        doc.Label=ModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label=ModelName
        restore_Main_Tools()
        #rotate if required
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
            z_RotateObject(doc, rot)
        out_dir=destination_dir
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        #out_dir="./generated_qfp/"
        # export STEP model
        exportSTEP(doc,ModelName,out_dir)

        # scale and export Vrml model
        scale=0.3937001
        exportVRML(doc,ModelName,scale,out_dir)

        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox

        FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True

        ## run()

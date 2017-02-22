# -*- coding: utf8 -*-
#!/usr/bin/python
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

## to run the script just do: freecad make_qfn_export_fc.py modelName
## e.g. c:\freecad\bin\freecad make_qfn_export_fc.py QFN16

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

__title__ = "make QFN ICs 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make QFN ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.3 17/02/2017"

###ToDo: QFN with ARC pad, exposed pad with chamfer

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import datetime
from datetime import datetime
sys.path.append("./exportVRML")
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


outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

#checking requirements
#######################################################################
FreeCAD.Console.PrintMessage("FC Version \r\n")
FreeCAD.Console.PrintMessage(FreeCAD.Version())
FC_majorV=FreeCAD.Version()[0];FC_minorV=FreeCAD.Version()[1]
FreeCAD.Console.PrintMessage('FC Version '+FC_majorV+FC_minorV+'\r\n')

if int(FC_majorV) <= 0:
    if int(FC_minorV) < 15:
        reply = QtGui.QMessageBox.information(None,"Warning! ...","use FreeCAD version >= "+FC_majorV+"."+FC_minorV+"\r\n")


# FreeCAD.Console.PrintMessage(all_params_soic)
FreeCAD.Console.PrintMessage(FreeCAD.ConfigGet("AppHomePath")+'Mod/')
file_path_cq=FreeCAD.ConfigGet("AppHomePath")+'Mod/CadQuery'
if os.path.exists(file_path_cq):
    FreeCAD.Console.PrintMessage('CadQuery exists\r\n')
else:
    file_path_cq=FreeCAD.ConfigGet("UserAppData")+'Mod/CadQuery'
    if os.path.exists(file_path_cq):
        FreeCAD.Console.PrintMessage('CadQuery exists\r\n')
    else:
        msg="missing CadQuery Module!\r\n\r\n"
        msg+="https://github.com/jmwright/cadquery-freecad-module/wiki"
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)

#######################################################################

# CadQuery Gui
from Gui.Command import *

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"


# from export_x3d import exportX3D, Mesh
import cadquery as cq
from Helpers import show
# maui end

#check version
cqv=cq.__version__.split(".")
#say2(cqv)
if int(cqv[0])==0 and int(cqv[1])<3:
    msg = "CadQuery Module needs to be at least 0.3.0!\r\n\r\n"
    reply = QtGui.QMessageBox.information(None, "Info ...", msg)
    say("cq needs to be at least 0.3.0")
    stop

if float(cq.__version__[:-2]) < 0.3:
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    msg+="actual CQ version "+cq.__version__
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)


import cq_params_qfn  # modules parameters
from cq_params_qfn import *

all_params= all_params_qfn

def make_qfn(params):

    c  = params.c
    ef  = params.ef
    cce = params.cce
    fp_r  = params.fp_r
    fp_d  = params.fp_d
    fp_z  = params.fp_z
#    K  = params.K
    L  = params.L
    D  = params.D
    E   = params.E
    A1  = params.A1
    A2  = params.A2
    b   = params.b
    e   = params.e
    m   = params.m
    sq  = params.sq
    npx = params.npx
    npy = params.npy
    mN  = params.modelName
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix

    if params.epad:
        D2 = params.epad[0]
        E2 = params.epad[1]

    A = A1 + A2


    if m == 0:
        case = cq.Workplane("XY").box(D-A1, E-A1, A2)  #margin to see fused pins
    else:
        case = cq.Workplane("XY").box(D, E, A2)  #NO margin, pins don't emerge
    if ef!=0:
        case.edges("|X").fillet(ef)
        case.edges("|Z").fillet(ef)
    #translate the object
    case=case.translate((0,0,A2/2+A1)).rotate((0,0,0), (0,0,1), 0)

    # first pin indicator is created with a spherical pocket
    sphere_r = (fp_r*fp_r/2 + fp_z*fp_z) / (2*fp_z)
    sphere_z = A + sphere_r * 2 - fp_z - sphere_r

    pinmark=cq.Workplane("XZ", (-D/2+fp_d+fp_r, -E/2+fp_d+fp_r, fp_z)).rect(fp_r/2, -2*fp_z, False).revolve().translate((0,0,A))#+fp_z))

    #stop
    if (color_pin_mark==False) and (place_pinMark==True):
        case = case.cut(pinmark)
    # show(pinmark)
    # show(case)
    # stop
    
    if sq: #square pins
        bpin1 = cq.Workplane("XY"). \
            moveTo(b, 0). \
            lineTo(b, L). \
            lineTo(0, L). \
            lineTo(0, 0). \
            close().extrude(c).translate((b/2,E/2,0))
            #close().extrude(c).translate((b/2,E/2,A1/2))
    else:
        bpin1 = cq.Workplane("XY"). \
            moveTo(b, 0). \
            lineTo(b, L-b/2). \
            threePointArc((b/2,L),(0, L-b/2)). \
            lineTo(0, 0). \
            close().extrude(c).translate((b/2,E/2,0))
            #close().extrude(c).translate((b/2,E/2,A1/2))
    bpin=bpin1.rotate((b/2,E/2,A1/2), (0,0,1), 180)

    pins = []
    # create top, bottom side pins
    first_pos = -(npx-1)*e/2
    for i in range(npx):
        if i not in excluded_pins_xmirror:
            pin = bpin.translate((first_pos+i*e, -m, 0))
            pins.append(pin)
        if i not in excluded_pins_x:
            pin = bpin.translate((first_pos+i*e, -m, 0)).\
                rotate((0,0,0), (0,0,1), 180)
            pins.append(pin)

    # create right, left side pins
    first_pos = -(npy-1)*e/2
    for i in range(npy):
        pin = bpin.translate((first_pos+i*e, (D-E)/2-m, 0)).\
            rotate((0,0,0), (0,0,1), 90)
        pins.append(pin)
        pin = bpin.translate((first_pos+i*e, (D-E)/2-m, 0)).\
            rotate((0,0,0), (0,0,1), 270)
        pins.append(pin)

    # create exposed thermal pad if requested
    if params.epad:
        #pins.append(cq.Workplane("XY").box(D2, E2, A1+A1/10).translate((0,0,A1+A1/10)))
        epad = cq.Workplane("XY", (0,0,A1/2)). \
        moveTo(-D2/2+cce, -E2/2). \
        lineTo(D2/2, -E2/2). \
        lineTo(D2/2, E2/2). \
        lineTo(-D2/2, E2/2). \
        lineTo(-D2/2, -E2/2+cce). \
        close().extrude(A1+A1/10)
        pins.append(epad)

    # merge all pins to a single object
    merged_pins = pins[0]
    for p in pins[1:]:
        merged_pins = merged_pins.union(p)
    pins = merged_pins

    #show(pins)
    #sleep
    # extract pins from case
    case = case.cut(pins)

    return (case, pins, pinmark)

import step_license as L


if __name__ == "__main__":
    expVRML.say(expVRML.__file__)
    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

# maui     run()
    color_pin_mark=True
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building qfn16')
        model_to_build='QFN16'
    else:
        model_to_build=sys.argv[2]
        if len(sys.argv)==4:
            FreeCAD.Console.PrintMessage(sys.argv[3]+'\r\n')
            if (sys.argv[3].find('no-pinmark-color')!=-1):
                color_pin_mark=False
            else:
                color_pin_mark=True


    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        excluded_pins_x=() ##no pin excluded
        excluded_pins_xmirror=() ##no pin excluded
        place_pinMark=True ##default =True used to exclude pin mark to build sot23-3; sot23-5; sc70 (asimmetrical pins, no pinmark)

        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        CheckedModelName = ModelName.replace('.', '')
        CheckedModelName = CheckedModelName.replace('-', '_')
        Newdoc = FreeCAD.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        case, pins, pinmark = make_qfn(all_params[variant])


        show(case)
        show(pins)
        show(pinmark)
        #stop
        
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)

        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],pins_color)
        Color_Objects(Gui,objs[2],marking_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        material_substitutions={
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pins_color_key,
            col_mark[:-1]:marking_color_key
        }
        expVRML.say(material_substitutions)
        ## objs[0].Label='body'
        ## objs[1].Label='pins'
        ## objs[2].Label='mark'
        ###
        ## print objs[0].Name, objs[1].Name, objs[2].Name

        ## sleep
        #if place_pinMark==True:
        if (color_pin_mark==True) and (place_pinMark==True):
            CutObjs_wColors(FreeCAD, FreeCADGui,
                           doc.Name, objs[0].Name, objs[2].Name)
        else:
            #removing pinMark
            App.getDocument(doc.Name).removeObject(objs[2].Name)
        ###
        #sleep
        del objs
        objs=GetListOfObjects(FreeCAD, doc)
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
        #out_dir=destination_dir+all_params[variant].dest_dir_prefix+'/'
        script_dir=os.path.dirname(os.path.realpath(__file__))
        expVRML.say(script_dir)
        out_dir=script_dir+os.sep+destination_dir+all_params[variant].dest_dir_prefix
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        #out_dir="./generated_qfp/"
        # export STEP model
        exportSTEP(doc, ModelName, out_dir)
        # scale and export Vrml model
        scale=1/2.54
        #exportVRML(doc,ModelName,scale,out_dir)
        objs=GetListOfObjects(FreeCAD, doc)
        expVRML.say("######################################################################")
        expVRML.say(objs)
        expVRML.say("######################################################################")
        export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
        export_file_name=destination_dir+os.sep+ModelName+'.wrl'
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox
        #FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()

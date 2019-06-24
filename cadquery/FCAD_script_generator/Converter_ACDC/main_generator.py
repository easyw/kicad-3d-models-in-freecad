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

__title__ = "make DIP switch 3D models"
__author__ = "Stefan, based on DIP script"
__Comment__ = 'make DIP switch 3D models exported to STEP and VRML for Kicad StepUP script'

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

# Import cad_tools
import cq_cad_tools
# Reload tools
def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)

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

# Sphinx workaround #2
try:
    cq
    checkRequirements(cq)
except NameError:
    cq = None
#

#checking requirements

try:
    close_CQ_Example(FreeCAD, Gui)
except: # catch *all* exceptions
    print("CQ 030 doesn't open example file")


destination_dir="/Converter_ACDC"
# rotation = 0


import cq_parameters  # modules parameters
from cq_parameters import *

CASE_THT_TYPE = 'tht'
CASE_SMD_TYPE = 'smd'
CASE_THTSMD_TYPE = 'thtsmd'
CASE_THT_N_TYPE = 'tht_n'
_TYPES = [CASE_THT_TYPE, CASE_SMD_TYPE, CASE_THT_N_TYPE ]


CORNER_NONE_TYPE = 'none'
CORNER_CHAMFER_TYPE = 'chamfer'
CORNER_FILLET_TYPE = 'fillet'
_CORNER = [CORNER_NONE_TYPE, CORNER_CHAMFER_TYPE, CORNER_FILLET_TYPE]



def make_case(params):

    L = params.L                    # package length
    W = params.W                    # package width
    H = params.H                    # package height
    A1 = params.A1                    # Body seperation height
    rim = params.rim                # Rim underneath
    rotation = params.rotation        # rotation if required
    pin1corner = params.pin1corner     # Left upp corner relationsship to pin 1
    pin = params.pin                # pin/pad cordinates
    roundbelly = params.roundbelly    # If belly of caseing should be round (or flat)
    pintype = params.pintype        # pin type , like SMD or THT
    
    ff = W / 20.0;

    if ff > 0.25:
        ff = 0.25

    mvX = 0
    mvY = 0
    # Dummy
    case=cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0).rect(1, 1, False).extrude(H)
    
    
    if (pintype == CASE_SMD_TYPE):
        mvX = 0 - (L / 2.0)
        mvY = 0 - (W / 2.0)
        case=cq.Workplane("XY").workplane(offset=A1).moveTo(mvX, mvY).rect(L, W, False).extrude(H)
    elif (pintype == CASE_THT_TYPE) or (pintype == CASE_THT_N_TYPE):
        p = pin[0]
        mvX = p[0] + pin1corner[0]
        mvY = p[1] - pin1corner[1]
        case=cq.Workplane("XY").workplane(offset=A1).moveTo(mvX, mvY).rect(L, -W, False).extrude(H)
    
    if rim != None:
        if len(rim) == 3:
            rdx = rim[0]
            rdy = rim[1]
            rdh = rim[2]
            FreeCAD.Console.PrintMessage('\r\n')
            FreeCAD.Console.PrintMessage("rdx " + str(rdx) + '\r\n')
            FreeCAD.Console.PrintMessage("rdy " + str(rdy) + '\r\n')
            FreeCAD.Console.PrintMessage("rdh " + str(rdh) + '\r\n')
            FreeCAD.Console.PrintMessage('\r\n')
            case1 = cq.Workplane("XY").workplane(offset=A1).moveTo(mvX + rdx, mvY).rect(L - (2.0 * rdx), 0 - (W + 1.0), False).extrude(rdh)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=A1).moveTo(mvX, mvY - rdy).rect(L + 1.0, 0 - (W - (2.0 * rdy)), False).extrude(rdh)
            case = case.cut(case1)

    case = case.faces("<X").edges("<Y").fillet(ff)
    case = case.faces("<X").edges(">Y").fillet(ff)
    case = case.faces(">X").edges("<Y").fillet(ff)
    case = case.faces(">X").edges(">Y").fillet(ff)
    case = case.faces(">Y").edges(">Z").fillet(ff)

    if roundbelly == 1 and rim == None:
        # Belly is rounded
        case = case.faces(">Y").edges("<Z").fillet(ff / 2.0)

    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)

    return (case)


def make_case_top(params):

    L = params.L                    # package length
    W = params.W                    # package width
    H = params.H                    # package height
    A1 = params.A1                    # Body seperation height
    rotation = params.rotation        # rotation if required
    pin1corner = params.pin1corner     # Left upp corner relationsship to pin 1
    pin = params.pin                # pin/pad cordinates
    show_top = params.show_top        # If top should be visible or not
    pintype = params.pintype        # pin type , like SMD or THT

    FreeCAD.Console.PrintMessage('make_case_top\r\n')

    mvX = 0
    mvY = 0
    # Dummy
    casetop=cq.Workplane("XY").workplane(offset=A1 + H).moveTo(0, 0).rect(1, 1, False).extrude(0.8)
    

    ff = W / 20.0;
    if ff > 1.0:
        ff = 1.0
    
    Ldt = ff
    Wdt = ff
    
    L1 = L - (2.0 * Ldt)
    W1 = W - (2.0 * Wdt)
    
    if show_top == 1:
        tty = A1 + H - 0.1

        if (pintype == CASE_SMD_TYPE):
            mvX = (0 - (L1 / 2.0)) + ((L - L1) / 2.0)
            mvY = (0 - (W1 / 2.0)) - ((W - W1) / 2.0)
            casetop=cq.Workplane("XY").workplane(offset=tty).moveTo(mvX, mvY).rect(L1, W1, False).extrude(0.2)
        elif (pintype == CASE_THT_TYPE):
            p = pin[0]
            mvX = (p[0] + pin1corner[0]) + ((L - L1) / 2.0)
            mvY = (p[1] - pin1corner[1]) - ((W - W1) / 2.0)
            casetop=cq.Workplane("XY").workplane(offset=tty).moveTo(mvX, mvY).rect(L1, -W1, False).extrude(0.2)

        casetop = casetop.faces("<X").edges("<Y").fillet(ff)
        casetop = casetop.faces("<X").edges(">Y").fillet(ff)
        casetop = casetop.faces(">X").edges("<Y").fillet(ff)
        casetop = casetop.faces(">X").edges(">Y").fillet(ff)
    else:
        # If it is not used, just hide it inside the body
        if (pintype == CASE_SMD_TYPE):
            mvX = 0
            mvY = 0
            casetop=cq.Workplane("XY").workplane(offset=A1 + (H / 4.0)).moveTo(mvX, mvY).rect(0.1, 0.1, False).extrude(0.1)
        else:
            p = pin[0]
            mvX = (p[0] + pin1corner[0]) + (L / 2.0)
            mvY = (p[1] - pin1corner[1]) - (W / 2.0)
            casetop=cq.Workplane("XY").workplane(offset=A1 + (H / 4.0)).moveTo(mvX, mvY).rect(0.1, 0.1, False).extrude(0.1)
            

    if (rotation != 0):
        casetop = casetop.rotate((0,0,0), (0,0,1), rotation)

    return (casetop)


def make_pins_tht(params):

    L = params.L                    # package length
    W = params.W                    # package width
    H = params.H                    # package height
    A1 = params.A1                    # Body seperation height
    rim = params.rim                # Rim underneth
    pinpadsize = params.pinpadsize    # pin diameter or pad size
    pinpadh = params.pinpadh        # pin length, pad height
    pintype = params.pintype        # Casing type
    rotation = params.rotation        # rotation if required
    pin = params.pin                # pin/pad cordinates

    pinss = 0.1
    if rim != None:
        if len(rim) == 3:
            rdx = rim[0]
            rdy = rim[1]
            rdh = rim[2]
            pinss = rdh + 0.1

    p = pin[0]
    pins=cq.Workplane("XY").workplane(offset=A1 + pinss).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + pinss))
    pins = pins.faces("<Z").fillet(pinpadsize / 5.0)

    for i in range(1, len(pin)):
        p = pin[i]
        pint=cq.Workplane("XY").workplane(offset=A1 + pinss).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + pinss))
        pint = pint.faces("<Z").fillet(pinpadsize / 5.0)
        pins = pins.union(pint)
 

    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)

    return (pins)


def make_pins_tht_n(params):

    L = params.L                    # package length
    W = params.W                    # package width
    H = params.H                    # package height
    A1 = params.A1                    # Body seperation height
    pinpadsize = params.pinpadsize    # pin diameter or pad size
    pinpadh = params.pinpadh        # pin length, pad height
    pintype = params.pintype        # Casing type
    rotation = params.rotation        # rotation if required
    pin = params.pin                # pin/pad cordinates

    FreeCAD.Console.PrintMessage('make_pins_tht_n\r\n')

    p = pin[0]
    pins=cq.Workplane("XY").workplane(offset=A1 + 2.0).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + 2.0))
    pins = pins.faces("<Z").fillet(pinpadsize / 5.0)

    pint=cq.Workplane("XZ").workplane(offset= 0 -p[1]).moveTo(p[0], 2.0).circle(pinpadsize / 2.0, False).extrude( 0 - (W / 2.0))
    pins = pins.union(pint)

    for i in range(1, len(pin)):
        p = pin[i]
        pint=cq.Workplane("XY").workplane(offset=A1 + 2.0).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + 2.0))
        pint = pint.faces("<Z").fillet(pinpadsize / 5.0)
        pins = pins.union(pint)
        pint=cq.Workplane("XZ").workplane(offset= 0 -p[1]).moveTo(p[0], 2.0).circle(pinpadsize / 2.0, False).extrude( 0 - (W / 2.0))
        pins = pins.union(pint)
 

    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)

    return (pins)


def make_pins_smd(params):

    L = params.L                    # package length
    W = params.W                    # package width
    H = params.H                    # package height
    A1 = params.A1                    # Body seperation height
    pinpadsize = params.pinpadsize    # pin diameter or pad size
    pinpadh = params.pinpadh        # pin length, pad height
    pintype = params.pintype        # Casing type
    rotation = params.rotation        # rotation if required
    pin = params.pin                # pin/pad cordinates

    FreeCAD.Console.PrintMessage('make_pins_smd\r\n')

    #
    # Dummy
    #
    pins=cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).rect(0.1, 0.1).extrude(0.1)
    #

    for i in range(0, len(pin)):
        p = pin[i]
        myX1 = p[0] - pinpadsize
        myY1 = -p[1]
        xD = myX1
        yD = pinpadsize
        if p[0] < 0 and (p[1] > (0 - (W / 2.0)) and p[1] < ((W / 2.0))):
            # Left side
            if p[0] < (0 - (L / 2.0)):
                # Normal pad
                myX1 = p[0] / 2.0
                myY1 = -p[1]
                xD = p[0]
                yD = pinpadsize
                pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
            else:
                # pad cordinate is inside the body
                myZ1 = pinpadsize / 2.0
                myY1 = -p[1]
                xD = pinpadsize
                yD = pinpadsize
                pint=cq.Workplane("ZY").workplane(offset=(L / 2.0) - (pinpadh / 2.0)).moveTo(myZ1, myY1).rect(xD, yD).extrude(pinpadh)
            
        #
        elif p[0] >= 0 and (p[1] > (0 - (W / 2.0)) and p[1] < ((W / 2.0))):
            # Right side
            if p[0] > (L / 2.0):
                # Normal pad
                myX1 = p[0] / 2.0
                xD = -p[0]
                yD = pinpadsize
                pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
            else:
                # pad cordinate is inside the body
                myZ1 = pinpadsize / 2.0
                myY1 = -p[1]
                xD = pinpadsize
                yD = pinpadsize
                pint=cq.Workplane("ZY").workplane(offset=0 - ((L / 2.0) + (pinpadh / 2.0))).moveTo(myZ1, myY1).rect(xD, yD).extrude(pinpadh)
        elif p[1] < 0:
            # top pad
            if p[1] < (W / 2.0):
                myX1 = p[0] - (pinpadsize / 2.0)
                myY1 = 0 - (p[1] / 2.0)
                yD = 0 - p[1]
                xD = pinpadsize
                pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
            else:
                # pad cordinate is inside the body
                myZ1 = pinpadsize / 2.0
                yD = pinpadsize
                xD = pinpadsize
                myX1 = p[0] - (pinpadsize / 2.0)
                pint=cq.Workplane("ZX").workplane(offset=((W / 2.0) - (pinpadh / 2.0))).moveTo(myZ1, myX1).rect(xD, yD).extrude(pinpadh)
        else:
            # bottom pad
            if p[1] > (W / 2.0):
                myX1 = p[0] - (pinpadsize / 2.0)
                myY1 = 0 - (p[1] / 2.0)
                yD = 0 - p[1]
                xD = pinpadsize
                pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
            else:
                # pad cordinate is inside the body
                myX1 =  p[0] - (pinpadsize / 2.0)
                myZ1 = pinpadsize / 2.0
                yD = pinpadsize
                xD = pinpadsize
                pint=cq.Workplane("ZX").workplane(offset=0 -((W / 2.0) + (pinpadh / 2.0))).moveTo(myZ1, myX1).rect(xD, yD).extrude(pinpadh)

        if i == 0:
            pins = pint
        else:
            pins = pins.union(pint)

    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)

    return (pins)


def make_3D_model(models_dir, variant):
                
    LIST_license = ["",]
    modelName = all_params[variant].modelName
        
    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)

    case = make_case(all_params[variant])
    casetop = make_case_top(all_params[variant])
    
    if (all_params[variant].pintype == CASE_THT_TYPE):
        pins = make_pins_tht(all_params[variant])
    
    if (all_params[variant].pintype == CASE_THT_N_TYPE):
        pins = make_pins_tht_n(all_params[variant])

    if (all_params[variant].pintype == CASE_SMD_TYPE):
        pins = make_pins_smd(all_params[variant])

    show(case)
    show(casetop)
    show(pins)
    #show(pinmark)
    #stop
    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)

    body_color_key = all_params[variant].body_color_key
    body_top_color_key = all_params[variant].body_top_color_key
    pin_color_key = all_params[variant].pin_color_key
    
    
    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
    pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],body_top_color)
    Color_Objects(Gui,objs[2],pin_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_body_top=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]

    material_substitutions={
        col_body[:-1]:body_color_key,
        col_body_top[:-1]:body_top_color_key,
        col_pin[:-1]:pin_color_key
    }

    expVRML.say(material_substitutions)
    while len(objs) > 1:
            FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
            del objs
            objs = GetListOfObjects(FreeCAD, doc)
        
    doc.Label = CheckedmodelName

    del objs
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = CheckedmodelName
    restore_Main_Tools()

    script_dir=os.path.dirname(os.path.realpath(__file__))
    expVRML.say(models_dir)
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    exportSTEP(doc, modelName, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', modelName+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,modelName,scale,out_dir)
    del objs
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

#import step_license as L
import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator_Converter_ACDC":

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

    
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building ACDC-Converter_Hahn-HS-400XX\r\n')
        model_to_build='ACDC-Converter_Hahn-HS-400XX'
    else:
        model_to_build=sys.argv[2]
    
    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n' + variant + '\r\n\r\n')
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping. " % variant)
            continue

        make_3D_model(models_dir, variant)

#!/usr/bin/python
# -*- coding: utf-8 -*-
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

__title__ = "make AC to DC  & DC to DC converter 3D models"
__author__ = "Stefan, based on DIP script"
__Comment__ = 'make AC to DC  & DC to DC converter 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.4.0/09/2020"

save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'
global_3dpath = '../_3Dmodels/'

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


if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui


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
 CutObjs_wColors, checkRequirements,  runGeometryCheck

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
    msg = "missing CadQuery 0.5.2 or later Module!\r\n\r\n"
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
    FreeCAD.Console.PrintMessage("CQ 030 doesn't open example file")


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
    A1 = params.A1                  # Body separation height
    rim = params.rim                # Rim underneath
    rotation = params.rotation      # rotation if required
    pin1corner = params.pin1corner  # Left upp corner relationsship to pin 1
    pin = params.pin                # pin/pad cordinates
    roundbelly = params.roundbelly  # If belly of caseing should be round (or flat)
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
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(mvX, mvY).rect(L, W, False).extrude(H)
    elif (pintype == CASE_THT_TYPE or pintype == CASE_THT_N_TYPE ):
        p = pin[0]
        mvX = p[1] + pin1corner[0]
        mvY = p[2] - pin1corner[1]
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(mvX, mvY).rect(L, -W, False).extrude(H)

    if rim != None:
        if len(rim) == 3:
            rdx = rim[0]
            rdy = rim[1]
            rdh = rim[2]
            if rdx != 0:
                case1 = cq.Workplane("XY").workplane(offset=A1).moveTo(mvX + rdx, mvY).rect(L - (2.0 * rdx), 0 - (W + 1.0), False).extrude(rdh)
                case = case.cut(case1)
            if rdy != 0:
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
    A1 = params.A1                  # Body separation height
    rotation = params.rotation      # rotation if required
    pin1corner = params.pin1corner  # Left upp corner relationsship to pin 1
    pin = params.pin                # pin/pad cordinates
    show_top = params.show_top      # If top should be visible or not
    pintype = params.pintype        # pin type , like SMD or THT

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
        elif (pintype == CASE_THT_TYPE or pintype == CASE_THT_N_TYPE ):
            p = pin[0]
            mvX = (p[1] + pin1corner[0]) + ((L - L1) / 2.0)
            mvY = (p[2] - pin1corner[1]) - ((W - W1) / 2.0)
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
            mvX = (p[1] + pin1corner[0]) + (L / 2.0)
            mvY = (p[2] - pin1corner[1]) - (W / 2.0)
            casetop=cq.Workplane("XY").workplane(offset=A1 + (H / 4.0)).moveTo(mvX, mvY).rect(0.1, 0.1, False).extrude(0.1)


    if (rotation != 0):
        casetop = casetop.rotate((0,0,0), (0,0,1), rotation)

    return (casetop)


def make_pins(params):

    L = params.L                    # package length
    W = params.W                    # package width
    H = params.H                    # package height
    A1 = params.A1                  # Body separation height
    rotation = params.rotation      # rotation if required
    pin = params.pin                # pin/pad cordinates
    rim = params.rim                # Rim underneath

    pins = None

    pinss = 0.1
    if rim != None:
        if len(rim) == 3:
            rdx = rim[0]
            rdy = rim[1]
            rdh = rim[2]
            pinss = rdh + 0.1
    #
    # Dummy
    #
    pins=cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).rect(0.1, 0.1).extrude(0.1)
    pint=cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).rect(0.1, 0.1).extrude(0.1)
    #

    for i in range(0, len(pin)):
        p = pin[i]

        pt = str(p[0])
        px = float(p[1])
        py = float(p[2])

        if pt == 'rect':
            pl = float(p[3])
            pw = float(p[4])
            ph = float(p[5])
            FreeCAD.Console.PrintMessage('make_pins 1.1\r\n')

            pint=cq.Workplane("XY").workplane(offset=A1 + pinss).moveTo(px, -py).rect(pl, pw).extrude(0 - (ph + pinss))

        elif pt == 'round':
            # FreeCAD.Console.PrintMessage('make_pins 1.2 i ' + str(i) + '\r\n')
            # FreeCAD.Console.PrintMessage('make_pins 1.2 pt ' + str(pt) + '\r\n')
            # FreeCAD.Console.PrintMessage('make_pins 1.2 px ' + str(px) + '\r\n')
            # FreeCAD.Console.PrintMessage('make_pins 1.2 py ' + str(py) + '\r\n')
            pd = p[3]
            ph = p[4]
            # FreeCAD.Console.PrintMessage('make_pins 1.2 pd ' + str(pd) + '\r\n')
            # FreeCAD.Console.PrintMessage('make_pins 1.2 ph ' + str(ph) + '\r\n')

            pint=cq.Workplane("XY").workplane(offset=A1 + pinss).moveTo(px, -py).circle(pd / 2.0, False).extrude(0 - (ph + pinss))
            pint = pint.faces("<Z").fillet(pd / 5.0)

        elif pt == 'smd':
            pd = p[3]
            ph = p[4]
            myX1 = px - pd
            myY1 = -py
            xD = myX1
            yD = pd
            if px < 0 and (py > (0 - (W / 2.0)) and py < ((W / 2.0))):
                # Left side
                if px < (0 - (L / 2.0)):
                    FreeCAD.Console.PrintMessage('make_pins smd 1\r\n')
                    # Normal pad
                    myX1 = px / 2.0
                    myY1 = -py
                    xD = px
                    yD = pd
                    pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(ph)
                else:
                    # pad cordinate is inside the body
                    FreeCAD.Console.PrintMessage('make_pins smd 2\r\n')
                    myZ1 = pd / 2.0
                    myY1 = -py
                    xD = pd
                    yD = pd
                    pint=cq.Workplane("ZY").workplane(offset=(L / 2.0) - (ph / 2.0)).moveTo(myZ1, myY1).rect(xD, yD).extrude(ph)

            elif px >= 0 and (py > (0 - (W / 2.0)) and py < ((W / 2.0))):
                # Right side
                if px > (L / 2.0):
                    FreeCAD.Console.PrintMessage('make_pins smd 3\r\n')
                    # Normal pad
                    myX1 = px / 2.0
                    xD = -px
                    yD = pd
                    pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(ph)
                else:
                    FreeCAD.Console.PrintMessage('make_pins smd 4\r\n')
                    # pad cordinate is inside the body
                    myZ1 = pd / 2.0
                    myY1 = -py
                    xD = pd
                    yD = pd
                    pint=cq.Workplane("ZY").workplane(offset=0 - ((L / 2.0) + (ph / 2.0))).moveTo(myZ1, myY1).rect(xD, yD).extrude(ph)
            elif py < 0:
                # top pad
                if p[1] < (W / 2.0):
                    FreeCAD.Console.PrintMessage('make_pins smd 5\r\n')
                    myX1 = px - (pd / 2.0)
                    myY1 = 0 - (py / 2.0)
                    yD = 0 - py
                    xD = pd
                    pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(ph)
                else:
                    FreeCAD.Console.PrintMessage('make_pins smd 6\r\n')
                    # pad cordinate is inside the body
                    myZ1 = pd / 2.0
                    yD = pd
                    xD = pd
                    myX1 = px - (pd / 2.0)
                    pint=cq.Workplane("ZX").workplane(offset=((W / 2.0) - (ph / 2.0))).moveTo(myZ1, myX1).rect(xD, yD).extrude(ph)
            else:
                # bottom pad
                if py > (W / 2.0):
                    FreeCAD.Console.PrintMessage('make_pins smd 7\r\n')
                    myX1 = px - (pd / 2.0)
                    myY1 = 0 - (py / 2.0)
                    yD = 0 - py
                    xD = pd
                    pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(ph)
                else:
                    FreeCAD.Console.PrintMessage('make_pins smd 8\r\n')
                    # pad cordinate is inside the body
                    myX1 =  px - (pd / 2.0)
                    myZ1 = pd / 2.0
                    yD = pd
                    xD = pd
                    pint=cq.Workplane("ZX").workplane(offset=0 -((W / 2.0) + (ph / 2.0))).moveTo(myZ1, myX1).rect(xD, yD).extrude(ph)

        elif pt == 'tht_n':
            pd = p[3]
            pl = p[4]

            pint= cq.Workplane("XY").workplane(offset=A1 + 2.0).moveTo(px, -py).circle(pd / 2.0, False).extrude(0 - (pl + 2.0))
            pint = pint.faces("<Z").fillet(pd / 5.0)
            pind= cq.Workplane("XZ").workplane(offset= 0 -py + (pd / 2.0)).moveTo(px, A1 + 2.0).circle(pd / 2.0, False).extrude( 0 - (W / 2.0))
            pind = pind.faces("<Y").fillet(pd / 2.0)
            pint = pint.union(pind)

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
    pins = make_pins(all_params[variant])

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
    out_dir=models_dir+os.sep+all_params[variant].dest_dir_prefix

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    step_path = '{dir:s}/{name:s}.step'.format(dir=out_dir, name=modelName)
    exportSTEP(doc, modelName, out_dir)


    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")

    Lic.addLicenseToStep(out_dir, '{:s}.step'.format(modelName),
            LIST_license,
            cq_parameters.LICENCE_Info.STR_licAuthor,
            cq_parameters.LICENCE_Info.STR_licEmail,
            cq_parameters.LICENCE_Info.STR_licOrgSys,
            cq_parameters.LICENCE_Info.STR_licPreProc)

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
    # expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    # Save the doc in Native FC format
    doc.recompute()
    saveFCdoc(App, Gui, doc, modelName, out_dir)


    #FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.activeDocument().activeView().viewAxometric()

    if save_memory == True or check_Model==True:
        FreeCAD.closeDocument(doc.Name)
        os.remove (out_dir+os.sep+modelName+'.FCStd')

    if check_Model==True:
        with open(out_dir+os.sep+check_log_file, 'a+') as log:
            log.write('# Check report for Molex 3d model genration\n')
            runGeometryCheck(App, Gui, step_path, log, modelName, save_memory=save_memory)
            log.close()


def run():
    ## # get variant names from command line

    return

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

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building Converter_ACDC_Hahn-HS-400xx\r\n')
        model_to_build='Converter_ACDC_Hahn_HS-400xx_THT'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n' + variant + '\r\n\r\n')
        if not variant in all_params:
            FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'all_params', skipping. " % variant)
            continue

        make_3D_model(models_dir, variant)

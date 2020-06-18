#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is derived from a cadquery script for generating Converter_DCDC 3D format
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

__title__ = "make Altech connector 3D models"
__author__ = "Stefan, based on Converter_DCDC script"
__Comment__ = 'make Altech connectors 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.4 18/06/2020"

# maui import cadquery as cq
# maui from Helpers import show
from collections import namedtuple

import math

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

# Sphinx workaround #2
try:
    cq
    checkRequirements(cq)
except NameError:
    cq = None
#


import cq_parameters  # modules parameters
from cq_parameters import *


import battery_common
from battery_common import *

import battery_pins
from battery_pins import *

import battery_contact
from battery_contact import *

import battery_caseBX0036
from battery_caseBX0036 import *

import battery_casebutton
from battery_casebutton import *

import battery_casecylinder
from battery_casecylinder import *

import cq_Seiko_MSXXXX
from cq_Seiko_MSXXXX import *

import cq_Keystone_2993
from cq_Keystone_2993 import *


    
def make_npthpins_S2(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize    # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    FreeCAD.Console.PrintMessage('make_npthpins_S2\r\n')
    
    x1 = npthpins[1]
    y1 = npthpins[2]
    dh = npthpins[3]
    pd = npthpins[4]
    ph = npthpins[5]
    #
    dx = (dh / 2.0) * math.sin(math.radians(0.0))
    dy = (dh / 2.0) * math.cos(math.radians(0.0))
    case = cq.Workplane("XY").workplane(offset=A1).moveTo(x1 + dx, 0.0 - (y1 + dy)).circle(pd / 2.0, False).extrude(0.0 - ph)
    case = case.faces("<Z").fillet(pd / 3.0)
    
    dx = (dh / 2.0) * math.sin(math.radians(120.0))
    dy = (dh / 2.0) * math.cos(math.radians(120.0))
    case1 = cq.Workplane("XY").workplane(offset=A1).moveTo(x1 + dx, 0.0 - (y1 + dy)).circle(pd / 2.0, False).extrude(0.0 - ph)
    case1 = case1.faces("<Z").fillet(pd / 3.0)
    case = case.union(case1)
    
    case1 = cq.Workplane("XY").workplane(offset=A1).moveTo(x1 - dx, 0.0 - (y1 + dy)).circle(pd / 2.0, False).extrude(0.0 - ph)
    case1 = case1.faces("<Z").fillet(pd / 3.0)
    case = case.union(case1)
    #
    #
    
    return case


def make_3D_model(models_dir, variant):

    LIST_license = ["",]

    FreeCAD.Console.PrintMessage("\r\nMaking %s\r\n" % variant)
    modelName = variant
    modelfileName = ''
    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)

    case = None
    pins = None

    if all_params[variant].modeltype == 'BX0036':
        case = make_case_BX0036(all_params[variant])
        pins = make_pins(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    elif all_params[variant].modeltype == 'Button1':
        case = make_case_Button1(all_params[variant])
        pins = make_pins(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    elif all_params[variant].modeltype == 'Button2':
        case = make_case_Button2(all_params[variant])
        pins = make_pins(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    elif all_params[variant].modeltype == 'Button3':
        case = make_case_Button3(all_params[variant])
        pins = make_pins(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    elif all_params[variant].modeltype == 'Button4':
        case = make_case_Button4(all_params[variant])
        pins = make_pins(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    elif all_params[variant].modeltype == 'Cylinder1':
        case = make_case_Cylinder1(all_params[variant])
        pins = make_pins(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    elif variant == 'Seiko_MS621F':
        case = make_case_Seiko_MS621F(all_params[variant])
        pins = make_pins_Seiko_MS621F(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    elif variant == 'Keystone_2993':
        case = make_case_Keystone_2993(all_params[variant])
        pins = make_pins_Keystone_2993(all_params[variant])
        show(case)
        show(pins)
        modelfileName = make_modelfileName_Common(all_params[variant])
        #
        #
    else:
        FreeCAD.Console.PrintMessage("\r\nSerie %s does not exist, skipping'\r\n" % all_params[variant].serie)
        return

    #show(pinmark)
    #stop
    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)

    body_color_key = all_params[variant].body_color_key
    pin_color_key = all_params[variant].pin_color_key

    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],pin_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]

    material_substitutions={
        col_body[:-1]:body_color_key,
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
    out_dir=models_dir + os.sep +  all_params[variant].dest_dir_prefix
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    exportSTEP(doc, modelfileName, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir + os.sep, modelfileName + ".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc, modelfileName,scale,out_dir)
    del objs
    objs=GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir + os.sep + modelfileName + '.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    #expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
    #scale=0.3937001
    #exportVRML(doc, modelfileName,scale,out_dir)
    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, modelfileName, out_dir)
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
    models_dir=sub_path + "_3Dmodels"
    
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building serie BX0036\r\n')
        model_to_build='BX0036'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = list(all_params.keys())
    else:
        variants = [model_to_build]


    for variant in variants:
        if variant in all_params:
            make_3D_model(models_dir, variant)
        else:
            FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'all_params', skipping. " % variant)

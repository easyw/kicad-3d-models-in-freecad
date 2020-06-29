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

#checking requirements

import cq_parameters  # modules parameters
from cq_parameters import *



PIN_THT_TYPE = 'tht'
PIN_SMD_TYPE = 'smd'
_TYPES = [PIN_THT_TYPE, PIN_SMD_TYPE ]

    
def make_case_AK300(params, pinnumber):

    W = params.W                    # package width
    H = params.H                    # package height
    WD = params.WD                  # > Y distance form pin center to package edge
    A1 = params.A1                  # Body seperation height
    PE = params.PE                  # Distance from edge to pin
    PS = params.PS                  # Pin distance
    PD = params.PD                  # Pin diameter
    PL = params.PL                  # Pin diameter
    PF = params.PF                  # Pin form
    SW = params.SW                  # Blender width
    rotation = params.rotation      # rotation if required

    lw = ((2.0 * PE) + ((pinnumber - 1) * PS))

    #
    # Create a plygon of the shape and extrude it along the Y axis
    # 
    pts = []
    pts.append((0.0, A1))
    #
    pts.append((0.0 - WD, A1))
    #
    pts.append((0.0 - WD, (A1 + H) - WD))
    #
    pts.append((0.0, A1 + H))
    #
    pts.append(((W - WD) - 0.5, A1 + H))
    #
    pts.append((W - WD, A1 + (H - 0.5)))
    #
    pts.append((W - WD, A1))
    #
    case = cq.Workplane("YZ").workplane(offset=0 - PE).polyline(pts).close().extrude(lw)
    #
    #
    A1A = A1 + 0.2
    bb = WD - 0.4
    SL = SW / 1.1       # Screw diameter
    
    px = 0.0
    pins = None
    
    for i in range(0, pinnumber):
        pp = cq.Workplane("XY").workplane(offset=A1A).moveTo(px, 0.0 - (WD / 2.0)).rect(SW + 0.4, bb).extrude(1.1 * H)
        case = case.cut(pp)
        # Cut out screw header
        po = cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0).circle(SL / 2.0, False).extrude(W)
        po = po.rotate((0,0,0), (1,0,0), 0 - 45.0)
        po = po.translate((px, 0.0, H / 2.0))
        case = case.cut(po)

        px = px + PS

#    case = case.faces("<Y").edges(">X").fillet(0.1)
    case = case.faces("<X").fillet(0.2)
    case = case.faces(">X").fillet(0.2)
    case = case.faces(">Z").fillet(0.2)
    case = case.faces("<Y").edges(">Z").fillet(0.2)

    if (rotation >  0.01):
        case = case.rotate((0,0,0), (0,0,1), rotation)
        
    return (case)


def make_pins_AK300(params, pinnumber):

    W = params.W                    # package width
    H = params.H                    # package height
    WD = params.WD                  # > Y distance form pin center to package edge
    A1 = params.A1                  # Body seperation height
    PE = params.PE                  # Distance from edge to pin
    PS = params.PS                  # Pin distance
    PD = params.PD                  # Pin diameter
    PL = params.PL                  # Pin diameter
    PF = params.PF                  # Pin form
    SW = params.SW                  # Blender width
    rotation = params.rotation      # rotation if required

    px = 0.0
    pins = None
    
    for i in range(0, pinnumber):
        if PF == 'round':
            pint = cq.Workplane("XY").workplane(offset=A1).moveTo(px, 0.0).circle(PD[0] / 2.0, False).extrude(0 - (A1 + PL))
            pint = pins.faces("<Z").fillet(PD[0] / 2.2)
        else:
            pint = cq.Workplane("XY").workplane(offset=A1).moveTo(px, 0.0).rect(PD[0], PD[1]).extrude(0 - (A1 + PL))
            if PD[0] < PD[1]:
                pint = pint.faces("<Z").fillet(PD[0] / 2.2)
            else:
                pint = pint.faces("<Z").fillet(PD[1] / 2.2)
                
        if i == 0:
            pins = pint
        else:
            pins = pins.union(pint)
    
        A1A = A1 + 0.2
        bb0 = WD - 0.5
        bb0 = bb0 / math.cos(math.radians(45.0))
        SL = SW / 1.1       # Screw diameter
        
        bb = bb0
        pl = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(SW, bb).extrude(0.0 - (WD))
        # Make hole
        bb1 = SW - (SW * 0.2)
        #
        plu = cq.Workplane("XY").workplane(offset=0.0 + 0.1).moveTo(0.0, 0.0 - ((bb / 2.0) - (bb1 / 2) - (SW * 0.2))).rect(bb1, bb1).extrude(0.0 - (1.1 * H + 0.2))
        pl = pl.cut(plu)
        
        plu = cq.Workplane("ZX").workplane(offset=0.0 - (WD - SL)).moveTo(0.0 - (bb / 2.0), 0.0).circle(SW / 2.5, False).extrude(SL)
        pl = pl.union(plu)
        pl = pl.rotate((0,0,0), (1,0,0), 45.0)
        pl = pl.translate((px, 0.0 - (WD / 2.0) + 0.1, A1 + ((H - WD) / 2.0) + WD - 0.3))
        #
        pins = pins.union(pl)
        #
        # Add Screw head
        bba = (W - WD) / math.cos(math.radians(45.0)) 
        bba = bba * 0.85
        po = cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0).circle(SL / 2.0, False).extrude(bba)
        po = po.faces(">Z").fillet(SL / 8.0)
        pr = cq.Workplane("XY").workplane(offset=A1 + bba - (SL / 8.0)).moveTo(0.0, 0.0).rect(SL / 4.0, 10.0).extrude(SL / 4.0)
        po = po.cut(pr)
        po = po.rotate((0,0,0), (1,0,0), 0 - 45.0)
        po = po.translate((px, 0.0, H / 2.0))
        pins = pins.union(po)
        
        px = px + PS
        
    
    if (rotation > 0.01):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)

    return (pins)


def make_3D_model(models_dir, variant, pinnumber):

    LIST_license = ["",]
    modelName = all_params[variant].serie + '_' + str(pinnumber)

    modelfileName = ''
    
    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)

    case = None
    pins = None
    if all_params[variant].serie == 'AK300':
        case = make_case_AK300(all_params[variant], pinnumber)
        pins = make_pins_AK300(all_params[variant], pinnumber)
        show(case)
        show(pins)
        #
        #
        modelfileName = modelfileName + all_params[variant].manufacture + '_' + all_params[variant].serie
        modelfileName = modelfileName + '_1x' + '{:02d}'.format(pinnumber)
        modelfileName = modelfileName + '_P' + '{:.2f}'.format(all_params[variant].PS) + "mm"
        modelfileName = modelfileName + '_45-Degree'
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
    out_dir=models_dir+ os.sep +  all_params[variant].dest_dir_prefix
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    exportSTEP(doc, modelfileName, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', modelfileName + ".step", LIST_license,\
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
        FreeCAD.Console.PrintMessage('No variant name is given! building serie AK300\r\n')
        model_to_build='AK300'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n' + variant + '\r\n\r\n')
        if variant in all_params:
            for p in all_params[variant].pin_number:
                make_3D_model(models_dir, variant, p)
        else:
            FreeCAD.Console.PrintMessage("\tParameters for %s doesn't exist in 'all_params', skipping. " % variant)
            continue

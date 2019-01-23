# -*- coding: utf-8 -*-
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

__title__ = "make DC to DC converter 3D models"
__author__ = "Stefan, based on DIP script"
__Comment__ = 'make varistor 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.3 14/08/2015"

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
import importlib
importlib.reload(cq_cad_tools)
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

destination_dir="/Varistor"
# rotation = 0

import cq_parameters  # modules parameters
from cq_parameters import *


CASE_THT_TYPE = 'tht'
CASE_SMD_TYPE = 'smd'
_TYPES = [CASE_THT_TYPE, CASE_SMD_TYPE ]



def make_case_RV_Disc(params):


    D = params.D                # package length
    E = params.E                # body overall width
    A1 = params.A1              # package height
    pin = params.pin            # Pins
    rotation = params.rotation  # Rotation if required
    pintype = params.pintype    # pin type , like SMD or THT

    FreeCAD.Console.PrintMessage('make_case_RV_Disc\r\n')
    #
    #
    #
    p0 = pin[0]
    p1 = pin[1]
    x0 = p0[0]
    y0 = p0[1]
    dx = math.fabs((p0[0] - p1[0]) / 2.0)
    dy = math.fabs((p0[1] - p1[1]) / 2.0)
    cx = x0 + dx
    cy = y0 + dy

    ff = E / 2.05
    
    case=cq.Workplane("XZ").workplane(offset=cy - (E / 2.0)).moveTo(cx, A1 + (D / 2.0)).circle(D / 2.0, False).extrude(E)

    case = case.faces("<X").edges("<Y").fillet(ff)
    case = case.faces(">X").edges(">Y").fillet(ff)

    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)

    return (case)



def make_pins_RV_Disc(params):

    A1 = params.A1                    # Body seperation height
    b = params.b            # pin diameter or pad size
    ph = params.ph                  # pin length
    rotation = params.rotation        # rotation if required
    pin = params.pin                # pin/pad cordinates
    D = params.D                # package length

    FreeCAD.Console.PrintMessage('make_pins_RV_Disc \r\n')

    p = pin[0]
    pins = cq.Workplane("XY").workplane(offset=A1 + (D / 2.0)).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + (D / 2.0)))
    pins = pins.faces("<Z").fillet(b / 5.0)

    for i in range(1, len(pin)):
        p = pin[i]
        pint = cq.Workplane("XY").workplane(offset=A1 + (D / 2.0)).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + (D / 2.0)))
        pint = pint.faces("<Z").fillet(b / 5.0)
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

    if (all_params[variant].serie == 'RV_Disc'):
        case = make_case_RV_Disc(all_params[variant])
        pins = make_pins_RV_Disc(all_params[variant])
        show(case)
        show(pins)
    else:
        print("Serie " + all_params[variant].serie + " is not supported")
        FreeCAD.Console.PrintMessage('\r\nSerie ' + all_params[variant].serie + ' is not supported\r\n')
        sys.exit()


    #show(pinmark)
    #stop
    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)
    
    FreeCAD.Console.PrintMessage('#1\r\n')

    body_color_key = all_params[variant].body_color_key
    pin_color_key = all_params[variant].pin_color_key

    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

    FreeCAD.Console.PrintMessage('#2\r\n')

    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],pin_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]

    FreeCAD.Console.PrintMessage('#3\r\n')
    
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
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    exportSTEP(doc, modelName, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', modelName+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    FreeCAD.Console.PrintMessage('#4\r\n')

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
if __name__ == "__main__" or __name__ == "main_generator_Converter_DCDC":

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
        FreeCAD.Console.PrintMessage('No variant name is given! building RV_Disc_D12mm_W3.9mm_P7.5mm\r\n')
        model_to_build='RV_Disc_D12mm_W3.9mm_P7.5mm'
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

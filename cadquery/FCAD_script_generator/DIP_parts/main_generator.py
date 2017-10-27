# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
    
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
#* cadquery script for generating DIP socket models in STEP AP214           *
#*   Copyright (c) 2017                                                     *
#* Maurice https://launchpad.net/~easyw                                     *                                *
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

__title__ = "make assorted DIP part 3D models"
__author__ = "maurice, hyOzd, Stefan, Terje"
__Comment__ = 'make make assorted DIP part 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.0 27/10/2017"

#
# mods by Terje: made generic in order to support class based model scripts
# TODO: improve part filtering, also to include family names?
#

from collections import namedtuple

import sys, os
import datetime
from datetime import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\..\_tools")
import exportPartToVRML as expVRML
import shaderColors

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
#from Gui.Command import *

outdir = os.path.dirname(os.path.realpath(__file__) + "/../_3Dmodels")
scriptdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)
sys.path.append(scriptdir)
if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

try:
    # Gui.SendMsgToActiveView("Run")
    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"

footprints_dir = os.environ['KISYSMOD']

from cq_base_model import part
from cq_parameters import * # Generic DIP parameters

from cq_model_socket_turned_pin import *
from cq_model_pin_switch import *
from cq_model_piano_switch import *
from cq_model_smd_switch import *
from cq_model_smd_switch_copal import *
from cq_model_smd_switch_omron_a6h import *

###########################
#  Model scratchpad area  #
###########################

from math import sqrt, tan, radians

###########################
# End of scratchpad area  #
###########################

family = 7
parts = [
 dip_socket_turned_pin,
 dip_switch,
 dip_switch_low_profile,
 dip_switch_piano,
 dip_smd_switch,
 dip_switch_copal_CHS_A,
 dip_switch_copal_CHS_B,
 dip_switch_omron_a6h
]

global ksu_present
ksu_present = False

def closeCurrentDoc(title):
    mw = FreeCADGui.getMainWindow()
    mdi = mw.findChild(QtGui.QMdiArea)
    mdiWin = mdi.currentSubWindow()
    print mdiWin.windowTitle()

    # We have a 3D view selected so we need to find the corresponding script window
    if mdiWin == 0 or ".FCMacro" not in mdiWin.windowTitle():
        subList = mdi.subWindowList()
        for sub in subList:
            print sub.windowTitle().split(':')[0].strip()
            if sub.windowTitle().split(':')[0].strip() == title:
                sub.close()
                return

def make_3D_model(models_dir, genericName, part, save_memory):

    if part.make_me != True:
        FreeCAD.Console.PrintMessage(' - not made')
        return

    global ksu_present

    LIST_license = ["",]

    modelName = part.make_modelname(genericName)

    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument = Gui.getDocument(CheckedmodelName)
    
    part.make()
    
    #stop

    doc = FreeCAD.ActiveDocument
    objs = GetListOfObjects(FreeCAD, doc)

    material_substitutions = {}
    
    for i in range(0, len(objs)):
        Color_Objects(Gui, objs[i], shaderColors.named_colors[part.color_keys[i]].getDiffuseFloat())
        material_substitutions[Gui.ActiveDocument.getObject(objs[i].Name).DiffuseColor[0][:-1]] = part.color_keys[i]

    expVRML.say(material_substitutions)
    expVRML.say(part.color_keys)
    expVRML.say(part.offsets)

    doc.Label = CheckedmodelName

    while len(objs) > 1:
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
        del objs
        objs = GetListOfObjects(FreeCAD, doc)

    objs[0].Label = CheckedmodelName
    restore_Main_Tools()

    #rotate if required
    if (part.rotation != 0):
        z_RotateObject(doc, part.rotation)
 
    s = objs[0].Shape
    shape = s.copy()
    shape.Placement = s.Placement;
    shape.translate(part.offsets)
    objs[0].Placement = shape.Placement

    expVRML.say(models_dir)

    out_dir = models_dir + os.sep + part.destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # export STEP model
    exportSTEP(doc, modelName, out_dir)

    if LIST_license[0] == "":
        LIST_license = Lic.LIST_int_license
        LIST_license.append("")

    Lic.addLicenseToStep(out_dir + os.sep, modelName + ".step", LIST_license, part.licAuthor, part.licEmail, part.licOrgSys, part.licOrg, part.licPreProc)

    # scale and export Vrml model
    scale = 1.0 / 2.54
    objs = GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name = out_dir + os.sep + modelName + '.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects, scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, modelName, out_dir)

    if not save_memory and part.footprints_dir is not None and footprints_dir is not None and os.path.isdir(footprints_dir):

        sys.argv = ["fc", "dummy", footprints_dir + os.sep + part.footprints_dir + os.sep + modelName, "savememory"]

        expVRML.say('Footprint: ' + sys.argv[2])

        if not ksu_present:
            try:
                import kicadStepUptools
                ksu_present = True
                expVRML.say("ksu present!")
                kicadStepUptools.KSUWidget.close()
                #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
                #kicadStepUptools.KSUWidget.destroy()
                #for i in QtGui.qApp.topLevelWidgets():
                #    if i.objectName() == "kicadStepUp":
                #        i.deleteLater()
                kicadStepUptools.KSUWidget.close()
            except:
                ksu_present = False
                expVRML.say("ksu not present")

        if ksu_present:
            kicadStepUptools.KSUWidget.close()
            reload(kicadStepUptools)
            kicadStepUptools.KSUWidget.close()
            #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
            #kicadStepUptools.KSUWidget.destroy()

    #display BBox
    if save_memory == False:
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()
    else:
        closeCurrentDoc(CheckedmodelName)

import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    full_path = os.path.realpath(__file__)
    expVRML.say(full_path)
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    expVRML.say(scriptdir)
    sub_path = full_path.split(scriptdir)
    expVRML.say(sub_path)
    sub_dir_name = full_path.split(os.sep)[-2]
    expVRML.say(sub_dir_name)
    sub_path = full_path.split(sub_dir_name)[0]
    expVRML.say(sub_path)
    models_dir = sub_path + "_3Dmodels"

    if len(sys.argv) < 3 or not (sys.argv[2] == "all" or sys.argv[2] == "allsmd"):
# TODO: validate user input!
        if sys.argv[0] == "fc":
            sys.argv = [""]
        variant =  parts[family].default_model if len(sys.argv) < 3 else sys.argv[2]
        FreeCAD.Console.PrintMessage('No variant name is given! building ' + variant)
        make_3D_model(models_dir, variant, parts[family](all_params[variant]), False)
    else:
        buildAllSMD = model_to_build == "allsmd"
        variants = all_params.keys()
        
        for i in range(0, len(variants) - 1):
            for variant in variants:
                FreeCAD.Console.PrintMessage('\r\nFamily: ' + str(family) + ': ' + variant)
                if not variant in all_params:
                    print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
                    continue
                if (buildAllSMD == False or all_params[variant].type == CASE_SMD_TYPE):
                    make_3D_model(models_dir, variant, parts[i](all_params[variant]), True)

    FreeCAD.Console.PrintMessage('\r\nDone\r\n')

### EOF ###

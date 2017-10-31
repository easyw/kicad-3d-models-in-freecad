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
#* Maurice https://launchpad.net/~easyw                                     *
#* Terje Io https://github.com/terjeio                                      *
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

___ver___ = "1.0.0 31/10/2017"

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
import re, fnmatch

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
#from Gui.Command import *

models_dir = None 
#models_dir = os.getenv('KISYS3DMOD') # write directly to prod folder if configured, comment out to write relative to main script folder
if models_dir == None:
    models_dir = os.path.dirname(os.path.realpath(__file__))
    models_dir = models_dir.split(models_dir.split(os.sep)[-1])[0] + "_3Dmodels"

script_dir = os.path.dirname(os.path.realpath(__file__))
footprints_dir = os.getenv('KISYSMOD')

scriptsource = "https://github.com/easyw/kicad-3d-models-in-freecad/tree/master/cadquery/FCAD_script_generator/"

#sys.path.append(models_dir)
sys.path.append(script_dir)
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

from cq_base_model import part
from cq_parameters import * # Generic DIP parameters

import cq_model_socket_turned_pin
import cq_model_pin_switch
import cq_model_piano_switch
import cq_model_smd_switch
import cq_model_smd_switch_copal
import cq_model_smd_switch_omron_a6h

#reload(cq_model_smd_switch_omron_a6h)

series = [
 cq_model_socket_turned_pin.dip_socket_turned_pin,
 cq_model_pin_switch.dip_switch,
 cq_model_pin_switch.dip_switch_low_profile,
 cq_model_piano_switch.dip_switch_piano,
 cq_model_smd_switch.dip_smd_switch,
 cq_model_smd_switch_copal.dip_switch_copal_CHS_A,
 cq_model_smd_switch_copal.dip_switch_copal_CHS_B,
 cq_model_smd_switch_omron_a6h.dip_switch_omron_a6h
]

family = 0 # set to None to generate all series

global kicadStepUptools
kicadStepUptools = None # set to False to disable, None to enable if present

global license
license = None

def closeCurrentDoc(title):
    mw = FreeCADGui.getMainWindow()
    mdi = mw.findChild(QtGui.QMdiArea)
    mdiWin = mdi.currentSubWindow()
#    print mdiWin.windowTitle()

    # We have a 3D view selected so we need to find the corresponding script window
    if mdiWin == 0 or ".FCMacro" not in mdiWin.windowTitle():
        subList = mdi.subWindowList()
        for sub in subList:
            print sub.windowTitle().split(':')[0].strip()
            if sub.windowTitle().split(':')[0].strip() == title:
                sub.close()
                return

def make_3D_model(models_dir, genericName, model, save_memory):

    modelName = model.make_modelname(genericName)

    FreeCAD.Console.PrintMessage('\r\n' + modelName)

    if model.make_me != True:
        FreeCAD.Console.PrintMessage(' - not made')
        return

    global license
    global kicadStepUptools

    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument = Gui.getDocument(CheckedmodelName)
    
    model.make()
    
    #stop

    doc = FreeCAD.ActiveDocument
    objs = GetListOfObjects(FreeCAD, doc)

    material_substitutions = {}
    
    for i in range(0, len(objs)):
        Color_Objects(Gui, objs[i], shaderColors.named_colors[model.color_keys[i]].getDiffuseFloat())
        material_substitutions[Gui.ActiveDocument.getObject(objs[i].Name).DiffuseColor[0][:-1]] = model.color_keys[i]

    expVRML.say(material_substitutions)
    expVRML.say(model.color_keys)
    expVRML.say(model.offsets)

    doc.Label = CheckedmodelName

    while len(objs) > 1:
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
        del objs
        objs = GetListOfObjects(FreeCAD, doc)

    objs[0].Label = CheckedmodelName
    restore_Main_Tools()

    #rotate if required
    if (model.rotation != 0):
        z_RotateObject(doc, model.rotation)
 
    s = objs[0].Shape
    shape = s.copy()
    shape.Placement = s.Placement;
    shape.translate(model.offsets)
    objs[0].Placement = shape.Placement

    out_dir = models_dir + os.sep + model.destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # export STEP model
    exportSTEP(doc, modelName, out_dir)

    if license == None:
        license = list(Lic.LIST_int_license) # make a copy to avoid modifying the original
        license.append("")
        license.append("")
        if scriptsource != "":
            license.append("Generated by script, source at:")
            license.append(scriptsource + script_dir.split(os.sep)[-1])
            license.append("")

    expVRML.say("")

    Lic.addLicenseToStep(out_dir + os.sep, modelName + ".step", license, model.licAuthor, model.licEmail, model.licOrgSys, model.licOrg, model.licPreProc)

    # scale and export Vrml model
    scale = 1.0 / 2.54
    objs = GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name = out_dir + os.sep + modelName + '.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects, scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, license)

    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, modelName, out_dir)

    if not save_memory and model.footprints_dir is not None and footprints_dir is not None and os.path.isdir(footprints_dir):

        sys.argv = ["fc", "dummy", footprints_dir + os.sep + model.footprints_dir + os.sep + modelName, "savememory"]

        expVRML.say('Footprint: ' + sys.argv[2])

        if kicadStepUptools == None:
            try:
                import kicadStepUptools
                expVRML.say("ksu present!")
                kicadStepUptools.KSUWidget.close()
                #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
                #kicadStepUptools.KSUWidget.destroy()
                #for i in QtGui.qApp.topLevelWidgets():
                #    if i.objectName() == "kicadStepUp":
                #        i.deleteLater()
                kicadStepUptools.KSUWidget.close()
            except:
                kicadStepUptools = False
                expVRML.say("ksu not present")

        if not kicadStepUptools == False:
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

if __name__ == "__main__" or __name__ == "main_generator":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    expVRML.say(models_dir)
    expVRML.say(script_dir)

    models_made = 0

    if len(sys.argv) >= 3 and not all_params.has_key(sys.argv[2]):

        models = get_all_models(series)

        if sys.argv[2] == "list":
            for variant in sorted(models):
                expVRML.say(variant)
        else:
            buildAllSMD = sys.argv[2] == "allsmd"
            filter = '*' if sys.argv[2] == "all" or sys.argv[2] == "allsmd" else sys.argv[2]
            filter = re.compile(fnmatch.translate(filter))
            for variant in models.keys():
                if filter.match(variant):
                    params = models[variant].params
                    model = models[variant].model(params)
                    if (buildAllSMD == False or params.type == CASE_SMD_TYPE) and model.make_me:
                        models_made = models_made + 1
                        make_3D_model(models_dir, variant, model, True)
    else:

        if family == None:

            models = get_sample_models(series)

            for variant in models.keys():
                params = models[variant].params
                model = models[variant].model(params)
                if model.make_me:
                    models_made = models_made + 1
                    make_3D_model(models_dir, variant, model, False)
                else:    
                    FreeCAD.Console.PrintMessage('\r\n' + model.make_modelname(variant) + ' - not made')

        else:

            variant_to_build = "" if len(sys.argv) < 3 else sys.argv[2]
            if variant_to_build == "":
                FreeCAD.Console.PrintMessage('No variant name is given! building default variants')
            for i in range(family, family + 1):
                variant = series[i].default_model if variant_to_build == "" else variant_to_build
                model = series[i](all_params[variant])
                if model.make_me:
                    models_made = models_made + 1
                    make_3D_model(models_dir, variant, series[i](all_params[variant]), False)
                else:    
                    FreeCAD.Console.PrintMessage('\r\n' + model.make_modelname(variant) + ' - not made')

    if models_made == 0:
        FreeCAD.Console.PrintMessage('\r\nDone - no models matched the provided filter!')
    else:  
        FreeCAD.Console.PrintMessage('\r\nDone - models made: ' + str(models_made))

    sys.argv = [""]

### EOF ###

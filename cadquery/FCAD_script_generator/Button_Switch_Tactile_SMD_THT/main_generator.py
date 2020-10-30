#!/usr/bin/python
# -*- coding: utf-8 -*-
#


#****************************************************************************
#*                                                                          *
#* scripts for generating generic parameters for tactile switches different *
#* types: Omron, C&K, Alps, Panasonic, Wuerth, etc.                         *
#*                                                                          *
#* This is part of FreeCAD & cadquery tools                                 *
#* to export generated models in STEP & VRML format.                        *
#*   Copyright (c) 2020                                                     *
#* Mountyrox   https://github.com/mountyrox                                 *
#*                                                                          *
#*                                                                          *
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




# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd


# Dimensions are from data sheets given in the settings of the corresponding KiCad footprint:

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py all

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

__title__ = "make Tact switch 3D models"
__author__ = "MountyRox, based on DIP_parts and Buzzer_Beeper scripts"
__Comment__ = 'make tactile switches 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.0 21/10/2020"

import collections
from collections import namedtuple

import math
import sys, os
import datetime
from datetime import datetime
import re, fnmatch

outdir=os.path.dirname(os.path.realpath(__file__)+"/../_3Dmodels")
script_dir  = os.path.dirname(os.path.realpath(__file__))
scripts_root = script_dir.split(script_dir.split(os.sep)[-1])[0]

print (script_dir)
sys.path.append(script_dir)
sys.path.append(scripts_root + "_tools")

import exportPartToVRML as expVRML
import shaderColors


# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
#from Gui.Command import *


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

def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)



import cq_parameters 
reload_lib(cq_parameters)

import cq_base_model  
reload_lib(cq_base_model)

# models for Omron, Panasonic, C&K, Alps tactile switches
import cq_base_tact_switches 
from cq_base_tact_switches import cqMakerTactSwitch, TactSwitchSeries, partsTactSwitches
reload_lib(cq_base_tact_switches)

# models for C&K PTS125 and Wuerth  tactile switches
import cq_cuk_pts125sx  
from cq_cuk_pts125sx import parts_cuk_pts125s, cqMakerCuKPTS125SxTactSwitch
reload_lib(cq_cuk_pts125sx)

# models for side actuated switches from Omron, Panasonic
import cq_ultra_small_tact_switch  
from cq_ultra_small_tact_switch import *
reload_lib(cq_ultra_small_tact_switch)

# models for C&K KMR2 tactile switches
import cq_cuk_kmr2x  
from cq_cuk_kmr2x import *
reload_lib(cq_cuk_kmr2x)

# models for C&K PTS810 tactile switches
import cq_cuk_pts810x  
from cq_cuk_pts810x import *
reload_lib(cq_cuk_pts810x)


def clear_console():
    #clearing previous messages
    mw=FreeCADGui.getMainWindow()
    c=mw.findChild(QtGui.QPlainTextEdit, "Python console")
    c.clear()
    r=mw.findChild(QtGui.QTextEdit, "Report view")
    r.clear()

clear_console()


# Array of model classes
different_models = [
    partsTactSwitches(),
    parts_cuk_pts125s(),
    partsUltraSmallTactSwitches(),
    parts_cuk_kmr2(),
    parts_cuk_pts810(),
    ]


def make_3D_model(models_dir, model_class, modelName):
    r"""Creates a 3D model and exports it to STEO and VRML.
    :param models_dir: directory name for STEP and VRML 3D model file export
    :type  models_dir: ``string``
    :param model_class: Class containing functions and parameter to generate the 3D model
    :type  model_class: ``class``
    :param modelName: The KiCad file name of the 3D model. 
    :type  modelName: ``string``

    """
    if not model_class.isValidModel ():
        FreeCAD.Console.PrintMessage("Model: " + modelName + ' has invalid parameter and was skipped.\r\n')
        return

    LIST_license = ["",]

    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)
    destination_dir = model_class.get_dest_3D_dir()
    
    material_substitutions = model_class.make_3D_model()
    
    doc = FreeCAD.ActiveDocument
    doc.Label = CheckedmodelName

    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = CheckedmodelName
    restore_Main_Tools()

    script_dir=os.path.dirname(os.path.realpath(__file__))
    expVRML.say(models_dir)
    out_dir=models_dir+os.sep+destination_dir
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
    export_file_name=out_dir + os.sep + modelName + '.wrl'
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
    
    model_to_build = ''
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('\
            No variant name is given, add a valid model name as an argument.\r\n\r\n\
            Valid arguments are:\r\n\
           \t"all"\t\t generate all models\r\n\
           \t"list"\t\t lists all models\r\n\r\n\
           or any search pattern like:\r\n\
           \t"*b3fs*"\t\t to generate all models containing B3SF\r\n')
        #model_to_build =  '*b3fs-105*'#
    else:
        model_to_build=sys.argv[2]

    found_one = False
    listOnly = model_to_build == 'list'

    if len(model_to_build) > 0:
        qfilter = '*' if model_to_build == "all" or model_to_build == "list" else model_to_build
        qfilter = re.compile(fnmatch.translate(qfilter), re.IGNORECASE)
        for modelType in different_models:
            paramList = modelType.get_param_list_all()  # get param list of all variants 
            for iParam in paramList:
                if listOnly:
                    FreeCAD.Console.PrintMessage('Model :' + iParam + '\r\n')
                else:
                    if qfilter.match(iParam):
                        found_one = True
                        #listModelsToBuild.append(modelType.getModelVariant (iParam))
                        # make an instance of the current model and initialize it with the corresponding parameter set
                        model = modelType.getModelVariant (iParam)
                        make_3D_model (models_dir, model, iParam)
                        #model.make_3D_model ()

        if not found_one and not listOnly:
            FreeCAD.Console.PrintMessage("\r\n========  Parameters for %s doesn't exist, skipping. ==========\r\n " % model_to_build)

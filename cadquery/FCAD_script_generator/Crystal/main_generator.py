# -*- coding: utf-8 -*-
#!/usr/bin/python
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

__title__ = "make Valve 3D models"
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

import add_license as Lic

#################################################################################################


import cq_parameters_Resonator_SMD_muRata_CSTx  # modules parameters
from cq_parameters_Resonator_SMD_muRata_CSTx import *

import cq_parameters_Resonator_AT310  # modules parameters
from cq_parameters_Resonator_AT310 import *

import cq_parameters_Resonator_C26_LF  # modules parameters
from cq_parameters_Resonator_C26_LF import *

import cq_parameters_Resonator_C38_LF  # modules parameters
from cq_parameters_Resonator_C38_LF import *

import cq_parameters_Resonator_peterman_smd  # modules parameters
from cq_parameters_Resonator_peterman_smd import *

import cq_parameters_Resonator_smd_type_2  # modules parameters
from cq_parameters_Resonator_smd_type_2 import *

different_models = [
    cq_parameters_Resonator_SMD_muRata_CSTx(),
    cq_parameters_Resonator_AT310(),
    cq_parameters_Resonator_C26_LF(),
    cq_parameters_Resonator_C38_LF(),
    cq_parameters_Resonator_peterman_smd(),
    cq_parameters_Resonator_smd_type_2(),
]


global save_memory
save_memory = False #reducing memory consuming for all generation params





def make_3D_model(models_dir, model_class, modelName):

    LIST_license = ["",]

    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)
    destination_dir = model_class.get_dest_3D_dir(modelName)
    
    model_filename = model_class.get_dest_file_name(modelName)
    
    material_substitutions = model_class.make_3D_model(modelName)
    
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

    exportSTEP(doc, model_filename, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', model_filename+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,model_filename,scale,out_dir)
    del objs
    objs=GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir+os.sep+model_filename+'.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
    Gui.activateWorkbench("PartWorkbench")
    # 
    if save_memory == False:
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()

    check_Model=True
    if save_memory == True:
        check_Model=True
        doc=FreeCAD.ActiveDocument
        FreeCAD.closeDocument(doc.Name)

    step_path=os.path.join(out_dir,model_filename+u'.step')
    docu = FreeCAD.ActiveDocument
    if check_Model==True:
        #ImportGui.insert(step_path,model_filename)
        ImportGui.open(step_path)
        docu = FreeCAD.ActiveDocument
        if cq_cad_tools.checkUnion(docu) == True:
            FreeCAD.Console.PrintMessage('step file for ' + model_filename + ' is correctly Unioned\n')
        else:
            FreeCAD.Console.PrintError('step file ' + model_filename + ' is NOT Unioned\n')
            FreeCAD.closeDocument(docu.Name)
            if save_memory == True:
                sys.exit()

    if save_memory == False:
        saveFCdoc(App, Gui, docu, model_filename,out_dir, False)
    
    if save_memory == True:
        FreeCAD.closeDocument(docu.Name)

def run():
    ## # get variant names from command line

    return


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
        FreeCAD.Console.PrintMessage('No variant name is given, add a valid model name as an argument or the argument "all"\r\n')
    else:
        model_to_build=sys.argv[2]

    
    found_one = False
    if len(model_to_build) > 0:
        if model_to_build == 'all' or model_to_build == 'All' or model_to_build == 'ALL':
            save_memory = True
            found_one = True
            for n in different_models:
                listall = n.get_list_all()
                for i in listall:
                    FreeCAD.Console.PrintMessage('\r\nMaking model :' + i + '\r\n')
                    make_3D_model(models_dir, n, i)
        else:
            for n in different_models:
                if n.model_exist(model_to_build):
                    found_one = True
                    make_3D_model(models_dir, n, model_to_build)
        
        if not found_one:
            print("Parameters for %s doesn't exist, skipping. " % model_to_build)

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

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py L35_D12.5_p05

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

__title__ = "make Standoff 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make Standoff Caps 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.3 23/01/2020"

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

body_color_key = "metal grey pins"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()


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

LIST_license = ["",]
#################################################################################################

# Import cad_tools
import cq_cad_tools
# Reload tools
try:
    reload(cq_cad_tools)
except:
    import importlib
    importlib.reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements


try:
    # Gui.SendMsgToActiveView("Run")
    # cq Gui            
    #from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print ("CQ 030 doesn't open example file")

import cq_parameters  # modules parameters
from cq_parameters import *

all_params = kicad_naming_params_standoff

def make_standoff(params):
    OD = params.OD # Outer Diameter, Flat side to flatside for HEX
    ID = params.ID # Inner Diameter
    H = params.H # Height of standoff
    shape = params.shape # Shape can be 'Round' or 'Hex'
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix
    
    if shape == 'Hex':
        a = OD/sqrt(3)
        body = cq.Workplane("XY").polygon(6, a*2).extrude(H)
        body = body.cut(cq.Workplane("XY").circle(ID/2).extrude(H))
    if shape == 'Round':
        body = cq.Workplane("XY").circle(OD/2).extrude(H)
        body = body.cut(cq.Workplane("XY").circle(ID/2).extrude(H))
    body = body.edges(">Z").fillet(a/20)
    body = body.edges("<Z").fillet(a/20)
    if params.stud_H > 0:
        body = body.union(cq.Workplane("XY").circle(ID/2).extrude(-params.stud_H-0.5).translate((0.0,0.0,0.5)))
        body = body.edges("<Z").fillet(a/20)

    #show(body)
    #show(leads)
    #stop
    return (body) #body, pins

    
#import step_license as L
import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":
    expVRML.say(expVRML.__file__)
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
    #expVRML.say(models_dir)
    #stop

    color_pin_mark=True
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building qfn16')
        model_to_build='L10_D5'
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
        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        #CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        CheckedModelName = ModelName.replace('-', '_').replace('(', '').replace(')', '')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(Newdoc.Name)
        Gui.ActiveDocument=Gui.getDocument(Newdoc.Name)
        #body, base, mark, pins = make_rect_th(all_params[variant])
        body= make_standoff(all_params[variant]) #body, base, mark, pins, top
        
        
        show(body)
        
        doc = FreeCAD.ActiveDocument
        objs = GetListOfObjects(FreeCAD, doc)
        Color_Objects(Gui,objs[0],body_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]

        material_substitutions={
            col_body[:-1]:body_color_key,
            }
        expVRML.say(material_substitutions)
        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        #stop
        doc.Label = CheckedModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label = CheckedModelName
        restore_Main_Tools()
        #rotate if required
        objs=GetListOfObjects(FreeCAD, doc)
        FreeCAD.Rotation(FreeCAD.Vector(0,0,1),all_params[variant].rotation)
        #out_dir=destination_dir+all_params[variant].dest_dir_prefix+'/'
        script_dir=os.path.dirname(os.path.realpath(__file__))
        expVRML.say(script_dir)
        #out_dir=script_dir+os.sep+destination_dir+os.sep+all_params[variant].dest_dir_prefix
        out_dir=models_dir+destination_dir
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        #out_dir="./generated_qfp/"
        # export STEP model
        exportSTEP(doc, ModelName, out_dir)
        if LIST_license[0]=="":
            LIST_license=Lic.LIST_int_license
            LIST_license.append("")
        Lic.addLicenseToStep(out_dir+'/', ModelName+".step", LIST_license,\
                           STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

        # scale and export Vrml model
        scale=1/2.54
        #exportVRML(doc,ModelName,scale,out_dir)
        objs=GetListOfObjects(FreeCAD, doc)
        expVRML.say("######################################################################")
        expVRML.say(objs)
        expVRML.say("######################################################################")
        export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
        export_file_name=out_dir+os.sep+ModelName+'.wrl'
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox
        #FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()
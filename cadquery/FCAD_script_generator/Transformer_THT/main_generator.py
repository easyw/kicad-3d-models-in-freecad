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
## e.g. c:\freecad\bin\freecad main_generator.py QFN-28-1EP_6x6mm_Pitch0.65mm

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

__title__ = "make QFN ICs 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make QFN ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.5 25/Feb/2017"

###ToDo: QFN with ARC pad, exposed pad with chamfer

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

LIST_license = ["",]
#################################################################################################

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
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"

import cq_parameters  # modules parameters
from cq_parameters import *


def make_transformer(params):

    modelName = params.modelName
    serie = params.serie
    A1 = params.A1
    body = params.body
    top = params.top
    pin = params.pin
    npth = params.npth
    rotation = params.rotation

    # Dummy
    tx = body[0]
    if body[0] < 0:
        tx = tx + 1
    else:
        tx = body[0] - 1
    ty = body[1]
    if body[0] < 0:
        ty = ty + 1
    else:
        ty = body[0] - 1
    case_top = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(tx, 0-ty).rect(0.1, 0.1, False).extrude(0.1)

    if top != None:
        case_top = cq.Workplane("XY").workplane(offset=A1 + body[4] - 0.1).moveTo(top[0], 0-top[1]).rect(top[2], 0-top[3], False).extrude(top[4] + 0.1)
        case_top = case_top.faces(">Y").edges("<X").fillet(1.0)
        case_top = case_top.faces(">Y").edges(">X").fillet(1.0)
        case_top = case_top.faces("<Y").edges("<X").fillet(1.0)
        case_top = case_top.faces("<Y").edges(">X").fillet(1.0)
        case_top = case_top.faces(">Z").edges(">X").fillet(1.0)
        #
        if (rotation != 0):
            case_top = case_top.rotate((0,0,0), (0,0,1), rotation)    
    
    case = cq.Workplane("XY").workplane(offset=A1).moveTo(body[0], 0-body[1]).rect(body[2], 0-body[3], False).extrude(body[4])
    case = case.faces(">Y").edges("<X").fillet(1.0)
    case = case.faces(">Y").edges(">X").fillet(1.0)
    case = case.faces("<Y").edges("<X").fillet(1.0)
    case = case.faces("<Y").edges(">X").fillet(1.0)
    case = case.faces(">Z").edges(">X").fillet(1.0)
    #
    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)    
        
    p = pin[0]
    pins = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(p[2] / 2.6, False).extrude(0 - (p[3] + A1 + 1.0))
    pins = pins.faces("<Z").fillet(p[2] / 5.0)
    for i in range(1, len(pin)):
        p = pin[i]
        pint = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(p[2] / 2.6, False).extrude(0 - (p[3] + A1 + 1.0))
        pint = pint.faces("<Z").fillet(p[2] / 5.0)
        pins = pins.union(pint)

    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)
    
    return (case_top, case, pins)

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

    color_pin_mark=True
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building Transformer_37x44')
        model_to_build='Transformer_37x44'
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
        save_memory=True
    else:
        variants = [model_to_build]

        
        
    for variant in variants:
        body_top_color_key = all_params[variant].body_top_color_key
        body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
        body_color_key = all_params[variant].body_color_key
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        pins_color_key = all_params[variant].pin_color_key
        pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
        #
        excluded_pins_x=() ##no pin excluded
        excluded_pins_xmirror=() ##no pin excluded
        place_pinMark=True ##default =True used to exclude pin mark to build sot23-3; sot23-5; sc70 (asimmetrical pins, no pinmark)

        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        case_top, case, pins = make_transformer(all_params[variant])

        show(case_top)
        show(case)
        show(pins)
        #stop
        
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)

        Color_Objects(Gui,objs[0], body_top_color)
        Color_Objects(Gui,objs[1], body_color)
        Color_Objects(Gui,objs[2], pins_color)

        col_body_top=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_body=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        material_substitutions={
            col_body_top[:-1]:body_top_color_key,
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pins_color_key
        }
        expVRML.say(material_substitutions)
        ## objs[0].Label='body'
        ## objs[1].Label='pins'
        ## objs[2].Label='mark'
        ###
        ## print objs[0].Name, objs[1].Name, objs[2].Name

        ## sleep
        #if place_pinMark==True:
        ###
        #sleep
        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[1].Name)
        doc.Label=CheckedModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label=CheckedModelName
        restore_Main_Tools()
        #rotate if required
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
            z_RotateObject(doc, rot)
        #out_dir=destination_dir+all_params[variant].dest_dir_prefix+'/'
        script_dir=os.path.dirname(os.path.realpath(__file__))
        #models_dir=script_dir+"/../_3Dmodels"
        expVRML.say(models_dir)
        if len(all_params[variant].dest_dir_prefix)>=1:
            out_dir=models_dir+destination_dir+os.sep+all_params[variant].dest_dir_prefix
        else:
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
        #expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox
        #FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        #Gui.activeDocument().activeView().viewBottom()
        Gui.activeDocument().activeView().viewAxometric()

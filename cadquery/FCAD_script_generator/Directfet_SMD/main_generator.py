# -*- coding: utf8 -*-
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

## to run the script just do: freecad make_gwexport_fc.py modelName
## e.g. c:\freecad\bin\freecad make_gw_export_fc.py SOIC_8

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

__title__ = "make DirecFETs 3D models"
__author__ = "maurice"
__Comment__ = 'make DirecFETs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.2 09/02/2017"

# thanks to Frank Severinsen Shack for including vrml materials

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt, sin
from collections import namedtuple

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "metal grey pins"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
die_color_key = "brown body"
die_color = shaderColors.named_colors[die_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
#from Gui.Command import *

import logging
logging.getLogger('builder').addHandler(logging.NullHandler())
#logger = logging.getLogger('builder')
#logging.info("Begin")

outdir=os.path.dirname(os.path.realpath(__file__)+"/../_3Dmodels")
scriptdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)
sys.path.append(scriptdir)

#import PySide
#from PySide import QtGui, QtCore
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


# from export_x3d import exportX3D, Mesh
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

all_params= kicad_naming_params_DirecFETs
#all_params= all_params_DirecFETs

def make_chip(params):
    # dimensions for DirectFET's
    A = params.A    # package length 
    B = params.B    # package width 
    C = params.C    # wing width
    D = params.D    # wing length

    M = params.M   # package height
    P = params.P   # die and body height over board
    R = params.R   # pad height over board

    if params.die:
        die_size_x = params.die[0]
        die_size_y = params.die[1]
        if len(params.die) > 2:
            die_pos_x = params.die[2]
            die_pos_y = params.die[3]
        else:
            die_pos_x = 0
            die_pos_y = 0

    pads = params.pads # pads
    
    modelName = params.modelName  # Model Name
    rotation = params.rotation   # rotation

    top_subtract = B -(B * 0.9)
    top_width = B - top_subtract
    top_lenght = (A-2*D)-top_subtract

    ec = (B-C)/2/3  # chamfer of edges
    shell_thickness = 0.1

    a = sin(45) * ec
    inner_ec = (a-shell_thickness/4)/sin(45)
    top_ec = inner_ec
    
    # Create a 3D box based on the dimension variables above and fillet it
    case = cq.Workplane("XY").box(A-2*D,B, (M-(P+R))*0.5, centered=(True, True, False))
    case.edges("|Z").chamfer(ec)
    case = case.edges("|Y").edges(">Z").fillet(((M-(P+R))*0.5)+P+R-(M*0.5))

    subtract = cq.Workplane("XY").box(A-2*D-shell_thickness*2,B-shell_thickness*2, ((M-(P+R))*0.5)-0.1, centered=(True, True, False))
    if inner_ec > 0:
        subtract.edges("|Z").chamfer(inner_ec)
    case.cut(subtract)
    
    top = cq.Workplane("XY").box(top_lenght,top_width, (M-(P+R))*0.5, centered=(True, True, False))
    if top_ec > 0:
        top.edges("|Z").fillet(top_ec)
    top_fillet = ((M-(P+R))*0.5)*0.9
    top = top.edges(">Z").fillet(top_fillet)
    top = top.translate((0,0,(M-P-R)*0.5))
    case = case.union(top)
    case = case.translate((0,0,P+R))
    
    wing1 = cq.Workplane("XY").box(D,C, M*0.5, centered=(True, True, False)).translate(((A-D)/2,0,0))
    wing2 = cq.Workplane("XY").box(D,C, M*0.5, centered=(True, True, False)).translate((-(A-D)/2,0,0))
    case = case.union(wing1).union(wing2)
    die = cq.Workplane("XY").box(die_size_x, die_size_y, (M-P)*0.5-(P+R), centered=(True, True, False)).translate((die_pos_x,die_pos_y,P+R))

    for Pad in range(len(pads)):
        if Pad == 0:
            Pads = cq.Workplane("XY").box(pads[Pad][0], pads[Pad][1], (M-(P+R))*0.5+P, centered=(True, True, False)).translate((pads[Pad][2],pads[Pad][3],R)).edges("<Z").fillet(P*0.9)
        else:
            Pads = Pads.union(cq.Workplane("XY").box(pads[Pad][0], pads[Pad][1], (M-(P+R))*0.5+P, centered=(True, True, False)).translate((pads[Pad][2],pads[Pad][3],R)).edges("<Z").fillet(P*0.9))
    case = case.union(Pads)
    return (case, die)
    


# The dimensions of the box. These can be modified rather than changing the
# object's code directly.

#import step_license as L
import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":
    expVRML.say(expVRML.__file__)
    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    full_path=os.path.realpath(__file__)
    expVRML.say(full_path)
    scriside_pins_Thicknessdir=os.path.dirname(os.path.realpath(__file__))
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

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building 0402')
        model_to_build='0402'
    else:
        model_to_build=sys.argv[2]

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
        CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        case, die = make_chip(all_params[variant])

        show(case)
        show(die)
   
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
        
        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],die_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_die=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]

        material_substitutions={
            col_body[:-1]:body_color_key,
            col_die[:-1]:die_color_key
        }

        expVRML.say(material_substitutions)

        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
        doc.Label = CheckedModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label = CheckedModelName
        restore_Main_Tools()
        #rotate if required
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
            z_RotateObject(doc, rot)
        #out_dir=destination_dir+all_params[variant].dest_dir_prefix+'/'
        script_dir=os.path.dirname(os.path.realpath(__file__))
        ## models_dir=script_dir+"/../_3Dmodels"
        expVRML.say(models_dir)
        out_dir=models_dir+destination_dir
        #out_dir=script_dir+os.sep+destination_dir
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

        #export_file_name=destination_dir+os.sep+ModelName+'.wrl'
        #export_file_name=script_dir+os.sep+destination_dir+os.sep+ModelName+'.wrl'
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
        

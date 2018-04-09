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

__title__ = "make Radial Caps 3D models"
__author__ = "maurice and hyOzd and Frank"
__Comment__ = 'make C axial Caps 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.2 10/02/2017"


# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt, sin, degrees
from collections import namedtuple

global save_memory
save_memory = False #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "orange body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
marking_color_key = "light brown body"
marking_color = shaderColors.named_colors[marking_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
#from Gui.Command import *

cd_new_notfound=False
cd_notfound=False
try:
    from CadQuery.Gui.Command import *
except:
    cd_new_notfound=True
try:
    from Gui.Command import *
except:
    cd_notfound=True
if cd_new_notfound and cd_notfound:
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)



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

try:
    # Gui.SendMsgToActiveView("Run")
    # cq Gui
    #from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except Exception as e: # catch *all* exceptions
    print(e)
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

# Import cad_tools
from cqToolsExceptions import *
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements, runGeometryCheck

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"

import cq_parameters  # modules parameters
from cq_parameters import *

#all_params = all_params_c_axial_th_cap
all_params = kicad_naming_params_c_axial_th_cap

def make_tantalum_th(params):
    L = params.L    # body length
    W = params.W    # body width
    d = params.d     # lead diameter
    F = params.F     # lead separation (center to center)
    ll = params.ll   # lead length
    bs = params.bs   # board separation
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix

    bend_offset_y = (sin(radians(60.0))*d)/sin(radians(90.0))
    bend_offset_z = (sin(radians(30.0))*d)/sin(radians(90.0))
    # draw the leads
    lead1 = cq.Workplane("XY").workplane(offset=-ll).center(-F/2,0).circle(d/2).extrude(ll+L/4-d+bs)
    lead1 = lead1.union(cq.Workplane("XY").workplane(offset=L/4-d+bs).center(-F/2,0).circle(d/2).center(-F/2+d/2,0).revolve(30,(-F/2+d/2+d,d)).transformed((-30,0,0),(-(-F/2+d/2),d-bend_offset_y,bend_offset_z)).circle(d/2).extrude(L/2))
    lead1 = lead1.rotate((-F/2,0,0), (0,0,1), -90)
    lead2 = lead1.rotate((-F/2,0,0), (0,0,1), 180).translate((F,0,0))
    leads = lead1.union(lead2)

    oval_base_w = 2*d
    oval_base_L = L*0.7

    body = cq.Workplane("XY").workplane(offset=bs).moveTo(-(oval_base_L/2-d), -oval_base_w/2).threePointArc((-oval_base_L/2, 0),(-(oval_base_L/2-d),oval_base_w/2)).line(oval_base_L-d*2,0).\
    threePointArc((oval_base_L/2, 0),(oval_base_L/2-d,-oval_base_w/2)).close().extrude(d).edges("<Z").fillet(d/4)
    body = body.union(cq.Workplane("XY").workplane(offset=bs+d).moveTo(-(oval_base_L/2-d), -oval_base_w/2).threePointArc((-oval_base_L/2, 0),(-(oval_base_L/2-d),oval_base_w/2)).line(oval_base_L-d*2,0).\
    threePointArc((oval_base_L/2, 0),(oval_base_L/2-d,-oval_base_w/2)).close().workplane(offset=L).circle(L/2).loft(combine=True))
    middlepoint = (sin(radians(45.0))*L/2)/sin(radians(90.0))
    body = body.union(cq.Workplane("YZ").moveTo(0,bs+d+L).vLine(L/2,forConstruction=False).threePointArc((middlepoint, bs+d+L+middlepoint),(L/2, bs+d+L),forConstruction=False).close().revolve())
    plussize = L/3
    plusthickness = plussize/3
    pinmark = cq.Workplane("XZ").workplane(offset=-L/2-1).moveTo(-plusthickness/2-L/4,bs+d+L+plusthickness/2).line(0,plusthickness).line(plusthickness,0).line(0,-plusthickness).line(plusthickness,0).\
    line(0,-plusthickness).line(-plusthickness,0).line(0,-plusthickness).line(-plusthickness,0).line(0,plusthickness).line(-plusthickness,0).line(0,plusthickness).close().extrude(L+2).\
    edges(">X").edges("|Y").fillet(plusthickness/2.5).\
    edges("<X").edges("|Y").fillet(plusthickness/2.5).\
    edges(">Z").edges("|Y").fillet(plusthickness/2.5).\
    edges("<Z").edges("|Y").fillet(plusthickness/2.5)
    subtract_part = pinmark.translate((0, 0.01, 0)).cut(body)
    subtract_part = subtract_part.translate((0, -0.02, 0)).cut(body).translate((0, 0.01, 0))
    pinmark = pinmark.cut(subtract_part)
    #draw the body
    leads = leads.cut(body)
    #show(leads)
    return (body, leads, pinmark) #body, pins


#import step_license as L
import add_license as Lic

def generateOneModel(params, log):
    ModelName = params.modelName
    FreeCAD.Console.PrintMessage(
        '\n\n##############  ' +
        part_params['code_metric'] +
        '  ###############\n')
    CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedModelName)
    App.setActiveDocument(CheckedModelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
    #body, base, mark, pins = make_tantalum_th(params)
    body, pins, pinmark= make_tantalum_th(params) #body, base, mark, pins, top

    show(body)
    show(pins)
    show(pinmark)

    doc = FreeCAD.ActiveDocument
    print(GetListOfObjects(FreeCAD, doc))
    objs = GetListOfObjects(FreeCAD, doc)

    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],pins_color)
    Color_Objects(Gui,objs[2],marking_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]

    material_substitutions={
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pins_color_key,
        col_mark[:-1]:marking_color_key
    }
    expVRML.say(material_substitutions)
    del objs

    objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
    objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
    #stop
    doc.Label = CheckedModelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = CheckedModelName
    restore_Main_Tools()
    #rotate if required
    objs=GetListOfObjects(FreeCAD, doc)
    FreeCAD.getDocument(doc.Name).getObject(objs[0].Name).Placement = FreeCAD.Placement(FreeCAD.Vector(params.F/2,0,0),
    FreeCAD.Rotation(FreeCAD.Vector(0,0,1),params.rotation))
    #out_dir=destination_dir+params.dest_dir_prefix+'/'
    script_dir=os.path.dirname(os.path.realpath(__file__))

    expVRML.say(script_dir)
    #out_dir=script_dir+os.sep+destination_dir+os.sep+params.dest_dir_prefix

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

    if save_memory == False:
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()

    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, ModelName,out_dir)
    if save_memory == True:
        doc=FreeCAD.ActiveDocument
        FreeCAD.closeDocument(doc.Name)


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
        FreeCAD.Console.PrintMessage('No variant name is given! building C_Disc_D12.0mm_W4.4mm_P7.75mm')
        model_to_build='C_Disc_D12.0mm_W4.4mm_P7.75mm'
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
        save_memory = True
    else:
        variants = [model_to_build]
    with open(check_log_file, 'w') as log:
        for variant in variants:
            FreeCAD.Console.PrintMessage('\r\n'+variant)
            if not variant in all_params:
                print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
                continue
            params = all_params[variant]
            try:
                generateOneModel(params, log)
            except GeometryError as e:
                e.print_errors(stop_on_first_error)
                if stop_on_first_error:
                    break
            except FreeCADVersionError as e:
                FreeCAD.Console.PrintError(e)
                break
            else:
                traceback.print_exc()
                raise

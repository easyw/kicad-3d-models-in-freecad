# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This was originaly derived from a cadquery script for generating PDIP models in X3D format
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Adapted by easyw for step and vrlm export
# See https://github.com/easyw/kicad-3d-models-in-freecad

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad scriptName modelName
## e.g. FreeCAD export_conn_jst_xh.py all

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are FreeCAD & cadquery tools                                       *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating JST-XH models in STEP AP214               *
#*   Copyright (c) 2016                                                     *
#* Rene Poeschl https://github.com/poeschlr                                 *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU General Public License (GPL)             *
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

__title__ = "make 3D models of Molex KK 6410 series connectors"
__author__ = "scripts: maurice and hyOzd; models: hackscribble"
__Comment__ = '''make 3D models of Molex KK 6410 series connectors'''

___ver___ = "0.2 14/04/2017"


import sys
import os

full_path=os.path.realpath(__file__)
script_dir_name =full_path.split(os.sep)[-2]
parent_path = full_path.split(script_dir_name)[0]
out_dir = parent_path + "_3Dmodels" + "/" + script_dir_name

sys.path.append("../_tools")
sys.path.append("cq_models")

import shaderColors


# Model details
#################################################################################################

import conn_molex_6410 as KK_6410

series = [KK_6410]

body_color_key = "white body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseInt()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseInt()


import add_license as L

# Licence information of the generated models.
#################################################################################################

L.STR_int_licAuthor = "Ray Benitez"
L.STR_int_licEmail = "hackscribble@outlook.com"

#################################################################################################


from datetime import datetime
import exportPartToVRML as expVRML
import re
import fnmatch

import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
import Draft
import ImportGui

from Gui.Command import *

import cq_cad_tools
reload(cq_cad_tools)
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, multiFuseObjs_wColors

Gui.activateWorkbench("CadQueryWorkbench")

import FreeCADGui as Gui

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

# checking requirements

FreeCAD.Console.PrintMessage("FC Version \r\n")
FreeCAD.Console.PrintMessage(FreeCAD.Version())
FC_majorV=FreeCAD.Version()[0];FC_minorV=FreeCAD.Version()[1]
FreeCAD.Console.PrintMessage('FC Version '+FC_majorV+FC_minorV+'\r\n')

if int(FC_majorV) <= 0:
    if int(FC_minorV) < 15:
        reply = QtGui.QMessageBox.information(None,"Warning! ...","use FreeCAD version >= "+FC_majorV+"."+FC_minorV+"\r\n")

FreeCAD.Console.PrintMessage(FreeCAD.ConfigGet("AppHomePath")+'Mod/')
file_path_cq=FreeCAD.ConfigGet("AppHomePath")+'Mod/CadQuery'
if os.path.exists(file_path_cq):
    FreeCAD.Console.PrintMessage('CadQuery exists\r\n')
else:
    msg="missing CadQuery Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)

try:
    close_CQ_Example(App, Gui)
except:
    FreeCAD.Console.PrintMessage("can't close example.")


def export_one_part(modul, variant,  with_plug=False):
    if not variant in modul.all_params:
        FreeCAD.Console.PrintMessage("Parameters for %s not found - skipping." % variant)
        return
    ModelName = variant
    ModelName = ModelName.replace(".","_")
    FileName = modul.all_params[variant].file_name

    FreeCAD.Console.PrintMessage(FileName)

    Newdoc = FreeCAD.newDocument(ModelName)
    App.setActiveDocument(ModelName)
    App.ActiveDocument=App.getDocument(ModelName)
    Gui.ActiveDocument=Gui.getDocument(ModelName)
    (pins, body) = modul.generate_part(variant, with_plug)

    color_attr = body_color + (0,)
    show(body, color_attr)

    color_attr = pins_color + (0,)
    show(pins, color_attr)

    doc = FreeCAD.ActiveDocument
    doc.Label=ModelName
    objs=FreeCAD.ActiveDocument.Objects
    FreeCAD.Console.PrintMessage(objs)

    i=0
    objs[i].Label = ModelName + "__body"
    i+=1
    objs[i].Label = ModelName + "__pins"
    i+=1

    restore_Main_Tools()

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    used_color_keys = [body_color_key, pins_color_key]
    export_file_name=out_dir+os.sep+FileName+'.wrl'

    export_objects = []
    i=0
    export_objects.append(expVRML.exportObject(freecad_object = objs[i],
            shape_color=body_color_key,
            face_colors=None))
    i+=1
    export_objects.append(expVRML.exportObject(freecad_object = objs[i],
            shape_color=pins_color_key,
            face_colors=None))
    i+=1

    scale=1/2.54
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)

    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, L.LIST_int_license)

    fusion = multiFuseObjs_wColors(FreeCAD, FreeCADGui,
                     ModelName, objs, keepOriginals=True)

    exportSTEP(doc,FileName,out_dir,fusion)
    L.addLicenseToStep(out_dir+'/', FileName+".step", L.LIST_int_license,\
        L.STR_int_licAuthor, L.STR_int_licEmail, L.STR_int_licOrgSys, L.STR_int_licPreProc)

    saveFCdoc(App, Gui, doc, FileName,out_dir)

    FreeCAD.activeDocument().recompute()
    FreeCADGui.SendMsgToActiveView("ViewFit")
    FreeCADGui.activeDocument().activeView().viewAxometric()


if __name__ == "__main__":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    modelfilter = ""
    with_plug = False

    modelfilter = "*"

    model_filter_regobj=re.compile(fnmatch.translate(modelfilter))
    for typ in series:
        for variant in typ.all_params.keys():
            if model_filter_regobj.match(variant):
                FreeCAD.Console.PrintMessage('\r\n'+variant+'\r\n')
                export_one_part(typ, variant, with_plug)

    FreeCAD.Console.PrintMessage('\r\nDone\r\n')


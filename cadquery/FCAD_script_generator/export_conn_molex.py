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

__title__ = "make 3D models of molex 53261-Connectors."
__author__ = "scripts: maurice and hyOzd; models: poeschlr"
__Comment__ = '''make 3D models of JST-XH-Connectors types molex 53261. (Top entry)'''

___ver___ = "1.1 12/04/2016"

import sys, os
import datetime
from datetime import datetime
sys.path.append("../../exportVRMLwColors")
import exportPartToVRML as expVRML
import shaderColors

# Licence information of the generated models.
#################################################################################################
STR_licAuthor = "Rene Poeschl"
STR_licEmail = "poeschlr@gmail.com"
STR_licOrgSys = ""
STR_licPreProc = ""

LIST_license = ["Copyright (C) "+datetime.now().strftime("%Y")+", " + STR_licAuthor,
                "",
                "This program is free software: you can redistribute it and/or modify",
                "it under the terms of the GNU General Public License (GPL)",
                "as published by the Free Software Foundation, either version 2 of",
                "the License, or any later version.",
                "",
                "As a special exception, if you create a design which uses this symbol,",
                "and embed this symbol or unaltered portions of this symbol into the design,",
                "this symbol does not by itself cause the resulting design to be covered by",
                "the GNU General Public License. This exception does not however invalidate",
                "any other reasons why the design itself might be covered by the",
                "GNU General Public License. If you modify this symbol, you may extend this",
                "exception to your version of the symbol, but you are not obligated to do so.",
                "If you do not wish to do so, delete this exception statement from your version.",
                "",
                "This program is distributed in the hope that it will be useful,",
                "but WITHOUT ANY WARRANTY; without even the implied warranty of",
                "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the",
                "GNU General Public License for more details.",
                "",
                "You should have received a copy of the GNU General Public License",
                "along with this program.  If not, see http://www.gnu.org/licenses/.",
                ""
                ]
#################################################################################################

body_color_key = "white body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseInt()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseInt()

destination_dir="Connectors_Molex"

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

#checking requirements
#######################################################################
FreeCAD.Console.PrintMessage("FC Version \r\n")
FreeCAD.Console.PrintMessage(FreeCAD.Version())
FC_majorV=FreeCAD.Version()[0];FC_minorV=FreeCAD.Version()[1]
FreeCAD.Console.PrintMessage('FC Version '+FC_majorV+FC_minorV+'\r\n')

if int(FC_majorV) <= 0:
    if int(FC_minorV) < 15:
        reply = QtGui.QMessageBox.information(None,"Warning! ...","use FreeCAD version >= "+FC_majorV+"."+FC_minorV+"\r\n")


# FreeCAD.Console.PrintMessage(M.all_params_soic)
FreeCAD.Console.PrintMessage(FreeCAD.ConfigGet("AppHomePath")+'Mod/')
file_path_cq=FreeCAD.ConfigGet("AppHomePath")+'Mod/CadQuery'
if os.path.exists(file_path_cq):
    FreeCAD.Console.PrintMessage('CadQuery exists\r\n')
else:
    msg="missing CadQuery Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)

#######################################################################
from Gui.Command import *

outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

close_CQ_Example(App, Gui)


import cadquery as cq
from math import sqrt
from Helpers import show
from collections import namedtuple
import FreeCAD, Draft, FreeCADGui
import ImportGui
sys.path.append("cq_models")
import conn_molex_53261 as M1
import conn_molex_53398 as M2
import step_license as L

def export_one_part(modul, variant):
    if not variant in modul.all_params:
        FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'M.all_params', skipping." % variant)
        return
    ModelName = modul.all_params[variant].model_name
    FileName = modul.all_params[variant].file_name
    Newdoc = FreeCAD.newDocument(ModelName)
    App.setActiveDocument(ModelName)
    Gui.ActiveDocument=Gui.getDocument(ModelName)
    (pins, body) = modul.generate_part(variant)

    color_attr = body_color + (0,)
    show(body, color_attr)

    color_attr = pins_color + (0,)
    show(pins, color_attr)

    doc = FreeCAD.ActiveDocument
    doc.Label=ModelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = ModelName + "__body"
    objs[1].Label = ModelName + "__pins"

    restore_Main_Tools()

    out_dir=destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    used_color_keys = [body_color_key, pins_color_key]
    export_file_name=destination_dir+os.sep+FileName+'.wrl'

    export_objects = []
    export_objects.append(expVRML.exportObject(freecad_object = objs[0],
            shape_color=body_color_key,
            face_colors=None))
    export_objects.append(expVRML.exportObject(freecad_object = objs[1],
            shape_color=pins_color_key,
            face_colors=None))

    scale=1/2.54
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    fusion = FuseObjs_wColors(FreeCAD, FreeCADGui,
                    ModelName, objs[0].Name, objs[1].Name, keepOriginals=True)
    exportSTEP(doc,FileName,out_dir,fusion)
    L.addLicenseToStep(out_dir+'/', FileName+".step", LIST_license,\
        STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licPreProc)

    saveFCdoc(App, Gui, doc, FileName,out_dir)


if __name__ == "__main__":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building all')
        model_to_build='all'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = M1.all_params.keys()
    else:
        variants = [model_to_build]
    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n'+variant+'\r\n')
        export_one_part(M1,variant)

    if model_to_build == "all":
        variants = M2.all_params.keys()
    else:
        variants = [model_to_build]
    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n'+variant+'\r\n')
        export_one_part(M2,variant)

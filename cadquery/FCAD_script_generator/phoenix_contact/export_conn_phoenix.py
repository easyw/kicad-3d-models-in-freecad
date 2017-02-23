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

__title__ = "make 3D models of phoenix contact connectors (MSTB and MC series)."
__author__ = "scripts: maurice and hyOzd; models: poeschlr"
__Comment__ = '''make 3D models of phoenix contact types MSTB and MC.'''

___ver___ = "1.1 12/04/2016"

import sys, os
import datetime
from datetime import datetime
sys.path.append("./exportVRML")
import exportPartToVRML as expVRML
import shaderColors
import re, fnmatch
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

body_color_key = "green body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseInt()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseInt()
insert_color_key = "gold pins"
insert_color = shaderColors.named_colors[insert_color_key].getDiffuseInt()
screw_color_key = "metal grey pins"
screw_color = shaderColors.named_colors[screw_color_key].getDiffuseInt()

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
sys.path.append("../")
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, multiFuseObjs_wColors

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

try:
    close_CQ_Example(App, Gui)
except:
    FreeCAD.Console.PrintMessage("can't close example.")

import cadquery as cq
from math import sqrt
from Helpers import show
from collections import namedtuple
import FreeCAD, Draft, FreeCADGui
import ImportGui
sys.path.append("cq_models")
import conn_phoenix_mstb as MSTB
import conn_phoenix_mc as MC
#import conn_molex_53398 as M2
import step_license as L

series = [MSTB,MC]

def export_one_part(modul, variant, with_plug=False):
    if not variant in modul.all_params:
        FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'M.all_params', skipping." % variant)
        return

    destination_dir="Connectors_Phoenix.3dshapes"
    if with_plug:
        destination_dir="Connectors_Phoenix__with_plug.3dshapes"
    ModelName = variant
    ModelName = ModelName.replace(".","_")
    FileName = modul.all_params[variant].file_name
    Newdoc = FreeCAD.newDocument(ModelName)
    App.setActiveDocument(ModelName)
    App.ActiveDocument=App.getDocument(ModelName)
    Gui.ActiveDocument=Gui.getDocument(ModelName)
    #App.setActiveDocument(ModelName)
    #Gui.ActiveDocument=Gui.getDocument(ModelName)
    (pins, body, insert, mount_screw, plug, plug_screws) = modul.generate_part(variant, with_plug)

    color_attr = body_color + (0,)
    show(body, color_attr)

    color_attr = pins_color + (0,)
    show(pins, color_attr)

    if insert is not None:
        color_attr = insert_color + (0,)
        show(insert, color_attr)
    if mount_screw is not None:
        color_attr = screw_color + (0,)
        show(mount_screw, color_attr)
    if plug is not None:
        color_attr = body_color + (0,)
        show(plug, color_attr)

        color_attr = screw_color + (0,)
        show(plug_screws, color_attr)

    doc = FreeCAD.ActiveDocument
    doc.Label=ModelName
    objs=FreeCAD.ActiveDocument.Objects
    FreeCAD.Console.PrintMessage(objs)

    i=0
    objs[i].Label = ModelName + "__body"
    i+=1
    objs[i].Label = ModelName + "__pins"
    i+=1
    if insert is not None:
        objs[i].Label = ModelName + "__thread_insert"
        i+=1
    if mount_screw is not None:
        objs[i].Label = ModelName + "__mount_screw"
        i+=1
    if plug is not None:
        objs[i].Label = ModelName + "__plug"
        i+=1
        objs[i].Label = ModelName + "__plug_screws"
    restore_Main_Tools()

    out_dir=destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    used_color_keys = [body_color_key, pins_color_key]
    export_file_name=destination_dir+os.sep+FileName+'.wrl'

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
    if insert is not None:
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=insert_color_key,
                face_colors=None))
        used_color_keys.append(insert_color_key)
        i+=1
    if mount_screw is not None:
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=screw_color_key,
                face_colors=None))
        used_color_keys.append(screw_color_key)
        i+=1
    if plug is not None:
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=body_color_key,
                face_colors=None))
        i+=1
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=screw_color_key,
                face_colors=None))
    scale=1/2.54
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    fusion = multiFuseObjs_wColors(FreeCAD, FreeCADGui,
                     ModelName, objs, keepOriginals=True)

    exportSTEP(doc,FileName,out_dir,fusion)
    L.addLicenseToStep(out_dir+'/', FileName+".step", LIST_license,\
        STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licPreProc)

    saveFCdoc(App, Gui, doc, FileName,out_dir)


if __name__ == "__main__":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building all')
        model_to_build='*'
    else:
        if sys.argv[2] == "MC_SERIES_ALL":
            model_to_build='*'
            series = [MC]
        elif sys.argv[2] == "MSTB_SERIES_ALL":
            model_to_build='*'
            series = [MSTB]
        else:
            model_to_build=fnmatch.translate(sys.argv[2])
        if len(sys.argv) < 4:
            with_plug=False
        else:
            with_plug = sys.argv[3]=="WITH_PLUG"

    model_filter_regobj=re.compile(fnmatch.translate(model_to_build))
    for typ in series:
        for variant in typ.all_params.keys():
            if model_filter_regobj.match(variant):
                FreeCAD.Console.PrintMessage('\r\n'+variant+'\r\n')
                export_one_part(typ, variant, with_plug)

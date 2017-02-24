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

from step_license import *

licAuthor = "Rene Poeschl"
licEmail = "poeschlr@gmail.com"

LIST_license = getLicense(licAuthor, licEmail)

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

from Gui.Command import *

outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import *

checkMinRequirements()

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

try:
    close_CQ_Example(App, Gui)
except:
    say("can't close example.")

import cadquery as cq
from math import sqrt
from Helpers import show
from collections import namedtuple
import FreeCAD, Draft, FreeCADGui
import ImportGui

sys.path.append("parameters")

import conn_phoenix_mstb as MSTB
import conn_phoenix_mc as MC
#import conn_molex_53398 as M2
import step_license as L

series = [MSTB,MC]

def export_one_part(modul, variant, with_plug=False):
    if not variant in modul.all_params:
        say("Parameters for %s doesn't exist in 'M.all_params', skipping." % variant)
        return

    if with_plug:
        destination_dir = getOutputDir("Connectors_Phoenix.3dshapes")
    else:
        destination_dir = getOutputDir("Connectors_Phoenix__with_plug.3dshapes")
    
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
    say(objs)

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

    say('\r\nRunning...\r\n')

    if len(sys.argv) < 3:
        say('No variant name is given! building all')
        model_to_build='.*'
        with_plug = False
    else:
        if sys.argv[2] == "MC_SERIES_ALL":
            model_to_build='.*'
            series = [MC]
        elif sys.argv[2] == "MSTB_SERIES_ALL":
            model_to_build='.*'
            series = [MSTB]
        else:
            model_to_build=fnmatch.translate(sys.argv[2])
        if len(sys.argv) < 4:
            with_plug=False
        else:
            with_plug = sys.argv[3]=="WITH_PLUG"

    model_filter_regobj=re.compile(model_to_build)
    for typ in series:
        for variant in typ.all_params.keys():
            if model_filter_regobj.match(variant):
                say('\r\n'+variant+'\r\n')
                export_one_part(typ, variant, with_plug)

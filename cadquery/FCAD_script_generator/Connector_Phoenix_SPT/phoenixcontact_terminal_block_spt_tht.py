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
#* Joel https://github.com/myfreescalewebpage                               *
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

from __future__ import division

import sys, os
import yaml
import datetime
sys.path.append("../_tools")
import add_license

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

try:
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
except Exception as e:
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None, "Info ...", "Missing CadQuery 0.3.0 or later Module!\r\n\r\nhttps://github.com/jmwright/cadquery-freecad-module/wiki\n")

import importlib
from cqToolsExceptions import *
import cq_cad_tools
importlib.reload(cq_cad_tools)
from cq_cad_tools import multiFuseObjs_wColors, GetListOfObjects, restore_Main_Tools, exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, runGeometryCheck

try:
    close_CQ_Example(App, Gui)
except:
    FreeCAD.Console.PrintMessage("Can't close example")
    
import ImportGui

import exportPartToVRML as expVRML
import shaderColors

# License information
class LICENCE_Info():
    STR_licAuthor = "Joel"
    STR_licEmail = "myfreescalewebpage@gmail.com"
    STR_licOrgSys = ""
    STR_licPreProc = ""
    LIST_license = ["",]
    
# Function used to generate pin socket
def generate_pinpockets(params, part_params):
    
    # Create a pin pocket, the volume to be removed is extruded, later it will be cut in the body
    if params['orientation'] == 'Horizontal':
        if params['series_prefix'] == 'SPT 1.5/':
            pocket = cq.Workplane("XY", origin=(0, 0) + (0,))\
                .lineTo(1.6, 0).lineTo(1.6, 2.1).lineTo(1.25, 3.0).lineTo(0, 3.0).close()\
                .revolve(360, (0,0,0), (0,1,0))
            rpocket = cq.Workplane("XZ", origin=(0, 0) + (3.35,))\
                .rect(2.25, 2.1).extrude(-3.0)
        if params['series_prefix'] == 'SPT 2.5/':
            pocket = cq.Workplane("XY", origin=(0, 0) + (0,))\
                .lineTo(2, 0).lineTo(2, 2).lineTo(1.5, 3.3).lineTo(0, 3.3).close()\
                .revolve(360, (0,0,0), (0,1,0))
            rpocket = cq.Workplane("XZ", origin=(0, 0) + (3.85,))\
                .rect(3.7, 2.4).extrude(-3.3)
        if params['series_prefix'] == 'SPT 5/':
            pocket = cq.Workplane("XY", origin=(0, 0) + (0,))\
                .lineTo(3.25, 0).lineTo(3.25, 5.7).lineTo(2, 7.75).lineTo(0, 7.75).close()\
                .revolve(360, (0,0,0), (0,1,0))
            rpocket = cq.Workplane("XZ", origin=(0, 0) + (6.65,))\
                .rect(3.7, 3.9).extrude(-6)
    else:
        if params['series_prefix'] == 'SPT 1.5/':
            pocket = cq.Workplane("XZ", origin=(0, 0) + (params['height'],))\
                .lineTo(1.6, 0).lineTo(1.6, -2.1).lineTo(1.25, -3.0).lineTo(0, -3.0).close()\
                .revolve(360, (0,0,0), (0,1,0))
            rpocket = cq.Workplane("XY", origin=(0, 3.35) + (params['height'],))\
                .rect(2.25, 2.1).extrude(-3.0)
        if params['series_prefix'] == 'SPT 2.5/':
            pocket = cq.Workplane("XZ", origin=(0, 0) + (params['height'],))\
                .lineTo(2, 0).lineTo(2, -2).lineTo(1.5, -3.3).lineTo(0, -3.3).close()\
                .revolve(360, (0,0,0), (0,1,0))
            rpocket = cq.Workplane("XY", origin=(0, 3.85) + (params['height'],))\
                .rect(3.7, 2.4).extrude(-3.3)
        if params['series_prefix'] == 'SPT 5/':
            pocket = cq.Workplane("XZ", origin=(0, 0) + (params['height'],))\
                .lineTo(3.25, 0).lineTo(3.25, -5.7).lineTo(2, -7.75).lineTo(0, -7.75).close()\
                .revolve(360, (0,0,0), (0,1,0))
            rpocket = cq.Workplane("XY", origin=(0, 6.65) + (params['height'],))\
                .rect(3.7, 3.9).extrude(-6)
    pocket = pocket.union(rpocket)
    
    # Append to have one row of pockets
    objs = []
    for i in range(0, part_params['pins']):
        if params['orientation'] == 'Horizontal':
            if params['series_prefix'] == 'SPT 1.5/':
                objs.append(pocket.translate((-(part_params['pins']*params['pitch']['x']+params['fab']['right'])/2+params['pitch']['x']/2+i*params['pitch']['x'], -(params['fab']['bottom']-params['fab']['top'])/2, 3.8)))
            if params['series_prefix'] == 'SPT 2.5/':
                objs.append(pocket.translate((-(part_params['pins']*params['pitch']['x']+params['fab']['right'])/2+params['pitch']['x']/2+i*params['pitch']['x'], -(params['fab']['bottom']-params['fab']['top'])/2, 4.1)))
            if params['series_prefix'] == 'SPT 5/':
                objs.append(pocket.translate((-(part_params['pins']*params['pitch']['x']+params['fab']['right'])/2+params['pitch']['x']/2+i*params['pitch']['x'], -(params['fab']['bottom']-params['fab']['top'])/2, 4.8)))
        else:
            if params['series_prefix'] == 'SPT 1.5/':
                objs.append(pocket.translate((-(part_params['pins']*params['pitch']['x']+params['fab']['right'])/2+params['pitch']['x']/2+i*params['pitch']['x'], -(params['fab']['bottom']-params['fab']['top'])/2 + 3.8, 0)))
            if params['series_prefix'] == 'SPT 2.5/':
                objs.append(pocket.translate((-(part_params['pins']*params['pitch']['x']+params['fab']['right'])/2+params['pitch']['x']/2+i*params['pitch']['x'], -(params['fab']['bottom']-params['fab']['top'])/2 + 4.1, 0)))
            if params['series_prefix'] == 'SPT 5/':
                objs.append(pocket.translate((-(part_params['pins']*params['pitch']['x']+params['fab']['right'])/2+params['pitch']['x']/2+i*params['pitch']['x'], -(params['fab']['bottom']-params['fab']['top'])/2 + 3.7, 0)))
    o = objs[0]
    for i in range(1, len(objs)):
        o = o.union(objs[i])
    pockets = o

    return pockets

# Function used to generate body
def generate_body(params, part_params):

    # Create body
    body = cq.Workplane("XY").rect(params['pitch']['x']*part_params['pins']+params['fab']['right'], params['fab']['bottom']-params['fab']['top']).extrude(params['height'])\
        .faces(">Z").edges(">Y").fillet(0.5).faces(">Z").edges("<Y").fillet(0.5).faces("<Z").edges(">Y").fillet(0.5).faces("<Z").edges("<Y").fillet(0.5)
    
    # Remove pin pocket
    body = body.cut(generate_pinpockets(params, part_params))
        
    # Translate to the right position
    body = body.translate(((params['pitch']['x']*part_params['pins']+params['fab']['right'])/2+params['fab']['left'], -params['fab']['top']-(params['fab']['bottom']-params['fab']['top'])/2, 0))
    
    return body

# Function used to generate pins
def generate_pins(params, part_params):

    # Create a pin
    pin = cq.Workplane("XY", (0, 0, 0)).circle(params['pads']['drill']/2).extrude(-0.5)
    if params['series_prefix'] == 'SPT 1.5/' or params['series_prefix'] == 'SPT 2.5/':
        pin = pin.faces("<Z").workplane().center(0, 0)\
            .moveTo(0.4, 0.1).lineTo(0.1, 0.4).lineTo(-0.1, 0.4).lineTo(-0.4, 0.1).lineTo(-0.4, -0.1).lineTo(-0.1, -0.4).lineTo(0.1, -0.4).lineTo(0.4, -0.1).close()\
            .extrude(2.1)
    if params['series_prefix'] == 'SPT 5/':
        pin = pin.faces("<Z").workplane().center(0, 0)\
            .rect(1.7, 0.8)\
            .extrude(4.1)

    # Append to have two rows of pins
    objs = []
    for i in range(0, (part_params['pins']+params['pads']['increment']-1)//params['pads']['increment']):
        objs.append(pin.translate((params['pitch']['x']*params['pads']['increment']*i, 0, 0)))
    for i in range(0, part_params['pins']//params['pads']['increment']):
        objs.append(pin.translate(((params['pads']['increment']-1)*params['pitch']['x']+params['pitch']['x']*params['pads']['increment']*i, -params['pitch']['y'], 0)))
    o = objs[0]
    for i in range(1, len(objs)):
        o = o.union(objs[i])
    pins = o
    
    return pins
    
# Function used to generate package3d
def generate_package3d(params, part_params, mpn):

    # License information
    if LICENCE_Info.LIST_license[0]=="":
        LIST_license = add_license.LIST_int_license
    else:
        LIST_license = LICENCE_Info.LIST_license
    LIST_license[0] = "Copyright (C) " + datetime.datetime.now().strftime("%Y") + ", " + LICENCE_Info.STR_licAuthor
    
    # Build model name
    model_name = "PhoenixContact_{series_prefix}{pins}-{orientation_short}-{pitch}{series_sufix}_{rows}x{pins:02d}_P{pitch}_{orientation}_{mpn}".format(
        series_prefix=params['series_prefix'].replace(' ', '_').replace('/', '_'), series_sufix=(params['series_sufix'] if params['series_sufix'] is not None else ''), rows=part_params['rows'], pins=part_params['pins'], pitch=params['pitch']['x'], orientation=params['orientation'], orientation_short=params['orientation'][:1], mpn=mpn)
    FreeCAD.Console.PrintMessage('\r\nGenerate: ' + model_name + '\r\n')
    
    # Create new document
    doc = FreeCAD.newDocument("doc")
    App.setActiveDocument("doc")
    App.ActiveDocument = App.getDocument("doc")
    Gui.ActiveDocument = Gui.getDocument("doc")

    # Generate body
    body_color_key = "green body"
    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    body = generate_body(params, part_params)
    show(body, body_color + (0,))
    
    # Generate pins
    pins_color_key = "metal grey pins"
    pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
    pins = generate_pins(params, part_params)
    show(pins, pins_color + (0,))
    
    # Finalize
    doc = FreeCAD.ActiveDocument
    objs = GetListOfObjects(FreeCAD, doc)
    restore_Main_Tools()
    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    material_substitutions={
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pins_color_key
    }
    expVRML.say(material_substitutions)

    # Create output directory
    output_dir = 'Connector_Phoenix_SPT.3dshapes/'
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    filename =  '{output_dir:s}{model_name:s}.wrl'.format(output_dir=output_dir, model_name=model_name)
    
    # Export wrl file
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects, 1/2.54)
    expVRML.writeVRMLFile(colored_meshes, filename, used_color_keys, LIST_license)

    # Export step file
    exportSTEP(doc, model_name, output_dir, objs[0])
    add_license.addLicenseToStep(output_dir, '{model_name}.step'.format(
        model_name=model_name),
        LIST_license, LICENCE_Info.STR_licAuthor, LICENCE_Info.STR_licEmail, LICENCE_Info.STR_licOrgSys, LICENCE_Info.STR_licPreProc)

    # Force recompute
    FreeCAD.activeDocument().recompute()

    # Save FCStd document
    saveFCdoc(App, Gui, doc, model_name, output_dir)

    # Close document
    doc = FreeCAD.ActiveDocument
    FreeCAD.closeDocument(doc.Name)

if __name__ == "__main__":

    # Load yaml file for this library
    with open('./phoenixcontact_terminal_block_spt_tht.yaml', 'r') as params_stream:
        try:
            params = yaml.safe_load(params_stream)
        except yaml.YAMLError as exc:
            print(exc)

    # Create each part
    for series in params:
        for mpn in params[series]['parts']:
            generate_package3d(params[series], params[series]['parts'][mpn], mpn)

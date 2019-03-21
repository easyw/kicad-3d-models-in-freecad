from collections import namedtuple
import sys, os
from sys import argv
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
import argparse
import yaml
import logging
import add_license as L
logging.getLogger('builder').addHandler(logging.NullHandler())
import add_license as Lic

import cq_cad_tools
reload(cq_cad_tools)

from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
    exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, Color_Objects, \
    checkRequirements

import cadquery as cq
from Helpers import show

# Licence information of the generated models.
#################################################################################################
STR_licAuthor = "kicad StepUp"
STR_licEmail = "ksu"
STR_licOrgSys = "kicad StepUp"
STR_licPreProc = "OCC"
STR_licOrg = "FreeCAD"   

LIST_license = ["",]
#################################################################################################

def MakeConnector(name, params):

    model_name = name
    full_model_name = name + "-6-0-{}{:02d}_1x{}_P2.50mm_Vertical".format(params["pins"], params["pins"], params["pins"])
    expVRML.say(model_name)
    expVRML.say(params)

    out_dir = "../../FCAD_script_generator/_3Dmodels/Connector_Stocko.3dshapes"

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    body_color_key = "grey body"
    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    pin_union_color_key = "metal silver"
    pin_union_color = shaderColors.named_colors[pin_union_color_key].getDiffuseFloat()

    newdoc = App.newDocument(model_name)
    App.setActiveDocument(model_name)
    App.ActiveDocument=App.getDocument(model_name)
    Gui.ActiveDocument=Gui.getDocument(model_name)

    body = cq.Workplane("XY").move(-params["outline_x"], 0).box((params["pitch"] * (params["pins"] - 1)) + 2 * params["outline_x"], \
    params["base_w"], params["base_h"], centered = (False,True,False))
    body = body.faces(">Z") \
    .workplane().rect(params["pitch"] * (params["pins"] - 1) + 2 * params["outline_x"] - params["lr_sides_t"], \
    params["base_w"] - params["tb_sides_t"]) \
    .cutBlind(-params["depth"]) \
    .faces(">Z") \
    .edges("not(<X or >X or <Y or >Y)") \
    .chamfer(0.7)
    body = body.edges("|Z and >X").fillet(0.5)
    body = body.edges("|Z and <X").fillet(0.5)
    body = body.faces(">Z").workplane().center(0, -params["base_w"] / 2 + params["base_cutout"] /2).rect( \
    params["pitch"] * (params["pins"] - 1) + 2 * (params["outline_x"] - params["leaf"]), \
    params["base_cutout"]) \
    .cutThruAll()
    if params["top_cutout"]:
        body = body.faces(">Y").workplane().center(0, 6.5).rect(params["t_cutout_w"], params["t_cutout_h"] ).cutThruAll()
    for x in range(params["pins"]):
        temp = (params["b_cutout_long_w"] - params["b_cutout_short_w"]) / 2
        body = body.faces(">Y").workplane(centerOption='CenterOfBoundBox').center( \
            ((params["pitch"] * (params["pins"] - 1) + 2 * params["outline_x"]) / 2) - params["outline_x"] - (params["b_cutout_long_w"] / 2) - x*params["pitch"], \
            -7).lineTo(params["b_cutout_long_w"], 0).lineTo(params["b_cutout_long_w"] - temp, params["b_cutout_h"]).lineTo(temp, params["b_cutout_h"]).close().cutThruAll()

    total_pin_length = params["pin"]["length_above_board"] + params["pin"]["length_below_board"]
    pin = cq.Workplane("XY").workplane(offset=-params["pin"]["length_below_board"]).box(params["pin"]["width"], \
             params["pin"]["width"], total_pin_length, centered = (True,True,False))

    pin = pin.edges("#Z").chamfer(params["pin"]["end_chamfer"])
    pins_union = cq.Workplane("XY").workplane(offset=-params["pin"]["length_below_board"])

    for x in range(params["pins"]):
        pins_union = pins_union.union(pin.translate((x*params["pitch"], 0, 0)))

    show(body)
    show(pins_union)

    doc = FreeCAD.ActiveDocument
    objs = GetListOfObjects(FreeCAD, doc)

    Color_Objects(Gui, objs[0], body_color)
    Color_Objects(Gui, objs[1], pin_union_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]

    material_substitutions={
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pin_union_color_key,
    }
    expVRML.say(material_substitutions)

    FuseObjs_wColors(FreeCAD, FreeCADGui,
        doc.Name, objs[0].Name, objs[1].Name)

    doc.Label=model_name
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=model_name
    restore_Main_Tools()

    doc.Label = model_name

    #save the STEP file
    exportSTEP(doc, full_model_name, out_dir)
    global LIST_license
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', full_model_name+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,ModelName,scale,out_dir)
    objs=GetListOfObjects(FreeCAD, doc)
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir+'/'+full_model_name+'.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

if __name__ == "__main__" or __name__ == "main_generator":

    try:
        with open('cq_parameters.yaml', 'r') as f:
            raw_params = yaml.load(f)
    except yaml.YAMLError as exc:
        print(exc)

    for part in raw_params:
        if part != "general":
            params = raw_params[part]
            params.update(raw_params["general"])
            MakeConnector(part, params)

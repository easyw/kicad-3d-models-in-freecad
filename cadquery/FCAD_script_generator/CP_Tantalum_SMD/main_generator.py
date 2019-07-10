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
## e.g. c:\freecad\bin\freecad main_generator.py CP_Tantalum_Case-B_EIA-3528-21

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

__title__ = "make Tantalum Caps 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make Tantalum Caps 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.2 10/02/2017"

save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'

# thanks to Frank Severinsen Shack for including vrml materials

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import traceback

import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "yellow body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
mark_color_key = "orange body"
mark_color = shaderColors.named_colors[mark_color_key].getDiffuseFloat()


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

# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements
# Sphinx workaround #1
try:
    QtGui
except NameError:
    QtGui = None
#

try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery
    cq = cadquery
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

# Sphinx workaround #2
try:
    cq
    checkRequirements(cq)
except NameError:
    cq = None
#

def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)


# Import cad_tools
import cq_cad_tools
# Reload tools
reload_lib(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements, runGeometryCheck

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print ("CQ 030 doesn't open example file")

import cq_parameters  # modules parameters
from cq_parameters import *
from cqToolsExceptions import *

def make_tantalum(params):

    L  = params.L
    W  = params.W
    H   = params.H
    F = params.F
    S = params.S
    B  = params.B
    P = params.P
    R = params.R
    T = params.T
    G = params.G
    E = params.E
    pml = params.pml
    #dest_dir_pref = params.dest_dir_prefix

    Lb = L - 2.*T        # body lenght
    ppH = (H * 0.45)    # pivot point height

    ma_rad=radians(ma_deg)
    dtop = (H-ppH) * tan(ma_rad)
    dbot = (ppH-T) * tan(ma_rad)

    body_base = cq.Workplane(cq.Plane.XY()).workplane(offset=0).rect(E, G). \
                workplane(offset=T).rect(E,G). \
                loft(ruled=True)

    body = cq.Workplane(cq.Plane.XY()).workplane(offset=T).rect(W-dbot, Lb-dbot). \
               workplane(offset=ppH-T).rect(W,Lb). \
               workplane(offset=H-ppH).rect(W-dtop, Lb-dtop). \
               loft(ruled=True)

    if B!=0:
        BS = cq.selectors.BoxSelector
        body = body.edges(BS((-(W-2.*dtop)/2, (Lb-2.*dtop)/2., H-0.2), ((W+2.*dtop)/2, (Lb+2.*dtop)/2., H+0.2))).chamfer(B)

    body=body.union(body_base)
    #sleep
    pinmark = cq.Workplane(cq.Plane.XY()).workplane(offset=H-T*0.01).rect(W-dtop-dtop, pml). \
                workplane(offset=T*0.01).rect(W-dtop-dtop, pml). \
                loft(ruled=True)

    #translate the object
    pinmark=pinmark.translate((0,Lb/2.-B-pml/2.-dtop/2.-dtop/2.,0)).rotate((0,0,0), (0,1,0), 0)
    # Create a pin object at the center of top side.
        #threePointArc((L+K/sqrt(2), b/2-K*(1-1/sqrt(2))),
        #              (L+K, b/2-K)). \
    bpin1 = cq.Workplane("XY"). \
        moveTo(0,Lb/2.-S). \
        lineTo(0,Lb/2.). \
        lineTo(F,Lb/2.). \
        lineTo(F,Lb/2.-S). \
        close().extrude(T+0.01*T)
    bpin1=bpin1.translate((-F/2.,0,0))
    bpin=bpin1.rotate((0,(Lb/2.-S)/2.,F/2.), (0,0,1), 180).translate((0,-Lb/2.+S,0))

    delta=0.01
    hpin=ppH-delta*ppH
    bpin2 = cq.Workplane("XY"). \
        moveTo(0,Lb/2.). \
        lineTo(0,Lb/2.+T). \
        lineTo(F,Lb/2.+T). \
        lineTo(F,Lb/2.). \
        close().extrude(hpin)
    bpin2=bpin2.translate((-F/2.,0,0))
    BS = cq.selectors.BoxSelector
    bpin2 = bpin2.edges(BS((0-delta,L/2.-delta,hpin-delta), (0+delta,L/2.+delta,hpin+delta))).fillet(T*2./3.)
    bpin2 = bpin2.edges(BS((0-delta,L/2.-delta,0-delta), (0+delta,L/2.+delta,0+delta))).fillet(T*2./3.)
    bpinv=bpin2.rotate((0,(T)/2.,F/2.), (0,0,1), 180).translate((0,-T,0))
    #show (bpinv)
    if P!=0:
        anode = cq.Workplane("XY"). \
        moveTo(0,Lb/2.). \
        lineTo(0,Lb/2.+T). \
        lineTo(R,Lb/2.+T). \
        lineTo(R,Lb/2.). \
        close().extrude(hpin-P).translate((-R/2.,0,P))
        #show (anode)
        bpin2 = bpin2.cut(anode)
    #show (bpin2)
    #show (bpinv)
    #show(bpin1)
    #show (bpin)

    merged_pins=bpin
    merged_pins=merged_pins.union(bpin1)
    merged_pins=merged_pins.union(bpin2)
    merged_pins=merged_pins.union(bpinv)
    pins = merged_pins

    #show(pins)
    #sleep

    return (body, pins, pinmark)

#import step_license as L
import add_license as Lic

show_all = False

def generateOneModel(part_params, log):
    place_pinMark=True ##default =True used to exclude pin mark to build sot23-3; sot23-5; sc70 (asimmetrical pins, no pinmark)

    FreeCAD.Console.PrintMessage(
        '\n\n##############  ' +
        part_params['code_metric'] +
        '  ###############\n')
    dim_params = part_params['param_nominal'] if use_nominal_size else part_params['param_max']
    if dim_params == None:
        if show_all:
            if use_nominal_size:
                dim_params = part_params['param_max']
            else:
                dim_params = part_params['param_nominal']
    if dim_params == None:
        FreeCAD.Console.PrintMessage('No params found for current variant. Skipped\n')
        return

    ModelName = model_name_format_str.format(
      prefix=model_name_prefix,
      code_metric=part_params['code_metric'],
      code_letter=part_params['code_letter'],
      old_name=part_params['modelName_old'],
      maui_name=part_params['modelName_maui']
    )
    CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedModelName)
    App.setActiveDocument(CheckedModelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
    body, pins, mark = make_tantalum(dim_params)

    show(body)
    show(pins)
    show(mark)
    
    doc = FreeCAD.ActiveDocument
    objs = GetListOfObjects(FreeCAD, doc)

    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],pins_color)
    Color_Objects(Gui,objs[2],mark_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
    material_substitutions={
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pins_color_key,
        col_mark[:-1]:mark_color_key
    }
    #expVRML.say(material_substitutions)
    del objs
    objs=GetListOfObjects(FreeCAD, doc)
    if (color_pin_mark==True) and (place_pinMark==True):
        CutObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[2].Name)
    else:
        #removing pinMark
        App.getDocument(doc.Name).removeObject(objs[2].Name)
    del objs
    objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
    doc.Label = CheckedModelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = CheckedModelName
    restore_Main_Tools()
    #rotate if required
    if (rotation!=0):
        rot = rotation
        z_RotateObject(doc, rot)
    #out_dir=destination_dir+all_params[variant].dest_dir_prefix+'/'
    script_dir=os.path.dirname(os.path.realpath(__file__))
    #models_dir=script_dir+"/../_3Dmodels"
    expVRML.say(models_dir)
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    #out_dir="./generated_qfp/"
    # export STEP model
    exportSTEP(doc, ModelName, out_dir)
    global LIST_license
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', ModelName+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,ModelName,scale,out_dir)
    objs=GetListOfObjects(FreeCAD, doc)
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir+os.sep+ModelName+'.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    saveFCdoc(App, Gui, doc, ModelName, out_dir)

    #FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.activeDocument().activeView().viewAxometric()

    if save_memory == True or check_Model==True:
        doc=FreeCAD.ActiveDocument
        FreeCAD.closeDocument(doc.Name)

    if check_Model==True:
        step_path = out_dir + '/' + ModelName + ".step"
        runGeometryCheck(App, Gui, step_path,
            log, ModelName, save_memory=save_memory)
            

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

# maui     run()
    color_pin_mark=True
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building EIA-3528-21')
        model_to_build='EIA-3528-21'
    else:
        model_to_build=sys.argv[2]
        if len(sys.argv)==4:
            FreeCAD.Console.PrintMessage(sys.argv[3]+'\r\n')
            if (sys.argv[3].find('no-pinmark-color')!=-1):
                color_pin_mark=False
            else:
                color_pin_mark=True
            if (sys.argv[3] == 'all'):
                show_all = True
    if model_to_build == "all":
        show_all = True
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    with open(check_log_file, 'w') as log:
        log.write('# Check report for Molex 3d model genration\n')
        for variant in variants:
            part_params = all_params[variant]
            try:
                generateOneModel(part_params, log)
            except GeometryError as e:
                e.print_errors(stop_on_first_error)
                if stop_on_first_error:
                    break
            except FreeCADVersionError as e:
                FreeCAD.Console.PrintError(e)
                break
#            else:
#                FreeCAD.Console.PrintMessage('generateOneModel 11 \n')
#                traceback.print_exc()
#                raise


    FreeCAD.Console.PrintMessage("\nDone\n")

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

__title__ = "make Smx Diodes 3D models"
__author__ = "maurice and hyOzd and Shack"
__Comment__ = 'make Diode Smx 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.0 18/03/2017"

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

body_color_key = "black body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
mark_color_key = "light brown label"
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

#all_params= all_params_tantalum
all_params= kicad_naming_params_tantalum

def make_Smx(params):

    L  = params.L
    W  = params.W
    H   = params.H
    F = params.F
    S = params.S
    T = params.T
    G = params.G
    pml = params.pml
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix

    Lb = L - 2.*T        # body lenght
    ppH = (H * 0.45)    # pivot point height
    
    ma_rad=radians(ma_deg)
    dtop = (H-ppH) * tan(ma_rad)
    dbot = (ppH-T) * tan(ma_rad)
    dbump = ppH * tan(ma_rad)
    
    body_base = cq.Workplane(cq.Plane.XY()).workplane(offset=0).rect(W-dbump, G). \
                workplane(offset=T).rect(W-dbot,G). \
                loft(ruled=True)

    body = cq.Workplane(cq.Plane.XY()).workplane(offset=T).rect(W-dbot, Lb-dbot). \
               workplane(offset=ppH-T).rect(W,Lb). \
               workplane(offset=H-ppH).rect(W-dtop, Lb-dtop). \
               loft(ruled=True)

    body=body.union(body_base)
    #sleep
    pinmark = cq.Workplane(cq.Plane.XY()).workplane(offset=H-T*0.01).rect(W-dtop-dtop, pml). \
                workplane(offset=T*0.01).rect(W-dtop-dtop, pml). \
                loft(ruled=True)

    #translate the object  
    pinmark=pinmark.translate((0,Lb/2.-pml/2.-dtop/2.-dtop/2.,0)).rotate((0,0,0), (0,1,0), 0)    
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
        FreeCAD.Console.PrintMessage('No variant name is given! building D_SMA_Standard')
        model_to_build='D_SMA_Standard'
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
    else:
        variants = [model_to_build]

    for variant in variants:
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
        body, pins, mark = make_Smx(all_params[variant])

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
        expVRML.say(material_substitutions)
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
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
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
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox
        #FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()
# -*- coding: utf8 -*-
#!/usr/bin/python
# This is derived from a cadquery script to generate all pin header models in X3D format.
# It takes a bit long to run! It can be run from cadquery freecad
# module as well.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd

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

__title__ = "make pin header 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make pin header 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.4.2 26/02/2017"


#sleep ### NB il modello presenta errori di geometria

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, cos, sin, radians, sqrt
from collections import namedtuple
global save_memory
save_memory = False #reducing memory consuming for all generation params
global closeformerDoc
closeformerDoc = False
global formerDOC

#from cq_cad_tools import say, sayw, saye

import sys, os
from sys import argv
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "black body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "gold pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
#marking_color_key = "light brown label"
#marking_color = shaderColors.named_colors[marking_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui

import logging
logging.getLogger('builder').addHandler(logging.NullHandler())
#logger = logging.getLogger('builder')
#logging.info("Begin")

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


# from export_x3d import exportX3D, Mesh
try:
    # Gui.SendMsgToActiveView("Run")
    # cq Gui
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

all_params = kicad_naming_params_pin_headers

#Make a single plastic base block (chamfered if required)
def MakeBaseBlock(params):
    block = cq.Workplane("XY").rect(params.p, params.w).extrude(params.h)
    #chamfer
    if params.c > 0:
        block = block.edges("|Z").chamfer(params.c)
        #move the base to the 'middle'
    if params.rows > 1:
        offset = params.p * (params.rows - 1) / 2.0
        block = block.translate((0,offset,0))
    if params.type == 'Angled':
        block = block.rotate((0, 0, 0),(1, 0, 0), 90).translate((0,params.hb+params.h+(params.rows-1)*params.p,params.h/2))
    return block
    
#Make the plastic base
#Note - making the 'blocks' separately and then making a UNION of the blocks seems to be the best way to get them to merge
#make the plastic base
def MakeBase(n, params, pinarray):
    global basecount
    global base
    if n == pinarray[0]:
        base = MakeBaseBlock(params)
        basecount = 1
    for i in range(basecount,n):
        block = MakeBaseBlock(params).translate((i*params.p,0,0))
        base = base.union(block)
    basecount = n
    return base
    
#make a single pin
def MakePin(n, row, params):
    row_offset = row*params.p
    if params.type == 'Straight':
        single_pin = cq.Workplane("XY").workplane(offset=-params.ph+params.hb).rect(params.pw,params.pw).extrude(params.ph+params.pa).translate((0,row_offset,0))
    
        #chamfer each end of the pin if required
        if params.pc > 0:
            single_pin = single_pin.faces("<Z").chamfer(params.pc)
            single_pin = single_pin.faces(">Z").chamfer(params.pc)
        
    elif params.type == 'Angled':
        R1 = params.pw/2 # pin upper corner inner radius
        R1_o = R1+params.pw # pin upper corner, outer radius

        single_pin = cq.Workplane("YZ", (0,0,0,)). \
        moveTo(params.pa+params.hb+row_offset, (params.w/params.rows-params.pw)/2). \
        line(-params.pa-params.hb-row_offset+R1+params.pw/2, 0). \
        threePointArc((params.pw/sqrt(2), (params.w/params.rows-params.pw)/2-R1*(1-1/sqrt(2))),
                      ((params.pw/2, (params.w/params.rows-params.pw)/2-R1))). \
        line(0, -(params.w/params.rows-params.pw)/2-R1-params.ph-row_offset). \
        line(-params.pw,0). \
        line(0, ((params.w/params.rows)-params.pw)/2+R1+params.ph+row_offset). \
        threePointArc((-(R1-params.pw/2)/sqrt(2), (params.w/params.rows+params.pw)/2-R1_o*(1-1/sqrt(2))),
                      (R1_o-params.pw/2, (params.w/params.rows+params.pw)/2)). \
        line(params.pa+params.hb-R1_o+params.pw/2+row_offset, 0).close().extrude(params.pw).translate((-params.pw/2,params.p*(params.rows-1-row),row_offset))
        
        if params.pc > 0:
            single_pin = single_pin.faces("<Z").chamfer(params.pc)
            single_pin = single_pin.faces(">Y").chamfer(params.pc)
    return single_pin
    
#make all the pinarray
def MakePinRow(n, ROW, params, pinarray):
    global pincount
    global pin
    global pinset
    #make some pins
    if n == pinarray[0]:
        pinset = MakePin(1, 0, params)
        if params.rows > 1:
            for i in range(1,params.rows):
                pinset = pinset.union(MakePin(1, i, params))
        pin = pinset
        pincount = 0
    
    for i in range(pincount,n):
        pin = pin.union(pinset.translate((params.p * i,0,0)))
    pincount = n
    return pin

#generate a name for the pin header
def HeaderName(n, params):
    return "Pin_Header_{}_{r:01}x{n:02}_Pitch{p:.2f}mm".format(params.type,r=params.rows,n=n,p=params.p)
    
#make a pin header using supplied parameters, n pins in each row
def MakeHeader(n, params, pinarray):
    global formerDOC
    global LIST_license
    name = HeaderName(n,params)
    
    # destination_dir="/Pin_Headers"

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
    script_dir=os.path.dirname(os.path.realpath(__file__))
    #models_dir=script_dir+"/../_3Dmodels"
    expVRML.say(models_dir)
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    #having a period '.' character in the model name REALLY messes with things.
    docname = name.replace(".","")
   
    newdoc = App.newDocument(docname)
    App.setActiveDocument(docname)
    App.ActiveDocument=App.getDocument(docname)
    Gui.ActiveDocument=Gui.getDocument(docname)
    
    pins_output = MakePinRow(n,0,params,pinarray)
    
    #duplicate pin rows

    base_output = MakeBase(n,params,pinarray)

    show(base_output)
    show(pins_output)

    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)
    
    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],pins_color)
    #Color_Objects(Gui,objs[2],marking_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    #col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
    material_substitutions={
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pins_color_key,
        #col_mark[:-1]:marking_color_key
    }
    expVRML.say(material_substitutions)

    ##assign some colors
    #base_color = (50,50,50)
    #pins_color = (225,175,0)
    #
    #show(base,base_color+(0,))
    #show(pins,pins_color+(0,))
    
    #objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui,
                   doc.Name, objs[0].Name, objs[1].Name)
    doc.Label=docname
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=docname
    restore_Main_Tools()

    if (params.rot !=0):
        z_RotateObject(doc, params.rot)
    
    #out_dir = models_dir+"/generated_pinheaders"
    
    doc.Label = docname
    
    #save the STEP file
    exportSTEP(doc, name, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', name+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)
    
    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,ModelName,scale,out_dir)
    objs=GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir+os.sep+name+'.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    #save the VRML file
    #scale=0.3937001
    #exportVRML(doc,name,scale,out_dir)
    
    if save_memory == False:
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()
    
    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, name,out_dir)
    Gui.activateWorkbench("StartWorkbench")
    if save_memory == True:
        App.setActiveDocument(docname)
        App.ActiveDocument=App.getDocument(docname)
        Gui.ActiveDocument=Gui.getDocument(docname)
        if n != pinarray[0]:
            #FreeCAD.closeDocument(formerDOC)
            App.closeDocument(formerDOC)
        FreeCADGui.updateGui()
        formerDOC = docname
    Gui.activateWorkbench("CadQueryWorkbench")
    return 0
    
#import step_license as L
import add_license as Lic

if __name__ == "__main__" or __name__ == "main_generator":
    
    from sys import argv
    models = []
    pinrange = []
    
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building 254single')
        model_to_build = "254single"
    else:
        model_to_build = sys.argv[2]
        
    if model_to_build == 'all':
        models = [all_params[model_to_build] for model_to_build in all_params.keys()]
        pinrange = range(1,41)
        save_memory = True
    else:
        models = [all_params[i] for i in model_to_build.split(',') if i in all_params.keys()]#separate model types with comma
        
    if len(sys.argv) < 4:
        FreeCAD.Console.PrintMessage("No pins specified, building 254single 1")
        p = "1"
    else:
        p = sys.argv[3].strip()
        
    #comma separarated pin numberings
    if ',' in p:
        try:
            pinrange = map(int,p.split(','))
        except:
            FreeCAD.Console.PrintMessage("Pin argument '",p,"' is invalid ,")
            pinrange = []
    
    #range of pins x-y
    elif '-' in p and len(p.split('-')) == 2:
        ps = p.split('-')
        
        try:
            p1, p2 = int(ps[0]),int(ps[1])
            pinrange = range(p1,p2+1)
        except:
            FreeCAD.Console.PrintMessage("Pin argument '",p,"' is invalid -")
            pinrange = []
        save_memory = True
            
    #otherwise try for a single pin
    else:
        try:
            pin_number = int(p)
            pinrange = [pin]
        except:
            FreeCAD.Console.PrintMessage("Pin argument '",p,"' is isnvalid")
            pinrange = []
    
    #make all the seleted models
    pincount = 0
    basecount = 0

    formerDOC = ""

    for model in models:
        for pin_number in pinrange:
            MakeHeader(pin_number,model,pinrange)

# when run from freecad-cadquery
if __name__ == "temp.module":
    pass
    #ModelName="mypin"
    ## Newdoc = FreeCAD.newDocument(ModelName)
    ## App.setActiveDocument(ModelName)
    ## Gui.ActiveDocument=Gui.getDocument(ModelName)
    ##
    ## case, pins = make_pinheader(5)
    ##
    ## show(case, (60,60,60,0))
    ## show(pins)



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
 CutObjs_wColors, checkRequirements, closeCurrentDoc


# from export_x3d import exportX3D, Mesh
try:
    # Gui.SendMsgToActiveView("Run")
    # cq Gui
    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except:
    try:
        from CadQuery.Gui.Command import *
        Gui.activateWorkbench("CadQueryWorkbench")
        import cadquery as cq
        from Helpers import show
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

#generate a name for the pin header
def HeaderName(n, params):
	if params.rows == 1:
		return "Pin_Header_Straight_{r:01}x{n:02}_Pitch{p:.2f}mm_SMD_{type}".format(r=params.rows,n=n,p=params.p,type=params.type)
	else:
		return "Pin_Header_Straight_{r:01}x{n:02}_Pitch{p:.2f}mm_SMD".format(r=params.rows,n=n,p=params.p)
    
#make a pin header using supplied parameters, n pins in each row
def MakeHeader(n, params):
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
    
    baseblock = cq.Workplane("XY").rect(params.p, params.w).extrude(params.h).edges("|Z").chamfer(params.p/10).translate((0,0,params.hb))
    base = baseblock
    for blocks in range(1,n):
    	baseblock = baseblock.translate((params.p,0,0))
    	base = base.union(baseblock)
    	    #move the base to the 'middle'
    if params.rows > 1:
        offset = params.p * (params.rows - 1) / 2.0
        base = base.translate((0,offset,0))

    Inner_point = params.pw/sqrt(2)
    Outer_point = (params.pw*2)/sqrt(2)
    single_pin = cq.Workplane("YZ", (0,0,0,)). \
    moveTo(params.pw/2,params.pa).line(0,-(params.pa-2*params.pw)).threePointArc((-(params.pw*1.5)+Outer_point,params.pw*2-Outer_point),(-(params.pw*1.5), 0)). \
    line(-(params.ph-2*params.pw),0).line(0,params.pw).line((params.ph-2*params.pw),0).threePointArc((-(params.pw*1.5)+Inner_point,params.pw*2-Inner_point), (-(params.pw/2), params.pw*2)). \
    line(0,params.pa-2*params.pw).close().extrude(params.pw).translate((-params.pw/2,0,0))
    single_pin = single_pin.faces(">Z").chamfer(params.pw/4)
    single_pin = single_pin.faces("<Y").chamfer(params.pw/4)
    pins = []
    if params.type:
    	if params.type == 'Pin1Left':
    		single_pin = single_pin.rotate((0,0,0), (0,0,1), 180)
    	for pincount in range(0,n):
    		single_pin = single_pin.rotate((0,0,0), (0,0,1), 180)
    		pin = single_pin.translate((params.p*pincount,0,0))
    		pins.append(pin)
    else:
    	for pincount in range(0,n):
    		pin = single_pin.translate((params.p*pincount,0,0))
    		pins.append(pin)
    	single_pin = single_pin.rotate((0,0,0), (0,0,1), 180)
    	for pincount in range(0,n):
    		pin = single_pin.translate((params.p*pincount,params.p,0))
    		pins.append(pin)

    merged_pins = pins[0]
    for p in pins[1:]:
  		merged_pins = merged_pins.union(p)
    pins = merged_pins
    if params.rows > 1:
    	row_offset = -params.p/2
    else:
    	row_offset = 0
    pins = pins.translate((-params.p*(n-1)/2,row_offset,0))
    base = base.translate((-params.p*(n-1)/2,row_offset,0))

    show(base)
    show(pins)

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
    if save_memory == True:
        closeCurrentDoc(docname)
    return 0
    
#import step_license as L
import add_license as Lic

if __name__ == "__main__" or __name__ == "main_generator":
    
    from sys import argv
    models = []
    pinrange = []

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building 254single')
        model_to_build = "Pin_Header_Straight_1xyy_Pitch2.54mm"
        pinrange = [1]
    else:
        model_to_build = sys.argv[2]
    if model_to_build == "all":
       	#expVRML.sayerr("'all' is not supported for this families\nuse 'allSOIC' or 'allSSOP' or 'allSOT' or 'allQFP' or 'allTSSOP' instead")
       	models = all_params.keys()
       	
    else:
    	models = [model_to_build]
    save_memory=True
    print "\n m"
    print model_to_build
    print pinrange

    for model in models:
    	pinrange = range(all_params[model].pins[0],all_params[model].pins[1]+1)
        for pin_number in pinrange:
            MakeHeader(pin_number,all_params[model])

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



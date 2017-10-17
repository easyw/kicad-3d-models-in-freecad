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

body_color_key = "blue body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
ceramic_color_key = "white body"
ceramic_color = shaderColors.named_colors[ceramic_color_key].getDiffuseFloat()
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

all_params = kicad_naming_params_resistors_tht

# make a cylindrical style resistor based on parameters
def MakeResistor(params):
    if (params.orient == 'v'):
        if (params.shape == 'din'):
            body = cq.Workplane("XY").circle(params.d/2*0.9).extrude(params.l)
            body = body.union(cq.Workplane("XY").circle(params.d/2).extrude(params.l/4))
            body = body.union(cq.Workplane("XY").workplane(offset=params.l*3/4).circle(params.d/2).extrude(params.l/4))
        elif (params.shape == 'power'):
            body = cq.Workplane("XY").rect(params.d, params.w).extrude(params.l)
        body = body.translate((0,0,1.0))
    else:
        # horizontal cylinder
        if (params.shape == 'din'):
            body = cq.Workplane("YZ").circle(params.d/2*0.9).extrude(params.l)
            body = body.union(cq.Workplane("YZ").circle(params.d/2).extrude(params.l/4))
            body = body.union(cq.Workplane("YZ").workplane(offset=params.l*3/4).circle(params.d/2).extrude(params.l/4))
        elif (params.shape == 'power') or (params.shape == 'box') or (params.shape == 'radial') or (params.shape == 'shunt'):
            body = cq.Workplane("YZ").rect(params.w, params.d).extrude(params.l)
        # sit on board, center between pads
        body = body.translate(((params.px-params.l)/2,0,params.d/2))
    return body
    
# make a bent resistor pin
def MakeResistorPin(params):
    
    zbelow = -3.0
    minimumstraight = 1.0
    
    # bent pin
    if (params.shape == "din") or (params.shape=="power") or (params.shape=="shunt"):
        r = params.pd*1.5
        arco = (1-sqrt(2)/2)*r
        if (params.orient == 'v'):
            # vertical
            h = params.l + 2*minimumstraight + r
        else:
            # horizontal
            h = params.d / 2
        path = cq.Workplane("XZ").lineTo(0,h-r-zbelow).threePointArc((arco,h-arco-zbelow),(r,h-zbelow)).lineTo(params.px-r,h-zbelow).threePointArc((params.px-arco,h-arco-zbelow),(params.px,h-r-zbelow)).lineTo(params.px,0)
        pin = cq.Workplane("XY").circle(params.pd/2).sweep(path).translate((0,0,zbelow))
    # simple pins using px/py
    elif (params.shape == "box") or (params.shape == "radial"):
        pin = cq.Workplane("XY").circle(params.pd/2).extrude(zbelow)
        pin = pin.union(pin.translate((params.px,params.py,0)))
    
    # add extra pins for shunt package using py as pitch
    if (params.shape == "shunt"):
        pin = pin.union(cq.Workplane("XY").circle(params.pd/2).extrude(zbelow).translate(((params.px-params.py)/2,0,0)))
        pin = pin.union(cq.Workplane("XY").circle(params.pd/2).extrude(zbelow).translate(((params.px+params.py)/2,0,0)))

    return pin

#generate a name for the part
def PartName(params, n=0):
    # even though we use the names as keys, this generates the name programatically
    fstring = "R_Axial_"
    if (params.shape == 'din'):
        if (params.d == 1.6):
            fstring += "DIN0204_"
        elif (params.d == 2.5):
            fstring += "DIN0207_"
        elif (params.d == 3.2):
            fstring += "DIN0309_"
        elif (params.d == 3.6):
            fstring += "DIN0411_"
        elif (params.d == 4.5):
            fstring += "DIN0414_"
        elif (params.d == 5.0):
            fstring += "DIN0516_"
        elif (params.d == 5.7):
            fstring += "DIN0614_"            
        elif (params.d == 6.0):
            fstring += "DIN0617_"
        elif (params.d == 5.7) and (params.l == 18.00):
            fstring += "DIN0918_"
        elif (params.d == 5.7) and (params.l == 20.00):    
            fstring += "RDIN00922_"
        fstring += "L{0:.1f}mm_D{1:.1f}mm_P{2:.2f}mm_"
        if (params.orient == 'v'):
            fstring += "Vertical"
        else:
            fstring += "Horizontal"
    elif (params.shape == 'power'):
        fstring += "Power_L{0:.1f}mm_W{1:.1f}mm_P{2:.2f}mm"
        if (params.orient == 'v'):
            fstring += "_Vertical"
    
    outstring = fstring.format(params.l, params.d, params.px)
    print(outstring)
    return outstring

    
#make a part using supplied parameters
def MakePart(params, n=0):
    global formerDOC
    global LIST_license
    name = PartName(params, n)

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
    expVRML.say(models_dir)
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    #having a period '.' character in the model name REALLY messes with things. also '-'
    docname = name.replace(".","").replace("-","_")
   
    newdoc = App.newDocument(docname)
    App.setActiveDocument(docname)
    App.ActiveDocument=App.getDocument(docname)
    Gui.ActiveDocument=Gui.getDocument(docname)
    
    FreeCAD.Console.PrintMessage(params)
    pins_output = MakeResistorPin(params)
    base_output = MakeResistor(params)
    
    show(base_output)
    show(pins_output)

    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)
    
    if (params.shape == "power") or (params.shape == "box") or (params.shape == "radial"):
        Color_Objects(Gui,objs[0],ceramic_color)
    elif (params.shape == "bare"):
        Color_Objects(Gui,objs[0],pins_color) # body same colour as pins
    else:
        Color_Objects(Gui,objs[0],body_color) # colourful resistors!
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

    #if (params.rot !=0):
    #    z_RotateObject(doc, params.rot)
    
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
    pinrange = [1]

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building example')
        model_to_build = "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"
    else:
        model_to_build = sys.argv[2]

    if model_to_build == 'all':
        models = [all_params[model_to_build] for model_to_build in all_params.keys()]
        pinrange = range(4,14)
        save_memory = True
    else:
        models = [all_params[i] for i in model_to_build.split(',') if i in all_params.keys()]#separate model types with comma
    
    #make all the seleted models
    pincount = 0
    basecount = 0

    print "\n m"
    print models
    print pinrange
    for model in models:
        # only arrays will pay attention to n
        if (model.shape == "array"):
            for pin_number in pinrange:
                MakePart(model)
        else:
            MakePart(model)

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



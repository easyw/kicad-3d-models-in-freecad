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

__title__ = "make Pin header 3D models"
__author__ = "maurice and Shack"
__Comment__ = 'make pin header 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "2.0.0 21/11/2017"


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
import argparse
import yaml
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


def make_Vertical_THT_base(n, pitch, base_width, base_height, base_chamfer):
    if base_chamfer == 0:
        base = cq.Workplane("XY").moveTo(-pitch/2.,pitch/2.).vLine(n*-pitch).hLine(base_width).vLine(n*pitch)
    else:
        base = cq.Workplane("XY").moveTo(-pitch/2.+base_chamfer,pitch/2.)
        for x in range(0, n):
            base = base.line(-base_chamfer,-base_chamfer).vLine(-pitch+base_chamfer*2.).line(base_chamfer,-base_chamfer)
        base = base.hLine(base_width-base_chamfer*2.)
        for x in range(0, n):
            base = base.line(base_chamfer,base_chamfer).vLine(pitch-base_chamfer*2.).line(-base_chamfer,base_chamfer)
    base = base.close().extrude(base_height)
    return base

def make_Horizontal_THT_base(n, pitch, base_width, base_height, base_x_offset, base_chamfer):
    if base_chamfer == 0:
        base = cq.Workplane("ZY").workplane(offset=-(base_x_offset+base_height)).moveTo(0.0,pitch/2.).vLine(n*-pitch).hLine(base_width).vLine(n*pitch)
    else:
        base = cq.Workplane("ZY").workplane(offset=-(base_x_offset+base_height)).moveTo(base_chamfer,pitch/2.)
        for x in range(0, n):
            base = base.line(-base_chamfer,-base_chamfer).vLine(-pitch+base_chamfer*2.).line(base_chamfer,-base_chamfer)
        base = base.hLine(base_width-base_chamfer*2.)
        for x in range(0, n):
            base = base.line(base_chamfer,base_chamfer).vLine(pitch-base_chamfer*2.).line(-base_chamfer,base_chamfer)
    base = base.close().extrude(base_height)
    return base

def make_Vertical_SMD_base(n, pitch, base_width, base_height, base_chamfer, base_z_offset = 0):
    if base_chamfer == 0:
        base = cq.Workplane("XY").workplane(offset=base_z_offset).moveTo(-base_width/2.0,n/2.*pitch).vLine(n*-pitch).hLine(base_width).vLine(n*pitch)
    else:
        base = cq.Workplane("XY").workplane(offset=base_z_offset).moveTo(-base_width/2.0+base_chamfer,n/2.*pitch)
        for x in range(0, n):
            base = base.line(-base_chamfer,-base_chamfer).vLine(-pitch+base_chamfer*2.).line(base_chamfer,-base_chamfer)
        base = base.hLine(base_width-base_chamfer*2.)
        for x in range(0, n):
            base = base.line(base_chamfer,base_chamfer).vLine(pitch-base_chamfer*2.).line(-base_chamfer,base_chamfer)
    base = base.close().extrude(base_height)
    return base

def make_Vertical_THT_pins(n, pitch, rows, pin_length_above_base, pin_length_below_board, base_height, pin_width, pin_end_chamfer):
    total_length = pin_length_below_board + base_height + pin_length_above_base
    pin = cq.Workplane("XY").workplane(offset=-pin_length_below_board).box(pin_width, pin_width, total_length, centered = (True,True,False))
    if pin_end_chamfer > 0:
        pin = pin.edges("#Z").chamfer(pin_end_chamfer)
    pins = cq.Workplane("XY").workplane(offset=-pin_length_below_board)
    for x in range(rows):
        for y in range(n):
            pins = pins.union(pin.translate((x*pitch,y*-pitch,0)))
    return pins

def make_Horizontal_THT_pins(n, pitch, rows, pin_length_above_base, pin_length_below_board, base_height, base_width, pin_width, pin_end_chamfer, base_x_offset):
    R1 = pin_width
    pin_array = []
    for row in range(rows):
        row_offset = row*pitch
        pin_array.append(cq.Workplane("ZX").workplane(offset=-pin_width/2). \
        moveTo(base_width/rows/2+pin_width/2+row_offset,base_x_offset+base_height+pin_length_above_base). \
        hLine(-pin_width). \
        vLine(-pin_length_above_base-base_height-base_x_offset-row_offset+pin_width/2). \
        hLine(-(base_width/rows-pin_width)/2-pin_length_below_board-row_offset). \
        vLine(-pin_width). \
        hLine(((base_width/rows)-pin_width)/2+pin_length_below_board+row_offset+pin_width). \
        close().extrude(pin_width).edges("<X and >Z").fillet(pin_width))

        if pin_end_chamfer > 0:
            pin_array[row] = pin_array[row].faces("<Z").chamfer(pin_end_chamfer)
            pin_array[row] = pin_array[row].faces(">X").chamfer(pin_end_chamfer)
    pins = cq.Workplane("XY") #.workplane(offset=-pin_length_below_board)
    for x in range(rows):
        for y in range(n):
            pins = pins.union(pin_array[x].translate((0 ,y*-pitch,0)))
    return pins

def make_Vertical_SMD_pins(n, pitch, rows, pin_length_above_base, pin_length_horizontal, base_height, base_width, pin_width, pin_end_chamfer, base_z_offset, pin_1_start = None):
    R1 = pin_width
    pin_array = []
    pin_array.append(cq.Workplane("XZ").workplane(offset=-((n-1)*pitch+pin_width)/2).moveTo(-((rows-1)*pitch-pin_width)/2,base_z_offset+base_height+pin_length_above_base). \
        hLine(-pin_width). \
        vLine(-base_z_offset-base_height-pin_length_above_base+pin_width). \
        hLine(-pin_length_horizontal+pin_width). \
        vLine(-pin_width). \
        hLine(pin_length_horizontal). \
        close().extrude(pin_width).edges(">X and <Z").fillet(pin_width))
    if pin_end_chamfer > 0:
        pin_array[0] = pin_array[0].faces(">Z").chamfer(pin_end_chamfer)
        pin_array[0] = pin_array[0].faces("<X").chamfer(pin_end_chamfer)
    pin_array.append(cq.Workplane("XZ").workplane(offset=-((n-1)*pitch+pin_width)/2).moveTo(((rows-1)*pitch-pin_width)/2,base_z_offset+base_height+pin_length_above_base). \
        hLine(pin_width). \
        vLine(-base_z_offset-base_height-pin_length_above_base+pin_width). \
        hLine(pin_length_horizontal-pin_width). \
        vLine(-pin_width). \
        hLine(-pin_length_horizontal). \
        close().extrude(pin_width).edges("<X and <Z").fillet(pin_width))
    if pin_end_chamfer > 0:
        pin_array[1] = pin_array[1].faces(">Z").chamfer(pin_end_chamfer)
        pin_array[1] = pin_array[1].faces(">X").chamfer(pin_end_chamfer)
    pins = cq.Workplane("XY") #.workplane(offset=-pin_length_below_board)
    if rows == 1:
        if pin_1_start == 'right':
            right_pin = range(1,n, 2)
            left_pin = range(0, n, 2)
        elif pin_1_start == 'left':
            right_pin = range(0,n, 2)
            left_pin = range(1, n, 2)
        else:
            print 'not found'
    else:
        right_pin = range(n)
        left_pin = range(n)

    for y in right_pin:
            pins = pins.union(pin_array[0].translate((0 ,y*-pitch,0)))
    for y in left_pin:
            pins = pins.union(pin_array[1].translate((0 ,y*-pitch,0)))
    return pins

#make a pin header using supplied parameters, n pins in each row
def MakeHeader(n, model, all_params):
    global formerDOC
    global LIST_license
    name = model.replace('yy', "{n:02}".format(n=n))

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
    out_dir=models_dir+all_params[model]['output_directory']
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    docname = name.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
   
    newdoc = App.newDocument(docname)
    App.setActiveDocument(docname)
    App.ActiveDocument=App.getDocument(docname)
    Gui.ActiveDocument=Gui.getDocument(docname)
    
    header_type = all_params[model]['type']
    pitch = all_params[model]['pitch']
    rows = all_params[model]['rows']
    base_width = all_params[model]['base_width']
    base_height = all_params[model]['base_height']
    base_chamfer = all_params[model]['base_chamfer']
    pin_width = all_params[model]['pin_width']
    pin_length_above_base = all_params[model]['pin_length_above_base']
    
    pin_end_chamfer = all_params[model]['pin_end_chamfer']
    rotation = all_params[model]['rotation']
    
    if base_chamfer == 'auto':
        base_chamfer = pitch/10.

    if pin_end_chamfer == 'auto':
        pin_end_chamfer = pin_width/4.

    if header_type == 'Vertical_THT':
        pin_length_below_board = all_params[model]['pin_length_below_board']
        base = make_Vertical_THT_base(n, pitch, base_width, base_height, base_chamfer)
        pins = make_Vertical_THT_pins(n, pitch, rows, pin_length_above_base, pin_length_below_board, base_height, pin_width, pin_end_chamfer)
    elif header_type == 'Horizontal_THT':
        pin_length_below_board = all_params[model]['pin_length_below_board']
        base_x_offset = all_params[model]['base_x_offset']
        base = make_Horizontal_THT_base(n, pitch, base_width, base_height, base_x_offset, base_chamfer)
        pins = make_Horizontal_THT_pins(n, pitch, rows, pin_length_above_base, pin_length_below_board, base_height, base_width, pin_width, pin_end_chamfer, base_x_offset)
    elif header_type == 'Vertical_SMD':
        pin_length_horizontal = all_params[model]['pin_length_horizontal']
        base_z_offset = all_params[model]['base_z_offset']
        if rows == 1:
            pin_1_start = all_params[model]['pin_1_start']
        else:
            pin_1_start = None
        pins = make_Vertical_SMD_pins(n, pitch, rows, pin_length_above_base, pin_length_horizontal, base_height, base_width, pin_width, pin_end_chamfer, base_z_offset, pin_1_start)
        base = make_Vertical_SMD_base(n, pitch, base_width, base_height, base_chamfer, base_z_offset)
    else:
        print 'Header type: '
        print header_type
        print ' is not recognized, please check parameters'
        stop

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

    #objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui,
                   doc.Name, objs[0].Name, objs[1].Name)
    doc.Label=docname
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=docname
    restore_Main_Tools()

    if (rotation !=0):
        z_RotateObject(doc, rotation)
    
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
    saveFCdoc(App, Gui, doc, name,out_dir, False)
    if save_memory == True:
        closeCurrentDoc(docname)
    return 0
    
#import step_license as L
import add_license as Lic

if __name__ == "__main__" or __name__ == "main_generator":
    try:
        with open('cq_parameters.yaml', 'r') as f:
            all_params = yaml.load(f)
    except yaml.YAMLError as exc:
        print(exc)
    '''
    for models_to_build in all_params:
        print models_to_build
    '''
    from sys import argv
    models = []
    pinrange = []

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building:\n')
        model_to_build = all_params.keys()[0]
    else:
        model_to_build = sys.argv[2]
    if len(sys.argv) > 3:
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
                pinrange = [pin_number]
            except:
                FreeCAD.Console.PrintMessage("Pin argument '",p,"' is invalid")
                pinrange = []

    if model_to_build == "all":
       	models = all_params
    else:
    	models = [model_to_build]

    for model in models:
        if len(pinrange) < 1:
    	   pinrange = range(all_params[model]['pins']['from'],all_params[model]['pins']['to']+1)
        
        if len(pinrange) > 2:
            save_memory=True
        print model
        print "\n"
        print 'pins:'
        print pinrange
        for pins in pinrange:
            MakeHeader(pins, model, all_params)

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



# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
# This is a 
# Dimensions are from Microchips Packaging Specification document:
# DS00000049BY. Body drawing is the same as QFP generator#

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module2512 

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

__title__ = "make chip LED's 3D models"
__author__ = "Frank & Maurice"
__Comment__ = 'make chip LEDs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "2.0.0 29/01/2018"

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple
global save_memory
save_memory = False #reducing memory consuming for all generation params

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "white body"  #"white body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "gold pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
top_color_key = "led white"
top_color = shaderColors.named_colors[top_color_key].getDiffuseFloat()
pinmark_color_key = "green body"
pinmark_color = shaderColors.named_colors[pinmark_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
import yaml
#from Gui.Command import *

import logging
logging.getLogger('builder').addHandler(logging.NullHandler())
#logger = logging.getLogger('builder')
#logging.info("Begin")

outdir=os.path.dirname(os.path.realpath(__file__)+"/../_3Dmodels")
scriptdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)
sys.path.append(scriptdir)

#import PySide
#from PySide import QtGui, QtCore
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

#checking requirements

try:
    close_CQ_Example(FreeCAD, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"

def make_chip(model, all_params):
    # dimensions for LED's
    package_found = True
    
    package_type = all_params[model]['package_type']
    length = all_params[model]['length'] # package length
    width = all_params[model]['width'] # package width
    height = all_params[model]['height'] # package height
    pin_band = all_params[model]['pin_band'] # pin band
    pin_thickness = all_params[model]['pin_thickness'] # pin thickness
    if pin_thickness == 'auto':
        pin_thickness = pin_band/10.0
    base_height = all_params[model]['base_height'] # pin thickness
    edge_fillet = all_params[model]['edge_fillet'] # fillet of edges
    place_pinmark = all_params[model]['pinmark']
    pinmark = 0
    if edge_fillet == 'auto':
        edge_fillet = pin_thickness

    if package_type == 'chip_lga':
        pin_distance_edge = all_params[model]['pin_distance_edge']
        if pin_thickness == 'auto':
            pin_thickness = 0.01
        # creating base
        base = cq.Workplane("XY").workplane(offset=pin_thickness).\
        box(length, width, base_height,centered=(True, True, False))
        #creating top
        top = cq.Workplane("XZ").workplane(offset=-width/2.).\
        moveTo(-(length/2.),base_height+pin_thickness).lineTo((-(length/2))*0.9, height).\
        lineTo((length/2.)*0.9, height).lineTo(length/2.,base_height+pin_thickness).close().extrude(width)
        #creating pins
        pin_center = length/2.-pin_distance_edge-pin_band/2.
        pins = cq.Workplane("XY").moveTo(-pin_center, 0).\
        box(pin_band, width-2*pin_distance_edge, pin_thickness,centered=(True, True, False)).\
        moveTo(pin_center, 0).\
        box(pin_band, width-2*pin_distance_edge, pin_thickness,centered=(True, True, False))
        if place_pinmark == True:
            pinmark_side = (length-pin_distance_edge*2.-pin_band*2.)*0.8
            pinmark_length = sqrt(pinmark_side*pinmark_side - pinmark_side/2*pinmark_side/2)
            pinmark = cq.Workplane("XY").workplane(offset=pin_thickness/2).moveTo(-pinmark_length/2,0).\
            lineTo(pinmark_length/2,pinmark_side/2).lineTo(pinmark_length/2,-pinmark_side/2).close().extrude(pin_thickness/2)
    elif package_type == 'chip_convex':
        # creating base
        base = cq.Workplane("XY").workplane(offset=pin_thickness).\
        box(length-2*pin_thickness, width, base_height-2*pin_thickness,centered=(True, True, False))
        # creating top
        top = cq.Workplane("XZ").workplane(offset=-width/2).moveTo(-(length/2-pin_band),base_height-pin_thickness).\
        lineTo((-(length/2-pin_band))*0.9, height).lineTo((length/2-pin_band)*0.9, height).\
        lineTo(length/2-pin_band,base_height-pin_thickness).close().extrude(width)
        # creating pins
        pins = cq.Workplane("XY").moveTo((length-pin_band)/2.,0).\
        box(pin_band, width, base_height,centered=(True, True, False)).moveTo(-(length-pin_band)/2.,0).\
        box(pin_band, width, base_height,centered=(True, True, False)).edges("|Y").fillet(edge_fillet)
        pins = pins.workplane(offset=base_height).moveTo(0, width/2).rect(length-pin_band/2, width/4, centered=True).cutThruAll().\
        moveTo(0, -width/2).rect(length-pin_band/2, width/4, centered=True).cutThruAll()
        pins = pins.cut(base)
        # creating pinmark
        if place_pinmark == True:
            pinmark_side = width*0.8
            pinmark_length = sqrt(pinmark_side*pinmark_side - pinmark_side/2*pinmark_side/2)
            pinmark = cq.Workplane("XY").workplane(offset=pin_thickness/2).moveTo(-pinmark_length/2,0).\
            lineTo(pinmark_length/2,pinmark_side/2).lineTo(pinmark_length/2,-pinmark_side/2).close().extrude(pin_thickness/2)
   
    elif package_type == 'chip_concave':
        base = cq.Workplane("XY").workplane(offset=pin_thickness).\
        box(length-2*pin_thickness, width, base_height-2*pin_thickness,centered=(True, True, False))
        base = base.workplane(offset=base_height).moveTo(-length/2, -width/4-0.1).\
        threePointArc((-length/2+pin_band/2+0.1, 0),(-length/2, width/4+0.1),forConstruction=False).close().\
        moveTo(length/2, -width/4-0.1).\
        threePointArc((length/2-pin_band/2-0.1, 0),(length/2, width/4+0.1),forConstruction=False).close().cutThruAll()
        # creating top
        top = cq.Workplane("XZ").workplane(offset=-width/2).moveTo(-(length/2-pin_band),base_height-pin_thickness).\
        lineTo((-(length/2-pin_band))*0.9, height).lineTo((length/2-pin_band)*0.9, height).\
        lineTo(length/2-pin_band,base_height-pin_thickness).close().extrude(width)
        # creating pins
        pins = cq.Workplane("XY").moveTo((length-pin_band)/2.,0).\
        box(pin_band, width, base_height,centered=(True, True, False)).moveTo(-(length-pin_band)/2.,0).\
        box(pin_band, width, base_height,centered=(True, True, False)).edges("|Y").fillet(edge_fillet)
        pins = pins.workplane(offset=base_height).moveTo(-length/2, -width/4).\
        threePointArc((-length/2+pin_band/2, 0),(-length/2, width/4),forConstruction=False).close().\
        moveTo(length/2, -width/4).\
        threePointArc((length/2-pin_band/2, 0),(length/2, width/4),forConstruction=False).close().cutThruAll()
        pins = pins.cut(base)
        # creating pinmark
        if place_pinmark == True:
            pinmark_side = width*0.8
            pinmark_length = sqrt(pinmark_side*pinmark_side - pinmark_side/2*pinmark_side/2)
            pinmark = cq.Workplane("XY").workplane(offset=pin_thickness/2).moveTo(-pinmark_length/2,0).\
            lineTo(pinmark_length/2,pinmark_side/2).lineTo(pinmark_length/2,-pinmark_side/2).close().extrude(pin_thickness/2)
   
    elif package_type == 'chip_concave_4':
    
        top_length = all_params[model]['top_length']
        top_width = all_params[model]['top_width']
        top_height = all_params[model]['top_height']

        pincnt = all_params[model]['pincnt']
        
        # creating base
        base = cq.Workplane("XY").workplane(offset=pin_thickness).moveTo(0.0, 0.0).rect(length, width, True).extrude(height)
        
        # creating top
        top = cq.Workplane("XY").workplane(offset=pin_thickness + (height - 0.0001)).moveTo(0.0, 0.0).rect(top_length, top_width, True).extrude(top_height)
        top = top.faces("<X").edges(">Z").chamfer(top_height - 0.002, top_height / 4.0)
        top = top.faces(">X").edges(">Z").chamfer(top_height / 4.0, top_height - 0.002)
        top = top.faces(">Z").edges(">X").fillet(top_height / 10.0)
        top = top.faces(">Z").edges("<X").fillet(top_height / 10.0)

        # creating pins
        pins = None
        for i in range(0, len(pincnt)):
            p = pincnt[i]
            px = p[0]
            py = p[1]
            pw = p[2]
            pl = p[3]
            ph = p[4]
            
            p2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(px, py).rect(pl, pw, True).extrude(ph)
            
            pcx = 0.0
            if px > 0:
                pcx = px + (pl / 2.0)
            else:
                pcx = (px - (pl / 2.0))
            
            pc0 = cq.Workplane("XY").workplane(offset=0.0).moveTo(pcx, py).circle(pw / 4.0, False).extrude(2 * base_height)
            p2 = p2.cut(pc0)
            base = base.cut(pc0)

            if i == 0:
                pins = p2
            else:
                pins = pins.union(p2)

        # creating pinmark
        if place_pinmark == True:
            pinmark_side = width*0.4
            pinmark_length = sqrt(pinmark_side*pinmark_side - pinmark_side/2*pinmark_side/2)
            pinmark = cq.Workplane("XY").workplane(offset=pin_thickness/2).moveTo(-pinmark_length/2,0).\
            lineTo(pinmark_length/2,pinmark_side/2).lineTo(pinmark_length/2,-pinmark_side/2).close().extrude(pin_thickness/2)
        else:
           pinmark = cq.Workplane("XY").workplane(offset=pin_thickness + 0.05).moveTo(0.0, 0.0).rect(0.05, 0.05, True).extrude(0.05)

   
    elif package_type == 'plcc_a':
        pincnt = all_params[model]['pincnt']
        #
        # Make the main block
        base = cq.Workplane("XY").workplane(offset=base_height).moveTo(0.0, 0.0).rect(length, width, True).extrude(height)
        #
        # Cut out the edge of the corner
        p2 = cq.Workplane("XY").workplane(offset=base_height + (height * 0.8)).moveTo(0.0, 0.0).rect(length, width, True).extrude(height)
        p2 = p2.rotate((0,0,0), (0,0,1), 45.0)
        p2 = p2.translate((0.0 - (length * 0.75), (width * 0.75), 0.0))
        base = base.cut(p2)
        #
        # Make rounded top
        base = base.faces(">Z").fillet(height / 20.0)
        #
        # Cut out the circular hole ontop
        tp = cq.Workplane("XY").workplane(offset=base_height + (height / 2.0)).moveTo(0.0, 0.0).circle(width / 3.0, False).extrude(2 * height)
        base = base.cut(tp)
        base = base.faces(">Z[3]").chamfer(height / 5.0)
        #
        # Create the glass top
        top = cq.Workplane("XY").workplane(offset=base_height + (height / 2.0)).moveTo(0.0, 0.0).circle(width / 3.0, False).extrude(height / 4.0)
        
        pins = None
        for i in range(0, len(pincnt)):
            p = pincnt[i]
            px = p[0]
            py = p[1]
            pw = p[2]
            pl = p[3]
            ph = p[4]
            
            p2 = cq.Workplane("XY").workplane(offset=0.0).moveTo(px, py).rect(pl, pw, True).extrude(ph)
            p3 = cq.Workplane("XY").workplane(offset=pin_thickness).moveTo(px, py).rect(pl - (2.0 * pin_thickness), pw + (2.0 * pin_thickness), True).extrude(ph - (2.0 * pin_thickness))
            p3 = p3.faces("<X").fillet(pin_thickness / 2.0)
            p3 = p3.faces(">X").fillet(pin_thickness / 2.0)
            p2 = p2.cut(p3)
            if px < 0:
                p2 = p2.faces("<X").edges(">Z").fillet(pin_thickness / 2.0)
                p2 = p2.faces("<X").edges("<Z").fillet(pin_thickness / 2.0)
            else:
                p2 = p2.faces(">X").edges(">Z").fillet(pin_thickness / 2.0)
                p2 = p2.faces(">X").edges("<Z").fillet(pin_thickness / 2.0)

            if i == 0:
                pins = p2
            else:
                pins = pins.union(p2)
            
        pinmark = cq.Workplane("XY").workplane(offset=pin_thickness + (height / 2.0)).moveTo(0.0, 0.0).circle(width / 3.0, False).extrude(height / 8.0)
        
    else:
        package_found = False
        base = 0
        top = 0
        pins = 0
        pinmark = 0
    return (base, top, pins, pinmark, package_found)
    

# The dimensions of the box. These can be modified rather than changing the
# object's code directly.

#import step_license as L
import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":
    destination_dir = '/LED_SMD.3dshapes'
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
    
    try:
        with open('cq_parameters.yaml', 'r') as f:
            all_params = yaml.load(f)
    except yaml.YAMLError as exc:
        FreeCAD.Console.PrintMessage('%s\r\n' % str(exc))
        print(exc)

    from sys import argv
    models = []

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building:\n')
        model_to_build = all_params.keys()[0]
        print model_to_build
    else:
        model_to_build = sys.argv[2]
    
    if model_to_build == "all":
        models = all_params
        save_memory=True
    else:
        models = [model_to_build]

    for model in models:
        if not model in all_params.keys():
            print("Parameters for %s doesn't exist in 'all_params', skipping." % model)
            continue
        print("building %s" % model)
        ModelName = model
        CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        base, top, pins, pinmark, package_found = make_chip(model, all_params)
        if package_found == False:
            print("package_type is not recognized")
            continue
            
        try:
            b_c = all_params[model]['body_color']
            if len(b_c) > 0:
                body_color_key = all_params[model]['body_color']
                body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        except:
            # Default value
            body_color_key = "white body"  #"white body"
            body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
            
            
        try:
            b_c = all_params[model]['top_color']
            if len(b_c) > 0:
                top_color_key = all_params[model]['top_color']
                top_color = shaderColors.named_colors[top_color_key].getDiffuseFloat()
        except:
            # Default value
            top_color_key = "led white"
            top_color = shaderColors.named_colors[top_color_key].getDiffuseFloat()

        try:
            b_c = all_params[model]['pin_color']
            if len(b_c) > 0:
                pins_color_key = all_params[model]['pin_color']
                pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
        except:
            # Default value
            pins_color_key = "gold pins"
            pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()

        try:
            b_c = all_params[model]['pinmark_color']
            if len(b_c) > 0:
                pinmark_color_key = all_params[model]['pinmark_color']
                pinmark_color = shaderColors.named_colors[pinmark_color_key].getDiffuseFloat()
        except:
            # Default value
            pinmark_color_key = "green body"
            pinmark_color = shaderColors.named_colors[pinmark_color_key].getDiffuseFloat()
                

        show(base)
        show(top)
        show(pins)
        show(pinmark)
   
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)

        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],top_color)
        Color_Objects(Gui,objs[2],pins_color)
        Color_Objects(Gui,objs[3],pinmark_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_top=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_pins=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        col_pinmark=Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]

        material_substitutions={
            col_body[:-1]:body_color_key,
            col_top[:-1]:top_color_key,
            col_pins[:-1]:pins_color_key,
            col_pinmark[:-1]:pinmark_color_key
        }

        expVRML.say(material_substitutions)

        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        while len(objs) > 1:
            FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
            del objs
            objs = GetListOfObjects(FreeCAD, doc)
        doc.Label = CheckedModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label = CheckedModelName
        restore_Main_Tools()
        #rotate if required
        rotation = all_params[model]['rotation']
        if (rotation!=0):
            z_RotateObject(doc, rotation)

        script_dir=os.path.dirname(os.path.realpath(__file__))
        ## models_dir=script_dir+"/../_3Dmodels"
        expVRML.say(models_dir)
        out_dir=models_dir+destination_dir
        #out_dir=script_dir+os.sep+destination_dir
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
        if save_memory == False:
            Gui.SendMsgToActiveView("ViewFit")
            Gui.activeDocument().activeView().viewAxometric()

        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir, False)


        check_Model=False
        if save_memory == True or check_Model==True:
            doc=FreeCAD.ActiveDocument
            FreeCAD.closeDocument(doc.Name)

        step_path=os.path.join(out_dir,ModelName+u'.step')
        if check_Model==True:
            #ImportGui.insert(step_path,ModelName)
            ImportGui.open(step_path)
            docu = FreeCAD.ActiveDocument
            if cq_cad_tools.checkUnion(docu) == True:
                FreeCAD.Console.PrintMessage('step file is correctly Unioned\n')
            else:
                FreeCAD.Console.PrintError('step file is NOT Unioned\n')
                stop
            FC_majorV=int(FreeCAD.Version()[0])
            FC_minorV=int(FreeCAD.Version()[1])
            if FC_majorV == 0 and FC_minorV >= 17:
                for o in docu.Objects:
                    if hasattr(o,'Shape'):
                        chks=cq_cad_tools.checkBOP(o.Shape)
                        print 'chks ',chks
                        print cq_cad_tools.mk_string(o.Label)
                        if chks != True:
                            msg='shape \''+o.Name+'\' \''+cq_cad_tools.mk_string(o.Label)+'\' is INVALID!\n'
                            FreeCAD.Console.PrintError(msg)
                            FreeCAD.Console.PrintWarning(chks[0])
                            stop
                        else:
                            msg='shape \''+o.Name+'\' \''+cq_cad_tools.mk_string(o.Label)+'\' is valid\n'
                            FreeCAD.Console.PrintMessage(msg)
            else:
                FreeCAD.Console.PrintError('BOP check requires FC 0.17+\n')
            # Save the doc in Native FC format
            saveFCdoc(App, Gui, docu, ModelName,out_dir, False)
            doc=FreeCAD.ActiveDocument
            FreeCAD.closeDocument(doc.Name)

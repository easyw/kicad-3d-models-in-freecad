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
__author__ = "Frank & Maurice & Stefan"
__Comment__ = 'make THT potentiometers exported to STEP and VRML for Kicad StepUP script'

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

body_color_key = "blue body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
top_color_key = "metal copper"
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
    pin1corner = all_params[model]['pin1corner']
    pincnt = all_params[model]['pincnt']
    base_height = all_params[model]['base_height']
    screw = all_params[model]['screw']
    rotation = all_params[model]['rotation']
    pinmark = all_params[model]['pinmark']
    source = all_params[model]['source']
    
    top = None
    base = None
    pins = None
    pinmark = None
    
    if package_type == 'Bourns_3005':
        #
        p0 = pincnt[0]
        p1 = pincnt[1]
        p2 = pincnt[2]
    
        # Create base
        base = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(length, width, True).extrude(height)
        base0 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(length - (2* 0.76), width + 0.2, True).extrude(0.89)
        base = base.cut(base0)
        base = base.faces(">X").edges(">Y").fillet(height / 60.0)
        base = base.faces(">X").edges("<Y").fillet(height / 60.0)
        base = base.faces("<X").edges(">Y").fillet(height / 60.0)
        base = base.faces("<X").edges("<Y").fillet(height / 60.0)
        base = base.faces(">Z").fillet(height / 60.0)
        base = base.translate((0.0 - ((length / 2.0) - pin1corner[0]), (p1[2] / 2.0), 0.0))

        # Create top (screw)
        st = screw[0]
        sl = screw[1]
        sd = screw[2]
        sc = screw[3]
        sh = screw[4]
        
        if st == 'lefttop':
            sx = length / 2.0
            top = cq.Workplane("ZY").workplane(offset = (length / 2.0) - 0.1).moveTo(sh, 0.0).circle(sd / 2.0, False).extrude(sl + 0.1)
            top = top.faces("<X").fillet(sl / 5.0)
            top0 = cq.Workplane("ZY").workplane(offset = ((length / 2.0)) + sl + 0.1).moveTo(sh, 0.0).rect(sd + 1.0, sd / 5.0, True).extrude(0.0 - (sc + 0.1))
            top = top.cut(top0)
            top = top.translate((0.0 - ((length / 2.0) - pin1corner[0]), (p1[2] / 2.0), 0.0))

    
    if package_type == 'Bourns_3299P' or package_type == 'Bourns_3299W' or package_type == 'Bourns_3299X' or package_type == 'Bourns_3299Y' or package_type == 'Bourns_3299Z':
        #
        p0 = pincnt[0]
        p1 = pincnt[1]
        p2 = pincnt[2]
    
        # Create base
        base = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(length, width, True).extrude(height)
        base0 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(length - (2* 0.38), width + 0.2, True).extrude(0.38)
        base = base.cut(base0)
        base0 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(length + 0.2, width- (2* 0.38), True).extrude(0.38)
        base = base.cut(base0)
        base0 = cq.Workplane("XY").workplane(offset=0.0).moveTo((length / 2.0) - (0.38 / 2.0), 0.0).rect(0.38, width - (2* 0.38), True).extrude(height)
        base = base.cut(base0)

        base = base.faces(">X").edges(">Y").fillet(height / 60.0)
        base = base.faces(">X").edges("<Y").fillet(height / 60.0)
        base = base.faces("<X").edges(">Y").fillet(height / 60.0)
        base = base.faces("<X").edges("<Y").fillet(height / 60.0)
        base = base.faces(">Z").fillet(height / 60.0)

        if package_type == 'Bourns_3299P':
            base = base.translate((((length / 2.0) - pin1corner[0]), 0.0 - ((width / 2.0) - (pin1corner[1])), 0.0))

        if package_type == 'Bourns_3299W' or package_type == 'Bourns_3299X' or package_type == 'Bourns_3299Y' or package_type == 'Bourns_3299Z':
            base = base.rotate((0,0,0), (1,0,0), 90.0)
            base = base.rotate((0,0,0), (0,1,0), 90.0)
            base = base.translate((0.0, height / 2.0, length / 2.0))
            base = base.translate((0.0 - ((width / 2.0) - pin1corner[0]), 0.0 - ((height / 2.0) - (pin1corner[1])), 0.0))

        # Create top (screw)
        st = screw[0]
        sl = screw[1]
        sd = screw[2]
        sc = screw[3]
        sz = screw[4]
        sy = screw[5]

        if st == 'lefttop':
            sx = length / 2.0
            top = cq.Workplane("ZY").workplane(offset = 0.0 - 0.1).moveTo(0.0, 0.0).circle(sd / 2.0, False).extrude(sl + 0.1)
            top = top.faces("<X").fillet(sl / 5.0)
            top0 = cq.Workplane("ZY").workplane(offset = sl + 0.1).moveTo(0.0, 0.0).rect(sd + 1.0, sd / 5.0, True).extrude(0.0 - (sc + 0.1))
            top = top.cut(top0)

            if package_type == 'Bourns_3299P':
                top = top.translate((0.0 - (length / 2.0), sy, sz))
                top = top.translate((((length / 2.0) - pin1corner[0]), 0.0 - ((width / 2.0) - (pin1corner[1])), 0.0))

            if package_type == 'Bourns_3299W' or package_type == 'Bourns_3299Y':
                top = top.rotate((0,0,0), (1,0,0), 90.0)
                top = top.rotate((0,0,0), (0,1,0), 90.0)
                top = top.translate((0.0, 0.0, length))
                top = top.translate(((pin1corner[0] - sy), pin1corner[1] - sz, 0.0))

            if package_type == 'Bourns_3299X' or package_type == 'Bourns_3299Z':
                top = top.rotate((0,0,0), (1,0,0), 90.0)
                top = top.translate((0.0 - width, 0.0, 0.0))
                top = top.translate(((pin1corner[0]), pin1corner[1] - sz, length - sy))


    # creating pins
    for i in range(0, len(pincnt)):
        p = pincnt[i]
        pt = p[0]
        px = p[1]
        py = p[2]
        
        if pt == 'tht':
            pl = p[3]
            pw = p[4]
            ph = p[5]
            p2 = cq.Workplane("XY").workplane(offset = 1.0).moveTo(px, py).rect(pl, pw, True).extrude((0.0 - ph) - 1.0)
            if pl > pw:
                p2 = p2.faces("<Z").edges("<X").fillet(pl / 2.5)
                p2 = p2.faces("<Z").edges(">X").fillet(pl / 2.5)
            else:
                p2 = p2.faces("<Z").edges("<Y").fillet(pw / 2.5)
                p2 = p2.faces("<Z").edges(">Y").fillet(pw / 2.5)
                
            p3 = None
            if py > 0.002:
                p3 = cq.Workplane("XY").workplane(offset = 1.0).moveTo(px - (pl / 2.0), py + (pw / 2.0)).rect(pl, 0.0 - (width / 2.0), False).extrude(pw)
                p2 = p2.union(p3)
                p2 = p2.faces(">Z").edges(">Y").fillet(pw / 1.5)
            else:
                p3 = cq.Workplane("XY").workplane(offset = 1.0).moveTo(px - (pl / 2.0), py - (pw / 2.0)).rect(pl, width / 2.0, False).extrude(pw)
                p2 = p2.union(p3)
                p2 = p2.faces(">Z").edges("<Y").fillet(pw / 1.5)

        if pt == 'round':
            pd = p[3]
            ph = p[4]
            p2 = cq.Workplane("XY").workplane(offset = 1.0).moveTo(px, py).circle(pd / 2.0, False).extrude((0.0 - ph) - 1.0)
            p2 = p2.faces("<Z").fillet(pd / 2.5)
        
        if i == 0:
            pins = p2
        else:
            pins = pins.union(p2)

    # Pin marker, dummy
    pinmark = cq.Workplane("XY").workplane(offset=height / 2.0).moveTo(0.0, 0.0).rect(0.1, 0.1, True).extrude(0.1)
    pinmark = pinmark.translate((0.0 - ((length / 2.0) - pin1corner[0]), (p1[2] / 2.0), 0.0))
    
    base = base.translate((0.0, 0.0, base_height))
    top = top.translate((0.0, 0.0, base_height))
    pins = pins.translate((0.0, 0.0, base_height))
    pinmark = pinmark.translate((0.0, 0.0, base_height))
        
    if base == None:
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
    destination_dir = '/Potentiometer_THT.3dshapes'
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
            FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'all_params', skipping." % model)
            continue
        FreeCAD.Console.PrintMessage('building %s\r\n' % model)
        file_name = all_params[model]['file_name']

        ModelName = model
        CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        base, top, pins, pinmark, package_found = make_chip(model, all_params)
        if package_found == False:
            FreeCAD.Console.PrintMessage("package_type is not recognized")
            continue
            
        try:
            b_c = all_params[model]['body_color']
            if len(b_c) > 0:
                body_color_key = all_params[model]['body_color']
                body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
        except:
            # Default value
            body_color_key = "blue body"
            body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
            
            
        try:
            b_c = all_params[model]['top_color']
            if len(b_c) > 0:
                top_color_key = all_params[model]['top_color']
                top_color = shaderColors.named_colors[top_color_key].getDiffuseFloat()
        except:
            # Default value
            top_color_key = "metal copper"
            top_color = shaderColors.named_colors[top_color_key].getDiffuseFloat()

        try:
            b_c = all_params[model]['pin_color']
            if len(b_c) > 0:
                pins_color_key = all_params[model]['pin_color']
                pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
        except:
            # Default value
            pins_color_key = "metal grey pins"
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
        exportSTEP(doc, file_name, out_dir)
        if LIST_license[0]=="":
            LIST_license=Lic.LIST_int_license
            LIST_license.append("")
        Lic.addLicenseToStep(out_dir+'/', file_name+".step", LIST_license,\
                           STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)
        # scale and export Vrml model
        scale=1/2.54
        #exportVRML(doc,file_name,scale,out_dir)
        objs=GetListOfObjects(FreeCAD, doc)
        expVRML.say("######################################################################")
        expVRML.say(objs)
        expVRML.say("######################################################################")
        export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
        export_file_name=out_dir+os.sep+file_name+'.wrl'
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

        # Save the doc in Native FC format
        if save_memory == False:
            Gui.SendMsgToActiveView("ViewFit")
            Gui.activeDocument().activeView().viewAxometric()

        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, file_name,out_dir, False)

        check_Model=False
        if save_memory == True or check_Model==True:
            check_Model = True
            doc=FreeCAD.ActiveDocument
            FreeCAD.closeDocument(doc.Name)

        step_path=os.path.join(out_dir,file_name+u'.step')
        if check_Model==True:
            #ImportGui.insert(step_path,file_name)
            ImportGui.open(step_path)
            docu = FreeCAD.ActiveDocument
            if cq_cad_tools.checkUnion(docu) == True:
                FreeCAD.Console.PrintMessage('step file is correctly Unioned\n')
            else:
                FreeCAD.Console.PrintError('step file is NOT Unioned\n')
                stop
                
            if save_memory == False:
                # Save the doc in Native FC format
                saveFCdoc(App, Gui, docu, file_name,out_dir, False)

        if save_memory == True:
            doc=FreeCAD.ActiveDocument
            FreeCAD.closeDocument(doc.Name)

    if save_memory == True:
        sys.exit()

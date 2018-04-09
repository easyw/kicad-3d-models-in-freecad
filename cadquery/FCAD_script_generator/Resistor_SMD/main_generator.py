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

__title__ = "make chip Resistors 3D models"
__author__ = "maurice"
__Comment__ = 'make chip Resistors 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.2 10/02/2017"

# thanks to Frank Severinsen Shack for including vrml materials

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

body_color_key = "white body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
top_color_key = "resistor black body"
top_color = shaderColors.named_colors[top_color_key].getDiffuseFloat()


# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
import yaml
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
    # dimensions for chip capacitors
    length = all_params[model]['length'] # package length
    width = all_params[model]['width'] # package width
    height = all_params[model]['height'] # package height

    pin_band = all_params[model]['pin_band'] # pin band
    pin_thickness = all_params[model]['pin_thickness'] # pin thickness
    if pin_thickness == 'auto':
        pin_thickness = height/10.

    edge_fillet = all_params[model]['edge_fillet'] # fillet of edges
    if edge_fillet == 'auto':
        edge_fillet = pin_thickness

    # Create a 3D box based on the dimension variables above and fillet it
    case = cq.Workplane("XY").workplane(offset=pin_thickness). \
    box(length-2*pin_thickness, width, height-2*pin_thickness,centered=(True, True, False))
    top = cq.Workplane("XY").workplane(offset=height-pin_thickness).box(length-2*pin_band, width, pin_thickness,centered=(True, True, False))

    # Create a 3D box based on the dimension variables above and fillet it
    pin1 = cq.Workplane("XY").box(pin_band, width, height)
    pin1.edges("|Y").fillet(edge_fillet)
    pin1=pin1.translate((-length/2+pin_band/2,0,height/2)).rotate((0,0,0), (0,0,1), 0)
    pin2 = cq.Workplane("XY").box(pin_band, width, height)
    pin2.edges("|Y").fillet(edge_fillet)
    pin2=pin2.translate((length/2-pin_band/2,0,height/2)).rotate((0,0,0), (0,0,1), 0)
    pins = pin1.union(pin2)
    #body_copy.ShapeColor=result.ShapeColor

    # extract case from pins
    # case = case.cut(pins)
    pins = pins.cut(case)

    return (case, top, pins)

#import step_license as L
import add_license as Lic

if __name__ == "__main__" or __name__ == "main_generator":
    destination_dir = '/Resistor_SMD.3dshapes'

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

        ModelName = model
        CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)

        body, pins, top = make_chip(model, all_params)

        show(body)
        show(pins)
        show(top)
        
        doc = FreeCAD.ActiveDocument
        objs = GetListOfObjects(FreeCAD, doc)

        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],top_color)
        Color_Objects(Gui,objs[2],pins_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_top=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        material_substitutions={
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pins_color_key,
            col_top[:-1]:top_color_key
        }
        expVRML.say(material_substitutions)
        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
        doc.Label = CheckedModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label = CheckedModelName
        restore_Main_Tools()
        #rotate if required
        rotation = all_params[model]['rotation']
        if (rotation!=0):
            z_RotateObject(doc, rotation)
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
        if save_memory == False:
            Gui.SendMsgToActiveView("ViewFit")
            Gui.activeDocument().activeView().viewAxometric()

        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir, False)

        check_Model=True
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


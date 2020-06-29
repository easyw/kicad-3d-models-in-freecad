#!/usr/bin/python
# -*- coding: utf-8 -*-
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
## e.g. c:\freecad\bin\freecad main_generator.py BGA-1156_34x34_35.0x35.0mm_Pitch1.0mm

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

__title__ = "make BGA ICs 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make BGA ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.7 18/06/2020"
global save_memory
save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'

# maui import cadquery as cq
# maui from Helpers import show
import argparse

from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_bot_color_key = "dark green body"
body_bot_color = shaderColors.named_colors[body_bot_color_key].getDiffuseFloat()
body_color_key = "black body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
marking_color_key = "light brown label"
marking_color = shaderColors.named_colors[marking_color_key].getDiffuseFloat()

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
from cqToolsExceptions import *
import cq_cad_tools
# Reload tools
from cq_cad_tools import reload_lib
reload_lib(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements, runGeometryCheck


try:
    # Gui.SendMsgToActiveView("Run")
    # cq Gui            
    #from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except Exception as e: # catch *all* exceptions
    print(e)
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    exit()
    # maui end

#checking requirements
checkRequirements(cq)

import cq_parameters  # modules parameters
from cq_parameters import *

#all_params= all_params_qfn
all_params= kicad_naming_params_qfn

def make_plg(wp, rw, rh, cv1, cv):
    """
    Creates a rectangle with chamfered corners.
    wp: workplane object
    rw: rectangle width
    rh: rectangle height
    cv1: chamfer value for 1st corner (lower left)
    cv: chamfer value for other corners
    """
    points = [
        (-rw/2., -rh/2.+cv1),
        (-rw/2., rh/2.-cv),
        (-rw/2.+cv, rh/2.),
        (rw/2.-cv, rh/2.),
        (rw/2., rh/2.-cv),
        (rw/2., -rh/2.+cv),
        (rw/2.-cv, -rh/2.),
        (-rw/2.+cv1, -rh/2.)#,
        #(-rw/2., -rh/2.+cv1)
    ]
    #return wp.polyline(points)
    sp = points.pop()
    wp=wp.moveTo(sp[0],sp[1])
    wp=wp.polyline(points).close().wire()

    return wp
    #return wp.polyline(points).wire() #, forConstruction=True)
##

def make_case(params):

    ef  = params.ef
    cff = params.cff
    cf = params.cf
    fp_r  = params.fp_r
    fp_d  = params.fp_d
    fp_z  = params.fp_z
    D  = params.D
    E   = params.E
    D1  = params.D1
    E1  = params.E1
    A1  = params.A1
    A2  = params.A2
    A  = params.A
    molded = params.molded
    b   = params.b
    e   = params.e
    ex   = params.ex
    sp   = params.sp
    npx = params.npx
    npy = params.npy
    mN  = params.modelName
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix

    if ex == None:
        ex = e
    if ex == 0:
        ex = e

    if params.excluded_pins is not None:
        epl = list(params.excluded_pins)
        #expVRML.say(epl)
        i=0
        for i in range (0, len(epl)):
            if isinstance(epl[i], int): #long is not supported in python 3
                epl[i]=str(int(epl[i]))
                i=i+1
        excluded_pins=tuple(epl)
        #expVRML.say(excluded_pins)
        #stop
    else:
        excluded_pins=() ##no pin excluded


    sphere_r = b/2 *(1.05) #added extra 0.5% diameter for fusion
    s_center =(0,0,0)
    sphere = cq.Workplane("XY", s_center). \
             sphere(sphere_r)
    bpin=sphere.translate((0,0,b/2-sp))

    pins = []
    # create top, bottom side pins
    pincounter = 1
    first_pos_x = (npx-1)*e/2
    for j in range(npy):
        for i in range(npx):
            if "internals" in excluded_pins:
                if str(int(pincounter)) not in excluded_pins:
                    if j==0 or j==npy-1 or i==0 or i==npx-1:
                        pin = bpin.translate((first_pos_x-i*e, (npy*ex/2-ex/2)-j*ex, 0)).\
                                rotate((0,0,0), (0,0,1), 180)
                        pins.append(pin)
            elif str(int(pincounter)) not in excluded_pins:
                pin = bpin.translate((first_pos_x-i*e, (npy*ex/2-ex/2)-j*ex, 0)).\
                        rotate((0,0,0), (0,0,1), 180)
                pins.append(pin)
                #expVRML.say(j)
            pincounter += 1
    expVRML.say(pincounter-1)

    # merge all pins to a single object
    merged_pins = pins[0]
    for p in pins[1:]:
        merged_pins = merged_pins.union(p)
    pins = merged_pins

    # first pin indicator is created with a spherical pocket
    if fp_r == 0:
        global place_pinMark
        place_pinMark=False
        fp_r = 0.1
    if molded is not None:
        the=24
        if D1 is None:
            D1=D*(1-0.065)
            E1=E*(1-0.065)
        D1_t = D1-2*tan(radians(the))*(A-A1-A2)
        E1_t = E1-2*tan(radians(the))*(A-A1-A2)
        # draw the case
        cw = D-2*A1
        cl = E-2*A1
        case_bot = cq.Workplane("XY").workplane(offset=0)
        case_bot= make_plg(case_bot, cw, cl, cff, cf)
        case_bot = case_bot.extrude(A2-0.01)
        case_bot = case_bot.translate((0,0,A1))
        #show(case_bot)

        case = cq.Workplane("XY").workplane(offset=A1)
        #case = make_plg(case, cw, cl, cce, cce)
        case = make_plg(case, D1, E1, 3*cf, 3*cf)
        #case = case.extrude(c-A1)
        case = case.extrude(0.01)
        case = case.faces(">Z").workplane()
        case = make_plg(case, D1, E1, 3*cf, 3*cf).\
            workplane(offset=A-A2-A1)
        case = make_plg(case, D1_t, E1_t, 3*cf, 3*cf).\
            loft(ruled=True)
        # fillet the bottom vertical edges
        if ef!=0:
            case = case.edges("|Z").fillet(ef)
        # fillet top and side faces of the top molded part
        if ef!=0:
            BS = cq.selectors.BoxSelector
            case = case.edges(BS((-D1/2, -E1/2, A2+0.001), (D1/2, E1/2, A+0.001))).fillet(ef)
            #case = case.edges(BS((-D1/2, -E1/2, c+0.001), (D1/2, E1/2, A+0.001+A1/2))).fillet(ef)
        case = case.translate((0,0,A2-0.01))
        #show(case)
        #stop
        pinmark=cq.Workplane("XZ", (-D/2+fp_d+fp_r, -E/2+fp_d+fp_r, fp_z)).rect(fp_r/2, -2*fp_z, False).revolve().translate((0,0,A))#+fp_z))
        pinmark=pinmark.translate(((D-D1_t)/2+fp_d+cff,(E-E1_t)/2+fp_d+cff,-sp))
        #stop
        if (color_pin_mark==False) and (place_pinMark==True):
            case = case.cut(pinmark)
        # extract pins from case
        #case = case.cut(pins)
        case_bot = case_bot.cut(pins)
        ##

    else:
        A2 = A - A1 #body height
        #if m == 0:
        #    case = cq.Workplane("XY").box(D-A1, E-A1, A2)  #margin to see fused pins
        #else:
        case = cq.Workplane("XY").box(D, E, A2)  #NO margin, pins don't emerge
        if ef!=0:
            case.edges("|X").fillet(ef)
            case.edges("|Z").fillet(ef)
        #translate the object
        case=case.translate((0,0,A2/2+A1-sp)).rotate((0,0,0), (0,0,1), 0)

        #sphere_r = (fp_r*fp_r/2 + fp_z*fp_z) / (2*fp_z)
        #sphere_z = A + sphere_r * 2 - fp_z - sphere_r

        pinmark=cq.Workplane("XZ", (-D/2+fp_d+fp_r, -E/2+fp_d+fp_r, fp_z)).rect(fp_r/2, -2*fp_z, False).revolve().translate((0,0,A2+A1-sp))#+fp_z))
        #pinmark=pinmark.translate((0,0,A1-sp))
        #stop
        if (color_pin_mark==False) and (place_pinMark==True):
            case = case.cut(pinmark)
        # extract pins from case
        case = case.cut(pins)
        case_bot = None
        #show(pins)
        #show(pinmark)
        #show(case)
        #stop


    #show(pins)
    #show(case)
    #Gui.SendMsgToActiveView("ViewFit")
    #Gui.activeDocument().activeView().viewBottom()
    #stop
    #sleep

    return (case_bot, case, pins, pinmark)

#import step_license as L
import add_license as Lic
global ksu_present
ksu_present=False

def generateOneModel(params, log):
    excluded_pins_x=() ##no pin excluded
    excluded_pins_xmirror=() ##no pin excluded
    place_pinMark=True ##default =True used to exclude pin mark to build sot23-3; sot23-5; sc70 (asimmetrical pins, no pinmark)


    ModelName = params.modelName
    FreeCAD.Console.PrintMessage(
        '\n\n##############  ' +
        ModelName +
        '  ###############\n')
    CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedModelName)
    App.setActiveDocument(CheckedModelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
    #case, pins, pinmark = make_case(params)
    case_bot, case, pins, pinmark = make_case(params)

    if case_bot is not None:
        show(case_bot)
    show(case)
    show(pins)
    show(pinmark)
    #stop

    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)

    if case_bot is not None:
        Color_Objects(Gui,objs[0],body_bot_color)
        Color_Objects(Gui,objs[1],body_color)
        Color_Objects(Gui,objs[2],pins_color)
        Color_Objects(Gui,objs[3],marking_color)

        col_body_bot=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_body=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        col_mark=Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
        material_substitutions={
            col_body_bot[:-1]:body_bot_color_key,
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pins_color_key,
            col_mark[:-1]:marking_color_key
        }
        expVRML.say(material_substitutions)
        if (color_pin_mark==True) and (place_pinMark==True):
            CutObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[1].Name, objs[3].Name)
        else:
            #removing pinMark
            App.getDocument(doc.Name).removeObject(objs[3].Name)
        ###
        #sleep
        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[1].Name)
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[1].Name)
    else:
        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],pins_color)
        Color_Objects(Gui,objs[2],marking_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        material_substitutions={
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pins_color_key,
            col_mark[:-1]:marking_color_key
        }
        #expVRML.say(material_substitutions)
        if (color_pin_mark==True) and (place_pinMark==True):
            CutObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[2].Name)
        else:
            #removing pinMark
            App.getDocument(doc.Name).removeObject(objs[2].Name)
        ###
        #sleep
        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui,
                        doc.Name, objs[0].Name, objs[1].Name)
    ## objs[0].Label='body'
    ## objs[1].Label='pins'
    ## objs[2].Label='mark'
    ###
    ## print objs[0].Name, objs[1].Name, objs[2].Name

    ## sleep
    doc.Label=CheckedModelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=CheckedModelName
    restore_Main_Tools()
    #rotate if required
    if (params.rotation!=0):
        rot= params.rotation
        z_RotateObject(doc, rot)
    #out_dir=destination_dir+params.dest_dir_prefix+'/'
    script_dir=os.path.dirname(os.path.realpath(__file__))
    #models_dir=script_dir+"/../_3Dmodels"
    #expVRML.say(models_dir)
    if len(params.dest_dir_prefix)>=1:
        out_dir=models_dir+destination_dir+os.sep+params.dest_dir_prefix
    else:
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
    #expVRML.writeVRMLFile added creaeAngle
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license, 0.9)
    # Save the doc in Native FC format
    #saveFCdoc(App, Gui, doc, ModelName,out_dir)
    #display BBox
    #FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
    if footprints_dir is not None and os.path.isdir(footprints_dir) and not save_memory and not check_Model: #it doesn't make sense to import the footprint right before we close the file.
        #expVRML.say (ModelName)
        #stop
        sys.argv = ["fc", "dummy", footprints_dir+os.sep+ModelName, "savememory"]
        #setup = get_setup_file()  # << You need the parentheses
        expVRML.say(sys.argv[2])
        if not ksu_present:
            try:
                import kicadStepUptools
                ksu_present=True
                expVRML.say("ksu present!")
                kicadStepUptools.KSUWidget.close()
                #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
                #kicadStepUptools.KSUWidget.destroy()
                #for i in QtGui.qApp.topLevelWidgets():
                #    if i.objectName() == "kicadStepUp":
                #        i.deleteLater()
                kicadStepUptools.KSUWidget.close()
            except:
                ksu_present=False
                expVRML.say("ksu not present")
        else:
            kicadStepUptools.KSUWidget.close()
            reload_lib(kicadStepUptools)
            kicadStepUptools.KSUWidget.close()
            #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
            #kicadStepUptools.KSUWidget.destroy()

    #FreeCADGui.insert(u"C:\Temp\FCAD_sg\QFN_packages\QFN-12-1EP_3x3mm_Pitch0_5mm.kicad_mod")
    #FreeCADGui.insert(script_dir+os.sep+"ModelName.kicad_mod")
    if save_memory == False:
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewBottom()
        #Gui.activeDocument().activeView().viewAxometric()
    saveFCdoc(App, Gui, doc, ModelName,out_dir)

    if save_memory == True or check_Model==True:
        doc=FreeCAD.ActiveDocument
        print("closing: {}".format(doc.Name))
        FreeCAD.closeDocument(doc.Name)

    if check_Model==True:
        step_path = out_dir + '/' + ModelName + ".step"
        runGeometryCheck(App, Gui, step_path,
            log, ModelName, save_memory=save_memory)

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
        FreeCAD.Console.PrintMessage('No variant name is given! building BGA-48_6x8_8.0x9.0mm_Pitch0.8mm')
        model_to_build='BGA-48_6x8_8.0x9.0mm_Pitch0.8mm'
    else:
        model_to_build=sys.argv[2]
        if len(sys.argv)==4:
            FreeCAD.Console.PrintMessage(sys.argv[3]+'\r\n')
            if (sys.argv[3].find('no-pinmark-color')!=-1):
                color_pin_mark=False
            else:
                color_pin_mark=True

    save_memory=False #reducing memory consuming for all generation params
    if model_to_build == "all":
        variants = all_params.keys()
        save_memory=True
    else:
        variants = [model_to_build]
    with open(check_log_file, 'w') as log:
        for variant in variants:
            if not variant in all_params:
                print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
                continue
            params = all_params[variant]
            try:
                generateOneModel(params, log)
            except GeometryError as e:
                e.print_errors(stop_on_first_error)
                if stop_on_first_error:
                    break
            except FreeCADVersionError as e:
                FreeCAD.Console.PrintError(e)
                break
            except: #previously "else" was causing exception to be raised "[No active exception to reraise]" at the end of script running
                #traceback.print_exc()
                raise
                
    FreeCAD.Console.PrintMessage("\nDone\n")

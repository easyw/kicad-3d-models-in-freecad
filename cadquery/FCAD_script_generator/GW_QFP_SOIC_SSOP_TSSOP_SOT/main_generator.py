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

__title__ = "make GullWings ICs 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make GullWings ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.9 14/02/2017"

# thanks to Frank Severinsen Shack for including vrml materials

save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'
global_3dpath = '../_3Dmodels/'
color_pin_mark=True
place_pinMark=True
no_export = False

max_cc1 = 1

from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import traceback

import datetime
from datetime import datetime
sys.path.append("../_tools")
sys.path.append("./")
import exportPartToVRML as expVRML
import shaderColors

import re, fnmatch

# maui start
import ImportGui
#from Gui.Command import *

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
try:
    # Gui.SendMsgToActiveView("Run")
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
    # maui end

import add_license as Lic
# Import cad_tools
from cqToolsExceptions import *
import cq_cad_tools
# Reload tools
#reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements, runGeometryCheck

#checking requirements
checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print("CQ 030 doesn't open example file")

def make_gw(params):
    c  = params.c
    the  = params.the
    tb_s  = params.tb_s
    ef  = params.ef
    cc1 = params.cc1
    fp_s = params.fp_s
    fp_r  = params.fp_r
    fp_d  = params.fp_d
    fp_z  = params.fp_z
    R1  = params.R1
    R2  = params.R2
    S  = params.S
# automatically calculated    L  = params.L
    D1  = params.D1
    E1  = params.E1
    E   = params.E
    A1  = params.A1
    A2  = params.A2
    b   = params.b
    e   = params.e
    npx = params.npx
    npy = params.npy
    mN  = params.modelName
    rot = params.rotation

    if params.excluded_pins:
        excluded_pins = params.excluded_pins
    else:
        excluded_pins=() ##no pin excluded

    A = A1 + A2
    A2_t = (A2-c)/2 # body top part height
    A2_b = A2_t     # body bottom part height
    D1_b = D1-2*tan(radians(the))*A2_b # bottom width
    E1_b = E1-2*tan(radians(the))*A2_b # bottom length
    D1_t1 = D1-tb_s # top part bottom width
    E1_t1 = E1-tb_s # top part bottom length
    D1_t2 = D1_t1-2*tan(radians(the))*A2_t # top part upper width
    E1_t2 = E1_t1-2*tan(radians(the))*A2_t # top part upper length

    epad_rotation = 0.0
    epad_offset_x = 0.0
    epad_offset_y = 0.0

    if params.epad:
        #if isinstance(params.epad, float):
        if not isinstance(params.epad, tuple):
            sq_epad = False
            epad_r = params.epad
        else:
            sq_epad = True
            D2 = params.epad[0]
            E2 = params.epad[1]
            if len(params.epad) > 2:
                epad_rotation = params.epad[2]
            if len(params.epad) > 3:
                if isinstance (params.epad[3], str):
                    if params.epad[3] == '-topin':
                        epad_offset_x = (D1_b/2-D2/2) * -1
                    elif params.epad[3] == '+topin':
                        epad_offset_x = D1_b/2-D2/2
                else:
                    epad_offset_x = params.epad[3]
            if len(params.epad) > 4:
                if isinstance (params.epad[4], str):
                    if params.epad[4] == '-topin':
                        epad_offset_y = (E1_b/2-E2/2) * -1
                    elif params.epad[4] == '+topin':
                        epad_offset_y = E1_b/2-E2/2
                else:
                    epad_offset_y = params.epad[4]

    # calculated dimensions for body
    # checking pin lenght compared to overall width
    # d=(E-E1 -2*(S+L)-2*(R1))
    L=(E-E1-2*(S+R1))/2
    #FreeCAD.Console.PrintMessage('E='+str(E)+';E1='+str(E1)+';S='+str(S)+';L='+str(L)+'\r\n')

    # calculate chamfers
    totpinwidthx = (npx-1)*e+b # total width of all pins on the X side
    totpinwidthy = (npy-1)*e+b # total width of all pins on the Y side

    if cc1!=0:
        cc1 = abs(min((D1-totpinwidthx)/2., (E1-totpinwidthy)/2.,cc1) - 0.5*tb_s)
        cc1 = min(cc1, max_cc1)
    # cc = cc1/2.
    cc=cc1

    def crect(wp, rw, rh, cv1, cv):
        """
        Creates a rectangle with chamfered corners.
        wp: workplane object
        rw: rectangle width
        rh: rectangle height
        cv1: chamfer value for 1st corner (lower left)
        cv: chamfer value for other corners
        """
        points = [
        #    (-rw/2., -rh/2.+cv1),
            (-rw/2., rh/2.-cv),
            (-rw/2.+cv, rh/2.),
            (rw/2.-cv, rh/2.),
            (rw/2., rh/2.-cv),
            (rw/2., -rh/2.+cv),
            (rw/2.-cv, -rh/2.),
            (-rw/2.+cv1, -rh/2.),
            (-rw/2., -rh/2.+cv1)
        ]
        #return wp.polyline(points)
        return wp.polyline(points).wire() #, forConstruction=True)

    if cc1!=0:
        case = cq.Workplane(cq.Plane.XY()).workplane(offset=A1).moveTo(-D1_b/2., -E1_b/2.+(cc1-(D1-D1_b)/4.))
        case = crect(case, D1_b, E1_b, cc1-(D1-D1_b)/4., cc-(D1-D1_b)/4.)  # bottom edges
        #show(case)
        case = case.pushPoints([(0,0)]).workplane(offset=A2_b).moveTo(-D1/2, -E1/2+cc1)
        case = crect(case, D1, E1, cc1, cc)     # center (lower) outer edges
        #show(case)
        case = case.pushPoints([(0,0)]).workplane(offset=c).moveTo(-D1/2,-E1/2+cc1)
        case = crect(case, D1,E1,cc1, cc)       # center (upper) outer edges
        #show(case)
        #case=cq.Workplane(cq.Plane.XY()).workplane(offset=c).moveTo(-D1_t1/2,-E1_t1/2+cc1-(D1-D1_t1)/4.)
        case=case.pushPoints([(0,0)]).workplane(offset=0).moveTo(-D1_t1/2,-E1_t1/2+cc1-(D1-D1_t1)/4.)
        case = crect(case, D1_t1,E1_t1, cc1-(D1-D1_t1)/4., cc-(D1-D1_t1)/4.) # center (upper) inner edges
        #show(case)
        #stop
        cc1_t = cc1-(D1-D1_t2)/4. # this one is defined because we use it later
        case = case.pushPoints([(0,0)]).workplane(offset=A2_t).moveTo(-D1_t2/2,-E1_t2/2+cc1_t)
        #cc1_t = cc1-(D1-D1_t2)/4. # this one is defined because we use it later
        case = crect(case, D1_t2,E1_t2, cc1_t, cc-(D1-D1_t2)/4.) # top edges
        #show(case)
        case = case.loft(ruled=True)
        if ef!=0:
            try:
                case = case.faces(">Z").fillet(ef)
            except Exception as exeption:
                FreeCAD.Console.PrintError("Case top face failed failed.\n")
                FreeCAD.Console.PrintError('{:s}\n'.format(exeption))


    else:
        case = cq.Workplane(cq.Plane.XY()).workplane(offset=A1).rect(D1_b, E1_b). \
            workplane(offset=A2_b).rect(D1, E1).workplane(offset=c).rect(D1,E1). \
            rect(D1_t1,E1_t1).workplane(offset=A2_t).rect(D1_t2,E1_t2). \
            loft(ruled=True)
        if ef!=0:
            try:
                case = case.faces(">Z").fillet(ef)
            except Exception as exeption:
                FreeCAD.Console.PrintError("Case top face failed failed.\n")
                FreeCAD.Console.PrintError('{:s}\n'.format(exeption))



        # fillet the corners
        if ef!=0:
            BS = cq.selectors.BoxSelector
            try:
                case = case.edges(BS((D1_t2/2, E1_t2/2, 0), (D1/2+0.1, E1/2+0.1, A2))).fillet(ef)
            except Exception as exeption:
                FreeCAD.Console.PrintError("Case fillet 1 failed\n")
                FreeCAD.Console.PrintError('{:s}\n'.format(exeption))

            try:
                case = case.edges(BS((-D1_t2/2, E1_t2/2, 0), (-D1/2-0.1, E1/2+0.1, A2))).fillet(ef)
            except Exception as exeption:
                FreeCAD.Console.PrintError("Case fillet 2 failed\n")
                FreeCAD.Console.PrintError('{:s}\n'.format(exeption))

            try:
                case = case.edges(BS((-D1_t2/2, -E1_t2/2, 0), (-D1/2-0.1, -E1/2-0.1, A2))).fillet(ef)
            except Exception as exeption:
                FreeCAD.Console.PrintError("Case fillet 3 failed\n")
                FreeCAD.Console.PrintError('{:s}\n'.format(exeption))

            try:
                case = case.edges(BS((D1_t2/2, -E1_t2/2, 0), (D1/2+0.1, -E1/2-0.1, A2))).fillet(ef)
            except Exception as exeption:
                FreeCAD.Console.PrintError("Case fillet 4 failed\n")
                FreeCAD.Console.PrintError('{:s}\n'.format(exeption))

    #fp_s = True
    if fp_r == 0:
            global place_pinMark
            place_pinMark=False
            fp_r = 0.1
    if fp_s == False:
        pinmark = cq.Workplane(cq.Plane.XY()).workplane(offset=A).box(fp_r, E1_t2-fp_d, fp_z*2) #.translate((E1/2,0,A1)).rotate((0,0,0), (0,0,1), 90)
        #translate the object
        pinmark=pinmark.translate((-D1_t2/2+fp_r/2.+fp_d/2,0,0)) #.rotate((0,0,0), (0,1,0), 0)
    else:
        # first pin indicator is created with a spherical pocket

        sphere_r = (fp_r*fp_r/2 + fp_z*fp_z) / (2*fp_z)
        sphere_z = A + sphere_r * 2 - fp_z - sphere_r
        # Revolve a cylinder from a rectangle
        # Switch comments around in this section to try the revolve operation with different parameters
        ##cylinder =
        #pinmark=cq.Workplane("XZ", (-D1_t2/2+fp_d+fp_r, -E1_t2/2+fp_d+fp_r, A)).rect(sphere_r/2, -fp_z, False).revolve()
        pinmark=cq.Workplane("XZ", (-D1_t2/2+fp_d+fp_r, -E1_t2/2+fp_d+fp_r, A)).rect(fp_r/2, -fp_z, False).revolve()

    if (color_pin_mark==False) and (place_pinMark==True):
        case = case.cut(pinmark)

    # calculated dimensions for pin
    R1_o = R1+c # pin upper corner, outer radius
    R2_o = R2+c # pin lower corner, outer radius

    # Create a pin object at the center of top side.
    bpin = cq.Workplane("YZ", (0,E1/2,0,)). \
        moveTo(-tb_s, A1+A2_b). \
        line(S+tb_s, 0). \
        threePointArc((S+R1/sqrt(2), A1+A2_b-R1*(1-1/sqrt(2))),
                      (S+R1, A1+A2_b-R1)). \
        line(0, -(A1+A2_b-R1-R2_o)). \
        threePointArc((S+R1+R2_o*(1-1/sqrt(2)), R2_o*(1-1/sqrt(2))),
                      (S+R1+R2_o, 0)). \
        line(L-R2_o, 0). \
        line(0, c). \
        line(-(L-R2_o), 0). \
        threePointArc((S+R1+R2_o-R2/sqrt(2), c+R2*(1-1/sqrt(2))),
                      (S+R1+R2_o-R1, c+R2)). \
        lineTo(S+R1+c, A1+A2_b-R1). \
        threePointArc((S+R1_o/sqrt(2), A1+A2_b+c-R1_o*(1-1/sqrt(2))),
                      (S, A1+A2_b+c)). \
        line(-S-tb_s, 0).close().extrude(b).translate((-b/2,0,0))

    pins = []
    pincounter = 1
    first_pos_x = (npx-1)*e/2
    for i in range(npx):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_x-i*e, 0, 0)).\
                rotate((0,0,0), (0,0,1), 180)
            pins.append(pin)
        pincounter += 1

    first_pos_y = (npy-1)*e/2
    for i in range(npy):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_y-i*e, (D1-E1)/2, 0)).\
                rotate((0,0,0), (0,0,1), 270)
            pins.append(pin)
        pincounter += 1

    for i in range(npx):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_x-i*e, 0, 0))
            pins.append(pin)
        pincounter += 1

    for i in range(npy):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_y-i*e, (D1-E1)/2, 0)).\
                rotate((0,0,0), (0,0,1), 90)
            pins.append(pin)
        pincounter += 1

    # create exposed thermal pad if requested
    if params.epad:
        if sq_epad:
            pins.append(cq.Workplane("XY").box(D2, E2, A1).translate((epad_offset_x,epad_offset_y,A1/2)).rotate((0,0,0), (0,0,1), epad_rotation))
        else:
            #epad = cq.Workplane("XY", (0,0,A1/2)). \
            epad = cq.Workplane("XY"). \
            circle(epad_r). \
            extrude(A1)#.translate((0,0,A1/2))
            #extrude(A1+A1/10)
            pins.append(epad)
    # merge all pins to a single object
    merged_pins = pins[0]
    for p in pins[1:]:
        merged_pins = merged_pins.union(p)
    pins = merged_pins

    # extract pins from case
    case = case.cut(pins)

    return (case, pins, pinmark)

def export_one_part(params, series_definition, log):
    ModelName = params.modelName
    footprint_dir = series_definition.footprint_dir
    CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')

    print('\n######################### {:s} ###########################\n'.format(ModelName))

    Newdoc = App.newDocument(CheckedModelName)
    App.setActiveDocument(CheckedModelName)
    App.ActiveDocument=App.getDocument(CheckedModelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedModelName)

    color_keys = [
        series_definition.body_color_key,
        series_definition.pins_color_key,
        series_definition.mark_color_key
    ]
    colors = [shaderColors.named_colors[key].getDiffuseInt() for key in color_keys]

    body, pins, mark = make_gw(params)

    show(body, colors[0]+(0,))
    show(pins, colors[1]+(0,))
    show(mark, colors[2]+(0,))

    doc = FreeCAD.ActiveDocument
    objs = GetListOfObjects(FreeCAD, doc)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
    material_substitutions={
        col_body[:-1]:series_definition.body_color_key,
        col_pin[:-1]:series_definition.pins_color_key,
        col_mark[:-1]:series_definition.mark_color_key
    }

    if (color_pin_mark==True) and (place_pinMark==True):
        CutObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[2].Name)
    else:
        #removing pinMark
        App.getDocument(doc.Name).removeObject(objs[2].Name)

    objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
    doc.Label=CheckedModelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=CheckedModelName

    restore_Main_Tools()
    #rotate if required
    if (params.rotation!=0):
        rot= params.rotation
        z_RotateObject(doc, rot)

    if no_export:
        return

    out_dir='{:s}{:s}.3dshapes'.format(global_3dpath, series_definition.lib_name)

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
    # Save the doc in Native FC format
    footprint_dir = series_definition.footprint_dir
    if footprint_dir is not None and os.path.isdir(footprint_dir) \
            and not save_memory and not check_Model:
        #expVRML.say (ModelName)
        #stop
        sys.argv = ["fc", "dummy", footprint_dir+os.sep+ModelName, "savememory"]
        #setup = get_setup_file()  # << You need the parentheses
        expVRML.say(sys.argv[2])
        ksu_already_loaded=False
        ksu_present=False
        for i in QtGui.qApp.topLevelWidgets():
            if i.objectName() == "kicadStepUp":
                ksu_already_loaded=True
        ksu_tab = FreeCADGui.getMainWindow().findChild(QtGui.QDockWidget, "kicadStepUp") #"kicad StepUp 3D tools")
        if ksu_tab:
            ksu_already_loaded=True
        if ksu_already_loaded!=True:
            try:
                import kicadStepUptools
                ksu_present=True
                ksu_already_loaded=True
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
            reload(kicadStepUptools)
            kicadStepUptools.KSUWidget.close()
            #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
            #kicadStepUptools.KSUWidget.destroy()

    saveFCdoc(App, Gui, doc, ModelName,out_dir)

    #FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.activeDocument().activeView().viewAxometric()

    if save_memory == True or check_Model==True:
        doc=FreeCAD.ActiveDocument
        FreeCAD.closeDocument(doc.Name)

    if check_Model==True:
        runGeometryCheck(App, Gui, out_dir+'/'+ ModelName+".step",
            log, ModelName, save_memory=save_memory)

def exportSeries(module, log, model_filter_regobj):
    series_definition = module.SeriesParams
    for variant in module.part_params:
        params = module.part_params[variant]
        try:
            if model_filter_regobj.match(params.modelName):
                export_one_part(params, series_definition, log)
        except GeometryError as e:
            e.print_errors(stop_on_first_error)
            if stop_on_first_error:
                return -1
        except FreeCADVersionError as e:
            FreeCAD.Console.PrintError(e)
            return -1
    return 0


#########################  ADD MODEL GENERATORS #########################

import cq_parameters_diode
import cq_parameters_qfp
import cq_parameters_qfp_maui
import cq_parameters_soic
import cq_parameters_soic_maui
import cq_parameters_sot
import cq_parameters_sot_maui
import cq_parameters_ssop
import cq_parameters_ssop_maui
import cq_parameters_tssop
import cq_parameters_tssop_maui

all_series = {
    'diode':cq_parameters_diode,
    'qfp':cq_parameters_qfp,
    'qfp_maui':cq_parameters_qfp_maui,
    'soic':cq_parameters_soic,
    'soic_maui':cq_parameters_soic_maui,
    'sot':cq_parameters_sot,
    'sot_maui':cq_parameters_sot_maui,
    'ssop':cq_parameters_ssop,
    'ssop_maui':cq_parameters_ssop_maui,
    'tssop':cq_parameters_tssop,
    'tssop_maui':cq_parameters_tssop_maui,
}

#########################################################################


class argparse():
    def __init__(self):
        self.config = '../_tools/config/connector_config_KLCv3.yaml'
        self.model_filter = '*'
        self.series = list(all_series.values())

    def parse_args(self, args):
        for arg in args:
            if '=' in arg:
                self.parseValueArg(*arg.split('='))
            else:
                self.argSwitchArg(arg)

    def parseValueArg(self, name, value):
        if name == 'model_filter':
            self.model_filter = value
        elif name == 'log':
            global check_log_file
            check_log_file = value
        elif name == 'series':
            #print("param series:")
            #print(value)
            series_str = value.split(',')
            self.series = []
            for s in series_str:
                if s.lower() in all_series:
                    self.series.append(all_series[s.lower()])

    def argSwitchArg(self, name):
        if name == '?':
            self.print_usage()
            exit()
        elif name == 'disable_check':
            global check_Model
            check_Model = False
        elif name == 'disable_Memory_reduction':
            global save_memory
            save_memory = False
        elif name == 'error_tolerant':
            global stop_on_first_error
            stop_on_first_error = False
        elif name == 'disable_marker_color':
            global color_pin_mark
            color_pin_mark = False
        elif name == 'no_export':
            global no_export
            no_export = True

    def print_usage(self):
        print("\nGenerater script for gull wing type packages 3d models.")
        print('usage: FreeCAD main_generator.py [optional arguments and switches]')
        print('optional arguments:')
        print('\tmodel_filter=[filter pincount using linux file filter syntax]')
        print('\tlog=[log file path]')
        print('\tseries=[series name],[series name],...')
        print('switches:')
        print('\tdisable_check')
        print('\tdisable_Memory_reduction')
        print('\terror_tolerant')
        print('\tdisable_marker_color\n')

    def __str__(self):
        return 'config:{:s}, filter:{:s}, series:{:s}, with_plug:{:d}'.format(
            self.config, self.model_filter, str(self.series), self.with_plug)


# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":
    args = argparse()
    args.parse_args(sys.argv)
    modelfilter = args.model_filter

    model_filter_regobj=re.compile(fnmatch.translate(modelfilter))

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')
    with open(check_log_file, 'w') as log:
        log.write('# Check report for gull wing packages 3d model genration\n')
        for typ in args.series:
            try:
                if exportSeries(typ, log, model_filter_regobj) != 0:
                    break
            except Exception as exeption:
                traceback.print_exc()
                break

    FreeCAD.Console.PrintMessage('\n\nDone\n')

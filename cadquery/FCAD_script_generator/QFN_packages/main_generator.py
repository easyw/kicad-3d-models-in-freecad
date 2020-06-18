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
## e.g. c:\freecad\bin\freecad main_generator.py QFN-28-1EP_6x6mm_Pitch0.65mm

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

__title__ = "make QFN ICs 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make QFN ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.6 18/06/2020"

###ToDo: QFN with ARC pad, exposed pad with chamfer

# maui import cadquery as cq
# maui from Helpers import show
import math
from math import tan, radians, sqrt
try:
    from math import isclose
except ImportError:
    def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
        '''
        Python 2 implementation of Python 3.5 math.isclose()
        https://hg.python.org/cpython/file/tip/Modules/mathmodule.c#l1993
        '''
        # sanity check on the inputs
        if rel_tol < 0 or abs_tol < 0:
            raise ValueError("tolerances must be non-negative")

        # short circuit exact equality -- needed to catch two infinities of
        # the same sign. And perhaps speeds things up a bit sometimes.
        if a == b:
            return True

        # This catches the case of two infinities of opposite sign, or
        # one infinity and one finite number. Two infinities of opposite
        # sign would otherwise have an infinite relative tolerance.
        # Two infinities of the same sign are caught by the equality check
        # above.
        if math.isinf(a) or math.isinf(b):
            return False

        # now do the regular computation
        # this is essentially the "weak" test from the Boost library
        diff = math.fabs(b - a)
        result = (((diff <= math.fabs(rel_tol * b)) or
                   (diff <= math.fabs(rel_tol * a))) or
                  (diff <= abs_tol))
        return result

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
import cq_cad_tools
# Reload tools
from cq_cad_tools import reload_lib
reload_lib(cq_cad_tools)

# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements, SimpleCopy_wColors

try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
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

import cq_parameters  # modules parameters
from cq_parameters import *

footprints_dir_diodes=None
import cq_parameters_diode  # modules parameters
from cq_parameters_diode import *

#   all_params= all_params_qfn
all_params= kicad_naming_params_qfn.copy()
all_params.update(kicad_naming_params_diode)

def make_qfn(params):

    c  = params.c
    ef  = params.ef
    cce = params.cce
    fp_s = params.fp_s
    fp_r  = params.fp_r
    fp_d  = params.fp_d
    fp_z  = params.fp_z
#    K  = params.K
    L  = params.L
    D  = params.D
    E   = params.E
    A1  = params.A1
    A2  = params.A2
    b   = params.b
    e   = params.e
    m   = params.m
    ps  = params.ps
    npx = params.npx
    npy = params.npy
    mN  = params.modelName
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix
    pin_shapes = params.pin_shapes
    if params.excluded_pins:
        excluded_pins = params.excluded_pins
    else:
        excluded_pins=() ##no pin excluded 

    if isclose(A1, 0.0):
        print("A1 can NOT be zero (or this script will fail). Setting A1 to 0.02")
        A1 = 0.02

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
                        epad_offset_x = (D/2-D2/2) * -1
                    elif params.epad[3] == '+topin':
                        epad_offset_x = D/2-D2/2
                else:
                    epad_offset_x = params.epad[3]
            if len(params.epad) > 4:
                if isinstance (params.epad[4], str):
                    if params.epad[4] == '-topin':
                        epad_offset_y = (E/2-E2/2) * -1
                    elif params.epad[4] == '+topin':
                        epad_offset_y = E/2-E2/2
                else:
                    epad_offset_y = params.epad[4]
            if params.epad_offsetX is not None:
                 epad_offset_x += params.epad_offsetX
            if params.epad_offsetY is not None:
                 epad_offset_y += params.epad_offsetY
                    
    A = A1 + A2


    if m == 0:
        case = cq.Workplane("XY").box(D-A1, E-A1, A2)  #margin to see fused pins
    else:
        case = cq.Workplane("XY").box(D, E, A2)  #NO margin, pins don't emerge
    if ef!=0:
        case.edges("|X").fillet(ef)
        case.edges("|Z").fillet(ef)
    #translate the object
    case=case.translate((0,0,A2/2+A1)).rotate((0,0,0), (0,0,1), 0)

    # first pin indicator is created with a spherical pocket
    if (fp_d is not None):
        fp_dx = fp_d
        fp_dy = fp_d
    else:
        if params.fp_dx is not None:
            fp_dx = params.fp_dx
        else:
            fp_dx = 0
        if params.fp_dy is not None:
            fp_dy = params.fp_dy
        else:
            fp_dy = 0

    if ps == 'concave' or ps == 'cshaped':
        if npy != 0:
            fp_dx = fp_d+L-A1/2
        if npx != 0:
            fp_dy = fp_d+L-A1/2
    if fp_r == 0:
        global place_pinMark
        place_pinMark=False
        fp_r = 0.1
    if fp_s == False:
        pinmark = cq.Workplane(cq.Plane.XY()).workplane(offset=A).box(fp_r, E-fp_dy*2, fp_z*2) #.translate((E1/2,0,A1)).rotate((0,0,0), (0,0,1), 90)
        #translate the object  
        pinmark=pinmark.translate((-D/2+fp_r/2+fp_dx,0,0)) #.rotate((0,0,0), (0,1,0), 0)
    else:
        sphere_r = (fp_r*fp_r/2 + fp_z*fp_z) / (2*fp_z)
        sphere_z = A + sphere_r * 2 - fp_z - sphere_r
    
        pinmark=cq.Workplane("XZ", (-D/2+fp_dx+fp_r, -E/2+fp_dy+fp_r, fp_z)).rect(fp_r/2, -2*fp_z, False).revolve().translate((0,0,A))#+fp_z))

    #stop
    if (color_pin_mark==False) and (place_pinMark==True):
        case = case.cut(pinmark)
    #stop
    if ps == 'square': #square pins
        bpin = cq.Workplane("XY"). \
            moveTo(b, 0). \
            lineTo(b, L). \
            lineTo(0, L). \
            lineTo(0, 0). \
            close().extrude(c).translate((b/2,E/2,0)). \
            rotate((b/2,E/2,A1/2), (0,0,1), 180)
            #close().extrude(c).translate((b/2,E/2,A1/2))
    elif ps == 'rounded':
        bpin = cq.Workplane("XY"). \
            moveTo(b, 0). \
            lineTo(b, L-b/2). \
            threePointArc((b/2,L),(0, L-b/2)). \
            lineTo(0, 0). \
            close().extrude(c).translate((b/2,E/2,0)). \
            rotate((b/2,E/2,A1/2), (0,0,1), 180)            
            #close().extrude(c).translate((b/2,E/2,A1/2))
    elif ps == 'concave':
        pincut = cq.Workplane("XY").box(b, L, A2+A1*2).translate((0,E/2-L/2,A2/2+A1))
        bpin = cq.Workplane("XY").box(b, L, A2+A1*2).translate((0,E/2-L/2,A2/2+A1)).edges("|X").fillet(A1)
        bpin = bpin.faces(">Z").edges(">Y").workplane().circle(b*0.3).cutThruAll()
    elif ps == 'cshaped':
        bpin = cq.Workplane("XY").box(b, L, A2+A1*2).translate((0,E/2-L/2,A2/2+A1)).edges("|X").fillet(A1)
    
    pins = []
    pincounter = 1
    if ps == 'custom':
        for pin_shape in pin_shapes:
            first_point = pin_shape[0]
            pin = cq.Workplane("XY"). \
                moveTo(first_point[0], first_point[1])
            for i in range(1, len(pin_shape)):
                point = pin_shape[i]
                pin = pin.lineTo(point[0], point[1])
            pin = pin.close().extrude(c)
            pins.append(pin)
        pincounter += 1
    else:
        # create top, bottom side pins
        first_pos_x = (npx-1)*e/2
        for i in range(npx):
            if pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_x-i*e, -m, 0)). \
                rotate((0,0,0), (0,0,1), 180)
                pins.append(pin)
                if ps == 'concave':
                    pinsubtract = pincut.translate((first_pos_x-i*e, -m, 0)). \
                    rotate((0,0,0), (0,0,1), 180)
                    case = case.cut(pinsubtract)

        pincounter += 1
    
        first_pos_y = (npy-1)*e/2
        for i in range(npy):
            if pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_y-i*e, (D-E)/2-m, 0)).\
                rotate((0,0,0), (0,0,1), 270)
                pins.append(pin)
                if ps == 'concave':
                    pinsubtract = pincut.translate((first_pos_y-i*e, (D-E)/2-m, 0)).\
                    rotate((0,0,0), (0,0,1), 270)
                    case = case.cut(pinsubtract)
            pincounter += 1

        for i in range(npx):
            if pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_x-i*e, -m, 0))
                pins.append(pin)
                if ps == 'concave':
                    pinsubtract = pincut.translate((first_pos_x-i*e, -m, 0))
                    case = case.cut(pinsubtract)
            pincounter += 1
        
        for i in range(npy):
            if pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_y-i*e, (D-E)/2-m, 0)).\
                rotate((0,0,0), (0,0,1), 90)
                pins.append(pin)
                if ps == 'concave':
                    pinsubtract = pincut.translate((first_pos_y-i*e, (D-E)/2-m, 0)).\
                    rotate((0,0,0), (0,0,1), 90)
                    case = case.cut(pinsubtract)
            pincounter += 1

    # create exposed thermal pad if requested
    if params.epad:
        if sq_epad:
            if params.epad_n is not None and \
               params.epad_pitch is not None:
                for nx in range(1,params.epad_n[0]+1):
                    for ny in range(1,params.epad_n[1]+1):
                        offset_x = -((params.epad_n[0]-1)*params.epad_pitch[0])/2+(nx-1)*params.epad_pitch[0]
                        offset_y = -((params.epad_n[1]-1)*params.epad_pitch[1])/2+(ny-1)*params.epad_pitch[1]
                        epad = cq.Workplane("XY").\
                        moveTo(-D2/2+cce, -E2/2). \
                        lineTo(D2/2, -E2/2). \
                        lineTo(D2/2, E2/2). \
                        lineTo(-D2/2, E2/2). \
                        lineTo(-D2/2, -E2/2+cce). \
                        close().extrude(A1+A1/2). \
                        translate((epad_offset_x+offset_x,epad_offset_y+offset_y,0)). \
                        rotate((0,0,0), (0,0,1), epad_rotation) #+A1/2).translate((0,0,A1/2))
                        #close().extrude(A1+A1/10)
                        pins.append(epad)
            else:
                #pins.append(cq.Workplane("XY").box(D2, E2, A1+A1/10).translate((0,0,A1+A1/10)))
                #epad = cq.Workplane("XY", (0,0,A1/2)). \
                epad = cq.Workplane("XY").\
                moveTo(-D2/2+cce, -E2/2). \
                lineTo(D2/2, -E2/2). \
                lineTo(D2/2, E2/2). \
                lineTo(-D2/2, E2/2). \
                lineTo(-D2/2, -E2/2+cce). \
                close().extrude(A1+A1/2). \
                translate((epad_offset_x,epad_offset_y,0)). \
                rotate((0,0,0), (0,0,1), epad_rotation) #+A1/2).translate((0,0,A1/2))
                #close().extrude(A1+A1/10)
                pins.append(epad)
        else:
            if params.epad_n is not None and \
               params.epad_pitch is not None:
                for nx in range(1,params.epad_n[0]):
                    for ny in range(1,params.epad_n[1]):
                        offset_x = -((params.epad_n[0]-1)*params.epad_pitch[0])/2+(nx-1)*params.epad_pitch[0]
                        offset_y = -((params.epad_n[1]-1)*params.epad_pitch[1])/2+(ny-1)*params.epad_pitch[1]
                        epad = cq.Workplane("XY").\
                        circle(epad_r). \
                        extrude(A1). \
                        translate((offset_x,offset_y,A1/2))
                        pins.append(epad)
            else:
                #pins.append(cq.Workplane("XY").box(D2, E2, A1+A1/10).translate((0,0,A1+A1/10)))
                #epad = cq.Workplane("XY", (0,0,A1/2)). \
                epad = cq.Workplane("XY").\
                circle(epad_r). \
                extrude(A1) #+A1/2).translate((0,0,A1/2))
                #extrude(A1+A1/2).translate((0,0,A1/2))
                pins.append(epad)

    # merge all pins to a single object
    merged_pins = pins[0]
    for p in pins[1:]:
        merged_pins = merged_pins.union(p)
    pins = merged_pins

    #show(pins)
    #sleep
    # extract pins from case
    case = case.cut(pins)

    return (case, pins, pinmark)

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
        FreeCAD.Console.PrintMessage('No variant name is given! building QFN-28-1EP_6x6mm_Pitch0.65mm')
        model_to_build='QFN-28-1EP_6x6mm_Pitch0.65mm'
    else:
        model_to_build=sys.argv[2]
        if len(sys.argv)==4:
            FreeCAD.Console.PrintMessage(sys.argv[3]+'\r\n')
            if (sys.argv[3].find('no-pinmark-color')!=-1):
                color_pin_mark=False
            else:
                color_pin_mark=True

    if model_to_build == "all":
        expVRML.sayerr("'all' is not supported for this families\nuse 'allQFN' or allDiodes instead")
    elif model_to_build == "allQFN":
        variants = kicad_naming_params_qfn.keys() 
        save_memory=True
    elif model_to_build == "allDiodes":
        variants = kicad_naming_params_diode.keys()  
        footprints_dir=footprints_dir_diodes
        save_memory=True
    else:
        variants = [model_to_build]

    for variant in variants:
        excluded_pins_x=() ##no pin excluded
        excluded_pins_xmirror=() ##no pin excluded
        place_pinMark=True ##default =True used to exclude pin mark to build sot23-3; sot23-5; sc70 (asimmetrical pins, no pinmark)

        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        case, pins, pinmark = make_qfn(all_params[variant])

        show(case)
        show(pins)
        show(pinmark)
        #stop
        
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)

        if (all_params[variant].body_color_key is not None):
            body_color_key = all_params[variant].body_color_key
            body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()

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
        expVRML.say(material_substitutions)
        ## objs[0].Label='body'
        ## objs[1].Label='pins'
        ## objs[2].Label='mark'
        ###
        ## print objs[0].Name, objs[1].Name, objs[2].Name

        ## sleep
        #if place_pinMark==True:
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
        FreeCAD.ActiveDocument.recompute()
        doc.Label=CheckedModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label=CheckedModelName
        restore_Main_Tools()
        #rotate if required
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
            z_RotateObject(doc, rot)
        #out_dir=destination_dir+all_params[variant].dest_dir_prefix+'/'
        script_dir=os.path.dirname(os.path.realpath(__file__))
        #models_dir=script_dir+"/../_3Dmodels"
        expVRML.say(models_dir)
        if len(all_params[variant].dest_dir_prefix)>=1:
            out_dir=models_dir+destination_dir+os.sep+all_params[variant].dest_dir_prefix
        else:
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
        #expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox
        #FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        #Gui.activeDocument().activeView().viewBottom()
        Gui.activeDocument().activeView().viewAxometric()

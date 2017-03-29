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

___ver___ = "1.0.5 25/Feb/2017"

###ToDo: QFN with ARC pad, exposed pad with chamfer

# maui import cadquery as cq
# maui from Helpers import show
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
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

try:
    # Gui.SendMsgToActiveView("Run")
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


import cq_parameters_molded  # modules parameters
from cq_parameters_molded import *

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

def poline(points, plane):
    sp = points.pop()
    plane=plane.moveTo(sp[0],sp[1])
    plane=plane.polyline(points)
    return plane
##

def make_qfn(params):

    c  = params.c
    ef  = params.ef
    cce = params.cce
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
    sq  = params.sq
    npx = params.npx
    npy = params.npy
    mN  = params.modelName
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix
    if params.excluded_pins:
        excluded_pins = params.excluded_pins
    else:
        excluded_pins=() ##no pin excluded 

    if params.epad:
        #if isinstance(params.epad, float):
        if not isinstance(params.epad, tuple):
            sq_epad = False
            epad_r = params.epad
        else:
            sq_epad = True
            D2 = params.epad[0]
            E2 = params.epad[1]

    A = A1 + A2

    the=12
    D1=D*(1-0.0625)
    E1=E*(1-0.0625)

    D1_t = D1-2*tan(radians(the))*(A-c)
    E1_t = E1-2*tan(radians(the))*(A-c)
    # draw the case
    cw = D-A1*2
    cl = E-A1*2
    case_bot = cq.Workplane("XY").workplane(offset=0)
    case_bot= make_plg(case_bot, cw, cl, cce, cce)
    case_bot = case_bot.extrude(c-A1-0.01)
    case_bot = case_bot.translate((0,0,A1))
    ##show(case_bot)
        
    case = cq.Workplane("XY").workplane(offset=A1)
    #case = make_plg(case, cw, cl, cce, cce)
    case = make_plg(case, D1, E1, cce, cce)
    #case = case.extrude(c-A1)
    case = case.extrude(0.01)
    case = case.faces(">Z").workplane()
    case = make_plg(case, D1, E1, cce, cce).\
        workplane(offset=A-c)
    case = make_plg(case, D1_t, E1_t, cce, cce).\
        loft(ruled=True)
    # fillet the bottom vertical edges
    ef=0.1
    if ef!=0:
        case = case.edges("|Z").fillet(ef)

    # fillet top and side faces of the top molded part
    if ef!=0:
        BS = cq.selectors.BoxSelector
        case = case.edges(BS((-D1/2, -E1/2, c+0.001), (D1/2, E1/2, A+0.001))).fillet(ef)
        #case = case.edges(BS((-D1/2, -E1/2, c+0.001), (D1/2, E1/2, A+0.001+A1/2))).fillet(ef)
    case = case.translate((0,0,c-A1-0.01))
    ##show(case)
    if params.molded is not None:
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewFront()
    else:
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxonometric()
    
    #stop
    #case=case.union(case_bot)
    
    ##show(case)
    ##stop
    #######################################################################
    
    # case = make_plg(cq.Workplane("XY"),10,8,1,1)
    # case = case.extrude(0.5)
    # fillet=0
    # if fillet:
    #     case.edges("|X").fillet(0.1)
    #     case.edges("|Y").fillet(0.1)
    #     case.edges("|Z").fillet(0.1)
    # show(case)
    # 
    # case_top = make_plg(cq.Workplane("XY"),9,7,0.5,0.5)
    # case_top = case_top.extrude(0.4)
    # 
    # case_top2 = make_plg(case_top.faces(">Z").workplane(offset=0),6,4,0.2,0.2) #\
    # #.workplane(offset=1.2).rect(0.75,0.5).loft(combine=True)
    # case_top2= case_top.faces(">Z").workplane(offset=1.2).make_plg(case_top.faces(">Z").workplane(offset=0),6,4,0.2,0.2).loft(combine=True)
    # 
    # show(case_top)
    # show(case_top2)
    # 
    # stop
    # case_top = make_plg(cq.Workplane("XY"),9,7,0.5,0.5)
    # case_top = case_top.extrude(0.4)
    # # case_top = case_top.faces(">Z").workplane(offset=0.5)       #workplane is offset from the object surface
    # show(case_top)
    # stop
    # 
    # case = cq.Workplane("XY").box(D, E, A2)  #NO margin, pins don't emerge
    #####
    #if m == 0:
    #    case = cq.Workplane("XY").box(D-A1, E-A1, A2)  #margin to see fused pins
    #else:
    #    case = cq.Workplane("XY").box(D, E, A2)  #NO margin, pins don't emerge
    #if ef!=0:
    #    case.edges("|X").fillet(ef)
    #    case.edges("|Z").fillet(ef)
    # #translate the object
    #case=case.translate((0,0,A2/2+A1)).rotate((0,0,0), (0,0,1), 0)

    # first pin indicator is created with a spherical pocket
    if fp_r == 0:
        global place_pinMark
        place_pinMark=False
        fp_r = 0.1
    sphere_r = (fp_r*fp_r/2 + fp_z*fp_z) / (2*fp_z)
    sphere_z = A + sphere_r * 2 - fp_z - sphere_r

    pinmark=cq.Workplane("XZ", (-D/2+fp_d+fp_r, -E/2+fp_d+fp_r, fp_z)).rect(fp_r/2, -2*fp_z, False).revolve().translate((0,0,A))#+fp_z))

    #stop
    if (color_pin_mark==False) and (place_pinMark==True):
        case = case.cut(pinmark)
    # show(pinmark)
    # show(case)
    # stop
    
    if sq: #square pins
        bpin1 = cq.Workplane("XY"). \
            moveTo(b, 0). \
            lineTo(b, L). \
            lineTo(0, L). \
            lineTo(0, 0). \
            close().extrude(c).translate((b/2,E/2,0))
            #close().extrude(c).translate((b/2,E/2,A1/2))
    else:
        bpin1 = cq.Workplane("XY"). \
            moveTo(b, 0). \
            lineTo(b, L-b/2). \
            threePointArc((b/2,L),(0, L-b/2)). \
            lineTo(0, 0). \
            close().extrude(c).translate((b/2,E/2,0))
            #close().extrude(c).translate((b/2,E/2,A1/2))
    bpin=bpin1.rotate((b/2,E/2,A1/2), (0,0,1), 180)

    pins = []
    # create top, bottom side pins
    pincounter = 1
    first_pos_x = (npx-1)*e/2
    for i in range(npx):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_x-i*e, -m, 0)).\
                rotate((0,0,0), (0,0,1), 180)
            pins.append(pin)
        pincounter += 1
    
    first_pos_y = (npy-1)*e/2
    for i in range(npy):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_y-i*e, (D-E)/2-m, 0)).\
                rotate((0,0,0), (0,0,1), 270)
            pins.append(pin)
        pincounter += 1

    for i in range(npx):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_x-i*e, -m, 0))
            pins.append(pin)
        pincounter += 1
    
    for i in range(npy):
        if pincounter not in excluded_pins:
            pin = bpin.translate((first_pos_y-i*e, (D-E)/2-m, 0)).\
                rotate((0,0,0), (0,0,1), 90)
            pins.append(pin)
        pincounter += 1

    # create exposed thermal pad if requested
    if params.epad:
        if sq_epad:
            #pins.append(cq.Workplane("XY").box(D2, E2, A1+A1/10).translate((0,0,A1+A1/10)))
            #epad = cq.Workplane("XY", (0,0,A1/2)). \
            epad = cq.Workplane("XY").\
            moveTo(-D2/2+cce, -E2/2). \
            lineTo(D2/2, -E2/2). \
            lineTo(D2/2, E2/2). \
            lineTo(-D2/2, E2/2). \
            lineTo(-D2/2, -E2/2+cce). \
            close().extrude(A1) #+A1/2).translate((0,0,A1/2))
            #close().extrude(A1+A1/10)
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
    #case = case.cut(pins)
    case_bot = case_bot.cut(pins)

    return (case_bot, case, pins, pinmark)

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
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        excluded_pins_x=() ##no pin excluded
        excluded_pins_xmirror=() ##no pin excluded
        place_pinMark=True ##default =True used to exclude pin mark to build sot23-3; sot23-5; sc70 (asimmetrical pins, no pinmark)

        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        CheckedModelName = ModelName.replace('.', '')
        CheckedModelName = CheckedModelName.replace('-', '_')
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        case_bot, case, pins, pinmark = make_qfn(all_params[variant])

        show(case_bot)
        show(case)
        show(pins)
        show(pinmark)
        #stop
        
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)

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
        ## objs[0].Label='body'
        ## objs[1].Label='pins'
        ## objs[2].Label='mark'
        ###
        ## print objs[0].Name, objs[1].Name, objs[2].Name

        #stop
        #if place_pinMark==True:
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
        doc.Label=ModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label=ModelName
        restore_Main_Tools()
        #rotate if required
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
            z_RotateObject(doc, rot)
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

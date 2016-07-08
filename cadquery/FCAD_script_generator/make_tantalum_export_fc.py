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

## to run the script just do: freecad make_qfn_export_fc.py modelName
## e.g. c:\freecad\bin\freecad make_qfn_export_fc.py QFN16

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

__title__ = "make Tantalum Caps 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make Tantalum Caps 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.1 27/08/2015"

###ToDo: 

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui


outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

#checking requirements
#######################################################################
FreeCAD.Console.PrintMessage("FC Version \r\n")
FreeCAD.Console.PrintMessage(FreeCAD.Version())
FC_majorV=FreeCAD.Version()[0];FC_minorV=FreeCAD.Version()[1]
FreeCAD.Console.PrintMessage('FC Version '+FC_majorV+FC_minorV+'\r\n')

if int(FC_majorV) <= 0:
    if int(FC_minorV) < 15:
        reply = QtGui.QMessageBox.information(None,"Warning! ...","use FreeCAD version >= "+FC_majorV+"."+FC_minorV+"\r\n")


# FreeCAD.Console.PrintMessage(all_params_soic)
FreeCAD.Console.PrintMessage(FreeCAD.ConfigGet("AppHomePath")+'Mod/')
file_path_cq=FreeCAD.ConfigGet("AppHomePath")+'Mod/CadQuery'
if os.path.exists(file_path_cq):
    FreeCAD.Console.PrintMessage('CadQuery exists\r\n')
else:
    msg="missing CadQuery Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)

#######################################################################

# CadQuery Gui
from Gui.Command import *

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "example not present"

# from export_x3d import exportX3D, Mesh
import cadquery as cq
from Helpers import show
# maui end

#check version
cqv=cq.__version__.split(".")
#say2(cqv)
if int(cqv[0])==0 and int(cqv[1])<3:
    msg = "CadQuery Module needs to be at least 0.3.0!\r\n\r\n"
    reply = QtGui.QMessageBox.information(None, "Info ...", msg)
    say("cq needs to be at least 0.3.0")
    stop

import cq_params_tantalum  # modules parameters
from cq_params_tantalum import *

all_params= all_params_tantalum

def make_tantalum(params):

    L  = params.L
    W  = params.W
    H   = params.H
    F = params.F
    S = params.S
    B  = params.B
    P = params.P
    R = params.R
    T = params.T
    G = params.G
    E = params.E
    pml = params.pml
    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix

    Lb = L - 2.*T        # body lenght
    ppH = (H * 0.45)    # pivot point height
    
    ma_rad=radians(ma_deg)
    dtop = (H-ppH) * tan(ma_rad)
    dbot = (ppH-T) * tan(ma_rad)
    
    case_base = cq.Workplane(cq.Plane.XY()).workplane(offset=0).rect(E, G). \
                workplane(offset=T).rect(E,G). \
                loft(ruled=True)

    case = cq.Workplane(cq.Plane.XY()).workplane(offset=T).rect(W-dbot, Lb-dbot). \
               workplane(offset=ppH-T).rect(W,Lb). \
               workplane(offset=H-ppH).rect(W-dtop, Lb-dtop). \
               loft(ruled=True)

    if B!=0:
        BS = cq.selectors.BoxSelector
        case = case.edges(BS((-(W-2.*dtop)/2, (Lb-2.*dtop)/2., H-0.2), ((W+2.*dtop)/2, (Lb+2.*dtop)/2., H+0.2))).chamfer(B)
    
    case=case.union(case_base)
    #sleep
    pinmark = cq.Workplane(cq.Plane.XY()).workplane(offset=H-T*0.01).rect(W-dtop-dtop, pml). \
                workplane(offset=T*0.01).rect(W-dtop-dtop, pml). \
                loft(ruled=True)

    #translate the object  
    pinmark=pinmark.translate((0,Lb/2.-B-pml/2.-dtop/2.-dtop/2.,0)).rotate((0,0,0), (0,1,0), 0)
    #color_attr=(207, 83, 0 ,0)
    #show(pinmark, color_attr)
    #case=case.union(pinmark)
    # Color body SandyBrown
    #color_attr=(244,164,96,0)
    #show(case, color_attr)
    #sleep
    
    # Create a pin object at the center of top side.
        #threePointArc((L+K/sqrt(2), b/2-K*(1-1/sqrt(2))),
        #              (L+K, b/2-K)). \
    bpin1 = cq.Workplane("XY"). \
        moveTo(0,Lb/2.-S). \
        lineTo(0,Lb/2.). \
        lineTo(F,Lb/2.). \
        lineTo(F,Lb/2.-S). \
        close().extrude(T+0.01*T)
    bpin1=bpin1.translate((-F/2.,0,0))
    bpin=bpin1.rotate((0,(Lb/2.-S)/2.,F/2.), (0,0,1), 180).translate((0,-Lb/2.+S,0))
    
    delta=0.01
    hpin=ppH-delta*ppH
    bpin2 = cq.Workplane("XY"). \
        moveTo(0,Lb/2.). \
        lineTo(0,Lb/2.+T). \
        lineTo(F,Lb/2.+T). \
        lineTo(F,Lb/2.). \
        close().extrude(hpin)
    bpin2=bpin2.translate((-F/2.,0,0))
    BS = cq.selectors.BoxSelector
    bpin2 = bpin2.edges(BS((0-delta,L/2.-delta,hpin-delta), (0+delta,L/2.+delta,hpin+delta))).fillet(T*2./3.)    
    bpin2 = bpin2.edges(BS((0-delta,L/2.-delta,0-delta), (0+delta,L/2.+delta,0+delta))).fillet(T*2./3.)    
    bpinv=bpin2.rotate((0,(T)/2.,F/2.), (0,0,1), 180).translate((0,-T,0))
    #show (bpinv)
    if P!=0:
        anode = cq.Workplane("XY"). \
        moveTo(0,Lb/2.). \
        lineTo(0,Lb/2.+T). \
        lineTo(R,Lb/2.+T). \
        lineTo(R,Lb/2.). \
        close().extrude(hpin-P).translate((-R/2.,0,P))
        #show (anode)
        bpin2 = bpin2.cut(anode)
    #show (bpin2)
    #show (bpinv)
    #show(bpin1)
    #show (bpin)
    
    merged_pins=bpin
    merged_pins=merged_pins.union(bpin1)
    merged_pins=merged_pins.union(bpin2)
    merged_pins=merged_pins.union(bpinv)
    pins = merged_pins

    #show(pins)
    #sleep

    return (case, pins, pinmark)


def run():  # unused
    FreeCAD.Console.PrintMessage('\r\nRun Called...\r\n')
    # get variant names from command line
    ## if len(sys.argv) < 2:
    ##     print("No variant name is given!")
    ##     return
    ##
    ## if sys.argv[1] == "all":
    ##     variants = all_params.keys()
    ## else:
    ##     variants = sys.argv[1:]
    ##
    ## outdir = os.path.abspath("./generated_qfp/")
    ## if not os.path.exists(outdir):
    ##     os.makedirs(outdir)
    ##
    ## for variant in variants:
    ##     if not variant in all_params:
    ##         print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
    ##         continue
    ##     make_one(variant, outdir + ("/qfp_%s.x3d" % variant))



if __name__ == "__main__":
    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')
# maui     run()
    color_pin_mark=True
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building Tant A')
        model_to_build='A_3216_18'
    else:
        model_to_build=sys.argv[2]
        if len(sys.argv)==4:
            FreeCAD.Console.PrintMessage(sys.argv[3]+'\r\n')
            if (sys.argv[3].find('no-pinmark-color')!=-1):
                color_pin_mark=False
            else:
                color_pin_mark=True

    #FreeCAD.Console.PrintMessage(str(color_pin_mark)+'\r\n')
    #FreeCAD.Console.PrintMessage(str(sys.argv[3].find('no-pinmark-color')))

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
        Newdoc = FreeCAD.newDocument(ModelName)
        App.setActiveDocument(ModelName)
        Gui.ActiveDocument=Gui.getDocument(ModelName)
        case, pins, pinmark = make_tantalum(all_params[variant])

        color_attr=case_color+(0,)
        show(case, color_attr)
        color_attr=pins_color+(0,)
        show(pins, color_attr)
        color_attr=mark_color+(0,)
        show(pinmark, color_attr)

        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
        ## objs[0].Label='body'
        ## objs[1].Label='pins'
        ## objs[2].Label='mark'
        ###
        ## print objs[0].Name, objs[1].Name, objs[2].Name

        ##sleep
        #if place_pinMark==True:
        if (color_pin_mark==True) and (place_pinMark==True):
            CutObjs_wColors(FreeCAD, FreeCADGui,
                           doc.Name, objs[0].Name, objs[2].Name)
        else:
            #removing pinMark
            App.getDocument(doc.Name).removeObject(objs[2].Name)
        ###
        ##sleep
        del objs
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
        out_dir=script_dir+destination_dir+all_params[variant].dest_dir_prefix+'/'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        #out_dir="./generated_qfp/"
        # export STEP model
        exportSTEP(doc,ModelName,out_dir)
        # scale and export Vrml model
        scale=0.3937001
        exportVRML(doc,ModelName,scale,out_dir)
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir)
        #display BBox
        FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()
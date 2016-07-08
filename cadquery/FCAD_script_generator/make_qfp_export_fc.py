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
## modified cadquery libs from
##   https://github.com/hyOzd/cadquery
## to substitute to cadquery lib in
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad make_qfp_export_fc.py modelName
## e.g. c:\freecad\bin\freecad make_qfp_export_fc.py AKA

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* This are a FreeCAD & cadquery tools                                      *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cad tools functions                                                      *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
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

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
from Gui.Command import *

outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject

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

import cq_params  # modules parameters
from cq_params import *

def make_qfp(params):

    D1  = params.D1
    E1  = params.E1
    A1  = params.A1
    A2  = params.A2
    b   = params.b
    e   = params.e
    npx = params.npx
    npy = params.npy
    #mN  = params.modelName

    if params.epad:
        D2 = params.epad[0]
        E2 = params.epad[1]

    # calculated dimensions for body
    A = A1 + A2
    A2_t = (A2-c)/2 # body top part height
    A2_b = A2_t     # body bottom part height
    D1_b = D1-2*tan(radians(the))*A2_b # bottom width
    E1_b = E1-2*tan(radians(the))*A2_b # bottom length
    D1_t1 = D1-tb_s # top part bottom width
    E1_t1 = E1-tb_s # top part bottom length
    D1_t2 = D1_t1-2*tan(radians(the))*A2_t # top part upper width
    E1_t2 = E1_t1-2*tan(radians(the))*A2_t # top part upper length

    case = cq.Workplane(cq.Plane.XY()).workplane(offset=A1).rect(D1_b, E1_b). \
           workplane(offset=A2_b).rect(D1, E1).workplane(offset=c).rect(D1,E1). \
           rect(D1_t1,E1_t1).workplane(offset=A2_t).rect(D1_t2,E1_t2). \
           loft(ruled=True).faces(">Z").fillet(ef)

    # fillet the corners
    BS = cq.selectors.BoxSelector
    case = case.edges(BS((D1_t2/2, E1_t2/2, 0), (D1/2+0.1, E1/2+0.1, A2))).fillet(ef)
    case = case.edges(BS((-D1_t2/2, E1_t2/2, 0), (-D1/2-0.1, E1/2+0.1, A2))).fillet(ef)
    case = case.edges(BS((-D1_t2/2, -E1_t2/2, 0), (-D1/2-0.1, -E1/2-0.1, A2))).fillet(ef)
    case = case.edges(BS((D1_t2/2, -E1_t2/2, 0), (D1/2+0.1, -E1/2-0.1, A2))).fillet(ef)

    # first pin indicator is created with a spherical pocket
    sphere_r = (fp_r*fp_r/2 + fp_z*fp_z) / (2*fp_z)
    sphere_z = A + sphere_r * 2 - fp_z - sphere_r
    sphere = cq.Workplane("XY", (-D1_t2/2+fp_d+fp_r, -E1_t2/2+fp_d+fp_r, sphere_z)). \
             sphere(sphere_r)
    case = case.cut(sphere)

    # calculated dimensions for pin
    R1_o = R1+c # pin upper corner, outer radius
    R2_o = R2+c # pin lower corner, outer radius

    # Create a pin object at the center of top side.
    bpin = cq.Workplane("YZ", (0,E1/2,0)). \
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
    # create top, bottom side pins
    first_pos = -(npx-1)*e/2
    for i in range(npx):
        pin = bpin.translate((first_pos+i*e, 0, 0))
        pins.append(pin)
        pin = bpin.translate((first_pos+i*e, 0, 0)).\
              rotate((0,0,0), (0,0,1), 180)
        pins.append(pin)

    # create right, left side pins
    first_pos = -(npy-1)*e/2
    for i in range(npy):
        pin = bpin.translate((first_pos+i*e, (D1-E1)/2, 0)).\
              rotate((0,0,0), (0,0,1), 90)
        pins.append(pin)
        pin = bpin.translate((first_pos+i*e, (D1-E1)/2, 0)).\
              rotate((0,0,0), (0,0,1), 270)
        pins.append(pin)

    # create exposed thermal pad if requested
    if params.epad:
        pins.append(cq.Workplane("XY").box(D2, E2, A1).translate((0,0,A1/2)))

    # merge all pins to a single object
    merged_pins = pins[0]
    for p in pins[1:]:
        merged_pins = merged_pins.union(p)
    pins = merged_pins

    # extract pins from case
    case = case.cut(pins)

    return (case, pins)


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
    ## if (not "modelName" in all_params['AKA']):
    ##     ModelName = "newModel" # "LQFP64_p05_h12"
    ## else:
    ##     ModelName = all_params.modelName

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building AKA')
        model_to_build='AKA'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        Newdoc = FreeCAD.newDocument(ModelName)
        App.setActiveDocument(ModelName)
        Gui.ActiveDocument=Gui.getDocument(ModelName)
        case, pins = make_qfp(all_params[variant])

        show(case, (80, 80, 80, 0))
        show(pins)

        doc = FreeCAD.ActiveDocument
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
        out_dir=destination_dir
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
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()
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

__title__ = "make Radial SMD Caps 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make QFN ICs 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.2 10/02/2017"

# thanks to Frank Severinsen Shack for including vrml materials

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import datetime
from datetime import datetime
sys.path.append("./exportVRML")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "metal grey pins"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
base_color_key = "black body"
base_color = shaderColors.named_colors[base_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
mark_color_key = "black body"
mark_color = shaderColors.named_colors[mark_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui

outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

# CadQuery Gui
from Gui.Command import *

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import *

# Load parameters
sys.path.append("parameters")
import cq_params_radial_smd_cap  # modules parameters
from cq_params_radial_smd_cap import *

output_dir = getOutputDir("cap_radial_smd")

all_params = kicad_naming_params_radial_smd_cap
# all_params = all_params_radial_smd_cap

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"


# from export_x3d import exportX3D, Mesh
import cadquery as cq
from Helpers import show
# maui end

checkMinRequirements(cq)


def make_radial_smd(params):

    L = params.L    # overall height
    D = params.D    # diameter
    A = params.A    # base width (x&y)
    H = params.H    # max width (x) with pins
    P = params.P    # distance between pins
    W = params.W    # pin width

    c = 0.15  # pin thickness

    bh = 1.0 # belt start height
    br = 0.2 # belt radius
    bf = 0.1 # belt fillet

    D2 = A+0.1  # cut diameter

    h1 = 1.  # bottom plastic height, cathode side
    h2 = 0.5 # bottom plastic base height, mid side
    h3 = 0.7 # bottom plastic height, anode side

    cf = 0.4  # cathode side corner fillet
    ac = A/5. # anode side chamfer

    ef = 0.2 # fillet of the top and bottom edges of the metallic body

    rot = params.rotation
    dest_dir_pref = params.dest_dir_prefix

    cimw = D/2.*0.7 # cathode identification mark width

    # draw aluminium the body
    body = cq.Workplane("XZ", (0,0,c+h2)).\
           lineTo(D/2., 0).\
           line(0, bh).\
           threePointArc((D/2.-br, bh+br), (D/2., bh+2*br)).\
           lineTo(D/2., L-c-h2).\
           line(-D/2, 0).\
           close().revolve()

    # fillet the belt edges
    BS = cq.selectors.BoxSelector
    body = body.edges(BS((-0.1,-0.1,c+h2+0.1), (0.1,0.1,L-0.1))).\
           fillet(bf)

    # fillet the top and bottom
    body = body.faces(">Z").fillet(ef).\
           faces("<Z").fillet(ef)

    # draw the plastic base
    base = cq.Workplane("XY", (0,0,c)).\
           moveTo(-A/2.,-A/2.).\
           line(A-ac, 0).\
           line(ac, ac).\
           line(0, A-2*ac).\
           line(-ac, ac).\
           line(-A+ac, 0).\
           close().extrude(h1)

    # fillet cathode side
    base = base.edges(BS((-A,-A,0), (-A/2.+0.01,-A/2.+0.01,c+h1+0.01))).\
           fillet(cf).\
           edges(BS((-A,A,0), (-A/2.+0.01,A/2.-0.01,c+h1+0.01))).\
           fillet(cf)

    # cut base center
    base = base.cut(
        cq.Workplane("XY", (0,0,c+h2)).\
        circle(D2/2.).extrude(h1-h2))

    # cut anode side of the base
    base = base.cut(
        cq.Workplane("XY", (0,-A/2.,c+h3)).\
        box(A/2., A, h1-h3, centered=(False, False, False)))

    # draw pins
    pins = cq.Workplane("XY").\
           moveTo(H/2., -W/2.).\
           line(0, W).\
           lineTo(P/2.+W/2., W/2.).\
           threePointArc((P/2.,0), (P/2.+W/2., -W/2)).\
           close().extrude(c)

    pins = pins.union(pins.rotate((0,0,0), (0,0,1), 180))

    # draw the cathode identification mark
    cim = cq.Workplane("XY", (-D/2.,0,L-ef)).\
          box(cimw, D, ef, centered=(False, True, False))

    # do intersection
    cim = cim.cut(cim.translate((0,0,0)).cut(body))

    body.cut(cim)

    return (body, base, cim, pins)

import step_license as L

if __name__ == "__main__":
    expVRML.say(expVRML.__file__)
    say('\r\nRunning...\r\n')

# maui     run()
    color_pin_mark=True
    if len(sys.argv) < 3:
        model_to_build='all'
    else:
        model_to_build=sys.argv[2]
        if len(sys.argv)==4:
            say(sys.argv[3]+'\r\n')
            if (sys.argv[3].find('no-pinmark-color')!=-1):
                color_pin_mark=False
            else:
                color_pin_mark=True
    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        say('\r\n'+variant)
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping." % variant)
            continue
        ModelName = all_params[variant].modelName
        CheckedModelName = ModelName.replace('.', '')
        CheckedModelName = CheckedModelName.replace('-', '_')
        Newdoc = FreeCAD.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        body, base, mark, pins = make_radial_smd(all_params[variant])

        show(body)
        show(base)
        show(pins)
        show(mark)
        
        doc = FreeCAD.ActiveDocument
        objs = GetListOfObjects(FreeCAD, doc)

        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],base_color)
        Color_Objects(Gui,objs[2],pins_color)
        Color_Objects(Gui,objs[3],mark_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_base=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        col_mark=Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
        material_substitutions={
            col_body[:-1]:body_color_key,
            col_base[:-1]:base_color_key,
            col_pin[:-1]:pins_color_key,
            col_mark[:-1]:mark_color_key
        }
        expVRML.say(material_substitutions)

        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[2].Name, objs[3].Name)
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)    
        doc.Label=ModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label=ModelName
        restore_Main_Tools()
        #rotate if required
        if (all_params[variant].rotation!=0):
            rot= all_params[variant].rotation
            z_RotateObject(doc, rot)
        
        
        # export STEP model
        exportSTEP(doc, ModelName, output_dir)
        
        # scale and export Vrml model
        scale=1/2.54
        objs=GetListOfObjects(FreeCAD, doc)
        expVRML.say("######################################################################")
        expVRML.say(objs)
        expVRML.say("######################################################################")
        export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
        export_file_name=output_dir+os.path.sep+ModelName+'.wrl'
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,output_dir)
        #display BBox
        #FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
        Gui.activateWorkbench("PartWorkbench")
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()
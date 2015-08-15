# -*- coding: utf8 -*-
#!/usr/bin/python
# This is derived from a cadquery script to generate all pin header models in X3D format.
# It takes a bit long to run! It can be run from cadquery freecad
# module as well.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd

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

__title__ = "make pin header 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make pin header 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.4.1 14/08/2015"


#sleep ### NB il modello presenta errori di geometria

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui

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

close_CQ_Example(App, Gui)

# from export_x3d import exportX3D, Mesh
import cadquery as cq
from Helpers import show
# maui end

npins = 5          # number of pins
sep = 2.54         # distance between pins
chamfer = 0.4      # chamfering of plastic base
hb = 2.54          # height of plastic base
hb2 = 0.5          # height of bottom cut
pw = 0.64          # width of a pin
pw_tip = pw/2      # width of pin at the tip
hp = 11.54         # height of a pin
h_tip = pw_tip*1.5 # height of pins tip
pos_y = -3         # vertical start position of a pin
delta =sep/1000    # added delta for avoid geometry problems in fusion maui

case_color = (50, 50, 50)
pins_color = (255, 215, 0)
destination_dir="./generated_pinheaders/"
rotation = 0
outdir = "" # handled below

def make_pinheader(npins):
    # create the base
    # left edge
    points = [
        (-sep/2-delta/2, -sep/2-delta/2+chamfer),
        (-sep/2-delta/2, sep/2+delta/2-chamfer)
        ]

    # top edges
    for i in range(npins):
        points.append((-sep/2-delta/2+chamfer+(sep)*i, sep/2+delta/2))
        points.append((sep/2+delta/2-chamfer+(sep)*i, sep/2+delta/2))
        points.append((sep/2+delta/2+(sep)*i, sep/2+delta/2-chamfer))

    # right edge
    points.append((sep/2+delta/2+(sep)*(npins-1), -sep/2-delta/2+chamfer))

    # bottom edges
    for i in reversed(range(npins)):
        points.append((sep/2+delta/2-chamfer+(sep)*i, -sep/2-delta/2))
        points.append((-sep/2-delta/2+chamfer+(sep)*i, -sep/2-delta/2))
        points.append((-sep/2-delta/2+(sep)*i, -sep/2-delta/2+chamfer))

    base = cq.Workplane("front").polyline(points).extrude(hb)
    # pin holes
    base = base.faces(">Z").workplane().rarray(sep, 1, npins, 1).rect(pw, pw).cutThruAll()
    # bottom cut
    base = base.faces("<X").workplane().center(0,-(hb-hb2)/2).rect(sep-2*chamfer, hb2).cutThruAll()
    # barely fillet the top
    base = base.faces(">Z").fillet(0.1)
    base=base.translate((-npins*sep/2+sep/2,0,0)) #maui

    # make pins
    def makePin():
        pin = cq.Workplane(cq.Plane.named("front",(0,0,pos_y))). \
            rect(pw_tip, pw_tip).workplane(offset=h_tip).rect(pw,pw).workplane(offset=hp-h_tip*2). \
            rect(pw,pw).workplane(offset=h_tip).rect(pw_tip, pw_tip).loft(ruled=True)
        return pin

    pin = makePin()
    pins = pin.translate((0,0,0))
    for i in range(1,npins):
        pins = pins.union(pin.translate((sep*i,0,0)))
    pins = pins.translate((-npins*sep/2+sep/2,0,0))

    return (base, pins)

## def shapeToMesh(shape, color):
##     mesh_data = shape.tessellate(1)
##     return Mesh(points = mesh_data[0],
##                 faces = mesh_data[1],
##                 color = color)

def make_one(npins):
    """Creates a pin header model file for given number of pins."""
    print("Generating pinheader %d" % npins)
    case, pins = make_pinheader(npins)
    ## exportX3D([shapeToMesh(case.toFreecad(), case_color),
    ##            shapeToMesh(pins.toFreecad(), pins_color)],
    ##           outdir+"/pinheader_1x%d.x3d" % npins)
    print("Done pinheader %d" % npins)

def make_all():
    """Creates all straight pin headers from 1 to 40 pins in X3D format in
    parallel."""
    global outdir
    outdir = os.path.abspath("./generated_pinheaders/")
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    ## from multiprocessing import Pool
    ##
    ## p = Pool()
    ## p.map(make_one, list(range(1,40+1)))  maui TBD


def build_and_save(i):

    ModelName='pinstrip_p254_'+str(i)+'x1'
    Newdoc = FreeCAD.newDocument(ModelName)
    App.setActiveDocument(ModelName)
    Gui.ActiveDocument=Gui.getDocument(ModelName)

    FreeCAD.Console.PrintMessage('making all pin headers\r\n')
    case, pins = make_pinheader(i)

    color_attr=case_color+(0,)
    show(case, color_attr)
    #FreeCAD.Console.PrintMessage(pins_color)
    color_attr=pins_color+(0,)
    #FreeCAD.Console.PrintMessage(color_attr)
    show(pins, color_attr)
    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui,
                    doc.Name, objs[0].Name, objs[1].Name)
    doc.Label=ModelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=ModelName
    restore_Main_Tools()
    #rotate if required
    if (rotation!=0):
        z_RotateObject(doc, rotation)
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
    #display BBox

    FreeCADGui.ActiveDocument.getObject("Part__Feature").BoundingBox = True
    #import ImportGui
    #ImportGui.insert(u"C:/Cad/Progetti_K/FreeCAD-models/scripts/3D-models/CadQuery/reference-block.step","mypin")

    Gui.SendMsgToActiveView("ViewFit")
    Gui.activeDocument().activeView().viewAxometric()

    return 0
# when run from command line
if __name__ == "__main__":
    # make_all() maui TBD

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')
# maui     run()

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building pinstrip_p254_5x1')
        model_to_build='5'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        for i in range(1, 41):
            build_and_save(i)
    else:
        build_and_save(int(model_to_build))





# when run from freecad-cadquery
if __name__ == "temp.module":
    ModelName="mypin"
    ## Newdoc = FreeCAD.newDocument(ModelName)
    ## App.setActiveDocument(ModelName)
    ## Gui.ActiveDocument=Gui.getDocument(ModelName)
    ##
    ## case, pins = make_pinheader(5)
    ##
    ## show(case, (60,60,60,0))
    ## show(pins)



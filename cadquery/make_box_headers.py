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

#from cq_cad_tools import say, sayw, saye

import sys, os

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui


from Gui.Command import *

outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

# Import cad_tools
import cq_cad_tools
from cq_cad_tools import say, sayw, saye

# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import *

checkMinRequirements()

out_dir = getOutputDir("box_headers")

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

#check version
cqv=cq.__version__.split(".")
#say2(cqv)
if int(cqv[0])==0 and int(cqv[1])<3:
    msg = "CadQuery Module needs to be at least 0.3.0!\r\n\r\n"
    reply = QtGui.QMessageBox.information(None, "Info ...", msg)
    say("cq needs to be at least 0.3.0")
    stop

from collections import namedtuple

#Make a single plastic base block (chamfered if required)
def MakeBase(pins):
    
    #length of the base block
    L = pins * 2.54 + 7.62
    
    #Width of base block
    W1 = 8.9

    #internal width
    W2 = 6.4
    
    #wall thickness
    T = (W1 - W2) / 2
    
    #length of pin array
    D = (pins - 1) * 2.54
    
    #height of the base
    H = 2.8
    
    base = cq.Workplane("XY").rect(L,W1).extrude(H - T)
    
    #wall height H2
    H2 = 8.9 - H
    
    #extrude the edge up around the base
    wall = cq.Workplane("XY").workplane(offset=H-T).rect(L,W1).extrude(H2+T).faces(">Z").shell(-T)
    
    base = base.union(wall)
    
    #cut a notch out of one side 
    CW = 4
    cutout = cq.Workplane("XY").workplane(offset=H).rect(CW,W1).extrude(H2).translate((0,-W2/2,0))
    
    base = base.cut(cutout)
    
    #now offset the location of the base appropriately
    base = base.translate(((pins-1)*1.27,1.27,0))
    
    return base
    
#make a single pin
def MakePin():

    #pin size
    size = 0.64
    
    #pin height
    H = 11.0
    
    #pin distance below z=0
    Z = -3.0

    pin = cq.Workplane("XY").workplane(offset=Z).rect(size,size).extrude(H)

    #Chamfer C
    C = 0.2
    
    pin = pin.faces("<Z").chamfer(C)
    pin = pin.faces(">Z").chamfer(C)
    
    return pin
    
#make all the pins
def MakePinRow(n):
    #make some pins
    pin = MakePin()
    
    for i in range(1,n):
        pin = pin.union(MakePin().translate((2.54 * i,0,0)))
    
    return pin

#generate a name for the pin header
def HeaderName(n):
    return "Box_Header_Straight_2x{n:02}x2.54mm".format(n=n)
    
#make a pin header using supplied parameters, n pins in each row
def MakeHeader(n):
    
    name = HeaderName(n)
    
    #having a period '.' character in the model name REALLY messes with things.
    docname = name.replace(".","")
    
    newdoc = FreeCAD.newDocument(docname)
    App.setActiveDocument(docname)
    Gui.ActiveDocument=Gui.getDocument(docname)
    
    pins = MakePinRow(n)
    pins = pins.union(MakePinRow(n).translate((0,2.54,0)))
    
    base = MakeBase(n)
        
    #assign some colors
    base_color = (50,50,50)
    pins_color = (225,175,0)

    show(base,base_color+(0,))
    show(pins,pins_color+(0,))
    
    doc = FreeCAD.ActiveDocument
        
    objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui,
                   doc.Name, objs[0].Name, objs[1].Name)
    doc.Label=docname
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=docname
    restore_Main_Tools()
    
    doc.Label = docname
    
    #save the STEP file
    exportSTEP(doc, name, out_dir)

    #save the VRML file
    scale=0.3937001
    exportVRML(doc,name,scale,out_dir)
    
    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, name,out_dir)

    Gui.SendMsgToActiveView("ViewFit")
    Gui.activeDocument().activeView().viewAxometric()

    return 0
    
if __name__ == "__main__":
    
    pins = []
    
    if len(sys.argv) < 3:
        say("Building all")
        pins = range(2,41)
    else:
        arg = sys.argv[2]
        if arg.lower() == "all":
            pins = range(2,41)
        else:
            pins = cq_cad_tools.getListOfNumbers(sys.argv[2])
    
    for pin in pins:
        MakeHeader(pin)



# when run from freecad-cadquery
if __name__ == "temp.module":
    pass
    #ModelName="mypin"
    ## Newdoc = FreeCAD.newDocument(ModelName)
    ## App.setActiveDocument(ModelName)
    ## Gui.ActiveDocument=Gui.getDocument(ModelName)
    ##
    ## case, pins = make_pinheader(5)
    ##
    ## show(case, (60,60,60,0))
    ## show(pins)



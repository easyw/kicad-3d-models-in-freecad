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

from collections import namedtuple

"""
Parameters for creating various pin-headers
"""
Params = namedtuple("Params", [
    'p', # pitch (separaration between pins)
    'rows', #number of rows
    'w', #width of plastic base
    'hole', # hole size (square) for each pin
    'h', # height of plastic base above board
    'pw1', #pin width in x-dir
    'pw2', #pin width in y-dir
    'pc', #pin end chamfer amount
    'ph', #pin height (below z=0)
    'rot', #rotation if required
])

headers = {
    #e.g. http://www.sullinscorp.com/drawings/78_P(N)PxCxxxLFBN-RC,_10492-H.pdf
    '254single': Params(
        p = 2.54,
        w = 2.54,
        rows = 1,
        hole = 1,
        h = 8.5,
        pw1 = 0.75,
        pw2 = 0.4,
        pc = 0.15,
        ph = 3.2,
        rot = 0,
    ),
}

destination_dir="./generated_pinheaders/"

outdir = "" # handled below

#Make a single plastic base block (chamfered if required)
def MakeBaseBlock(params):
    block = cq.Workplane("XY").rect(params.p, params.w).extrude(params.h)
    
    hole = block.faces(">Z").rect(params.hole,params.hole)
    
    hole_ext = hole.extrude(-params.h * 0.75)
    
    block = block.cut(hole_ext)
    
    #block = block.edges(">Z").chamfer(0.25 * params.hole)
    
    return block
    
#Make the plastic base
#Note - making the 'blocks' separately and then making a UNION of the blocks seems to be the best way to get them to merge
#make the plastic base
def MakeBase(n, params):

    base = MakeBaseBlock(params)
    
    for i in range(1,n):
        block = MakeBaseBlock(params).translate((i*params.p,0,0))
        base = base.union(block)
        
    #move the base to the 'middle'
    if params.rows > 1:
        offset = params.p * (params.rows - 1) / 2.0
        base = base.translate((0,offset,0))
        
    return base
    
#make a single pin
def MakePin(params):
    pin = cq.Workplane("XY").workplane(offset=-params.ph).rect(params.pw1,params.pw2).extrude(params.ph + 0.1) #extrude a little way into the base
    
    #chamfer each end of the pin if required
    if params.pc > 0:
        #pin = pin.faces(">Z").chamfer(params.pc)
        pin = pin.faces("<Z").chamfer(params.pc)
    
    return pin
    
#make all the pins
def MakePinRow(n, params):
    #make some pins
    pin = MakePin(params)
    
    for i in range(1,n):
        pin = pin.union(MakePin(params).translate((params.p * i,0,0)))
    
    return pin

#generate a name for the socket strip
def HeaderName(n, params):
    return "SocketStrip_Straight_{r:01}x{n:02}x{p:.2f}mm".format(r=params.rows,n=n,p=params.p)
    
#make a pin header using supplied parameters, n pins in each row
def MakeHeader(n, params):
    
    name = HeaderName(n,params)
    
    #having a period '.' character in the model name REALLY messes with things.
    docname = name.replace(".","")
    
    newdoc = FreeCAD.newDocument(docname)
    App.setActiveDocument(docname)
    Gui.ActiveDocument=Gui.getDocument(docname)
    
    pins = MakePinRow(n,params)
    
    #duplicate pin rows
    if params.rows > 1:
        for i in range(1,params.rows):
            pins = pins.union(MakePinRow(n,params).translate((0,i*params.p,0)))
    
    base = MakeBase(n,params)
        
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

    if (params.rot !=0):
        z_RotateObject(doc, params.rot)
    
    out_dir = "./generated_socketstrips/"
    
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
    
    models = []
    
    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage("Nothing to build...")
        FreeCAD.Console.PrintMessage("Specify name and pins")
        
    else:
        model = sys.argv[2]
        
        if model == 'all':
            models = [headers[model] for model in headers.keys()]
        else:
            models = [headers[i] for i in model.split(',') if i in headers.keys()]#separate model types with comma
            
    pins = []
    
    if len(sys.argv) < 4:
        FreeCAD.Console.PrintMessage("No pins specifed. Not building")
    else:
        p = sys.argv[3].strip()
        
        #comma separarated pin numberings
        if ',' in p:
            try:
                pins = map(int,p.split(','))
            except:
                FreeCAD.Console.PrintMessage("Pin argument '"+p+"' is invalid ,")
                pins = []
        
        #range of pins x-y
        elif '-' in p and len(p.split('-')) == 2:
            ps = p.split('-')
            
            try:
                p1, p2 = int(ps[0]),int(ps[1])
                pins = range(p1,p2+1)
            except:
                FreeCAD.Console.PrintMessage("Pin argument '"+p+"' is invalid -")
                pins = []
                
        #otherwise try for a single pin
        else:
            try:
                pin = int(p)
                pins = [pin]
            except:
                FreeCAD.Console.PrintMessage("Pin argument '"+p+"' is invalid")
                pins = []
                
    #make all the seleted models
    for model in models:
        for pin in pins:
            MakeHeader(pin,model)



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



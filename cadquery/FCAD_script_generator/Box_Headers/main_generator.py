#!/usr/bin/python
# -*- coding: utf-8 -*-
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

___ver___ = "1.4.3 18/06/2020"

# Licence information of the generated models.
#################################################################################################
STR_licAuthor = "kicad StepUp"
STR_licEmail = "ksu"
STR_licOrgSys = "kicad StepUp"
STR_licPreProc = "OCC"
STR_licOrg = "FreeCAD"

LIST_license = ["",]
#################################################################################################

save_memory = True #reducing memory consuming for all generation params
check_Model = True
check_log_file = 'check-log.md'

body_color_key = "black body"
pins_color_key = "gold pins"
color_keys = [body_color_key, pins_color_key]

import sys, os
import datetime
from datetime import datetime
from math import sqrt
from collections import namedtuple

sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors
import add_license as Lic

import re, fnmatch
import yaml

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)

#######################################################################

# Import cad_tools
import cq_cad_tools

# Reload tools
from cq_cad_tools import reload_lib
reload_lib(cq_cad_tools)

# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
CutObjs_wColors, checkRequirements, multiFuseObjs_wColors, runGeometryCheck


checkRequirements(cq)


import ImportGui

#Make a single plastic base block (chamfered if required)
# dimensions taken from Wurth Elektronik (WE) 612 0xx 216 21: http://katalog.we-online.de/em/datasheet/6120xx21621.pdf
# dimensions not shown on drawing are estimated or taken from physical example
def MakeBase(pins, highDetail=True):

    #length of the base block
    L = pins * 2.54 + 7.66
    #Width of base block
    W1 = 8.85
    #internal width
    W2 = 6.35
    #wall thickness
    T = (W1 - W2) / 2.0
    #length of pin array
    D = (pins - 1) * 2.54
    #height of the base
    H = 8.85-6.50
    base = cq.Workplane("XY").rect(W1,L).extrude(H)
    #wall height H2
    H2 = 6.50

    #extrude the edge up around the base
    wall = cq.Workplane("XY").workplane(offset=H).rect(W1,L).extrude(H2)
    wall = wall.cut(cq.Workplane("XY").rect(W2,(pins-1)*2.54+7.88).extrude(8.85))
    # add a chamfer to the wall inner (only for high detail version)
    # if (highDetail):
    #     wall = wall.faces(">Z").edges("not(<X or >X or <Y or >Y)").chamfer(0.5)
    base = base.union(wall)

    #cut a notch out of one side
    CW = 4.5

    # in detail version, this tab extends slightly below base top surface
    if (highDetail):
        undercut = 0.5
    else:
        undercut = 0.0

    cutout = cq.Workplane("XY").workplane(offset=H-undercut).rect(2*2.0,CW).extrude(H2+undercut).translate((-W1/2.0,0,0))
    base = base.cut(cutout)

    # add visual / non-critical details
    if (highDetail):

        # long bobbles
        bobbleR = 0.5
        bobbleH = 9.10-8.85
        longbobble1 = cq.Workplane("XY").center(W1/2.0-bobbleR+bobbleH, L/2.0-2.5).circle(bobbleR).extrude(8.5)
        longbobble2 = cq.Workplane("XY").center(W1/2.0-bobbleR+bobbleH, 0).circle(bobbleR).extrude(8.5)
        longbobble3 = cq.Workplane("XY").center(W1/2.0-bobbleR+bobbleH, -L/2.0+2.5).circle(bobbleR).extrude(8.5)
        base = base.union(longbobble1)
        base = base.union(longbobble2)
        base = base.union(longbobble3)

        # wee bobbles
        weebobbles = cq.Workplane("XY").center(2.85, L/2.0-2.5).circle(0.5).extrude(8.85-9.10)
        weebobbles = weebobbles.union(cq.Workplane("XY").center(2.85, 0).circle(0.5).extrude(8.85-9.10))
        weebobbles = weebobbles.union(cq.Workplane("XY").center(2.85, -L/2.0+2.5).circle(0.5).extrude(8.85-9.10))
        weebobbles = weebobbles.union(weebobbles.translate((-5.7,0,0)))
        base = base.union(weebobbles)

        # sidecuts
        sidecut = cq.Workplane("XY").rect(3.5, 1.25*2).extrude(H2).translate((0,L/2.0,0))
        sidecut = sidecut.union(sidecut.translate((0,-L,0)))
        base = base.cut(sidecut)

    #now offset the location of the base appropriately
    base = base.translate((1.27,(pins-1)*-1.27,9.10-8.85))

    return base

#make a single pin
def MakePin(Z, H):

    #pin size
    size = 0.64
    #pin distance below z=0
    #Z = -3.0
    #pin height (above board)
    #H = 8.0
    pin = cq.Workplane("XY").workplane(offset=Z).rect(size,size).extrude(H - Z)
    #Chamfer C
    C = 0.2
    pin = pin.faces("<Z").chamfer(C)
    pin = pin.faces(">Z").chamfer(C)

    return pin

# make a single angle pin
def MakeAnglePin(Z, H, L, highDetail=False):
    #pin size
    size = 0.64
    pin = cq.Workplane("XY").workplane(offset=Z).rect(size,size).extrude(H - Z + size/2.0)
    pin = pin.union(cq.Workplane("YZ").workplane(offset=size/2.0).rect(size,size).extrude(L-size/2.0).translate((0,0,H)))
    #Chamfer C
    C = 0.2
    pin = pin.faces("<Z").chamfer(C)
    pin = pin.faces(">X").chamfer(C)

    # fillet on back of pin
    if (highDetail):
        R = size
        pin = pin.faces(">Z").edges("<X").fillet(R)

    return pin

# make a row of straight pins
def MakePinRow(n, Z, H):

    #make some pins
    pin = MakePin(Z, H)

    for i in range(1,n):
        pin = pin.union(MakePin(Z, H).translate((0,-2.54 * i,0)))

    return pin

# make a row of angled (bent) pins
def MakeAnglePinRow(n, Z, H, L, highDetail=False):

    pin = MakeAnglePin(Z, H, L, highDetail)

    for i in range(1,n):
        pin = pin.union(MakeAnglePin(Z, H, L, highDetail).translate((0,-2.54 * i,0)))

    return pin

# generate a name for the pin header
def HeaderName(n, isAngled):
    if (isAngled):
        return "IDC-Header_2x{n:02}_P2.54mm_Horizontal".format(n=n)
    else:
        return "IDC-Header_2x{n:02}_P2.54mm_Vertical".format(n=n)

# make a pin header using supplied parameters, n pins in each row

def MakeHeader(n, isAngled, log, highDetail=False):
    global LIST_license
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")

    LIST_license[0] = "Copyright (C) "+datetime.now().strftime("%Y")+", " + STR_licAuthor

    name = HeaderName(n, isAngled)
    print('\n############ ' + name + ' #############\n')

    lib_name='Connector_IDC'


    full_path=os.path.realpath(__file__)
    sub_dir_name =full_path.split(os.sep)[-2]
    sub_path = full_path.split(sub_dir_name)[0]
    models_dir=sub_path+"_3Dmodels"+os.sep
    #models_dir=script_dir+"/../_3Dmodels"

    out_dir=models_dir+'{:s}.3dshapes'.format(lib_name)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    #having a period '.' or '-' character in the model name REALLY messes with things.
    docname = name.replace(".","").replace("-","_").replace('(', '').replace(')', '')

    Newdoc = FreeCAD.newDocument(docname)
    App.setActiveDocument(docname)
    App.ActiveDocument=App.getDocument(docname)
    Gui.ActiveDocument=Gui.getDocument(docname)

    base = MakeBase(n, highDetail)

    if (isAngled):
        pins = MakeAnglePinRow(n, -3, 5.94, 12.38, highDetail)
        pins = pins.union(MakeAnglePinRow(n, -3, 3.40, 9.84, highDetail).translate((2.54,0,0)))
        # rotate the base into the angled position
        base = base.rotate((0,0,0),(0,1,0),90).translate((4.13,0,5.94))
    else:
        pins = MakePinRow(n, -3.0, 8.0)
        pins = pins.union(MakePinRow(n, -3.0, 8.0).translate((2.54,0,0)))


    colors = [shaderColors.named_colors[key].getDiffuseInt() for key in color_keys]

    cq_obj_data = [base, pins]
    obj_suffixes = ['__base', '__pins']


    for i in range(len(cq_obj_data)):
        color_i = colors[i] + (0,)
        show(cq_obj_data[i], color_i)


    doc = FreeCAD.ActiveDocument
    doc.Label = docname
    objs=GetListOfObjects(FreeCAD, doc)

    for i in range(len(objs)):
        objs[i].Label = docname + obj_suffixes[i]

    restore_Main_Tools()

    used_color_keys = color_keys
    export_file_name=out_dir+os.sep+name+'.wrl'

    export_objects = []
    for i in range(len(objs)):
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=color_keys[i],
                face_colors=None))

    scale=1/2.54
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    fusion = multiFuseObjs_wColors(FreeCAD, FreeCADGui,
                     doc.Label, objs, keepOriginals=True)
    exportSTEP(doc,name,out_dir,fusion)

    step_path = '{dir:s}/{name:s}.step'.format(dir=out_dir, name=name)

    Lic.addLicenseToStep(out_dir, '{:s}.step'.\
        format(name), LIST_license,
            STR_licAuthor,
            STR_licEmail,
            STR_licOrgSys,
            STR_licPreProc)

    FreeCAD.activeDocument().recompute()
    print("Safe to: {}".format(out_dir))
    saveFCdoc(App, Gui, doc, name, out_dir)

    #FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.activeDocument().activeView().viewAxometric()

    if save_memory == True or check_Model==True:
        doc=FreeCAD.ActiveDocument
        print("closing: {}".format(doc.Name))
        FreeCAD.closeDocument(doc.Name)

    if check_Model==True:
        runGeometryCheck(App, Gui, step_path,
            log, name, save_memory=save_memory)

if __name__ == "__main__" or __name__ == "main_generator":
    pins = []
    # select whether to include visual detail features
    highDetail = True

    close_doc=False
    if len(sys.argv) < 3:
        print("Nothing specified to build...")
        pins = cq_cad_tools.getListOfNumbers("10")
    else:
        arg = sys.argv[2]
        if arg.lower() == "all":
            close_doc=True
            pins = (3, 4, 5, 6, 7, 8, 10, 13, 15, 17, 20, 25, 30, 32)
        else:
            pins = cq_cad_tools.getListOfNumbers(sys.argv[2])

    with open(check_log_file, 'w') as log:
        log.write('# Check report for IDC Header 3d model genration\n')
        for pin in pins:
            # make an angled and a straight version
            for isAngled in (True, False):
                out_dir = MakeHeader(pin, isAngled, log, highDetail)


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

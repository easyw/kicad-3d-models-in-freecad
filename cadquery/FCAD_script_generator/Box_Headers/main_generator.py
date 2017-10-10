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

___ver___ = "1.4.2 26/02/2017"


#sleep ### NB il modello presenta errori di geometria

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

#from cq_cad_tools import say, sayw, saye

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

body_color_key = "black body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "gold pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
#marking_color_key = "light brown label"
#marking_color = shaderColors.named_colors[marking_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui

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

outdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)

# Import cad_tools
import cq_cad_tools
from cq_cad_tools import say, sayw, saye

# Reload tools
reload(cq_cad_tools)

# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements


# from export_x3d import exportX3D, Mesh
try:
    # Gui.SendMsgToActiveView("Run")
    # cq Gui
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

# import cq_parameters  # modules parameters
# from cq_parameters import *


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
    base = cq.Workplane("XY").rect(W1,L).extrude(H - T)
    #wall height H2
    H2 = 8.9 - H
    #extrude the edge up around the base
    wall = cq.Workplane("XY").workplane(offset=H-T).rect(W1,L).extrude(H2+T).faces(">Z").shell(-T)
    base = base.union(wall)
    #cut a notch out of one side 
    CW = 4.4
    cutout = cq.Workplane("XY").workplane(offset=H).rect(W1,CW).extrude(H2).translate((-W2/2,0,0))
    base = base.cut(cutout)
    #now offset the location of the base appropriately
    base = base.translate((1.27,(pins-1)*-1.27,0))
    
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
def MakeAnglePin(Z, H, L):
    #pin size
    size = 0.64
    pin = cq.Workplane("XY").workplane(offset=Z).rect(size,size).extrude(H - Z + size/2)
    pin = pin.union(cq.Workplane("YZ").workplane(offset=size/2).rect(size,size).extrude(L-size/2).translate((0,0,H)))
    #Chamfer C
    C = 0.2
    pin = pin.faces("<Z").chamfer(C)
    pin = pin.faces(">X").chamfer(C)
    # fillet on back of pin
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
def MakeAnglePinRow(n, Z, H, L):
    
    pin = MakeAnglePin(Z, H, L)
    
    for i in range(1,n):
        pin = pin.union(MakeAnglePin(Z, H, L).translate((0,-2.54 * i,0)))
    
    return pin
    
# generate a name for the pin header
def HeaderName(n, isAngled):
    if (isAngled):    
        return "IDC-Header_2x{n:02}_Pitch2.54mm_Angled".format(n=n)
    else:
        return "IDC-Header_2x{n:02}_Pitch2.54mm_Straight".format(n=n)
    
# make a pin header using supplied parameters, n pins in each row
def MakeHeader(n, isAngled):
    
    global LIST_license, docname
    name = HeaderName(n, isAngled)
    
    destination_dir="/IDC-Headers"
    
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
    script_dir=os.path.dirname(os.path.realpath(__file__))
    #models_dir=script_dir+"/../_3Dmodels"
    expVRML.say(models_dir)
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    #having a period '.' or '-' character in the model name REALLY messes with things.
    docname = name.replace(".","").replace("-","_")
    
    newdoc = App.newDocument(docname)
    App.setActiveDocument(docname)
    a_doc = Gui.ActiveDocument
    Gui.ActiveDocument=Gui.getDocument(docname)
    
    base = MakeBase(n)
    
    if (isAngled):
        pins = MakeAnglePinRow(n, -3, 5.72, 12.66)
        pins = pins.union(MakeAnglePinRow(n, -3, 3.18, 10.12).translate((2.54,0,0)))
        # rotate the base into the angled position
        base = base.rotate((0,0,0),(0,1,0),90).translate((4.66,0,5.72))
    else:
        pins = MakePinRow(n, -3.0, 8.0)
        pins = pins.union(MakePinRow(n, -3.0, 8.0).translate((2.54,0,0)))
        
    ##assign some colors
    #base_color = (50,50,50)
    #pins_color = (225,175,0)
    #
    #show(base,base_color+(0,))
    #show(pins,pins_color+(0,))
    show(base)
    show(pins)
    
    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)
    
    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],pins_color)
    #Color_Objects(Gui,objs[2],marking_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    #col_mark=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
    material_substitutions={
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pins_color_key,
        #col_mark[:-1]:marking_color_key
    }
    expVRML.say(material_substitutions)
    
    #objs=GetListOfObjects(FreeCAD, doc)
    FuseObjs_wColors(FreeCAD, FreeCADGui,
                   doc.Name, objs[0].Name, objs[1].Name)
    doc.Label=docname
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label=name
    restore_Main_Tools()
    
    #out_dir = "./generated_pinheaders/"
    
    doc.Label = docname
    
    #save the STEP file
    exportSTEP(doc, name, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', name+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,ModelName,scale,out_dir)
    objs=GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir+os.sep+name+'.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    ###save the VRML file
    ##scale=0.3937001
    ##exportVRML(doc,name,scale,out_dir)
    
    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, name,out_dir)

    if close_doc != True: # avoid operations for memory leak
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()

    return 0
    
import add_license as Lic

if __name__ == "__main__" or __name__ == "main_generator":
    
    global docname
    pins = []
    
    close_doc=False
    if len(sys.argv) < 3:
        say("Nothing specified to build...")
        pins = cq_cad_tools.getListOfNumbers("10")
    else:
        arg = sys.argv[2]
        if arg.lower() == "all":
            close_doc=True
            pins = (3, 4, 5, 6, 7, 8, 10, 13, 15, 17, 20, 25, 30, 32)
        else:
            pins = cq_cad_tools.getListOfNumbers(sys.argv[2])
    
    for pin in pins:
        for isAngled in (True, False):
            MakeHeader(pin, isAngled)
            App.setActiveDocument(docname)
            doc = FreeCAD.ActiveDocument
            if close_doc: #closing doc to avoid memory leak
                expVRML.say("closing doc to save memory")
                expVRML.say(docname)
                App.closeDocument(doc.Name)
                App.setActiveDocument("")
                App.ActiveDocument=None
                Gui.ActiveDocument=None



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



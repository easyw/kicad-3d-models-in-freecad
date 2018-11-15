# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
# This is a
# Dimensions are from Microchips Packaging Specification document:
# DS00000049BY. Body drawing is the same as QFP generator#

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8

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

__title__ = "make Valve 3D models"
__author__ = "Stefan, based on DIP script"
__Comment__ = 'make varistor 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.3 14/08/2015"

# maui import cadquery as cq
# maui from Helpers import show
from collections import namedtuple

import math
import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors


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


#################################################################################################

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

# Sphinx workaround #1
try:
    QtGui
except NameError:
    QtGui = None
#

try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery
    cq = cadquery
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

# Sphinx workaround #2
try:
    cq
    checkRequirements(cq)
except NameError:
    cq = None
#

#checking requirements

try:
    close_CQ_Example(FreeCAD, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"

destination_dir="/Valve"
# rotation = 0

import cq_parameters  # modules parameters
from cq_parameters import *


CASE_THT_TYPE = 'tht'
CASE_SMD_TYPE = 'smd'
_TYPES = [CASE_THT_TYPE, CASE_SMD_TYPE ]


def make_case_top_ECC(params):

    D = params.D                # package length
    E = params.E                # body overall width
    H = params.H                # body overall height
    A1 = params.A1              # package height
    pin = params.pin            # Pins
    rotation = params.rotation  # Rotation if required
    pintype = params.pintype    # Pin type , like SMD or THT
    center = params.center      # Body center
    
    FreeCAD.Console.PrintMessage('make_case_top_ECC\r\n')
    #
    #
    #
    p0 = pin[0]
    p1 = pin[1]
    x0 = p0[0]
    y0 = p0[1]

    ff = D / 8.0

    case = cq.Workplane("XY").workplane(offset=A1 + H * 0.90 - (D / 4.0)).moveTo(center[0], center[1]).circle(D / 2.0, False).extrude((D / 4.0))
    case = case.faces(">Z").edges(">Y").fillet(D / 4.1)

    case2=cq.Workplane("XY").workplane(offset=A1 + H * 0.90).moveTo(center[0], center[1]).circle(D / 8.0, False).extrude(A1 + H * 0.10 )
    case = case.union(case2)
    case = case.faces(">Z").edges(">Y").fillet(D / 8.1)

    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)

    return (case)


def make_case_ECC(params):

    D = params.D                # package length
    E = params.E                # body overall width
    H = params.H                # body overall height
    A1 = params.A1              # package height
    pin = params.pin            # Pins
    rotation = params.rotation  # Rotation if required
    pintype = params.pintype    # Pin type , like SMD or THT
    center = params.center      # Body center
    
    FreeCAD.Console.PrintMessage('make_case_ECC\r\n')
    #
    #
    #
    As = A1
    Hs = A1 + H * 0.90 - (D / 4.0)
    Ds = D / 2.0

    ffs = D / 12.0
    case = cq.Workplane("XY").workplane(offset=As).moveTo(center[0], center[1]).circle(Ds, False).extrude(Hs)
    case = case.faces("<Z").edges("<Y").fillet(ffs)

    dd = 0.2
    At = As + (2.0 * dd)
    Dt = Ds - (2.0 * dd)
    Ht = Hs - (2.0 * dd)
    fft = Dt / 16.0
    case1 = cq.Workplane("XY").workplane(offset=At).moveTo(center[0], center[1]).circle(Dt, False).extrude(Ht)
    case1 = case1.faces("<Z").edges("<Y").fillet(fft)
    
    case = case.cut(case1)

    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)

    return (case)

    
def make_pins_ECC(params):

    D = params.D                # package length
    H = params.H                # body overall height
    A1 = params.A1              # Body seperation height
    b = params.b                # pin diameter or pad size
    ph = params.ph              # pin length
    rotation = params.rotation  # rotation if required
    pin = params.pin            # pin/pad cordinates
    npthhole = params.npthhole  # NPTH holes
    center = params.center      # Body center
    
    FreeCAD.Console.PrintMessage('make_pins_ECC \r\n')

    p = pin[0]
    pins = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0))
    pins = pins.faces("<Z").fillet(b / 5.0)
    
    for i in range(1, len(pin)):
        p = pin[i]
        pint = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0))
        pint = pint.faces("<Z").fillet(b / 5.0)
        pins = pins.union(pint)

    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)

    return (pins)


def make_npth_pins_ECC(params):

    D = params.D                # package length
    E = params.E                # body overall width
    H = params.H                # body overall height
    A1 = params.A1              # Body seperation height
    b = params.b                # pin diameter or pad size
    ph = params.ph              # pin length
    rotation = params.rotation  # rotation if required
    pin = params.pin            # pin/pad cordinates
    npthhole = params.npthhole  # NPTH holes
    center = params.center      # Body center

    FreeCAD.Console.PrintMessage('make_npth_pins_ECC \r\n')

    
    pins = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo(center[0], center[1]).circle((D / 2.0) - 0.5, False).extrude(A1 + 2.0)
    
    pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo((center[0] - (D / 2.0)) + 3.0, center[1]).circle(0.5, False).extrude((2.0 * H) / 3.0)
    pint = pint.faces(">Z").fillet(0.4)
    pins = pins.union(pint)
    #
    pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo((center[0] + (D / 2.0)) - 3.0, center[1]).circle(0.5, False).extrude((2.0 * H) / 3.0)
    pint = pint.faces(">Z").fillet(0.4)
    pins = pins.union(pint)
    #
    pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo(center[0] - 1.0, center[1]).circle(0.5, False).extrude((2.0 * H) / 3.0)
    pint = pint.faces(">Z").fillet(0.4)
    pins = pins.union(pint)
    #
    pint = cq.Workplane("XY").workplane(offset=A1 + 0.5).moveTo(center[0] + 1.0, center[1]).circle(0.5, False).extrude((2.0 * H) / 3.0)
    pint = pint.faces(">Z").fillet(0.4)
    pins = pins.union(pint)
    #
    pint = cq.Workplane("XY").workplane(offset=A1 + (H / 4.0)).moveTo(center[0], center[1]).rect(D / 1.5, D / 1.5).extrude(H / 4.0)
    pint = pint.faces(">Z").fillet(D / 5.0)
    pint = pint.faces("<Z").fillet(D / 5.0)
    pins = pins.union(pint)


    
    if npthhole != None:
        FreeCAD.Console.PrintMessage('make_npth_pins_ECC 2\r\n')
        if len(npthhole) > 0:
            FreeCAD.Console.PrintMessage('make_npth_pins_ECC 3\r\n')
            p = npthhole[0]
            b = p[2]
            ph = p[3]
            pint = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 0.1))
            pint = pint.faces("<Z").fillet(b / 5.0)
            pins = pins.union(pint)

            for i in range(1, len(npthhole)):
                p = npthhole[i]
                b = p[2]
                ph = p[3]
                pint = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0))
                pint = pint.faces("<Z").fillet(b / 5.0)
                pins = pins.union(pint)


    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)

    return (pins)



def make_case_top_Glimm(params):

    D = params.D                # package length
    E = params.E                # body overall width
    H = params.H                # body overall height
    A1 = params.A1              # Body seperation height
    b = params.b                # pin diameter or pad size
    ph = params.ph              # pin length
    rotation = params.rotation  # rotation if required
    pin = params.pin            # pin/pad cordinates
    npthhole = params.npthhole  # NPTH holes
    center = params.center      # Body center

    FreeCAD.Console.PrintMessage('make_case_top_Glimm\r\n')

    As = A1
    Es = E
    Ds = D
    Hs = A1+H

    dd = 1.5
    At = As + dd
    Et = Es - (2.0 * dd)
    Dt = Ds - (2.0 * dd)
    Ht = Hs - (2.0 * dd)
    Dt = D - (2.0 * dd)
    fft = Dt / 2.1
    case1 = cq.Workplane("XY").workplane(offset=At).moveTo(center[0], center[1]).rect(Et, Dt).extrude(Ht)
    case1 = case1.faces("<X").edges(">Y").fillet(fft)
    case1 = case1.faces("<X").edges("<Y").fillet(fft)
    case1 = case1.faces(">X").edges(">Y").fillet(fft)
    case1 = case1.faces(">X").edges("<Y").fillet(fft)
    case1 = case1.faces(">Z").fillet(fft)
    case1 = case1.faces("<Z").fillet(fft)
    
    return (case1)


def make_case_Glimm(params):

    D = params.D                # package length
    E = params.E                # body overall width
    H = params.H                # body overall height
    A1 = params.A1              # package height
    pin = params.pin            # Pins
    rotation = params.rotation  # Rotation if required
    pintype = params.pintype    # Pin type , like SMD or THT
    center = params.center      # Body center
    
    FreeCAD.Console.PrintMessage('make_case_Glimm\r\n')
    #
    #
    #

    As = A1
    Es = E
    Ds = D
    Hs = A1+H
    ff = Ds / 2.1
    case = cq.Workplane("XY").workplane(offset=As).moveTo(center[0], center[1]).rect(Es, Ds).extrude(Hs)
    case = case.faces("<X").edges(">Y").fillet(ff)
    case = case.faces("<X").edges("<Y").fillet(ff)
    case = case.faces(">X").edges(">Y").fillet(ff)
    case = case.faces(">X").edges("<Y").fillet(ff)
    case = case.faces(">Z").fillet(ff)
    case = case.faces("<Z").fillet(ff)

    
    dd = 0.1
    At = As + dd
    Et = Es - (2.0 * dd)
    Dt = Ds - (2.0 * dd)
    Ht = Hs - (2.0 * dd)
    Dt = D - (2.0 * dd)
    fft = Dt / 2.1
    case1 = cq.Workplane("XY").workplane(offset=At).moveTo(center[0], center[1]).rect(Et, Dt).extrude(Ht)
    case1 = case1.faces("<X").edges(">Y").fillet(fft)
    case1 = case1.faces("<X").edges("<Y").fillet(fft)
    case1 = case1.faces(">X").edges(">Y").fillet(fft)
    case1 = case1.faces(">X").edges("<Y").fillet(fft)
    case1 = case1.faces(">Z").fillet(fft)
    case1 = case1.faces("<Z").fillet(fft)
    
    case = case.cut(case1)
    
    
#    case = case.faces("<Y").shell(0.1)

    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)

    return (case)


def make_pins_Glimm(params):

    D = params.D                # package length
    H = params.H                # body overall height
    A1 = params.A1              # Body seperation height
    b = params.b                # pin diameter or pad size
    ph = params.ph              # pin length
    rotation = params.rotation  # rotation if required
    pin = params.pin            # pin/pad cordinates
    npthhole = params.npthhole  # NPTH holes
    center = params.center      # Body center
    
    FreeCAD.Console.PrintMessage('make_pins_ECC \r\n')

    p = pin[0]
    pins = cq.Workplane("XY").workplane(offset=A1 + 1.0 + (H / 2.0)).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0 + (H / 2.0)))
    pins = pins.faces("<Z").fillet(b / 5.0)
    
    for i in range(1, len(pin)):
        p = pin[i]
        pint = cq.Workplane("XY").workplane(offset=A1 + 1.0 + (H / 2.0)).moveTo(p[0], -p[1]).circle(b / 2.0, False).extrude(0 - (ph + A1 + 1.0 + (H / 2.0)))
        pint = pint.faces("<Z").fillet(b / 5.0)
        pins = pins.union(pint)

    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)

    return (pins)


def make_npth_pins_Glimm(params):

    D = params.D                # package length
    E = params.E                # body overall width
    H = params.H                # body overall height
    A1 = params.A1              # Body seperation height
    b = params.b                # pin diameter or pad size
    ph = params.ph              # pin length
    rotation = params.rotation  # rotation if required
    pin = params.pin            # pin/pad cordinates
    npthhole = params.npthhole  # NPTH holes
    center = params.center      # Body center

    FreeCAD.Console.PrintMessage('make_npth_pins_RSX\r\n')

    p = pin[0]
    pins = cq.Workplane("XY").workplane(offset=A1).moveTo(p[0], -p[1]).circle(0.05, False).extrude(0 - (A1 + 0.1))

    return (pins)





def make_3D_model(models_dir, variant):

    LIST_license = ["",]
    modelName = all_params[variant].modelName

    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)

    npth_pins = None

    if (all_params[variant].serie == 'ECC'):
        case_top = make_case_top_ECC(all_params[variant])
        case = make_case_ECC(all_params[variant])
        pins = make_pins_ECC(all_params[variant])
        npth_pins = make_npth_pins_ECC(all_params[variant])
        show(case_top)
        show(case)
        show(pins)
        show(npth_pins)

    elif (all_params[variant].serie == 'GLIMM'):
        case_top = make_case_top_Glimm(all_params[variant])
        case = make_case_Glimm(all_params[variant])
        pins = make_pins_Glimm(all_params[variant])
        npth_pins = make_npth_pins_Glimm(all_params[variant])
        show(case_top)
        show(case)
        show(pins)
        show(npth_pins)
    else:
        print("Serie " + all_params[variant].serie + " is not supported")
        FreeCAD.Console.PrintMessage('\r\nSerie ' + all_params[variant].serie + ' is not supported\r\n')
        sys.exit()

 
    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)
 
    body_top_color_key = all_params[variant].body_top_color_key
    body_color_key = all_params[variant].body_color_key
    pin_color_key = all_params[variant].pin_color_key
    npth_pin_color_key = all_params[variant].npth_pin_color_key

    body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()
    npth_pin_color = shaderColors.named_colors[npth_pin_color_key].getDiffuseFloat()

    Color_Objects(Gui,objs[0],body_top_color)
    Color_Objects(Gui,objs[1],body_color)
    Color_Objects(Gui,objs[2],pin_color)
    Color_Objects(Gui,objs[3],npth_pin_color)

    col_body_top=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_body=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
    col_npth_pin=Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
    
    material_substitutions={
        col_body_top[:-1]:body_top_color_key,
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pin_color_key,
        col_npth_pin[:-1]:npth_pin_color_key
    }

    expVRML.say(material_substitutions)
    while len(objs) > 1:
            FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
            del objs
            objs = GetListOfObjects(FreeCAD, doc)
    doc.Label = CheckedmodelName

    del objs
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = CheckedmodelName
    restore_Main_Tools()

    script_dir=os.path.dirname(os.path.realpath(__file__))
    expVRML.say(models_dir)
    out_dir=models_dir+destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    exportSTEP(doc, modelName, out_dir)
    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")
    Lic.addLicenseToStep(out_dir+'/', modelName+".step", LIST_license,\
                       STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

    # scale and export Vrml model
    scale=1/2.54
    #exportVRML(doc,modelName,scale,out_dir)
    del objs
    objs=GetListOfObjects(FreeCAD, doc)
    expVRML.say("######################################################################")
    expVRML.say(objs)
    expVRML.say("######################################################################")
    export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
    export_file_name=out_dir+os.sep+modelName+'.wrl'
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    #expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
    #scale=0.3937001
    #exportVRML(doc,modelName,scale,out_dir)
    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, modelName,out_dir)
    #display BBox
    Gui.activateWorkbench("PartWorkbench")
    Gui.SendMsgToActiveView("ViewFit")
    Gui.activeDocument().activeView().viewAxometric()
    #FreeCADGui.ActiveDocument.activeObject.BoundingBox = True


def run():
    ## # get variant names from command line

    return

#import step_license as L
import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator_Converter_DCDC":

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

    if len(sys.argv) < 3:
        FreeCAD.Console.PrintMessage('No variant name is given! building RV_Disc_D12mm_W3.9mm_P7.5mm\r\n')
        model_to_build='Valve_ECC-83-1'
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]

    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n' + variant + '\r\n\r\n')
        if not variant in all_params:
            print("Parameters for %s doesn't exist in 'all_params', skipping. " % variant)
            continue

        make_3D_model(models_dir, variant)

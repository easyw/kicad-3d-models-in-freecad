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

## to run the script just do: FreeCAD main_generator.py modelName (or all)
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

__title__ = "make THT resistor 3D models"
__author__ = "maurice, hyOzd and grob"
__Comment__ = 'make THT resistor 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "2.0.0 2020-09-30"


save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'
global_3dpath = '../_3Dmodels/'

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


# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
#from Gui.Command import *


if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui


#################################################################################################

# Import cad_tools
import cq_cad_tools
# Reload tools
def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)

reload_lib(cq_cad_tools)


# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements,  runGeometryCheck

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
    msg = "missing CadQuery 0.5.2 or later Module!\r\n\r\n"
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
    FreeCAD.Console.PrintMessage("CQ 030 doesn't open example file")


import cq_parameters  # modules parameters
from cq_parameters import all_params, dest_dir_prefix


# Make marking (only applies to array at this point)
def make_marking(params, n=1):
    if (params.shape == 'array'):
        mr = 0.5 # radius of dot
        mt = 0.01 # thickness of marking
        moff = 2.0 # offset of marking from edge of body
        c = 0.3 # height of body off board
        marking = cq.Workplane("XZ").circle(mr).extrude(mt).translate((moff-params.px/2,-params.w/2,c+params.d-moff))
    else:
        marking = None
    return marking

    # make a resistor body based on input parameters
def make_body(params, n=1):

    if (params.shape == 'array'):
        # resistor array body: rectangle with rounded corners
        c = 0.3 # height off board
        l = params.px * n # length of body
        body = cq.Workplane("YZ").rect(params.w, params.d).extrude(l)
        body = body.translate((-params.px/2,0,c+params.d/2))
        body = body.edges().fillet(params.w/3)
    elif (params.shape == 'bare'):
        # bare metal element - note that pins below board level are done in the MakePins routine
        c = 1.0 # height off board
        t = 1.0 # element thickness
        r = t*1.5 # radius of bend
        arco = (1-sqrt(2)/2)*r # helper value sets a mid point in the radius arcs
        h = params.d - t/2 - c # height of centerline of element - model gets moved up by c later.
        # construct path for element
        path = cq.Workplane("XZ").lineTo(0,h-r).threePointArc((arco,h-arco),(r,h)).lineTo(params.px-r,h).threePointArc((params.px-arco,h-arco),(params.px,h-r)).lineTo(params.px,0)
        body = cq.Workplane("XY").rect(t,params.w).sweep(path).translate((0,0,c))
        # make wee circular feet
        body = body.union(cq.Workplane("XY").circle(1.6).extrude(c*2))
        body = body.union(cq.Workplane("XY").circle(1.6).extrude(c*2).translate((params.px,0,0)))
    else:
        if (params.orient == 'v'):
            if (params.shape == 'din'):
                # vertical cylindrical resistor body
                body = cq.Workplane("XY").circle(params.d/2*0.9).extrude(params.l)
                body = body.union(cq.Workplane("XY").circle(params.d/2).extrude(params.l/4))
                body = body.union(cq.Workplane("XY").workplane(offset=params.l*3/4).circle(params.d/2).extrude(params.l/4))
                body = body.edges(">Z or <Z").fillet(params.d/4)
            else: #(params.shape == 'power'):
                # all vertical types that are not din will make a box!
                body = cq.Workplane("XY").rect(params.d, params.w).extrude(params.l)
            # sits off the board by 1mm
            body = body.translate((0,0,1.0))
        else:
            if (params.shape == 'din'):
                # horizontal cylindrical resistor
                body = cq.Workplane("YZ").circle(params.d/2*0.9).extrude(params.l)
                body = body.union(cq.Workplane("YZ").circle(params.d/2).extrude(params.l/4))
                body = body.union(cq.Workplane("YZ").workplane(offset=params.l*3/4).circle(params.d/2).extrude(params.l/4))
                body = body.edges(">X or <X").fillet(params.d/4)
            else: # elif (params.shape == 'power') or (params.shape == 'box') or (params.shape == 'radial') or (params.shape == 'shunt'):
                # otherwise it's a box
                body = cq.Workplane("YZ").rect(params.w, params.d).extrude(params.l)
            if (params.shape == 'radial') and (params.py == 0.0):
                # for the vishay series of radial resistors
                # add the cool undercut from the datasheet http://www.vishay.com/docs/30218/cpcx.pdf
                # doesn't apply to the centered-pin vitrohm types (with py>0) - see below
                flat = 1.0 # length of flat part at edges
                cut_h = 3.0 # height of cutout
                # generate a trapezoidal body to cut out of main body
                cutbody = (
                    cq.Workplane("XZ").workplane(offset=-params.w/2)
                    .center(flat, -params.d/2)
                    .lineTo(cut_h, cut_h)
                    .lineTo(params.l-2*flat-cut_h, cut_h)
                    .lineTo(params.l-2*flat,0)
                    .close()
                    .extrude(params.w)
                )
                body = body.cut(cutbody) # cut!
            if (params.shape == "radial") and (params.py != 0.0):
                # center on pin 1 http://www.vitrohm.com/content/files/vitrohm_series_kvs_-_201702.pdf
                body = body.translate((-params.l/2,0,params.d/2))
            else:
                # sit on board, and center between pads
                body = body.translate(((params.px-params.l)/2,0,params.d/2))
    return body

# makes a simple rectangular array pin, including the larger section above board
# c is height above board
# zbelow is negative value, length of pin below board level
def MakeSingleArrayPin(c, zbelow):
    pin = cq.Workplane("XY").rect(0.5,0.3).extrude(c-zbelow).translate((0,0,zbelow))
    pin = pin.union(cq.Workplane("XY").rect(1.14,0.5).extrude(c))
    return pin

# make a bent resistor pin - suitable for din and power resistors, horiz or vert
def make_pins(params, n=1):

    zbelow = -3.0 # negative value, length of pins below board level
    minimumstraight = 1.0 # short straight section of pins next to bends, body

    # bent pin - upside down u shape
    if (params.shape == "din") or (params.shape=="power") or (params.shape=="shunt"):
        r = params.pd*1.5 # radius of pin bends
        arco = (1-sqrt(2)/2)*r # helper factor to create midpoints of profile radii
        if (params.orient == 'v'):
            # vertical
            h = params.l + 2*minimumstraight + r
        else:
            # horizontal
            h = params.d / 2
        # create the path and pin
        path = (
            cq.Workplane("XZ")
            .lineTo(0,h-r-zbelow)
            .threePointArc((arco,h-arco-zbelow),(r,h-zbelow))
            .lineTo(params.px-r,h-zbelow)
            .threePointArc((params.px-arco,h-arco-zbelow),(params.px,h-r-zbelow))
            .lineTo(params.px,0)
            )
        pin = cq.Workplane("XY").circle(params.pd/2).sweep(path).translate((0,0,zbelow))
    # simple pins using px/py - just two cylinders at appropriate locations
    elif (params.shape == "box") or (params.shape == "radial") or (params.shape == "bare"):
        # extends somewhat above the board to allow for more complex body shapes, e.g. radial
        aboveboardfactor = 0.5
        if (params.shape == "bare"):
            aboveboardfactor = 0 # don't extend up if making a bare resistor
        pin = cq.Workplane("XY").circle(params.pd/2).extrude(params.d*aboveboardfactor-zbelow).translate((0,0,zbelow))
        pin = pin.union(pin.translate((params.px,params.py,0))) # add second pin
    elif (params.shape == "array"):
        # resistor array has rectangular pins
        c = 0.8 # height off board - from datasheet
        pin = MakeSingleArrayPin(c, zbelow)
        for i in range(1,n):
            pin = pin.union(MakeSingleArrayPin(c, zbelow).translate((i*params.px,0,0)))

    # add extra pins for shunt package using py as pitch
    if (params.shape == "shunt"):
        pin = pin.union(cq.Workplane("XY").circle(params.pd/2).extrude(zbelow).translate(((params.px-params.py)/2,0,0)))
        pin = pin.union(cq.Workplane("XY").circle(params.pd/2).extrude(zbelow).translate(((params.px+params.py)/2,0,0)))

    return pin


def make_3D_model(models_dir, variant, n=1):

    LIST_license = ["",]

    if n == 1:
        modelName = variant    # the key is the model name
    else:
        modelName = variant + "{0}".format(n) # except for arrays

    CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedmodelName)
    App.setActiveDocument(CheckedmodelName)
    Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)

    body = make_body(all_params[variant], n)
    pins = make_pins(all_params[variant], n)
    marking = make_marking(all_params[variant], n)

    show(body)
    show(pins)
    if marking != None:
        show(marking)


    doc = FreeCAD.ActiveDocument
    objs=GetListOfObjects(FreeCAD, doc)

    body_color_key = all_params[variant].body_color_key
    pin_color_key = all_params[variant].pin_color_key

    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

    Color_Objects(Gui,objs[0],body_color)
    Color_Objects(Gui,objs[1],pin_color)

    col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
    col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]

    material_substitutions={
        col_body[:-1]:body_color_key,
        col_pin[:-1]:pin_color_key
    }

    # white dot marking (for array pin1)
    if n>1:
        Color_Objects(Gui,objs[2], shaderColors.named_colors['white body'].getDiffuseFloat())
        col_marking=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
        material_substitutions[col_marking[:-1]] = 'white body'

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
    out_dir=models_dir+os.sep+dest_dir_prefix

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    step_path = '{dir:s}/{name:s}.step'.format(dir=out_dir, name=modelName)
    exportSTEP(doc, modelName, out_dir)


    if LIST_license[0]=="":
        LIST_license=Lic.LIST_int_license
        LIST_license.append("")

    Lic.addLicenseToStep(out_dir, '{:s}.step'.format(modelName),
            LIST_license,
            cq_parameters.LICENCE_Info.STR_licAuthor,
            cq_parameters.LICENCE_Info.STR_licEmail,
            cq_parameters.LICENCE_Info.STR_licOrgSys,
            cq_parameters.LICENCE_Info.STR_licPreProc)

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
    # expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    # Save the doc in Native FC format
    doc.recompute()
    saveFCdoc(App, Gui, doc, modelName, out_dir)


    #FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.activeDocument().activeView().viewAxometric()

    if save_memory == True or check_Model==True:
        FreeCAD.closeDocument(doc.Name)
        os.remove (out_dir+os.sep+modelName+'.FCStd')

    if check_Model==True:
        with open(out_dir+os.sep+check_log_file, 'a+') as log:
            log.write('# Check report for THT resistors model generator\n')
            runGeometryCheck(App, Gui, step_path, log, modelName, save_memory=save_memory)
            log.close()


import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":

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
        FreeCAD.Console.PrintMessage('No variant name is given! building R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal\r\n')
        model_to_build="R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"
    else:
        model_to_build=sys.argv[2]

    if model_to_build == "all":
        variants = all_params.keys()
    else:
        variants = [model_to_build]


    for variant in variants:
        FreeCAD.Console.PrintMessage('\r\n' + variant + '\r\n\r\n')
        if not variant in all_params:
            FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'all_params', skipping. " % variant)
            continue

        # pinrange should be extracted from 'variant' !
        if (all_params[variant].shape == "array"):
            pinrange = range (4, 15)
        else:
            pinrange = range (1,2)

        for pin_number in pinrange:
            make_3D_model(models_dir, variant, pin_number)

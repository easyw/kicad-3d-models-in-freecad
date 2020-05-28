# -*- coding: utf8 -*-
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
##   https://github.com/jmwright/cadquery-freecad-module2512 

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

__title__ = "make terminal block phoenix 3D models"
__author__ = "maurice & Frank/Shack & grob6000"
__Comment__ = 'make termianl block phoenix 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.0 14/05/2020"

# thanks to Frank Severinsen Shack for including vrml materials

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple
global save_memory
save_memory = False #reducing memory consuming for all generation params

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors

#body_color_key = "brown body"
#body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()

# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
import yaml
#from Gui.Command import *

import logging
logging.getLogger('builder').addHandler(logging.NullHandler())
#logger = logging.getLogger('builder')
#logging.info("Begin")

outdir=os.path.dirname(os.path.realpath(__file__)+"/../_3Dmodels")
scriptdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)
sys.path.append(scriptdir)

#import PySide
#from PySide import QtGui, QtCore
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


# Import cad_tools
import cq_cad_tools
# Reload tools
try:
    reload(cq_cad_tools)
except:
    import importlib
    importlib.reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements, SimpleCopy_wColors
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
    print ("CQ doesn't open example file")

screw_clearance = 0.10
screw_t = 0.70
screw_down = 0.20

def make_pin(model, i, bs):

    # make pin
    pinsize = 1.0
    px = 1.0
    py = 1.0
    if 'pin_size' in bs:
        px = bs['pin_size']
    if 'pin_sizex' in bs:
        px = bs['pin_sizex']
    if 'pin_sizey' in bs:
        py = bs['pin_sizey']
    pinl = bs['pin_l']
    h = bs['height']
    FreeCAD.Console.PrintMessage('  Making pin...\n')
    if (bs['pin_shape'] == "rect"):
        pin = cq.Workplane("XY", origin=(0,0,bs['opening_z'])).workplane().rect(px,py).extrude(-1*(pinl + bs['opening_z']))
    else:
        pin = cq.Workplane("XY", origin=(0,0,bs['opening_z'])).workplane().circle(px/2).extrude(-1*(pinl + bs['opening_z']))
    
    # make terminal
    FreeCAD.Console.PrintMessage('  Making terminal...\n')
    pin = pin.union(cq.Workplane("XY",origin=(0,0,bs['opening_z'])).rect(bs['opening_w'], bs['terminal_d']).extrude(bs['opening_h']))

    # screw model
    FreeCAD.Console.PrintMessage('  Making screw...\n')
    pin = pin.union(cq.Workplane("XY",origin=(0,bs['screw_y'],bs['opening_z']+bs['opening_h'])).circle(bs['screw_dia']/2 - screw_clearance).extrude(h-bs['opening_h']-bs['opening_z']-screw_down))
    pin = pin.cut(cq.Workplane("XY",origin=(0,bs['screw_y'],h-screw_down)).rect(screw_t, bs['screw_dia']).extrude(-1*screw_t))
    if bs['screw_cross']:
        pin = pin.cut(cq.Workplane("XY",origin=(0,bs['screw_y'],h-screw_down)).rect(bs['screw_dia']/2,screw_t).extrude(-1*screw_t))
   
    # make terminal hole
    FreeCAD.Console.PrintMessage('  Making terminal hole...\n')
    if bs['terminal_hole'] == 'rect':
        hole = cq.Workplane("XZ",origin=(0,bs['terminal_d']/2,bs['terminal_hole_z'])).rect(bs['terminal_hole_w'],bs['terminal_hole_h']).extrude(bs['terminal_d'])
        if bs['terminal_hole_r']>0:
            hole = hole.edges("|Y").fillet(bs['terminal_hole_r'])
        pin = pin.cut(hole)
    else:
        pin = pin.cut(cq.Workplane("XZ",origin=(0,bs['terminal_d']/2,bs['terminal_hole_z'])).circle(bs['terminal_hole_d']).extrude(bs['terminal_d']))
    
    # move into position
    FreeCAD.Console.PrintMessage('  Moving pin...\n')
    pin = pin.translate((bs['pitch']*i,0,0))

    return pin
    
def get_bodystyle(model, all_params):

    if 'bodystyle' in all_params[model]:
        if all_params[model]['bodystyle'] in all_params['bodystyles']:
            bs = all_params['bodystyles'][all_params[model]['bodystyle']]
            # allow overrides in model def
            for k in bs.keys():
                if k in all_params[model]:
                    bs[k] = all_params[model][k]
        return bs
    
    # not defined - pitch required to defined other values
    if 'pitch' in all_params[model]:
        p = all_params[model]['pitch']
    else:
        p = 5.0;
    
    bsdefault = {
        'pitch': p,
        'height': 12,
        'width' : 8,
        'chf' : False,
        'chb' : False,
        'opening_w' : p*0.8,
        'opening_h' : p*0.8,
        'opening_z' : 1.0,
        'terminal_d' : p*0.8,
        'terminal_hole' : 'circle',
        'terminal_hole_d' : p*0.6,
        'screw_dia' : p*0.8,
        'screw_t': 0,
        'screw_cross' : False,
        'pin_shape' : 'circle',
        'pin_size' : 1.0,
        'pin_l' : 3.5,
        'key': 'none',
        'pinslot': 0
        
        }    
    #allow overrides again
    for k in bsdefault.keys():
        if k in all_params[model]:
            bsdefault[k] = all_params[model][k]
    return bsdefault
        
def make_dovetail(body, bs):
    dt_w = bs['key_w']
    dt_l = bs['key_l']
    dt_h = bs['key_h']
    return body.moveTo(0,dt_w/4).lineTo(dt_l,dt_w/2).lineTo(dt_l,-0.5*dt_w).lineTo(0,-0.25*dt_w).close().extrude(dt_h)

    

def make_part(model, all_params):

    # bodystyle defines series features/dimensions
    bs = get_bodystyle(model, all_params)
    
    # get often-used params
    p = bs['pitch']
    w = bs['width']
    n = all_params[model]['n']
    h = bs['height']
    bo = bs['backoffset']
    
    # calculate helper dimensions
    l = p * n
    
    # make base body (rectangle)
    if 'endpadding' in bs:
        ep = bs['endpadding']
    else:
        ep = 0;
    body = cq.Workplane("YZ", origin=(-1*ep,0,0)).rect(w, h, False).extrude(l+2*ep)

    
    # add front nub for pt (has to happen first)
    if 'phoenix_pt' in all_params[model]['bodystyle']:
        FreeCAD.Console.PrintMessage('Making nubs...\n')
        if all_params[model]['bodystyle'] == "phoenix_pt_5":
            nub_h = 3.5
            nub_w = 0.75
        else: # _35
            nub_h = 2.85
            nub_w = 0.55
        body = body.union(cq.Workplane("YZ",origin=(0,-1*nub_w,h-bs['chf_z']-nub_h)).rect(nub_w, nub_h, False).extrude(l).edges("<Y").edges("|X").fillet(nub_w*0.8))
    
    
    # common style features
    for i in range(0,n): # per opening
        xcl = p*(i+0.5)
        FreeCAD.Console.PrintMessage('Making body pinwise features for pin ' + str(i+1) + ' @ x=' + str(xcl) + '...\n')
        FreeCAD.Console.PrintMessage('  Making cutout...\n')
        body = body.cut(cq.Workplane("XZ",origin=(xcl,-100,bs['opening_z']+bs['opening_h']/2)).rect(bs['opening_w'], bs['opening_h']).extrude(-1*(100+w-bo+(bs['terminal_d']/2)))) # opening
        body = body.cut(cq.Workplane("XY",origin=(xcl,w-bo+bs['screw_y'],h)).circle(bs['screw_dia']/2).extrude(-1*(h-bs['opening_z']))) # screw hole
        pinco_w = 2.2
        if 'pinslot' in bs and bs['pinslot'] > 0:
            FreeCAD.Console.PrintMessage('  Making pinslot...\n')
            body = body.cut(cq.Workplane("XZ",origin=(xcl,0,bs['opening_z']/2)).rect(bs['pinslot'],bs['opening_z']).extrude(-1*(w-bo+bs['pinslot']/2)).edges(">Y").edges("|Z").fillet(bs['pinslot']*0.45)) # slot for pin
        if 'phoenix_pt' in all_params[model]['bodystyle']:
            FreeCAD.Console.PrintMessage('  Cleaning nub...\n')
            body = body.cut(cq.Workplane("XY",origin=(xcl,-50,0)).rect(bs['opening_w'],100).extrude(h)) # clear out nub (anything forward of front face)
        if all_params[model]['bodystyle'] == "phoenix_pt_5":
            backhole_d = 2.2
            backhole_h = 5.35
            FreeCAD.Console.PrintMessage('  Adding backhole...\n')
            body = body.cut(cq.Workplane("XZ",origin=(xcl,w,backhole_h)).circle(backhole_d/2).extrude(w))
        if 'phoenix_m' in all_params[model]['bodystyle']:
            FreeCAD.Console.PrintMessage('  Lofting entry...\n')
            if 'mkds_3' in all_params[model]['bodystyle']:
                loft_w = 4.00
                loft_zu = 3.15
                loft_zd = 2.35
                loft_d = 2.20
            elif 'mpt_05' in all_params[model]['bodystyle']:
                loft_w = 2.15
                loft_zu = 2.40
                loft_zd = 2.05
                loft_d = 1.15              
            else: #mkds_15
                loft_w = 3.60
                loft_zu = 3.05
                loft_zd = 2.15
                loft_d = 0.80    
            body = body.cut(cq.Workplane("XZ",origin=(xcl,loft_d,bs['opening_z']+bs['opening_h']/2)).rect(bs['opening_w'], bs['opening_h']).workplane(offset=loft_d).moveTo(-0.5*loft_w, -1*loft_zd).lineTo(-0.5*loft_w, loft_zu).lineTo(0.5*loft_w,loft_zu).lineTo(0.5*loft_w,-1*loft_zd).close().loft())
        if all_params[model]['bodystyle'] == "phoenix_mpt_05_254" and n < 4:
            FreeCAD.Console.PrintMessage('  Adding locator pin...\n')
            body = body.union(cq.Workplane("XY",origin=(xcl, w-bo-p, 0)).circle(0.55).extrude(-1.50))
            
    if bs['chf']: # front chamfer
        FreeCAD.Console.PrintMessage('Making front chamfer...\n')
        if bs['chf_ins'] > 0:
            body = body.cut(cq.Workplane("YZ", origin=(-1*ep,0,0)).moveTo(0,h).lineTo(bs['chf_y']+bs['chf_ins'], h).lineTo(bs['chf_ins'],h-bs['chf_z']).lineTo(0,h-bs['chf_z']).close().extrude(l+2*ep))
        else:
            body = body.cut(cq.Workplane("YZ",origin=(-1*ep,0,0)).moveTo(0,h).lineTo(bs['chf_y'], h).lineTo(0,h-bs['chf_z']).close().extrude(l+2*ep))
    if bs['chb']: # front chamfer
        FreeCAD.Console.PrintMessage('Making back chamfer...\n')
        if bs['chb_ins'] > 0:
            body = body.cut(cq.Workplane("YZ",origin=(-1*ep,0,0)).moveTo(w,h).lineTo(w-bs['chb_y']-bs['chb_ins'], h).lineTo(w-bs['chb_ins'],h-bs['chb_z']).lineTo(w,h-bs['chb_z']).close().extrude(l+2*ep))
        else:
            body = body.cut(cq.Workplane("YZ",origin=(-1*ep,0,0)).moveTo(w,h).lineTo(w-bs['chb_y'], h).lineTo(w,h-bs['chb_z']).close().extrude(l+2*ep))

    if all_params[model]['bodystyle'] == "phoenix_pt_5":
        FreeCAD.Console.PrintMessage('Making back ribs...\n')
        rib_w = 0.80
        rib_h = 9.36
        for i in range(1,n):
            xcl = p*i
            body = body.union(cq.Workplane("XZ",origin=(xcl,w,rib_h/2)).rect(rib_w,rib_h).extrude(bs['chb_y']))

    # add keys
    if 'key' in bs and not bs['key'] == 'none':
        k = 0
        if bs['key_l']<0:
           k = l; 
        key_z = 0
        klat = bs['key_lat']
        if bs['key_vert'] == 'top':
            key_z = h-bs['key_h']    
        key_y = bs['key_off']
        if bs['key'] == 'dovetail':
            if klat == 'front' or klat == 'both':
                FreeCAD.Console.PrintMessage('Making front dovetails...\n')
                body = body.cut(make_dovetail(cq.Workplane("XY", origin=(0+k,(w-bo)-key_y,key_z)), bs))
                body = body.union(make_dovetail(cq.Workplane("XY", origin=(l-k,(w-bo)-key_y,key_z)), bs))
            if klat == 'back' or klat == 'both':
                FreeCAD.Console.PrintMessage('Making back dovetails...\n')
                body = body.cut(make_dovetail(cq.Workplane("XY", origin=(0+k,(w-bo)+key_y,key_z)), bs))
                body = body.union(make_dovetail(cq.Workplane("XY", origin=(l-k,(w-bo)+key_y,key_z)), bs))         
        elif bs['key'] == 'rect':
            kl = bs['key_l']
            kw = bs['key_w']
            kh = bs['key_h']
            if klat == 'front' or klat == 'both':
                FreeCAD.Console.PrintMessage('Making front keys...\n')
                body = body.cut(cq.Workplane("XY", origin=((-0.5*kl)+k,(w-bo)-key_y,key_z)).rect(kl, kw).extrude(bs['key_h']))
                body = body.extrude(cq.Workplane("XY", origin=((0.5*kl)+l-k,(w-bo)-key_y,key_z)).rect(kl, kw).extrude(bs['key_h']))
            if klat == 'back' or klat == 'both':
                FreeCAD.Console.PrintMessage('Making back keys...\n')
                body = body.cut(cq.Workplane("XY", origin=((-0.5*kl)+k,(w-bo)+key_y,key_z)).rect(kl, kw).extrude(bs['key_h']))            
                body = body.extrude(cq.Workplane("XY", origin=((0.5*kl)+l-k,(w-bo)+key_y,key_z)).rect(kl, kw).extrude(bs['key_h']))        
        
    
    # position body
    body = body.translate((-0.5*p,-1*(w-bo),0))
    
    #make pins
    
    FreeCAD.Console.PrintMessage('Making pin 1...\n')
    pins = make_pin(model, 0, bs)
    for i in range(1,n):
        FreeCAD.Console.PrintMessage('Making pin ' + str(i+1) + '...\n')
        pins = pins.union(make_pin(model, i, bs))
    
    return (body, pins)


#import step_license as L
import add_license as Lic

# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":
    #destination_dir = '/TerminalBlock_Phoenix.3dshapes'
    expVRML.say(expVRML.__file__)
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
    #expVRML.say(models_dir)
    #stop

    try:
        with open('cq_parameters.yaml', 'r') as f:
            all_params = yaml.load(f)
    except yaml.YAMLError as exc:
        FreeCAD.Console.PrintMessage(exc)

    from sys import argv
    models = []

    if len(sys.argv) < 3:
        model_to_build = list(all_params)[0]
        FreeCAD.Console.PrintMessage('No variant name is given! building: ' + model_to_build)
    else:
        model_to_build = sys.argv[2]

    if model_to_build == "all":
        models = list(all_params)
        save_memory=True
    elif model_to_build == "sample": # chocolate box of all the 2-pin variants
        for model in all_params:
            if (not model == 'bodystyles') and all_params[model]['n'] == 2:
                models.append(model)
    else:
        models = [model_to_build]
        save_memory=False

    for model in models:
        if not model in all_params.keys():
            FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'all_params', skipping.\n" % model)
            continue
        
        if model == 'bodystyles':
            continue

        ModelName = model
        CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '').replace(',','')
        FreeCAD.Console.PrintMessage("checked model name = " + CheckedModelName + "\n")
        Newdoc = App.newDocument(CheckedModelName)
        App.setActiveDocument(CheckedModelName)
        Gui.ActiveDocument=Gui.getDocument(CheckedModelName)
        
        #case, pins = make_chip(model, all_params)
        (body, pins) = make_part(model, all_params)
        
        #show(case)
        #show(pins)
        show(body)
        show(pins)
   
        doc = FreeCAD.ActiveDocument
        objs=GetListOfObjects(FreeCAD, doc)
        
        # generate body color from parameters
        # try to be safe; & default is GREEN
        if 'color' in all_params[model]:
            body_color_key = str(all_params[model]['color']) + " body"
        else:
            body_color_key = "green body"
        if not body_color_key in shaderColors.named_colors:
            body_color_key = "green body"
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()

        Color_Objects(Gui,objs[0],body_color)
        Color_Objects(Gui,objs[1],pins_color)

        col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_pin=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        material_substitutions={
            col_body[:-1]:body_color_key,
            col_pin[:-1]:pins_color_key
        }

        expVRML.say(material_substitutions)

        del objs
        objs=GetListOfObjects(FreeCAD, doc)
        FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
        doc.Label = CheckedModelName
        objs=GetListOfObjects(FreeCAD, doc)
        objs[0].Label = CheckedModelName
        restore_Main_Tools()
        #rotate if required
        if 'rotation' in all_params[model]:
            rotation = all_params[model]['rotation']
        else:
            rotation = 0
        if (rotation!=0):
            z_RotateObject(doc, rotation)

        script_dir=os.path.dirname(os.path.realpath(__file__))
        ## models_dir=script_dir+"/../_3Dmodels"
        expVRML.say(models_dir)
        lib = 'TerminalBlock'
        if 'lib' in all_params[model]:
            lib = all_params[model]['lib']
        out_dir=models_dir+'/'+lib+".3dshapes"
        #out_dir=script_dir+os.sep+destination_dir
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        #out_dir="./generated_qfp/"
        # export STEP model
        exportSTEP(doc, ModelName, out_dir)
        if LIST_license[0]=="":
            LIST_license=Lic.LIST_int_license
            LIST_license.append("")
        Lic.addLicenseToStep(out_dir+'/', ModelName+".step", LIST_license,\
                           STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)
        # scale and export Vrml model
        scale=1/2.54
        #exportVRML(doc,ModelName,scale,out_dir)
        objs=GetListOfObjects(FreeCAD, doc)
        expVRML.say("######################################################################")
        expVRML.say(objs)
        expVRML.say("######################################################################")
        export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
        export_file_name=out_dir+os.sep+ModelName+'.wrl'
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

        # Save the doc in Native FC format
        if save_memory == False:
            Gui.SendMsgToActiveView("ViewFit")
            Gui.activeDocument().activeView().viewAxometric()

        # Save the doc in Native FC format
        saveFCdoc(App, Gui, doc, ModelName,out_dir, False)


        check_Model=True
        if save_memory == True or check_Model==True:
            doc=FreeCAD.ActiveDocument
            FreeCAD.closeDocument(doc.Name)

        step_path=os.path.join(out_dir,ModelName+u'.step')
        if check_Model==True:
            #ImportGui.insert(step_path,ModelName)
            ImportGui.open(step_path)
            docu = FreeCAD.ActiveDocument
            if cq_cad_tools.checkUnion(docu) == True:
                FreeCAD.Console.PrintMessage('step file is correctly Unioned\n')
            else:
                FreeCAD.Console.PrintError('step file is NOT Unioned\n')
                stop
            FC_majorV=int(FreeCAD.Version()[0])
            FC_minorV=int(FreeCAD.Version()[1])
            if FC_majorV == 0 and FC_minorV >= 17:
                for o in docu.Objects:
                    if hasattr(o,'Shape'):
                        chks=cq_cad_tools.checkBOP(o.Shape)
                        FreeCAD.Console.PrintMessage('chks ' + str(chks)+"\n")
                        FreeCAD.Console.PrintMessage(cq_cad_tools.mk_string(o.Label)+"\n")
                        if chks != True:
                            msg='shape \''+o.Name+'\' \''+cq_cad_tools.mk_string(o.Label)+'\' is INVALID!\n'
                            FreeCAD.Console.PrintError(msg)
                            FreeCAD.Console.PrintWarning(chks[0])
                            stop
                        else:
                            msg='shape \''+o.Name+'\' \''+cq_cad_tools.mk_string(o.Label)+'\' is valid\n'
                            FreeCAD.Console.PrintMessage(msg+"\n")
            else:
                FreeCAD.Console.PrintError('BOP check requires FC 0.17+\n')
            # Save the doc in Native FC format
            saveFCdoc(App, Gui, docu, ModelName,out_dir, False)
            doc=FreeCAD.ActiveDocument
            FreeCAD.closeDocument(doc.Name)

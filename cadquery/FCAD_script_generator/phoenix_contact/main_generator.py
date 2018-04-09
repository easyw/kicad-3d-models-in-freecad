# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This was originaly derived from a cadquery script for generating PDIP models in X3D format
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Adapted by easyw for step and vrlm export
# See https://github.com/easyw/kicad-3d-models-in-freecad

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad scriptName modelName
## e.g. FreeCAD main_generator.py all

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are FreeCAD & cadquery tools                                       *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating JST-XH models in STEP AP214               *
#*   Copyright (c) 2016                                                     *
#* Rene Poeschl https://github.com/poeschlr                                 *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU General Public License (GPL)             *
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

__title__ = "make 3D models of phoenix contact connectors (MSTB and MC series)."
__author__ = "scripts: maurice and hyOzd; models: poeschlr"
__Comment__ = '''make 3D models of phoenix contact types MSTB and MC.'''

___ver___ = "1.2 03/12/2017"

import sys, os
import traceback

import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors
import re, fnmatch
import yaml

save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'
global_3dpath = '../_3Dmodels/'

# Licence information of the generated models.
#################################################################################################
STR_licAuthor = "Rene Poeschl"
STR_licEmail = "poeschlr@gmail.com"
STR_licOrgSys = ""
STR_licPreProc = ""

LIST_license = ["",]
#################################################################################################

body_color_key = "green body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseInt()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseInt()
insert_color_key = "gold pins"
insert_color = shaderColors.named_colors[insert_color_key].getDiffuseInt()
screw_color_key = "metal grey pins"
screw_color = shaderColors.named_colors[screw_color_key].getDiffuseInt()

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

#checking requirements
#######################################################################
try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
    # CadQuery Gui
except Exception as e: # catch *all* exceptions
    print(e)
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)

#######################################################################
from Gui.Command import *

# Import cad_tools
#sys.path.append("../")
from cqToolsExceptions import *
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import GetListOfObjects, restore_Main_Tools,\
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, multiFuseObjs_wColors,\
 runGeometryCheck

try:
    close_CQ_Example(App, Gui)
except:
    FreeCAD.Console.PrintMessage("can't close example.")

from math import sqrt
from collections import namedtuple
#import FreeCAD, Draft, FreeCADGui
import ImportGui

sys.path.append("cq_models")
import conn_phoenix_mstb as MSTB
import conn_phoenix_mc as MC

import add_license as L

if LIST_license[0]=="":
    LIST_license=L.LIST_int_license
    LIST_license.append("")

def export_one_part(modul, variant, configuration, log, with_plug=False):
    if not variant in modul.all_params:
        FreeCAD.Console.PrintMessage("Parameters for %s doesn't exist in 'M.all_params', skipping." % variant)
        return
    LIST_license[0] = "Copyright (C) "+datetime.now().strftime("%Y")+", " + STR_licAuthor

    params = modul.all_params[variant]
    series_params = modul.seriesParams
    series = series_params.series_name

    subseries, connector_style = params.series_name.split('-')
    pitch_mpn = '-{:g}'.format(params.pin_pitch)
    if series[0] == 'MSTB':
        pitch_mpn = ''
        if params.pin_pitch == 5.08:
            pitch_mpn = '-5,08'
        elif params.pin_pitch == 7.62:
            pitch_mpn = '-7,62'
    lib_name = configuration['lib_name_format_str'].format(series=series[0], style=series[1], pitch=params.pin_pitch)
    mpn = configuration['mpn_format_string'].format(subseries=subseries, style = connector_style,
        rating=series[1], num_pins=params.num_pins, pitch=pitch_mpn)
    FileName = configuration['fp_name_format_string'].format(man = configuration['manufacturer'],
        series = series[0], mpn = mpn, num_rows = 1,
        num_pins = params.num_pins, pitch = params.pin_pitch,
        orientation = configuration['orientation_str'][1] if params.angled else configuration['orientation_str'][0],
        flanged = configuration['flanged_str'][1] if params.flanged else configuration['flanged_str'][0],
        mount_hole = configuration['mount_hole_str'][1] if params.mount_hole else configuration['mount_hole_str'][0])

    destination_dir=global_3dpath+lib_name
    if with_plug:
        destination_dir += "__with_plug"
    destination_dir+=".3dshapes"

    ModelName = variant
    ModelName = ModelName.replace(".","_")
    Newdoc = FreeCAD.newDocument(ModelName)
    App.setActiveDocument(ModelName)
    App.ActiveDocument=App.getDocument(ModelName)
    Gui.ActiveDocument=Gui.getDocument(ModelName)
    #App.setActiveDocument(ModelName)
    #Gui.ActiveDocument=Gui.getDocument(ModelName)
    (pins, body, insert, mount_screw, plug, plug_screws) = modul.generate_part(variant, with_plug)

    color_attr = body_color + (0,)
    show(body, color_attr)

    color_attr = pins_color + (0,)
    show(pins, color_attr)

    if insert is not None:
        color_attr = insert_color + (0,)
        show(insert, color_attr)
    if mount_screw is not None:
        color_attr = screw_color + (0,)
        show(mount_screw, color_attr)
    if plug is not None:
        color_attr = body_color + (0,)
        show(plug, color_attr)

        color_attr = screw_color + (0,)
        show(plug_screws, color_attr)

    doc = FreeCAD.ActiveDocument
    doc.Label=ModelName
    objs=FreeCAD.ActiveDocument.Objects
    FreeCAD.Console.PrintMessage(objs)

    i=0
    objs[i].Label = ModelName + "__body"
    i+=1
    objs[i].Label = ModelName + "__pins"
    i+=1
    if insert is not None:
        objs[i].Label = ModelName + "__thread_insert"
        i+=1
    if mount_screw is not None:
        objs[i].Label = ModelName + "__mount_screw"
        i+=1
    if plug is not None:
        objs[i].Label = ModelName + "__plug"
        i+=1
        objs[i].Label = ModelName + "__plug_screws"
    restore_Main_Tools()

    out_dir=destination_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    used_color_keys = [body_color_key, pins_color_key]
    export_file_name=destination_dir+os.sep+FileName+'.wrl'

    export_objects = []
    i=0
    export_objects.append(expVRML.exportObject(freecad_object = objs[i],
            shape_color=body_color_key,
            face_colors=None))
    i+=1
    export_objects.append(expVRML.exportObject(freecad_object = objs[i],
            shape_color=pins_color_key,
            face_colors=None))
    i+=1
    if insert is not None:
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=insert_color_key,
                face_colors=None))
        used_color_keys.append(insert_color_key)
        i+=1
    if mount_screw is not None:
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=screw_color_key,
                face_colors=None))
        used_color_keys.append(screw_color_key)
        i+=1
    if plug is not None:
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=body_color_key,
                face_colors=None))
        i+=1
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=screw_color_key,
                face_colors=None))
    scale=1/2.54
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    fusion = multiFuseObjs_wColors(FreeCAD, FreeCADGui,
                     ModelName, objs, keepOriginals=True)

    exportSTEP(doc,FileName,out_dir,fusion)

    step_path = '{dir:s}/{name:s}.step'.format(dir=out_dir, name=FileName)

    L.addLicenseToStep(out_dir, '{:s}.step'.format(FileName), LIST_license,\
        STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licPreProc)

    FreeCAD.activeDocument().recompute()
    # FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewAxometric()


    # Save the doc in Native FC format
    saveFCdoc(App, Gui, doc, FileName, out_dir)
    if save_memory == True or check_Model==True:
        doc=FreeCAD.ActiveDocument
        FreeCAD.closeDocument(doc.Name)

    if check_Model==True:
        runGeometryCheck(App, Gui, step_path,
            log, ModelName, save_memory=save_memory)

class argparse():
    def __init__(self):
        self.config = 'config_phoenix_KLCv3.0.yaml'
        self.model_filter = '*'
        self.series = ['mc','mstb']
        self.with_plug = False

    def parse_args(self, args):
        for arg in args:
            if '=' in arg:
                self.parseValueArg(*arg.split('='))
            else:
                self.argSwitchArg(arg)

    def parseValueArg(self, name, value):
        if name == 'config':
            self.config = value
        elif name == 'model_filter':
            self.model_filter = value
        elif name == 'series':
            self.series = value.split(',')

    def argSwitchArg(self, name):
        if name == '?':
            self.print_usage()
            exit()
        elif name == 'with_plug':
            self.with_plug = True
        elif name == 'disable_check':
            global check_Model
            check_Model = False
        elif name == 'disable_Memory_reduction':
            global save_memory
            save_memory = False
        elif name == 'error_tolerant':
            global stop_on_first_error
            stop_on_first_error = False

    def print_usage(self):
        print("Generater script for phoenix contact 3d models.")
        print('usage: FreeCAD main_generator.py [optional arguments]')
        print('optional arguments:')
        print('\tconfig=[config file]: default:config_phoenix_KLCv3.0.yaml')
        print('\tmodel_filter=[filter using linux file filter syntax]')
        print('\tseries=[series name],[series name],...')
        print('switches:')
        print('\twith_plug')
        print('\tdisable_check')
        print('\tdisable_Memory_reduction')
        print('\terror_tolerant\n')

    def __str__(self):
        return 'config:{:s}, filter:{:s}, series:{:s}, with_plug:{:d}'.format(
            self.config, self.model_filter, str(self.series), self.with_plug)

def exportSeries(series_params, log):
    for variant in series_params.all_params.keys():
        if model_filter_regobj.match(variant):
            #FreeCAD.Console.PrintMessage('\r\n'+variant+'\r\n')
            try:
                export_one_part(series_params, variant, configuration, log, with_plug)
            except GeometryError as e:
                e.print_errors(stop_on_first_error)
                if stop_on_first_error:
                    return -1
            except FreeCADVersionError as e:
                FreeCAD.Console.PrintError(e)
                return -1
    return 0

if __name__ == "__main__" or __name__ == "main_generator":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    series_to_build = []
    modelfilter = ""
    with_plug = False

    args = argparse()
    args.parse_args(sys.argv)

    with open(args.config, 'r') as config_stream:
        try:
            configuration = yaml.load(config_stream)
        except yaml.YAMLError as exc:
            print(exc)

    series_to_build = map(str.lower, args.series)
    print(args)
    modelfilter = args.model_filter

    series = []
    if 'mc' in series_to_build:
        series += [MC]
    if 'mstb' in series_to_build:
        series += [MSTB]

    model_filter_regobj=re.compile(fnmatch.translate(modelfilter))
    print("########################################")

    print(args.model_filter)
    with open(check_log_file, 'w') as log:
        log.write('# Check report for Phoenix Contact 3d model genration\n')
        for typ in series:
            try:
                if exportSeries(typ, log) != 0:
                    break
            except Exception as exeption:
                traceback.print_exc()
                break

    FreeCAD.Console.PrintMessage('\r\nDone\r\n')

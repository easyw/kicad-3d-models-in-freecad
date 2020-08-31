# -*- coding: utf8 -*-
#!/usr/bin/python
#
# Based on molex/main_generator.py
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
#* cadquery script for generating Molex models in STEP AP214                *
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

__title__ = "main generator for FFC-FPC connector models"
__author__ = "scripts: maurice and hyOzd; models: see cq_model files"
__Comment__ = '''This generator loads cadquery model scripts and generates step/wrl files for the official kicad library.'''

___ver___ = "1.3 29/12/2019"


save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'
global_3dpath = '../_3Dmodels/'

import sys, os
import traceback

import datetime
from datetime import datetime
from math import sqrt
from collections import namedtuple

sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors
import add_license as L

import re, fnmatch
import yaml

save_memory = True #reducing memory consuming for all generation params
check_Model = True
check_log_file = 'check-log.md'

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

#import FreeCADGui as Gui

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

#from Gui.Command import *

# Import cad_tools
#sys.path.append("../_tools")
from cqToolsExceptions import *
import cq_cad_tools
# Reload tools
try:
    reload(cq_cad_tools)
except:
    import importlib
    importlib.reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import multiFuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject,\
 runGeometryCheck

# Gui.SendMsgToActiveView("Run")
#Gui.activateWorkbench("CadQueryWorkbench")
#import FreeCADGui as Gui

#try:
#    close_CQ_Example(App, Gui)
#except:
#    FreeCAD.Console.PrintMessage("can't close example.")

#import FreeCAD, Draft, FreeCADGui
import ImportGui


def export_one_part(module, pincount, configuration, log):
    series_definition = module.series_params

    if module.LICENCE_Info.LIST_license[0]=="":
        LIST_license=L.LIST_int_license
        LIST_license.append("")
    else:
        LIST_license=module.LICENCE_Info.LIST_license

    LIST_license[0] = "Copyright (C) "+datetime.now().strftime("%Y")+", " + module.LICENCE_Info.STR_licAuthor
    pins_per_row = pincount//series_definition.number_of_rows
    # for TE series only double digit pincount parts have leading chars on the PN
    if pincount >= 10:
        pn_prefix = str(pincount)[0] + "-"
    else:
        pn_prefix = ""
    mpn = series_definition.mpn_format_string.format(pincount=pincount, pnp=pn_prefix, pns=str(pincount)[-1], pins_per_row=pins_per_row)


    orientation = configuration['orientation_options'][series_definition.orientation]
    format_string = getattr(series_definition, 'fp_name_format_string',
        configuration[getattr(series_definition, 'fp_name_format', 'fp_name_format_string')])
    FileName = format_string.format(man=series_definition.manufacturer,
            series=series_definition.series,
            mpn=mpn, num_rows=series_definition.number_of_rows, pins_per_row=pins_per_row,
            pins=pincount, pitch=series_definition.pitch, orientation=orientation,
            mount_pin=series_definition.mount_pin)
    FileName = FileName.replace('__', '_')

    lib_name = configuration['lib_name_format_string'].format(man=series_definition.manufacturer)
    fc_mpn = mpn.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')

    ModelName = '{:s}_{:s}'.format(series_definition.manufacturer, fc_mpn) # For some reason the Model name can not start with a number.

    FreeCAD.Console.PrintMessage('\r\n'+FileName+'\r\n')
    #FileName = modul.all_params[variant].file_name
    Newdoc = FreeCAD.newDocument(ModelName)
    print(Newdoc.Label)
    App.setActiveDocument(ModelName)
    App.ActiveDocument=App.getDocument(ModelName)
    Gui.ActiveDocument=Gui.getDocument(ModelName)

    color_keys = series_definition.color_keys
    obj_suffixes = series_definition.obj_suffixes
    colors = [shaderColors.named_colors[key].getDiffuseInt() for key in color_keys]

    cq_obj_data = module.generate_part(pincount)


    for i in range(len(cq_obj_data)):
        color_i = colors[i] + (0,)
        show(cq_obj_data[i], color_i)


    doc = FreeCAD.ActiveDocument
    doc.Label = ModelName
    objs=GetListOfObjects(FreeCAD, doc)


    for i in range(len(objs)):
        objs[i].Label = ModelName + obj_suffixes[i]


    restore_Main_Tools()

    out_dir='{:s}Connector_FFC-FPC.3dshapes'.format(global_3dpath)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    used_color_keys = color_keys
    export_file_name=out_dir+os.sep+FileName+'.wrl'

    export_objects = []
    for i in range(len(objs)):
        export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                shape_color=color_keys[i],
                face_colors=None))

    scale=1/2.54
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    fusion = multiFuseObjs_wColors(FreeCAD, FreeCADGui,
                     ModelName, objs, keepOriginals=True)
    exportSTEP(doc,FileName,out_dir,fusion)

    step_path = '{dir:s}/{name:s}.step'.format(dir=out_dir, name=FileName)

    L.addLicenseToStep(out_dir, '{:s}.step'.\
        format(FileName), LIST_license,
            module.LICENCE_Info.STR_licAuthor,
            module.LICENCE_Info.STR_licEmail,
            module.LICENCE_Info.STR_licOrgSys,
            module.LICENCE_Info.STR_licPreProc)

    FreeCAD.activeDocument().recompute()

    saveFCdoc(App, Gui, doc, FileName, out_dir)

    #FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.activeDocument().activeView().viewAxometric()

    if save_memory == True or check_Model==True:
        doc=FreeCAD.ActiveDocument
        FreeCAD.closeDocument(doc.Name)

    if check_Model==True:
        runGeometryCheck(App, Gui, step_path,
            log, ModelName, save_memory=save_memory)

def exportSeries(module, configuration, log, model_filter_regobj):
    for pins in module.series_params.pinrange:
        try:
            if model_filter_regobj.match(str(pins)):
                export_one_part(module, pins, configuration, log)
        except GeometryError as e:
            e.print_errors(stop_on_first_error)
            if stop_on_first_error:
                return -1
        except FreeCADVersionError as e:
            FreeCAD.Console.PrintError(e)
            return -1
    return 0

#########################  ADD MODEL GENERATORS #########################

sys.path.append("cq_models")
import conn_te_84952
import conn_te_84953

all_series = {
    '84952':conn_te_84952,
    '84953':conn_te_84953
}

#########################################################################

class argparse():
    def __init__(self):
        self.config = '../_tools/config/connector_config_KLCv3.yaml'
        self.model_filter = '*'
        self.series = all_series.values()

    def parse_args(self, args):
        for arg in args:
            if '=' in arg:
                self.parseValueArg(*arg.split('='))
            else:
                self.argSwitchArg(arg)

    def parseValueArg(self, name, value):
        if name == 'config':
            self.config = value
        elif name == 'pins_filter':
            self.model_filter = value
        elif name == 'log':
            global check_log_file
            check_log_file = value
        elif name == 'series':
            series_str = value.split(',')
            self.series = []
            for s in series_str:
                if s.lower() in all_series:
                    self.series.append(all_series[s.lower()])

    def argSwitchArg(self, name):
        if name == '?':
            self.print_usage()
            exit()
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
        print("Generater script for molex connector 3d models.")
        print('usage: FreeCAD main_generator.py [optional arguments and switches]')
        print('optional arguments:')
        print('\tconfig=[config file]: default:connector_config_KLCv3.0.yaml')
        print('\tpins_filter=[filter pincount using linux file filter syntax]')
        print('\tlog=[log file path]')
        print('\tseries=[series name],[series name],...')
        print('switches:')
        print('\tdisable_check')
        print('\tdisable_Memory_reduction')
        print('\terror_tolerant\n')

    def __str__(self):
        return 'config:{:s}, filter:{:s}, series:{:s}, with_plug:{:d}'.format(
            self.config, self.model_filter, str(self.series), self.with_plug)

if __name__ == "__main__" or __name__ == "main_generator":
    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    args = argparse()
    args.parse_args(sys.argv)
    modelfilter = args.model_filter

    with open(args.config, 'r') as config_stream:
        try:
            configuration = yaml.load(config_stream)
        except yaml.YAMLError as exc:
            print(exc)

    model_filter_regobj=re.compile(fnmatch.translate(modelfilter))


    with open(check_log_file, 'w') as log:
        log.write('# Check report for Molex 3d model genration\n')
        for typ in args.series:
            try:
                if exportSeries(typ, configuration, log, model_filter_regobj) != 0:
                    break
            except Exception as exeption:
                traceback.print_exc()
                break


    FreeCAD.Console.PrintMessage('\r\Done\r\n')

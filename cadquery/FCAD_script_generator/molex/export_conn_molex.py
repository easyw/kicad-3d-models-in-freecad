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
## e.g. FreeCAD export_conn_jst_xh.py all

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

__title__ = "make 3D models of molex 53261-Connectors."
__author__ = "scripts: maurice and hyOzd; models: poeschlr"
__Comment__ = '''make 3D models of JST-XH-Connectors types molex 53261. (Top entry)'''

___ver___ = "1.2 03/12/2017"

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors
import re, fnmatch
import yaml

save_memory = True #reducing memory consuming for all generation params
check_Model = True
check_log_file = 'check-log.md'

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


# FreeCAD.Console.PrintMessage(M.all_params_soic)
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

# Import cad_tools
#sys.path.append("../_tools")
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject,\
 closeCurrentDoc, checkBOP, checkUnion

# Gui.SendMsgToActiveView("Run")
Gui.activateWorkbench("CadQueryWorkbench")
import FreeCADGui as Gui

try:
    close_CQ_Example(App, Gui)
except:
    FreeCAD.Console.PrintMessage("can't close example.")


import cadquery as cq
from math import sqrt
from Helpers import show
from collections import namedtuple
import FreeCAD, Draft, FreeCADGui
import ImportGui
sys.path.append("cq_models")
import add_license as L

def export_one_part(module, pincount, configuration, log):
    series_definition = module.series_params

    body_color_key = series_definition.body_color_key
    body_color = shaderColors.named_colors[body_color_key].getDiffuseInt()
    pins_color_key = series_definition.pins_color_key
    pins_color = shaderColors.named_colors[pins_color_key].getDiffuseInt()

    if module.LICENCE_Info.LIST_license[0]=="":
        LIST_license=L.LIST_int_license
        LIST_license.append("")
    else:
        LIST_license=module.LICENCE_Info.LIST_license

    LIST_license[0] = "Copyright (C) "+datetime.now().strftime("%Y")+", " + module.LICENCE_Info.STR_licAuthor

    mpn = series_definition.mpn_format_string.format(pincount=pincount)


    orientation = configuration['orientation_options'][series_definition.orientation]
    FileName = configuration['fp_name_format_string'].\
        format(man=series_definition.manufacturer,
            series=series_definition.series,
            mpn=mpn, num_rows=1, pins_per_row=pincount,
            pitch=series_definition.pitch, orientation=orientation)
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
    (pins, body) = module.generate_part(pincount)

    color_attr = body_color + (0,)
    show(body, color_attr)

    color_attr = pins_color + (0,)
    show(pins, color_attr)

    doc = FreeCAD.ActiveDocument
    doc.Label=ModelName
    objs=GetListOfObjects(FreeCAD, doc)
    objs[0].Label = ModelName + "__body"
    objs[1].Label = ModelName + "__pins"

    restore_Main_Tools()

    out_dir='{:s}.3dshapes'.format(lib_name)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    used_color_keys = [body_color_key, pins_color_key]
    export_file_name=out_dir+os.sep+FileName+'.wrl'

    export_objects = []
    export_objects.append(expVRML.exportObject(freecad_object = objs[0],
            shape_color=body_color_key,
            face_colors=None))
    export_objects.append(expVRML.exportObject(freecad_object = objs[1],
            shape_color=pins_color_key,
            face_colors=None))

    scale=1/2.54
    colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
    expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

    fusion = FuseObjs_wColors(FreeCAD, FreeCADGui,
                    ModelName, objs[0].Name, objs[1].Name, keepOriginals=True)
    exportSTEP(doc,FileName,out_dir,fusion)

    step_path = '{dir:s}/{name:s}.step'.format(dir=out_dir, name=FileName)

    L.addLicenseToStep(out_dir, '{:s}.step'.\
        format(FileName), LIST_license,
            module.LICENCE_Info.STR_licAuthor,
            module.LICENCE_Info.STR_licEmail,
            module.LICENCE_Info.STR_licOrgSys,
            module.LICENCE_Info.STR_licPreProc)

    saveFCdoc(App, Gui, doc, FileName,out_dir)

    FreeCAD.activeDocument().recompute()
    #FreeCADGui.activateWorkbench("PartWorkbench")
    if save_memory == False and check_Model==False:
        FreeCADGui.SendMsgToActiveView("ViewFit")
        FreeCADGui.activeDocument().activeView().viewAxometric()

    if save_memory == True or check_Model==True:
        closeCurrentDoc(ModelName)

    if check_Model==True:
        #ImportGui.insert(step_path,ModelName)

        ImportGui.open(step_path)
        docu = FreeCAD.ActiveDocument
        docu.Label=ModelName
        log.write('\n## Checking {:s}\n'.format(ModelName))

        if checkUnion(docu) == True:
            FreeCAD.Console.PrintMessage('step file is correctly Unioned\n')
            log.write('\t- Union check:    [    pass    ]\n')
        else:
            FreeCAD.Console.PrintError('step file is NOT Unioned\n')
            log.write('\t- Union check:    [    FAIL    ]\n')
            #stop
        FC_majorV=int(FreeCAD.Version()[0])
        FC_minorV=int(FreeCAD.Version()[1])
        if FC_majorV == 0 and FC_minorV >= 17:
            for o in docu.Objects:
                if hasattr(o,'Shape'):
                    chks=checkBOP(o.Shape)
                    #print 'chks ',chks
                    if chks != True:
                        #msg='shape \''+o.Name+'\' \''+ mk_string(o.Label)+'\' is INVALID!\n'
                        msg = 'shape "{name:s}" "{label:s}" is INVALID'.format(name=o.Name, label=o.Label)
                        FreeCAD.Console.PrintError(msg)
                        FreeCAD.Console.PrintWarning(chks[0])
                        log.write('\t- Geometry check: [    FAIL    ]\n')
                        log.write('\t\t- Effected shape: "{name:s}" "{label:s}"\n'.format(name=o.Name, label=o.Label))
                        #stop
                    else:
                        #msg='shape \''+o.Name+'\' \''+ mk_string(o.Label)+'\' is valid\n'
                        msg = 'shape "{name:s}" "{label:s}" is valid'.format(name=o.Name, label=o.Label)
                        FreeCAD.Console.PrintMessage(msg)
                        log.write('\t- Geometry check: [    pass    ]\n')
        else:
            FreeCAD.Console.PrintError('BOP check requires FC 0.17+\n')
            log.write('\t- Geometry check: [  skipped   ]\n')
            log.write('\t\t- Geometry check needs FC 0.17+\n')

        if save_memory == True:
            saveFCdoc(App, Gui, docu, 'temp', out_dir)
            docu = FreeCAD.ActiveDocument
            closeCurrentDoc(docu.Label)
    return out_dir

def exportSeries(module, configuration, log, model_filter_regobj):
    for pins in module.series_params.pinrange:
        if model_filter_regobj.match(str(pins)):
            out_dir = export_one_part(module, pins, configuration, log)
    if save_memory == True:
        os.remove('{}/temp.FCStd'.format(out_dir))

import conn_molex_53261
import conn_molex_53398

class argparse():
    def __init__(self):
        self.config = 'conn_config_KLCv3.yaml'
        self.model_filter = '*'
        self.series = [conn_molex_53261, conn_molex_53398]

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
        elif name == 'log':
            global check_log_file
            check_log_file = value
        elif name == 'series':
            series_str = value.split(',')
            self.series = []
            for s in series_str:
                if '53261' in s:
                    series_str.append(conn_molex_53261)
                elif '53398' in s:
                    series_str.append(conn_molex_53398)

    def argSwitchArg(self, name):
        if name == '?':
            self.print_usage()
        elif name == 'disable_check':
            global check_Model
            check_Model = False
        elif name == 'disable_Memory_reduction':
            global save_memory
            save_memory = False

    def print_usage(self):
        print("Generater script for phoenix contact 3d models.")
        print('usage: FreeCAD export_conn_phoenix.py [optional arguments and switches]')
        print('optional arguments:')
        print('\tconfig=[config file]: default:config_phoenix_KLCv3.0.yaml')
        print('\tmodel_filter=[filter pincount using linux file filter syntax]')
        print('\tlog=[log file path]')
        print('\tseries=[series name],[series name],...')
        print('switches:')
        print('\tdisable_check')
        print('\tdisable_Memory_reduction')

    def __str__(self):
        return 'config:{:s}, filter:{:s}, series:{:s}, with_plug:{:d}'.format(
            self.config, self.model_filter, str(self.series), self.with_plug)

if __name__ == "__main__":
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
            exportSeries(typ, configuration, log, model_filter_regobj)


    FreeCAD.Console.PrintMessage('\r\Done\r\n')

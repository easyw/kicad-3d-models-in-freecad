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

from __future__ import division

__title__ = "generator for wuert smt mounting hardware with inner through holes"
__author__ = "scripts: maurice and hyOzd; models: poeschlr"
__Comment__ = '''This generates step/wrl files for the official kicad library.'''

___ver___ = "1.0 26/05/2019"

class LICENCE_Info():
    ############################################################################
    STR_licAuthor = "Rene Poeschl"
    STR_licEmail = "poeschlr@gmail.com"
    STR_licOrgSys = ""
    STR_licPreProc = ""

    LIST_license = ["",]
    ############################################################################


save_memory = True #reducing memory consuming for all generation params
check_Model = True
stop_on_first_error = True
check_log_file = 'check-log.md'
global_3dpath = '../_3Dmodels/'


import sys, os
import traceback
from datetime import datetime
from math import sqrt

thread_minor_diameter = {
    'M1.6': 1.22,
    'M2': 1.57,
    'M2.5': 2.01,
    'M3': 2.46,
    'M4': 3.24
    }

def generate(**kwargs):
    id = kwargs.get('id')
    od = kwargs['od']
    od1 = kwargs.get('od1')
    h1 = kwargs.get('h1', 0)
    h = kwargs['h']
    td = kwargs.get('td')
    dd = kwargs.get('dd')
    id1 = kwargs.get('id1')
    t1 = kwargs.get('t1', 0)
    ext_thread = kwargs.get('ext_thread')

    body = cq.Workplane("XY").circle(od/2).extrude(h)
    if od1 is not None:
        body = body.faces("<Z").workplane().circle(od1/2).extrude(h1)

    if ext_thread is not None:
        od = float(ext_thread['od'][1:])
        thread = cq.Workplane("XY").workplane(h+ext_thread['undercut']['L'][0])\
            .circle(od/2).extrude(ext_thread['L']-ext_thread['undercut']['L'][0])

        thread = thread.faces("<Z").chamfer(
                   ext_thread['undercut']['L'][1] - ext_thread['undercut']['L'][0],
                   (od - ext_thread['undercut']['od'])/2)
        thread = thread.faces(">Z").chamfer(
                    (od - thread_minor_diameter[ext_thread['od']])/2)
        thread = thread.faces("<Z").workplane()\
                    .circle(ext_thread['undercut']['od']/2)\
                    .extrude(ext_thread['undercut']['L'][0]+0.1)

        body = body.union(thread)
        body = body.edges(cq.selectors.BoxSelector(
            [-ext_thread['undercut']['od']/2-0.1,
             -ext_thread['undercut']['od']/2-0.1,
             h-0.1
             ],
             [ext_thread['undercut']['od']/2+0.1,
             ext_thread['undercut']['od']/2+0.1,
             h+0.1
             ], boundingbox=True)).fillet(ext_thread['undercut']['r'])

    if id is not None:
        if id in thread_minor_diameter:
            idf = thread_minor_diameter[id]
            ch = (float(id[1:])-idf)/2
        else:
            idf = float(id)
            ch = 0

        if td is not None:
            body = body.faces(">Z").workplane(-t1).circle(idf/2).cutBlind(-td+t1)
            body = body.faces(">Z").workplane(-t1).circle(idf/2-0.01).cutBlind(-dd+t1)

            if ch > 0:
                body = body.edges(cq.selectors.BoxSelector(
                            [-idf/2-0.1,
                             -idf/2-0.1,
                             h-0.1
                             ],
                             [idf/2+0.1,
                             idf/2+0.1,
                             h+0.1
                             ], boundingbox=True))\
                         .chamfer(ch)
        else:
            body = body.faces(">Z").workplane(-t1).circle(idf/2).cutBlind(-(h+h1-t1))
        if id1 is not None:
            body = body.faces(">Z").workplane().circle(id1/2).cutBlind(-(t1))
    return body

# opend from within freecad
if "module" in __name__:
    import cadquery as cq
    from Helpers import show

    ext_thread = {
      'od': 'M3',
      'L': 6,
      'undercut':{
        'od': 2.2,
        'L': [0.5, 1.25],
        'r': 0.2
        }
    }

    body = generate(
        id="M2.5",
        od=4.35,
        od1=2.8,
        h1=1.4,
        h=3,
        td=2,
        dd=2.5)
    # body = generate(
    #     od=6,
    #     od1=0.8,
    #     h1=0.5,
    #     h=3,
    #     ext_thread=ext_thread
    # )
    show(body)

if __name__ == "__main__" or __name__ == "wuerth_smt_spacer":
    sys.path.append("../_tools")
    import exportPartToVRML as expVRML
    import shaderColors
    import add_license as L

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
    import importlib
    importlib.reload(cq_cad_tools)
    # Explicitly load all needed functions
    from cq_cad_tools import multiFuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
     exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject,\
     runGeometryCheck

    # Gui.SendMsgToActiveView("Run")
    #Gui.activateWorkbench("CadQueryWorkbench")
    #import FreeCADGui as Gui

    try:
        close_CQ_Example(App, Gui)
    except:
        FreeCAD.Console.PrintMessage("can't close example.")

    #import FreeCAD, Draft, FreeCADGui
    import ImportGui

    #######################################################################

    def export_one_part(params, mpn, log):
        print('\n##########################################################')

        if LICENCE_Info.LIST_license[0]=="":
            LIST_license=L.LIST_int_license
            # LIST_license.append("")
        else:
            LIST_license=LICENCE_Info.LIST_license

        LIST_license[0] = "Copyright (C) "+datetime.now().strftime("%Y")+", " + LICENCE_Info.STR_licAuthor

        fp_params = params['footprint']
        mech_params = params['mechanical']
        part_params = params['parts'][mpn]

        if 'id' in mech_params:
            size = str(mech_params['id'])
        elif 'ext_thread' in mech_params:
            size = str(mech_params['ext_thread']['od'])

        if 'M' not in size:
            size = "{}mm".format(size)

        td = ""
        size_prefix = ""
        if 'thread_depth' in part_params:
            td = "_ThreadDepth{}mm".format(part_params['thread_depth'])
        elif 'ext_thread' in mech_params:
            size_prefix = 'External'

        h = part_params['h'] if 'h' in part_params else part_params['h1']

        suffix = ''
        if 'suffix' in params:
            suffix = '_{}'.format(params['suffix'])

        FileName = "Mounting_Wuerth_{series}-{size_prefix}{size}_H{h}mm{td}{suffix}_{mpn}".format(
                        size=size, h=h, mpn=mpn, td=td, size_prefix=size_prefix,
                        series=params['series_prefix'], suffix=suffix)

        lib_name = "Mounting_Wuerth"

        ModelName = FileName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')

        FreeCAD.Console.PrintMessage('\r\n'+FileName+'\r\n')
        #FileName = modul.all_params[variant].file_name
        Newdoc = FreeCAD.newDocument(ModelName)
        print(Newdoc.Label)
        App.setActiveDocument(ModelName)
        App.ActiveDocument=App.getDocument(ModelName)
        Gui.ActiveDocument=Gui.getDocument(ModelName)

        color_keys = ["metal grey pins"]
        colors = [shaderColors.named_colors[key].getDiffuseInt() for key in color_keys]

        cq_obj_data = generate(
                            id=mech_params.get('id'),
                            od=mech_params['od'],
                            od1=mech_params.get('od1'),
                            h1=mech_params.get('h1', part_params.get('h1', 0)),
                            h=part_params.get('h', mech_params.get('h')),
                            td=part_params.get('thread_depth'),
                            dd=part_params.get('drill_depth'),
                            id1=mech_params.get('id1'),
                            t1=mech_params.get('t1', 0),
                            ext_thread=mech_params.get('ext_thread')
                            )

        color_i = colors[0] + (0,)
        show(cq_obj_data, color_i)

        doc = FreeCAD.ActiveDocument
        doc.Label = ModelName
        objs=GetListOfObjects(FreeCAD, doc)

        objs[0].Label = ModelName

        restore_Main_Tools()

        out_dir='{:s}{:s}.3dshapes'.format(global_3dpath, lib_name)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        used_color_keys = color_keys
        export_file_name=out_dir+os.sep+FileName+'.wrl'

        export_objects = []
        print('objs')
        print(objs)
        for i in range(len(objs)):
            export_objects.append(expVRML.exportObject(freecad_object = objs[i],
                    shape_color=color_keys[i],
                    face_colors=None))

        scale=1/2.54
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)

        exportSTEP(doc,FileName,out_dir,objs[0])

        step_path = '{dir:s}/{name:s}.step'.format(dir=out_dir, name=FileName)

        L.addLicenseToStep(out_dir, '{:s}.step'.\
            format(FileName), LIST_license,
                LICENCE_Info.STR_licAuthor,
                LICENCE_Info.STR_licEmail,
                LICENCE_Info.STR_licOrgSys,
                LICENCE_Info.STR_licPreProc)

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

    with open('./wuerth_smt_spacer.yaml', 'r') as params_stream:
        try:
            params = yaml.safe_load(params_stream)
        except yaml.YAMLError as exc:
            print(exc)

    with open(check_log_file, 'w') as log:
        for series in params:
            for mpn in params[series]['parts']:
                try:
                    export_one_part(params[series], mpn, log)
                except Exception as exeption:
                    traceback.print_exc()
                    break

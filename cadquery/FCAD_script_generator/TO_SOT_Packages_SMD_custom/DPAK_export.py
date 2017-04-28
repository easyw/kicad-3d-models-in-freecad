# TODO add software licence

import sys
import os

full_path=os.path.realpath(__file__)
script_dir_name =full_path.split(os.sep)[-2]
parent_path = full_path.split(script_dir_name)[0]
out_dir = parent_path + "_3Dmodels" + "/" + script_dir_name

sys.path.append("../_tools")
sys.path.append("cq_models")

import add_license as L


##########################################################################################

# DEVICE-DEPENDENT CONFIGURATION

# Models
from DPAK_factory import *
CONFIG = 'DPAK_config.yaml'


# Licence information included in the generated models
L.STR_int_licAuthor = "Ray Benitez"
L.STR_int_licEmail = "hackscribble@outlook.com"

##########################################################################################


import argparse
import yaml
import pprint


# TODO device dependent
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--family', help='device type to build: TO-263  (default is all)',
                        type=str, nargs=1)
    parser.add_argument('-v', '--verbose', help='show extra information while generating the footprint',
                        action='store_true')
    return parser.parse_args()


import shaderColors

from datetime import datetime
import exportPartToVRML as expVRML
import re
import fnmatch

import cadquery as cq
from Helpers import show
from collections import namedtuple
import FreeCAD
import Draft
import ImportGui

from Gui.Command import *

import cq_cad_tools
reload(cq_cad_tools)
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, multiFuseObjs_wColors, \
 checkRequirements

Gui.activateWorkbench("CadQueryWorkbench")

import FreeCADGui as Gui

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

# checking requirements

try:
    # Gui.SendMsgToActiveView("Run")
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

checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"



if __name__ == "__main__":

    FreeCAD.Console.PrintMessage('\r\nExport started ...\r\n')

    # args = get_args()

    # if args.family:
        # if args.family[0] == 'TO263':
            # build_list = [TO263(CONFIG)]
        # else:
            # print('ERROR: family not recognised')
            # build_list = []
    # else:


    # TODO device dependent
    # build_list = [TO252(CONFIG), TO263(CONFIG), TO268(CONFIG)]
    build_list = [TO268(CONFIG)]

    n = 0
    for package in build_list:
        for model in package.build_family(verbose=True):
            file_name = model['__name']
            parts_list = model.keys()
            parts_list.remove('__name')
            # create document
            safe_name = file_name.replace('-', '_')
            FreeCAD.Console.PrintMessage('Model: {:s}\r\n'.format(file_name))
            n += 1
            Newdoc = FreeCAD.newDocument(safe_name)
            App.setActiveDocument(safe_name)
            App.ActiveDocument = App.getDocument(safe_name)
            Gui.ActiveDocument = Gui.getDocument(safe_name)
            # colour model
            used_colour_keys = []
            for part in parts_list:
                colour_key = model[part]['colour']
                used_colour_keys.append(colour_key)
                colour = shaderColors.named_colors[colour_key].getDiffuseInt()
                colour_attr = colour + (0,)
                show(model[part]['part'], colour_attr)
            doc = FreeCAD.ActiveDocument
            doc.Label=safe_name
            objs=FreeCAD.ActiveDocument.Objects
            i = 0
            for part in parts_list:
                objs[i].Label = '{n:s}__{p:s}'.format(n=safe_name, p=part)
                i += 1
            restore_Main_Tools()
            FreeCAD.activeDocument().recompute()
            FreeCADGui.SendMsgToActiveView("ViewFit")
            FreeCADGui.activeDocument().activeView().viewTop()
            # create output folder
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            # export VRML
            export_file_name = '{d:s}{s:s}{n:s}.wrl'.format(d=out_dir, s=os.sep, n=file_name)
            export_objects = []
            i = 0
            for part in parts_list:
                export_objects.append(expVRML.exportObject(freecad_object=objs[i],
                                      shape_color=model[part]['colour'],
                                      face_colors=None))
                i += 1
            scale = 1 / 2.54
            coloured_meshes = expVRML.getColoredMesh(Gui, export_objects, scale)
            expVRML.writeVRMLFile(coloured_meshes, export_file_name, used_colour_keys, L.LIST_int_license)
            # export STEP
            fusion = multiFuseObjs_wColors(FreeCAD, FreeCADGui, safe_name, objs, keepOriginals=True)
            exportSTEP(doc, file_name, out_dir, fusion)
            print('in STEP')
            L.addLicenseToStep('{d:s}/'.format(d=out_dir), '{n:s}.step'.format(n=file_name), L.LIST_int_license,
                               L.STR_int_licAuthor, L.STR_int_licEmail, L.STR_int_licOrgSys, L.STR_int_licPreProc)
            # save FreeCAD models
            saveFCdoc(App, Gui, doc, file_name, out_dir)

    FreeCAD.Console.PrintMessage('\r\nDone\r\n')


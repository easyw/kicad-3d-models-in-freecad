import sys
import os
import argparse
import yaml
import pprint


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--family', help='device type to build: TO-263  (default is all)',
                        type=str, nargs=1)
    parser.add_argument('-v', '--verbose', help='show extra information while generating the footprint',
                        action='store_true')
    return parser.parse_args()

import sys
import os

full_path=os.path.realpath(__file__)
script_dir_name =full_path.split(os.sep)[-2]
parent_path = full_path.split(script_dir_name)[0]
out_dir = parent_path + "_3Dmodels" + "/" + script_dir_name

sys.path.append("../_tools")
sys.path.append("cq_models")

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

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')
    print('Building DPAK')

    # args = get_args()

    from DPAK import DPAK, TO263

    CONFIG = 'DPAK_config.yaml'

    # if args.family:
        # if args.family[0] == 'TO263':
            # build_list = [TO263(CONFIG)]
        # else:
            # print('ERROR: family not recognised')
            # build_list = []
    # else:
    build_list = [TO263(CONFIG)]

    for package in build_list:
        n = 0
        for (body, tab, pins) in package.build_family(verbose=True):
            ModelName = 'foobar_{:d}'.format(n)
            n += 1
            Newdoc = FreeCAD.newDocument(ModelName)
            App.setActiveDocument(ModelName)
            App.ActiveDocument = App.getDocument(ModelName)
            Gui.ActiveDocument = Gui.getDocument(ModelName)
            show(body)
            show(tab)
            show(pins)
            doc = FreeCAD.ActiveDocument
            doc.Label=ModelName
            objs=FreeCAD.ActiveDocument.Objects
            i=0
            objs[i].Label = ModelName + "__body"
            i+=1
            objs[i].Label = ModelName + "__tab"
            i+=1
            objs[i].Label = ModelName + "__pins"
            i+=1
            restore_Main_Tools()
            FreeCAD.activeDocument().recompute()
            FreeCADGui.SendMsgToActiveView("ViewFit")
            FreeCADGui.activeDocument().activeView().viewAxometric()

    FreeCAD.Console.PrintMessage('\r\nDone\r\n')

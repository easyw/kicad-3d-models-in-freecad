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

    from DPAK import DPAK, TO252, TO263

    CONFIG = 'DPAK_config.yaml'

    # if args.family:
        # if args.family[0] == 'TO263':
            # build_list = [TO263(CONFIG)]
        # else:
            # print('ERROR: family not recognised')
            # build_list = []
    # else:
    build_list = [TO252(CONFIG)]

    for package in build_list:
        n = 0
        for model in package.build_family(verbose=True):
            FC_name = model['__name'].replace('-', '_')
            print(FC_name)
            n += 1
            Newdoc = FreeCAD.newDocument(FC_name)
            App.setActiveDocument(FC_name)
            App.ActiveDocument = App.getDocument(FC_name)
            Gui.ActiveDocument = Gui.getDocument(FC_name)
            for key in model.keys():
                if key is not '__name':
                    colour_key = model[key]['colour']
                    colour = shaderColors.named_colors[colour_key].getDiffuseInt()
                    colour_attr = colour + (0,)
                    show(model[key]['part'], colour_attr)
            doc = FreeCAD.ActiveDocument
            doc.Label=FC_name
            objs=FreeCAD.ActiveDocument.Objects
            i = 0
            for key in model.keys():
                if key is not '__name':
                    objs[i].Label = FC_name + "__" + key
                    i += 1
            restore_Main_Tools()
            FreeCAD.activeDocument().recompute()
            FreeCADGui.SendMsgToActiveView("ViewFit")
            FreeCADGui.activeDocument().activeView().viewTop()

    FreeCAD.Console.PrintMessage('\r\nDone\r\n')




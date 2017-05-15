# -*- coding: utf8 -*-
#!/usr/bin/python


"""
#############################################################################

CadQuery script to export KiCad 3D models from factory classes

#############################################################################

Original script: 
    Copyright (c) 2016 Hasan Yavuz Özderya https://bitbucket.org/hyOzd
                       Maurice https://github.com/easyw
                       Rene Poeschl https://github.com/poeschlr
                       
Refactored to be model-independent:
    Copyright (c) 2017 Ray Benitez https://github.com/hackscribble

#############################################################################

    This program is free software; you can redistribute it and/or modify   
    it under the terms of the GNU General Public License (GPL)             
    as published by the Free Software Foundation; either version 2 of      
    the License, or (at your option) any later version.                    
    for detail see the LICENCE text file.                                  
                                                                          
    This program is distributed in the hope that it will be useful,        
    but WITHOUT ANY WARRANTY; without even the implied warranty of         
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
    GNU Library General Public License for more details.                   
                                                                          
    You should have received a copy of the GNU Library General Public      
    License along with this program; if not, write to the Free Software    
    Foundation, Inc.,                                                      
    51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           
                                                                          
    The models generated with this script add the following exception:       
    As a special exception, if you create a design which uses this symbol, 
    and embed this symbol or unaltered portions of this symbol into the    
    design, this symbol does not by itself cause the resulting design to   
    be covered by the GNU General Public License. This exception does not  
    however invalidate any other reasons why the design itself might be    
    covered by the GNU General Public License. If you modify this symbol,  
    you may extend this exception to your version of the symbol, but you   
    are not obligated to do so. If you do not wish to do so, delete this   
    exception statement from your version.                                 

#############################################################################

"""

__title__ = 'factory export script'
__author__ = 'hackscribble'
__Comment__ = 'TBA'

___ver___ = '0.2 01/05/2017'


import sys
import os

full_path=os.path.realpath(__file__)
script_dir_name =full_path.split(os.sep)[-2]
parent_path = full_path.split(script_dir_name)[0]
out_dir = parent_path + "_3Dmodels" + "/" + script_dir_name

sys.path.append("./")
sys.path.append("../_tools")

import add_license as L


##########################################################################################

# MODEL LICENCE CONFIGURATION

# Details to be included in the generated models
L.STR_int_licAuthor = "Ray Benitez"
L.STR_int_licEmail = "hackscribble@outlook.com"

##########################################################################################

##########################################################################################

# DEVICE-DEPENDENT CONFIGURATION

# Models
from DPAK_factory import *
CONFIG = 'DPAK_config.yaml'

##########################################################################################


from datetime import datetime
import shaderColors
import exportPartToVRML as expVRML
import FreeCAD
import Draft
import ImportGui
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, multiFuseObjs_wColors, \
 checkRequirements

Gui.activateWorkbench("CadQueryWorkbench")

import FreeCADGui as Gui

if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui


# checking requirements

try:
    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery as cq
    from Helpers import show
except: # catch *all* exceptions
    msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    reply = QtGui.QMessageBox.information(None,"Info ...",msg)

checkRequirements(cq)

try:
    close_CQ_Example(App, Gui)
except: # catch *all* exceptions
    print("CQ 030 doesn't open example file")


def export_model(model):
    file_name = model['metadata']['name']
    parts = model['parts']
    parts_list = parts.keys()

    # create document
    safe_name = file_name.replace('-', '_')
    FreeCAD.Console.PrintMessage('Model: {:s}\r\n'.format(file_name))
    FreeCAD.newDocument(safe_name)
    App.setActiveDocument(safe_name)
    App.ActiveDocument = App.getDocument(safe_name)
    Gui.ActiveDocument = Gui.getDocument(safe_name)

    # colour model
    used_colour_keys = []
    for part in parts_list:
        colour_key = parts[part]['colour']
        used_colour_keys.append(colour_key)
        colour = shaderColors.named_colors[colour_key].getDiffuseInt()
        colour_attr = colour + (0,)
        show(parts[part]['name'], colour_attr)

    # label model and parts
    doc = FreeCAD.ActiveDocument
    doc.Label=safe_name
    objects=doc.Objects
    i = 0
    for part in parts_list:
        objects[i].Label = '{n:s}__{p:s}'.format(n=safe_name, p=part)
        i += 1
    restore_Main_Tools()
    doc.recompute()
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
        export_objects.append(expVRML.exportObject(freecad_object=objects[i],
                              shape_color=parts[part]['colour'],
                              face_colors=None))
        i += 1
    scale = 1 / 2.54
    coloured_meshes = expVRML.getColoredMesh(Gui, export_objects, scale)

    L.LIST_int_license[0] = "Copyright (C) " + datetime.now().strftime("%Y") + ", " + L.STR_int_licAuthor
    expVRML.writeVRMLFile(coloured_meshes, export_file_name, used_colour_keys, L.LIST_int_license)

    # export STEP
    fusion = multiFuseObjs_wColors(FreeCAD, FreeCADGui, safe_name, objects, keepOriginals=True)
    exportSTEP(doc, file_name, out_dir, fusion)
    L.addLicenseToStep('{d:s}/'.format(d=out_dir), '{n:s}.step'.format(n=file_name), L.LIST_int_license,
                       L.STR_int_licAuthor, L.STR_int_licEmail, L.STR_int_licOrgSys, L.STR_int_licPreProc)

    # save FreeCAD models
    saveFCdoc(App, Gui, doc, file_name, out_dir)
    return


if __name__ == "__main__":

    FreeCAD.Console.PrintMessage('\r\nEXPORT STARTED ...\r\n')
    build_list = Factory(CONFIG).get_build_list()
    
    for series in build_list:
        for model in series.build_series(verbose=True):
            export_model(model)

    FreeCAD.Console.PrintMessage('\r\nEXPORT FINISHED.\r\n')


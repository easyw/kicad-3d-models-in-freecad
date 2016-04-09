# -*- coding: utf-8 -*-

# PartToVRML.FCMacro
# creates VRML model of selected object(s), with colors (for Kicad and Blender compatibility)
# useful messages on Report view
#
# Copyright (c) 2015 Maurice easyw@katamail.com
# Copyright (c) 2015 Hasan Yavuz �zderya
# Copyright Nico
# this is a part of kicad StepUp tools; please refer to kicad StepUp tools
# for the full licence
#
#

__title__ = "PartToVRMLwithMaterials"
__author__ = "easyw-fc, hyOzd, poeschlr"
__url__     = "http://www.freecadweb.org/"
__version__ = "1.9.4 split export functionality and macro (make python import of this export scripts possible)"
__date__    = "09/04/2016"

__Comment__ = "This macro creates VRML model of selected object(s), with colors (for Kicad and Blender compatibility)"
__Web__ = "http://www.freecadweb.org/"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_PartToVRML"
__Icon__  = "/usr/lib/freecad/Mod/plugins/icons/Macro_PartToVRML.png"
__IconW__  = "C:/Users/User Name/AppData/Roaming/FreeCAD/Macro_PartToVRML.png"
__Help__ = "start the macro and follow the instructions or call export function from within python"
__Status__ = "stable"
__Requires__ = "Freecad"

# FreeCAD VRML python exporter is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This sw is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with expVrmlColor.FCMacro.  If not, see
# <http://www.gnu.org/licenses/>.

## export VRML from FreeCAD is a python macro that will export simplified VRML of
## a (multi)selected Part or fused Part to VRML optimized to Kicad and compatible with Blender
## the size of VRML is much smaller compared to the one exported from FC Gui
## and the loading/rendering time is smaller too
## change mesh deviation to increase quality of VRML

## to do
#  export material properties to vrml

import FreeCAD,FreeCADGui,Part,Mesh
#import PySide
from PySide import QtGui, QtCore
from collections import namedtuple
import sys, os
from os.path import expanduser
import re


def say(msg):
    FreeCAD.Console.PrintMessage(msg)
    FreeCAD.Console.PrintMessage('\n')

def clear_console():
    #clearing previous messages
    mw=FreeCADGui.getMainWindow()
    c=mw.findChild(QtGui.QPlainTextEdit, "Python console")
    c.clear()
    r=mw.findChild(QtGui.QTextEdit, "Report view")
    r.clear()

#if not Mod_ENABLED:
clear_console()

#color_list=[];index_color=0

Materials=True
## "PIN-01";"metal grey pins"
## "PIN-02";"gold pins"
## "IC-BODY-EPOXY-04";"black body"
## "RES-SMD-01";"resistor black body"
## "IC-BODY-EPOXY-01";"grey body"
## "CAP-CERAMIC-05";"dark grey body"
## "CAP-CERAMIC-06";"brown body"
## "PLASTIC-GREEN-01";"green body"
## "PLASTIC-BLUE-01";"blue body"
## "PLASTIC-WHITE-01";"white body"
## "IC-LABEL-01";"light brown label"
## LED-GREEN, LED-RED, LED-BLUE

as_is=""

metal_grey_pins="""material DEF PIN-01 Material {
        ambientIntensity 0.271
        diffuseColor 0.824 0.820 0.781
        specularColor 0.328 0.258 0.172
        emissiveColor 0.0 0.0 0.0
        shininess 0.70
        transparency 0.0
        }"""

gold_pins="""material DEF PIN-02 Material {
        ambientIntensity 0.379
        diffuseColor 0.859 0.738 0.496
        specularColor 0.137 0.145 0.184
        emissiveColor 0.0 0.0 0.0
        shininess 0.40
        transparency 0.0
        }"""

black_body="""material DEF IC-BODY-EPOXY-04 Material {
        ambientIntensity 0.293
        diffuseColor 0.148 0.145 0.145
        specularColor 0.180 0.168 0.160
        emissiveColor 0.0 0.0 0.0
        shininess 0.35
        transparency 0.0
        }"""

resistor_black_body="""material DEF RES-SMD-01 Material {
        diffuseColor 0.082 0.086 0.094
        emissiveColor 0.000 0.000 0.000
        specularColor 0.066 0.063 0.063
        ambientIntensity 0.638
        transparency 0.0
        shininess 0.3
        }"""

dark_grey_body="""material DEF CAP-CERAMIC-05 Material {
        ambientIntensity 0.179
        diffuseColor 0.273 0.273 0.273
        specularColor 0.203 0.188 0.176
        emissiveColor 0.0 0.0 0.0
        shininess 0.15
        transparency 0.0
        }"""

grey_body="""material DEF IC-BODY-EPOXY-01 Material {
        ambientIntensity 0.117
        diffuseColor 0.250 0.262 0.281
        specularColor 0.316 0.281 0.176
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

brown_body="""material DEF CAP-CERAMIC-06 Material {
        ambientIntensity 0.453
        diffuseColor 0.379 0.270 0.215
        specularColor 0.223 0.223 0.223
        emissiveColor 0.0 0.0 0.0
        shininess 0.15
        transparency 0.0
        }"""

light_brown_body="""material DEF RES-THT-01 Material {
        ambientIntensity 0.149
        diffuseColor 0.883 0.711 0.492
        specularColor 0.043 0.121 0.281
        emissiveColor 0.0 0.0 0.0
        shininess 0.40
        transparency 0.0
        }"""

blue_body="""material DEF PLASTIC-BLUE-01 Material {
        ambientIntensity 0.565
        diffuseColor 0.137 0.402 0.727
        specularColor 0.359 0.379 0.270
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

green_body="""material DEF PLASTIC-GREEN-01 Material {
        ambientIntensity 0.315
        diffuseColor 0.340 0.680 0.445
        specularColor 0.176 0.105 0.195
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

orange_body="""material DEF PLASTIC-ORANGE-01 Material {
        ambientIntensity 0.284
        diffuseColor 0.809 0.426 0.148
        specularColor 0.039 0.102 0.145
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

red_body="""material DEF RED-BODY Material {
        ambientIntensity 0.683
        diffuseColor 0.700 0.100 0.050
        emissiveColor 0.000 0.000 0.000
        specularColor 0.300 0.400 0.150
        transparency 0.0
        shininess 0.25
        }"""

pink_body="""material DEF CAP-CERAMIC-02 Material {
        ambientIntensity 0.683
        diffuseColor 0.578 0.336 0.352
        specularColor 0.105 0.273 0.270
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

yellow_body="""material DEF PLASTIC-YELLOW-01 Material {
        ambientIntensity 0.522
        diffuseColor 0.832 0.680 0.066
        specularColor 0.160 0.203 0.320
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

white_body="""material DEF PLASTIC-WHITE-01 Material {
        ambientIntensity 0.494
        diffuseColor 0.895 0.891 0.813
        specularColor 0.047 0.055 0.109
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

light_brown_label="""material DEF IC-LABEL-01 Material {
        ambientIntensity 0.082
        diffuseColor 0.691 0.664 0.598
        specularColor 0.000 0.000 0.000
        emissiveColor 0.0 0.0 0.0
        shininess 0.01
        transparency 0.0
        }"""

led_red="""material DEF LED-RED Material {
        ambientIntensity 0.789
        diffuseColor 0.700 0.100 0.050
        emissiveColor 0.000 0.000 0.000
        specularColor 0.300 0.400 0.150
        transparency 0.10
        shininess 0.125
        }"""

led_green="""material DEF LED-GREEN Material {
        ambientIntensity 0.789
        diffuseColor 0.400 0.700 0.150
        emissiveColor 0.000 0.000 0.000
        specularColor 0.600 0.300 0.100
        transparency 0.10
        shininess 0.05
        }"""

led_blue="""material DEF LED-BLUE Material {
        ambientIntensity 0.789
        diffuseColor 0.100 0.250 0.700
        emissiveColor 0.000 0.000 0.000
        specularColor 0.500 0.600 0.300
        transparency 0.10
        shininess 0.125
        }"""

led_white="""material DEF LED-WHITE Material {
        ambientIntensity 0.494
        diffuseColor 0.895 0.891 0.813
        specularColor 0.047 0.055 0.109
        emissiveColor 0.0 0.0 0.0
        transparency 0.10
        shininess 0.125
        }"""

material_properties_names=["as is","metal grey pins","gold pins","black body","resistor black body",\
                           "grey body","dark grey body","brown body","light brown body","blue body",\
                           "green body","orange body","red_body","pink body","yellow body","white body","light brown label",\
                           "led red","led green","led blue", "led white"]
material_properties=[as_is,metal_grey_pins,gold_pins,black_body,resistor_black_body,\
                     grey_body,dark_grey_body,brown_body,light_brown_body,blue_body,\
                     green_body,orange_body,red_body,pink_body,yellow_body,white_body,light_brown_label,\
                     led_red,led_green,led_blue,led_white]

material_definitions=""
for mat in material_properties[1:]:
    material_definitions+="Shape {\n    appearance Appearance {"+mat+"\n    }\n}\n"

material_ids=[]
material_ids.append("")

for mat in material_properties[1:]:
    m = re.search('DEF\s(.+?)\sMaterial', mat)
    if m:
        found = m.group(1)
        #say(found)
        material_ids.append(found)
#say(material_ids)
#say (material_definitions)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 164)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(180, 40, 191, 22))
        self.comboBox.setMaxVisibleItems(25)
        self.comboBox.setObjectName("comboBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 53, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 53, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 40, 31, 31))
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(120, 40, 31, 31))
        self.plainTextEdit_2.setBackgroundVisible(False)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 20, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 351, 16))
        self.label_4.setObjectName("label_4")
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.SIGNAL_comboBox_Changed)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def SIGNAL_comboBox_Changed(self,text):
        #say("combo changed "+text)
        comboBox_Changed(text)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Material Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Materials", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setToolTip(QtGui.QApplication.translate("Dialog", "Shape Color", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit_2.setToolTip(QtGui.QApplication.translate("Dialog", "Diffuse Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Diffuse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Note: set Material will unmatch colors between wrl and STEP ", None, QtGui.QApplication.UnicodeUTF8))

#####################################
# Function infoDialog
#####################################
def infoDialog(msg):
    #QtGui.qFreeCAD.setOverrideCursor(QtCore.Qt.WaitCursor)
    QtGui.qApp.restoreOverrideCursor()
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Info Message",msg )
    diag.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    diag.exec_()
    QtGui.qApp.restoreOverrideCursor()


# points: [Vector, Vector, ...]
# faces: [(pi, pi, pi), ], pi: point index
# color: (Red, Green, Blue), values range from 0 to 1.0 or color name as defined within this document.
Mesh = namedtuple('Mesh', ['points', 'faces', 'color', 'transp'])
#object name: I get an error for freecad_object.Transparency so i use App.getObject('name')
exportObject = namedtuple('exportObject', ['freecad_object', 'shape_color', 'face_colors'])

def shapeToMesh(shape, color, transp, scale=None):
    mesh_deviation=0.03 #the smaller the best quality, 1 coarse; 0.03 good compromise :)
    mesh_data = shape.tessellate(mesh_deviation)
    points = mesh_data[0]
    if scale != None:
        points = map(lambda p: p*scale, points)
    newMesh= Mesh(points = points,
                faces = mesh_data[1],
                color = color, transp=transp)
    return newMesh

def writeVRMLFile(objects, filepath):
    """Export given list of Mesh objects to a VRML file.

    `Mesh` structure is defined at root."""

    with open(filepath, 'w') as f:
        # write the standard VRML header
        f.write("#VRML V2.0 utf8\n#kicad StepUp wrl exported\n\n")
        f.write(material_definitions)

        for obj in objects:
            f.write("Shape { geometry IndexedFaceSet \n{ coordIndex [")
            # write coordinate indexes for each face
            f.write(','.join("%d,%d,%d,-1" % f for f in obj.faces))
            f.write("]\n") # closes coordIndex
            f.write("coord Coordinate { point [")
            # write coordinate points for each vertex
            #f.write(','.join('%.3f %.3f %.3f' % (p.x, p.y, p.z) for p in obj.points))
            f.write(','.join('%.3f %.3f %.3f' % (p.x, p.y, p.z) for p in obj.points))
            f.write("]\n}") # closes Coordinate
            #shape_col=(1.0, 0.0, 0.0)#, 0.0)
            f.write("}\n") # closes points

            #say(color_list_mat[col_index])
            if not isinstance(obj.color,basestring):
                shape_transparency=obj.transp
                f.write("appearance Appearance{material Material{diffuseColor %f %f %f\n" % obj.color)
                f.write("transparency %f}}" % shape_transparency)
                f.write("}\n") # closes Shape
            else:
                material_index=material_properties_names.index(obj.color)
                #say(material_properties[material_index])
                #f.write("appearance Appearance{"+material_properties[material_index]+"}}\n")
                f.write("appearance Appearance{material USE "+material_ids[material_index]+" }}\n")
        say(filepath+' written')
###
def comboBox_Changed(text_combo):
    global ui
    say(text_combo)
    material_index=material_properties_names.index(text_combo)
    #say(material_index)
    mat_prop = material_properties[material_index].split('\n')
    if len(mat_prop)>1:
        say(mat_prop[2])
        color_rgb=mat_prop[2].split(' ')
        say (color_rgb)
        say(color_rgb[9]+" "+color_rgb[10]+" "+color_rgb[11])
        pal = QtGui.QPalette()
        bgc = QtGui.QColor(float(color_rgb[9])*255,float(color_rgb[10])*255, float(color_rgb[11])*255)
        pal.setColor(QtGui.QPalette.Base, bgc)
        ui.plainTextEdit_2.viewport().setPalette(pal)

###
def getColoredMesh(Gui, export_objects , scale=None):
    """ Exports given ComponentModel object using FreeCAD.

    `componentObjs` : a ComponentObjs list
    `fullfilePathName` : name of the FC file, extension is important

    """
    meshes=[]
    applyDiffuse=0
    for exp_obj in export_objects:
        gui_obj = Gui.ActiveDocument.getObject(exp_obj.freecad_object.Name)
        color=exp_obj.shape_color
        if color is None:
            color = gui_obj.ShapeColor
            color = color [:-1]

        transparency=gui_obj.Transparency/100.0
        shape1=exp_obj.freecad_object.Shape

        if(exp_obj.face_colors is None or len(exp_obj.face_colors) != len(shape1.Faces)):
            applyDiffuse=0 #use shape color for all faces
        else:
            applyDiffuse=1

        for face_index in range(len(shape1.Faces)):
            singleFace=shape1.Faces[face_index]
            if applyDiffuse:
                meshes.append(shapeToMesh(singleFace, exp_obj.face_colors[face_index], transparency, scale))
            else:
                meshes.append(shapeToMesh(singleFace, color, transparency, scale))
    return meshes
###
def getNamedColors(color_list):
     used_colors = list(set(color_list))
     return [x for x in used_colors if isinstance(x, basestring)]

def determineColors(Gui, objects):
    global ui
    know_material_substitutions={}
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.comboBox.addItems(material_properties_names)
    material="as is"


    objs = []
    for obj in sel:
        freecad_object = Gui.ActiveDocument.getObject(obj.Name)
        face_colors = []
        for color in freecad_object.DiffuseColor:
            color = color[:-1]
            say(color)
            if color not in know_material_substitutions:
                pal = QtGui.QPalette()
                bgc = QtGui.QColor(color[0]*255, color[1]*255, color[2]*255)
                pal.setColor(QtGui.QPalette.Base, bgc)
                ui.plainTextEdit.viewport().setPalette(pal)
                #ui.comboBox.addItems(color_list)
                reply=Dialog.exec_()
                #Dialog.exec_()
                say(reply)
                if reply==1:
                    retval = str(ui.comboBox.currentText())
                    if retval == "as is":
                        material = color
                    else:
                        material = retval
                else:
                    #material="as is"
                    material=color
                know_material_substitutions.update({color:material})
                say(material)
                face_colors.append(material)
            else:
                face_colors.append(know_material_substitutions[color])
        objs.append(exportObject(freecad_object = obj,
                shape_color=face_colors[0],
                face_colors=face_colors))
    return (objs, getNamedColors(know_material_substitutions.values()))

def generateFileName(label, fullFilePathName, scale):
    path, fname = os.path.split(fullfilePathName)
    fname=os.path.splitext(fname)[0]
    if scale != None:
        filename=path+os.sep+label+'.wrl'
    else:
        filename=path+os.sep+label+'_1_1.wrl'
    say(filename)
    return filename

def exportVRMLfromSelction(Gui, fullFilePathName):
    sel = FreeCADGui.Selection.getSelection()
    if not sel:
        FreeCAD.Console.PrintWarning("Select something first!\n\n")
        msg="export VRML from FreeCAD is a python macro that will export simplified VRML of "
        msg+="a (multi)selected Part or fused Part to VRML optimized to Kicad and compatible with Blender "
        msg+="the size of VRML is much smaller compared to the one exported from FC Gui "
        msg+="and the loading/rendering time is also smaller\n"
        msg+="change mesh deviation to increase quality of VRML"
        say(msg)
    else:
        export_objects, used_color_keys = determineColors(Gui, sel)
        scale = 1/2.54
        export_file_name = generateFileName(sel[0].Label, fullFilePathName, scale)
        #export(objs, fullFilePathName, scale=None)
        colored_meshes = export(Gui, objs , scale)

        writeVRMLFile(colored_meshes, export_file_name)

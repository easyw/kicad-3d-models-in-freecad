# -*- coding: utf8 -*-                                                      *
#* These are a FreeCAD & cadquery tools                                      *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cad tools functions                                                      *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
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

__title__ = "CadQuery exporting and fusion libs"
__author__ = "maurice"
__Comment__ = 'CadQuery exporting and fusion libs to generate STEP and VRML models with colors'

___ver___ = "1.2.3 16/08/2015"

import FreeCAD, Draft, FreeCADGui
import ImportGui
from Gui.Command import *

#helper funcs for displaying messages in FreeCAD
def say(*arg):
    FreeCAD.Console.PrintMessage(" ".join(map(str,arg)) + "\r\n")
    
def sayw(*arg):
    FreeCAD.Console.PrintWarning(" ".join(map(str,arg)) + "\r\n")
    
def saye(*arg):
    FreeCAD.Console.PrintError(" ".join(map(str,arg)) + "\r\n")

###################################################################
# close_CQ_Example()  maui
#	Function to close CQ Example and restore "
#   "Report view" "Python console" "Combo View"
###################################################################
def close_CQ_Example(App, Gui):

    #close the example
    App.setActiveDocument("Ex000_Introduction")
    App.ActiveDocument=App.getDocument("Ex000_Introduction")
    Gui.ActiveDocument=Gui.getDocument("Ex000_Introduction")
    App.closeDocument("Ex000_Introduction")
    FreeCAD.Console.PrintMessage('\r\nEx000 Closed\r\n')

    #Getting the main window will allow us to start setting things up the way we want
    mw = FreeCADGui.getMainWindow()

    #Adjust the docks as usual
    dockWidgets = mw.findChildren(QtGui.QDockWidget)
    for widget in dockWidgets:
        if (widget.objectName() == "Report view") or (widget.objectName() == "Python console") or (widget.objectName() == "Combo View"):
            widget.setVisible(True)
        if (widget.objectName()=="cqCodeView"):
            widget.setVisible(False)
    FreeCAD.Console.PrintMessage('Dock adjusted\r\n')

    return 0


###################################################################
# FuseObjs_wColors()  maui
#	Function to fuse two objects together.
###################################################################
def FuseObjs_wColors(App, Gui,
                           docName, part1, part2):

    # Fuse two objects
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(docName)
    App.ActiveDocument=App.getDocument(docName)
    Gui.ActiveDocument=Gui.getDocument(docName)
    App.activeDocument().addObject("Part::MultiFuse","Fusion")
    App.activeDocument().Fusion.Shapes = [App.ActiveDocument.getObject(part1), App.ActiveDocument.getObject(part2)]
    Gui.ActiveDocument.Fusion.ShapeColor=Gui.ActiveDocument.getObject(part1).ShapeColor
    Gui.ActiveDocument.Fusion.DisplayMode=Gui.ActiveDocument.getObject(part1).DisplayMode
    App.ActiveDocument.recompute()

    App.ActiveDocument.addObject('Part::Feature','Fusion').Shape=App.ActiveDocument.Fusion.Shape
    App.ActiveDocument.ActiveObject.Label=docName

    Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Fusion.ShapeColor
    Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Fusion.LineColor
    Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Fusion.PointColor
    Gui.ActiveDocument.ActiveObject.DiffuseColor=Gui.ActiveDocument.Fusion.DiffuseColor
    App.ActiveDocument.recompute()

    ## ## TBD refine Shape to reduce size maui
    ## App.ActiveDocument.addObject('Part::Feature','Fusion').Shape=App.ActiveDocument.Fusion.Shape.removeSplitter()
    ## App.ActiveDocument.ActiveObject.Label=App.ActiveDocument.Fusion.Label
    ## Gui.ActiveDocument.Fusion.hide()
    ##
    ## Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Fusion.ShapeColor
    ## Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Fusion.LineColor
    ## Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Fusion.PointColor
    ## Gui.ActiveDocument.ActiveObject.DiffuseColor=Gui.ActiveDocument.Fusion.DiffuseColor
    ## App.ActiveDocument.recompute()
    ## App.ActiveDocument.ActiveObject.Label=docName
    #######################################################
    # Remove the part1 part2 objects
    App.getDocument(docName).removeObject(part1)
    App.getDocument(docName).removeObject(part2)

    # Remove the fusion itself
    App.getDocument(docName).removeObject("Fusion")
    ## App.getDocument(docName).removeObject("Fusion001")

    return 0

###################################################################
# FuseObjs_wColors_naming()  maui
#	Function to fuse two objects together.
###################################################################
def FuseObjs_wColors_naming(App, Gui,
                           docName, part1, part2, name):

    # Fuse two objects
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(docName)
    App.ActiveDocument=App.getDocument(docName)
    Gui.ActiveDocument=Gui.getDocument(docName)
    App.activeDocument().addObject("Part::MultiFuse","Fusion")
    App.activeDocument().Fusion.Shapes = [App.ActiveDocument.getObject(part1), App.ActiveDocument.getObject(part2)]
    Gui.ActiveDocument.Fusion.ShapeColor=Gui.ActiveDocument.getObject(part1).ShapeColor
    Gui.ActiveDocument.Fusion.DisplayMode=Gui.ActiveDocument.getObject(part1).DisplayMode
    App.ActiveDocument.recompute()

    App.ActiveDocument.addObject('Part::Feature','Fusion').Shape=App.ActiveDocument.Fusion.Shape
    App.ActiveDocument.ActiveObject.Label=name

    Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Fusion.ShapeColor
    Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Fusion.LineColor
    Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Fusion.PointColor
    Gui.ActiveDocument.ActiveObject.DiffuseColor=Gui.ActiveDocument.Fusion.DiffuseColor
    App.ActiveDocument.recompute()

    ## ## TBD refine Shape to reduce size maui
    ## App.ActiveDocument.addObject('Part::Feature','Fusion').Shape=App.ActiveDocument.Fusion.Shape.removeSplitter()
    ## App.ActiveDocument.ActiveObject.Label=App.ActiveDocument.Fusion.Label
    ## Gui.ActiveDocument.Fusion.hide()
    ##
    ## Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Fusion.ShapeColor
    ## Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Fusion.LineColor
    ## Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Fusion.PointColor
    ## Gui.ActiveDocument.ActiveObject.DiffuseColor=Gui.ActiveDocument.Fusion.DiffuseColor
    ## App.ActiveDocument.recompute()
    ## App.ActiveDocument.ActiveObject.Label=docName
    #######################################################
    # Remove the part1 part2 objects
    App.getDocument(docName).removeObject(part1)
    App.getDocument(docName).removeObject(part2)

    # Remove the fusion itself
    App.getDocument(docName).removeObject("Fusion")
    ## App.getDocument(docName).removeObject("Fusion001")

    return 0    
    
###################################################################
# CutObjs_wColors()  maui
#	Function to fuse two objects together.
###################################################################
def CutObjs_wColors(App, Gui,
                           docName, part1, part2):

    # Fuse two objects
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(docName)
    App.ActiveDocument=App.getDocument(docName)
    Gui.ActiveDocument=Gui.getDocument(docName)
    #Gui.activateWorkbench("PartWorkbench")
    obj1=App.ActiveDocument.getObject(part1)
    obj2=App.ActiveDocument.getObject(part2)
    App.activeDocument().addObject("Part::Cut","Cut")

    App.activeDocument().Cut.Base = obj1
    App.activeDocument().Cut.Tool = obj2
    #Gui.activeDocument().getObject(objs[0].Name).Visibility=False
    #Gui.activeDocument().getObject(objs[2].Name).Visibility=False
    #Gui.ActiveDocument.Cut.ShapeColor=Gui.ActiveDocument.Shape0_0403661773302.ShapeColor
    #Gui.ActiveDocument.Cut.DisplayMode=Gui.ActiveDocument.Shape0_0403661773302.DisplayMode
    App.ActiveDocument.recompute()

    ### App.ActiveDocument.addObject('Part::Feature','Fusion').Shape=App.ActiveDocument.Fusion.Shape
    App.ActiveDocument.ActiveObject.Label=docName

    # Remove the part1 part2 objects
    App.getDocument(docName).removeObject(part1)
    App.getDocument(docName).removeObject(part2)

    # Remove the fusion itself
    #App.getDocument(docName).removeObject("Fusion")
    ## App.getDocument(docName).removeObject("Fusion001")

    return 0

###################################################################
# GetListOfObjects()  maui
#	Function to fuse two objects together.
###################################################################
def GetListOfObjects(App, docName):

    # Create list of objects, starting with object names
    objs=[]
    for obj in docName.Objects:
        # do what you want to automate
        objs.append(getAppObject(obj.Name))
        say(obj.Name)

    return objs

###################################################################
# Color_Objects()  maui
#	Function to color objects.
###################################################################
def Color_Objects(Gui,obj,color):

    say('Coloring:',gbj.Name)
    
    gObj = getGuiObject(obj.Name)
    
    if not gObj:
        return 0
    
    gObj.ShapeColor = color
    gObj.LineColor = color
    gObj.PointColor = color
    gObj.DiffuseColor = color

    return 0


###################################################################
# restore_Main_Tools()  maui
#	Function to restore
#   "Report view" "Python console" "Combo View"
###################################################################
def restore_Main_Tools():

    #Getting the main window will allow us to start setting things up the way we want
    mw = FreeCADGui.getMainWindow()

    #Adjust the docks as usual
    dockWidgets = mw.findChildren(QtGui.QDockWidget)
    for widget in dockWidgets:
        if (widget.objectName() == "Report view") or (widget.objectName() == "Python console") or (widget.objectName() == "Combo View"):
            widget.setVisible(True)
        if (widget.objectName()=="cqCodeView"):
            widget.setVisible(False)

    return 0


###################################################################
# z_RotateObject()  maui
#	Function to z-rotate an object
#
###################################################################
def z_RotateObject(doc, rot):

    # z-Rotate
    objs=GetListOfObjects(FreeCAD, doc)
    FreeCAD.getDocument(doc.Name).getObject(objs[0].Name).Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),rot))

    return 0


###################################################################
# exportSTEP()  maui
#	Function to Export to STEP
#
###################################################################
def exportSTEP(doc,modelName, dir):

    ## Export to STEP
    ## Get cwd

    ## outdir=os.path.dirname(os.path.realpath(__file__))+dir
    outdir=dir
    FreeCAD.Console.PrintMessage('\r\n'+outdir)
    StepFileName=outdir+'/'+modelName+'.step'
    objs=[]
    objs=GetListOfObjects(FreeCAD, doc)
    import ImportGui
    FreeCAD.Console.PrintMessage('\r\n'+StepFileName)
    # FreeCAD.Console.PrintMessage(objs)
    FreeCAD.Console.PrintMessage('\r\n'+outdir)
    ImportGui.export(objs,StepFileName)

    return 0

###################################################################
# exportVRML()  maui
#	Function to Export to VRML
#
###################################################################
def exportVRML(doc,modelName,scale,dir):

    ## Export to VRML scaled 1/2.54
    #VrmlFileName='.//'+doc.Label+'.wrl'
    ## outdir=os.path.dirname(os.path.realpath(__file__))+dir
    outdir=dir
    FreeCAD.Console.PrintMessage('\r\n'+outdir)
    VrmlFileName=outdir+'/'+modelName+'.wrl'
    StepFileName=outdir+'/'+modelName+'.step'
    objs=[]
    objs=GetListOfObjects(FreeCAD, doc)

    vrml = FreeCAD.ActiveDocument.addObject('Part::Feature','Vrml_model')
    vrml.Shape=objs[0].Shape
    vrml.Label='Vrml_model'
    
    #copy colors across
    copyColors(objs[0].Name, vrml.Name)
    
    newObj=FreeCAD.getDocument(doc.Name).getObject('Vrml_model')
    #scale to export vrml  start
    Draft.scale(newObj,delta=FreeCAD.Vector(scale,scale,scale),center=FreeCAD.Vector(0,0,0),legacy=True)

    FreeCAD.activeDocument().recompute()
    #we need to remove object to export only scaled model
    FreeCAD.getDocument(doc.Name).removeObject(objs[0].Name)
    __objs__=[]
    __objs__.append(FreeCAD.getDocument(doc.Name).getObject("Vrml_model"))
    FreeCADGui.export(__objs__,VrmlFileName)
    FreeCAD.activeDocument().recompute()

    #restoring step module
    import ImportGui
    ImportGui.insert(StepFileName,doc.Name)

    FreeCAD.Console.PrintMessage(FreeCAD.ActiveDocument.ActiveObject.Label+" exported and scaled to Vrml\r\n")
    del __objs__

    return 0

###################################################################
# saveFCdoc()  maui
#	Function to save in Native FreeCAD format the doc
#
###################################################################
def saveFCdoc(App, Gui, doc, modelName,dir):

    ## Save to disk in native format
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(doc.Name)
    App.ActiveDocument=App.getDocument(doc.Name)
    Gui.ActiveDocument=Gui.getDocument(doc.Name)

    ## outdir=os.path.dirname(os.path.realpath(__file__))+dir
    outdir=dir
    FreeCAD.Console.PrintMessage('\r\n'+outdir)
    FCName=outdir+'/'+modelName+'.FCStd'
    FreeCAD.Console.PrintMessage('\r\n'+FCName+'\r\n')
    App.getDocument(doc.Name).saveAs(FCName)
    App.ActiveDocument.recompute()

    App.getDocument(doc.Name).Label = doc.Name
    Gui.SendMsgToActiveView("Save")
    App.getDocument(doc.Name).save()

    return 0
    
#Find a GUI object (within the active document) (or return None if it does not exist)
def getGuiObject(objName):
    if type(objName) is not str:
        sayw("getGuiObject - 'objName' must be a string")
    try:
        return FreeCADGui.ActiveDocument.getObject(objName)
    except NameError:
        sayw("FreeCADGui.ActiveDocument has no object named",objName)
    except:
        sayw("Error in getGuiObject()")
    return None
    
#Find an APP object (within the active document) (or return None if it does not exist)
def getAppObject(objName):
    if type(objName) is not str:
        sayw("getAppObject - 'objName' must be a string")
    try:
        return FreeCAD.ActiveDocument.getObject(objName)
    except NameError:
        sayw("FreeCAD.Activedocument has no object named",objName)
    except:
        sayw("Error in getAppObject()")
        
#pass the names of two objects
#copy the colors of obj1 (master) to obj2 (slave)
def copyColors(obj1Name, obj2Name):
    
    obj1 = getGuiObject(obj1Name)
    obj2 = getGuiObject(obj2Name)
    
    #couldn't get object references
    if not obj1 or not obj2:
        sayw("copyColors() - could not find objects!")
        return
        
    #copy the color info across
    obj2.ShapeColor = obj1.ShapeColor
    obj2.LineColor = obj1.LineColor
    obj2.PointColor = obj1.PointColor
    obj2.DiffuseColor = obj1.DiffuseColor
    
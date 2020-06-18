#!/usr/bin/python
# -*- coding: utf-8 -*-
#****************************************************************************
#*                                                                          *
#* These are a FreeCAD & cadquery tools                                     *
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

___ver___ = "1.2.6 18/06/2020"

import FreeCAD, Draft, FreeCADGui
from cqToolsExceptions import *
import ImportGui
if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui
#from Gui.Command import *
import os, sys

#helper funcs for displaying messages in FreeCAD
def say(*arg):
    FreeCAD.Console.PrintMessage(" ".join(map(str,arg)) + "\r\n")

def sayw(*arg):
    FreeCAD.Console.PrintWarning(" ".join(map(str,arg)) + "\r\n")

def saye(*arg):
    FreeCAD.Console.PrintError(" ".join(map(str,arg)) + "\r\n")

def mk_string(input):
    if (sys.version_info > (3, 0)):  #py3
        if isinstance(input, str):
            return input
        else:
            input =  input.encode('utf-8')
            return input
    else:  #py2
        if type(input) == unicode:
            input =  input.encode('utf-8')
            return input
        else:
            return input
##

def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)
##

def checkUnion(docu):
    """ counting NBR of objects in the doc
        if NBR>1, then the STEP file is not correctly Unioned in a siingle object
    """
    i=0
    for o in docu.Objects:
        i+=1
    if i != 1:
        return False
    else:
        return True
##

def checkBOP(shape):
    """ checking BOP errors of a shape
    returns:
      - True if Shape is Valid
      - the Shape errors
    """

    # enabling BOP check
    paramGt = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/Part/CheckGeometry")
    paramGt.SetBool("RunBOPCheck",True)

    try:
        shape.check(True)
        return True
    except Exception:
        return sys.exc_info()[1] #ValueError #sys.exc_info() #False
##

#from an argument string, extract a list of numbers
#numbers can be individual e.g. "3"
#numbers can be comma delimited e.g. "3,5"
#numbers can be in a range e.g. "3-8"
#numbers can't be < 1
def getListOfNumbers(string):
    numbers = []
    #does this number contain a hyphen?
    if '-' in string:
        if len(string.split('-')) == 2:
            a,b = string.split('-')
            try:
                a = int(a)
                b = int(b)
                if a > 0 and b > a:
                    numbers = [i for i in range(a,b+1)]
            except Exception as exp:
                FreeCAD.Console.PrintWarning("Error in getListOfNumbers range case:")
                FreeCAD.Console.PrintWarning('{:s}\n'.format(exp))

    elif ',' in string:
        #Now, split by comma
        ss = string.split(",")

        for s in ss:
            try:
                numbers += [int(s)]
            except Exception as exp:
                FreeCAD.Console.PrintWarning("Error in getListOfNumbers list case:")
                FreeCAD.Console.PrintWarning('{:s}\n'.format(exp))

    else:
        try:
            numbers = [int(string)]
        except Exception as exp:
            FreeCAD.Console.PrintWarning("Error in getListOfNumbers single number case:")
            FreeCAD.Console.PrintWarning('{:s}\n'.format(exp))

    return numbers

###################################################################
# open_CQ_Example()  Qbort
#   Function to open CQ Example
###################################################################
def open_CQ_Example(App, Gui):
    App.newDocument("Ex000_Introduction")

###################################################################
# close_CQ_Example()  maui
#   Function to close CQ Example and restore "
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
#   Function to fuse two objects together.
###################################################################
def FuseObjs_wColors(App, Gui,
                           docName, part1, part2, keepOriginals=False):

    # Fuse two objects
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(docName)
    App.ActiveDocument=App.getDocument(docName)
    Gui.ActiveDocument=Gui.getDocument(docName)
    App.activeDocument().addObject("Part::MultiFuse","Fusion")
    App.activeDocument().Fusion.Shapes = [App.activeDocument().getObject(part1),App.activeDocument().getObject(part2),]
    Gui.activeDocument().getObject(part1).Visibility=False
    Gui.activeDocument().getObject(part2).Visibility=False
    Gui.ActiveDocument.Fusion.ShapeColor=Gui.activeDocument().getObject(part1).ShapeColor
    Gui.ActiveDocument.Fusion.DisplayMode=Gui.activeDocument().getObject(part1).DisplayMode
    App.ActiveDocument.ActiveObject.Label=docName
    App.ActiveDocument.recompute()
    
    fusedObj = App.ActiveDocument.ActiveObject
    SimpleCopy_wColors(fusedObj)
    FreeCAD.ActiveDocument.removeObject(fusedObj.Name)
    App.getDocument(docName).removeObject(part1)
    App.getDocument(docName).removeObject(part2)
    fused_obj = App.ActiveDocument.ActiveObject
    
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

    return fused_obj
    
###################################################################
# SimpleCopy_wColors()  maui
#   Function to make a simple copy with colors
###################################################################
def SimpleCopy_wColors(obj):

    s=obj.Shape
    FreeCAD.ActiveDocument.addObject('Part::Feature',obj.Label+"_cp").Shape=s
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor
    FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.getObject(obj.Name).LineColor
    FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.getObject(obj.Name).PointColor
    FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.getObject(obj.Name).DiffuseColor
    FreeCADGui.ActiveDocument.ActiveObject.Transparency=FreeCADGui.ActiveDocument.getObject(obj.Name).Transparency
    new_label=obj.Label+'_cp'
    FreeCAD.ActiveDocument.ActiveObject.Label=new_label
    FreeCAD.ActiveDocument.recompute()

    
###################################################################
# FuseObjs_wColors()  poeschlr
#   Function to fuse multible objects together.
###################################################################
def multiFuseObjs_wColors(App, Gui, docName, objs, keepOriginals=False):

    # Fuse two objects
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(docName)
    App.ActiveDocument=App.getDocument(docName)
    Gui.ActiveDocument=Gui.getDocument(docName)
    App.activeDocument().addObject("Part::MultiFuse","Fusion")
    App.activeDocument().Fusion.Shapes = objs
    Gui.ActiveDocument.Fusion.ShapeColor=Gui.ActiveDocument.getObject(objs[0].Name).ShapeColor
    Gui.ActiveDocument.Fusion.DisplayMode=Gui.ActiveDocument.getObject(objs[0].Name).DisplayMode
    App.ActiveDocument.recompute()

    App.ActiveDocument.addObject('Part::Feature','Fusion').Shape=App.ActiveDocument.Fusion.Shape
    App.ActiveDocument.ActiveObject.Label=docName
    fused_obj = App.ActiveDocument.ActiveObject

    Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Fusion.ShapeColor
    Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Fusion.LineColor
    Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Fusion.PointColor
    Gui.ActiveDocument.ActiveObject.DiffuseColor=Gui.ActiveDocument.Fusion.DiffuseColor
    App.ActiveDocument.recompute()

    # Remove the part1 part2 objects
    if not keepOriginals:
        for o in objs:
            App.getDocument(docName).removeObject(o.Name)

    # Remove the fusion itself
    fusedObj = App.ActiveDocument.ActiveObject
    SimpleCopy_wColors(fusedObj)
    FreeCAD.ActiveDocument.removeObject(fusedObj.Name)
    fused_obj = App.ActiveDocument.ActiveObject

    return fused_obj

###################################################################
# FuseObjs_wColors()  poeschlr
#   Function to fuse multible objects together.
###################################################################
def multiFuseObjs_wColors(App, Gui, docName, objs, keepOriginals=False):

    # Fuse two objects
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(docName)
    App.ActiveDocument=App.getDocument(docName)
    Gui.ActiveDocument=Gui.getDocument(docName)
    App.activeDocument().addObject("Part::MultiFuse","Fusion")
    App.activeDocument().Fusion.Shapes = objs
    Gui.ActiveDocument.Fusion.ShapeColor=Gui.ActiveDocument.getObject(objs[0].Name).ShapeColor
    Gui.ActiveDocument.Fusion.DisplayMode=Gui.ActiveDocument.getObject(objs[0].Name).DisplayMode
    App.ActiveDocument.recompute()

    App.ActiveDocument.addObject('Part::Feature','Fusion').Shape=App.ActiveDocument.Fusion.Shape
    App.ActiveDocument.ActiveObject.Label=docName
    fused_obj = App.ActiveDocument.ActiveObject

    Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Fusion.ShapeColor
    Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Fusion.LineColor
    Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Fusion.PointColor
    Gui.ActiveDocument.ActiveObject.DiffuseColor=Gui.ActiveDocument.Fusion.DiffuseColor
    App.ActiveDocument.recompute()

    # Remove the part1 part2 objects
    if not keepOriginals:
        for o in objs:
            App.getDocument(docName).removeObject(o.Name)

    # Remove the fusion itself
    App.getDocument(docName).removeObject("Fusion")

    return fused_obj

###################################################################
# FuseObjs_wColors_naming()  maui
#   Function to fuse two objects together.
###################################################################
def FuseObjs_wColors_naming(App, Gui,
                           docName, part1, part2, name, keepOriginals=False):

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
    if not keepOriginals:
        App.getDocument(docName).removeObject(part1)
        App.getDocument(docName).removeObject(part2)
    # Remove the fusion itself
    App.getDocument(docName).removeObject("Fusion")
    ## App.getDocument(docName).removeObject("Fusion001")

    return 0

def RmvSubTree(objs):
    def addsubobjs(obj,toremoveset):
        toremove.add(obj)
        if hasattr(obj,'OutList'):
            for subobj in obj.OutList:
                addsubobjs(subobj,toremoveset)
    import FreeCAD
    toremove=set()
    for obj in objs:
        addsubobjs(obj,toremove)
    checkinlistcomplete =False
    while not checkinlistcomplete:
        for obj in toremove:
            if (obj not in objs) and (frozenset(obj.InList) - toremove):
                toremove.remove(obj)
                break
        else:
            checkinlistcomplete = True
    for obj in toremove:
        try:
            obj.Document.removeObject(obj.Name)
        except:
            pass
###




###################################################################
# CutObjs_wColors()  maui
#   Function to fuse two objects together.
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
    App.activeDocument().Cut.Base = App.activeDocument().getObject(obj1.Name)
    App.activeDocument().Cut.Tool = App.activeDocument().getObject(obj2.Name)
    App.ActiveDocument.recompute()
    cutObj = App.ActiveDocument.ActiveObject  #App.activeDocument().getObject('Cut')
    SimpleCopy_wColors(cutObj)
    cut_obj = App.ActiveDocument.ActiveObject
    FreeCAD.ActiveDocument.removeObject(cutObj.Name)
    App.getDocument(docName).removeObject(part1)
    App.getDocument(docName).removeObject(part2)
    App.ActiveDocument.recompute()
    #RmvSubTree([FreeCAD.ActiveDocument.getObject(cutObj.Name)])
    App.ActiveDocument.ActiveObject.Label=docName

    return 0

###################################################################
# GetListOfObjects()  maui
#   Function to fuse two objects together.
###################################################################
def GetListOfObjects(App, docName):

    # Create list of objects, starting with object names
    objs=[]
    for obj in docName.Objects:
        # do what you want to automate
        objs.append(App.ActiveDocument.getObject(obj.Name))
        #FreeCAD.Console.PrintMessage(obj.Name)
        #FreeCAD.Console.PrintMessage(' objName\r\n')

    return objs

###################################################################
# Color_Objects()  maui
#   Function to color objects.
###################################################################
def Color_Objects(Gui,obj,color):

    #FreeCAD.Console.PrintMessage(obj.Name+'\r\n')
    Gui.ActiveDocument.getObject(obj.Name).ShapeColor = color
    Gui.ActiveDocument.getObject(obj.Name).LineColor = color
    Gui.ActiveDocument.getObject(obj.Name).PointColor = color
    Gui.ActiveDocument.getObject(obj.Name).DiffuseColor = color
    #FreeCAD.Console.PrintMessage(obj.Name)
    #FreeCAD.Console.PrintMessage(' objName\r\n')
    #obj.Label=ModelName

    return 0


###################################################################
# restore_Main_Tools()  maui
#   Function to restore
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
#   Function to z-rotate an object
#
###################################################################
def z_RotateObject(doc, rot):

    # z-Rotate
    objs=GetListOfObjects(FreeCAD, doc)
    FreeCAD.getDocument(doc.Name).getObject(objs[0].Name).Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),rot))

    return 0


###################################################################
# exportSTEP()  maui
#   Function to Export to STEP
#
###################################################################
def exportSTEP(doc,modelName, dir, objectToExport=None):

    ## Export to STEP
    ## Get cwd

    ## outdir=os.path.dirname(os.path.realpath(__file__))+dir
    outdir=dir
    #FreeCAD.Console.PrintMessage('\r\n'+outdir)
    StepFileName=outdir+os.sep+modelName+'.step'
    objs=[]
    if objectToExport is None:
        objs=GetListOfObjects(FreeCAD, doc)
    else:
        objs.append(objectToExport)
    import ImportGui
    #FreeCAD.Console.PrintMessage('\r\n'+StepFileName)
    # FreeCAD.Console.PrintMessage(objs)
    #FreeCAD.Console.PrintMessage('\r\n'+outdir)
    ImportGui.export(objs,StepFileName)
    FreeCAD.Console.PrintMessage(StepFileName + ' exported\n')

    return 0

###################################################################
# exportVRML()  maui
#   Function to Export to VRML
#
###################################################################
def exportVRML(doc,modelName,scale,dir):

    ## Export to VRML scaled 1/2.54
    #VrmlFileName='.//'+doc.Label+'.wrl'
    ## outdir=os.path.dirname(os.path.realpath(__file__))+dir
    outdir=dir
    #FreeCAD.Console.PrintMessage('\r\n'+outdir)
    VrmlFileName=outdir+'/'+modelName+'.wrl'
    StepFileName=outdir+'/'+modelName+'.step'
    objs=[]
    objs=GetListOfObjects(FreeCAD, doc)
    #objs.append(FreeCAD.getDocument(doc.Name).getObject("Fusion001"))
    FreeCAD.ActiveDocument.addObject('Part::Feature','Vrml_model').Shape=objs[0].Shape
    FreeCAD.ActiveDocument.ActiveObject.Label='Vrml_model'
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.getDocument(doc.Name).getObject(objs[0].Name).ShapeColor
    FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.getDocument(doc.Name).getObject(objs[0].Name).LineColor
    FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.getDocument(doc.Name).getObject(objs[0].Name).PointColor
    FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.getDocument(doc.Name).getObject(objs[0].Name).DiffuseColor
    FreeCAD.ActiveDocument.recompute()
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
#   Function to save in Native FreeCAD format the doc
#
###################################################################
def saveFCdoc(App, Gui, doc, modelName,dir, saving = True):

    ## Save to disk in native format
    App.ActiveDocument=None
    Gui.ActiveDocument=None
    App.setActiveDocument(doc.Name)
    App.ActiveDocument=App.getDocument(doc.Name)
    Gui.ActiveDocument=Gui.getDocument(doc.Name)

    ## outdir=os.path.dirname(os.path.realpath(__file__))+dir
    outdir=dir
    #FreeCAD.Console.PrintMessage('\r\n'+outdir)
    FCName=outdir+os.sep+modelName+'.FCStd'
    #FreeCAD.Console.PrintMessage('\r\n'+FCName+'\r\n')
    App.getDocument(doc.Name).saveAs(FCName)
    App.ActiveDocument.recompute()

    App.getDocument(doc.Name).Label = doc.Name
    Gui.SendMsgToActiveView("Save")
    App.getDocument(doc.Name).save()
    try:
        os.remove(outdir+os.sep+modelName+'.FCStd1') #removing backup file
    except Exception as exp:
        FreeCAD.Console.PrintWarning("Error while trying to remove backup file in saveFCdoc:")
        FreeCAD.Console.PrintWarning('{:s}\n'.format(str(exp)))
    if saving == False:
        try:
            os.remove(outdir+os.sep+modelName+'.FCStd') #removing project file
        except Exception as exp:
            FreeCAD.Console.PrintWarning("Error while trying to remove file in saveFCdoc (with save == False):")
            FreeCAD.Console.PrintWarning('{:s}\n'.format(exp))
    else:
        FreeCAD.Console.PrintMessage(outdir+os.sep+modelName+'.FCStd saved\n')
    return 0

###################################################################
# checkRequirements()  maui
#   Function to check FC and CQ minimum versions
#
###################################################################
def checkRequirements(cq):

    #checking requirements
    FreeCAD.Console.PrintMessage("FC Version \r\n")
    FreeCAD.Console.PrintMessage(FreeCAD.Version())
    FC_majorV=str(FreeCAD.Version()[0]).replace(',','.');FC_minorV=str(FreeCAD.Version()[1]).replace(',','.')
    FreeCAD.Console.PrintMessage('FC Version '+FC_majorV+FC_minorV+'\r\n')
    import PySide, sys
    FreeCAD.Console.PrintMessage('QtCore Version '+PySide.QtCore.qVersion()+'\n')
    FreeCAD.Console.PrintMessage('Python Version '+sys.version+'\n') 

    if int(float(FC_majorV)) <= 0:
        if int(float(FC_minorV)) < 15:
            reply = QtGui.QMessageBox.information(None,"Warning! ...","use FreeCAD version >= "+FC_majorV+"."+FC_minorV+"\r\n")

    #check version
    cqv=cq.__version__.split(".")
    #say2(cqv)
    if int(cqv[0])==0 and int(cqv[1])<3:
        msg = "CadQuery Module needs to be at least 0.3.0!\r\n\r\n"
        reply = QtGui.QMessageBox.information(None, "Info ...", msg)
        say("cq needs to be at least 0.3.0")
        raise #todo: create a suitable exception

    if float(cq.__version__[:-2]) < 0.3:
        msg="missing CadQuery 0.3.0 or later Module!\r\n\r\n"
        msg+="https://github.com/jmwright/cadquery-freecad-module/wiki\n"
        msg+="actual CQ version "+cq.__version__
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
        raise #todo: create a suitable exception
    #do a check to test all works:
    try:
        open_CQ_Example(FreeCAD, FreeCADGui)
        close_CQ_Example(FreeCAD, FreeCADGui)
    except: # catch *all* exceptions
        msg="CadQuery 030 didn't open an example file!\r\n\r\n"
        reply = QtGui.QMessageBox.information(None, "Error ...", msg)
        FreeCAD.Console.PrintMessage("CQ 030 doesn't open example file")
        raise #re-raise exception that caused the problem

    return 0

###################################################################
# runGeometryCheck()  maui/poeschlr
#   Do the geometry check.
#
###################################################################
def runGeometryCheck(App, Gui, step_path, log,
        modelName, save_memory=True, stop_on_first_error = True):

    FC_majorV=int(float(str(FreeCAD.Version()[0]).replace(',','.')))
    FC_minorV=int(float(str(FreeCAD.Version()[1]).replace(',','.')))
    try:
        FC_subV=int(float(str(FreeCAD.Version()[2]).replace(',','.').split(" ")[0]))
    except Exception:
        FC_subV = 0

    if FC_majorV == 0 and FC_minorV == 16 and FC_subV < 6712:
        raise FreeCADVersionError('0.16-6712', 'old 0.16 releases have a bug in the step exporter.')

    geometry_error_container = GeometryError()

    ImportGui.open(step_path)
    docu = FreeCAD.ActiveDocument
    docu.Label = modelName
    log.write('\n## Checking {:s}\n'.format(modelName))


    if checkUnion(docu):
        FreeCAD.Console.PrintMessage('step file is correctly Unioned\n')
        log.write('\t- Union check:    [    pass    ]\n')
    else:
        #FreeCAD.Console.PrintError('step file is NOT Unioned\n')
        log.write('\t- Union check:    [    FAIL    ]\n')
        geometry_error_container.append(NotUnionedError(modelName))
        #stop
    if FC_majorV == 0 and FC_minorV >= 17:
        if docu.Objects == 0:
            FreeCAD.Console.PrintError('Step import seems to fail. No objects to check\n')
        for o in docu.Objects:
            if hasattr(o,'Shape'):
                o.Shape.fixTolerance(1e-4)
                chks=checkBOP(o.Shape)
                #print 'chks ',chks
                if chks != True:
                    #msg='shape \''+o.Name+'\' \''+ mk_string(o.Label)+'\' is INVALID!\n'
                    msg = 'shape "{name:s}" "{label:s}" is INVALID\n'.format(name=o.Name, label=o.Label)
                    #FreeCAD.Console.PrintError(msg)
                    #FreeCAD.Console.PrintWarning(chks[0])
                    geometry_error_container.append(BOBError(modelName, o.Name, o.Label, chks[0]))
                    log.write('\t- Geometry check: [    FAIL    ]\n')
                    log.write('\t\t- Effected shape: "{name:s}" "{label:s}"\n'.format(name=o.Name, label=o.Label))
                    #stop
                else:
                    #msg='shape \''+o.Name+'\' \''+ mk_string(o.Label)+'\' is valid\n'
                    msg = 'shape "{name:s}" "{label:s}" is valid\n'.format(name=o.Name, label=o.Label)
                    FreeCAD.Console.PrintMessage(msg)
                    log.write('\t- Geometry check: [    pass    ]\n')
    else:
        log.write('\t- Geometry check: [  skipped   ]\n')
        log.write('\t\t- Geometry check needs FC 0.17+\n')
        raise FreeCADVersionError('0.17', 'Geometry check needs FC 0.17')

    if stop_on_first_error and geometry_error_container.error_encountered:
        raise geometry_error_container

    if save_memory == True:
        saveFCdoc(App, Gui, docu, 'temp', './', False)
        docu = FreeCAD.ActiveDocument
        FreeCAD.closeDocument(docu.Name)

    if geometry_error_container.error_encountered:
        raise geometry_error_container

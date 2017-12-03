#!/usr/bin/python
# -*- coding: utf-8 -*-
#****************************************************************************

import FreeCAD, FreeCADGui
import sys

doc = FreeCAD.ActiveDocument
#FreeCAD.open(u"D:/Temp/res_err.FCStd")
FreeCAD.setActiveDocument(doc.Name)
FreeCAD.ActiveDocument=FreeCAD.getDocument(doc.Name)
FreeCADGui.ActiveDocument=Gui.getDocument(doc.Name)
#App.ActiveDocument.Part__Feature.Shape.check(True)

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
    except:
        return sys.exc_info()[1] #ValueError #sys.exc_info() #False
##

if checkUnion(doc) is True:
    FreeCAD.Console.PrintMessage('step file is correctly Unioned\n')
else:
    FreeCAD.Console.PrintError('step file is NOT Unioned\n')


for o in doc.Objects:
    if hasattr(o,'Shape'):
        chks=checkBOP(o.Shape)
        if chks is not True:
            FreeCAD.Console.PrintError('shape \''+o.Name+'\' \''+mk_string(o.Label)+'\' is INVALID!\n')
            FreeCAD.Console.PrintWarning(chks[0])
        else:
            FreeCAD.Console.PrintMessage('shape \''+o.Name+'\' \''+mk_string(o.Label)+'\' is valid\n')

# end

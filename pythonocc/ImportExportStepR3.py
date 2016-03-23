#!/usr/bin/env python

##Copyright 2009-2014 Jelle Ferina (jelleferinga@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox

from OCC.STEPControl import STEPControl_Writer, STEPControl_AsIs, STEPControl_ManifoldSolidBrep, \
     STEPControl_GeometricCurveSet, STEPControl_ShellBasedSurfaceModel, STEPControl_FacetedBrep,\
     STEPControl_BrepWithVoids, STEPControl_ActorWrite    
from OCC.Interface import Interface_Static_SetCVal
from OCC.IFSelect import IFSelect_RetDone

from OCC.STEPControl import STEPControl_Reader
from OCC.IFSelect import IFSelect_ItemsByEntity
from OCC.Display.SimpleGui import init_display

from OCC.BRepTools import *

step_reader = STEPControl_Reader()

#from __future__ import print_function


from OCC.TCollection import TCollection_ExtendedString

from OCC.TDocStd import Handle_TDocStd_Document
from OCC.XCAFApp import XCAFApp_Application
from OCC.XCAFDoc import (XCAFDoc_DocumentTool_ShapeTool,
                         XCAFDoc_DocumentTool_ColorTool,
                         XCAFDoc_DocumentTool_LayerTool,
                         XCAFDoc_DocumentTool_MaterialTool)
from OCC.STEPCAFControl import STEPCAFControl_Reader
from OCC.IFSelect import IFSelect_RetDone
from OCC.TDF import TDF_LabelSequence

#from OCC.Display.SimpleGui import init_display
from OCC.STEPCAFControl import STEPCAFControl_Writer


status = step_reader.ReadFile('./sg1-c5-214-in.stp')

# creates a basic shape
#box_s = BRepPrimAPI_MakeBox(10, 20, 30).Shape()

if status == IFSelect_RetDone:  # check status
    failsonly = False
    step_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
    step_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)
 
    ok = step_reader.TransferRoot(1)
    _nbs = step_reader.NbShapes()
    aResShape = step_reader.Shape(1)
else:
    print("Error: can't read file.")
    sys.exit(0)

##breptools_Clean(aResShape)
    
# initialize the STEP exporter
step_writer = STEPControl_Writer()
##step_writer = STEPControl_ActorWrite()
## step_writer = STEPCAFControl_Writer()

Interface_Static_SetCVal("write.step.schema", "AP214")

# transfer shapes and write file
#step_writer.Transfer(box_s, STEPControl_AsIs)
#status = step_writer.Write("box.stp")

step_writer.Transfer(aResShape, STEPControl_AsIs)
## step_writer.Transfer(aResShape, STEPControl_GeometricCurveSet)
## step_writer.Transfer(aResShape, STEPControl_ManifoldSolidBrep)
## step_writer.Transfer(aResShape, STEPControl_ShellBasedSurfaceModel)
### step_writer.Transfer(aResShape, STEPControl_FacetedBrep)
### step_writer.Transfer(aResShape, STEPControl_BrepWithVoids)

# -  case STEPControl_AsIs : ModeTrans() = 0; break;
# -  case STEPControl_ManifoldSolidBrep : ModeTrans() = 3; break;
# -  case STEPControl_BrepWithVoids :     ModeTrans() = 5; break;
# -  case STEPControl_FacetedBrep :       ModeTrans() = 1; break;
# -  case STEPControl_FacetedBrepAndBrepWithVoids : ModeTrans() = 6; break;
# -  case STEPControl_ShellBasedSurfaceModel :      ModeTrans() = 2;
# -  case STEPControl_GeometricCurveSet :           ModeTrans() = 4;
# -  case STEPControl_Hybrid : ModeTrans() = 0; break;  // PAS IMPLEMENTE !!
##step_writer.Transfer(aResShape)
status = step_writer.Write("sg1-c5-214-out.stp")

assert(status == IFSelect_RetDone)

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(aResShape, update=True)
start_display()
# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
# This is a
# Dimensions are from Microchips Packaging Specification document:
# DS00000049BY. Body drawing is the same as QFP generator#

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are a FreeCAD & cadquery tools									 *
#* to export generated models in STEP & VRML format.						*
#*																		  *
#* cadquery script for generating QFP/SOIC/SSOP/TSSOP models in STEP AP214  *
#*   Copyright (c) 2015													 *
#* Maurice https://launchpad.net/~easyw									 *
#* All trademarks within this guide belong to their legitimate owners.	  *
#*																		  *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Lesser General Public License (LGPL)	 *
#*   as published by the Free Software Foundation; either version 2 of	  *
#*   the License, or (at your option) any later version.					*
#*   for detail see the LICENCE text file.								  *
#*																		  *
#*   This program is distributed in the hope that it will be useful,		*
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of		 *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the		  *
#*   GNU Library General Public License for more details.				   *
#*																		  *
#*   You should have received a copy of the GNU Library General Public	  *
#*   License along with this program; if not, write to the Free Software	*
#*   Foundation, Inc.,													  *
#*   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA		   *
#*																		  *
#****************************************************************************

__title__ = "make DIP switch 3D models"
__author__ = "Stefan, based on DIP script"
__Comment__ = 'make DIP switch 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.3.3 14/08/2015"

# maui import cadquery as cq
# maui from Helpers import show
from math import tan, radians, sqrt
from collections import namedtuple

import sys, os
import datetime
from datetime import datetime
sys.path.append("../_tools")
import exportPartToVRML as expVRML
import shaderColors


# maui start
import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui
#from Gui.Command import *

	
#import step_license as L
import add_license as Lic


outdir=os.path.dirname(os.path.realpath(__file__)+"/../_3Dmodels")
scriptdir=os.path.dirname(os.path.realpath(__file__))
sys.path.append(outdir)
sys.path.append(scriptdir)
if FreeCAD.GuiUp:
	from PySide import QtCore, QtGui

# Licence information of the generated models.
#################################################################################################
STR_licAuthor = "kicad StepUp"
STR_licEmail = "ksu"
STR_licOrgSys = "kicad StepUp"
STR_licPreProc = "OCC"
STR_licOrg = "FreeCAD"   


#################################################################################################

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

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

#checking requirements
checkRequirements(cq)

try:
	close_CQ_Example(App, Gui)
except: # catch *all* exceptions
	print "CQ 030 doesn't open example file"

destination_dir="/Switch_SMD_packages"
# rotation = 0


CASE_THT_TYPE = 'tht'
CASE_SMD_TYPE = 'smd'
CASE_THTSMD_TYPE = 'thtsmd'
_TYPES = [CASE_THT_TYPE, CASE_SMD_TYPE ]


CORNER_NONE_TYPE = 'none'
CORNER_CHAMFER_TYPE = 'chamfer'
CORNER_FILLET_TYPE = 'fillet'
_CORNER = [CORNER_NONE_TYPE, CORNER_CHAMFER_TYPE, CORNER_FILLET_TYPE]


Params = namedtuple("Params", [
	'L',				# package length
	'W',			   	# package width
	'H',				# package height
	'pitch',			# pin pitch
	'paddist',			# paddist pitch
	'PH',		   		# pin height above package height
	'A1',				# package board seperation
	'npins',			# number of pins
	'modelName',		#modelName
	'rotation',		 	#rotation if required
	'type',			 	# THT and/or SMD
	'corner',			# Chamfer or corner
	'pinshape',			# If pin is L shape
	'padsw',			# pad height
	'padsh',			# pad width
	'body_color_key',	# Body colour
	'pig_color_key',	# Pig colour
	'pin_color_key'		# Pin colour
])

def make_params(L, W, H, pitch, paddist, PH, npins, padsw, pinshape, modelName, rotation, type, corner):
	return Params(
		L = L,				  	# package length
		W = W,				  	# package width
		H = H,				  	# package height
		pitch = pitch,			# pin pitch
		paddist = paddist,		# pad distance
		PH =  PH,			   	# pin height above package height
		A1 = 0.1,				# package board seperation
		npins = npins,		  	# total number of pins
		modelName = modelName,  # Model Name
		rotation = rotation,	# rotation if required
		type = type,			# SMD and/or THT
		corner = corner,		# Chamfer or corner	
		pinshape = pinshape, 	# If pin is L shape
		padsw = padsw,			# pad width
		padsh = 0.1,			# pad height
		body_color_key = "blue body",
		pig_color_key = "white body",
		pin_color_key = "metal grey pins"
	)

all_params = {

#	Name												  Length	Width	 Height		Pitch	pad dist	pig height	pins		pin width	pin type	
	"SW_DIP_x1_W5.08mm_Slide_Copal_CHS-A"	: make_params(5.08,		 2.54,	 2.5,		0.00,	 2.540,		 0.5,	 	 2,			0.76,		0,			'SW_DIP_x1_W5.08mm_Slide_Copal_CHS-A',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x1_W7.62mm_Slide_Copal_CHS-B"	: make_params(5.00,		 2.54,	 2.5,		0.00,	 3.810,		 0.5,	 	 2, 		0.76,		1,			'SW_DIP_x1_W7.62mm_Slide_Copal_CHS-B',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x1_W8.61mm_Slide_LowProfile"	: make_params(5.00,		 4.10,	 1.5,		0.00,	 4.305,		 0.5,	 	 2, 		1.12,		1,			'SW_DIP_x1_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_SPST_EVQPE1"						: make_params(5.00,		 3.50,	 1.5,		0.00,	 0.000,		 0.5,	 	 2, 		1.00,		0,			'SW_SPST_EVQPE1',						 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_SPST_REED_CT05-XXXX-G1"				: make_params(6.40,		 3.50,	2.30,		0.00,	 4.28,		 0.5,	 	 2, 		1.50,		1,			'SW_SPST_REED_CT05-XXXX-G1',			 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_SPST_REED_CT05-XXXX-J1"				: make_params(6.40,		 3.50,	2.30,		0.00,	 6.40,		 0.5,	 	 2, 		1.25,		0,			'SW_SPST_REED_CT05-XXXX-J1',			 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_SPST_REED_CT10-XXXX-G1"				: make_params(11.6,		 2.40,	2.30,		0.00,	 7.56,		 0.5,	 	 2, 		1.50,		1,			'SW_SPST_REED_CT10-XXXX-G1',			 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_SPST_REED_CT10-XXXX-G2"				: make_params(11.6,		 2.40,	2.30,		0.00,	9.210,		 0.5,	 	 2, 		1.50,		1,			'SW_SPST_REED_CT10-XXXX-G2',			 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_SPST_REED_CT10-XXXX-G4"				: make_params(11.6,		 2.40,	2.30,		0.00,	9.220,		 0.5,	 	 2, 		1.50,		1,			'SW_SPST_REED_CT10-XXXX-G4',			 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	
	"SW_DIP_x2_W5.08mm_Slide_Copal_CHS-A"	: make_params(5.40,		 3.81,	 2.5,		1.27,	5.40,		 0.5,	 	 4, 		0.76,		0,			'SW_DIP_x2_W5.08mm_Slide_Copal_CHS-A',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x2_W6.15mm_Slide_Omron_A6H"		: make_params(4.50,		 3.81,	 2.5,		1.27,	3.075,		 0.5,	 	 4, 		0.76,		1,			'SW_DIP_x2_W6.15mm_Slide_Omron_A6H',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x2_W7.62mm_Slide_Copal_CHS-B"	: make_params(5.40,		 3.81,	 2.5,		1.27,	3.810,		 0.5,	 	 4, 		0.75,		1,			'SW_DIP_x2_W7.62mm_Slide_Copal_CHS-B',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x2_W8.61mm_Slide_LowProfile"	: make_params(6.68,		 6.64,	 1.5,		2.54,	4.305,		 0.5,	 	 4, 		1.00,		1,			'SW_DIP_x2_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x3_W8.61mm_Slide_LowProfile"	: make_params(6.68,		 9.18,	 1.5,		2.54,	4.305,		 0.5,	 	 6, 		1.00,		1,			'SW_DIP_x3_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x4_W5.08mm_Slide_Copal_CHS-A"	: make_params(5.40,		 6.35,	 2.5,		1.27,	5.40,		 0.5,	 	 8, 		0.75,		0,			'SW_DIP_x4_W5.08mm_Slide_Copal_CHS-A',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x4_W6.15mm_Slide_Omron_A6H"		: make_params(4.50,		 6.35,	 2.5,		1.27,	3.075,		 0.5,	 	 8, 		0.75,		1,			'SW_DIP_x4_W6.15mm_Slide_Omron_A6H',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x4_W7.62mm_Slide_Copal_CHS-B"	: make_params(5.40,		 6.35,	 2.5,		1.27,	3.81,		 0.5,	 	 8, 		0.75,		1,			'SW_DIP_x4_W7.62mm_Slide_Copal_CHS-B',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x4_W8.61mm_Slide_LowProfile"	: make_params(6.68,		11.72,	 1.5,		2.54,	4.305,		 0.5,	 	 8, 		1.00,		1,			'SW_DIP_x4_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x5_W8.61mm_Slide_LowProfile"	: make_params(6.68,		14.26,	 2.5,		2.54,	4.305,		 0.5,	 	10, 		1.00,		1,			'SW_DIP_x5_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x6_W5.08mm_Slide_Copal_CHS-A"	: make_params(5.40,		 8.89,	 2.5,		1.27,	5.40,		 0.5,	 	12, 		0.75,		0,			'SW_DIP_x6_W5.08mm_Slide_Copal_CHS-A',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x6_W6.15mm_Slide_Omron_A6H"		: make_params(4.50,		 8.89,	 2.5,		1.27,	3.075,		 0.5,	 	12, 		0.75,		1,			'SW_DIP_x6_W6.15mm_Slide_Omron_A6H',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x6_W7.62mm_Slide_Copal_CHS-B"	: make_params(5.40,		 8.89,	 2.5,		1.27,	3.81,		 0.5,	 	12, 		0.75,		1,			'SW_DIP_x6_W7.62mm_Slide_Copal_CHS-B',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x6_W8.61mm_Slide_LowProfile"	: make_params(6.68,		16.80,	 1.5,		2.54,	4.305,		 0.5,	 	12, 		1.00,		1,			'SW_DIP_x6_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x7_W8.61mm_Slide_LowProfile"	: make_params(6.68,		19.34,	 1.5,		2.54,	4.305,		 0.5,	 	14, 		1.00,		1,			'SW_DIP_x7_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x8_W5.08mm_Slide_Copal_CHS-A"	: make_params(5.30,		11.43,	 2.5,		1.27,	6.68,		 0.5,	 	16, 		0.75,		0,			'SW_DIP_x8_W5.08mm_Slide_Copal_CHS-A',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x8_W6.15mm_Slide_Omron_A6H"		: make_params(4.50,		11.43,	 2.5,		1.27,	3.075,		 0.5,	 	16, 		0.75,		1,			'SW_DIP_x8_W6.15mm_Slide_Omron_A6H',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x8_W7.62mm_Slide_Copal_CHS-B"	: make_params(5.40,		11.43,	 2.5,		1.27,	3.81,		 0.5,	 	16, 		0.75,		1,			'SW_DIP_x8_W7.62mm_Slide_Copal_CHS-B',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x8_W8.61mm_Slide_LowProfile"	: make_params(6.68,		21.88,	 1.5,		2.54,	4.305,		 0.5,	 	16, 		1.00,		1,			'SW_DIP_x8_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x9_W8.61mm_Slide_LowProfile"	: make_params(6.68,		24.42,	 1.5,		2.54,	4.305,		 0.5,	 	18, 		1.00,		1,			'SW_DIP_x9_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	
	"SW_DIP_x10_W5.08mm_Slide_Copal_CHS-A"	: make_params(5.30,		13.97,	 2.5,		1.27,	6.68,		 0.5,	 	20, 		0.75,		0,			'SW_DIP_x10_W5.08mm_Slide_Copal_CHS-A',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x10_W6.15mm_Slide_Omron_A6H"	: make_params(4.50,		13.97,	 2.5,		1.27,	3.075,		 0.5,	 	20, 		0.75,		1,			'SW_DIP_x10_W6.15mm_Slide_Omron_A6H',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x10_W7.62mm_Slide_Copal_CHS-B"	: make_params(5.40,		13.97,	 2.5,		1.27,	3.81,		 0.5,	 	20, 		0.75,		1,			'SW_DIP_x10_W7.62mm_Slide_Copal_CHS-B',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),
	"SW_DIP_x10_W8.61mm_Slide_LowProfile"	: make_params(6.68,		26.99,	 1.5,		2.54,	4.305,		 0.5,	 	20, 		1.00,		1,			'SW_DIP_x10_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x11_W8.61mm_Slide_LowProfile"	: make_params(6.68,		29.50,	 1.5,		2.54,	4.305,		 0.5,	 	22, 		1.00,		1,			'SW_DIP_x11_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE),

	"SW_DIP_x12_W8.61mm_Slide_LowProfile"	: make_params(6.68,		32.04,	 1.5,		2.54,	4.305,		 0.5,	 	24, 		0.75,		1,			'SW_DIP_x12_W8.61mm_Slide_LowProfile',	 0, CASE_SMD_TYPE,  CORNER_CHAMFER_TYPE)
}




def make_case(params):

	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	pitch = params.pitch			# pin pitch
	PH = params.PH				  	# pin height above package height
	npins = params.npins			# total number of pins
	rotation = params.rotation		# rotation if required
	corner = params.corner			# Chamfer or corner
	A1 = params.A1					# Body seperation height

	FreeCAD.Console.PrintMessage('make_case\r\n')

	xd = H / 4.0
	tpins = npins / 2
	mvX = L / 2.0
	mvY = W / 2.0
	case=cq.Workplane("XY").workplane(offset=A1).moveTo(-mvX, -mvY).rect(L, W, False).extrude(H)

	if npins < 3:
		xd = L / 4.0
		yd = W / 3.0
		myXD = xd * 2.0
		myYD = yd
		myX = 0 - (xd / 2.0)
		myY = 0 - (yd / 2)
		pighole=cq.Workplane("XY").workplane(offset=A1 + H).moveTo(myX, myY).rect(myXD, myYD, False).extrude(-(H / 4))
		case = case.cut(pighole)
	else:
		xd = L / 4.0
		yd = pitch / 3.0
		
		myX = 0 - (xd / 2.0)
		myY = 0 - ((tpins / 2) * (pitch / 2.0) + (yd / 2.0))
		myXD = xd * 2.0
		myYD = yd
		
		if tpins %2 == 0:
			myY = ((pitch / 2.0) + (((tpins / 2) - 1) * pitch))
		else:
			myY = (((tpins / 2) - 1) * pitch) + pitch
			
		myY = myY - (myYD / 2)
		for i in range(0, tpins):
			pighole=cq.Workplane("XY").workplane(offset=A1 + H).moveTo(myX, myY).rect(myXD, myYD, False).extrude(-(H / 4))
			case = case.cut(pighole)
			myY = myY - pitch
	
	xd = H / 4.0
	if corner == CORNER_CHAMFER_TYPE:
		case = case.faces("<X").edges(">Z").chamfer(xd, xd)
		
	if corner == CORNER_FILLET_TYPE:
		case = case.faces("<X").edges(">Z").fillet(xd)


	if (rotation != 0):
		case = case.rotate((0,0,0), (0,0,1), rotation)

	return (case)



def make_pigs(params):

	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	pitch = params.pitch			# pin pitch
	PH = params.PH				  	# pin height above package height
	npins = params.npins			# total number of pins
	rotation = params.rotation		# rotation if required
	corner = params.corner			# Chamfer or corner
	A1 = params.A1					# Body seperation height

	FreeCAD.Console.PrintMessage('make_pigs\r\n')

	tpins = npins / 2
	xd = L / 4.0
	yd = W / 3.0
	myXD = xd / 2.0
	myYD = yd
	myX = 0 - (xd / 2.0)
	myY = 0 - (yd / 2.0)
	pigs = cq.Workplane("XY").workplane(offset=A1 + H + PH).moveTo(myX, myY).rect(myXD, myYD, False).extrude(-(PH + (H / 4)))

	if npins > 2:
		xd = L / 4.0
		yd = pitch / 3.0
		myX = 0 - (xd / 2.0)
		myXD = xd / 2.0
		myYD = yd
		
		if tpins % 2 == 0:
			myY = ((pitch / 2.0) + (((tpins / 2) - 1) * pitch))
		else:
			myY = (((tpins / 2) - 1) * pitch) + pitch
	
		myY = myY - (myYD / 2)
		pigs=cq.Workplane("XY").workplane(offset=A1 + H + PH).moveTo(myX, myY).rect(myXD, myYD, False).extrude(-(PH + (H / 4)))
		for i in range(0, tpins):
			pig=cq.Workplane("XY").workplane(offset=A1 + H + PH).moveTo(myX, myY).rect(myXD, myYD, False).extrude(-(PH + (H / 4)))
			pigs = pigs.union(pig)
			myY = myY - pitch

	if (rotation != 0):
		pigs = pigs.rotate((0,0,0), (0,0,1), rotation)

	return (pigs)

def make_pins_smd(params):
	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	pitch = params.pitch			# pitch
	paddist = params.paddist		# pad distance
	PH = params.PH				  	# pin height above package height
	npins = params.npins			# total number of pins
	rotation = params.rotation	  	# rotation if required
	corner = params.corner		  	# Chamfer or corner
	A1 = params.A1				  	# Body seperation height
	pinshape = params.pinshape		# If pin is L shape	
	padsh = params.padsh		  	# pads height
	padsw = params.padsw		  	# pads width
	
	FreeCAD.Console.PrintMessage("make_pins_smd, npins: %f\r\n" % npins)

	# pinshape 0 type - just a metallic surface on to the side of the block
	# pinshape 1 type - an S shape leg
	# pinshape 2 type - a leg comming along the board under the block
	
	tpins = npins / 2

	xd = padsw
	yd = padsw
	myXD = xd / 2.0
	myYD = yd
	myX = 0.0 - ((paddist) + (padsh / 2.0))
	myY = 0.0 - (padsw / 2.0)
	
	if pinshape == 0:
		myX = 0.0 - ((L / 2.0) + (padsh / 2.0))

	if pinshape == 1:
		myX = 0.0 - (paddist - (padsw / 2.0))

	if pinshape == 2:
		myX = 0.0 - paddist

	# Dummy creation to create pins and pin1 otside the 'if' scopes
	pins = cq.Workplane("ZY").workplane(offset=-myX - padsw - (padsh / 2.0)).moveTo(0, myY).rect(padsw, padsw, False).extrude(padsh)
	pin1 = cq.Workplane("ZY").workplane(offset=-myX - padsw - (padsh / 2.0)).moveTo(0, myY).rect(padsw, padsw, False).extrude(padsh)

	if pinshape == 0:
		pin1 = cq.Workplane("ZY").workplane(offset=myX).moveTo(0, 0 - (padsw / 2)).rect(padsw, padsw, False).extrude(padsh)
	
	elif pinshape == 1:
		pin1 = cq.Workplane("ZY").workplane(offset=-myX).moveTo(0, myY).rect(padsw, padsw, False).extrude(padsh)
		pint = cq.Workplane("XY").workplane(offset=padsw - padsh).moveTo(myX, myY).rect(-myX, padsw, False).extrude(padsh)
		pin1 = pin1.union(pint)
		pin1 = pin1.faces("<X").edges(">Z").fillet(padsh / 2)
		pint = cq.Workplane("XY").workplane(offset=0).moveTo(myX, myY).rect(-padsw, padsw, False).extrude(padsh)
		pin1 = pin1.union(pint)
		pin1 = pin1.faces("<Z").edges(">X").fillet(padsh / 2)
	
	elif pinshape == 2:
		pin1 = cq.Workplane("XY").workplane(offset=0).moveTo(myX, myY).rect(myX, padsw, False).extrude(padsh)
		
	pin2 = pin1.rotate((0,0,0), (0,0,1), 180)
	pin1 = pin1.union(pin2)
	pins = pin1

	if npins > 2:
		if tpins %2 == 0:
			myY = ((pitch / 2.0) + (((tpins / 2) - 1) * pitch))
		else:
			myY = (((tpins / 2) - 1) * pitch) + pitch
	
		pint = pin1.translate((0, myY, 0))
		pins = pint
		myY = myY - pitch
		
		for i in range(1, tpins):
			pint = pin1.translate((0, myY, 0))
			pins = pins.union(pint)
			myY = myY - pitch

	if (rotation != 0):
		pins = pins.rotate((0,0,0), (0,0,1), rotation)
			
	return (pins)

	
def make_3D_model(models_dir, variant):
				
	LIST_license = ["",]
	modelName = all_params[variant].modelName
		
	CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
	Newdoc = App.newDocument(CheckedmodelName)
	App.setActiveDocument(CheckedmodelName)
	Gui.ActiveDocument=Gui.getDocument(CheckedmodelName)

	case = make_case(all_params[variant])
	pigs = make_pigs(all_params[variant])
	
	if (all_params[variant].type == CASE_THT_TYPE):
		pins = make_pins_tht(all_params[variant])

	if (all_params[variant].type == CASE_SMD_TYPE):
		pins = make_pins_smd(all_params[variant])

	show(case)
	show(pigs)
	show(pins)
	#show(pinmark)
	#stop
	doc = FreeCAD.ActiveDocument
	objs=GetListOfObjects(FreeCAD, doc)

	body_color_key = all_params[variant].body_color_key
	pig_color_key = all_params[variant].pig_color_key
	pin_color_key = all_params[variant].pin_color_key
	
	body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
	pig_color = shaderColors.named_colors[pig_color_key].getDiffuseFloat()
	pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

	Color_Objects(Gui,objs[0],body_color)
	Color_Objects(Gui,objs[1],pig_color)
	Color_Objects(Gui,objs[2],pin_color)

	col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
	col_pig=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
	col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]

	material_substitutions={
		col_body[:-1]:body_color_key,
		col_pig[:-1]:pig_color_key,
		col_pin[:-1]:pin_color_key
	}

	expVRML.say(material_substitutions)
	FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name, objs[2].Name)
	doc.Label = CheckedmodelName

	del objs
	objs=GetListOfObjects(FreeCAD, doc)
	objs[0].Label = CheckedmodelName
	restore_Main_Tools()

	script_dir=os.path.dirname(os.path.realpath(__file__))
	expVRML.say(models_dir)
	out_dir=models_dir+destination_dir
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)

	exportSTEP(doc, modelName, out_dir)
	if LIST_license[0]=="":
		LIST_license=Lic.LIST_int_license
		LIST_license.append("")
	Lic.addLicenseToStep(out_dir+'/', modelName+".step", LIST_license,\
					   STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)

	# scale and export Vrml model
	scale=1/2.54
	#exportVRML(doc,modelName,scale,out_dir)
	del objs
	objs=GetListOfObjects(FreeCAD, doc)
	expVRML.say("######################################################################")
	expVRML.say(objs)
	expVRML.say("######################################################################")
	export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
	export_file_name=out_dir+os.sep+modelName+'.wrl'
	colored_meshes = expVRML.getColoredMesh(Gui, export_objects , scale)
	#expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys)# , LIST_license
	expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, LIST_license)
	#scale=0.3937001
	#exportVRML(doc,modelName,scale,out_dir)
	# Save the doc in Native FC format
	saveFCdoc(App, Gui, doc, modelName,out_dir)
	#display BBox
	Gui.activateWorkbench("PartWorkbench")
	Gui.SendMsgToActiveView("ViewFit")
	Gui.activeDocument().activeView().viewAxometric()
	#FreeCADGui.ActiveDocument.activeObject.BoundingBox = True

	
def run():
	## # get variant names from command line

	return


# when run from command line
if __name__ == "__main__" or __name__ == "main_generator":

	FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

	full_path=os.path.realpath(__file__)
	expVRML.say(full_path)
	scriptdir=os.path.dirname(os.path.realpath(__file__))
	expVRML.say(scriptdir)
	sub_path = full_path.split(scriptdir)
	expVRML.say(sub_path)
	sub_dir_name =full_path.split(os.sep)[-2]
	expVRML.say(sub_dir_name)
	sub_path = full_path.split(sub_dir_name)[0]
	expVRML.say(sub_path)
	models_dir=sub_path+"_3Dmodels"

	
	if len(sys.argv) < 3:
		FreeCAD.Console.PrintMessage('No variant name is given! building SW_DIP_x2_W5.08mm_Slide_Copal_CHS-A\r\n')
		model_to_build='SW_DIP_x2_W5.08mm_Slide_Copal_CHS-A'
	else:
		model_to_build=sys.argv[2]
	
	if model_to_build == "all":
		variants = all_params.keys()
	else:
		variants = [model_to_build]

	for variant in variants:
		FreeCAD.Console.PrintMessage('\r\n' + variant + '\r\n\r\n')
		if not variant in all_params:
			print("Parameters for %s doesn't exist in 'all_params', skipping. " % variant)
			continue

		make_3D_model(models_dir, variant)

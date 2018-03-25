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

destination_dir="/Converter_ACDC"
# rotation = 0


CASE_THT_TYPE = 'tht'
CASE_SMD_TYPE = 'smd'
CASE_THTSMD_TYPE = 'thtsmd'
CASE_THT_N_TYPE = 'tht_n'
_TYPES = [CASE_THT_TYPE, CASE_SMD_TYPE, CASE_THT_N_TYPE ]


CORNER_NONE_TYPE = 'none'
CORNER_CHAMFER_TYPE = 'chamfer'
CORNER_FILLET_TYPE = 'fillet'
_CORNER = [CORNER_NONE_TYPE, CORNER_CHAMFER_TYPE, CORNER_FILLET_TYPE]


Params = namedtuple("Params", [
	'modelName',		#modelName
	'roundbelly',		# If belly of caseing should be round (or flat)
	'L',				# package length
	'W',			   	# package width
	'H',				# package height
	'pinpadsize',		# pin diameter or pad size
	'pinpadh',			# pin length, pad height
	'pintype',			# Casing type
	'rotation',			# Rotation if required
	'pin1corner',		# Left upp corner relationsship to pin 1
	'pin',				# pin pitch
	'A1',				# package board seperation
	'corner',			# If top should be cut
	'show_top',			# If top should be visible or not
	'body_color_key',	# Body colour
	'body_top_color_key',	# Body top colour
	'pin_color_key'		# Pin colour
])


def make_params(modelName, L, W, H, pinpadsize, pinpadh, pintype, rotation, pin1corner, pin):
	return Params(
		modelName = modelName,  		# Model Name
		L = L,				  			# package length
		W = W,				  			# package width
		H = H,				  			# package height
		pinpadsize = pinpadsize,		# pin diameter or pad size
		pinpadh = pinpadh,				# pin length, pad height
		pintype = pintype,				# Casing type
		rotation = rotation,			# rotation if required
		pin1corner = pin1corner,		# Left upp corner relationsship to pin 1
		pin = pin,						# pin/pad cordinates
		A1 = 0.1,						# package board seperation
		roundbelly = 1,					# If belly of caseing should be round (or flat)
		corner = CORNER_NONE_TYPE,		# Chamfer or corner	
		show_top = 0,					# If top should be visible or not
		body_color_key = "black body",
		body_top_color_key = "black body",
		pin_color_key = "metal grey pins"
	)

def make_params_black_body(modelName, roundbelly, L, W, H, pinpadsize, pinpadh, pin1corner, pin):
	return Params(
		modelName = modelName,  		# Model Name
		roundbelly = roundbelly,  		# If belly of caseing should be round (or flat)
		L = L,				  			# package length
		W = W,				  			# package width
		H = H,				  			# package height
		pinpadsize = pinpadsize,		# pin diameter or pad size
		pinpadh = pinpadh,				# pin length, pad height
		pintype = CASE_THT_TYPE,			# Casing type
		pin1corner = pin1corner,		# Left upp corner relationsship to pin 1
		pin = pin,						# pin/pad cordinates
		rotation = 0,					# rotation if required
		A1 = 0.1,						# package board seperation
		corner = CORNER_NONE_TYPE,		# Chamfer or corner	
		show_top = 0,					# If top should be visible or not
		body_color_key = "black body",
		body_top_color_key = "black body",
		pin_color_key = "metal grey pins"
	)

def make_params_grey_body(modelName, roundbelly, L, W, H, pinpadsize, pinpadh, pin1corner, pin):
	return Params(
		modelName = modelName,  		# Model Name
		roundbelly = roundbelly,  		# If belly of caseing should be round (or flat)
		L = L,				  			# package length
		W = W,				  			# package width
		H = H,				  			# package height
		pinpadsize = pinpadsize,		# pin diameter or pad size
		pinpadh = pinpadh,				# pin length, pad height
		pintype = CASE_THT_TYPE,		# Casing type
		pin1corner = pin1corner,		# Left upp corner relationsship to pin 1
		pin = pin,						# pin/pad cordinates
		rotation = 0,					# rotation if required
		A1 = 0.1,						# package board seperation
		corner = CORNER_NONE_TYPE,		# Chamfer or corner	
		show_top = 0,					# If top should be visible or not
		body_color_key = "black body",
		body_top_color_key = "red body",
		pin_color_key = "metal grey pins"
	)


def make_params_orange_body(modelName, L, W, H, pinpadsize, pinpadh, pin1corner, pin):
	return Params(
		modelName = modelName,  		# Model Name
		L = L,				  			# package length
		W = W,				  			# package width
		H = H,				  			# package height
		pinpadsize = pinpadsize,		# pin diameter or pad size
		pinpadh = pinpadh,				# pin length, pad height
		pin1corner = pin1corner,		# Left upp corner relationsship to pin 1
		pin = pin,						# pin/pad cordinates
		pintype = CASE_THT_TYPE,		# Casing type
		rotation = 0,					# rotation if required
		A1 = 0.1,						# package board seperation
		roundbelly = 1,				# If belly of caseing should be round (or flat)
		corner = CORNER_NONE_TYPE,		# Chamfer or corner	
		show_top = 0,					# If top should be visible or not
		body_color_key = "orange body",
		body_top_color_key = "black body",
		pin_color_key = "metal grey pins"
	)


def make_params_silver_body_red_top(modelName, roundbelly, L, W, H, pinpadsize, pinpadh, pin1corner, pin):
	return Params(
		modelName = modelName,  		# Model Name
		roundbelly = roundbelly,  		# If belly of caseing should be round (or flat)
		L = L,				  			# package length
		W = W,				  			# package width
		H = H,				  			# package height
		pinpadsize = pinpadsize,		# pin diameter or pad size
		pinpadh = pinpadh,				# pin length, pad height
		pin1corner = pin1corner,		# Left upp corner relationsship to pin 1
		pin = pin,						# pin/pad cordinates
		pintype = CASE_THT_TYPE,		# Casing type
		rotation = 0,					# rotation if required
		A1 = 0.1,						# package board seperation
		corner = CORNER_NONE_TYPE,		# Chamfer or corner	
		show_top = 1,					# If top should be visible or not
		body_color_key = "metal grey pins",
		body_top_color_key = "red body",
		pin_color_key = "metal grey pins"
	)


def make_params_red_body(modelName, roundbelly, L, W, H, pinpadsize, pinpadh, pin1corner, pin):
	return Params(
		modelName = modelName,  		# Model Name
		roundbelly = roundbelly,  		# If belly of caseing should be round (or flat)
		L = L,				  			# package length
		W = W,				  			# package width
		H = H,				  			# package height
		pinpadsize = pinpadsize,		# pin diameter or pad size
		pinpadh = pinpadh,				# pin length, pad height
		pintype = CASE_THT_TYPE,			# Casing type
		pin1corner = pin1corner,		# Left upp corner relationsship to pin 1
		pin = pin,						# pin/pad cordinates
		rotation = 0,					# rotation if required
		A1 = 0.1,						# package board seperation
		corner = CORNER_NONE_TYPE,		# Chamfer or corner	
		show_top = 0,					# If top should be visible or not
		body_color_key = "red body",
		body_top_color_key = "red body",
		pin_color_key = "metal grey pins"
	)


def make_params_black_body_red_top(modelName, roundbelly, L, W, H, pinpadsize, pinpadh, pin1corner, pin):
	return Params(
		modelName = modelName,  		# Model Name
		roundbelly = roundbelly,  		# If belly of caseing should be round (or flat)
		L = L,				  			# package length
		W = W,				  			# package width
		H = H,				  			# package height
		pinpadsize = pinpadsize,		# pin diameter or pad size
		pinpadh = pinpadh,				# pin length, pad height
		pintype = CASE_THT_TYPE,			# Casing type
		pin1corner = pin1corner,		# Left upp corner relationsship to pin 1
		pin = pin,						# pin/pad cordinates
		rotation = 0,					# rotation if required
		A1 = 0.1,						# package board seperation
		corner = CORNER_NONE_TYPE,		# Chamfer or corner	
		show_top = 1,					# If top should be visible or not
		body_color_key = "black body",
		body_top_color_key = "red body",
		pin_color_key = "metal grey pins"
	)
	
	

all_params = {

#
# NOTE NOTE ALL cordinates are in kiCAd foot print cordinates, that is, a reversed Y axis
# so the easiest way is to contruct the foot print first and then add the 3D model here
#
#

#	Name												  												Length		Width	 Height		Pin size 	Pin height	pin1corner			pin
	"Converter_ACDC_Hahn_HS-400xx_THT"	: make_params_black_body('Converter_ACDC_Hahn_HS-400xx_THT',1,	32.80,		27.80,	 25.8,		 1.0,		4.0,		(-06.40,  -3.90),	((00.00, 00.00), (20.00, 00.00), (15.00, 20.00), (05.00, 20.00))	),

	"Converter_ACDC_MeanWell_IRM-02-xx_THT"	: 
	make_params_black_body('Converter_ACDC_MeanWell_IRM-02-xx_THT',									1,	33.7,		22.20,	 15.0,		 0.6,		6.0,		(-02.85,  -3.50),	((00.00, 00.00), (00.00, 15.20), (28.00, 00.00), (28.00, 07.60))	),

	"Converter_ACDC_MeanWell_IRM-02-xx_SMD"	: 
	make_params('Converter_ACDC_MeanWell_IRM-02-xx_SMD',				24.0,		 37.0,	 16.0,		 1.0,		0.4,	CASE_SMD_TYPE,		  000.0,		( 00.00,  00.00),	(
	(-13.200, -15.24), (-13.200, -10.16), (-13.200, -05.08), (-13.200,  7.62), (-13.200,  10.16), (-13.200,  12.70), (-13.200,  15.24), 
	( 13.200, -15.24), ( 13.200, -10.16), ( 13.200, -05.08), ( 13.200,  7.62), ( 13.200,  10.16), ( 13.200,  12.70), ( 13.200,  15.24)
	)	),
	
	"Converter_ACDC_MeanWell_IRM-03-xx_THT"	: 
	make_params_black_body('Converter_ACDC_MeanWell_IRM-03-xx_THT',									1,	37.00,		24.00,	 15.0,		 0.6,		3.50,		(-03.26,  -3.11),	((00.00, 00.00), (05.08, 00.00), (30.48, 00.00), (30.48, 17.18), (25.40, 17.18))	),
	
	"Converter_ACDC_MeanWell_IRM-03-xx_SMD"	: 
	
	make_params('Converter_ACDC_MeanWell_IRM-03-xx_SMD',												24.0,		 37.0,	 16.0,		 1.0,		0.4,	CASE_SMD_TYPE,		  000.0,		( 00.00,  00.00),	(
	(-14.45, -15.24), (-14.45, -10.16), (-14.45, -05.08), (-14.45,  7.62), (-14.45,  10.16), (-14.450,  12.70), (-14.45,  15.24), 
	( 14.45, -15.24), ( 14.45, -10.16), ( 14.45, -05.08), ( 14.45,  7.62), ( 14.45,  10.16), (  14.45,  12.70), ( 14.45,  15.24)
	)	),

	"Converter_ACDC_MeanWell_IRM-20-xx_THT"	: 
	make_params_black_body('Converter_ACDC_MeanWell_IRM-20-xx_THT',		1,	52.4,		27.20,	 24.0,		 1.04,		3.5,		(-02.85,  -3.50),	((00.00, 00.00), (00.00, 20.80), (45.00, 20.80), (45.00, 12.80))	),
	
	"Converter_ACDC_Vigortronix_VTX-214-010-xxx_THT"		: 
	make_params_orange_body('Converter_ACDC_Vigortronix_VTX-214-010-xxx_THT',	36.00,		 56.00,	 25.50,		 1.00,		3.0,		(-12.00, -04.00),	((00.00, 00.00), (12.00, 00.00), (00.00, 48.00), (05.00,   48.00) )	),
	
	"Converter_ACDC_Vigortronix_VTX-214-015-1xx_THT"		: 
	make_params_orange_body('Converter_ACDC_Vigortronix_VTX-214-015-1xx_THT',	55.00,		 45.00,	 24.00,		 1.00,		5.0,		(-04.00, -04.00),	((00.00, 00.00), (00.00, 17.50), (00.00, 35.00), (47.00,   27.50), (47.00,   07.50) )	),

	"Converter_ACDC_TRACO_TMLM-04_THT"	: make_params_black_body_red_top('Converter_ACDC_TRACO_TMLM-04_THT',	0,	36.50,		27.00,	 17.10,		 0.50,		4.0,		(-03.75,  -3.00),	(
	(00.00, 00.00), (21.50, 00.00), (25.25, 00.00), (29.00, 00.00),
	(29.00, 21.00), (21.50, 21.00), (00.00, 21.00)
	)	),

	"Converter_ACDC_TRACO_TMLM-05_THT"		: make_params_black_body_red_top('Converter_ACDC_TRACO_TMLM-05_THT',		0, 	50.08,		25.40,	 15.16,		 1.04,		8.0,		(-02.54, -12.26),	((00.00, 00.00), (00.00, 10.16), (45.72, 10.16), (45.72,  -10.16))	),
	"Converter_ACDC_TRACO_TMLM-10-20_THT"	: make_params_black_body_red_top('Converter_ACDC_TRACO_TMLM-10-20_THT',		0,	52.40,		27.20,	 23.50,		 1.00,		8.0,		(-02.54, -12.26),	((00.00, 00.00), (00.00, 10.16), (45.72, 10.16), (45.72,  -10.16) )	),

}


def make_case(params):

	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	A1 = params.A1					# Body seperation height
	rotation = params.rotation		# rotation if required
	pin1corner = params.pin1corner 	# Left upp corner relationsship to pin 1
	pin = params.pin				# pin/pad cordinates
	roundbelly = params.roundbelly	# If belly of caseing should be round (or flat)
	pintype = params.pintype		# pin type , like SMD or THT
	
	FreeCAD.Console.PrintMessage('make_case\r\n')

	ff = W / 20.0;
	
	if ff > 1.0:
		ff = 1.0

	mvX = 0
	mvY = 0
	# Dummy
	case=cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0).rect(1, 1, False).extrude(H)
	
	
	if (pintype == CASE_SMD_TYPE):
		mvX = 0 - (L / 2.0)
		mvY = 0 - (W / 2.0)
		case=cq.Workplane("XY").workplane(offset=A1).moveTo(mvX, mvY).rect(L, W, False).extrude(H)
	elif (pintype == CASE_THT_TYPE) or (pintype == CASE_THT_N_TYPE):
		p = pin[0]
		mvX = p[0] + pin1corner[0]
		mvY = p[1] - pin1corner[1]
		case=cq.Workplane("XY").workplane(offset=A1).moveTo(mvX, mvY).rect(L, -W, False).extrude(H)
	
	case = case.faces("<X").edges("<Y").fillet(ff)
	case = case.faces("<X").edges(">Y").fillet(ff)
	case = case.faces(">X").edges("<Y").fillet(ff)
	case = case.faces(">X").edges(">Y").fillet(ff)
	case = case.faces(">Y").edges(">Z").fillet(ff / 2.0)
	
	if roundbelly == 1:
		# Belly is rounded
		case = case.faces(">Y").edges("<Z").fillet(ff / 2.0)
		
	


	if (rotation != 0):
		case = case.rotate((0,0,0), (0,0,1), rotation)

	return (case)


def make_case_top(params):

	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	A1 = params.A1					# Body seperation height
	rotation = params.rotation		# rotation if required
	pin1corner = params.pin1corner 	# Left upp corner relationsship to pin 1
	pin = params.pin				# pin/pad cordinates
	show_top = params.show_top		# If top should be visible or not
	pintype = params.pintype		# pin type , like SMD or THT

	FreeCAD.Console.PrintMessage('make_case_top\r\n')

	mvX = 0
	mvY = 0
	# Dummy
	casetop=cq.Workplane("XY").workplane(offset=A1 + H).moveTo(0, 0).rect(1, 1, False).extrude(0.8)
	

	ff = W / 20.0;
	if ff > 1.0:
		ff = 1.0
	
	Ldt = ff
	Wdt = ff
	
	L1 = L - (2.0 * Ldt)
	W1 = W - (2.0 * Wdt)
	
	if show_top == 1:
		tty = A1 + H - 0.1

		if (pintype == CASE_SMD_TYPE):
			mvX = (0 - (L1 / 2.0)) + ((L - L1) / 2.0)
			mvY = (0 - (W1 / 2.0)) - ((W - W1) / 2.0)
			casetop=cq.Workplane("XY").workplane(offset=tty).moveTo(mvX, mvY).rect(L1, W1, False).extrude(0.2)
		elif (pintype == CASE_THT_TYPE):
			p = pin[0]
			mvX = (p[0] + pin1corner[0]) + ((L - L1) / 2.0)
			mvY = (p[1] - pin1corner[1]) - ((W - W1) / 2.0)
			casetop=cq.Workplane("XY").workplane(offset=tty).moveTo(mvX, mvY).rect(L1, -W1, False).extrude(0.2)

		casetop = casetop.faces("<X").edges("<Y").fillet(ff)
		casetop = casetop.faces("<X").edges(">Y").fillet(ff)
		casetop = casetop.faces(">X").edges("<Y").fillet(ff)
		casetop = casetop.faces(">X").edges(">Y").fillet(ff)
	else:
		# If it is not used, just hide it inside the body
		if (pintype == CASE_SMD_TYPE):
			mvX = 0
			mvY = 0
			casetop=cq.Workplane("XY").workplane(offset=A1 + (H / 4.0)).moveTo(mvX, mvY).rect(0.1, 0.1, False).extrude(0.1)
		else:
			p = pin[0]
			mvX = (p[0] + pin1corner[0]) + (L / 2.0)
			mvY = (p[1] - pin1corner[1]) - (W / 2.0)
			casetop=cq.Workplane("XY").workplane(offset=A1 + (H / 4.0)).moveTo(mvX, mvY).rect(0.1, 0.1, False).extrude(0.1)
			

	if (rotation != 0):
		casetop = casetop.rotate((0,0,0), (0,0,1), rotation)

	return (casetop)


def make_pins_tht(params):

	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	A1 = params.A1					# Body seperation height
	pinpadsize = params.pinpadsize	# pin diameter or pad size
	pinpadh = params.pinpadh		# pin length, pad height
	pintype = params.pintype		# Casing type
	rotation = params.rotation		# rotation if required
	pin = params.pin				# pin/pad cordinates

	FreeCAD.Console.PrintMessage('make_pins_tht\r\n')

	p = pin[0]
	pins=cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + 0.1))
	pins = pins.faces("<Z").fillet(pinpadsize / 5.0)

	for i in range(1, len(pin)):
		p = pin[i]
		pint=cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + 0.1))
		pint = pint.faces("<Z").fillet(pinpadsize / 5.0)
		pins = pins.union(pint)
 

	if (rotation != 0):
		pins = pins.rotate((0,0,0), (0,0,1), rotation)

	return (pins)


def make_pins_tht_n(params):

	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	A1 = params.A1					# Body seperation height
	pinpadsize = params.pinpadsize	# pin diameter or pad size
	pinpadh = params.pinpadh		# pin length, pad height
	pintype = params.pintype		# Casing type
	rotation = params.rotation		# rotation if required
	pin = params.pin				# pin/pad cordinates

	FreeCAD.Console.PrintMessage('make_pins_tht_n\r\n')

	p = pin[0]
	pins=cq.Workplane("XY").workplane(offset=A1 + 2.0).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + 2.0))
	pins = pins.faces("<Z").fillet(pinpadsize / 5.0)

	pint=cq.Workplane("XZ").workplane(offset= 0 -p[1]).moveTo(p[0], 2.0).circle(pinpadsize / 2.0, False).extrude( 0 - (W / 2.0))
	pins = pins.union(pint)

	for i in range(1, len(pin)):
		p = pin[i]
		pint=cq.Workplane("XY").workplane(offset=A1 + 2.0).moveTo(p[0], -p[1]).circle(pinpadsize / 2.0, False).extrude(0 - (pinpadh + 2.0))
		pint = pint.faces("<Z").fillet(pinpadsize / 5.0)
		pins = pins.union(pint)
		pint=cq.Workplane("XZ").workplane(offset= 0 -p[1]).moveTo(p[0], 2.0).circle(pinpadsize / 2.0, False).extrude( 0 - (W / 2.0))
		pins = pins.union(pint)
 

	if (rotation != 0):
		pins = pins.rotate((0,0,0), (0,0,1), rotation)

	return (pins)


def make_pins_smd(params):

	L = params.L					# package length
	W = params.W					# package width
	H = params.H					# package height
	A1 = params.A1					# Body seperation height
	pinpadsize = params.pinpadsize	# pin diameter or pad size
	pinpadh = params.pinpadh		# pin length, pad height
	pintype = params.pintype		# Casing type
	rotation = params.rotation		# rotation if required
	pin = params.pin				# pin/pad cordinates

	FreeCAD.Console.PrintMessage('make_pins_smd\r\n')

	#
	# Dummy
	#
	pins=cq.Workplane("XY").workplane(offset=0).moveTo(0, 0).rect(0.1, 0.1).extrude(0.1)
	#

	for i in range(0, len(pin)):
		p = pin[i]
		myX1 = p[0] - pinpadsize
		myY1 = -p[1]
		xD = myX1
		yD = pinpadsize
		if p[0] < 0 and (p[1] > (0 - (W / 2.0)) and p[1] < ((W / 2.0))):
			# Left side
			if p[0] < (0 - (L / 2.0)):
				# Normal pad
				myX1 = p[0] / 2.0
				myY1 = -p[1]
				xD = p[0]
				yD = pinpadsize
				pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
			else:
				# pad cordinate is inside the body
				myZ1 = pinpadsize / 2.0
				myY1 = -p[1]
				xD = pinpadsize
				yD = pinpadsize
				pint=cq.Workplane("ZY").workplane(offset=(L / 2.0) - (pinpadh / 2.0)).moveTo(myZ1, myY1).rect(xD, yD).extrude(pinpadh)
			
		#
		elif p[0] >= 0 and (p[1] > (0 - (W / 2.0)) and p[1] < ((W / 2.0))):
			# Right side
			if p[0] > (L / 2.0):
				# Normal pad
				myX1 = p[0] / 2.0
				xD = -p[0]
				yD = pinpadsize
				pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
			else:
				# pad cordinate is inside the body
				myZ1 = pinpadsize / 2.0
				myY1 = -p[1]
				xD = pinpadsize
				yD = pinpadsize
				pint=cq.Workplane("ZY").workplane(offset=0 - ((L / 2.0) + (pinpadh / 2.0))).moveTo(myZ1, myY1).rect(xD, yD).extrude(pinpadh)
		elif p[1] < 0:
			# top pad
			if p[1] < (W / 2.0):
				myX1 = p[0] - (pinpadsize / 2.0)
				myY1 = 0 - (p[1] / 2.0)
				yD = 0 - p[1]
				xD = pinpadsize
				pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
			else:
				# pad cordinate is inside the body
				myZ1 = pinpadsize / 2.0
				yD = pinpadsize
				xD = pinpadsize
				myX1 = p[0] - (pinpadsize / 2.0)
				pint=cq.Workplane("ZX").workplane(offset=((W / 2.0) - (pinpadh / 2.0))).moveTo(myZ1, myX1).rect(xD, yD).extrude(pinpadh)
		else:
			# bottom pad
			if p[1] > (W / 2.0):
				myX1 = p[0] - (pinpadsize / 2.0)
				myY1 = 0 - (p[1] / 2.0)
				yD = 0 - p[1]
				xD = pinpadsize
				pint=cq.Workplane("XY").workplane(offset=0).moveTo(myX1, myY1).rect(xD, yD).extrude(pinpadh)
			else:
				# pad cordinate is inside the body
				myX1 =  p[0] - (pinpadsize / 2.0)
				myZ1 = pinpadsize / 2.0
				yD = pinpadsize
				xD = pinpadsize
				pint=cq.Workplane("ZX").workplane(offset=0 -((W / 2.0) + (pinpadh / 2.0))).moveTo(myZ1, myX1).rect(xD, yD).extrude(pinpadh)

		if i == 0:
			pins = pint
		else:
			pins = pins.union(pint)

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
	casetop = make_case_top(all_params[variant])
	
	if (all_params[variant].pintype == CASE_THT_TYPE):
		pins = make_pins_tht(all_params[variant])
	
	if (all_params[variant].pintype == CASE_THT_N_TYPE):
		pins = make_pins_tht_n(all_params[variant])

	if (all_params[variant].pintype == CASE_SMD_TYPE):
		pins = make_pins_smd(all_params[variant])

	show(case)
	show(casetop)
	show(pins)
	#show(pinmark)
	#stop
	doc = FreeCAD.ActiveDocument
	objs=GetListOfObjects(FreeCAD, doc)

	body_color_key = all_params[variant].body_color_key
	body_top_color_key = all_params[variant].body_top_color_key
	pin_color_key = all_params[variant].pin_color_key
	
	
	body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
	body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
	pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

	Color_Objects(Gui,objs[0],body_color)
	Color_Objects(Gui,objs[1],body_top_color)
	Color_Objects(Gui,objs[2],pin_color)

	col_body=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
	col_body_top=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
	col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]

	material_substitutions={
		col_body[:-1]:body_color_key,
		col_body_top[:-1]:body_top_color_key,
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

#import step_license as L
import add_license as Lic

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
		FreeCAD.Console.PrintMessage('No variant name is given! building ACDC-Converter_Hahn-HS-400XX\r\n')
		model_to_build='ACDC-Converter_Hahn-HS-400XX'
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

# -*- coding: utf8 -*-
#!/usr/bin/python
  
## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are a FreeCAD & cadquery tools                                     *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating DIP socket models in STEP AP214           *
#*   Copyright (c) 2017                                                     *
#* Terje Io https://github.com/terjeio                                      *
#* All trademarks within this guide belong to their legitimate owners.      *
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

__title__ = "pin socket strip 3D models"
__author__ = "maurice, hyOzd, Stefan, Terje"
__Comment__ = 'make make pin socket strip 3D models exported to STEP and VRML'

___ver___ = "1.0.0 23/11/2017"

import sys, os

script_dir  = os.path.dirname(os.path.realpath(__file__))
scripts_root = script_dir.split(script_dir.split(os.sep)[-1])[0]

sys.path.append(script_dir)
sys.path.append(scripts_root + os.sep + "_tools")

from cq_model_generator import All, ModelGenerator

import parameters
reload(parameters)

import cq_socket_strips
reload(cq_socket_strips)

family = All # set to All to generate all series

series = [
 cq_socket_strips.socket_strip,
 cq_socket_strips.angled_socket_strip,
 cq_socket_strips.smd_socket_strip
]

options = sys.argv[2:] if len(sys.argv) >= 3 else []
#options = [["list"]]

gen = ModelGenerator(scripts_root, script_dir, saveToKicad=False)
#gen.kicadStepUptools = False
gen.footprints_dir = "\\\MEDIA\MyStuff\Electronics\KiCad\New\genmod"
gen.setLicense(ModelGenerator.alt_license)
gen.makeModels(options, series, family, parameters.params())

### EOF ###

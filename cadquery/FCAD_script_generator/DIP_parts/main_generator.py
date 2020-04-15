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
#* Copyright (c) 2017 Terje Io https://github.com/terjeio                   *
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

__title__ = "make assorted DIP part 3D models"
__author__ = "maurice, hyOzd, Stefan, Terje"
__Comment__ = 'make make assorted DIP part 3D models exported to STEP and VRML'

___ver___ = "1.0.0 27/11/2017"

import sys, os

script_dir  = os.path.dirname(os.path.realpath(__file__))
scripts_root = script_dir.split(script_dir.split(os.sep)[-1])[0]

sys.path.append(script_dir)
sys.path.append(scripts_root + "/_tools")

from cq_model_generator import All, ModelGenerator

import cq_parameters
reload(cq_parameters)

import cq_model_socket_turned_pin
import cq_model_pin_switch
import cq_model_piano_switch
import cq_model_smd_switch
import cq_model_smd_switch_copal
import cq_model_smd_switch_omron
import cq_model_smd_switch_kingtek
reload(cq_model_socket_turned_pin)
reload(cq_model_pin_switch)
reload(cq_model_piano_switch)
reload(cq_model_smd_switch)
reload(cq_model_smd_switch_copal)
reload(cq_model_smd_switch_omron)
reload(cq_model_smd_switch_kingtek)

series = [
 cq_model_socket_turned_pin.dip_socket_turned_pin,
 cq_model_pin_switch.dip_switch,
 cq_model_pin_switch.dip_switch_low_profile,
 cq_model_piano_switch.dip_switch_piano,
 cq_model_piano_switch.dip_switch_piano_cts,
 cq_model_smd_switch.dip_smd_switch,
 cq_model_smd_switch.dip_smd_switch_lowprofile,
 cq_model_smd_switch.dip_smd_switch_lowprofile_jpin,
 cq_model_smd_switch_copal.dip_switch_copal_CHS_A,
 cq_model_smd_switch_copal.dip_switch_copal_CHS_B,
 cq_model_smd_switch_copal.dip_switch_copal_CVS,
 cq_model_smd_switch_omron.dip_switch_omron_a6h,
 cq_model_smd_switch_omron.dip_switch_omron_a6s,
 cq_model_smd_switch_kingtek.dip_switch_kingtek_dshp04tj,
 cq_model_smd_switch_kingtek.dip_switch_kingtek_dshp06ts,
]

family = All # set to All generate all series

options = sys.argv[2:] if len(sys.argv) >= 3 else []
#options = [["list"]]

gen = ModelGenerator(scripts_root, script_dir, saveToKicad=False)
#gen.kicadStepUptools = False
gen.setLicense(ModelGenerator.alt_license)
gen.makeModels(options, series, family, cq_parameters.params())

### EOF ###

# -*- coding: utf8 -*-
#!/usr/bin/python

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#
# This is derived from a cadquery script for generating QFP models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## requirements
## modified cadquery libs from
##   https://github.com/hyOzd/cadquery
## to substitute to cadquery lib in
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad make_qfp_export_fc.py modelName
## e.g. c:\freecad\bin\freecad make_qfp_export_fc.py AKA
## e.g. c:\freecad\bin\freecad make_qfp_export_fc.py all


## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* This are a FreeCAD & cadquery tools                                      *
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
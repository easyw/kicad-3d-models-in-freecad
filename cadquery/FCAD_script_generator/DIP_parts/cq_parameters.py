# -*- coding: utf8 -*-
#!/usr/bin/python
#

#****************************************************************************
#*                                                                          *
#* class for generating generic parameters for DIP parts                    *
#*                                                                          *
#* This is part of FreeCAD & cadquery tools                                 *
#* to export generated models in STEP & VRML format.                        *
#*   Copyright (c) 2017                                                     *
#* Terje Io https://github.com/terjeio                                      *
#*                                                                          *
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

from collections import namedtuple
from cq_base_parameters import PartParametersBase, CaseType

class params (PartParametersBase):

    Params = namedtuple("Params", [
        'pin_rows_distance', # distance between pin rows
        'num_pins',          # number of pins
        'type'               # THT and/or SMD
    ])

    Model = namedtuple("Model", [
        'variant',      # generic model name
        'params',       # parameters
        'model'         # model creator class
    ])


    def __init__(self):
        self.base_params = {
            "DIP-4"                 : self.make_params(7.62,    4, CaseType.THT),
            "DIP-4_Wide"            : self.make_params(10.16,   4, CaseType.THT),
            "DIP-6"                 : self.make_params(7.62,    6, CaseType.THT),
            "DIP-6_Wide"            : self.make_params(10.16,   6, CaseType.THT),
            "DIP-8"                 : self.make_params(7.62,    8, CaseType.THT),
            "DIP-8_Wide"            : self.make_params(10.16,   8, CaseType.THT),
            "DIP-10"                : self.make_params(7.62,   10, CaseType.THT),
            "DIP-12"                : self.make_params(7.62,   12, CaseType.THT),
            "DIP-14"                : self.make_params(7.62,   14, CaseType.THT),
            "DIP-16"                : self.make_params(7.62,   16, CaseType.THT),
            "DIP-18"                : self.make_params(7.62,   18, CaseType.THT),
            "DIP-20"                : self.make_params(7.62,   20, CaseType.THT),
            "DIP-22_Narrow"         : self.make_params(7.62,   22, CaseType.THT),
            "DIP-22"                : self.make_params(10.16,  22, CaseType.THT),
            "DIP-24_Narrow"         : self.make_params(7.62,   24, CaseType.THT),
            "DIP-24"                : self.make_params(10.16,  24, CaseType.THT),
            "DIP-24_Wide"           : self.make_params(15.24,  24, CaseType.THT),
            "DIP-28_Narrow"         : self.make_params(7.62,   28, CaseType.THT),
            "DIP-28"                : self.make_params(15.24,  28, CaseType.THT),
            "DIP-32_Narrow"         : self.make_params(7.62,   32, CaseType.THT),
            "DIP-32"                : self.make_params(15.24,  32, CaseType.THT),
            "DIP-40"                : self.make_params(15.24,  40, CaseType.THT),
            "DIP-48"                : self.make_params(15.24,  48, CaseType.THT),
            "DIP-64"                : self.make_params(15.24,  64, CaseType.THT),

            "DIP-2_SMD"             : self.make_params(7.62,    2, CaseType.SMD),
            "DIP-4_SMD"             : self.make_params(7.62,    4, CaseType.SMD),
            "DIP-4_SMD_Wide"        : self.make_params(10.16,   4, CaseType.SMD),
            "DIP-6_SMD"             : self.make_params(7.62,    6, CaseType.SMD),
            "DIP-6_SMD_Wide"        : self.make_params(10.16,   6, CaseType.SMD),
            "DIP-8_SMD"             : self.make_params(7.62,    8, CaseType.SMD),
            "DIP-8_SMD_Wide"        : self.make_params(10.16,   8, CaseType.SMD),
            "DIP-10_SMD"            : self.make_params(7.62,   10, CaseType.SMD),
            "DIP-12_SMD"            : self.make_params(7.62,   12, CaseType.SMD),
            "DIP-14_SMD"            : self.make_params(7.62,   14, CaseType.SMD),
            "DIP-16_SMD"            : self.make_params(7.62,   16, CaseType.SMD),
            "DIP-18_SMD"            : self.make_params(7.62,   18, CaseType.SMD),
            "DIP-20_SMD"            : self.make_params(7.62,   20, CaseType.SMD),
            "DIP-22_SMD_Narrow"     : self.make_params(7.62,   22, CaseType.SMD),
            "DIP-22_SMD"            : self.make_params(10.16,  22, CaseType.SMD),
            "DIP-24_SMD_Narrow"     : self.make_params(7.62,   24, CaseType.SMD),
            "DIP-24_SMD"            : self.make_params(10.16,  24, CaseType.SMD),
            "DIP-24_SMD_Wide"       : self.make_params(15.24,  24, CaseType.SMD),
            "DIP-28_SMD_Narrow"     : self.make_params(7.62,   28, CaseType.SMD),
            "DIP-28_SMD"            : self.make_params(15.24,  28, CaseType.SMD),
            "DIP-32_SMD_Narrow"     : self.make_params(7.62,   32, CaseType.SMD),
            "DIP-32_SMD"            : self.make_params(15.24,  32, CaseType.SMD),
            "DIP-40_SMD"            : self.make_params(15.24,  40, CaseType.SMD),
            "DIP-48_SMD"            : self.make_params(15.24,  48, CaseType.SMD),
            "DIP-64_SMD"            : self.make_params(15.24,  64, CaseType.SMD)
        }

    def make_params(self, pin_rows_distance, num_pins, type):
        return self.Params(
            pin_rows_distance = pin_rows_distance,  # pin rows distance
            num_pins = num_pins,                    # total number of pins
            type = type                             # SMD and/or THT
        )

### EOF ###

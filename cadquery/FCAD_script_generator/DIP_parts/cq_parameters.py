# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Generic DIP parameters
#

from collections import namedtuple

CASE_THT_TYPE = 'tht'
CASE_SMD_TYPE = 'smd'

model_to_build = 'DIP-10'

Params = namedtuple("Params", [
    'pin_row_distance', # package shoulder-to-shoulder width
    'num_pins',         # number of pins
    'type'              # THT and/or SMD
])

def make_params(pin_row_distance, num_pins, type):
    return Params(
        pin_row_distance = pin_row_distance,    # pin rows distance
        num_pins = num_pins,                    # total number of pins
        type = type                             # SMD and/or THT
    )

all_params = {
#
# E - pin rows distance
# P - total number of pins
# Case - case type
#   Generic name                          E        P  Case
    "DIP-4"                 : make_params(7.62,    4, CASE_THT_TYPE),
    "DIP-4_Wide"            : make_params(10.16,   4, CASE_THT_TYPE),
    "DIP-6"                 : make_params(7.62,    6, CASE_THT_TYPE),
    "DIP-6_Wide"            : make_params(10.16,   6, CASE_THT_TYPE),
    "DIP-8"                 : make_params(7.62,    8, CASE_THT_TYPE),
    "DIP-8_Wide"            : make_params(10.16,   8, CASE_THT_TYPE),
    "DIP-10"                : make_params(7.62,   10, CASE_THT_TYPE),
    "DIP-12"                : make_params(7.62,   12, CASE_THT_TYPE),
    "DIP-14"                : make_params(7.62,   14, CASE_THT_TYPE),
    "DIP-16"                : make_params(7.62,   16, CASE_THT_TYPE),
    "DIP-18"                : make_params(7.62,   18, CASE_THT_TYPE),
    "DIP-20"                : make_params(7.62,   20, CASE_THT_TYPE),
    "DIP-22_Narrow"         : make_params(7.62,   22, CASE_THT_TYPE),
    "DIP-22"                : make_params(10.16,  22, CASE_THT_TYPE),
    "DIP-24_Narrow"         : make_params(7.62,   24, CASE_THT_TYPE),
    "DIP-24"                : make_params(10.16,  24, CASE_THT_TYPE),
    "DIP-24_Wide"           : make_params(15.24,  24, CASE_THT_TYPE),
    "DIP-28_Narrow"         : make_params(7.62,   28, CASE_THT_TYPE),
    "DIP-28"                : make_params(15.24,  28, CASE_THT_TYPE),
    "DIP-32_Narrow"         : make_params(7.62,   32, CASE_THT_TYPE),
    "DIP-32"                : make_params(15.24,  32, CASE_THT_TYPE),
    "DIP-40"                : make_params(15.24,  40, CASE_THT_TYPE),
    "DIP-48"                : make_params(15.24,  48, CASE_THT_TYPE),
    "DIP-64"                : make_params(15.24,  64, CASE_THT_TYPE),

    "DIP-2_SMD"             : make_params(7.62,    2, CASE_SMD_TYPE),
    "DIP-4_SMD"             : make_params(7.62,    4, CASE_SMD_TYPE),
    "DIP-4_SMD_Wide"        : make_params(10.16,   4, CASE_SMD_TYPE),
    "DIP-6_SMD"             : make_params(7.62,    6, CASE_SMD_TYPE),
    "DIP-6_SMD_Wide"        : make_params(10.16,   6, CASE_SMD_TYPE),
    "DIP-8_SMD"             : make_params(7.62,    8, CASE_SMD_TYPE),
    "DIP-8_SMD_Wide"        : make_params(10.16,   8, CASE_SMD_TYPE),
    "DIP-10_SMD"            : make_params(7.62,   10, CASE_SMD_TYPE),
    "DIP-12_SMD"            : make_params(7.62,   12, CASE_SMD_TYPE),
    "DIP-14_SMD"            : make_params(7.62,   14, CASE_SMD_TYPE),
    "DIP-16_SMD"            : make_params(7.62,   16, CASE_SMD_TYPE),
    "DIP-18_SMD"            : make_params(7.62,   18, CASE_SMD_TYPE),
    "DIP-20_SMD"            : make_params(7.62,   20, CASE_SMD_TYPE),
    "DIP-22_SMD_Narrow"     : make_params(7.62,   22, CASE_SMD_TYPE),
    "DIP-22_SMD"            : make_params(10.16,  22, CASE_SMD_TYPE),
    "DIP-24_SMD_Narrow"     : make_params(7.62,   24, CASE_SMD_TYPE),
    "DIP-24_SMD"            : make_params(10.16,  24, CASE_SMD_TYPE),
    "DIP-24_SMD_Wide"       : make_params(15.24,  24, CASE_SMD_TYPE),
    "DIP-28_SMD_Narrow"     : make_params(7.62,   28, CASE_SMD_TYPE),
    "DIP-28_SMD"            : make_params(15.24,  28, CASE_SMD_TYPE),
    "DIP-32_SMD_Narrow"     : make_params(7.62,   32, CASE_SMD_TYPE),
    "DIP-32_SMD"            : make_params(15.24,  32, CASE_SMD_TYPE),
    "DIP-40_SMD"            : make_params(15.24,  40, CASE_SMD_TYPE),
    "DIP-48_SMD"            : make_params(15.24,  48, CASE_SMD_TYPE),
    "DIP-64_SMD"            : make_params(15.24,  64, CASE_SMD_TYPE)
}

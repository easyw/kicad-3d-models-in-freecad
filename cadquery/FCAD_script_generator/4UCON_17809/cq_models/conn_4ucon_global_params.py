#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


lib_name="Connectors_4UCON"
out_dir=lib_name+".pretty"+os.sep
packages_3d=lib_name+".3dshapes"+os.sep

manufacturer_tag = "4ucon "

def generate_footprint_name(series_name, num_pins, pin_pitch):
    name = '4UCON_{:s}_02x{:02d}x{:.2f}mm_Vertical'.format(series_name, num_pins // 2, pin_pitch)
    return name

"""
return "4UCON_" + series_name + "_02x"+ ('%02d' % num_pins / 2)\
        + "x" + ('%.2f' % pin_pitch) + "mm_Vertical"
"""

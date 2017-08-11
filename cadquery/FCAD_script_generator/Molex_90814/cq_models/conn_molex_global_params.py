import os
import sys


lib_name="Connectors_Molex"
out_dir=lib_name+".pretty"+os.sep
packages_3d=lib_name+".3dshapes"+os.sep

manufacturer_tag = "molex "

def generate_footprint_name(series_name, num_pins, pin_pitch):
    return "Molex_" + series_name + "_" \
        + ('%02d' % num_pins) + "x" + ('%.2f' % pin_pitch) + "mm_Straight_SMD"



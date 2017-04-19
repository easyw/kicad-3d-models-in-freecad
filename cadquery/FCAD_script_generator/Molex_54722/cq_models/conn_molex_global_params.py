import os
import sys


lib_name="Connectors_Molex"
out_dir=lib_name+".pretty"+os.sep
packages_3d=lib_name+".3dshapes"+os.sep

manufacturer_tag = "molex "

def generate_footprint_name(series_name, part_name, num_pins, pin_pitch):
    name = 'Molex_SlimStack_Receptacle_02x{:02d}_{:.1f}mm_{:s}-{:s}'.format(num_pins / 2, pin_pitch, series_name, part_name)
    return name

# e.g. "Molex_SlimStack_Receptacle_02x08_0.5mm_54722-0164"


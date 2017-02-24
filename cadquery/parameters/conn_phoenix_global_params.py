import os
import sys


#class globalParams():


lib_name="Connectors_Phoenix"
out_dir=lib_name+".pretty"+os.sep
packages_3d=lib_name+".3dshapes"+os.sep

manufacturer_tag = "phoenix_contact "

def generate_footprint_name(series_name, num_pins, pin_pitch, angled, mount_hole, flanged):
    return "PhoenixContact_" + series_name + "_"+ ('%02d' % num_pins) + "x"\
    + ('%.2f' % pin_pitch) + "mm_" + ('Angled' if angled else 'Vertical')\
    + ('_ThreadedFlange' + ('_MountHole' if mount_hole else '') if flanged else '')

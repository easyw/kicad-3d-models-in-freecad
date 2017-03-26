# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

from collections import namedtuple

destination_dir="/BGA_packages"
# destination_dir="./"


Params = namedtuple("Params", [
    'c',    # pin thickness, body center part height
#    'K',    # Fillet radius for pin edges
    'L',    # pin top flat part length (including fillet radius)
    'fp_r', # first pin indicator radius, set to 0.0 to remove first pin indicator
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges
    'cce',  # chamfer of the epad 1st pin corner
    'D',    # body overall lenght
    'E',    # body overall width
    'A1',   # body-board separation
    'A2',   # body height
    'b',    # pin width
    'e',    # pin (center-to-center) distance
    'sp',   # seating plane (pcb penetration)
    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'excluded_pins', #pins to exclude
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefixD2 = params.epad[0]
])
    
kicad_naming_params_qfn = {
    'BGA-48_6x8_8.0x9.0mm_Pitch0.8mm': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 9.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.22,  # body-board separation 
        A2 = 0.77,  # body height
        b = 0.5,  # ball pin width diameter
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.12, #seating plane (pcb penetration)
        npx = 8,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        excluded_pins = None, #no pin excluded
        modelName = 'BGA-48_6x8_8.0x9.0mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
}

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

destination_dir="/generated_qfn/"
# destination_dir="./"

case_color = (26, 26, 26)
#case_color = (50, 50, 50)
#pins_color = (230, 230, 230)
pins_color = (205,205,192)
#mark_color = (255,255,255) #white
#mark_color = (255,250,250) #snow
#mark_color = (255,255,240) #ivory
mark_color = (248,248,255) #ghost white
#max_cc1 = 1     # maximum size for 1st pin corner chamfer

Params = namedtuple("Params", [
    'c',    # pin thickness, body center part height
#    'K',    # Fillet radius for pin edges
    'L',    # pin top flat part length (including fillet radius)
    'fp_r', # first pin indicator radius
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

    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'epad',  # exposed pad, None or the dimensions as tuple: (width, length)
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_qfn = {
    'QFN16': Params( # 3x3, 0.5 pitch, 16 pins, 1.0mm height  QFN16 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (1.7,1.7), # e Pad #epad = None, # e Pad
        modelName = 'qfn16_3x3_p05', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN44': Params( # 8x8, 0.65 pitch, 44 pins, 1.0mm height  QFN44 p065 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (6.45,6.45), # e Pad #epad = None, # e Pad
        modelName = 'qfn44_8x8_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN64': Params( # 9x9, 0.5 pitch, 64 pins, 0.9mm height  QFN64 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
        D = 9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.88,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (4.7,4.7), # e Pad #epad = None, # e Pad
        modelName = 'qfn64_9x9_p05', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = ''
        ),
}
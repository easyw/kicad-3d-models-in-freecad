# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

from collections import namedtuple

destination_dir="./generated_qfp/"
# destination_dir="./"

case_color = (0.1, 0.1, 0.1)
pins_color = (0.9, 0.9, 0.9)

# common dimensions from MS-026D
the = 12.0      # body angle in degrees
tb_s = 0.15     # top part of body is that much smaller

c = 0.1         # pin thickness, body center part height
R1 = 0.1        # pin upper corner, inner radius
R2 = 0.1        # pin lower corner, inner radius
S = 0.2         # pin top flat part length (excluding corner arc)
L = 0.6         # pin bottom flat part length (including corner arc)

# other common dimensions
fp_r = 0.5      # first pin indicator radius
fp_d = 0.2      # first pin indicator distance from edge
fp_z = 0.1      # first pin indicator depth
ef = 0.05       # fillet of edges

Params = namedtuple("Params", [
    'D1',   # body width
    'E1',   # body length
    'A1',   # body-board seperation
    'A2',   # body height

    'b',    # pin width
    'e',    # pin (center-to-center) distance

    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'epad',  # exposed pad, None or the dimensions as tuple: (width, length)
    'modelName', #modelName
    'rotation' #rotation if required
])

all_params = {
    'AKA': Params( # 4x4, pitch 0.65 20pin 1mm height
        D1 = 4.0,  # body width
        E1 = 4.0,  # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 5,   # number of pins along X axis (width)
        npy = 5,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp20_4x4_p032', #modelName
        rotation = 0 # rotation if required
        ),

    'ABD': Params( # 7x7, 0.4 pitch, 64 pins, 1mm height
        D1 = 7.0, # body width
        E1 = 7.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,   # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp32_7x7_p04', #modelName
        rotation = 0 # rotation if required
        ),

    'AFB': Params( # 20x20, 0.5 pitch, 144pins, 1mm height
        D1 = 20.0, # body width
        E1 = 20.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,   # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp64_20x20_p05', #modelName
        rotation = 0 # rotation if required
        ),

    'ACB': Params( # 10x10, 0.8 pitch, 44 pins, 1mm height
        D1 = 10.0, # body width
        E1 = 10.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.37,  # pin width
        e = 0.8,   # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp44_10x10_p08', #modelName
        rotation = 0 # rotation if required
        ),

    'ACC': Params( # 10x10, 0.65 pitch, 52 pins, 1mm height
        D1 = 10.0, # body width
        E1 = 10.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp52_10x10_p065', #modelName
        rotation = 0 # rotation if required
        ),

    'ACE': Params( # 10x10, 0.4 pitch, 80 pins, 1mm height
        D1 = 10.0, # body width
        E1 = 10.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp80_10x10_p04', #modelName
        rotation = 0 # rotation if required
        ),

    'ACX': Params( # 10x10, 0.5 pitch, 64 pins, 1.2mm height  LQFP64 p05 microchip maui
        D1 = 10.0, # body width
        E1 = 10.0, # body length
        A1 = 0.1,  # body-board seperation  maui to check
        A2 = 1.2,  # body height
        b = 0.20,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp64_10x10_p05', #modelName
        rotation = 0 # rotation if required
        ),

    'ADC': Params( # 12x12, 0.65 pitch, 64 pins, 1mm height
        D1 = 12.0, # body width
        E1 = 12.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp64_12x12_p065', #modelName
        rotation = 0 # rotation if required
        ),

    'ADD': Params( # 12x12, 0.5 pitch, 80 pins, 1mm height
        D1 = 12.0, # body width
        E1 = 12.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp80_12x12_p05', #modelName
        rotation = 0 # rotation if required
        ),

    'AEC': Params( # 14x14, 0.65 pitch, 80 pins, 1mm height
        D1 = 14.0, # body width
        E1 = 14.0, # body length
        A1 = 0.1,  # body-board seperation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp80_14x14_p065', #modelName
        rotation = 0 # rotation if required
        ),
}

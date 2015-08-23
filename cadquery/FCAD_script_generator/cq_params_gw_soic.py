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

destination_dir="/generated_gw/"
# destination_dir="./"

case_color = (26, 26, 26)
#case_color = (50, 50, 50)
#pins_color = (230, 230, 230)
pins_color = (205,205,192)
#mark_color = (255,255,255) #white
#mark_color = (255,250,250) #snow
#mark_color = (255,255,240) #ivory
mark_color = (248,248,255) #ghost white
max_cc1 = 1     # maximum size for 1st pin corner chamfer

Params = namedtuple("Params", [
    'the',  # body angle in degrees
    'tb_s', # top part of body is that much smaller
    'c',    # pin thickness, body center part height
    'R1',   # pin upper corner, inner radius
    'R2',   # pin lower corner, inner radius
    'S',    # pin top flat part length (excluding corner arc)
# automatic calculated    'L',    # pin bottom flat part length (including corner arc)
    'fp_r', # first pin indicator radius
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges
    'cc1',  # chamfer of the 1st pin corner

    'D1',   # body lenght
    'E1',   # body width
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

all_params_soic = {
    'SOIC_8': Params( # 3.9x4.9, pitch 1.27 8pin 1.75mm height
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 0.65,       # pin bottom flat part length (including corner arc)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 4.9,       # body length
        E1 = 3.9,       # body width
        E = 6.0,        # body overall width
        A1 = 0.1,       # body-board separation
        A2 = 1.65,      # body height
        b = 0.45,       # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 4,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        modelName = 'soic_8_39x49_p127', #modelName
        rotation = 0,   # rotation if required
        dest_dir_prefix = 'soic'
        ),
     'SOIC_16': Params( # 3.9x9.9, pitch 1.27 16pin 1.75mm height
         the = 9.0,      # body angle in degrees
         tb_s = 0.15,    # top part of body is that much smaller
         c = 0.2,        # pin thickness, body center part height
         R1 = 0.1,       # pin upper corner, inner radius
         R2 = 0.1,       # pin lower corner, inner radius
         S = 0.25,       # pin top flat part length (excluding corner arc)
#         L = 0.79,       # pin bottom flat part length (including corner arc)
         fp_r = 0.5,     # first pin indicator radius
         fp_d = 0.2,     # first pin indicator distance from edge
         fp_z = 0.1,     # first pin indicator depth
         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
         cc1 = 0.25, #0.45 chamfer of the 1st pin corner
         D1 = 9.9,       # body length
         E1 = 3.9,       # body width
         E = 6.0,        # body overall width
         A1 = 0.1,       # body-board separation
         A2 = 1.65,      # body height
         b = 0.45,       # pin width
         e = 1.27,
         npx = 8,        # number of pins along X axis (width)
         npy = 0,        # number of pins along y axis (length)
         epad = None,    # e Pad
         modelName = 'soic_16_39x99_p127', #modelName
         rotation = 0,   # rotation if required
         dest_dir_prefix = 'soic'        
         ),
    'SOIC_16_W': Params( # 7.5x10.3, pitch 1.27 16pin 1.75mm height
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.35,       # pin top flat part length (excluding corner arc)
#        L = 0.95,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.30,       # body length
        E1 = 7.5,       # body width
        E = 10.30,        # body overall width
        A1 = 0.1,       # body-board separation
        A2 = 1.65,      # body height
        b = 0.45,       # pin width
        e = 1.27,
        npx = 8,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        modelName = 'soic_16_75x103_p127', #modelName
        rotation = 0,   # rotation if required
        dest_dir_prefix = 'soic'        
        ),
}

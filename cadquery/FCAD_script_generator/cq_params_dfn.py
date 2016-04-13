                               # -*- coding: utf8 -*-
                               # !/usr/bin/python
                               #
                               # This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
                               #
                               # from https://bitbucket.org/hyOzd/freecad-macros
                               # author hyOzd
                               #
                               # Dimensions are from Jedec MS-026D document.

                               # # file of parametric definitions

from collections import namedtuple

destination_dir="/generated_dfn/"
                               # destination_dir="./"

case_color = (26, 26, 26)
                               # case_color = (50, 50, 50)
                               # pins_color = (230, 230, 230)
pins_color = (205,205,192)
                               # mark_color = (255,255,255) #white
                               # mark_color = (255,250,250) #snow
                               # mark_color = (255,255,240) #ivory
mark_color = (248,248,255)     # ghost white
                               # max_cc1 = 1     # maximum size for 1st pin corner chamfer

Params = namedtuple("Params", [
'c',                           # pin thickness, body center part height
                               # 'K',    # Fillet radius for pin edges
'L',                           # pin top flat part length (including fillet radius)
'fp_r',                        # first pin indicator radius
'fp_d',                        # first pin indicator distance from edge
'fp_z',                        # first pin indicator depth
'ef',                          # fillet of edges
'cce',                         # chamfer of the epad 1st pin corner
'D',                           # body overall lenght
'E',                           # body overall width
'A1',                          # body-board separation
'A2',                          # body height
'b',                           # pin width
'e',                           # pin (center-to-center) distance

'npx',                         # number of pins along X axis (width)
'npy',                         # number of pins along y axis (length)
'epad',                        # exposed pad, None or the dimensions as tuple: (width, length)
'modelName',                   # modelName
'rotation',                    # rotation if required
'dest_dir_prefix'              # destination dir prefix
])

all_params_dfn = {
    'DFN4A': Params(
        c = 0.2,                       # pin thickness, body center part height
                                       # K=0.2,          # Fillet radius for pin edges
        L = 0.35,                      # pin top flat part length (including fillet radius)
        fp_r = 0.15,                   # first pin indicator radius
        fp_d = 0.03,                   # first pin indicator distance from edge
        fp_z = 0.01,                  # first pin indicator depth
        ef = 0.0,                      # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,                     # 0.45 chamfer of the epad 1st pin corner
        D = 1.1,                       # body overall length
        E = 0.9,                       # body overall width
        A1 = 0.02,                     # body-board separation  maui to check
        A2 = 0.55,                     # body height
        b = 0.2,                       # pin width
        e = 0.55,                      # pin (center-to-center) distance
        npx = 0,                       # number of pins along X axis (width)
        npy = 2,                       # number of pins along y axis (length)
        epad = None,                   # e Pad #epad = None, # e Pad
        modelName = 'DFN4_09x12_p055', # modelName
        rotation = 0,                  # rotation if required
        dest_dir_prefix = ''
        ),
    'UTDFN8': Params(
        c = 0.2,                       # pin thickness, body center part height
                                       # K=0.2,          # Fillet radius for pin edges
        L = 0.35,                      # pin top flat part length (including fillet radius)
        fp_r = 0.15,                   # first pin indicator radius
        fp_d = 0.03,                   # first pin indicator distance from edge
        fp_z = 0.01,                   # first pin indicator depth
        ef = 0.0,                      # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,                     # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,                       # bwody overall length
        E = 2.0,                       # body overall width
        A1 = 0.02,                     # body-board separation  maui to check
        A2 = 0.55,                     # body height
        b = 0.23,                      # pin width
        e = 0.45,                      # pin (center-to-center) distance
        npx = 4,                       # number of pins along X axis (width)
        npy = 0,                       # number of pins along y axis (length)
        epad = (1.37,0.64),            # e Pad #epad = None, # e Pad
        modelName = 'UTDFN8_2x2_p045', # modelName
        rotation = 0,                  # rotation if required
        dest_dir_prefix = ''
        ),
    'UTDFN10': Params(
        c = 0.2,                       # pin thickness, body center part height
                                       # K=0.2,          # Fillet radius for pin edges
        L = 0.35,                      # pin top flat part length (including fillet radius)
        fp_r = 0.15,                   # first pin indicator radius
        fp_d = 0.03,                   # first pin indicator distance from edge
        fp_z = 0.01,                   # first pin indicator depth
        ef = 0.0,                      # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,                     # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,                       # body overall length
        E = 3.0,                       # body overall width
        A1 = 0.02,                     # body-board separation  maui to check
        A2 = 0.55,                     # body height
        b = 0.25,                      # pin width
        e = 0.5,                       # pin (center-to-center) distance
        npx = 5,                       # number of pins along X axis (width)
        npy = 0,                       # number of pins along y axis (length)
        epad = (2.38,1.65),            # e Pad #epad = None, # e Pad
        modelName = 'UTDFN10_3x3_p05', # modelName
        rotation = 0,                  # rotation if required
        dest_dir_prefix = ''
        ),
    'UTDFN14': Params(
        c = 0.2,                       # pin thickness, body center part height
                                       # K=0.2,          # Fillet radius for pin edges
        L = 0.35,                      # pin top flat part length (including fillet radius)
        fp_r = 0.15,                   # first pin indicator radius
        fp_d = 0.03,                   # first pin indicator distance from edge
        fp_z = 0.01,                   # first pin indicator depth
        ef = 0.0,                      # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,                     # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,                       # body overall length
        E = 3.0,                       # body overall width
        A1 = 0.02,                     # body-board separation  maui to check
        A2 = 0.55,                     # body height
        b = 0.25,                      # pin width
        e = 0.5,                       # pin (center-to-center) distance
        npx = 7,                       # number of pins along X axis (width)
        npy = 0,                       # number of pins along y axis (length)
        epad = (3.25,1.65),            # e Pad #epad = None, # e Pad
        modelName = 'UTDFN14_4x3_p05', # modelName
        rotation = 0,                  # rotation if required
        dest_dir_prefix = ''
        ),
        }
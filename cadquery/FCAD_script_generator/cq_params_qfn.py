# -*- coding: utf8 -*-
# !/usr/bin/python
#
# This is derived from a cadquery script for generating qfn models.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# minor contributions from metacollin
# Dimensions are from Jedec MS-026D document.

# file of parametric definitions

from collections import namedtuple

destination_dir = "/generated_qfn/"

case_color = (26,  26,  26)
# case_color = (50,  50,  50)
# pins_color = (230,  230,  230)
pins_color = (205,  205,  192)
# mark_color = (255, 255, 255)  #white
# mark_color = (255, 250, 250)  #snow
# mark_color = (255, 255, 240)  #ivory
mark_color = (248,  248,  255)  # ghost white

Params = namedtuple("Params",  [
    'c',                # pin thickness,  body center part height
    'L',                # pin top flat part length (including fillet)
    'fp_r',             # first pin indicator radius
    'fp_d',             # first pin indicator distance from edge
    'fp_z',             # first pin indicator depth
    'ef',               # Fillet of edges
    'cce',              # chamfer of the epad 1st pin corner
    'D',                # body overall lenght
    'E',                # body overall width
    'A1',               # body-board separation
    'A2',               # body height
    'b',                # pin width
    'e',                # pin (center-to-center) distance
    'npx',              # number of pins along X axis (width)
    'npy',              # number of pins along y axis (length)
    'epad',             # epad none or tuple: (width,  length)
    'modelName',        # self-explanatory
    'rotation',         # rotation if required
    'dest_dir_prefix'   # destination dir prefix
])

all_params_qfn = {
    'QFN12': Params(
        c=0.2,               # pin thickness,  body center part height
                             # Fillet radius for pin edges
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=3.0,               # body overall length
        E=3.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=3,               # number of pins along X axis (width)
        npy=3,               # number of pins along y axis (length)
        epad=(1.65, 1.65),
        modelName='qfn12_3x3_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN16': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=3.0,               # body overall length
        E=3.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=4,               # number of pins along X axis (width)
        npy=4,               # number of pins along y axis (length)
        epad=(1.65, 1.65),
        modelName='qfn16_3x3_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN20': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=4.0,               # body overall length
        E=4.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=5,               # number of pins along X axis (width)
        npy=5,               # number of pins along y axis (length)
        epad=(2, 2),
        modelName='qfn20_3x3_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN20': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=4.0,               # body overall length
        E=4.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=5,               # number of pins along X axis (width)
        npy=5,               # number of pins along y axis (length)
        epad=(2, 2),
        modelName='qfn20_3x3_p05',
        rotation=-90,        # rotation if
        dest_dir_prefix=''
        ),
    'QFN40': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=6.0,               # body overall length
        E=6.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=10,              # number of pins along X axis (width)
        npy=10,              # number of pins along y axis (length)
        epad=(4.42, 4.42),
        modelName='qfn40_6x6_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN24': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=4.15,              # body overall length
        E=4.15,              # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=6,               # number of pins along X axis (width)
        npy=6,               # number of pins along y axis (length)
        epad=(2.45, 2.45),
        modelName='qfn24_415x415_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN28': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=5,                 # body overall length
        E=5,                 # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=7,               # number of pins along X axis (width)
        npy=7,               # number of pins along y axis (length)
        epad=(3, 3),
        modelName='qfn28_5x5_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN28_p04': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=4,                 # body overall length
        E=4,                 # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.55,             # body height
        b=0.20,              # pin width
        e=0.4,               # pin (center-to-center) distance
        npx=7,               # number of pins along X axis (width)
        npy=7,               # number of pins along y axis (length)
        epad=(2.64, 2.64),
        modelName='qfn28_4x4_p04',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN32': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.4,               # pin top flat part length (including fillet)
        fp_r=0.5,            # first pin indicator radius
        fp_d=0.2,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.3,             # 0.45 chamfer of the epad 1st pin corner
        D=5.0,               # body overall length
        E=5.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.3,               # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=8,               # number of pins along X axis (width)
        npy=8,               # number of pins along y axis (length)
        epad=(3.6, 3.6),
        modelName='qfn32_5x5_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN40': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.4,               # pin top flat part length (including fillet)
        fp_r=0.5,            # first pin indicator radius
        fp_d=0.2,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.3,             # 0.45 chamfer of the epad 1st pin corner
        D=6.0,               # body overall length
        E=6.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.3,               # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=10,              # number of pins along X axis (width)
        npy=10,              # number of pins along y axis (length)
        epad=(4.2, 4.2),
        modelName='qfn40_6x6_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN40_p04': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.4,               # pin top flat part length (including fillet)
        fp_r=0.5,            # first pin indicator radius
        fp_d=0.2,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.3,             # 0.45 chamfer of the epad 1st pin corner
        D=5.0,               # body overall length
        E=5.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.2,               # pin width
        e=0.4,               # pin (center-to-center) distance
        npx=10,              # number of pins along X axis (width)
        npy=10,              # number of pins along y axis (length)
        epad=(3.5, 3.5),
        modelName='qfn40_5x5_p04',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN44_p065': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.4,               # pin top flat part length (including fillet)
        fp_r=0.5,            # first pin indicator radius
        fp_d=0.2,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.3,             # 0.45 chamfer of the epad 1st pin corner
        D=8.0,               # body overall length
        E=8.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.3,               # pin width
        e=0.65,              # pin (center-to-center) distance
        npx=11,              # number of pins along X axis (width)
        npy=11,              # number of pins along y axis (length)
        epad=(6.45, 6.45),
        modelName='qfn44_8x8_p065',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN44': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.4,               # pin top flat part length (including fillet)
        fp_r=0.5,            # first pin indicator radius
        fp_d=0.2,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.3,             # 0.45 chamfer of the epad 1st pin corner
        D=7.0,               # body overall length
        E=7.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.3,               # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=11,              # number of pins along X axis (width)
        npy=11,              # number of pins along y axis (length)
        epad=(5.15, 5.15),
        modelName='qfn44_7x7_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN48': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=7.0,               # body overall length
        E=7.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=12,              # number of pins along X axis (width)
        npy=12,              # number of pins along y axis (length)
        epad=(5.15, 5.15),
        modelName='qfn48_7x7_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN64': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.4,               # pin top flat part length (including fillet)
        fp_r=0.5,            # first pin indicator radius
        fp_d=0.2,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.4,             # 0.45 chamfer of the epad 1st pin corner
        D=9.0,               # body overall length
        E=9.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.88,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=16,              # number of pins along X axis (width)
        npy=16,              # number of pins along y axis (length)
        epad=(7.15, 7.15),
        modelName='qfn64_9x9_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN72': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=10.0,              # body overall length
        E=10.0,              # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=18,              # number of pins along X axis (width)
        npy=18,              # number of pins along y axis (length)
        epad=(6, 6),
        modelName='qfn72_10x10_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN68': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=12.0,              # body overall length
        E=7.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.98,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=12,              # number of pins along X axis (width)
        npy=22,              # number of pins along y axis (length)
        epad=(5.6, 10),
        modelName='qfn68_7x12_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN64_79': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=9.0,               # body overall length
        E=7.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.2,               # pin width
        e=0.4,               # pin (center-to-center) distance
        npx=13,              # number of pins along X axis (width)
        npy=19,              # number of pins along y axis (length)
        epad=(5.41, 7.15),
        modelName='qfn64_7x9_p04',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN64_711': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=9.0,               # body overall length
        E=7.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=12,              # number of pins along X axis (width)
        npy=20,              # number of pins along y axis (length)
        epad=(5.2, 9),
        modelName='qfn64_7x11_p05',
        rotation=-90,
        dest_dir_prefix=''
        ),
    'QFN58': Params(
        c=0.2,               # pin thickness,  body center part height
        L=0.35,              # pin top flat part length (including fillet)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.01,           # first pin indicator depth
        ef=0.0,              # Fillet of edges
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=9.0,               # body overall length
        E=5.0,               # body overall width
        A1=0.02,             # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.2,               # pin width
        e=0.4,               # pin (center-to-center) distance
        npx=10,              # number of pins along X axis (width)
        npy=19,              # number of pins along y axis (length)
        epad=(2.32, 4.8),
        modelName='qfn58_5x9_p04',
        rotation=-90,
        dest_dir_prefix=''
        ),
}

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
destination_dir = "generated_qfn"
# destination_dir="./"

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
    'rotation',
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
    'LGA1633': Params(  # 3x3mm, 16-pin LGA package, 1.0mm height
        c=0.2,               # pin thickness, body center part height
        L=0.3,               # pin top flat part length (including fillet radius)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.02,           # first pin indicator depth
        ef=0.0,              # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=3.0,               # body overall length
        E=3.0,               # body overall width
        A1=0.025,            # body-board separation  maui to check
        A2=1.0,              # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=5,               # number of pins along X axis (width)
        npy=3,               # number of pins along y axis (length)
        epad=None,
        modelName='lga16_3x3_p05',
        rotation=-90,
        dest_dir_prefix=''
    ),
    'DFN622': Params(  # 2x2, 0.65 pitch, 6 pins, 0.75mm height  DFN (DD / LTC)
        # Example - http://www.onsemi.com/pub_link/Collateral/NCP308-D.PDF
        c=0.2,               # pin thickness, body center part height
        L=0.3,               # pin top flat part length (including fillet radius)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.02,           # first pin indicator depth
        ef=0.0,              # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=2.0,               # body overall length
        E=2.0,               # body overall width
        A1=0.025,            # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.3,               # pin width
        e=0.65,              # pin (center-to-center) distance
        npx=3,               # number of pins along X axis (width)
        npy=0,               # number of pins along y axis (length)
        epad=(1.6, 1.0),
        modelName='dfn6_2x2_p065',
        rotation=-90,
        dest_dir_prefix=''
    ),
    'DFN8-33-50': Params(  # 3x3, 0.5 pitch, 8 pins, 0.75mm height  DFN (DD / LTC)
        # Example - http://cds.linear.com/docs/en/datasheet/2875f.pdf
        c=0.2,               # pin thickness, body center part height
                             # pin top flat part length (including fillet radius)
        L=0.7 - 0.25,
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.02,           # first pin indicator depth
        ef=0.0,              # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=3.0,               # body overall length
        E=3.0,               # body overall width
        A1=0.025,            # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=4,               # number of pins along X axis (width)
        npy=0,               # number of pins along y axis (length)
        epad=(2.38, 1.65),
        modelName='dfn8_3x3_p05',
        rotation=-90,
        dest_dir_prefix=''
    ),

    'DFN8-33-65': Params(  # 3x3, 0.65 pitch, 8 pins, 1.0mm height  DFN (DD / LTC)
        # Example -
        # http://www.st.com/web/en/resource/technical/document/datasheet/CD00001508.pdf
        c=0.2,               # pin thickness, body center part height
        L=0.4,               # pin top flat part length (including fillet radius)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.02,           # first pin indicator depth
        ef=0.0,              # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=3.0,               # body overall length
        E=3.0,               # body overall width
        A1=0.025,            # body-board separation  maui to check
        A2=1.0,              # body height
        b=0.25,              # pin width
        e=0.65,              # pin (center-to-center) distance
        npx=4,               # number of pins along X axis (width)
        npy=0,               # number of pins along y axis (length)
        epad=(2.5, 1.5),
        modelName='dfn8_3x3_p065',
        rotation=-90,
        dest_dir_prefix=''
    ),
    'DFN823': Params(  # 2x3, 0.5 pitch, 8 pins, 0.75mm height  DFN (DD / LTC)
        # Example - http://cds.linear.com/docs/en/datasheet/4365fa.pdf
        c=0.2,               # pin thickness, body center part height
        L=0.45,              # pin top flat part length (including fillet radius)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.02,           # first pin indicator depth
        ef=0.0,              # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=3.0,               # body overall length
        E=2.0,               # body overall width
        A1=0.025,            # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=4,               # number of pins along X axis (width)
        npy=0,               # number of pins along y axis (length)
        epad=(2.2, 0.61),
        modelName='dfn8_2x3_p05',
        rotation=-90,
        dest_dir_prefix=''
    ),
    'DFN865': Params(  # 6x5, 1.27mm pitch, 8 pins, 1.0mm height  DFN
        # Example - https://www.everspin.com/file/217/download
        c=0.2,               # pin thickness, body center part height
        L=0.45,              # pin top flat part length (including fillet radius)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.02,           # first pin indicator depth
        ef=0.0,              # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=5.0,               # body overall length
        E=6.0,               # body overall width
        A1=0.025,            # body-board separation  maui to check
        A2=1,                # body height
        b=0.4,               # pin width
        e=1.27,              # pin (center-to-center) distance
        npx=4,               # number of pins along X axis (width)
        npy=0,               # number of pins along y axis (length)
        epad=(2, 2),
        modelName='dfn8_6x5_p127',
        rotation=-90,
        dest_dir_prefix=''
    ),
    'DFN1023': Params(  # 2x3, 0.5mm pitch, 10 pins, 0.75mm height  DFN
        # Example -
        # http://www.ti.com.cn/general/cn/docs/lit/getliterature.tsp?genericPartNumber=tps62177&fileType=pdf
        c=0.2,               # pin thickness, body center part height
        L=0.15,              # pin top flat part length (including fillet radius)
        fp_r=0.35,           # first pin indicator radius
        fp_d=0.1,            # first pin indicator distance from edge
        fp_z=0.02,           # first pin indicator depth
        ef=0.0,              # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce=0.2,             # 0.45 chamfer of the epad 1st pin corner
        D=3.0,               # body overall length
        E=2.0,               # body overall width
        A1=0.025,            # body-board separation  maui to check
        A2=0.75,             # body height
        b=0.25,              # pin width
        e=0.5,               # pin (center-to-center) distance
        npx=5,               # number of pins along X axis (width)
        npy=0,               # number of pins along y axis (length)
        epad=(2.4, 0.84),    # e Pad #epad = None, # e Pad
        modelName='dfn10_2x3_p05',
        rotation=-90,
        dest_dir_prefix=''
    ),
}

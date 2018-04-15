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

import collections
from collections import namedtuple

destination_dir="/Package_BGA.3dshapes"
# destination_dir="./"
old_footprints_dir="Housings_BGA.pretty"
footprints_dir="Package_BGA.pretty"
##footprints_dir=None #to exclude importing of footprints

##enabling optional/default values to None
def namedtuple_with_defaults(typename, field_names, default_values=()):

    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T

Params =namedtuple_with_defaults ("Params", [
    'fp_r', # first pin indicator radius, set to 0.0 to remove first pin indicator
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges
    'cff',  # chamfer of the 1st pin corner
    'cf',   # chamfer of the others corner
    'D',    # body overall lenght
    'E',    # body overall width
    'D1',   # top body overall length
    'E1',   # top body overall width
    'A1',   # body-board separation
    'A2',   # body height or body bottom height optional, needed for molded
    'A',    # body  overall height
    'b',    # ball pin width diameter with a small extra to obtain a union of balls and case
    'e',    # pin (center-to-center) distance
    'sp',   # seating plane (pcb penetration)
    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'excluded_pins', #pins to exclude -> None or "internal
    'molded', # molded = True, omitted -> None
    'old_modelName', #old_modelName
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefixD2 = params.epad[0]
])

kicad_naming_params_qfn = {
#    'BGA-48': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
#        fp_r = 0.4,     # first pin indicator radius
#        fp_d = 0.08,     # first pin indicator distance from edge
#        fp_z = 0.01,     # first pin indicator depth
#        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#        D = 9.0,       # body overall length
#        E = 8.0,       # body overall width
#        A1 = 0.22,  # body-board separation
#        A = 0.77,  # body height
#        b = 0.505,  # ball pin width diameter with a small extra to obtain a union of balls and case
#        e = 0.8,  # pin (center-to-center) distance
#        sp = 0.0, #seating plane (pcb penetration)
#        npx = 8,  # number of pins along X axis (width)
#        npy = 6,  # number of pins along y axis (length)
#        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
#        old_modelName = 'BGA-48', #old_modelName
#        modelName = '',
#        rotation = -90, # rotation if required
#        dest_dir_prefix = '',
#        ),
    'BGA-9_3x3_1.6x1.6mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/bq27421-g1.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.04,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.6,       # body overall length
        E = 1.6,       # body overall width
        A1 = 0.25,  # body-board separation
        A = 0.625,  # body  overall height
        b = 0.3,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 3,  # number of pins along X axis (width)
        npy = 3,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-9_3x3_1.6x1.6mm_Pitch0.5mm', #old_modelName
        modelName = 'BGA-9_1.6x1.6mm_Layout3x3_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Maxim_WLP-12': Params( # W121B2+1 from http://pdfserv.maximintegrated.com/package_dwgs/21-0009.PDF
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.04,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0    , 	# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.6,       	# body overall length
        E = 2.0,       	# body overall width
        A1 = 0.24,  	# body-board separation
        A = 0.64,  		# body  overall height
        b = 0.31,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 3,  		# number of pins along X axis (width)
        npy = 4,  		# number of pins along y axis (length)
        excluded_pins = ("None",), #pins to exclude -> None or "internals"
        old_modelName = 'Maxim_WLP-12', #old_modelName
        modelName = 'Maxim_WLP-12', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-16_4x4_1.92x1.92mm_Pitch0.5mm': Params( # from http://www.st.com/content/ccc/resource/technical/document/datasheet/group2/bc/cd/62/9e/8f/30/47/69/CD00151267/files/CD00151267.pdf/jcr:content/translations/en.CD00151267.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.04,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.92,       # body overall length
        E = 1.92,       # body overall width
        A1 = 0.25,  # body-board separation
        A = 0.65,  # body  overall height
        b = 0.3,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-16_4x4_1.92x1.92mm_Pitch0.5mm', #old_modelName
        modelName = 'BGA-16_1.92x1.92mm_Layout4x4_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-25_5x5_6.35x6.35mm_Pitch1.27mm': Params( # from http://cds.linear.com/docs/en/datasheet/4624fc.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 6.25,       # body overall length
        E = 6.25,       # body overall width
        A1 = 0.60,  # body-board separation
        A = 5.01,  # body  overall height
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.27,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 5,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-25_5x5_6.35x6.35mm_Pitch1.27mm', #old_modelName
        modelName = 'BGA-25_6.35x6.35mm_Layout5x5_P1.27mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-48_6x8_8.0x9.0mm_Pitch0.8mm': Params( # from https://www.xilinx.com/support/documentation/package_specs/fs48.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 9.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.30,  # body-board separation
        A = 1.2,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 8,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-48_6x8_8.0x9.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-48_8.0x9.0mm_Layout6x8_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-64_10x10_9.0x9.0mm_Pitch0.8mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT926-1.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.35,  # body-board separation
        A = 1.2,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-64_10x10_9.0x9.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-64_9.0x9.0mm_Layout10x10_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-90_2x3x15_8.0x13.0mm_Pitch0.8mm': Params( # from http://www.issi.com/WW/pdf/42-45S32800J.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 13.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.32,  # body-board separation
        A = 1.2,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 15,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        excluded_pins = ("internals", 46, 60, 61, 75, 76, 90), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-90_2x3x15_8.0x13.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-90_8.0x13.0mm_Layout2x3x15_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-96_2x3x16_9.0x13.0mm_Pitch0.8mm': Params( # from http://www.mouser.com/ds/2/198/43-46TR16640B-81280BL-706483.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 13.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.32,  # body-board separation
        A = 1.2,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 16,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        excluded_pins = ("internals", 49, 64, 65, 80, 81, 96), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-96_2x3x16_9.0x13.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-96_9.0x13.0mm_Layout2x3x16_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-100_10x10_9.0x9.0mm_Pitch0.8mm': Params( # from http://www.mouser.com/ds/2/198/43-46TR16640B-81280BL-706483.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.35,  # body-board separation
        A = 1.2,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-100_10x10_9.0x9.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-100_9.0x9.0mm_Layout10x10_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-121_11x11_12.0x12.0mm_Pitch1.0mm': Params( # from http://cds.linear.com/docs/en/packaging/05081891_A_bga121.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 12.0,       # body overall length
        E = 12.0,       # body overall width
        A1 = 0.3,  # body-board separation
        A = 4.92,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-121_11x11_12.0x12.0mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-121_12.0x12.0mm_Layout11x11_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-144_12x12_13.0x13.0mm_Pitch1.0mm': Params( # from http://www.topline.tv/drawings/pdf/BGA%201,0mm%20pitch/LBGA144T1.0-DC128.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 13.0,       # body overall length
        E = 13.0,       # body overall width
        A1 = 0.6,  # body-board separation
        A = 1.6,  # body  overall height
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-144_12x12_13.0x13.0mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-144_13.0x13.0mm_Layout12x12_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-256_16x16_17.0x17.0mm_Pitch1.0mm': Params( # from https://www.intersil.com/content/dam/Intersil/documents/v256/v256.17x17.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 17.0,       # body overall length
        E = 17.0,       # body overall width
        A1 = 0.4,  # body-board separation
        A = 1.50,  # body overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-256_16x16_17.0x17.0mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-256_17.0x17.0mm_Layout16x16_P1.0mm_Ball0.5mm_Pad0.4mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-352_26x26_35.0x35.0mm_Pitch1.27mm': Params( # from https://www.fujitsu.com/downloads/MICRO/fma/pdfmcu/b352p05.pdf
        fp_r = 1.0,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cff = 0.6,      #0.5 chamfer of the 1st pin corner
        cf = 0.3,      #0.5 chamfer of the others corner
        D = 35.0,       # body overall length
        E = 35.0,       # body overall width
        D1 = 25.0,       # top body overall length
        E1 = 25.0,       # top body overall width
        A1 = 0.6,  # body-board separation
        A2 = 2.0,  # body bottom height optional, needed for molded
        A  = 3.1,  # body  overall height
        molded = True, # molded = True, omitted -> None
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.27,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 26,  # number of pins along X axis (width)
        npy = 26,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-352_26x26_35.0x35.0mm_Pitch1.27mm', #old_modelName
        modelName = 'BGA-352_35.0x35.0mm_Layout26x26_P1.27mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-400_20x20_17.0x17.0mm_Pitch0.8mm': Params( # from https://www.xilinx.com/support/documentation/user_guides/ug865-Zynq-7000-Pkg-Pinout.pdf
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 17.0,       # body overall length
        E = 17.0,       # body overall width
        D1 = 15.2,       # top body overall length
        E1 = 15.2,       # top body overall width
        A1 = 0.40,  # body-board separation
        A  = 1.47,  # body  overall height
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-400_20x20_17.0x17.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-400_17.0x17.0mm_Layout20x20_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-400_20x20_21.0x21.0mm_Pitch1.0mm': Params( # from https://www.xilinx.com/support/documentation/package_specs/fg400.pdf
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cff = 0.4,      #0.5 chamfer of the 1st pin corner
        cf = 0.2,      #0.5 chamfer of the others corner
        D = 21.0,       # body overall length
        E = 21.0,       # body overall width
        D1 = 19.0,       # top body overall length
        E1 = 19.0,       # top body overall width
        A1 = 0.50,  # body-board separation
        A2 = 0.60,  # body bottom height optional, needed for molded
        A  = 2.23,  # body  overall height
        molded = True, # molded = True, omitted -> None
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-400_20x20_21.0x21.0mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-400_21.0x21.0mm_Layout20x20_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-484_22x22_23.0x23.0mm_Pitch1.0mm': Params( # from https://www.xilinx.com/support/documentation/package_specs/fg484.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.14,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cff = 0.05,      #0.5 chamfer of the 1st pin corner
        cf = 0.25,      #0.5 chamfer of the others corner
        D = 23.0,       # body overall length
        E = 23.0,       # body overall width
        D1 = 20.5,       # top body overall length
        E1 = 20.5,       # top body overall width
        A1 = 0.50,  # body-board separation
        A2 = 1.0,  # body bottom height optional, needed for molded
        A  = 2.3,  # body  overall height
        molded = True, # molded = True, omitted -> None
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 22,  # number of pins along X axis (width)
        npy = 22,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-484_22x22_23.0x23.0mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-484_23.0x23.0mm_Layout22x22_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-625_25x25_21.0x21.0mm_Pitch0.8mm': Params( # from http://www.analog.com/media/en/technical-documentation/data-sheets/ADSP-TS101S.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.14,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cff = 0.05,      #0.5 chamfer of the 1st pin corner
        cf = 0.25,      #0.5 chamfer of the others corner
        D = 25.0,       # body overall length
        E = 25.0,       # body overall width
        D1 = 16.95,       # top body overall length
        E1 = 16.95,       # top body overall width
        A1 = 0.40,  # body-board separation
        A2 = .55,  # body bottom height optional, needed for molded
        A  = 2.5,  # body  overall height
        molded = True, # molded = True, omitted -> None
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-625_25x25_21.0x21.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-625_21.0x21.0mm_Layout25x25_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-1023_32x32_33.0x33.0mm_Pitch1.0mm': Params( # from https://www.idt.com/document/psc/hmrm-1023-package-outline-33-x-33-mm-body-100-mm-pitch-fcbga IDT_PSC-4260.pdf
        fp_r = 1.0,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.1    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cff = 0.8,      #0.5 chamfer of the 1st pin corner
        cf = 0.5,      #0.5 chamfer of the others corner
        D = 33.2,       # body overall length
        E = 33.2,       # body overall width
        D1 = 30.0,       # top body overall length
        E1 = 30.0,       # top body overall width
        A1 = 0.45,  # body-board separation
        A2 = 1.2,  # body bottom height optional, needed for molded
        A  = 2.5,  # body  overall height
        molded = True, # molded = True, omitted -> None
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 32,  # number of pins along X axis (width)
        npy = 32,  # number of pins along y axis (length)
        excluded_pins = ("internals",1), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-1023_32x32_33.0x33.0mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-1023_33.0x33.0mm_Layout32x32_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-1156_34x34_35.0x35.0mm_Pitch1.0mm': Params( # from https://www.xilinx.com/support/documentation/package_specs/pk401_FF_G_1156.pdf
        fp_r = 1.0,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cff = 0.7,      #0.5 chamfer of the 1st pin corner
        cf = 0.2,      #0.5 chamfer of the others corner
        D = 35.5,       # body overall length
        E = 35.5,       # body overall width
        D1 = 30.0,       # top body overall length
        E1 = 30.0,       # top body overall width
        A1 = 0.5,  # body-board separation
        A2 = 1.0,  # body bottom height optional, needed for molded
        A  = 2.7,  # body  overall height
        molded = True, # molded = True, omitted -> None
        b = 0.60,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 34,  # number of pins along X axis (width)
        npy = 34,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-1156_34x34_35.0x35.0mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-1156_35.0x35.0mm_Layout34x34_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-1295_36x36_37.5x37.5mm_Pitch1.0mm': Params( # from http://www.datasheets360.com/pdf/6857809988541063510
        fp_r = 2.0,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.1    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cff = 0.4,      #0.5 chamfer of the 1st pin corner
        cf = 0.2,      #0.5 chamfer of the others corner
        D = 37.5,       # body overall length
        E = 37.5,       # body overall width
        D1 = 27.3,       # top body overall length
        E1 = 27.3,       # top body overall width
        A1 = 0.5,  # body-board separation
        A2 = 1.5,  # body bottom height optional, needed for molded
        A  = 3.19,  # body  overall height
        molded = True, # molded = True, omitted -> None
        b = 0.50,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-1295_36x36_37.5x37.5mm_Pitch1.0mm', #old_modelName
        modelName = 'BGA-1295_37.5x37.5mm_Layout36x36_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'DSBGA-8_2x4_0.9x1.9mm_Pitch0.5mm_Dia0.25mm': Params( # from http://www.ti.com/lit/ds/symlink/txb0102.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.9,       # body overall length
        E = 0.9,       # body overall width
        A1 = 0.17,  # body-board separation
        A = 0.5,  # body  overall height
        b = 0.20,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 4,  # number of pins along X axis (width)
        npy = 2,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'DSBGA-8_2x4_0.9x1.9mm_Pitch0.5mm_Dia0.25mm', #old_modelName
        modelName = 'Texas_DSBGA-8_0.9x1.9mm_Layout2x4_P0.5mm', rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'DSBGA-12_3x4_1.36x1.86mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/txb0104.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.36,       # body overall length
        E = 1.86,       # body overall width
        A1 = 0.17,  	# body-board separation
        A = 0.625,  	# body  overall height
        b = 0.25,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 3,  		# number of pins along X axis (width)
        npy = 4,  		# number of pins along y axis (length)
        excluded_pins = ("None",), #pins to exclude -> None or "internals"
        old_modelName = 'DSBGA-12_3x4_1.36x1.86mm_Pitch0.5mm', #old_modelName
        modelName = 'Texas_DSBGA-12_1.36x1.86mm_Layout3x4_P0.5mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Texas_MicroStar_Junior_BGA-12_4x3_2.0x2.5mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/txb0104.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 2.00,       # body overall length
        E = 2.50,       # body overall width
        A1 = 0.20,  	# body-board separation
        A = 0.36,  		# body  overall height
        b = 0.30,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 3,  		# number of pins along X axis (width)
        npy = 4,  		# number of pins along y axis (length)
        excluded_pins = ("None",), #pins to exclude -> None or "internals"
        old_modelName = 'Texas_MicroStar_Junior_BGA-12_4x3_2.0x2.5mm_Pitch0.5mm', #old_modelName
        modelName = 'Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Texas_Junior_DSBGA-48': Params( # from http://www.ti.com/lit/ml/mpbg309/mpbg309.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 4.00,       # body overall length
        E = 4.00,       # body overall width
        A1 = 0.20,  	# body-board separation
        A = 0.74,  		# body  overall height
        b = 0.30,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 7,  		# number of pins along X axis (width)
        npy = 7,  		# number of pins along y axis (length)
        excluded_pins = ("none", 17), #pins to exclude -> None or "internals"
        old_modelName = 'Texas_Junior_DSBGA-48', #old_modelName
        modelName = 'Texas_Junior_DSBGA-48_4.0x4.0mm_Layout7x7_P0.5mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
}

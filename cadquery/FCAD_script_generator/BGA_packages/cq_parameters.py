#!/usr/bin/python
# -*- coding: utf-8 -*-
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
    'e',    # pin (center-to-center) distance along x and y axis unless e1 is present
    'ex',   # pin (center-to-center) distance along x-axis, if this parameter is not present, then e is used
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
#        ex = 0.4,  # pin (center-to-center) distance along x-axis, if this parameter is not present, then e is used
#        sp = 0.0, #seating plane (pcb penetration)
#        npx = 8,  # number of pins along X axis (width)
#        npy = 6,  # number of pins along y axis (length)
#        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
#        old_modelName = 'BGA-48', #old_modelName
#        modelName = '',
#        rotation = -90, # rotation if required
#        dest_dir_prefix = '',
#        ),
    'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.4mm': Params( # from http://www.fujitsu.com/global/documents/products/devices/semiconductor/fram/lineup/MB85RS1MT-DS501-00022-7v0-E.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.04,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 3.09,       # body overall length
        E = 2.28,       # body overall width
        A1 = 0.08,      # body-board separation
        A = 0.25,       # body  overall height
        b = 0.20,       # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.3,        # pin (center-to-center) distance
        ex = 0.4,        # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 5,        # number of pins along X axis (width)
        npy = 3,        # number of pins along y axis (length)
        excluded_pins = (2, 4, 6, 8, 10, 12, 14), #pins to exclude -> None or "internals"
        old_modelName = 'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.4mm', #old_modelName
        modelName = 'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),

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
    'BGA-68_5.0x5.0mm_Layout9x9_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD': Params( # from https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/packaging/04r00344-01.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.20,  # body-board separation
        A = 1.05,  # body  overall height
        b = 0.3,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 9,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-68_5.0x5.0mm_Layout9x9_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD', #old_modelName
        modelName = 'BGA-68_5.0x5.0mm_Layout9x9_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-81_4.496x4.377mm_Layout9x9_P0.4mm_Ball0.25mm_Pad0.2mm_NSMD': Params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00478-01.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 4.496,       # body overall length
        E = 4.377,       # body overall width
        A1 = 0.13,  # body-board separation
        A = 0.46,  # body  overall height
        b = 0.25,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 9,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-81_4.496x4.377mm_Layout9x9_P0.4mm_Ball0.25mm_Pad0.2mm_NSMD', #old_modelName
        modelName = 'BGA-81_4.496x4.377mm_Layout9x9_P0.4mm_Ball0.25mm_Pad0.2mm_NSMD',
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
    'BGA-100_6.0x6.0mm_Layout11x11_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD': Params( # from https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/packaging/04r00345-01.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 6.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.20,  # body-board separation
        A = 1.05,  # body  overall height
        b = 0.3,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-100_6.0x6.0mm_Layout11x11_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD', #old_modelName
        modelName = 'BGA-100_6.0x6.0mm_Layout11x11_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD',
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
    'BGA-100_11.0x11.0mm_Layout10x10_P1.0mm_Ball0.5mm_Pad0.4mm_NSMD': Params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00223-02.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 11.0,       # body overall length
        E = 11.0,       # body overall width
        A1 = 0.40,  # body-board separation
        A = 1.4,  # body  overall height
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-100_11.0x11.0mm_Layout10x10_P1.0mm_Ball0.5mm_Pad0.4mm_NSMDm', #old_modelName
        modelName = 'BGA-100_11.0x11.0mm_Layout10x10_P1.0mm_Ball0.5mm_Pad0.4mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-121_9.0x9.0mm_Layout11x11_P0.8mm': Params( # from http://cds.linear.com/docs/en/packaging/05081891_A_bga121.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D =  9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.15,  # body-board separation
        A = 1.10,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-121_9.0x9.0mm_Layout11x11_P0.8mm', #old_modelName
        modelName = 'BGA-121_9.0x9.0mm_Layout11x11_P0.8mm',
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
    'BGA-144_7.0x7.0mm_Layout13x13_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD': Params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00346-00.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.0,       # body overall length
        E = 7.0,       # body overall width
        A1 = 0.2,  # body-board separation
        A = 1.05,  # body  overall height
        b = 0.3,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.50,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-144_7.0x7.0mm_Layout13x13_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD', #old_modelName
        modelName = 'BGA-144_7.0x7.0mm_Layout13x13_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD',
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
    'BGA-169_11.0x11.0mm_Layout13x13_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD': Params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00470-01.pdf
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 11.0,       # body overall length
        E = 11.0,       # body overall width
        A1 = 0.4,  # body-board separation
        A = 1.40,  # body  overall height
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-169_11.0x11.0mm_Layout13x13_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD', #old_modelName
        modelName = 'BGA-169_11.0x11.0mm_Layout13x13_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-256_11.0x11.0mm_Layout20x20_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD': Params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00348-01.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 11.0,       # body overall length
        E = 11.0,       # body overall width
        A1 = 0.3,  # body-board separation
        A = 1.05,  # body overall height
        b = 0.3,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.50,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-256_11.0x11.0mm_Layout20x20_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD', #old_modelName
        modelName = 'BGA-256_11.0x11.0mm_Layout20x20_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-256_14.0x14.0mm_Layout16x16_P0.8mm_Ball0.45mm_Pad0.32mm_NSMD': Params( # from https://www.xilinx.com/support/documentation/package_specs/ft256.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 14.0,       # body overall length
        E = 14.0,       # body overall width
        A1 = 0.4,  # body-board separation
        A = 1.40,  # body overall height
        b = 0.45,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.80,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-256_14.0x14.0mm_Layout16x16_P0.8mm_Ball0.45mm_Pad0.32mm_NSMD', #old_modelName
        modelName = 'BGA-256_14.0x14.0mm_Layout16x16_P0.8mm_Ball0.45mm_Pad0.32mm_NSMD',
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
    'BGA-324_15.0x15.0mm_Layout18x18_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD': Params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00474-02.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 15.0,       # body overall length
        E = 15.0,       # body overall width
        A1 = 0.4,  # body-board separation
        A = 1.40,  # body overall height
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.80,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 18,  # number of pins along X axis (width)
        npy = 18,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-324_15.0x15.0mm_Layout18x18_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD', #old_modelName
        modelName = 'BGA-324_15.0x15.0mm_Layout18x18_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-324_19.0x19.0mm_Layout18x18_P1.0mm_Ball0.5mm_Pad0.4mm_NSMD': Params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00474-02.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 19.0,       # body overall length
        E = 19.0,       # body overall width
        A1 = 0.5,  # body-board separation
        A = 1.75,  # body overall height
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.00,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 18,  # number of pins along X axis (width)
        npy = 18,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'BGA-324_19.0x19.0mm_Layout18x18_P1.0mm_Ball0.5mm_Pad0.4mm_NSMD', #old_modelName
        modelName = 'BGA-324_19.0x19.0mm_Layout18x18_P1.0mm_Ball0.5mm_Pad0.4mm_NSMD',
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
    'BGA-624_25x25_21.0x21.0mm_Pitch0.8mm': Params( # from https://www.nxp.com/docs/en/package-information/SOT1529-1.pdf
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 21.0,       # body overall length
        E = 21.0,       # body overall width
        A1 = 0.40,  # body-board separation
        A  = 1.6,  # body  overall height
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        excluded_pins = ("internals",1), #"internals", #pins to exclude -> None or "internals"
        old_modelName = 'BGA-624_25x25_21.0x21.0mm_Pitch0.8mm', #old_modelName
        modelName = 'BGA-624_21.0x21.0mm_Layout25x25_P0.8mm',
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
    'LFBGA-100_10x10mm_Layout10x10_P0.8mm': Params( # from http://www.st.com/resource/en/datasheet/stm32f103tb.pdf page 87
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 10.0,       # body overall length
        E = 10.0,       # body overall width
        A1 = 0.27,  # body-board separation
        A = 1.7,  # body  overall height
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'LFBGA-100_10x10mm_Layout10x10_P0.8mm', #old_modelName
        modelName = 'LFBGA-100_10x10mm_Layout10x10_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'LFBGA-144_10x10mm_Layout12x12_P0.8mm': Params( # from http://www.st.com/resource/en/datasheet/stm32f103ze.pdf page 114
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 10.0,       # body overall length
        E = 10.0,       # body overall width
        A1 = 0.3,  # body-board separation
        A = 1.7,  # body  overall height
        b = 0.4,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'LFBGA-144_10x10mm_Layout12x12_P0.8mm', #old_modelName
        modelName = 'LFBGA-144_10x10mm_Layout12x12_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Linear_BGA-133_15.0x15.0_Layout12x12_P1.27mm': Params( # from https://www.analog.com/media/en/technical-documentation/data-sheets/4637fc.pdf page 28
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 15.0,       # body overall length
        E = 15.0,       # body overall width
        A1 = 0.6,  # body-board separation
        A = 4.92,  # body  overall height
        b = 0.75,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.27,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'Linear_BGA-133_15.0x15.0_Layout12x12_P1.27mm', #old_modelName
        modelName = 'Linear_BGA-133_15.0x15.0_Layout12x12_P1.27mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Texas_DSBGA-10_1.36x1.86mm_Layout3x4_P0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/txs0104e.pdf page 29
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.86,       # body overall length
        E = 1.36,       # body overall width
        A1 = 0.17,  	# body-board separation
        A = 0.625,  	# body  overall height
        b = 0.23,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 4,  		# number of pins along X axis (width)
        npy = 3,  		# number of pins along y axis (length)
        excluded_pins = ("None",), #pins to exclude -> None or "internals"
        old_modelName = 'Texas_DSBGA-10_1.36x1.86mm_Layout3x4_P0.5mm', #old_modelName
        modelName = 'Texas_DSBGA-10_1.36x1.86mm_Layout3x4_P0.5mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm': Params( # from http://www.ti.com/lit/ds/symlink/msp430f2234.pdf page 90
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 3.33,       # body overall length
        E = 3.488,       # body overall width
        A1 = 0.05,  	# body-board separation
        A = 0.625,  	# body  overall height
        b = 0.25,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 7,  		# number of pins along X axis (width)
        npy = 7,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm', #old_modelName
        modelName = 'Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm', #old_modelName
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
    'Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/tlv320aic23b.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 5.00,       # body overall length
        E = 5.00,       # body overall width
        A1 = 0.20,  	# body-board separation
        A = 1.00,  		# body  overall height
        b = 0.30,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 9,  		# number of pins along X axis (width)
        npy = 9,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm', #old_modelName
        modelName = 'Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm': Params( # from http://www.ti.com/lit/ml/mpbg674/mpbg674.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.00,       # body overall length
        E = 7.00,       # body overall width
        A1 = 0.20,  	# body-board separation
        A = 1.00,  		# body  overall height
        b = 0.30,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 12,  		# number of pins along X axis (width)
        npy = 12,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm', #old_modelName
        modelName = 'Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm', #old_modelName
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
    'TFBGA-64_5x5mm_Layout8x8_P0.5mm': Params( # from http://www.st.com/resource/en/datasheet/stm32f100v8.pdf page 83
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 5.00,      # body overall length
        E = 5.00,      # body overall width
        A1 = 0.15,  	# body-board separation
        A = 1.20,  		# body  overall height
        b = 0.30,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 8,  		# number of pins along X axis (width)
        npy = 8,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'TFBGA-64_5x5mm_Layout8x8_P0.5mm', #old_modelName
        modelName = 'TFBGA-64_5x5mm_Layout8x8_P0.5mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TFBGA-100_8x8mm_Layout10x10_P0.8mm': Params( # from http://www.st.com/resource/en/datasheet/stm32f746zg.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 8.00,      # body overall length
        E = 8.00,      # body overall width
        A1 = 0.15,  	# body-board separation
        A = 1.10,  		# body  overall height
        b = 0.40,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 10,  		# number of pins along X axis (width)
        npy = 10,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'TFBGA-100_8x8mm_Layout10x10_P0.8mm', #old_modelName
        modelName = 'TFBGA-100_8x8mm_Layout10x10_P0.8mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TFBGA-100_9.0x9.0mm_Layout10x10_P0.8mm': Params( # from 
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 9.00,      # body overall length
        E = 9.00,      # body overall width
        A1 = 0.15,  	# body-board separation
        A = 1.10,  		# body  overall height
        b = 0.40,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 10,  		# number of pins along X axis (width)
        npy = 10,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'TFBGA-100_9.0x9.0mm_Layout10x10_P0.8mm', #old_modelName
        modelName = 'TFBGA-100_9.0x9.0mm_Layout10x10_P0.8mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TFBGA-121_10x10mm_Layout11x11_P0.8mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#p495 
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 10.00,      # body overall length
        E = 10.00,      # body overall width
        A1 = 0.30,  	# body-board separation
        A = 1.10,  		# body  overall height
        b = 0.40,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 11,  		# number of pins along X axis (width)
        npy = 11,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'TFBGA-121_10x10mm_Layout11x11_P0.8mm', #old_modelName
        modelName = 'TFBGA-121_10x10mm_Layout11x11_P0.8mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TFBGA-216_13x13mm_Layout15x15_P0.8mm': Params( # from http://www.st.com/resource/en/datasheet/stm32f746zg.pdf page 219
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 13.00,      # body overall length
        E = 13.00,      # body overall width
        A1 = 0.15,  	# body-board separation
        A = 1.10,  		# body  overall height
        b = 0.40,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 15,  		# number of pins along X axis (width)
        npy = 15,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'TFBGA-216_13x13mm_Layout15x15_P0.8mm', #old_modelName
        modelName = 'TFBGA-216_13x13mm_Layout15x15_P0.8mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TFBGA-265_14x14mm_Layout17x17_P0.8mm': Params( # from
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 14.00,      # body overall length
        E = 14.00,      # body overall width
        A1 = 0.15,  	# body-board separation
        A = 1.10,  		# body  overall height
        b = 0.40,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 17,  		# number of pins along X axis (width)
        npy = 17,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'TFBGA-265_14x14mm_Layout17x17_P0.8mm', #old_modelName
        modelName = 'TFBGA-265_14x14mm_Layout17x17_P0.8mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TFBGA-636_19.0x19.0mm_Layout28x28_P0.65mm': Params( # from
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.01,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, 		# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 19.00,      # body overall length
        E = 19.00,      # body overall width
        A1 = 0.15,  	# body-board separation
        A = 1.10,  		# body  overall height
        b = 0.40,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.65,  		# pin (center-to-center) distance
        sp = 0.0, 		# seating plane (pcb penetration)
        npx = 28,  		# number of pins along X axis (width)
        npy = 28,  		# number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        old_modelName = 'TFBGA-636_19.0x19.0mm_Layout28x28_P0.65mm', #old_modelName
        modelName = 'TFBGA-636_19.0x19.0mm_Layout28x28_P0.65mm', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'FBGA-78_7.5x11mm_Layout2x3x13_P0.8mm': Params( # from https://www.skhynix.com/product/filedata/fileDownload.do?seq=7687
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 11.0,       # body overall length
        E = 7.5,       # body overall width
        A1 = 0.34,  # body-board separation
        A = 1.1,  # body  overall height
        b = 0.45,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 13,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        excluded_pins = ("none", 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78), #pins to exclude -> None or "internals"
        old_modelName = 'FBGA-78_2x3x13_7.5x11.0mm_Pitch0.8mm', #old_modelName
        modelName = 'FBGA-78_7.5x11mm_Layout2x3x13_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'ucBGA-49_3x3mm_Layout7x7_P0.4mm': Params( #https://www.latticesemi.com/view_document?document_id=213
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.2,  # body-board separation
        A = 1.0,  # body  overall height
        b = 0.25,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 7,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        excluded_pins = (None), #pins to exclude -> None or "internals"
        old_modelName = 'ucBGA-49_3x3mm_Layout7x7_P0.4mm', #old_modelName
        modelName = 'ucBGA-49_3x3mm_Layout7x7_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'ucBGA-36_2.5x2.5mm_Layout6x6_P0.4mm': Params( #https://www.latticesemi.com/view_document?document_id=213
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 2.5,       # body overall length
        E = 2.5,       # body overall width
        A1 = 0.2,  # body-board separation
        A = 1.0,  # body  overall height
        b = 0.25,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        excluded_pins = (None), #pins to exclude -> None or "internals"
        old_modelName = 'ucBGA-36_2.5x2.5mm_Layout6x6_P0.4mm', #old_modelName
        modelName = 'ucBGA-36_2.5x2.5mm_Layout6x6_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'WLP-4_0.83x0.83mm_P0.4mm': Params( #https://pdfserv.maximintegrated.com/package_dwgs/21-100107.PDF
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.02,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 0.828,      # body overall length
        E = 0.828,      # body overall width
        A1 = 0.19,      # body-board separation
        A = 0.5,        # body  overall height
        b = 0.27,       # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,        # pin (center-to-center) distance
        sp = 0.0,       #seating plane (pcb penetration)
        npx = 2,        # number of pins along X axis (width)
        npy = 2,        # number of pins along y axis (length)
        excluded_pins = (None), #pins to exclude -> None or "internals"
        old_modelName = 'WLP-4_0.83x0.83mm_P0.4mm', #old_modelName
        modelName = 'WLP-4_0.83x0.83mm_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'WLP-4_0.86x0.86mm_P0.4mm': Params( #https://pdfserv.maximintegrated.com/package_dwgs/21-0612.PDF
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.02,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 0.835,      # body overall length
        E = 0.835,      # body overall width
        A1 = 0.19,      # body-board separation
        A = 0.5,        # body  overall height
        b = 0.27,       # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,        # pin (center-to-center) distance
        sp = 0.0,       #seating plane (pcb penetration)
        npx = 2,        # number of pins along X axis (width)
        npy = 2,        # number of pins along y axis (length)
        excluded_pins = (None), #pins to exclude -> None or "internals"
        old_modelName = 'WLP-4_0.86x0.86mm_P0.4mm', #old_modelName
        modelName = 'WLP-4_0.86x0.86mm_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-153_8.0x8.0mm_Layout15x15_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD': Params(
        #
        # Altera MBGA-153, https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00471-00.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is BGA-153_8.0x8.0mm_Layout15x15_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.3,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 15,      # number of pins along X axis (width)
        npy = 15,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'BGA-153_8.0x8.0mm_Layout15x15_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD', # Old_modelName
        modelName = 'BGA-153_8.0x8.0mm_Layout15x15_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'BGA-36_3.396x3.466mm_Layout6x6_P0.4mm_Ball0.25mm_Pad0.2mm_NSMD': Params(
        #
        # Altera V36, https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00486-00.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is BGA-36_3.396x3.466mm_Layout6x6_P0.4mm_Ball0.25mm_Pad0.2mm_NSMD.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 3.466,      # body overall length
        E = 3.396,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'BGA-36_3.396x3.466mm_Layout6x6_P0.4mm_Ball0.25mm_Pad0.2mm_NSMD', # Old_modelName
        modelName = 'BGA-36_3.396x3.466mm_Layout6x6_P0.4mm_Ball0.25mm_Pad0.2mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'BGA-672_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD': Params(
        #
        # Altera BGA-672, https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00472-00.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is BGA-672_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 27.0,      # body overall length
        E = 27.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.6,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 26,      # number of pins along X axis (width)
        npy = 26,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'BGA-672_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD', # Old_modelName
        modelName = 'BGA-672_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'BGA-676_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD': Params(
        #
        # XILINX BGA-676, https://www.xilinx.com/support/documentation/package_specs/fg676.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is BGA-676_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 27.0,      # body overall length
        E = 27.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.6,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 26,      # number of pins along X axis (width)
        npy = 26,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'BGA-676_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD', # Old_modelName
        modelName = 'BGA-676_27.0x27.0mm_Layout26x26_P1.0mm_Ball0.6mm_Pad0.5mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm': Params(
        #
        # Texas Instruments, DSBGA, 3.415x3.535x0.625mm, 64 ball 8x8 area grid, NSMD pad definition (http://www.ti.com/lit/ds/slas718g/slas718g.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 3.535,      # body overall length
        E = 3.415,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.2,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm', # Old_modelName
        modelName = 'Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm': Params(
        #
        # Texas Instruments, DSBGA, 0.9x1.4mm, 6 bump 2x3 (perimeter) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/ts5a3159a.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.1,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.4,      # body overall length
        E = 0.94,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 3,      # number of pins along X axis (width)
        npy = 2,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm', # Old_modelName
        modelName = 'Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm': Params(
        #
        # Texas Instruments, DSBGA, 1.43x1.41mm, 8 bump 3x3 (perimeter) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/lmc555.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.1,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.43,      # body overall length
        E = 1.41,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 3,      # number of pins along X axis (width)
        npy = 3,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm', # Old_modelName
        modelName = 'Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'Texas_DSBGA-9_1.4715x1.4715mm_Layout3x3_P0.5mm': Params(
        #
        # Texas Instruments, DSBGA, 1.4715x1.4715mm, 9 bump 3x3 array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/lm4990.pdf, http://www.ti.com/lit/an/snva009ag/snva009ag.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is Texas_DSBGA-9_1.4715x1.4715mm_Layout3x3_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.1,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.4715,      # body overall length
        E = 1.4715,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 3,      # number of pins along X axis (width)
        npy = 3,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'Texas_DSBGA-9_1.4715x1.4715mm_Layout3x3_P0.5mm', # Old_modelName
        modelName = 'Texas_DSBGA-9_1.4715x1.4715mm_Layout3x3_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UCBGA-81_4x4mm_Layout9x9_P0.4mm': Params(
        #
        # UCBGA-81, 9x9 raster, 4x4mm package, pitch 0.4mm; https://www.latticesemi.com/view_document?document_id=213
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UCBGA-81_4x4mm_Layout9x9_P0.4mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.2,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 9,      # number of pins along X axis (width)
        npy = 9,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UCBGA-81_4x4mm_Layout9x9_P0.4mm', # Old_modelName
        modelName = 'UCBGA-81_4x4mm_Layout9x9_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-100_7x7mm_Layout12x12_P0.5mm': Params(
        #
        # UFBGA-100, 12x12 raster, 7x7mm package, pitch 0.5mm; see section 7.1 of http://www.st.com/resource/en/datasheet/stm32f103tb.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-100_7x7mm_Layout12x12_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-100_7x7mm_Layout12x12_P0.5mm', # Old_modelName
        modelName = 'UFBGA-100_7x7mm_Layout12x12_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-132_7x7mm_Layout12x12_P0.5mm': Params(
        #
        # UFBGA-132, 12x12 raster, 7x7mm package, pitch 0.5mm; see section 7.4 of http://www.st.com/resource/en/datasheet/stm32l152zc.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-132_7x7mm_Layout12x12_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-132_7x7mm_Layout12x12_P0.5mm', # Old_modelName
        modelName = 'UFBGA-132_7x7mm_Layout12x12_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-132_7x7mm_P0.5mm': Params(
        #
        # UFBGA 132 Pins, 0.5mm Pitch, 0.3mm Ball, http://www.st.com/resource/en/datasheet/stm32l486qg.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-132_7x7mm_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 11,      # number of pins along X axis (width)
        npy = 11,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-132_7x7mm_P0.5mm', # Old_modelName
        modelName = 'UFBGA-132_7x7mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-144_10x10mm_Layout12x12_P0.8mm': Params(
        #
        # UFBGA-144, 12x12 raster, 10x10mm package, pitch 0.8mm; see section 7.5 of http://www.st.com/resource/en/datasheet/stm32f446ze.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-144_10x10mm_Layout12x12_P0.8mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 10.0,      # body overall length
        E = 10.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.4,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.8,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-144_10x10mm_Layout12x12_P0.8mm', # Old_modelName
        modelName = 'UFBGA-144_10x10mm_Layout12x12_P0.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-144_7x7mm_Layout12x12_P0.5mm': Params(
        #
        # UFBGA-144, 12x12 raster, 7x7mm package, pitch 0.5mm; see section 7.4 of http://www.st.com/resource/en/datasheet/stm32f446ze.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-144_7x7mm_Layout12x12_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-144_7x7mm_Layout12x12_P0.5mm', # Old_modelName
        modelName = 'UFBGA-144_7x7mm_Layout12x12_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm': Params(
        #
        # UFBGA-15, 4x4, 3x3mm package, pitch 0.65mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.325,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.65,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm', # Old_modelName
        modelName = 'UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-169_7x7mm_Layout13x13_P0.5mm': Params(
        #
        # UFBGA-169, 13x13 raster, 7x7mm package, pitch 0.5mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32f429ng.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-169_7x7mm_Layout13x13_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 13,      # number of pins along X axis (width)
        npy = 13,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-169_7x7mm_Layout13x13_P0.5mm', # Old_modelName
        modelName = 'UFBGA-169_7x7mm_Layout13x13_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-201_10x10mm_Layout15x15_P0.65mm': Params(
        #
        # UFBGA-201, 15x15 raster, 10x10mm package, pitch 0.65mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32f207vg.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-201_10x10mm_Layout15x15_P0.65mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 10.0,      # body overall length
        E = 10.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.325,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.65,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 15,      # number of pins along X axis (width)
        npy = 15,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-201_10x10mm_Layout15x15_P0.65mm', # Old_modelName
        modelName = 'UFBGA-201_10x10mm_Layout15x15_P0.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm': Params(
        #
        # UFBGA-32, 6x6, 4x4mm package, pitch 0.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm', # Old_modelName
        modelName = 'UFBGA-32_4.0x4.0mm_Layout6x6_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'UFBGA-64_5x5mm_Layout8x8_P0.5mm': Params(
        #
        # UFBGA-64, 8x8 raster, 5x5mm package, pitch 0.5mm; see section 7.1 of http://www.st.com/resource/en/datasheet/stm32f051t8.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is UFBGA-64_5x5mm_Layout8x8_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'UFBGA-64_5x5mm_Layout8x8_P0.5mm', # Old_modelName
        modelName = 'UFBGA-64_5x5mm_Layout8x8_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm': Params(
        #
        # VFBGA-100, 10x10, 7x7mm package, pitch 0.65mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.325,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.65,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 10,      # number of pins along X axis (width)
        npy = 10,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm', # Old_modelName
        modelName = 'VFBGA-100_7.0x7.0mm_Layout10x10_P0.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm': Params(
        #
        # VFBGA-49, 7x7, 5x5mm package, pitch 0.65mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.325,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.65,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 7,      # number of pins along X axis (width)
        npy = 7,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm', # Old_modelName
        modelName = 'VFBGA-49_5.0x5.0mm_Layout7x7_P0.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'XFBGA-121_8x8mm_Layout11x11_P0.65mm': Params(
        #
        # XFBGA-121, https://www.nxp.com/docs/en/package-information/SOT1533-1.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is XFBGA-121_8x8mm_Layout11x11_P0.65mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.325,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.65,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 11,      # number of pins along X axis (width)
        npy = 11,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'XFBGA-121_8x8mm_Layout11x11_P0.65mm', # Old_modelName
        modelName = 'XFBGA-121_8x8mm_Layout11x11_P0.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm': Params(
        #
        # XFBGA-36, https://www.nxp.com/docs/en/package-information/SOT1555-1.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 3.5,      # body overall length
        E = 3.5,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm', # Old_modelName
        modelName = 'XFBGA-36_3.5x3.5mm_Layout6x6_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

    'XFBGA-64_5.0x5.0mm_Layout8x8_P0.5mm': Params(
        #
        # XFBGA-64, https://www.nxp.com/docs/en/package-information/SOT1555-1.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is XFBGA-64_5.0x5.0mm_Layout8x8_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        sp = 0.0,       # seating plane (pcb penetration)
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        old_modelName = 'XFBGA-64_5.0x5.0mm_Layout8x8_P0.5mm', # Old_modelName
        modelName = 'XFBGA-64_5.0x5.0mm_Layout8x8_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_BGA.3dshapes',
        ),

}

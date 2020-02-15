# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MO-153G document.

## file of parametric definitions

from Params import *

class SeriesParams():
    footprint_dir="Package_TSSOP.pretty"
    lib_name = "Package_TSSOP"

    body_color_key = "black body"
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"


part_params = {
    'TSSOP-30_6.1x9.7mm_P0.65mm': Params(
        #
        # TSSOP, 30 Pin (JEDEC MO-153 Var DB-1 https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-30_6.1x9.7mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 15,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-30_6.1x9.7mm_P0.65mm',            # modelName
        modelName = 'TSSOP-30_6.1x9.7mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-44_4.4x11mm_P0.5mm': Params(
        #
        # TSSOP, 44 Pin (JEDEC MO-153 Var BE https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-44_4.4x11mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 22,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-44_4.4x11mm_P0.5mm',            # modelName
        modelName = 'TSSOP-44_4.4x11mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-40_8x14mm_P0.65mm': Params(
        #
        # TSSOP, 40 Pin (JEDEC MO-153 Var GD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-40_8x14mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-40_8x14mm_P0.65mm',            # modelName
        modelName = 'TSSOP-40_8x14mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-52_8x11mm_P0.4mm': Params(
        #
        # TSSOP, 52 Pin (JEDEC MO-153 Var JB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-52_8x11mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 26,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-52_8x11mm_P0.4mm',            # modelName
        modelName = 'TSSOP-52_8x11mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-28_6.1x7.8mm_P0.5mm': Params(
        #
        # TSSOP, 28 Pin (JEDEC MO-153 Var EA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-28_6.1x7.8mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.8,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-28_6.1x7.8mm_P0.5mm',            # modelName
        modelName = 'TSSOP-28_6.1x7.8mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-50_4.4x12.5mm_P0.5mm': Params(
        #
        # TSSOP, 50 Pin (JEDEC MO-153 Var BF https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-50_4.4x12.5mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 25,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-50_4.4x12.5mm_P0.5mm',            # modelName
        modelName = 'TSSOP-50_4.4x12.5mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-28_8x9.7mm_P0.65mm': Params(
        #
        # TSSOP, 28 Pin (JEDEC MO-153 Var GA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-28_8x9.7mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-28_8x9.7mm_P0.65mm',            # modelName
        modelName = 'TSSOP-28_8x9.7mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-32_8x11mm_P0.65mm': Params(
        #
        # TSSOP, 32 Pin (JEDEC MO-153 Var GB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-32_8x11mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-32_8x11mm_P0.65mm',            # modelName
        modelName = 'TSSOP-32_8x11mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-56_8x14mm_P0.5mm': Params(
        #
        # TSSOP, 56 Pin (JEDEC MO-153 Var HD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-56_8x14mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 28,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-56_8x14mm_P0.5mm',            # modelName
        modelName = 'TSSOP-56_8x14mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),


    'TSSOP-36_4.4x7.8mm_P0.4mm': Params(
        #
        # TSSOP, 36 Pin (JEDEC MO-153 Var CC https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-36_4.4x7.8mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.8,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-36_4.4x7.8mm_P0.4mm',            # modelName
        modelName = 'TSSOP-36_4.4x7.8mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-36_8x9.7mm_P0.5mm': Params(
        #
        # TSSOP, 36 Pin (JEDEC MO-153 Var HA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-36_8x9.7mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-36_8x9.7mm_P0.5mm',            # modelName
        modelName = 'TSSOP-36_8x9.7mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-28_6.1x9.7mm_P0.65mm': Params(
        #
        # TSSOP, 28 Pin (JEDEC MO-153 Var DB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-28_6.1x9.7mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-28_6.1x9.7mm_P0.65mm',            # modelName
        modelName = 'TSSOP-28_6.1x9.7mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-36_4.4x9.7mm_P0.5mm': Params(
        #
        # TSSOP, 36 Pin (JEDEC MO-153 Var BD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-36_4.4x9.7mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-36_4.4x9.7mm_P0.5mm',            # modelName
        modelName = 'TSSOP-36_4.4x9.7mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-56_8x12.5mm_P0.4mm': Params(
        #
        # TSSOP, 56 Pin (JEDEC MO-153 Var JC https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-56_8x12.5mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 28,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-56_8x12.5mm_P0.4mm',            # modelName
        modelName = 'TSSOP-56_8x12.5mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-24_6.1x7.8mm_P0.65mm': Params(
        #
        # TSSOP, 24 Pin (JEDEC MO-153 Var DA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-24_6.1x7.8mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.8,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-24_6.1x7.8mm_P0.65mm',            # modelName
        modelName = 'TSSOP-24_6.1x7.8mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-52_6.1x11mm_P0.4mm': Params(
        #
        # TSSOP, 52 Pin (JEDEC MO-153 Var FC https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-52_6.1x11mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 26,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-52_6.1x11mm_P0.4mm',            # modelName
        modelName = 'TSSOP-52_6.1x11mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-60_8x12.5mm_P0.4mm': Params(
        #
        # TSSOP, 60 Pin (JEDEC MO-153 Var JC-1 https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-60_8x12.5mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 30,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-60_8x12.5mm_P0.4mm',            # modelName
        modelName = 'TSSOP-60_8x12.5mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-64_6.1x14mm_P0.4mm': Params(
        #
        # TSSOP, 64 Pin (JEDEC MO-153 Var FE https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-64_6.1x14mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 32,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-64_6.1x14mm_P0.4mm',            # modelName
        modelName = 'TSSOP-64_6.1x14mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-40_8x11mm_P0.5mm': Params(
        #
        # TSSOP, 40 Pin (JEDEC MO-153 Var HB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-40_8x11mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-40_8x11mm_P0.5mm',            # modelName
        modelName = 'TSSOP-40_8x11mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-36_6.1x7.8mm_P0.4mm': Params(
        #
        # TSSOP, 36 Pin (JEDEC MO-153 Var FA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-36_6.1x7.8mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.8,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-36_6.1x7.8mm_P0.4mm',            # modelName
        modelName = 'TSSOP-36_6.1x7.8mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-48_8x9.7mm_P0.4mm': Params(
        #
        # TSSOP, 48 Pin (JEDEC MO-153 Var JA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-48_8x9.7mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 24,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-48_8x9.7mm_P0.4mm',            # modelName
        modelName = 'TSSOP-48_8x9.7mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-80_6.1x17mm_P0.4mm': Params(
        #
        # TSSOP, 80 Pin (JEDEC MO-153 Var FF https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-80_6.1x17mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 17.0,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 40,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-80_6.1x17mm_P0.4mm',            # modelName
        modelName = 'TSSOP-80_6.1x17mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-36_6.1x9.7mm_P0.5mm': Params(
        #
        # TSSOP, 36 Pin (JEDEC MO-153 Var EB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-36_6.1x9.7mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-36_6.1x9.7mm_P0.5mm',            # modelName
        modelName = 'TSSOP-36_6.1x9.7mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-48_8x12.5mm_P0.5mm': Params(
        #
        # TSSOP, 48 Pin (JEDEC MO-153 Var HC https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-48_8x12.5mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 24,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-48_8x12.5mm_P0.5mm',            # modelName
        modelName = 'TSSOP-48_8x12.5mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-40_6.1x14mm_P0.65mm': Params(
        #
        # TSSOP, 40 Pin (JEDEC MO-153 Var DE https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-40_6.1x14mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-40_6.1x14mm_P0.65mm',            # modelName
        modelName = 'TSSOP-40_6.1x14mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-64_6.1x17mm_P0.5mm': Params(
        #
        # TSSOP, 64 Pin (JEDEC MO-153 Var EF https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-64_6.1x17mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 17.0,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 32,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-64_6.1x17mm_P0.5mm',            # modelName
        modelName = 'TSSOP-64_6.1x17mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-40_6.1x11mm_P0.5mm': Params(
        #
        # TSSOP, 40 Pin (JEDEC MO-153 Var EC https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-40_6.1x11mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-40_6.1x11mm_P0.5mm',            # modelName
        modelName = 'TSSOP-40_6.1x11mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-44_6.1x11mm_P0.5mm': Params(
        #
        # TSSOP, 44 Pin (JEDEC MO-153 Var EC-1 https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-44_6.1x11mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 22,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-44_6.1x11mm_P0.5mm',            # modelName
        modelName = 'TSSOP-44_6.1x11mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-32_4.4x6.5mm_P0.4mm': Params(
        #
        # TSSOP, 32 Pin (JEDEC MO-153 Var CB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-32_4.4x6.5mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-32_4.4x6.5mm_P0.4mm',            # modelName
        modelName = 'TSSOP-32_4.4x6.5mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-64_8x14mm_P0.4mm': Params(
        #
        # TSSOP, 64 Pin (JEDEC MO-153 Var JD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-64_8x14mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 32,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-64_8x14mm_P0.4mm',            # modelName
        modelName = 'TSSOP-64_8x14mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-28_4.4x7.8mm_P0.5mm': Params(
        #
        # TSSOP, 28 Pin (JEDEC MO-153 Var BC https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-28_4.4x7.8mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.8,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-28_4.4x7.8mm_P0.5mm',            # modelName
        modelName = 'TSSOP-28_4.4x7.8mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-48_4.4x9.7mm_P0.4mm': Params(
        #
        # TSSOP, 48 Pin (JEDEC MO-153 Var CD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-48_4.4x9.7mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 24,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-48_4.4x9.7mm_P0.4mm',            # modelName
        modelName = 'TSSOP-48_4.4x9.7mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-20_4.4x5mm_P0.5mm': Params(
        #
        # TSSOP, 20 Pin (JEDEC MO-153 Var BA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-20_4.4x5mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.0,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 10,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-20_4.4x5mm_P0.5mm',            # modelName
        modelName = 'TSSOP-20_4.4x5mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-36_6.1x12.5mm_P0.65mm': Params(
        #
        # TSSOP, 36 Pin (JEDEC MO-153 Var DD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-36_6.1x12.5mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-36_6.1x12.5mm_P0.65mm',            # modelName
        modelName = 'TSSOP-36_6.1x12.5mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-36_8x12.5mm_P0.65mm': Params(
        #
        # TSSOP, 36 Pin (JEDEC MO-153 Var GC https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-36_8x12.5mm_P0.65mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-36_8x12.5mm_P0.65mm',            # modelName
        modelName = 'TSSOP-36_8x12.5mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-24_4.4x5mm_P0.4mm': Params(
        #
        # TSSOP, 24 Pin (JEDEC MO-153 Var CA https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-24_4.4x5mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.0,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-24_4.4x5mm_P0.4mm',            # modelName
        modelName = 'TSSOP-24_4.4x5mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-24_4.4x6.5mm_P0.5mm': Params(
        #
        # TSSOP, 24 Pin (JEDEC MO-153 Var BB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-24_4.4x6.5mm_P0.5mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,         # body length
        E1 = 4.4,         # body width
        E = 6.4,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-24_4.4x6.5mm_P0.5mm',            # modelName
        modelName = 'TSSOP-24_4.4x6.5mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-48_6.1x9.7mm_P0.4mm': Params(
        #
        # TSSOP, 48 Pin (JEDEC MO-153 Var FB https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-48_6.1x9.7mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 24,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-48_6.1x9.7mm_P0.4mm',            # modelName
        modelName = 'TSSOP-48_6.1x9.7mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-56_6.1x12.5mm_P0.4mm': Params(
        #
        # TSSOP, 56 Pin (JEDEC MO-153 Var FD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-56_6.1x12.5mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 6.1,         # body width
        E = 8.1,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 28,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-56_6.1x12.5mm_P0.4mm',            # modelName
        modelName = 'TSSOP-56_6.1x12.5mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),

    'TSSOP-68_8x14mm_P0.4mm': Params(
        #
        # TSSOP, 68 Pin (JEDEC MO-153 Var JD-1 https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is TSSOP-68_8x14mm_P0.4mm.kicad_mod
        #
        the = 9.0,         # body angle in degrees
        tb_s = 0.1,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 8.0,         # body width
        E = 10.0,          # body overall width
        A1 = 0.2,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 34,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-68_8x14mm_P0.4mm',            # modelName
        modelName = 'TSSOP-68_8x14mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
#        dest_dir_prefix = '../Package_SO.3dshapes',      # destination directory
        ),
}

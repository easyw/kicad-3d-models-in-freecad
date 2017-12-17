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

from Params import *

class SeriesParams():
    # footprint_dir="Housings_QFP.pretty"
    # lib_name = "Housings_QFP"

    footprint_dir="Package_QFP.pretty"
    lib_name = "Package_QFP"

    body_color_key = "black body"
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"

part_params = {
    'LQFP-32_5x5mm_Pitch0.5mm': Params(
    #from http://www.nxp.com/documents/outline_drawing/SOT401-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 5.0,       # body width
        E = 7.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 8,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-32_5x5mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-32_5x5mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-32-1EP_5x5mm_Pitch0.5mm': Params(
    #from http://www.nxp.com/documents/outline_drawing/SOT401-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 5.0,       # body width
        E = 7.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 8,   # number of pins along y axis (length)
        epad = (3.45,3.45), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-32-1EP_5x5mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-32-1EP_5x5mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-32_7x7mm_Pitch0.8mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT358-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 8,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-32_7x7mm_Pitch0.8mm', #modelName
        modelName = 'LQFP-32_7x7mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-36_7x7mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub_link/Collateral/561AV.PDF
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.7,  # body height
        b = 0.3,  # pin width
        e = 0.65,   # pin (center-to-center) distance
        npx = 9,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-36_7x7mm_Pitch0.65mm', #modelName
        modelName = 'LQFP-36_7x7mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-44_10x10mm_Pitch0.8mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT389-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.40,  # pin width
        e = 0.8,   # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-44_10x10mm_Pitch0.8mm', #modelName
        modelName = 'LQFP-44_10x10mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-48_7x7mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT313-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,   # pin (center-to-center) distance
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-48_7x7mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-48_7x7mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-52_10x10mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1671-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-52_10x10mm_Pitch0.65mm', #modelName
        modelName = 'LQFP-52_10x10mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-52-1EP_10x10mm_Pitch0.65mm': Params(
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = (4.8,4.8), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-52-1EP_10x10mm_Pitch0.65mm', #modelName
        modelName = 'LQFP-52-1EP_10x10mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-64_7x7mm_Pitch0.4mm': Params( # http://www.nxp.com/documents/outline_drawing/SOT414-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-64_7x7mm_Pitch0.4mm', #modelName
        modelName = 'LQFP-64_7x7mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-64_10x10mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT314-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-64_10x10mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-64_10x10mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-64-1EP_10x10mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT314-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (6.5,6.5), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-64-1EP_10x10mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-64-1EP_10x10mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-64_14x14mm_Pitch0.8mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT791-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.37,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-64_14x14mm_Pitch0.8mm', #modelName
        modelName = 'LQFP-64_14x14mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-80_12x12mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT315-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 14.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-80_12x12mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-80_12x12mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-100_14x14mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT407-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-100_14x14mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-100_14x14mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-128_14x14mm_Pitch0.4mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT315-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 32,  # number of pins along X axis (width)
        npy = 32,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-128_14x14mm_Pitch0.4mm', #modelName
        modelName = 'LQFP-128_14x14mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-128_14x20mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT425-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 38,  # number of pins along X axis (width)
        npy = 26,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-128_14x20mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-128_14x20mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-144_20x20mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT486-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-144_20x20mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-144_20x20mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-160_24x24mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT435-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 24.0,       # body length
        E1 = 24.0,       # body width
        E = 26.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 40,  # number of pins along X axis (width)
        npy = 40,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-160_24x24mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-160_24x24mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-176_20x20mm_Pitch0.4mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1017-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 44,  # number of pins along X axis (width)
        npy = 44,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-176_20x20mm_Pitch0.4mm', #modelName
        modelName = 'LQFP-176_20x20mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
         ),
    'LQFP-176_24x24mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT506-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 24.0,       # body length
        E1 = 24.0,       # body width
        E = 26.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 44,  # number of pins along X axis (width)
        npy = 44,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-176_24x24mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-176_24x24mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-208_28x28mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT459-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 28.0,       # body length
        E1 = 28.0,       # body width
        E = 30.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 52,  # number of pins along X axis (width)
        npy = 52,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-208_28x28mm_Pitch0.5mm', #modelName
        modelName = 'LQFP-208_28x28mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'LQFP-216_24x24mm_Pitch0.4mm': Params( # from https://www.renesas.com/en-in/package-image/pdf/outdrawing/p216gm-40-gby.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 24.0,       # body length
        E1 = 24.0,       # body width
        E = 26.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 54,  # number of pins along X axis (width)
        npy = 54,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'LQFP-216_24x24mm_Pitch0.4mm', #modelName
        modelName = 'LQFP-216_24x24mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'PQFP-80_14x20mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ds/symlink/tl16pir552.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.15, #0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.7,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.15, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 14.0,       # body width
        E = 17.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.7,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 24,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'PQFP-80_14x20mm_Pitch0.8mm', #modelName
        modelName = 'PQFP-80_14x20mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'PQFP-100_14x20mm_Pitch0.65mm': Params( # from http://pdf1.alldatasheet.com/datasheet-pdf/view/181852/STMICROELECTRONICS/PQFP100.html
        the = 8.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.7,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 14.0,       # body width
        E = 17.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.7,  # body height
        b = 0.31,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 30,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'PQFP-100_14x20mm_Pitch0.65mm', #modelName
        modelName = 'PQFP-100_14x20mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'PQFP-256_28x28mm_Pitch0.4mm': Params( # from http://www.topline.tv/drawings/pdf/qfp/QFP256T15.7-2.6.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.17,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.7,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.0, #0.45 chamfer of the 1st pin corner
        D1 = 28.0,       # body length
        E1 = 28.0,       # body width
        E = 30.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.5,  # body-board separation
        A2 = 3.5,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 64,  # number of pins along X axis (width)
        npy = 64,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'PQFP-256_28x28mm_Pitch0.4mm', #modelName
        modelName = 'PQFP-256_28x28mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-32_7x7mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ml/mpqf112/mpqf112.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.37,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 8,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-32_7x7mm_Pitch0.8mm', #modelName
        modelName = 'TQFP-32_7x7mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-44_10x10mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ml/mpqf075/mpqf075.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-44_10x10mm_Pitch0.8mm', #modelName
        modelName = 'TQFP-44_10x10mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-44-1EP_10x10mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ml/mpqf074c/mpqf074c.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (4.5,4.5), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-44-1EP_10x10mm_Pitch0.8mm', #modelName
        modelName = 'TQFP-44-1EP_10x10mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-48_7x7mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf019a/mtqf019a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-48_7x7mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-48_7x7mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-48-1EP_7x7mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf019a/mtqf019a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = (3.5,3.5), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-48-1EP_7x7mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-48-1EP_7x7mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-64_7x7mm_Pitch0.4mm': Params( # from http://www.ti.com/lit/ml/mpqf039a/mpqf039a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.16,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-64_7x7mm_Pitch0.4mm', #modelName
        modelName = 'TQFP-64_7x7mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-64_10x10mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf006a/mtqf006a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-64_10x10mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-64_10x10mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-64_1EP_10x10mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf006a/mtqf006a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (4.5,4.5), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-64_1EP_10x10mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-64_1EP_10x10mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'HTQFP-64_1EP_10x10mm_Pitch0.5mm_ThermalPad': Params( # from http://www.ti.com/lit/ml/mtqf006a/mtqf006a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (7.5,7.5), #None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'HTQFP-64_1EP_10x10mm_Pitch0.5mm_ThermalPad', #modelName
        modelName = 'HTQFP-64_1EP_10x10mm_P0.5mm_ThermalPad', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-64_14x14mm_Pitch0.8mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.37,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-64_14x14mm_Pitch0.8mm', #modelName
        modelName = 'TQFP-64_14x14mm_P0.8mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-80_12x12mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf009a/mtqf009a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 14.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-80_12x12mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-80_12x12mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-80_14x14mm_Pitch0.65mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-80_14x14mm_Pitch0.65mm', #modelName
        modelName = 'TQFP-80_14x14mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-100_12x12mm_Pitch0.4mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 14.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-100_12x12mm_Pitch0.4mm', #modelName
        modelName = 'TQFP-100_12x12mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-100_14x14mm_Pitch0.5mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-100_14x14mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-100_14x14mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-100_1EP_14x14mm_Pitch0.5mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = (7.5,7.5), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-100_1EP_14x14mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-100_1EP_14x14mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-120_14x14mm_Pitch0.4mm': Params( # from http://www.ti.com/lit/ml/mpqf012/mpqf012.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 30,  # number of pins along X axis (width)
        npy = 30,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-120_14x14mm_Pitch0.4mm', #modelName
        modelName = 'TQFP-120_14x14mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-128_14x14mm_Pitch0.4mm': Params( # from http://www.ti.com/lit/ml/mpqf013/mpqf013.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 32,  # number of pins along X axis (width)
        npy = 32,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-128_14x14mm_Pitch0.4mm', #modelName
        modelName = 'TQFP-128_14x14mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-144_16x16mm_Pitch0.4mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/70616g.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 16.0,       # body length
        E1 = 16.0,       # body width
        E = 18.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-144_16x16mm_Pitch0.4mm', #modelName
        modelName = 'TQFP-144_16x16mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TQFP-144_20x20mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mpqf082/mpqf082.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'TQFP-144_20x20mm_Pitch0.5mm', #modelName
        modelName = 'TQFP-144_20x20mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
}

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
    'LQFP-52_14x14mm_Pitch1mm': Params( # from http://www.holtek.com/documents/10179/116711/HT1632Cv170.pdf
        the = 12.0,  # body angle in degrees
        tb_s = 0.15,  # top part of body is that much smaller
        c = 0.1,  # pin thickness, body center part height
        R1 = 0.1,  # pin upper corner, inner radius
        R2 = 0.1,  # pin lower corner, inner radius
        S = 0.2,  # pin top flat part length (excluding corner arc)
        # L = 0.6,  # pin bottom flat part length (including corner arc)
        fp_s = True,  # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,  # first pin indicator radius
        fp_d = 0.2,  # first pin indicator distance from edge
        fp_z = 0.1,  # first pin indicator depth
        ef = 0.05,  # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,  # 0.45 chamfer of the 1st pin corner
        D1 = 14,  # body length
        E1 = 14,  # body width
        E = 16,  # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.44,  # pin width
        e = 1,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = None,  # e Pad
        excluded_pins = None,  # no pin excluded
        old_modelName = 'LQFP-52_14x14mm_Pitch1mm',
        modelName = 'LQFP-52_14x14mm_P1mm',
        rotation = -90,  # rotation if required
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
        modelName = 'TQFP-64-1EP_10x10mm_P0.5mm', #modelName
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
        modelName = 'HTQFP-64-1EP_10x10mm_P0.5mm', #modelName
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
        modelName = 'TQFP-100-1EP_14x14mm_P0.5mm', #modelName
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
    'TQFP-64_10x10mm_Pitch0.5mm_EP8x8mm': Params(
        #
        # 64-Lead Plastic Thin Quad Flatpack (PT) - 10x10x1 mm Body, 2.00 mm Footprint [HTQFP] thermal pad
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HTQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.0,         # body length
        E1 = 10.0,         # body width
        E = 12.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 16,           # number of pins along y axis (length)
        epad = (8.0, 8.0),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TQFP-64_10x10mm_Pitch0.5mm_EP8x8mm',            # modelName
        modelName = 'TQFP-64_10x10mm_Pitch0.5mm_EP8x8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'LQFP-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm_EP3.45x3.45mm': Params(
        #
        # LQFP32: plastic low profile quad flat package; 32 leads; body 5 x 5 x 1.4 mm (see NXP sot401-1_fr.pdf and sot401-1_po.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is LQFP-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.0,         # body length
        E1 = 5.0,         # body width
        E = 7.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 8,           # number of pins along y axis (length)
        epad = (3.45, 3.45),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'LQFP-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm_EP3.45x3.45mm',            # modelName
        modelName = 'LQFP-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm_EP3.45x3.45mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm': Params(
        #
        # LQFP, 48 Pin (http://www.analog.com/media/en/technical-documentation/data-sheets/LTC7810.pdf), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.0,         # body length
        E1 = 7.0,         # body width
        E = 9.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 12,           # number of pins along y axis (length)
        epad = (3.6, 3.6),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm',            # modelName
        modelName = 'LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'LQFP-80_10x10mm_P0.4mm': Params(
        #
        # LQFP80: plastic low profile quad flat package; 80 leads; body 10 x 10  mm (see Intersil q80.10x10.pdf and wiznet W5100_Datasheet_v1.2.7.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is LQFP-80_10x10mm_P0.4mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.0,         # body length
        E1 = 10.0,         # body width
        E = 12.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 20,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'LQFP-80_10x10mm_P0.4mm',            # modelName
        modelName = 'LQFP-80_10x10mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'LQFP-80_14x14mm_P0.65mm': Params(
        #
        # 80-Lead Quad Flatpack, 14x14x1.6mm Body (http://www.analog.com/media/en/technical-documentation/data-sheets/AD9852.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is LQFP-80_14x14mm_P0.65mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 14.0,         # body width
        E = 16.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 20,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'LQFP-80_14x14mm_P0.65mm',            # modelName
        modelName = 'LQFP-80_14x14mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-112_20x20mm_P0.65mm': Params(
        #
        # PQFP, 112 pins, 20mm sq body, 0.65mm pitch (http://cache.freescale.com/files/shared/doc/package_info/98ASS23330W.pdf, http://www.nxp.com/docs/en/application-note/AN4388.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-112_20x20mm_P0.65mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 20.0,         # body length
        E1 = 20.0,         # body width
        E = 22.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 28,           # number of pins along X axis (width)
        npy = 28,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-112_20x20mm_P0.65mm',            # modelName
        modelName = 'PQFP-112_20x20mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-132_24x24mm_P0.635mm': Params(
        #
        # PQFP, 132 pins, 24mm sq body, 0.635mm pitch (https://www.intel.com/content/dam/www/public/us/en/documents/packaging-databooks/packaging-chapter-02-databook.pdf, http://www.nxp.com/docs/en/application-note/AN4388.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-132_24x24mm_P0.635mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 24.0,         # body length
        E1 = 24.0,         # body width
        E = 27.8,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.25,          # pin width
        e = 0.64,          # pin (center-to-center) distance
        npx = 33,           # number of pins along X axis (width)
        npy = 33,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-132_24x24mm_P0.635mm',            # modelName
        modelName = 'PQFP-132_24x24mm_P0.635mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-132_24x24mm_P0.635mm_i386': Params(
        #
        # PQFP, 132 pins, 24mm sq body, 0.635mm pitch, Intel 386EX (https://www.intel.com/content/dam/www/public/us/en/documents/packaging-databooks/packaging-chapter-02-databook.pdf, http://www.nxp.com/docs/en/application-note/AN4388.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-132_24x24mm_P0.635mm_i386.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 24.0,         # body length
        E1 = 24.0,         # body width
        E = 27.8,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.25,          # pin width
        e = 0.64,          # pin (center-to-center) distance
        npx = 33,           # number of pins along X axis (width)
        npy = 33,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-132_24x24mm_P0.635mm_i386',            # modelName
        modelName = 'PQFP-132_24x24mm_P0.635mm_i386',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-144_28x28mm_P0.65mm': Params(
        #
        # PQFP, 144 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-144_28x28mm_P0.65mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 28.0,         # body length
        E1 = 28.0,         # body width
        E = 31.25,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 36,           # number of pins along X axis (width)
        npy = 36,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-144_28x28mm_P0.65mm',            # modelName
        modelName = 'PQFP-144_28x28mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-160_28x28mm_P0.65mm': Params(
        #
        # PQFP, 160 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-160_28x28mm_P0.65mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 28.0,         # body length
        E1 = 28.0,         # body width
        E = 31.25,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 40,           # number of pins along X axis (width)
        npy = 40,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-160_28x28mm_P0.65mm',            # modelName
        modelName = 'PQFP-160_28x28mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-208_28x28mm_P0.5mm': Params(
        #
        # PQFP, 208 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-208_28x28mm_P0.5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 28.0,         # body length
        E1 = 28.0,         # body width
        E = 30.93,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 52,           # number of pins along X axis (width)
        npy = 52,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-208_28x28mm_P0.5mm',            # modelName
        modelName = 'PQFP-208_28x28mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-240_32.1x32.1mm_P0.5mm': Params(
        #
        # PQFP, 240 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-240_32.1x32.1mm_P0.5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 32.1,         # body length
        E1 = 32.1,         # body width
        E = 34.92,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 60,           # number of pins along X axis (width)
        npy = 60,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-240_32.1x32.1mm_P0.5mm',            # modelName
        modelName = 'PQFP-240_32.1x32.1mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PQFP-44_10x10mm_P0.8mm': Params(
        #
        # 44-Lead Plastic Quad Flatpack - 10x10x2.5mm Body (http://www.onsemi.com/pub/Collateral/122BK.PDF)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PQFP-44_10x10mm_P0.8mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.0,         # body length
        E1 = 10.0,         # body width
        E = 13.1,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.32,          # pin width
        e = 0.8,          # pin (center-to-center) distance
        npx = 11,           # number of pins along X axis (width)
        npy = 11,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PQFP-44_10x10mm_P0.8mm',            # modelName
        modelName = 'PQFP-44_10x10mm_P0.8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TQFP-100_14x14mm_P0.5mm_EP5x5mm': Params(
        #
        # 100-Lead Plastic Thin Quad Flatpack (PF) - 14x14x1 mm Body 2.00 mm Footprint with Exposed Pad [TQFP] (see Microchip Packaging Specification 00000049BS.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 14.0,         # body width
        E = 16.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 25,           # number of pins along X axis (width)
        npy = 25,           # number of pins along y axis (length)
        epad = (5.0, 5.0),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TQFP-100_14x14mm_P0.5mm_EP5x5mm',            # modelName
        modelName = 'TQFP-100_14x14mm_P0.5mm_EP5x5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TQFP-176_24x24mm_P0.5mm': Params(
        #
        # TQFP, 176 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TQFP-176_24x24mm_P0.5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 24.0,         # body length
        E1 = 24.0,         # body width
        E = 26.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 44,           # number of pins along X axis (width)
        npy = 44,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TQFP-176_24x24mm_P0.5mm',            # modelName
        modelName = 'TQFP-176_24x24mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TQFP-48-1EP_7x7mm_P0.5mm_EP5x5mm': Params(
        #
        # TQFP, 48 Pin (https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2100_datasheet_Rev1.08.pdf (page 45)), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TQFP-48-1EP_7x7mm_P0.5mm_EP5x5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.0,         # body length
        E1 = 7.0,         # body width
        E = 9.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 12,           # number of pins along y axis (length)
        epad = (5.0, 5.0),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TQFP-48-1EP_7x7mm_P0.5mm_EP5x5mm',            # modelName
        modelName = 'TQFP-48-1EP_7x7mm_P0.5mm_EP5x5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm': Params(
        #
        # TQFP, 52 Pin (http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/tqfp_edsv/sv_52_1.pdf), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.0,         # body length
        E1 = 10.0,         # body width
        E = 12.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 13,           # number of pins along X axis (width)
        npy = 13,           # number of pins along y axis (length)
        epad = (6.5, 6.5),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm',            # modelName
        modelName = 'TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TQFP-64_10x10mm_P0.5mm_EP8x8mm': Params(
        #
        # 64-Lead Plastic Thin Quad Flatpack (PT) - 10x10x1 mm Body, 2.00 mm Footprint [TQFP] thermal pad
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.0,         # body length
        E1 = 10.0,         # body width
        E = 12.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 16,           # number of pins along y axis (length)
        epad = (8.0, 8.0),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TQFP-64_10x10mm_P0.5mm_EP8x8mm',            # modelName
        modelName = 'TQFP-64_10x10mm_P0.5mm_EP8x8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm': Params(
        #
        # 80-Lead Plastic Thin Quad Flatpack (PF) - 14x14mm body, 9.5mm sq thermal pad (http://www.analog.com/media/en/technical-documentation/data-sheets/AD9852.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 14.0,         # body width
        E = 16.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 20,           # number of pins along y axis (length)
        epad = (9.5, 9.5),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm',            # modelName
        modelName = 'TQFP-80-1EP_14x14mm_P0.65mm_EP9.5x9.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'VQFP-100_14x14mm_P0.5mm': Params(
        #
        # VQFP, 100 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is VQFP-100_14x14mm_P0.5mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 14.0,         # body width
        E = 16.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 25,           # number of pins along X axis (width)
        npy = 25,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'VQFP-100_14x14mm_P0.5mm',            # modelName
        modelName = 'VQFP-100_14x14mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'VQFP-128_14x14mm_P0.4mm': Params(
        #
        # VQFP, 128 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is VQFP-128_14x14mm_P0.4mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 14.0,         # body width
        E = 16.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 32,           # number of pins along X axis (width)
        npy = 32,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'VQFP-128_14x14mm_P0.4mm',            # modelName
        modelName = 'VQFP-128_14x14mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'VQFP-176_20x20mm_P0.4mm': Params(
        #
        # VQFP, 176 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is VQFP-176_20x20mm_P0.4mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 20.0,         # body length
        E1 = 20.0,         # body width
        E = 22.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.16,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        npx = 44,           # number of pins along X axis (width)
        npy = 44,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'VQFP-176_20x20mm_P0.4mm',            # modelName
        modelName = 'VQFP-176_20x20mm_P0.4mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'VQFP-80_14x14mm_P0.65mm': Params(
        #
        # VQFP, 80 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_qfp_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is VQFP-80_14x14mm_P0.65mm.kicad_mod
        # 
        the = 12.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.1,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 14.0,         # body width
        E = 16.32,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 20,           # number of pins along X axis (width)
        npy = 20,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'VQFP-80_14x14mm_P0.65mm',            # modelName
        modelName = 'VQFP-80_14x14mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

}

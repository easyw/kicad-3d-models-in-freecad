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
    # footprint_dir="Housings_SOIC.pretty"
    # lib_name = "Housings_SOIC"

    footprint_dir="Package_SOIC.pretty"
    lib_name = "Package_SOIC"

    body_color_key = "black body"
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"

part_params = {
	'SO-6L_10x3.84mm_Pitch1.27mm': Params( # TLP2770 https://toshiba.semicon-storage.com/info/docget.jsp?did=53548&prodName=TLP2770
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 0.65,      # pin bottom flat part length (including corner arc)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.05,    # first pin indicator distance from edge
        fp_z = 0.05,    # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,		#0.45 chamfer of the 1st pin corner
        D1 = 3.84,      # body length
        E1 = 7.5,       # body width
        E = 10.0,       # body overall width
        A1 = 0.1,       # body-board separation
        A2 = 2.1,       # body height
        b = 0.38,       # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 3,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SO-6L_10x3.84mm_Pitch1.27mm', #modelName
        modelName = 'SO-6L_10x3.84mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
	'SO-20_12.8x7.5mm_Pitch1.27mm': Params( # SA605 https://www.nxp.com/docs/en/data-sheet/SA605.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 0.65,      # pin bottom flat part length (including corner arc)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.05,    # first pin indicator distance from edge
        fp_z = 0.05,    # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,		#0.45 chamfer of the 1st pin corner
        D1 = 12.8,      # body length
        E1 = 7.5,       # body width
        E = 10.325,     # body overall width
        A1 = 0.2,       # body-board separation
        A2 = 2.35,      # body height
        b = 0.425,      # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 10,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SO-20_12.8x7.5mm_Pitch1.27mm', #modelName
        modelName = 'SO-20_12.8x7.5mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-8_3.9x4.9mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/msoi002j/msoi002j.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 0.65,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
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
        b = 0.41,       # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 4,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-8_3.9x4.9mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-8_3.9x4.9mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-8-1EP_3.9x4.9mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/msoi002j/msoi002j.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 0.65,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
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
        b = 0.41,       # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 4,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = (2.35,2.35),    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-8-1EP_3.9x4.9mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-8-1EP_3.9x4.9mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
	'SOIC-8_5.275x5.275mm_P1.27mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/20005045C.pdf#page=23
        the = 8.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.22,       # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 0.65,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.275,     # body length
        E1 = 5.275,     # body width
        E = 7.9,        # body overall width
        A1 = 0.1,       # body-board separation
        A2 = 1.955,     # body height
        b = 0.425,      # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 4,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-8_5.275x5.275mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-8_5.275x5.275mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-14_3.9x8.7mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/mpds177g/mpds177g.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 0.65,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 8.7,       # body length
        E1 = 3.9,       # body width
        E = 6.0,        # body overall width
        A1 = 0.1,       # body-board separation
        A2 = 1.65,      # body height
        b = 0.41,       # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 7,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-14_3.9x8.7mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-14_3.9x8.7mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-14W_7.5x9.0mm_P1.27mm': Params( # from http://www.ti.com/lit/ml/mpds386/mpds386.pdf
         the = 9.0,      # body angle in degrees
         tb_s = 0.15,    # top part of body is that much smaller
         c = 0.28,       # pin thickness, body center part height
         R1 = 0.1,       # pin upper corner, inner radius
         R2 = 0.1,       # pin lower corner, inner radius
         S = 0.30,       # pin top flat part length (excluding corner arc)
#        L = 1,         # pin bottom flat part length (including corner arc)
         fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
         fp_r = 1.0,     # first pin indicator radius
         fp_d = 0.1,    # first pin indicator distance from edge
         fp_z = 0.05,    # first pin indicator depth
         ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
         cc1 = 0.43,     # chamfer of the 1st pin corner
         D1 = 9.0,         # body length
         E1 = 7.5,       # body width
         E = 10.3,       # body overall width
         A1 = 0.2,       # body-board separation
         A2 = 2.5,       # body height
         b = 0.41,       # pin width
        e = 1.27,       # pin (center-to-center) distance
        npx = 7,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-14W_7.5x9.0mm_P1.27mm', #modelName
        modelName = 'SOIC-14W_7.5x9.0mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-16_3.9x9.9mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/mpds178g/mpds178g.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.9,       # body length
        E1 = 3.9,       # body width
        E = 6.0,        # body overall width
        A1 = 0.1,       # body-board separation
        A2 = 1.65,      # body height
        b = 0.41,       # pin width
        e = 1.27,
        npx = 8,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-16_3.9x9.9mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-16_3.9x9.9mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-16W_7.5x10.3mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/msoi003g/msoi003g.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.3,       # body length
        E1 = 7.5,       # body width
        E = 10.3,        # body overall width
        A1 = 0.2,       # body-board separation
        A2 = 2.55,      # body height
        b = 0.41,       # pin width
        e = 1.27,
        npx = 8,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-16W_7.5x10.3mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-16W_7.5x10.3mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-18W_7.5x11.6mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/mpds172a/mpds172a.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 11.55,       # body length
        E1 = 7.5,       # body width
        E = 10.3,        # body overall width
        A1 = 0.2,       # body-board separation
        A2 = 2.55,      # body height
        b = 0.41,       # pin width
        e = 1.27,
        npx = 9,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-18W_7.5x11.6mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-18W_7.5x11.6mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-20W_7.5x12.8mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/mpds173b/mpds173b.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.8,       # body length
        E1 = 7.5,       # body width
        E = 10.3,        # body overall width
        A1 = 0.2,       # body-board separation
        A2 = 2.55,      # body height
        b = 0.41,       # pin width
        e = 1.27,
        npx = 10,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-20W_7.5x12.8mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-20W_7.5x12.8mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-24W_7.5x15.4mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/mpds173b/mpds173b.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 15.4,       # body length
        E1 = 7.5,       # body width
        E = 10.3,        # body overall width
        A1 = 0.2,       # body-board separation
        A2 = 2.55,      # body height
        b = 0.41,       # pin width
        e = 1.27,
        npx = 12,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-24W_7.5x15.4mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-24W_7.5x15.4mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIC-28W_7.5x17.9mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/mpds175a/mpds175a.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 17.9,       # body length
        E1 = 7.5,       # body width
        E = 10.3,        # body overall width
        A1 = 0.2,       # body-board separation
        A2 = 2.55,      # body height
        b = 0.41,       # pin width
        e = 1.27,
        npx = 14,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIC-28W_7.5x17.9mm_Pitch1.27mm', #modelName
        modelName = 'SOIC-28W_7.5x17.9mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'SOIJ-8_5.3x5.3mm_Pitch1.27mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AU.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.3,       # body length
        E1 = 5.3,       # body width
        E = 7.94,        # body overall width
        A1 = 0.15,       # body-board separation
        A2 = 1.86,      # body height
        b = 0.45,       # pin width
        e = 1.27,
        npx = 4,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'SOIJ-8_5.3x5.3mm_Pitch1.27mm', #modelName
        modelName = 'SOIJ-8_5.3x5.3mm_P1.27mm', #modelName
        rotation = -90,   # rotation if required
        ),
    'ST_MultiPowerSO-30': Params( # from https://www.st.com/resource/en/datasheet/vnh5019a-e.pdf
        the = 9.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c    = 0.275,   # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.79,      # pin bottom flat part length (including corner arc)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,     #0.45 chamfer of the 1st pin corner
        D1 = 17.2,      # body length
        E1 = 16.0 ,     # body width
        E =  19.0,      # body overall width
        A1 = 0.15,      # body-board separation
        A2 = 2.05,      # body height
        b =  0.5 ,      # pin width
        e =  1.00,
        npx = 15,       # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName = 'ST_MultiPowerSO-30', #modelName
        modelName = 'ST_MultiPowerSO-30', #modelName
        rotation = -90,   # rotation if required
        ),
    'HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugUp': Params(
        #
        # HSOP 11.0x15.9mm Pitch 0.65mm Slug Up (PowerSO-36) [JEDEC MO-166] (http://www.st.com/resource/en/datasheet/vn808cm-32-e.pdf, http://www.st.com/resource/en/application_note/cd00003801.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugUp.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 15.9,         # body length
        E1 = 11.0,         # body width
        E = 14.7,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugUp',            # modelName
        modelName = 'HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugUp',            # modelName
        rotation = -90,      # rotation if required
        ),

    'HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm': Params(
        #
        # HSOP, 8 Pin (https://www.st.com/resource/en/datasheet/l5973d.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,         # body length
        E1 = 3.9,         # body width
        E = 6.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.42,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (3.1, 2.41),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm',            # modelName
        modelName = 'HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm': Params(
        #
        # HTSOP, 8 Pin (https://media.digikey.com/pdf/Data%20Sheets/Rohm%20PDFs/BD9G341EFJ.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,         # body length
        E1 = 3.9,         # body width
        E = 6.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.42,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (3.2, 2.4),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm',            # modelName
        modelName = 'HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSSOP-16-1EP_4.4x5mm_Pitch0.65mm_EP3.4x5mm': Params(
        #
        # 16-Lead Plastic HTSSOP (4.4x5x1.2mm); Thermal pad; (http://www.ti.com/lit/ds/symlink/drv8833.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.3,         # body length
        E1 = 4.4,         # body width
        E = 5.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-16-1EP_4.4x5mm_Pitch0.65mm_EP3.4x5mm',            # modelName
        modelName = 'TSSOP-16-1EP_4.4x5mm_Pitch0.65mm_EP3.4x5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_Mask2.75x3.43mm': Params(
        #
        # HTSSOP, 20 Pin (http://www.ti.com/lit/ds/symlink/tlc5971.pdf#page=37&zoom=160,-90,3), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_Mask2.75x3.43mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,         # body length
        E1 = 4.4,         # body width
        E = 6.72,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 10,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (6.0, 3.4),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_Mask2.75x3.43mm',            # modelName
        modelName = 'HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_Mask2.75x3.43mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.4x7.8mm_Mask2.4x4.68mm': Params(
        #
        # HTSSOP, 24 Pin (http://www.ti.com/lit/ds/symlink/tps703.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.4x7.8mm_Mask2.4x4.68mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.8,         # body length
        E1 = 4.4,         # body width
        E = 6.72,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (7.3, 3.4),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.4x7.8mm_Mask2.4x4.68mm',            # modelName
        modelName = 'HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.4x7.8mm_Mask2.4x4.68mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm': Params(
        #
        # HTSSOP32: plastic thin shrink small outline package; 32 leads; body width 6.1 mm; lead pitch 0.65 mm (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot487-1_po.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm_Mask4.11x4.36mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 11.0,         # body length
        E1 = 6.1,         # body width
        E = 8.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (10.5, 5.2),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm',            # modelName
        modelName = 'HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'HTSSOP-38-1EP_6.1x12.5mm_P0.65mm_EP5.2x12.5mm_Mask3.39x6.35mm': Params(
        #
        # HTSSOP, 38 Pin (http://www.ti.com/lit/ds/symlink/tlc5951.pdf#page=47&zoom=140,-67,15), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is HTSSOP-38-1EP_6.1x12.5mm_P0.65mm_EP5.2x12.5mm_Mask3.39x6.35mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 6.1,         # body width
        E = 8.43,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 19,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (12.0, 5.2),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HTSSOP-38-1EP_6.1x12.5mm_P0.65mm_EP5.2x12.5mm_Mask3.39x6.35mm',            # modelName
        modelName = 'HTSSOP-38-1EP_6.1x12.5mm_P0.65mm_EP5.2x12.5mm_Mask3.39x6.35mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'Linear_MSOP-12-16-1EP_3x4mm_P0.5mm': Params(
        #
        # 12-Lead Plastic Micro Small Outline Package (MS) [MSOP], variant of MSOP-16 (see http://cds.linear.com/docs/en/datasheet/3630fd.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Linear_MSOP-12-16-1EP_3x4mm_P0.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,         # body length
        E1 = 3.0,         # body width
        E = 5.21,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 6,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'Linear_MSOP-12-16-1EP_3x4mm_P0.5mm',            # modelName
        modelName = 'Linear_MSOP-12-16-1EP_3x4mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'MSOP-12-16-1EP_3x4mm_Pitch0.5mm_EP1.65x2.85mm': Params(
        #
        # 10-Lead Plastic Micro Small Outline Package (MS) [MSOP] (see Microchip Packaging Specification 00000049BS.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is MSOP-12-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm_ThermalVias.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,         # body length
        E1 = 3.0,         # body width
        E = 4.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [2, 4, 13, 15],          # pin excluded
        old_modelName = 'MSOP-12-16-1EP_3x4mm_Pitch0.5mm_EP1.65x2.85mm',            # modelName
        modelName = 'MSOP-12-16-1EP_3x4mm_Pitch0.5mm_EP1.65x2.85mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'MSOP-16-1EP_3x4mm_Pitch0.5mm_EP1.65x2.85mm': Params(
        #
        # 10-Lead Plastic Micro Small Outline Package (MS) [MSOP] (see Microchip Packaging Specification 00000049BS.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is MSOP-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm_ThermalVias.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,         # body length
        E1 = 3.0,         # body width
        E = 4.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'MSOP-16-1EP_3x4mm_Pitch0.5mm_EP1.65x2.85mm',            # modelName
        modelName = 'MSOP-16-1EP_3x4mm_Pitch0.5mm_EP1.65x2.85mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'MSOP-8-1EP_3x3mm_P0.65mm_EP2.54x2.8mm': Params(
        #
        # MME Package; 8-Lead Plastic MSOP, Exposed Die Pad (see Microchip http://ww1.microchip.com/downloads/en/DeviceDoc/mic5355_6.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is MSOP-8-1EP_3x3mm_P0.65mm_EP2.54x2.8mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,         # body length
        E1 = 3.0,         # body width
        E = 5.8,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (2.5, 2.54),       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'MSOP-8-1EP_3x3mm_P0.65mm_EP2.54x2.8mm',            # modelName
        modelName = 'MSOP-8-1EP_3x3mm_P0.65mm_EP2.54x2.8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PowerIntegrations_eSOP-12B': Params(
        #
        # eSOP-12B SMT Flat Package with Heatsink Tab, see https://ac-dc.power.com/sites/default/files/product-docs/topswitch-jx_family_datasheet.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_eSOP-12B.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.16,         # body length
        E1 = 8.89,         # body width
        E = 10.9,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.78,          # pin (center-to-center) distance
        npx = 6,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [5],          # pin excluded
        old_modelName = 'PowerIntegrations_eSOP-12B',            # modelName
        modelName = 'PowerIntegrations_eSOP-12B',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PowerIntegrations_SO-8': Params(
        #
        # Power-Integrations variant of 8-Lead Plastic Small Outline (SN) - Narrow, 3.90 mm Body [SOIC], see https://ac-dc.power.com/sites/default/files/product-docs/senzero_family_datasheet.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_SO-8.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.90,         # body length
        E1 = 3.90,         # body width
        E = 6.00,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'PowerIntegrations_SO-8',            # modelName
        modelName = 'PowerIntegrations_SO-8',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PowerIntegrations_SO-8B': Params(
        #
        # Power-Integrations variant of 8-Lead Plastic Small Outline (SN) - Narrow, 3.90 mm Body [SOIC], see https://www.mouser.com/ds/2/328/linkswitch-pl_family_datasheet-12517.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_SO-8B.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.90,         # body length
        E1 = 3.90,         # body width
        E = 6.00,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [6],          # pin excluded
        old_modelName = 'PowerIntegrations_SO-8B',            # modelName
        modelName = 'PowerIntegrations_SO-8B',            # modelName
        rotation = -90,      # rotation if required
        ),

    'PowerIntegrations_SO-8C': Params(
        #
        # Power-Integrations variant of 8-Lead Plastic Small Outline (SN) - Narrow, 3.90 mm Body [SOIC], see https://www.mouser.com/ds/2/328/linkswitch-pl_family_datasheet-12517.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_SO-8C.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.90,         # body length
        E1 = 3.90,         # body width
        E = 6.00,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [3],          # pin excluded
        old_modelName = 'PowerIntegrations_SO-8C',            # modelName
        modelName = 'PowerIntegrations_SO-8C',            # modelName
        rotation = -90,      # rotation if required
        ),

    'QSOP-20_3.9x8.7mm_P0.635mm': Params(
        #
        # 20-Lead Plastic Shrink Small Outline Narrow Body (http://www.analog.com/media/en/technical-documentation/data-sheets/ADuM7640_7641_7642_7643.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is QSOP-20_3.9x8.7mm_P0.635mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 8.7,         # body length
        E1 = 3.9,         # body width
        E = 6.31,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.25,          # pin width
        e = 0.64,          # pin (center-to-center) distance
        npx = 10,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'QSOP-20_3.9x8.7mm_P0.635mm',            # modelName
        modelName = 'QSOP-20_3.9x8.7mm_P0.635mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SO-4_4.4x2.3mm_P1.27mm': Params(
        #
        # 4-Lead Plastic Small Outline (SO), see http://datasheet.octopart.com/OPIA403BTRE-Optek-datasheet-5328560.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SO-4_4.4x2.3mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 2.3,         # body length
        E1 = 4.4,         # body width
        E = 7.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 2,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SO-4_4.4x2.3mm_P1.27mm',            # modelName
        modelName = 'SO-4_4.4x2.3mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SO-4_4.4x3.6mm_P2.54mm': Params(
        #
        # 4-Lead Plastic Small Outline (SO), see https://www.elpro.org/de/index.php?controller=attachment&id_attachment=339
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SO-4_4.4x3.6mm_P2.54mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 3.6,         # body length
        E1 = 4.4,         # body width
        E = 7.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.45,          # pin width
        e = 2.54,          # pin (center-to-center) distance
        npx = 2,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SO-4_4.4x3.6mm_P2.54mm',            # modelName
        modelName = 'SO-4_4.4x3.6mm_P2.54mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SO-4_4.4x4.3mm_P2.54mm': Params(
        #
        # 4-Lead Plastic Small Outline (SO), see https://docs.broadcom.com/docs/AV02-0173EN
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SO-4_4.4x4.3mm_P2.54mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.3,         # body length
        E1 = 4.4,         # body width
        E = 7.0,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.84,          # pin width
        e = 2.54,          # pin (center-to-center) distance
        npx = 2,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SO-4_4.4x4.3mm_P2.54mm',            # modelName
        modelName = 'SO-4_4.4x4.3mm_P2.54mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SO-4_7.6x3.6mm_P2.54mm': Params(
        #
        # 4-Lead Plastic Small Outline (SO) (http://www.everlight.com/file/ProductFile/201407061745083848.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SO-4_7.6x3.6mm_P2.54mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 3.6,         # body length
        E1 = 7.6,         # body width
        E = 10.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.45,          # pin width
        e = 2.54,          # pin (center-to-center) distance
        npx = 2,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SO-4_7.6x3.6mm_P2.54mm',            # modelName
        modelName = 'SO-4_7.6x3.6mm_P2.54mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SO-5_4.4x3.6mm_P1.27mm': Params(
        #
        # 5-Lead Plastic Small Outline (SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SO-5_4.4x3.6mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 3.6,         # body length
        E1 = 4.4,         # body width
        E = 6.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 3,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [2],          # pin excluded
        old_modelName = 'SO-5_4.4x3.6mm_P1.27mm',            # modelName
        modelName = 'SO-5_4.4x3.6mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SO-6_4.4x3.6mm_P1.27mm': Params(
        #
        # 6-Lead Plastic Small Outline (SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SO-6_4.4x3.6mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 3.6,         # body length
        E1 = 4.4,         # body width
        E = 7.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 3,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SO-6_4.4x3.6mm_P1.27mm',            # modelName
        modelName = 'SO-6_4.4x3.6mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SO-8_5.3x6.2mm_P1.27mm': Params(
        #
        # 8-Lead Plastic Small Outline, 5.3x6.2mm Body (http://www.ti.com.cn/cn/lit/ds/symlink/tl7705a.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SO-8_5.3x6.2mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 6.2,         # body length
        E1 = 5.3,         # body width
        E = 8.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.39,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SO-8_5.3x6.2mm_P1.27mm',            # modelName
        modelName = 'SO-8_5.3x6.2mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOIC-16W-12_7.5x10.3mm_P1.27mm': Params(
        #
        # SOIC-16 With 12 Pin Placed - Wide, 7.50 mm Body [SOIC] (https://docs.broadcom.com/docs/AV02-0169EN)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOIC-16W-12_7.5x10.3mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.3,         # body length
        E1 = 7.5,         # body width
        E = 9.3,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [4, 5, 12, 13],          # pin excluded
        old_modelName = 'SOIC-16W-12_7.5x10.3mm_P1.27mm',            # modelName
        modelName = 'SOIC-16W-12_7.5x10.3mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOIC-16W_5.3x10.2mm_P1.27mm': Params(
        #
        # 16-Lead Plastic Small Outline (SO) - Wide, 5.3 mm Body (http://www.ti.com/lit/ml/msop002a/msop002a.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOIC-16W_5.3x10.2mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.2,         # body length
        E1 = 5.3,         # body width
        E = 7.1,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SOIC-16W_5.3x10.2mm_P1.27mm',            # modelName
        modelName = 'SOIC-16W_5.3x10.2mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOIC-16W_7.5x12.8mm_P1.27mm': Params(
        #
        # 16-Lead Plastic Small Outline (SO) - Wide, 7.50 mm x 12.8 mm Body (http://www.analog.com/media/en/technical-documentation/data-sheets/ADuM6000.PDF)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOIC-16W_7.5x12.8mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.2,         # body length
        E1 = 5.3,         # body width
        E = 7.1,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SOIC-16W_7.5x12.8mm_P1.27mm',            # modelName
        modelName = 'SOIC-16W_7.5x12.8mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOIC-28W_7.5x18.7mm_P1.27mm': Params(
        #
        # 28-Lead Plastic Small Outline (SO) - Wide, 7.50 mm X 18.7 mm Body [SOIC] (https://www.akm.com/akm/en/file/datasheet/AK5394AVS.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOIC-28W_7.5x18.7mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 18.7,         # body length
        E1 = 7.5,         # body width
        E = 9.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SOIC-28W_7.5x18.7mm_P1.27mm',            # modelName
        modelName = 'SOIC-28W_7.5x18.7mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOIC-8-N7_3.9x4.9mm_P1.27mm': Params(
        #
        # 8-Lead Plastic Small Outline (SN) - Narrow, 3.90 mm Body [SOIC], pin 7 removed (Microchip Packaging Specification 00000049BS.pdf, http://www.onsemi.com/pub/Collateral/NCP1207B.PDF)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOIC-8-N7_3.9x4.9mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,         # body length
        E1 = 3.9,         # body width
        E = 5.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [7],          # pin excluded
        old_modelName = 'SOIC-8-N7_3.9x4.9mm_P1.27mm',            # modelName
        modelName = 'SOIC-8-N7_3.9x4.9mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOJ-36_10.16x23.49mm_P1.27mm': Params(
        #
        # SOJ, 36 Pin (http://www.issi.com/WW/pdf/61-64C5128AL.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOJ-36_10.16x23.49mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 23.49,         # body length
        E1 = 10.16,         # body width
        E = 11.66,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SOJ-36_10.16x23.49mm_P1.27mm',            # modelName
        modelName = 'SOJ-36_10.16x23.49mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOP-16_7.5x10.4mm_P1.27mm': Params(
        #
        # 16-Lead Plastic Small Outline http://www.vishay.com/docs/49633/sg2098.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOP-16_7.5x10.4mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.4,         # body length
        E1 = 7.5,         # body width
        E = 10.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.51,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 8,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SOP-16_7.5x10.4mm_P1.27mm',            # modelName
        modelName = 'SOP-16_7.5x10.4mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SOP-18_7.0x12.5mm_P1.27mm': Params(
        #
        #  SOP, 18 Pin (https://toshiba.semicon-storage.com/info/docget.jsp?did=30523), generated with kicad-footprint-generator package_soic_sop.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SOP-18_7.0x12.5mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 7.0,         # body width
        E = 9.72,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.42,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 9,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SOP-18_7.0x12.5mm_P1.27mm',            # modelName
        modelName = 'SOP-18_7.0x12.5mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSO-6_6.8x4.6mm_P1.27mm_Clearance7mm': Params(
        #
        # 8-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSO-6_6.8x4.6mm_P1.27mm_Clearance7mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.6,         # body length
        E1 = 6.8,         # body width
        E = 9.54,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 3,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSO-6_6.8x4.6mm_P1.27mm_Clearance7mm',            # modelName
        modelName = 'SSO-6_6.8x4.6mm_P1.27mm_Clearance7mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSO-6_6.8x4.6mm_P1.27mm_Clearance8mm': Params(
        #
        # 8-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSO-6_6.8x4.6mm_P1.27mm_Clearance8mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.6,         # body length
        E1 = 6.8,         # body width
        E = 11.74,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 3,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSO-6_6.8x4.6mm_P1.27mm_Clearance8mm',            # modelName
        modelName = 'SSO-6_6.8x4.6mm_P1.27mm_Clearance8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSO-8_13.6x6.3mm_P1.27mm_Clearance14.2mm': Params(
        #
        # 8-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSO-8_13.6x6.3mm_P1.27mm_Clearance14.2mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 6.3,         # body length
        E1 = 13.6,         # body width
        E = 16.96,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSO-8_13.6x6.3mm_P1.27mm_Clearance14.2mm',            # modelName
        modelName = 'SSO-8_13.6x6.3mm_P1.27mm_Clearance14.2mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSO-8_6.8x5.9mm_P1.27mm_Clearance7mm': Params(
        #
        # 8-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSO-8_6.8x5.9mm_P1.27mm_Clearance7mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.9,         # body length
        E1 = 6.8,         # body width
        E = 9.54,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSO-8_6.8x5.9mm_P1.27mm_Clearance7mm',            # modelName
        modelName = 'SSO-8_6.8x5.9mm_P1.27mm_Clearance7mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSO-8_6.8x5.9mm_P1.27mm_Clearance8mm': Params(
        #
        # 8-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSO-8_6.8x5.9mm_P1.27mm_Clearance8mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.9,         # body length
        E1 = 6.8,         # body width
        E = 11.7,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSO-8_6.8x5.9mm_P1.27mm_Clearance8mm',            # modelName
        modelName = 'SSO-8_6.8x5.9mm_P1.27mm_Clearance8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSO-8_9.6x6.3mm_P1.27mm_Clearance10.5mm': Params(
        #
        # 8-Lead Plastic Stretched Small Outline (SSO/Stretched SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSO-8_9.6x6.3mm_P1.27mm_Clearance10.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 6.3,         # body length
        E1 = 9.6,         # body width
        E = 13.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.45,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSO-8_9.6x6.3mm_P1.27mm_Clearance10.5mm',            # modelName
        modelName = 'SSO-8_9.6x6.3mm_P1.27mm_Clearance10.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSOP-10_3.9x4.9mm_P1.00mm': Params(
        #
        # 10-Lead SSOP, 3.9 x 4.9mm body, 1.00mm pitch (http://www.st.com/resource/en/datasheet/viper01.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSOP-10_3.9x4.9mm_P1.00mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,         # body length
        E1 = 3.9,         # body width
        E = 6.1,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.36,          # pin width
        e = 1.0,          # pin (center-to-center) distance
        npx = 5,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSOP-10_3.9x4.9mm_P1.00mm',            # modelName
        modelName = 'SSOP-10_3.9x4.9mm_P1.00mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSOP-20_3.9x8.7mm_P0.635mm': Params(
        #
        # SSOP20: plastic shrink small outline package; 24 leads; body width 3.9 mm; lead pitch 0.635; (see http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT231X.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSOP-20_3.9x8.7mm_P0.635mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 8.7,         # body length
        E1 = 3.9,         # body width
        E = 6.2,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.25,          # pin width
        e = 0.64,          # pin (center-to-center) distance
        npx = 10,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSOP-20_3.9x8.7mm_P0.635mm',            # modelName
        modelName = 'SSOP-20_3.9x8.7mm_P0.635mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSOP-28_3.9x9.9mm_P0.635mm': Params(
        #
        # SSOP28: plastic shrink small outline package; 28 leads; body width 3.9 mm; lead pitch 0.635; (see http://cds.linear.com/docs/en/datasheet/38901fb.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSOP-28_3.9x9.9mm_P0.635mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.9,         # body length
        E1 = 3.9,         # body width
        E = 6.2,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.25,          # pin width
        e = 0.64,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSOP-28_3.9x9.9mm_P0.635mm',            # modelName
        modelName = 'SSOP-28_3.9x9.9mm_P0.635mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSOP-32_11.305x20.495mm_P1.27mm': Params(
        #
        # SSOP, 32 Pin (http://www.issi.com/WW/pdf/61-64C5128AL.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSOP-32_11.305x20.495mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 20.5,         # body length
        E1 = 11.3,         # body width
        E = 14.1,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.42,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSOP-32_11.305x20.495mm_P1.27mm',            # modelName
        modelName = 'SSOP-32_11.305x20.495mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSOP-44_5.3x12.8mm_P0.5mm': Params(
        #
        # 44-Lead Plastic Shrink Small Outline (SS)-5.30 mm Body [SSOP] (http://cds.linear.com/docs/en/datasheet/680313fa.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSOP-44_5.3x12.8mm_P0.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.8,         # body length
        E1 = 5.3,         # body width
        E = 7.75,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.17,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 22,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSOP-44_5.3x12.8mm_P0.5mm',            # modelName
        modelName = 'SSOP-44_5.3x12.8mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSOP-8_3.9x5.05mm_P1.27mm': Params(
        #
        # SSOP, 8 Pin (http://www.fujitsu.com/downloads/MICRO/fsa/pdf/products/memory/fram/MB85RS16-DS501-00014-6v0-E.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSOP-8_3.9x5.05mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.05,         # body length
        E1 = 3.9,         # body width
        E = 6.35,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.42,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSOP-8_3.9x5.05mm_P1.27mm',            # modelName
        modelName = 'SSOP-8_3.9x5.05mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'SSOP-8_5.25x5.24mm_P1.27mm': Params(
        #
        # SSOP, 8 Pin (http://www.fujitsu.com/ca/en/Images/MB85RS2MT-DS501-00023-1v0-E.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is SSOP-8_5.25x5.24mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 5.24,         # body length
        E1 = 5.25,         # body width
        E = 8.22,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.42,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'SSOP-8_5.25x5.24mm_P1.27mm',            # modelName
        modelName = 'SSOP-8_5.25x5.24mm_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'ST_MultiPowerSO-30': Params(
        #
        # MultiPowerSO-30 3EP 16.0x17.2mm Pitch 1mm (http://www.st.com/resource/en/datasheet/vnh2sp30-e.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is ST_MultiPowerSO-30.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 17.4,         # body length
        E1 = 16.0,         # body width
        E = 18.25,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.5,          # pin width
        e = 1.0,          # pin (center-to-center) distance
        npx = 15,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'ST_MultiPowerSO-30',            # modelName
        modelName = 'ST_MultiPowerSO-30',            # modelName
        rotation = -90,      # rotation if required
        ),

    'ST_PowerSSO-24_SlugDown': Params(
        #
        # ST PowerSSO-24 1EP 7.5x10.3mm Pitch 0.8mm [JEDEC MO-271] (http://www.st.com/resource/en/datasheet/tda7266p.pdf, http://freedatasheets.com/downloads/Technical%20Note%20Powersso24%20TN0054.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is ST_PowerSSO-24_SlugDown.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.3,         # body length
        E1 = 7.5,         # body width
        E = 9.87,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.3,          # pin width
        e = 0.8,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'ST_PowerSSO-24_SlugDown',            # modelName
        modelName = 'ST_PowerSSO-24_SlugDown',            # modelName
        rotation = -90,      # rotation if required
        ),

    'ST_PowerSSO-24_SlugUp': Params(
        #
        # ST PowerSSO-24 1EP 7.5x10.3mm Pitch 0.8mm [JEDEC MO-271] (http://www.st.com/resource/en/datasheet/tda7266p.pdf, http://freedatasheets.com/downloads/Technical%20Note%20Powersso24%20TN0054.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is ST_PowerSSO-24_SlugUp.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.3,         # body length
        E1 = 7.5,         # body width
        E = 9.87,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.3,          # pin width
        e = 0.8,          # pin (center-to-center) distance
        npx = 12,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'ST_PowerSSO-24_SlugUp',            # modelName
        modelName = 'ST_PowerSSO-24_SlugUp',            # modelName
        rotation = -90,      # rotation if required
        ),

    'ST_PowerSSO-36_SlugDown': Params(
        #
        # ST PowerSSO-36 1EP 7.5x10.3mm Pitch 0.8mm [JEDEC MO-271] (http://www.st.com/resource/en/datasheet/tda7492p.pdf, http://freedatasheets.com/downloads/Technical%20Note%20Powersso24%20TN0054.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is ST_PowerSSO-36_SlugDown.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.3,         # body length
        E1 = 7.5,         # body width
        E = 9.87,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'ST_PowerSSO-36_SlugDown',            # modelName
        modelName = 'ST_PowerSSO-36_SlugDown',            # modelName
        rotation = -90,      # rotation if required
        ),

    'ST_PowerSSO-36_SlugUp': Params(
        #
        # ST PowerSSO-36 1EP 7.5x10.3mm Pitch 0.8mm [JEDEC MO-271] (http://www.st.com/resource/en/datasheet/tda7492p.pdf, http://freedatasheets.com/downloads/Technical%20Note%20Powersso24%20TN0054.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is ST_PowerSSO-36_SlugUp.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 10.3,         # body length
        E1 = 7.5,         # body width
        E = 9.87,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 18,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'ST_PowerSSO-36_SlugUp',            # modelName
        modelName = 'ST_PowerSSO-36_SlugUp',            # modelName
        rotation = -90,      # rotation if required
        ),

    'HTSOP-8-1EP_3.9x4.9mm_Pitch1.27mm': Params(
        #
        # Texas Instruments HSOP 9, 1.27mm pitch, 3.9x4.9mm body, exposed pad, DDA0008J (http://www.ti.com/lit/ds/symlink/tps5430.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Texas_HSOP-8-1EP_3.9x4.9mm_P1.27mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,         # body length
        E1 = 3.9,         # body width
        E = 5.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'HTSOP-8-1EP_3.9x4.9mm_Pitch1.27mm',            # modelName
        modelName = 'HTSOP-8-1EP_3.9x4.9mm_Pitch1.27mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.85x4.9mm_Mask2.4x3.1mm_ThermalVias': Params(
        #
        # 8-pin HTSOP package with 1.27mm pin pitch, compatible with SOIC-8, 3.9x4.9mm body, exposed pad, thermal vias, http://www.ti.com/lit/ds/symlink/drv8870.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.95x4.9mm_Mask2.4x3.1mm_ThermalVias.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,         # body length
        E1 = 3.9,         # body width
        E = 5.75,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.4,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.85x4.9mm_Mask2.4x3.1mm_ThermalVias',            # modelName
        modelName = 'Texas_HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.85x4.9mm_Mask2.4x3.1mm_ThermalVias',            # modelName
        rotation = -90,      # rotation if required
        ),

    'Texas_PWP0020A': Params(
        #
        # 20-Pin Thermally Enhanced Thin Shrink Small-Outline Package, Body 4.4x6.5x1.1mm, Pad 3.0x4.2mm, Texas Instruments (see http://www.ti.com/lit/ds/symlink/lm5118.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Texas_PWP0020A.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,         # body length
        E1 = 4.4,         # body width
        E = 5.94,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 10,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'Texas_PWP0020A',            # modelName
        modelName = 'Texas_PWP0020A',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TI_SO-PowerPAD-8': Params(
        #
        # 8-Lead Plastic PSOP, Exposed Die Pad (TI DDA0008B, see http://www.ti.com/lit/ds/symlink/lm3404.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TI_SO-PowerPAD-8.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,         # body length
        E1 = 3.9,         # body width
        E = 5.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TI_SO-PowerPAD-8',            # modelName
        modelName = 'TI_SO-PowerPAD-8',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-5_1.65x3.05mm_P0.95mm': Params(
        #
        # TSOP-5 package (comparable to TSOT-23), https://www.vishay.com/docs/71200/71200.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-5_1.65x3.05mm_P0.95mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,        # first pin indicator radius
        fp_d = 0.05,       # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 3.05,         # body length
        E1 = 1.65,         # body width
        E = 2.8,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.4,          # pin width
        e = 0.95,          # pin (center-to-center) distance
        npx = 3,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = [5],          # pin excluded
        old_modelName = 'TSOP-5_1.65x3.05mm_P0.95mm',            # modelName
        modelName = 'TSOP-5_1.65x3.05mm_P0.95mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-6_1.65x3.05mm_P0.95mm': Params(
        #
        # TSOP-6 package (comparable to TSOT-23), https://www.vishay.com/docs/71200/71200.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-6_1.65x3.05mm_P0.95mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,        # first pin indicator radius
        fp_d = 0.05,       # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 3.05,         # body length
        E1 = 1.65,         # body width
        E = 2.8,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.0,          # body height
        b = 0.4,          # pin width
        e = 0.95,          # pin (center-to-center) distance
        npx = 3,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-6_1.65x3.05mm_P0.95mm',            # modelName
        modelName = 'TSOP-6_1.65x3.05mm_P0.95mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-I-28_11.8x8mm_P0.55mm': Params(
        #
        # TSOP I, 28 pins, 18.8x8mm body, 0.55mm pitch, IPC-calculated pads (http://ww1.microchip.com/downloads/en/devicedoc/doc0807.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-I-28_11.8x8mm_P0.55mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 8.0,         # body length
        E1 = 11.8,         # body width
        E = 13.2,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.55,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-I-28_11.8x8mm_P0.55mm',            # modelName
        modelName = 'TSOP-I-28_11.8x8mm_P0.55mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-I-32_11.8x8mm_P0.5mm': Params(
        #
        # TSOP-I, 32 Pin (http://www.issi.com/WW/pdf/61-64C5128AL.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-I-32_11.8x8mm_P0.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.10,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 8.0,         # body length
        E1 = 11.8,         # body width
        E = 13.2,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.50,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-I-32_11.8x8mm_P0.5mm',            # modelName
        modelName = 'TSOP-I-32_11.8x8mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-I-32_18.4x8mm_P0.5mm': Params(
        #
        # TSOP I, 32 pins, 18.4x8mm body (https://www.micron.com/~/media/documents/products/technical-note/nor-flash/tn1225_land_pad_design.pdf, http://www.fujitsu.com/downloads/MICRO/fma/pdfmcu/f32pm25.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-I-32_18.4x8mm_P0.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.10,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 8.0,         # body length
        E1 = 18.4,         # body width
        E = 20.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.17,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 16,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-I-32_18.4x8mm_P0.5mm',            # modelName
        modelName = 'TSOP-I-32_18.4x8mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-I-48_18.4x12mm_P0.5mm': Params(
        #
        # TSOP I, 32 pins, 18.4x8mm body (https://www.micron.com/~/media/documents/products/technical-note/nor-flash/tn1225_land_pad_design.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-I-48_18.4x12mm_P0.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.10,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.0,         # body length
        E1 = 18.4,         # body width
        E = 20.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.17,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 24,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-I-48_18.4x12mm_P0.5mm',            # modelName
        modelName = 'TSOP-I-48_18.4x12mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-I-56_18.4x14mm_P0.5mm': Params(
        #
        # TSOP I, 32 pins, 18.4x8mm body (https://www.micron.com/~/media/documents/products/technical-note/nor-flash/tn1225_land_pad_design.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-I-56_18.4x14mm_P0.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.10,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 14.0,         # body length
        E1 = 18.4,         # body width
        E = 20.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.17,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 28,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-I-56_18.4x14mm_P0.5mm',            # modelName
        modelName = 'TSOP-I-56_18.4x14mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-II-44_10.16x18.41mm_P0.8mm': Params(
        #
        # TSOP-II, 44 Pin (http://www.issi.com/WW/pdf/61-64C5128AL.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-II-44_10.16x18.41mm_P0.8mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 18.41,         # body length
        E1 = 10.16,         # body width
        E = 11.66,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.25,          # pin width
        e = 0.8,          # pin (center-to-center) distance
        npx = 22,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-II-44_10.16x18.41mm_P0.8mm',            # modelName
        modelName = 'TSOP-II-44_10.16x18.41mm_P0.8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSOP-II-54_22.2x10.16mm_P0.8mm': Params(
        #
        # 54-lead TSOP typ II package
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSOP-II-54_22.2x10.16mm_P0.8mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 22.2,         # body length
        E1 = 10.16,         # body width
        E = 11.66,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.25,          # pin width
        e = 0.8,          # pin (center-to-center) distance
        npx = 27,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSOP-II-54_22.2x10.16mm_P0.8mm',            # modelName
        modelName = 'TSOP-II-54_22.2x10.16mm_P0.8mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSSOP-14-1EP_4.4x5mm_P0.65mm': Params(
        #
        # 14-Lead Plastic Thin Shrink Small Outline (ST)-4.4 mm Body [TSSOP] with exposed pad (http://cds.linear.com/docs/en/datasheet/34301fa.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSSOP-14-1EP_4.4x5mm_P0.65mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 4.5,         # body length
        E1 = 4.4,         # body width
        E = 5.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.25,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 7,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-14-1EP_4.4x5mm_P0.65mm',            # modelName
        modelName = 'TSSOP-14-1EP_4.4x5mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSSOP-28_4.4x9.7mm_Pitch0.65mm': Params(
        #
        # TSSOP28: plastic thin shrink small outline package; 28 leads; body width 4.4 mm; Exposed Pad Variation; (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot361-1_po.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSSOP-28-1EP_4.4x9.7mm_P0.65mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,         # body length
        E1 = 4.4,         # body width
        E = 5.5,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.25,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 14,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-28_4.4x9.7mm_Pitch0.65mm',            # modelName
        modelName = 'TSSOP-28_4.4x9.7mm_Pitch0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSSOP-30_4.4x7.8mm_P0.5mm': Params(
        #
        # TSSOP30: plastic thin shrink small outline package; 30 leads; body width 4.4 mm (http://www.ti.com/lit/ds/symlink/bq78350.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSSOP-30_4.4x7.8mm_P0.5mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 7.8,         # body length
        E1 = 4.4,         # body width
        E = 6.7,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        npx = 15,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-30_4.4x7.8mm_P0.5mm',            # modelName
        modelName = 'TSSOP-30_4.4x7.8mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        ),

    'TSSOP-38_6.1x12.5mm_P0.65mm': Params(
        #
        # TSSOP38: plastic thin shrink small outline package; 38 leads; body width 6.1 mm (http://www.ti.com/lit/ds/symlink/msp430g2744.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is TSSOP-38_6.1x12.5mm_P0.65mm.kicad_mod
        # 
        the = 9.0,         # body angle in degrees
        tb_s = 0.15,       # top part of body is that much smaller
        c = 0.1,           # pin thickness, body center part height
        R1 = 0.1,          # pin upper corner, inner radius
        R2 = 0.1,          # pin lower corner, inner radius
        S  = 0.1,          # pin top flat part length (excluding corner arc)
#        L = 0.65,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.05,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        D1 = 12.5,         # body length
        E1 = 6.1,         # body width
        E = 8.4,          # body overall width
        A1 = 0.1,          # body-board separation
        A2 = 1.5,          # body height
        b = 0.21,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        npx = 19,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        old_modelName = 'TSSOP-38_6.1x12.5mm_P0.65mm',            # modelName
        modelName = 'TSSOP-38_6.1x12.5mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        ),

}

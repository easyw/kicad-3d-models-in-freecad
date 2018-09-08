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
}

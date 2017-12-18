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
    footprint_dir="Housings_SSOP.pretty"
    lib_name = "SSOP"

    body_color_key = "black body"
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"

part_params = {
        'SSOP_20': Params( # 5.6x7.2, pitch 0.65 20pin 2.0mm height
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
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.9,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='ssop_20_53x72_p065', #modelName
        modelName ='ssop_20_53x72_p065', #modelName
        rotation = 0, # rotation if required
        ),
    'SSOP_20_Pad': Params( # 5.6x7.2, pitch 0.65 20pin 2.0mm height
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
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.001,  # body-board separation
        A2 = 1.999,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (5.0,3.0), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='ssop_20_53x72_pad_p065', #modelName
        modelName ='ssop_20_53x72_pad_p065', #modelName
        rotation = 0, # rotation if required
        ),
}

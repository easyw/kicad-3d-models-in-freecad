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
    # footprint_dir="Diodes_SMD.pretty"
    # lib_name = "Diodes_SMD"

    footprint_dir="Diode_SMD.pretty"
    lib_name = "Diode_SMD"

    body_color_key = "black body"
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"

part_params = {
    'D_SOD-123': Params( # from http://www.nxp.com/documents/outline_drawing/SOD123.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.20,        # pin thickness, body center part height
        R1 = 0.12,       # pin upper corner, inner radius
        R2 = 0.12,       # pin lower corner, inner radius
        S = 0.0,       # pin top flat part length (excluding corner arc)
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        D1 = 2.75,       # body length
        E1 = 1.6,       # body width
        E = 2.65,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.15,  # body height
        b = 0.65,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        old_modelName = 'D_SOD-123', #modelName
        modelName = 'D_SOD-123', #modelName
        rotation = 0, # rotation if required
        ),
    'D_SOD-323': Params( # from http://www.nxp.com/documents/outline_drawing/SOD123.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.07,       # pin upper corner, inner radius
        R2 = 0.07,       # pin lower corner, inner radius
        S = 0.0,       # pin top flat part length (excluding corner arc)
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        D1 = 1.7,       # body length
        E1 = 1.25,       # body width
        E = 2.05,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        old_modelName = 'D_SOD-323', #modelName
        modelName = 'D_SOD-323', #modelName
        rotation = 0, # rotation if required
        ),
    'D_SOT-23': Params( # http://www.ti.com/lit/ml/mpds026k/mpds026k.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.0,       # pin top flat part length (excluding corner arc)
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.0,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        D1 = 3.0,       # body length
        E1 = 1.4,       # body width
        E = 2.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.40,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2,4,6), #no pin excluded
        old_modelName = 'D_SOT-23', #modelName
        modelName = 'D_SOT-23', #modelName
        rotation = -90, # rotation if required
        ),
}

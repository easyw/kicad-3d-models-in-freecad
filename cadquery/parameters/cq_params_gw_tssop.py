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

from collections import namedtuple
import cq_params_gw_soic  # modules parameters
from cq_params_gw_soic import *

all_params_tssop = {
    'TSSOP_14': Params( # 5.0x4.4, pitch 0.65 14pin 1.2mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.25,     # first pin indicator distance from edge
        fp_z = 0.15,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 7,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'tssop_14_50x44_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'tssop'
        ),
}


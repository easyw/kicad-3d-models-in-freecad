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
import cq_parameters_soic  # modules parameters
from cq_parameters_soic import *

destination_dir="/GullWings_packages"
# destination_dir="./"

all_params_sod = {

}
kicad_naming_params_sod = {
	'D_SOD-123': Params( # from http://www.nxp.com/documents/outline_drawing/SOD123.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.20,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        D1 = 1.6,       # body length
        E1 = 2.75,       # body width
        E = 3.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.15,  # body height
        b = 0.65,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 1,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        modelName = 'D_SOD-123', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SOD'
        ),
    
}
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


all_params_ssop = {
    'QSOP-24_3.9x8.7mm_Pitch0.635mm': Params( # 3.9x8.7, pitch 0.635 24pin 1.5mm height
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.17,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 8.7,             # body length
        E1 = 3.9,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.17,            # body-board separation
        A2 = 1.47,            # body height
        b = 0.25,             # pin width
        e = 0.635,            # pin (center-to-center) distance
        npx = 12,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'QSOP-24_3.9x8.7mm_Pitch0.635mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-20_5.3x7.2mm_Pitch0.65mm': Params( # 5.3x7.2, pitch 0.65 20pin 2.0mm height
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
        D1 = 6.9,       # body length
        E1 = 5.3,       # body width
        E = 7.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.9,  # body height
        b = 0.30,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SSOP-20_5.3x7.2mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-8-1EP_3x3mm_Pitch0.65mm': Params( # 3x3, pitch 0.65 8pin 1.0mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 3.0,       # body length
        E1 = 3.0,       # body width
        E = 4.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.001,  # body-board separation
        A2 = 0.999,  # body height
        b = 0.33,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (1.7,1.7), # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='MSOP-8-1EP_3x3mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-14_4.4x5mm_Pitch0.65mm': Params( # 5.0x4.4, pitch 0.65 14pin 1.1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.3,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.65,     # first pin indicator radius
        fp_d = 0.15,     # first pin indicator distance from edge
        fp_z = 0.10,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 7,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-14_4.4x5mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
        
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
        modelName ='ssop_20_53x72_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'SSOP'
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
        modelName ='ssop_20_53x72_pad_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
}
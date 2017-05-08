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
import cq_parameters  # modules parameters
from cq_parameters import *

destination_dir="/QFN_packages"
# destination_dir="./"
footprints_dir_diodes="Diodes_SMD.pretty"
##footprints_dir=None #to exclude importing of footprints

all_params_diode = {

}
kicad_naming_params_diode = {
        'D_0603': Params( # from http://datasheets.avx.com/schottky.pdf
        c = 0.8,        # pin thickness, not used for concave pins
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.12,     # first pin indicator radius
        fp_d = 0.03,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 1.6,       # body overall length
        E = 0.9,       # body overall width
        A1 = 0.03,  # body-board separation  maui to check
        A2 = 0.6,  # body height
        b = 0.7,  # pin width
        e = 0.0,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        ps = 'concave',   # rounded pads
        npx = 0,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'D_0603', #modelName 
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_0805': Params( # from http://datasheets.avx.com/schottky.pdf
        c = 0.8,        # pin thickness, not used for concave pins
#        K=0.2,          # Fillet radius for pin edges
        L = 0.45,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.06,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 1.3,       # body overall width
        A1 = 0.03,  # body-board separation  maui to check
        A2 = 0.74,  # body height
        b = 1.0,  # pin width
        e = 0.0,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        ps = 'concave',   # rounded pads
        npx = 0,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'D_0805', #modelName 
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_1206': Params( # from http://datasheets.avx.com/schottky.pdf
        c = 0.8,        # pin thickness, not used for concave pins
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.4,       # body overall length
        E = 1.9,       # body overall width
        A1 = 0.03,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 1.6,  # pin width
        e = 0.0,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        ps = 'concave',   # rounded pads
        npx = 0,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'D_1206', #modelName 
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_2010': Params( # from http://datasheets.avx.com/schottky.pdf
        c = 0.8,        # pin thickness, not used for concave pins
#        K=0.2,          # Fillet radius for pin edges
        L = 0.95,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.5,       # body overall length
        E = 2.2,       # body overall width
        A1 = 0.05,  # body-board separation  maui to check
        A2 = 0.86,  # body height
        b = 1.6,  # pin width
        e = 0.0,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        ps = 'concave',   # rounded pads
        npx = 0,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'D_2010', #modelName 
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_2114': Params( # from http://datasheets.avx.com/schottky.pdf
        c = 0.8,        # pin thickness, not used for concave pins
#        K=0.2,          # Fillet radius for pin edges
        L = 1.15,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.2,       # body overall length
        E = 3.6,       # body overall width
        A1 = 0.05,  # body-board separation  maui to check
        A2 = 0.95,  # body height
        b = 3.01,  # pin width
        e = 0.0,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        ps = 'concave',   # rounded pads
        npx = 0,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'D_2114', #modelName 
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_3220': Params( # from http://datasheets.avx.com/schottky.pdf
        c = 0.8,        # pin thickness, not used for concave pins
#        K=0.2,          # Fillet radius for pin edges
        L = 1.95,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.15,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.05,  # body-board separation  maui to check
        A2 = 0.95,  # body height
        b = 3.9,  # pin width
        e = 0.0,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        ps = 'concave',   # rounded pads
        npx = 0,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'D_3220', #modelName 
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_SOD-110': Params( # from http://www.nxp.com/documents/outline_drawing/SOD110.pdf
        c = 0.8,        # pin thickness, not used for concave pins
#        K=0.2,          # Fillet radius for pin edges
        L = 0.45,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.02, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 1.25,       # body overall width
        A1 = 0.1,  # body-board separation  maui to check
        A2 = 1.6,  # body height
        b = 0.9,  # pin width
        e = 0.0,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        ps = 'cshaped',   # rounded pads
        npx = 0,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'D_SOD-110', #modelName 
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
}
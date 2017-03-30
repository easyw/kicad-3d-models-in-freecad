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

import collections
from collections import namedtuple

destination_dir="/QFN_packages"
# destination_dir="./"
footprints_dir="Housings_DFN_QFN.pretty"
##footprints_dir=None #to exclude importing of footprints
#footprints_dir must be a subdir of the script DIR

def namedtuple_with_defaults(typename, field_names, default_values=()):
    
    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T

Params =namedtuple_with_defaults ("Params", [
    'c',    # pin thickness, body center part height
#    'K',    # Fillet radius for pin edges
    'L',    # pin top flat part length (including fillet radius)
    'fp_r', # first pin indicator radius, set to 0.0 to remove first pin indicator
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges
    'cce',  # chamfer of the epad 1st pin corner
    'D',    # body overall lenght
    'E',    # body overall width
    'A1',   # body-board separation
    'A2',   # body height
    'b',    # pin width
    'e',    # pin (center-to-center) distance
    'm',    # margin between pins and body  
    'sq',   # square pads True/False
    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'epad',  # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    'excluded_pins', #pins to exclude
    'molded', # molded = True, omitted -> None
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefixD2 = params.epad[0]
])
    
kicad_naming_params_qfn = {
    'DFN-6-1EP_2x2mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        sq = False,   # square pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.37,0.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_2x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN-6-1EP_2x2mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1118D.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.25,        # pin top flat part length (including fillet radius)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.62,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body  
        sq = False,   # square pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.64,0.9), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_2x2mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
#     'DFN-6-1EP_3x3mm_Pitch0.95mm': Params( # from https://www.onsemi.com/pub/Collateral/506AX.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.5,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.85,  # body height
#         b = 0.35,  # pin width
#         e = 0.95,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = True,   # square pads
#         npx = 3,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.0,1.2), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-6-1EP_3x3mm_Pitch0.95mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8_2x2mm_Pitch0.5mm': Params( # from https://www.onsemi.com/pub/Collateral/506AQ.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 2.0,       # body overall length
#         E = 2.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = None, # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8_2x2mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_2x2mm_Pitch0.5mm': Params( # from https://www.onsemi.com/pub/Collateral/506AQ.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.35,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 2.0,       # body overall length
#         E = 2.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (1.2,0.6), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_2x2mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_2x2mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_8_05-08-1719.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
#         D = 2.0,       # body overall length
#         E = 2.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.23,  # pin width
#         e = 0.45,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (1.37,0.64), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_2x2mm_Pitch0.45mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_2x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081702_C_DDB8.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 2.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.15,0.56), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_2x3mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_3x2mm_Pitch0.5mm': Params( # http://www.onsemi.com/pub/Collateral/517DH.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 2.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (1.4,1.4), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_3x2mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_3x2mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_8_05-08-1718.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator DFN-8-1EP_3x2mm_Pitch0
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 2.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.23,  # pin width
#         e = 0.45,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (1.65,1.35), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_3x2mm_Pitch0.45mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_8_05-08-1698.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.38,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_3x3mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_3x3mm_Pitch0.65mm': Params( # from https://www.onsemi.com/pub/Collateral/506BY.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.3,1.5), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_3x3mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_4x4mm_Pitch0.8mm': Params( # from https://www.onsemi.com/pub/Collateral/488AF.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.3,  # pin width
#         e = 0.8,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.06,2.4), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_4x4mm_Pitch0.8mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-8-1EP_6x5mm_Pitch1.27mm': Params( # from http://www.onsemi.com/pub/Collateral/506CG.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 6.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.85,  # body height
#         b = 0.4,  # pin width
#         e = 1.27,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.0,4.0), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-8-1EP_6x5mm_Pitch1.27mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-10-1EP_2x3mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/506DH.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator DFN-8-1EP_3x2mm_Pitch
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 2.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 5,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.4,0.6), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-10-1EP_2x3mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-10-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_10_05-08-1699.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.50,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 5,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.38,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-10-1EP_3x3mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-12-1EP_2x3mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_12_05-08-1723.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator DFN-8-1EP_3x2mm_Pitch
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 2.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.23,  # pin width
#         e = 0.45,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.39,0.64), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-12-1EP_2x3mm_Pitch0.45mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-12-1EP_3x3mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_12_05-08-1725.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.23,  # pin width
#         e = 0.45,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (2.25,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-12-1EP_3x3mm_Pitch0.45mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-12-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_12_05-08-1695.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (3.3,1.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-12-1EP_3x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-12-1EP_4x4mm_Pitch0.5mm': Params( # http://cds.linear.com/docs/en/packaging/05081733_A_DF12.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (3.38,2.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-12-1EP_4x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-12-1EP_4x4mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/506CE.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (3.4,2.5), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-12-1EP_4x4mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-14-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_14_05-08-1708.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (3.3,1.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-14-1EP_3x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-14-1EP_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081963_0_DFN14%2812%29.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (3.6,2.86), # e Pad #epad = None, # e Pad from footprint
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-14-1EP_4x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-16-1EP_3x4mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_16_05-08-1732.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.23,  # pin width
#         e = 0.45,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (3.3,1.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-16-1EP_3x4mm_Pitch0.45mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-16-1EP_3x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_16_05-08-1706.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.4,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-16-1EP_3x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-16-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081707_A_DHD16.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.34,2.44), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-16-1EP_4x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-16-1EP_5x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_16_05-08-1709.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (3.99,3.45), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-16-1EP_5x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-18-1EP_3x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081955_0_DHC18.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 9,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.4,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-18-1EP_3x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-18-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081955_0_DHC18.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 9,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.34,2.44), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-18-1EP_4x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-20-1EP_5x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/505AB.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 10,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.13,3.13), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-20-1EP_5x6mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-22-1EP_5x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/506AF.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 11,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.13,3.13), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-22-1EP_5x6mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-24-1EP_4x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_24_05-08-1864.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 12,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (6.43,2.64), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-24-1EP_4x7mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-32-1EP_4x7mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_32_05-08-1734.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 16,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (6.43,2.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-32-1EP_4x7mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-44-1EP_5x8.9mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/506BU.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 8.9,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.85,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 22,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (8.3,3.6), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-44-1EP_5x8.9mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'DFN-S-8-1EP_6x5mm_Pitch1.27mm': Params( # from http://www.onsemi.com/pub/Collateral/506BG.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 6.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.5,  # pin width
#         e = 1.27,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (4.0,3.0), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'DFN-S-8-1EP_6x5mm_Pitch1.27mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-12-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_12_%2005-08-1855.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.05    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 3,  # number of pins along X axis (width)
#         npy = 3,  # number of pins along y axis (length)
#         #epad = (1.65,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         molded = True, # molded = True, omitted -> None
#         modelName = 'QFN-12-1EP_3x3mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-16-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_16_05-08-1700.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (1.65,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-16-1EP_3x3mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-16-1EP_4x4mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_16_05-08-1692.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (2.15,2.15), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-16-1EP_4x4mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-16-1EP_5x5mm_Pitch0.8mm': Params( # from http://www.onsemi.com/pub/Collateral/485AC.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.3,  # pin width
#         e = 0.8,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (2.7,2.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-16-1EP_5x5mm_Pitch0.8mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-20-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1742.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (2.65,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-20-1EP_3x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-20-1EP_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1710.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 5,  # number of pins along X axis (width)
#         npy = 5,  # number of pins along y axis (length)
#         epad = (2.45,2.45), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-20-1EP_4x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-20-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1711.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (3.65,2.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-20-1EP_4x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-20-1EP_5x5mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1818.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 5,  # number of pins along X axis (width)
#         npy = 5,  # number of pins along y axis (length)
#         epad = (2.7,2.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-20-1EP_5x5mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-24_3x3mm_Pitch0.4mm': Params( # from https://www.invensense.com/products/motion-tracking/9-axis/mpu-9250/
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 1.0,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 6,  # number of pins along y axis (length)
#         epad = None, # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-24_3x3mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-24_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UF24%29%20QFN%2005-08-1697%20Rev%20B.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 6,  # number of pins along y axis (length)
#         epad = None, # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-24_4x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-24-1EP_3x3mm_Pitch0.4mm': Params( # from https://www.invensense.com/products/motion-tracking/9-axis/mpu-9250/
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 1.0,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 6,  # number of pins along y axis (length)
#         epad = (1.7,1.54), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-24-1EP_3x3mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-24-1EP_3x4mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_24_05-08-1745.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 5,  # number of pins along y axis (length)
#         epad = (2.65,1.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-24-1EP_3x4mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-24-1EP_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UF24%29%20QFN%2005-08-1697%20Rev%20B.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 6,  # number of pins along y axis (length)
#         epad = (2.45,2.45), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-24-1EP_4x4mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-24-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_24_05-08-1696.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 5,  # number of pins along y axis (length)
#         epad = (3.65,2.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-24-1EP_4x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-24-1EP_5x5mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UH24%29%20QFN%2005-08-1747%20Rev%20A.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 6,  # number of pins along X axis (width)
#         npy = 6,  # number of pins along y axis (length)
#         epad = (3.2,3.2), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-24-1EP_5x5mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-28-1EP_3x6mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081926_0_UDE28.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 10,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (4.75,1.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-28-1EP_3x6mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-28-1EP_4x4mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_28_05-08-1721.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 7,  # number of pins along y axis (length)
#         epad = (2.64,2.64), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-28-1EP_4x4mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-28-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081712_C_UFD28.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 6,  # number of pins along y axis (length)
#         epad = (3.65,2.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-28-1EP_4x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-28-1EP_5x5mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/485FH.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 7,  # number of pins along y axis (length)
#         epad = (3.15,3.15), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-28-1EP_5x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-28-1EP_5x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/485FH.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 6,  # number of pins along y axis (length)
#         epad = (4.65,3.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-28-1EP_5x6mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-28-1EP_6x6mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/560AC.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 6.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 7,  # number of pins along y axis (length)
#         epad = (4.55,4.55), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-28-1EP_6x6mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-32-1EP_4x4mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/485CD.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 8,  # number of pins along y axis (length)
#         epad = (2.7,2.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-32-1EP_4x4mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-32-1EP_5x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_32_05-08-1693.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 8,  # number of pins along y axis (length)
#         epad = (3.45,3.45), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-32-1EP_5x5mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-32-1EP_7x7mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/485ED.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.55,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 7.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.85,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 8,  # number of pins along X axis (width)
#         npy = 8,  # number of pins along y axis (length)
#         epad = (4.7,4.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-32-1EP_7x7mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-36-1EP_5x6mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UHE36%29%20QFN%2005-08-1876%20Rev%20%C3%98.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 10,  # number of pins along X axis (width)
#         npy = 8,  # number of pins along y axis (length)
#         epad = (4.6,3.6), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-36-1EP_5x6mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-36-1EP_6x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/485EC.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 6.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 9,  # number of pins along X axis (width)
#         npy = 9,  # number of pins along y axis (length)
#         epad = (4.4,4.4), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-36-1EP_6x6mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-38-1EP_4x6mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_38_05-08-1750.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 12,  # number of pins along X axis (width)
#         npy = 7,  # number of pins along y axis (length)
#         epad = (4.65,2.65), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-38-1EP_4x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-38-1EP_5x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_38_05-08-1701.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 12,  # number of pins along X axis (width)
#         npy = 7,  # number of pins along y axis (length)
#         epad = (5.15,3.15), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-38-1EP_5x7mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-40-1EP_5x5mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/05081746_B_UH40.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.1,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 10,  # number of pins along X axis (width)
#         npy = 10,  # number of pins along y axis (length)
#         epad = (3.5,3.5), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-40-1EP_5x5mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-40-1EP_6x6mm_Pitch0.5mm': Params( # 6x6, 0.5 pitch, 40 pins, 1.0mm height  QFN44 p005
#         #datasheet example - http://www.ti.com/lit/ds/symlink/drv8308.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.1, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 6.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.98,  # body height
#         b = 0.23,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = True,   # square pads
#         npx = 10,  # number of pins along X axis (width)
#         npy = 10,  # number of pins along y axis (length)
#         epad = (4.1,4.1), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-40-1EP_6x6mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-42-1EP_5x6mm_Pitch0.4mm': Params( # 5x6, 0.4 pitch, 42 pins, 1.0mm height  QFN42 p004
#         #datasheet example - http://www.ti.com/lit/ds/symlink/drv8308.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.98,  # body height
#         b = 0.23,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 12,  # number of pins along X axis (width)
#         npy = 9,  # number of pins along y axis (length)
#         epad = (4.7,3.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-42-1EP_5x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-44-1EP_7x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_44_05-08-1763.pdf 
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 7.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 11,  # number of pins along X axis (width)
#         npy = 11,  # number of pins along y axis (length)
#         epad = (5.15,5.15), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-44-1EP_7x7mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-44-1EP_8x8mm_Pitch0.65mm': Params( # 8x8, 0.65 pitch, 44 pins, 1.0mm height  QFN44 p065 microchip
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 8.0,       # body overall length
#         E = 8.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.98,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 11,  # number of pins along X axis (width)
#         npy = 11,  # number of pins along y axis (length)
#         epad = (6.45,6.45), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-44-1EP_8x8mm_Pitch0.65mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-48-1EP_7x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_48_05-08-1704.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 7.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 12,  # number of pins along X axis (width)
#         npy = 12,  # number of pins along y axis (length)
#         epad = (5.15,5.15), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-48-1EP_7x7mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-52-1EP_7x8mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_52_05-08-1729.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 8.0,       # body overall length
#         E = 7.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 14,  # number of pins along X axis (width)
#         npy = 12,  # number of pins along y axis (length)
#         epad = (6.45,5.41), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-52-1EP_7x8mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-56-1EP_7x7mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/485BT-01.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 7.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 14,  # number of pins along X axis (width)
#         npy = 14,  # number of pins along y axis (length)
#         epad = (5.7,5.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-56-1EP_7x7mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-56-1EP_7x7mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/485BT-01.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
#         D = 7.0,       # body overall length
#         E = 7.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 14,  # number of pins along X axis (width)
#         npy = 14,  # number of pins along y axis (length)
#         epad = (5.7,5.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-56-1EP_7x7mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'QFN-64-1EP_9x9mm_Pitch0.5mm': Params( # 9x9, 0.5 pitch, 64 pins, 0.9mm height  QFN64 p05 microchip
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
#         D = 9.0,       # body overall length
#         E = 9.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.73,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 16,  # number of pins along X axis (width)
#         npy = 16,  # number of pins along y axis (length)
#         epad = (7.15,7.15), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'QFN-64-1EP_9x9mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-10_1.4x1.8mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/523AQ.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.1,      #0.45 chamfer of the epad 1st pin corner
#         D = 1.8,       # body overall length
#         E = 1.4,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.55,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 2,  # number of pins along X axis (width)
#         npy = 3,  # number of pins along y axis (length)
#         epad = None, # e Pad #epad = None, # e Pad
#         molded = True,
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-10_1.4x1.8mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-16-1EP_3x3mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/523AJ.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.5,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = True,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (1.95,1.95), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-16-1EP_3x3mm_Pitch0.5mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-16-1EP_4x4mm_Pitch0.65mm': Params( # from footprint
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.6,  # body height
#         b = 0.3,  # pin width
#         e = 0.65,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = True,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 4,  # number of pins along y axis (length)
#         epad = (2.7,2.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-16-1EP_4x4mm_Pitch0.65mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-20-1EP_3x3mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/523AL.PDF
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 3.0,       # body overall length
#         E = 3.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.5,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 5,  # number of pins along X axis (width)
#         npy = 5,  # number of pins along y axis (length)
#         epad = (1.8,1.8), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-20-1EP_3x3mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-20-1EP_4x4mm_Pitch0.5mm': Params( # from footprint
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.6,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 5,  # number of pins along X axis (width)
#         npy = 5,  # number of pins along y axis (length)
#         epad = (2.8,2.8), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-20-1EP_4x4mm_Pitch0.5mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-28-1EP_4x4mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/%28PF28%29%20UTQFN%2005-08-1759%20Rev%20%C3%98.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 4.0,       # body overall length
#         E = 4.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.55,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 7,  # number of pins along X axis (width)
#         npy = 7,  # number of pins along y axis (length)
#         epad = (2.64,2.64), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-28-1EP_4x4mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-40-1EP_5x5mm_Pitch0.4mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/41364E.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 5.0,       # body overall length
#         E = 5.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.5,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 10,  # number of pins along X axis (width)
#         npy = 10,  # number of pins along y axis (length)
#         epad = (3.7,3.7), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-40-1EP_5x5mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'UQFN-48-1EP_6x6mm_Pitch0.4mm': Params( # 9x9, 0.5 pitch, 64 pins, 0.9mm height  QFN64 p05 microchip
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.4,        # pin top flat part length (including fillet radius)
#         fp_r = 0.5,     # first pin indicator radius
#         fp_d = 0.2,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
#         D = 6.0,       # body overall length
#         E = 6.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.9,  # body height
#         b = 0.2,  # pin width
#         e = 0.4,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 12,  # number of pins along X axis (width)
#         npy = 12,  # number of pins along y axis (length)
#         epad = (4.5,4.5), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
#     'VDFN-8-1EP_2x2mm_Pitch0.5mm': Params( # from http://www.s-manuals.com/pdf/datasheet/r/t/rt9012_richtek.pdf
#         c = 0.2,        # pin thickness, body center part height
# #        K=0.2,          # Fillet radius for pin edges
#         L = 0.35,        # pin top flat part length (including fillet radius)
#         fp_r = 0.4,     # first pin indicator radius
#         fp_d = 0.08,     # first pin indicator distance from edge
#         fp_z = 0.01,     # first pin indicator depth
#         ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
#         cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
#         D = 2.0,       # body overall length
#         E = 2.0,       # body overall width
#         A1 = 0.02,  # body-board separation  maui to check
#         A2 = 0.75,  # body height
#         b = 0.25,  # pin width
#         e = 0.5,  # pin (center-to-center) distance
#         m = 0.0,  # margin between pins and body  
#         sq = False,   # square pads
#         npx = 4,  # number of pins along X axis (width)
#         npy = 0,  # number of pins along y axis (length)
#         epad = (1.125,0.525), # e Pad #epad = None, # e Pad
#         excluded_pins = None, #no pin excluded
#         modelName = 'VDFN-8-1EP_2x2mm_Pitch0.5mm', #modelName
#         rotation = -90, # rotation if required
#         dest_dir_prefix = ''
#         ),
 }

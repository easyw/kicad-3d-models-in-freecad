# -*- coding: utf-8 -*-
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

destination_dir="/QFN_packages"
# destination_dir="./"


Params = namedtuple("Params", [
    'c',    # pin thickness, body center part height
#    'K',    # Fillet radius for pin edges
    'L',    # pin top flat part length (including fillet radius)
    'fp_s',  # True for circular pinmark, False for square pinmark (useful for diodes)
    'fp_r', # first pin indicator radius, set to 0.0 to remove first pin indicator
    'fp_d', # first pin indicator distance from edge
    'fp_dx', # first pin indicator distance from X edge
    'fp_dy', # first pin indicator distance from Y edge
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
    'ps',   # pad shape square, rounded, concave or custom
    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'epad',  # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    'epad_offsetX',  # offset X for exposed pad
    'epad_offsetY',  # offset X for exposed pad
    'epad_n', # number of exposed pads, specified as tuple (along X axis, along Y axis) in case a matrix of them is needed.
    'epad_pitch', # epad center to epad center, specified as tuple (along X axis, along Y axis)
    'excluded_pins', #pins to exclude
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix', #destination dir prefixD2 = params.epad[0],
    'body_color_key', # body color key if not None
    'pin_shapes',   # coords for pin shapes as [(x,y)]
])
Params.__new__.__defaults__ = (None,) * len(Params._fields)

all_params_qfn = {
    'AMS_LGA-10-1EP_2.7x4mm_P0.6mm': Params(
        #example - http://ams.com/documents/20143/36005/CCS811_DS000459_6-00.pdf/c7091525-c7e5-37ac-eedb-b6c6828b0dcf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,        # body overall length
        E = 2.7,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 1.1,       # body height
        b = 0.3,        # pin width
        e = 0.6,        # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 5,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = (2.4, 1.2), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'AMS_LGA-10-1EP_2.7x4mm_P0.6mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'LGA-12_2x2mm_P0.5mm': Params(
        #example -
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,        # body overall length
        E = 2.0,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 1.0,       # body height
        b = 0.25,       # pin width
        e = 0.5,        # pin (center-to-center) distance
        m = 0.1,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 4,        # number of pins along X axis (width)
        npy = 2,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'LGA-12_2x2mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'LGA-16_3x3mm_P0.5mm': Params(
        #example - http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00250937.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.35,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,        # body overall length
        E = 3.0,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 1.0,       # body height
        b = 0.25,       # pin width
        e = 0.5,        # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 4,        # number of pins along X axis (width)
        npy = 4,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'LGA-16_3x3mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y': Params(
        #example - http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00250937.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.35,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,        # body overall length
        E = 3.0,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 1.0,       # body height
        b = 0.25,       # pin width
        e = 0.5,        # pin (center-to-center) distance
        m = 0.1,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 5,        # number of pins along X axis (width)
        npy = 3,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y': Params(
        #example - http://www.st.com/resource/en/datasheet/l3gd20.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.40,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,        # body overall length
        E = 4.0,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 1.0,       # body height
        b = 0.30,       # pin width
        e = 0.65,        # pin (center-to-center) distance
        m = 0.1,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 4,        # number of pins along X axis (width)
        npy = 4,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'LGA-24L_3x3.5mm_P0.43mm': Params(
        #example - http://www.st.com/resource/en/datasheet/l3gd20.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.35,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,        # body overall length
        E = 3.5,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 1.0,       # body height
        b = 0.23,       # pin width
        e = 0.43,       # pin (center-to-center) distance
        m = 0.1,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 4,        # number of pins along X axis (width)
        npy = 8,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'LGA-24L_3x3.5mm_P0.43mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'LGA-28_5.2x3.8mm_P0.5mm': Params(
        #example - http://www.st.com/resource/en/datasheet/l3gd20.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.475,      # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.8,        # body overall length
        E = 5.2,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 1.0,       # body height
        b = 0.25,       # pin width
        e = 0.50,       # pin (center-to-center) distance
        m = 0.1,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 4,        # number of pins along X axis (width)
        npy = 10,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'LGA-28_5.2x3.8mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'ST_HLGA-10_2.5x2.5mm_P0.6mm_LayoutBorder3x2y': Params(
        #example - https://www.st.com/resource/en/datasheet/lps25hb.pdf#page=46
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.45,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.5,        # body overall length
        E = 2.5,        # body overall width
        A1 = 0.025,     # body-board separation  maui to check
        A2 = 0.8,       # body height
        b = 0.30,       # pin width
        e = 0.6,        # pin (center-to-center) distance
        m = 0.1,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 4,        # number of pins along X axis (width)
        npy = 2,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'ST_HLGA-10_2.5x2.5mm_P0.6mm_LayoutBorder3x2y', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_LGA.3dshapes/'
    ),
    'LGA1633': Params( #3x3mm, 16-pin LGA package, 1.0mm height
        #example - http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00250937.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 1.0,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 3,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'lga16_3x3_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    'DFN622': Params( # 2x2, 0.65 pitch, 6 pins, 0.75mm height  DFN (DD / LTC)
        #Example - http://www.onsemi.com/pub_link/Collateral/NCP308-D.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.6,1.0), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'dfn6_2x2_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN8-33-50': Params( # 3x3, 0.5 pitch, 8 pins, 0.75mm height  DFN (DD / LTC)
        #Example - http://cds.linear.com/docs/en/datasheet/2875f.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7 - 0.25,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.38,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'dfn8_3x3_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN8-33-65': Params( # 3x3, 0.65 pitch, 8 pins, 1.0mm height  DFN (DD / LTC)
        #Example - http://www.st.com/web/en/resource/technical/document/datasheet/CD00001508.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 1.0,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.4,1.4), #(2.5,1.5), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'dfn8_3x3_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN823': Params( # 2x3, 0.5 pitch, 8 pins, 0.75mm height  DFN (DD / LTC)
        #Example - http://cds.linear.com/docs/en/datasheet/4365fa.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7 - 0.25,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.2,0.61), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'dfn8_2x3_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DHVQFN14': Params( #
        #Example - http://www.nxp.com/documents/outline_drawing/SOT762-1.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.5,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 1.0,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 2,  # number of pins along y axis (length)
        epad = (1.5,1.0), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DHVQFN14', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = ''
        ),
    'SOT891': Params( # 1x1, 0.35 pitch, 6 pins, 0.5mm height  DFN (DD / LTC)
        #Example - http://cds.linear.com/docs/en/datasheet/4365fa.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.05,      #0.45 chamfer of the epad 1st pin corner
        D = 1.0,       # body overall length
        E = 1.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.20,  # pin width
        e = 0.35,  # pin (center-to-center) distance
        m = 0.05,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'sot891_1x1_p035', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN865': Params( # 6x5, 1.27mm pitch, 8 pins, 1.0mm height  DFN
        #Example - https://www.everspin.com/file/217/download
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7 - 0.25,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 1,  # body height
        b = 0.4,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2,2), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'dfn8_6x5_p127', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'DFN1023': Params( # 2x3, 0.5mm pitch, 10 pins, 0.75mm height  DFN
        #Example - http://www.ti.com.cn/general/cn/docs/lit/getliterature.tsp?genericPartNumber=tps62177&fileType=pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3 - 0.15,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.025,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.4,0.84), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'dfn10_2x3_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN16': Params( # 3x3, 0.5 pitch, 16 pins, 1.0mm height  QFN16 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (1.7,1.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'qfn16_3x3_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN24': Params( # 4.15x4.15, 0.5 pitch, 24 pins, 1.0mm height  QFN24 p05 texas
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.15,       # body overall length
        E = 4.15,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = (2.45,2.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'qfn24_415x415_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN28': Params( # 6x6, 0.65 pitch, 28 pins, 0.9mm height QFN28 Microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 6,       # body overall length
        E = 6,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.38,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (3.7,3.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'qfn28_6x6_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN32': Params( # 5x5, 0.5 pitch, 32 pins, 1.0mm height  QFN32 p05 ATMEL
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.3,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = (3.6,3.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'qfn32_5x5_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN40': Params( # 6x6, 0.5 pitch, 40 pins, 1.0mm height  QFN44 p005
        #datasheet example - http://www.ti.com/lit/ds/symlink/drv8308.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        epad = (3.52,2.62), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'qfn40_6x6_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN44': Params( # 8x8, 0.65 pitch, 44 pins, 1.0mm height  QFN44 p065 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (6.45,6.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'qfn44_8x8_p065', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'QFN64': Params( # 9x9, 0.5 pitch, 64 pins, 0.9mm height  QFN64 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
        D = 9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.88,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (4.7,4.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'qfn64_9x9_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'TCPT1350': Params( # 2
        c = 0.47,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.7,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.95,  # body height
        b = 0.5,  # pin width
        e = 1.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'TCPT1350x01', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
}

kicad_naming_params_qfn = {
    'AVX_M620720': Params( # from http://datasheets.avx.com/ethertronics/AVX-E_M620720.pdf
        c = 0.3,        # pin thickness, body center part height
        L = 2,        # pin top flat part length (including fillet radius)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.04,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.0,      #0.45 chamfer of the epad 1st pin corner
        D = 6,       # body overall length
        E = 2,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 1.08,  # body height
        b = 1.005,  # pin width
        e = 4.995,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 2,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (0.89,2.0), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'AVX_M620720', #modelName
        body_color_key = 'white body',
        rotation = 0, # rotation if required
        dest_dir_prefix = '../RF_Antenna.3dshapes/'
        ),
    'UDFN-10_1.35x2.6mm_Pitch0.5mm': Params( # from http://www.st.com/content/ccc/resource/technical/document/datasheet/f2/11/8a/ed/40/31/40/56/DM00088292.pdf/files/DM00088292.pdf/jcr:content/translations/en.DM00088292.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.5,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.04,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.6,       # body overall length
        E = 1.35,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UDFN-10_1.35x2.6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-4-1EP_1x1mm_P0.65mm_EP0.5x0.5mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/MIC550x-300mA-Single-Output-LDO-in-Small-Packages-DS20006006A.pdf
        c = 0.025,      # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.2,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.08,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.0,      # epad chamfer
        D = 1.0,        # body overall length
        E = 1.0,        # body overall width
        A1 = 0.02,      # body-board separation  maui to check
        A2 = 0.55,      # body height
        b = 0.225,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'custom',  # pads shape
        pin_shapes = [
            [(-0.65/2-0.225/2, -0.5), (-0.65/2+0.225/2, -0.5), (-0.65/2+0.225/2, -0.5+0.07), (-0.3925, -0.25), (-0.65/2-0.225/2, -0.25)],
            [(0.65/2+0.225/2, -0.5), (0.65/2-0.225/2, -0.5), (0.65/2-0.225/2, -0.5+0.07), (0.3925, -0.25), (0.65/2+0.225/2, -0.25)],
            [(0.65/2+0.225/2, 0.5), (0.65/2-0.225/2, 0.5), (0.65/2-0.225/2, 0.5-0.07), (0.3925, 0.25), (0.65/2+0.225/2, 0.25)],
            [(-0.65/2-0.225/2, 0.5), (-0.65/2+0.225/2, 0.5), (-0.65/2+0.225/2, 0.5-0.07), (-0.3925, 0.25), (-0.65/2-0.225/2, 0.25)],
        ],
        npx = 2,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = (0.5,0.5,45), # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-4-1EP_1x1mm_P0.65mm_EP0.5x0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm': Params( # from http://www.onsemi.com/pub/Collateral/NCP133-D.PDF
        c = 0.025,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.2,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.15,      #0.45 chamfer of the epad 1st pin corner
        D = 1.2,       # body overall length
        E = 1.2,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.375,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (0.94,0.3), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'Balun_Johanson_0896BM15A0001': Params( # from http://www.onsemi.com/pub/Collateral/NCP133-D.PDF
        c = 0.7,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        #fp_d = 0.08,     # first pin indicator distance from edge.
        fp_dx = 0.15,     # first pin indicator distance from edge.
        fp_dy = 0.45,     # first pin indicator distance from edge.
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.15,      #0.45 chamfer of the epad 1st pin corner
        D = 2,       # body overall length
        E = 1.25,       # body overall width
        A1 = 0.0,  # body-board separation  maui to check
        A2 = 0.7,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        #epad = (0.94,0.3), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Balun_Johanson_0896BM15A0001', #modelName
        rotation = -90, # rotation if required,
        body_color_key = 'white body',
        dest_dir_prefix = '../RF_Converter.3dshapes/'
        ),
    'Balun_Johanson_0900PC15J0013': Params( # from https://www.johansontechnology.com/datasheets/0900PC15J0013/0900PC15J0013.pdf
        c = 1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.2,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        #fp_d = 0.08,     # first pin indicator distance from edge.
        fp_dx = 0.15,     # first pin indicator distance from edge.
        fp_dy = 0.45,     # first pin indicator distance from edge.
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.15,      #0.45 chamfer of the epad 1st pin corner
        D = 2,       # body overall length
        E = 1.25,       # body overall width
        A1 = 0.0,  # body-board separation  maui to check
        A2 = 1,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 1,  # number of pins along y axis (length)
        #epad = (0.94,0.3), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Balun_Johanson_0900PC15J0013', #modelName
        rotation = -90, # rotation if required,
        body_color_key = 'white body',
        dest_dir_prefix = '../RF_Converter.3dshapes/'
        ),
    'DFN-6-1EP_2x2mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.37,0.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_2x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-6-1EP_2x2mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1118D.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.25,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.62,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.64,0.9), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_2x2mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'TDFN-6-1EP_2.5x2.5mm_P0.65mm_EP1.3x2mm': Params( # from https://www.nve.com/Downloads/ab3.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0, # 0.05,   # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.1,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.5,        # body overall length
        E = 2.5,        # body overall width
        A1 = 0.05,      # body-board separation  maui to check
        A2 = 0.8,       # body height
        b = 0.3,        # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.00,       # margin between pins and body
        ps = 'square',  # square pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.0, 1.3), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'TDFN-6-1EP_2.5x2.5mm_P0.65mm_EP1.3x2mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/'
        ),
    'DFN-6-1EP_3x3mm_Pitch0.95mm': Params( # from https://www.onsemi.com/pub/Collateral/506AX.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.5,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.35,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.0,1.2), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_3x3mm_Pitch0.95mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-6-1EP_3x3mm_Pitch1mm': Params( # from https://www.silabs.com/documents/public/data-sheets/Si7020-A20.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.5,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.35,  # pin width
        e = 1.00,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.0,1.2), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_3x3mm_Pitch1mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-6-1EP_3x2mm_Pitch0.5mm': Params( # from https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-dfn/(DCB6)%20DFN%2005-08-1715%20Rev%20A.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.35,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_3x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8_2x2mm_Pitch0.5mm': Params( # from https://www.onsemi.com/pub/Collateral/506AQ.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8_2x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_2x2mm_Pitch0.5mm': Params( # from https://www.onsemi.com/pub/Collateral/506AQ.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.2,0.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_2x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
'DFN-8-1EP_2x2mm_P0.5mm_EP0.7x1.3mm': Params( # from https://www.onsemi.com/pub/Collateral/506AQ.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.2,0.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_2x2mm_P0.5mm_EP0.7x1.3mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),

    'DFN-8-1EP_2x2mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_8_05-08-1719.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.23,  # pin width
        e = 0.45,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.37,0.64), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_2x2mm_Pitch0.45mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_2x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081702_C_DDB8.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.15,0.56), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_2x3mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_3x2mm_Pitch0.5mm': Params( # http://www.onsemi.com/pub/Collateral/517DH.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.4,1.4), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_3x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_3x2mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_8_05-08-1718.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator DFN-8-1EP_3x2mm_Pitch0
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.23,  # pin width
        e = 0.45,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.65,1.35), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_3x2mm_Pitch0.45mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_8_05-08-1698.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.38,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_3x3mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_3x3mm_Pitch0.65mm': Params( # from https://www.onsemi.com/pub/Collateral/506BY.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.3,1.5), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_3x3mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_4x4mm_Pitch0.8mm': Params( # from https://www.onsemi.com/pub/Collateral/488AF.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.3,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.06,2.4), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_4x4mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-8-1EP_6x5mm_Pitch1.27mm': Params( # from http://www.onsemi.com/pub/Collateral/506CG.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.4,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.0,4.0), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_6x5mm_Pitch1.27mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-10-1EP_2x3mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/506DH.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator DFN-8-1EP_3x2mm_Pitch
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.4,0.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-10-1EP_2x3mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-10-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_10_05-08-1699.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.50,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.38,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-10-1EP_3x3mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-12-1EP_2x3mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_12_05-08-1723.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator DFN-8-1EP_3x2mm_Pitch
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.23,  # pin width
        e = 0.45,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.39,0.64), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-12-1EP_2x3mm_Pitch0.45mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-12-1EP_3x3mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_12_05-08-1725.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.23,  # pin width
        e = 0.45,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.25,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-12-1EP_3x3mm_Pitch0.45mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-12-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_12_05-08-1695.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.3,1.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-12-1EP_3x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-12-1EP_4x4mm_Pitch0.5mm': Params( # http://cds.linear.com/docs/en/packaging/05081733_A_DF12.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.38,2.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-12-1EP_4x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-12-1EP_4x4mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/506CE.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.4,2.5), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-12-1EP_4x4mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-14-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_14_05-08-1708.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.3,1.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-14-1EP_3x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-14-1EP_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081963_0_DFN14%2812%29.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.6,2.86), # e Pad #epad = None, # e Pad from footprint
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-14-1EP_4x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-16-1EP_3x4mm_Pitch0.45mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_16_05-08-1732.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.23,  # pin width
        e = 0.45,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.3,1.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-16-1EP_3x4mm_Pitch0.45mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-16-1EP_3x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_16_05-08-1706.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.4,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-16-1EP_3x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-16-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081707_A_DHD16.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.34,2.44), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-16-1EP_4x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-16-1EP_5x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_16_05-08-1709.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.99,3.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-16-1EP_5x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-18-1EP_3x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081955_0_DHC18.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 9,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.4,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-18-1EP_3x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-18-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081955_0_DHC18.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 9,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.34,2.44), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-18-1EP_4x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-20-1EP_5x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/505AB.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 10,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.13,3.13), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-20-1EP_5x6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'WQFN-20-1EP_4.5x2.5mm_Pitch0.5mm_EP2.9x1.0mm': Params( # from http://www.onsemi.com/pub/Collateral/505AB.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      # chamfer of the epad 1st pin corner
        D = 4.5,       # body overall length
        E = 2.5,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.78,  # body height
        b = 0.24,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 2,  # number of pins along y axis (length)
        epad = (2.9,1.0), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WQFN-20-1EP_4.5x2.5mm_Pitch0.5mm_EP2.9x1.0mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-22-1EP_5x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/506AF.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 11,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.13,3.13), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-22-1EP_5x6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-24-1EP_4x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_24_05-08-1864.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 12,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (6.43,2.64), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-24-1EP_4x7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-32-1EP_4x7mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/DFN_32_05-08-1734.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 16,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (6.43,2.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-32-1EP_4x7mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-44-1EP_5x8.9mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/506BU.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 8.9,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 22,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (8.3,3.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-44-1EP_5x8.9mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-S-8-1EP_6x5mm_Pitch1.27mm': Params( # from http://www.onsemi.com/pub/Collateral/506BG.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.5,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (4.0,3.0), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-S-8-1EP_6x5mm_Pitch1.27mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'MLF-6-1EP_1.6x1.6mm_P0.5mm_EP0.5x1.26mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/mic5353.pdf
        c = 0.15,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 1.6,       # body overall length
        E = 1.6,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.55,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.26,0.5), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'MLF-6-1EP_1.6x1.6mm_P0.5mm_EP0.5x1.26mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-12-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_12_%2005-08-1855.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 3,  # number of pins along y axis (length)
        epad = (1.65,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-12-1EP_3x3mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-16-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_16_05-08-1700.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (1.65,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-16-1EP_3x3mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-16-1EP_4x4mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_16_05-08-1692.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (2.15,2.15), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-16-1EP_4x4mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-16-1EP_5x5mm_Pitch0.8mm': Params( # from http://www.onsemi.com/pub/Collateral/485AC.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.3,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (2.7,2.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-16-1EP_5x5mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-20-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1742.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (2.65,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-20-1EP_3x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-20-1EP_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1710.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        epad = (2.45,2.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-20-1EP_4x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-20-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1711.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (3.65,2.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-20-1EP_4x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-20-1EP_5x5mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_20_05-08-1818.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        epad = (2.7,2.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-20-1EP_5x5mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-24_3x3mm_Pitch0.4mm': Params( # from https://www.invensense.com/products/motion-tracking/9-axis/mpu-9250/
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 1.0,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24_3x3mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-24_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UF24%29%20QFN%2005-08-1697%20Rev%20B.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24_4x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-24-1EP_3x3mm_Pitch0.4mm': Params( # from https://www.invensense.com/products/motion-tracking/9-axis/mpu-9250/
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 1.0,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = (1.7,1.54), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_3x3mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-24-1EP_3x4mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_24_05-08-1745.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        epad = (2.65,1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_3x4mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-24-1EP_4x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UF24%29%20QFN%2005-08-1697%20Rev%20B.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = (2.45,2.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_4x4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-24-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_24_05-08-1696.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        epad = (3.65,2.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_4x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-24-1EP_5x5mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UH24%29%20QFN%2005-08-1747%20Rev%20A.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = (3.2,3.2), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_5x5mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-28-1EP_3x6mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081926_0_UDE28.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 10,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (4.75,1.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_3x6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-28-1EP_4x4mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_28_05-08-1721.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (2.64,2.64), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_4x4mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-28-1EP_4x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081712_C_UFD28.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = (3.65,2.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_4x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-28-1EP_5x5mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/485FH.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (3.15,3.15), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_5x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-28-1EP_5x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/485FH.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        epad = (4.65,3.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_5x6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-28-1EP_6x6mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/560AC.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (4.55,4.55), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_6x6mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-28-1EP_6x6mm_P0.65mm_EP4.8x4.8mm': Params(
        #
        # QFN, 28 Pin (https://www.semtech.com/uploads/documents/DS_SX1276-7-8-9_W_APP_V6.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is QFN-28-1EP_6x6mm_P0.65mm_EP4.8x4.8mm.kicad_mod
        # 
        c = 0.2,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.4,         # pin bottom flat part length (including corner arc)
        fp_s = True,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,          # First pin indicator radius
        fp_d = 0.1,          # First pin indicator distance from edge
        fp_z = 0.01,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,         # body length
        E = 6.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.9,          # body-board separation
        b = 0.3,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body 
        ps = 'rounded',          # rounded, square pads
        npx = 7,           # number of pins along X axis (width)
        npy = 7,           # number of pins along y axis (length)
        epad = (4.8, 4.8),       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'QFN-28-1EP_6x6mm_P0.65mm_EP4.8x4.8mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),
    'QFN-32-1EP_4x4mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/485CD.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = (2.7,2.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_4x4mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-32-1EP_5x5mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_32_05-08-1693.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = (3.45,3.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_5x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-32-1EP_5x5mm_P0.5mm_EP3.3x3.3mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/00002164B.pdf
        c = 0.2,            # pin thickness, body center part height
#        K=0.2,             # Fillet radius for pin edges
        L = 0.4,            # pin top flat part length (including fillet radius)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,         # first pin indicator radius
        fp_d = 0.1,         # first pin indicator distance from edge
        fp_z = 0.01,        # first pin indicator depth
        ef = 0.0, # 0.05,   # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,          #0.45 chamfer of the epad 1st pin corner
        D = 5.0,            # body overall length
        E = 5.0,            # body overall width
        A1 = 0.025,         # body-board separation  maui to check
        A2 = 0.85,          # body height
        b = 0.25,           # pin width
        e = 0.5,            # pin (center-to-center) distance
        m = 0.0,            # margin between pins and body
        ps = 'rounded',     # rounded pads
        npx = 8,            # number of pins along X axis (width)
        npy = 8,            # number of pins along y axis (length)
        epad = (3.30,3.30),     # e Pad #epad = None, # e Pad
        excluded_pins = None,   #no pin excluded
        modelName = 'QFN-32-1EP_5x5mm_P0.5mm_EP3.3x3.3mm', #modelName
        rotation = -90,     # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm': Params( #
        c = 0.2,            # pin thickness, body center part height
#        K=0.2,             # Fillet radius for pin edges
        L = 0.4,            # pin top flat part length (including fillet radius)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,         # first pin indicator radius
        fp_d = 0.1,         # first pin indicator distance from edge
        fp_z = 0.01,        # first pin indicator depth
        ef = 0.0, # 0.05,   # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,          #0.45 chamfer of the epad 1st pin corner
        D = 5.0,            # body overall length
        E = 5.0,            # body overall width
        A1 = 0.025,         # body-board separation  maui to check
        A2 = 0.75,          # body height
        b = 0.25,           # pin width
        e = 0.5,            # pin (center-to-center) distance
        m = 0.0,            # margin between pins and body
        ps = 'rounded',     # rounded pads
        npx = 8,            # number of pins along X axis (width)
        npy = 8,            # number of pins along y axis (length)
        epad = (3.60,3.60),     # e Pad #epad = None, # e Pad
        excluded_pins = None,   #no pin excluded
        modelName = 'QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm', #modelName
        rotation = -90,     # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-32-1EP_7x7mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/485ED.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.55,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 7.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = (4.7,4.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_7x7mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-36-1EP_5x6mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/%28UHE36%29%20QFN%2005-08-1876%20Rev%20%C3%98.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 10,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = (4.6,3.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-36-1EP_5x6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-36-1EP_6x6mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/485EC.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 9,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        epad = (4.4,4.4), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-36-1EP_6x6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-38-1EP_4x6mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_38_05-08-1750.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 12,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (4.65,2.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-38-1EP_4x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-38-1EP_5x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_38_05-08-1701.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 12,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (5.15,3.15), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-38-1EP_5x7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-40-1EP_5x5mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/05081746_B_UH40.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        epad = (3.5,3.5), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-40-1EP_5x5mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-40-1EP_6x6mm_Pitch0.5mm': Params( # 6x6, 0.5 pitch, 40 pins, 1.0mm height  QFN44 p005
        #datasheet example - http://www.ti.com/lit/ds/symlink/drv8308.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.23,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        epad = (4.1,4.1), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-40-1EP_6x6mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-42-1EP_5x6mm_Pitch0.4mm': Params( # 5x6, 0.4 pitch, 42 pins, 1.0mm height  QFN42 p004
        #datasheet example - http://www.ti.com/lit/ds/symlink/drv8308.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.23,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 12,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        epad = (4.7,3.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-42-1EP_5x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-44-1EP_7x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_44_05-08-1763.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 7.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (5.15,5.15), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-44-1EP_7x7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-44-1EP_8x8mm_Pitch0.65mm': Params( # 8x8, 0.65 pitch, 44 pins, 1.0mm height  QFN44 p065 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (6.45,6.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-44-1EP_8x8mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-48-1EP_5x5mm_P0.35mm_EP3.70x3.70mm': Params( # from https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf
        c = 0.2,            # pin thickness, body center part height
#        K=0.2,             # Fillet radius for pin edges
        L = 0.4,            # pin top flat part length (including fillet radius)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,         # first pin indicator radius
        fp_d = 0.2,         # first pin indicator distance from edge
        fp_z = 0.01,        # first pin indicator depth
        ef = 0.0, # 0.05,   # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,          #0.45 chamfer of the epad 1st pin corner
        D = 5.0,            # body overall length
        E = 5.0,            # body overall width
        A1 = 0.025,         # body-board separation  maui to check
        A2 = 0.60,          # body height
        b = 0.12,           # pin width
        e = 0.35,           # pin (center-to-center) distance
        m = 0.0,            # margin between pins and body
        ps = 'rounded',     # rounded pads
        npx = 12,           # number of pins along X axis (width)
        npy = 12,           # number of pins along y axis (length)
        epad = (3.70, 3.70),    # e Pad #epad = None, # e Pad
        excluded_pins = None,   #no pin excluded
        modelName = 'QFN-48-1EP_5x5mm_P0.35mm_EP3.70x3.70mm', #modelName
        rotation = -90,     # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-48-1EP_6x6mm_P0.4mm_EP4.30x4.30mm': Params( # from https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf
        c = 0.2,            # pin thickness, body center part height
#        K=0.2,             # Fillet radius for pin edges
        L = 0.4,            # pin top flat part length (including fillet radius)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,         # first pin indicator radius
        fp_d = 0.2,         # first pin indicator distance from edge
        fp_z = 0.01,        # first pin indicator depth
        ef = 0.0, # 0.05,   # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,          #0.45 chamfer of the epad 1st pin corner
        D = 6.0,            # body overall length
        E = 6.0,            # body overall width
        A1 = 0.025,         # body-board separation  maui to check
        A2 = 0.85,          # body height
        b = 0.20,           # pin width
        e = 0.4,            # pin (center-to-center) distance
        m = 0.0,            # margin between pins and body
        ps = 'rounded',     # rounded pads
        npx = 12,           # number of pins along X axis (width)
        npy = 12,           # number of pins along y axis (length)
        epad = (4.30, 4.30),    # e Pad #epad = None, # e Pad
        excluded_pins = None,   #no pin excluded
        modelName = 'QFN-48-1EP_6x6mm_P0.4mm_EP4.30x4.30mm', #modelName
        rotation = -90,     # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-48-1EP_7x7mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_48_05-08-1704.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 7.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = (5.15,5.15), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_7x7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-52-1EP_7x8mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/QFN_52_05-08-1729.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 7.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 14,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = (6.45,5.41), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-52-1EP_7x8mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-56-1EP_7x7mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/485BT-01.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 7.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 14,  # number of pins along X axis (width)
        npy = 14,  # number of pins along y axis (length)
        epad = (5.7,5.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-56-1EP_7x7mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-56-1EP_7x7mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/485BT-01.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 7.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 14,  # number of pins along X axis (width)
        npy = 14,  # number of pins along y axis (length)
        epad = (5.7,5.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-56-1EP_7x7mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-56-1EP_8x8mm_P0.5mm_EP4.5x5.2mm': Params( # from http://www.cypress.com/file/138911/download
        c = 0.2,        # pin thickness, body center part height
    #    K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      # chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.98,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 14,  # number of pins along X axis (width)
        npy = 14,  # number of pins along y axis (length)
        epad = (5.2,4.5), # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-56-1EP_8x8mm_P0.5mm_EP4.5x5.2mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-64-1EP_8x8mm_P0.4mm_EP6.5x6.5mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/64L_VQFN_8x8_with%206_5x6_5%20EP_JXX_C04-0437A.pdf
        c = 0.2,        # pin thickness, body center part height
    #    K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      # chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (6.5,6.5), # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_8x8mm_P0.4mm_EP6.5x6.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-64-1EP_9x9mm_Pitch0.5mm': Params( # 9x9, 0.5 pitch, 64 pins, 0.9mm height  QFN64 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
        D = 9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.73,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (7.15,7.15), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-68-1EP_8x8mm_P0.4mm_EP5.2x5.2mm': Params( # from https://www.mouser.com/ds/2/523/Microsemi_VSC8541-01_Datasheet_10496_V40-1148034.pdf
        c = 0.2,        # pin thickness, body center part height
    #    K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      # chamfer of the epad 1st pin corner
        D = 8.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 17,  # number of pins along X axis (width)
        npy = 17,  # number of pins along y axis (length)
        epad = (5.2,5.2), # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-68-1EP_8x8mm_P0.4mm_EP5.2x5.2mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'QFN-76-1EP_9x9mm_P0.4mm_EP3.8x3.8mm': Params( # from https://www.marvell.com/documents/bqcwxsoiqfjkcjdjhkvc/
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
        D = 9.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.85,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 19,  # number of pins along X axis (width)
        npy = 19,  # number of pins along y axis (length)
        epad = (3.8,3.8), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-76-1EP_9x9mm_P0.4mm_EP3.8x3.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-10_1.4x1.8mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/523AQ.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.1,      #0.45 chamfer of the epad 1st pin corner
        D = 1.8,       # body overall length
        E = 1.4,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.55,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 2,  # number of pins along X axis (width)
        npy = 3,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-10_1.4x1.8mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-16-1EP_3x3mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/523AJ.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (1.95,1.95), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-16-1EP_3x3mm_Pitch0.5mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-16-1EP_4x4mm_Pitch0.65mm': Params( # from footprint
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.6,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 4,  # number of pins along X axis (width)
        npy = 4,  # number of pins along y axis (length)
        epad = (2.7,2.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-16-1EP_4x4mm_Pitch0.65mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-20-1EP_3x3mm_Pitch0.4mm': Params( # from http://www.onsemi.com/pub/Collateral/523AL.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        epad = (1.8,1.8), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-20-1EP_3x3mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-20_3x3mm_P0.4mm': Params( # from https://resurgentsemi.com/wp-content/uploads/2018/09/MPR121_rev5-Resurgent.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.5,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.05,  # body-board separation  maui to check
        A2 = 0.6,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        #epad = (1.8,1.8), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-20_3x3mm_P0.4mm', #modelName 'UQFN-20_3x3mm_P0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/'
        ),
    'UQFN-20-1EP_4x4mm_Pitch0.5mm': Params( # from footprint
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.6,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        epad = (2.8,2.8), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-20-1EP_4x4mm_Pitch0.5mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-28-1EP_4x4mm_Pitch0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/%28PF28%29%20UTQFN%2005-08-1759%20Rev%20%C3%98.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.55,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (2.64,2.64), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-28-1EP_4x4mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-40-1EP_5x5mm_Pitch0.4mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/41364E.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 5.0,       # body overall length
        E = 5.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 10,  # number of pins along X axis (width)
        npy = 10,  # number of pins along y axis (length)
        epad = (3.7,3.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-40-1EP_5x5mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'UQFN-48-1EP_6x6mm_Pitch0.4mm': Params( # 9x9, 0.5 pitch, 64 pins, 0.9mm height  QFN64 p05 microchip
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.4,      #0.45 chamfer of the epad 1st pin corner
        D = 6.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = (4.5,4.5), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName 'UQFN-48-1EP_6x6mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'VDFN-8-1EP_2x2mm_Pitch0.5mm': Params( # from http://www.s-manuals.com/pdf/datasheet/r/t/rt9012_richtek.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.125,0.525), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'VDFN-8-1EP_2x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'DFN-14-1EP_3x3mm_Pitch0.4mm': Params( # from http://pdfserv.maximintegrated.com/package_dwgs/21-0137.PDF
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.3,1.7), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-14-1EP_3x3mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'SOT-886': Params( # from http://www.nxp.com/documents/outline_drawing/SOT886.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.025,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 1.45,       # body overall length
        E = 1.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.025,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'SOT-886', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../TO_SOT_Packages_SMD.3dshapes/'
        ),
    'SOT-383F': Params( # from http://www.comchiptech.com/cms/UserFiles/CPDVR085V0UA-HF-RevA.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.35,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.1,       # body overall length
        E = 1.6,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.3,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.5,0.45), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'SOT-383F', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../TO_SOT_Packages_SMD.3dshapes/'
        ),
    'SOT-1334-1': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1334-1.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.8,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 8,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None,#(0.2, 1.0),  # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'SOT-1334-1', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../TO_SOT_Packages_SMD.3dshapes/'
        ),
    'SOT-1333-1': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1333-1.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.8,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 2.5,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # square pads
        npx = 5,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (0.2, 1.0), #None, #(0.1,0.1), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'SOT-1333-1', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../TO_SOT_Packages_SMD.3dshapes/'
        ),
    'NXP_XSON-16': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1341-1.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.8,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      #0.45 chamfer of the epad 1st pin corner
        D = 3.2,       # body overall length
        E = 2.5,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'NXP_XSON-16', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm': Params( # from http://www.ti.com/lit/ds/symlink/tvs3300.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.25,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.8,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.6, 1.0), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_SON.3dshapes/'
        ),
    'WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm': Params( # from http://www.ti.com/lit/ds/symlink/tlv62080.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 2.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.8,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (1.6, 0.9), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_SON.3dshapes/'
        ),
    'WSON-8-1EP_3x3mm_P0.5mm_EP1.6x2.0mm': Params( # from http://www.chip.tomsk.ru/chip/chipdoc.nsf/Package/C67E729A4D6C883A4725793E004C8739!OpenDocument
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.8,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.0, 1.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON-8-1EP_3x3mm_P0.5mm_EP1.6x2.0mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_SON.3dshapes/'
        ),
    'WSON-12-1EP_1.35x2.5mm_P0.4mm_EP0.4x2mm': Params( # from http://www.ti.com/lit/ds/symlink/tpd6f003.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.25,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 2.5,       # body overall length
        E = 1.35,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.0, 0.4), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON-12-1EP_1.35x2.5mm_P0.4mm_EP0.4x2mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_SON.3dshapes/'
        ),
    'WSON-16_3.3x1.35_Pitch0.4mm': Params( # from http://www.chip.tomsk.ru/chip/chipdoc.nsf/Package/C67E729A4D6C883A4725793E004C8739!OpenDocument
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.25,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 3.3,       # body overall length
        E = 1.35,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.8, 0.4), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON-16_3.3x1.35_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'VSON-10-1EP_3x3mm_Pitch0.5mm_ThermalPad': Params( # from http://chip.tomsk.ru/chip/chipdoc.nsf/Package/D8A64DD165C2AAD9472579400024FC41!OpenDocument
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.43,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.24,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 2,  # number of pins along y axis (length)
        epad = (2.35, 1.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'VSON-10-1EP_3x3mm_Pitch0.5mm_ThermalPad', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'Texas_R-VFQFN-28-1EP_3.5x4.5mm_P0.4mm_EP2.1x3.1mm': Params( # from http://www.ti.com/lit/ds/symlink/tps51363.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 4.5,       # body overall length
        E = 3.5,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 9,  # number of pins along X axis (width)
        npy = 5,  # number of pins along y axis (length)
        epad = (3.1, 2.1), # e Pad #epad = None, # e Pad
        excluded_pins = None, #
        modelName = 'Texas_R-VFQFN-28-1EP_3.5x4.5mm_P0.4mm_EP2.1x3.1mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'Texas_S-PDSO-N12': Params( # from http://www.ti.com/lit/ml/mpds289a/mpds289a.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 2.5,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.24,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 6,  # number of pins along X axis (width)
        npy = 7,  # number of pins along y axis (length)
        epad = (2.0, 2.64), # e Pad #epad = None, # e Pad
        excluded_pins = (8,9,10,11,12,21,22,23,24,25), #
        modelName = 'Texas_S-PDSO-N12', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'Texas_S-PVSON-N10': Params( # from http://www.ti.com/lit/ds/symlink/lm5165.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.24,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 2,  # number of pins along y axis (length)
        epad = (2.5, 1.8), # e Pad #epad = None, # e Pad
        excluded_pins = None,
        modelName = 'Texas_S-PVSON-N10', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'Texas_S-PVSON-N8': Params( # from http://www.ti.com/lit/ds/symlink/opa2333.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.3,      #0.45 chamfer of the epad 1st pin corner
        D = 3.0,       # body overall length
        E = 3.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.4, 1.65), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Texas_S-PVSON-N8', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'Texas_R_PUQFN-N12': Params( # from http://www.ti.com/lit/ds/symlink/txb0104.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.05,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,     # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,        # body overall length
        E =  1.7,       # body overall width
        A1 = 0.02,      # body-board separation  maui to check
        A2 = 0.5,       # body height
        b = 0.20,       # pin width
        e = 0.4,        # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 5,        # number of pins along X axis (width)
        npy = 1,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #
        modelName = 'Texas_R_PUQFN-N12', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
    'Texas_S-PVQFN-N14': Params( # from http://www.ti.com/lit/ds/symlink/txb0104.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,     # 0.45 chamfer of the epad 1st pin corner
        D = 4.3,        # body overall length
        E =  4.3,       # body overall width
        A1 = 0.02,      # body-board separation  maui to check
        A2 = 0.9,       # body height
        b = 0.28,       # pin width
        e = 0.25,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'rounded', # rounded pads
        npx = 9,        # number of pins along X axis (width)
        npy = 9,        # number of pins along y axis (length)
        epad = (2.05, 2.05), # e Pad #epad = None, # e Pad
        excluded_pins = ( 2,4,6,8, 10,12,13,14,15,16,18, 20,22,24,26, 28,30,31,32,33,34,36), #
#        excluded_pins = ( 1,3,4,5,6,7,9, 11,13,15,17, 19,21,22,23,24,25,27, 29,31,33,35,37), #
        modelName = 'Texas_S-PVQFN-N14', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_DFN_QFN.3dshapes/'
        ),
        'USON-10_2.5x1.0mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/tpd4e02b04.pdf
        c = 0.13,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.36,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 2.5,       # body overall length
        E = 1.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 5,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'USON-10_2.5x1.0mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'Texas_DQK': Params( # from http://www.ti.com/lit/ds/symlink/csd16301q2.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.05,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,     # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,        # body overall length
        E =  2.0,       # body overall width
        A1 = 0.02,      # body-board separation  maui to check
        A2 = 0.8,       # body height
        b = 0.30,       # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded pads
        npx = 3,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #
        modelName = 'Texas_DQK', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_SON.3dshapes/'
        ),
    'USON-20_2x4mm_Pitch0.4mm': Params( # from http://www.ti.com/lit/ds/symlink/txb0108.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.55,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 2.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.5,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 10,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'USON-20_2x4mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'VSON-8_3.3x3.3mm_Pitch0.65mm_NexFET': Params( # from http://www.ti.com/lit/ds/symlink/csd87334q3d.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.45,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 3.3,       # body overall length
        E = 3.3,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.95,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (2.7, 1.8), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'VSON-8_3.3x3.3mm_Pitch0.65mm_NexFET', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'VSON-10-1EP_3x3mm_P0.5mm_EP1.2x2mm': Params( # 3x3mm, 10-pin VSON package, 1.0mm height
        # reference: http://rohmfs.rohm.com/en/techdata_basic/ic/package/vson010v3030_1-e.pdf
        c = 0.2,        # pin thickness, body center part height
        # K = 0.2,        # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,    # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,    # first pin indicator depth
        ef = 0.0,       # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,     # chamfer of the epad 1st pin corner
        D = 3.0,        # body overall length
        E = 3.0,        # body overall width
        A1 = 0.02,      # body-board separation  maui to check
        A2 = 1.0,       # body height
        b = 0.25,       # pin width
        e = 0.5,        # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'rounded', # pad shape
        npx = 5,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = (2.0,1.2), # e Pad
        excluded_pins = None, # no pin excluded
        modelName = 'VSON-10-1EP_3x3mm_P0.5mm_EP1.2x2mm', # modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
    ),
    'WSON6_1.5x1.5mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/tps717.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.5,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 1.5,       # body overall length
        E = 1.5,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.75,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 3,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON6_1.5x1.5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'WSON8_4x4mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ds/symlink/lm5107.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.8,  # body height
        b = 0.3,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.0, 2.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON8_4x4mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'X2SON-8_1.4x1mm_Pitch0.35mm': Params( # from http://www.ti.com/lit/ds/symlink/pca9306.pdf
        c = 0.13,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.3,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.01,      #0.45 chamfer of the epad 1st pin corner
        D = 1.4,       # body overall length
        E = 1.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.37,  # body height
        b = 0.18,  # pin width
        e = 0.35,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 4,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = None, # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'X2SON-8_1.4x1mm_Pitch0.35mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'WSON-14_1EP_4.0x4.0mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/lp3947.pdf
        c = 0.1,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.25,      #0.45 chamfer of the epad 1st pin corner
        D = 4.0,       # body overall length
        E = 4.0,       # body overall width
        A1 = 0.02,  # body-board separation  maui to check
        A2 = 0.8,  # body height
        b = 0.25,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'square',   # rounded pads
        npx = 7,  # number of pins along X axis (width)
        npy = 0,  # number of pins along y axis (length)
        epad = (3.0, 2.6), # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WSON-14_1EP_4.0x4.0mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Housings_SON.3dshapes/'
        ),
    'AMS_QFN-4-1EP_2x2mm_P0.95mm': Params(
        #
        # UFD Package, 4-Lead Plastic QFN (2mm x 2mm), http://ams.com/eng/content/download/950231/2267959/483138
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.28,      # pin width
        e = 0.95,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 2,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.6, 0.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'AMS_QFN-4-1EP_2x2mm_P0.95mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-56-1EP_8x8mm_P0.5mm_EP6.22x6.22mm_ThermalVias': Params(
        #
        # 56-Lead Plastic Quad Flat, No Lead Package (ML) - 8x8x0.9 mm Body [QFN] (see datasheet at http://www.cypress.com/file/138911/download and app note at http://www.cypress.com/file/140006/download)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 14,      # number of pins along X axis (width)
        npy = 14,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-56-1EP_8x8mm_P0.5mm_EP6.22x6.22mm_ThermalVias',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-10-1EP_3x3mm_P0.5mm_EP1.75x2.7mm': Params(
        #
        # 10-Lead Plastic Dual Flat No-Lead Package, 3x3mm Body (see Atmel Appnote 8826)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.7, 1.75),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-10-1EP_3x3mm_P0.5mm_EP1.75x2.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-10-1EP_4x4mm_P0.65mm_EP2.65x3.05mm': Params(
        #
        # 10-Lead Plastic Dual Flat No-Lead Package, 4x4mm body, 0.65mm pitch with 2.65 x 3.05mm
        # heat sink pad.
        # See https://www.ichaus.de/upload/pdf/Package%20dimensions%20DFN_QFN_b2es.pdf
        #
        c = 0.2,        # pin thickness, body center part height
        #K=0.175,        # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,        # body overall length
        E = 4.0,        # body overall width
        A1 = 0.1,       # body-board separation
        A2 = 0.9,       # body overall height
        b = 0.3,        # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,        # number of pins along X axis (width)
        npy = 0,        # number of pins along y axis (length)
        epad = (3.05, 2.65),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-10-1EP_4x4mm_P0.65mm_EP2.65x3.05mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-10_2x2mm_P0.4mm': Params(
        #
        # 10-Lead Plastic DFN (2mm x 2mm)  0.40mm pitch
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.17,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-10_2x2mm_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm': Params(
        #
        # 10-Lead Plastic Dual Flat, No Lead Package (MF) - 3x3x0.9 mm Body [DFN] (see Microchip Packaging Specification 00000049BS.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.86, 2.05),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-14-1EP_3x4.5mm_P0.65mm': Params(
        #
        # 14-lead very thin plastic quad flat, 3.0x4.5mm size, 0.65mm pitch (http://ww1.microchip.com/downloads/en/DeviceDoc/14L_VDFN_4_5x3_0mm_JHA_C041198A.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.5,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.24,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 7,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (4.25, 1.65),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-14-1EP_3x4.5mm_P0.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm_PullBack': Params(
        #
        # DFN, 6 Pin (http://www.onsemi.com/pub/Collateral/NCP133-D.PDF), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 1.2,      # body overall length
        E = 1.2,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.13333333333333333,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (0.94, 0.3),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_1.2x1.2mm_P0.4mm_EP0.3x0.94mm_PullBack',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-6-1EP_2x1.8mm_P0.5mm_EP1.2x1.6mm': Params(
        #
        # DFN, 6 Pin (https://www.diodes.com/assets/Package-Files/U-DFN2018-6.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 1.8,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.14,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.6, 1.2),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_2x1.8mm_P0.5mm_EP1.2x1.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-6-1EP_3x3mm_P1mm_EP1.5x2.4mm': Params(
        #
        # DFN, 6 Pin (https://www.silabs.com/documents/public/data-sheets/Si7020-A20.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.28,      # pin width
        e = 1.0,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.4, 1.5),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6-1EP_3x3mm_P1mm_EP1.5x2.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-6_1.3x1.2mm_P0.4mm': Params(
        #
        # 6-Lead Plastic DFN (1.3mm x 1.2mm)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 1.2,      # body overall length
        E = 1.3,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.2,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-6_1.3x1.2mm_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.5mm': Params(
        #
        # DFN, 8 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8127-AVR-8-bit-Microcontroller-ATtiny4-ATtiny5-ATtiny9-ATtiny10_Datasheet.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.5, 0.9),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_2x2mm_P0.5mm_EP0.9x1.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-8-1EP_3x2mm_P0.5mm_EP1.36x1.46mm': Params(
        #
        # 8-Lead Plastic Dual Flat, No Lead Package (8MA2) - 2x3x0.6 mm Body (http://ww1.microchip.com/downloads/en/DeviceDoc/20005010F.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.46, 1.36),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_3x2mm_P0.5mm_EP1.36x1.46mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm': Params(
        #
        # 8-Lead Plastic Dual Flat, No Lead Package (8MA2) - 2x3x0.6 mm Body [UDFN] (see Atmel-8815-SEEPROM-AT24CS01-02-Datasheet.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.5, 1.3),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-8-1EP_3x3mm_P0.65mm_EP1.7x2.05mm': Params(
        #
        # DFN, 8 Pin (http://www.ixysic.com/home/pdfs.nsf/www/IX4426-27-28.pdf/$file/IX4426-27-28.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.05, 1.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_3x3mm_P0.65mm_EP1.7x2.05mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-8-1EP_4x4mm_P0.8mm_EP2.39x2.21mm': Params(
        #
        # 8-Lead Plastic Dual Flat, No Lead Package (MD) - 4x4x0.9 mm Body [DFN] (http://www.onsemi.com/pub/Collateral/NCP4308-D.PDF)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.24,      # pin width
        e = 0.8,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.21, 2.39),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_4x4mm_P0.8mm_EP2.39x2.21mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-8-1EP_6x5mm_P1.27mm_EP2x2mm': Params(
        #
        # DD Package; 8-Lead Plastic DFN (6mm x 5mm) (see http://www.everspin.com/file/236/download)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 6.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.4,      # pin width
        e = 1.27,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_6x5mm_P1.27mm_EP2x2mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-8-1EP_6x5mm_Pitch1.27mm': Params(
        #
        # DD Package; 8-Lead Plastic DFN (6mm x 5mm) (see http://www.everspin.com/file/236/download)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 6.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.45,      # pin width
        e = 1.27,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-8-1EP_6x5mm_Pitch1.27mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Diodes_DFN1006-3': Params(
        #
        # DFN package size 1006 3 pins
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 0.6,      # body overall length
        E = 1.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.05,      # pin width
        e = 0.225,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = (2,4,6), #no pin excluded
        modelName = 'Diodes_DFN1006-3',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Infineon_MLPQ-40-32-1EP_7x7mm_P0.5mm': Params(
        #
        # MLPQ 32 leads, 7x7mm, 0.127mm stencil (https://www.infineon.com/dgdl/Infineon-AN1170-AN-v05_00-EN.pdf?fileId=5546d462533600a40153559ac3e51134)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.15,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 10,      # number of pins along X axis (width)
        npy = 10,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = (13, 14, 15, 35,36, 37), #no pin excluded
        modelName = 'Infineon_MLPQ-40-32-1EP_7x7mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.15x5.15mm': Params(
        #
        # MLPQ 48 leads, 7x7mm (https://www.infineon.com/dgdl/irs2052mpbf.pdf?fileId=5546d462533600a401535675d3b32788)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.15,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.15x5.15mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'DFN-14-1EP_3x4mm_Pitch0.5mm': Params(
        #
        # DE Package; 14-Lead Plastic DFN (4mm x 3mm) with special pads (see http://cds.linear.com/docs/en/datasheet/3032ff.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 7,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'DFN-14-1EP_3x4mm_Pitch0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Linear_UGK52_QFN-46-52': Params(
        #
        # Linear UKG52(46) package, QFN-52-1EP variant (see http://cds.linear.com/docs/en/datasheet/3886fe.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 8.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 14,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = (3, 37, 41, 45, 49, 51), #no pin excluded
        modelName = 'Linear_UGK52_QFN-46-52',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.8x1.3mm_ThermalVias': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.15,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.8x1.3mm_ThermalVias',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-16-1EP_4x4mm_Pitch0.65mm': Params(
        #
        # 16-Lead Quad Flat, No Lead Package (8E) - 4x4x0.9 mm Body [UQFN]; (see Microchip Packaging Specification 00000049BS.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.25,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-16-1EP_4x4mm_Pitch0.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm': Params(
        #
        # QFN, 44 Pin, dual row (http://ww1.microchip.com/downloads/en/DeviceDoc/44L_VQFN_5x5mm_Dual_Row_%5BS3B%5D_C04-21399a.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.25,      # pin width
        e = 0.7,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm': Params(
        #
        # QFN, 64 Pin, dual row (http://ww1.microchip.com/downloads/en/DeviceDoc/64L_VQFN_7x7_Dual_Row_%5BSVB%5D_C04-21420a.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.25,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm': Params(
        #
        # 40-Lead (32-Lead Populated) Plastic Quad Flat, No Lead Package - 6x8x0.9mm Body (https://www.microsemi.com/document-portal/doc_download/131677-pd70224-datasheet)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 8.0,      # body overall length
        E = 6.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = (4, 9, 15, 18, 24, 29, 35, 38), #no pin excluded
        modelName = 'Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Mini-Circuits_DL805': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.25,      # body overall length
        E = 3.25,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.3,      # pin width
        e = 0.66,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 1,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Mini-Circuits_DL805',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm': Params(
        #
        # MLF, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/doc8246.pdf (page 263)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 5,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm': Params(
        #
        # 8-Pin ePad 3mm x 3mm MLF - 3x3x0.85 mm Body (see Microchip datasheet http://ww1.microchip.com/downloads/en/DeviceDoc/mic5355_6.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.2,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.3, 1.55),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'MLPQ-16-1EP_4x4mm_P0.65mm_EP2.8x2.8mm': Params(
        #
        # Micro Leadframe Package, 16 pin with exposed pad
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.24,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (2.8, 2.8),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'MLPQ-16-1EP_4x4mm_P0.65mm_EP2.8x2.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Nordic_AQFN-73-1EP_7x7mm_P0.5mm': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = (3, 11, 12, 33, 35, 46, 47, 48), #no pin excluded
        modelName = 'Nordic_AQFN-73-1EP_7x7mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'OnSemi_DFN-8_2x2mm_P0.5mm': Params(
        #
        # DFN8 2x2, 0.5P (https://www.onsemi.com/pub/Collateral/511AT.PDF)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'OnSemi_DFN-8_2x2mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),
    'OnSemi_SIP-38-6EP-9x7mm_P0.65mm_EP0.95x0.95mm': Params( # 2x3, 0.5mm pitch, 10 pins, 0.75mm height  DFN
        #From- https://www.onsemi.com/pub/Collateral/AX-SIP-SFEU-D.PDF#page=19
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.60,        # pin top flat part length (including fillet radius)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.35,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0,      #0.45 chamfer of the epad 1st pin corner
        D = 7.0,       # body overall length
        E = 9.0,       # body overall width
        A1 = 0.05,  # body-board separation  maui to check
        A2 = 0.996,  # body height
        b = 0.25,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        m = 0.0,  # margin between pins and body
        ps = 'rounded',   # rounded pads
        npx = 8,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (0.95,0.95), # e Pad #epad = None, # e Pad
        epad_n = (2, 3), # Matrix of epads
        epad_pitch = (2, 2), 
        excluded_pins = None, #no pin excluded
        modelName = 'OnSemi_SIP-38-6EP-9x7mm_P0.65mm_EP0.95x0.95mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'OnSemi_VCT-28_3.5x3.5mm_P0.4mm': Params(
        #
        # OnSemi  VCT, 28 Pin (http://www.onsemi.com/pub/Collateral/601AE.PDF), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.5,      # body overall length
        E = 3.5,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.18,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 7,      # number of pins along X axis (width)
        npy = 7,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'OnSemi_VCT-28_3.5x3.5mm_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm': Params(
        #
        # Panasonic HQFN-16, 4x4x0.85mm (https://industrial.panasonic.com/content/data/SC/ds/ds7/c0/PKG_HQFN016-A-0404XZL_EN.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Panasonic_HSON-8_8x8mm_P2.00mm': Params(
        #
        # Panasonic HSON-8, 8x8x1.25mm (https://industrial.panasonic.com/content/data/SC/ds/ds7/c0/PKG_HSON008-A-0808XXI_EN.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 1.0,      # pin width
        e = 2.0,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Panasonic_HSON-8_8x8mm_P2.00mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Vishay_PowerPAK_1212-8_Single': Params(
        #
        # Vishay_PowerPAK_1212-8_Single (https://www.vishay.com/docs/62847/siss27dn.pdf)
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.43,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.3,      # body overall length
        E = 3.3,      # body overall width
        A1 = 0.05,      # body-board separation
        A2 = 0.75,       # body overall height
        b = 0.3,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.25, 1.7),    # e Pad #epad = None, # e Pad
        epad_offsetY = 0.39,
        excluded_pins = None, #no pin excluded
        modelName = 'Vishay_PowerPAK_1212-8_Single',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_SO.3dshapes/',
        ),

    'QFN-16-1EP_3x3mm_P0.5mm_EP2.7x2.7mm_ThermalVias': Params(
        #
        # 16-Lead Plastic Quad Flat, No Lead Package (NG) - 3x3x0.9 mm Body [QFN]; (see Microchip Packaging Specification 00000049BS.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (2.7, 2.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-16-1EP_3x3mm_P0.5mm_EP2.7x2.7mm_ThermalVias',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm': Params(
        #
        # QFN, 16 Pin (http://www.thatcorp.com/datashts/THAT_1580_Datasheet.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.21,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (2.1, 2.1),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm': Params(
        #
        # QFN, 16 Pin (https://www.allegromicro.com/~/media/Files/Datasheets/A4403-Datasheet.ashx), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.21,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (2.7, 2.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-20-1EP_3x3mm_P0.45mm_EP1.6x1.6mm': Params(
        #
        # QFN, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/atmel-8235-8-bit-avr-microcontroller-attiny20_datasheet.pdf (Page 212)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.1,      # pin width
        e = 0.45,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 5,      # number of pins along y axis (length)
        epad = (1.6, 1.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-20-1EP_3x3mm_P0.45mm_EP1.6x1.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-20-1EP_4x4mm_P0.5mm_EP2.25x2.25mm': Params(
        #
        # 20-Lead Plastic Quad Flat No-Lead Package, 4x4mm Body (see Atmel Appnote 8826)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 5,      # number of pins along y axis (length)
        epad = (2.25, 2.25),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-20-1EP_4x4mm_P0.5mm_EP2.25x2.25mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.6mm': Params(
        #
        # QFN, 24 Pin (https://store.invensense.com/datasheets/invensense/MPU-6050_DataSheet_V3%204.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (2.6, 2.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm': Params(
        #
        # QFN, 24 Pin (http://www.alfarzpp.lv/eng/sc/AS3330.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (2.7, 2.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-24-1EP_5x5mm_P0.65mm_EP3.4x3.4mm': Params(
        #
        # QFN, 24 Pin (http://www.thatcorp.com/datashts/THAT_5173_Datasheet.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (3.4, 3.4),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-24-1EP_5x5mm_P0.65mm_EP3.4x3.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm': Params(
        #
        # QFN, 28 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/8008S.pdf (Page 16)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.13,      # pin width
        e = 0.45,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 7,      # number of pins along X axis (width)
        npy = 7,      # number of pins along y axis (length)
        epad = (2.4, 2.4),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_4x4mm_P0.45mm_EP2.4x2.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-28-1EP_4x5mm_P0.5mm_EP2.65x3.65mm': Params(
        #
        # QFN, 28 Pin (http://www.analog.com/media/en/technical-documentation/data-sheets/3555fe.pdf (Page 32)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (3.65, 2.65),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28-1EP_4x5mm_P0.5mm_EP2.65x3.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-28_4x4mm_P0.5mm': Params(
        #
        # QFN, 28 Pin (http://www.st.com/resource/en/datasheet/stm32f031k6.pdf (Page 280)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 7,      # number of pins along X axis (width)
        npy = 7,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-28_4x4mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-32-1EP_4x4mm_P0.4mm_EP2.9x2.9mm': Params(
        #
        # QFN, 32 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/atmel-8153-8-and-16-bit-avr-microcontroller-xmega-e-atxmega8e5-atxmega16e5-atxmega32e5_datasheet.pdf (Page 70)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.14,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (2.9, 2.9),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_4x4mm_P0.4mm_EP2.9x2.9mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm': Params(
        #
        # QFN, 32 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/8008S.pdf (Page 20)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (3.1, 3.1),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-32-1EP_5x5mm_P0.5mm_EP3.65x3.65mm': Params(
        #
        # QFN, 32 Pin (https://www.exar.com/ds/mxl7704.pdf (Page 35)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (3.65, 3.65),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_5x5mm_P0.5mm_EP3.65x3.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm': Params(
        #
        # QFN, 32 Pin (http://infocenter.nordicsemi.com/pdf/nRF52810_PS_v1.1.pdf (Page 468)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (3.6, 3.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-32-1EP_7x7mm_P0.65mm_EP4.65x4.65mm': Params(
        #
        # QFN, 32 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8209-8-bit%20AVR%20ATmega16M1-32M1-64M1_Datasheet.pdf (Page 426)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.24,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (4.65, 4.65),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_7x7mm_P0.65mm_EP4.65x4.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-32-1EP_7x7mm_P0.65mm_EP4.7x4.7mm': Params(
        #
        # QFN, 32 Pin (https://www.nxp.com/docs/en/data-sheet/LPC111X.pdf (Page 108)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.21,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (4.7, 4.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_7x7mm_P0.65mm_EP4.7x4.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-32-1EP_7x7mm_P0.65mm_EP5.4x5.4mm': Params(
        #
        # QFN, 32 Pin (http://www.thatcorp.com/datashts/THAT_5171_Datasheet.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (5.4, 5.4),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-32-1EP_7x7mm_P0.65mm_EP5.4x5.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.1mm': Params(
        #
        # QFN, 36 Pin (https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2100_datasheet_Rev1.08.pdf (page 43)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 10,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (4.1, 3.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-36-1EP_6x6mm_P0.5mm_EP4.1x4.1mm': Params(
        #
        # QFN, 36 Pin (www.st.com/resource/en/datasheet/stm32f101t6.pdf (page 72)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,      # body overall length
        E = 6.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 9,      # number of pins along X axis (width)
        npy = 9,      # number of pins along y axis (length)
        epad = (4.1, 4.1),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-36-1EP_6x6mm_P0.5mm_EP4.1x4.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm': Params(
        #
        # QFN, 44 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/2512S.pdf (page 17)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 11,      # number of pins along X axis (width)
        npy = 11,      # number of pins along y axis (length)
        epad = (5.2, 5.2),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm': Params(
        #
        # QFN, 44 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf (page 153)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.24,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 11,      # number of pins along X axis (width)
        npy = 11,      # number of pins along y axis (length)
        epad = (6.45, 6.45),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-44-1EP_8x8mm_P0.65mm_EP6.45x6.45mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm': Params(
        #
        # 44-Lead Plastic Quad Flat, No Lead Package - 9x9 mm Body [QFN]; see section 10.3 of https://www.parallax.com/sites/default/files/downloads/P8X32A-Propeller-Datasheet-v1.4.0_0.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.23,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 11,      # number of pins along X axis (width)
        npy = 11,      # number of pins along y axis (length)
        epad = (7.5, 7.5),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-44-1EP_9x9mm_Pitch0.65mm_EP7.5x7.5mm': Params(
        #
        # 44-Lead Plastic Quad Flat, No Lead Package - 9x9 mm Body [QFN] with thermal vias; see section 10.3 of https://www.parallax.com/sites/default/files/downloads/P8X32A-Propeller-Datasheet-v1.4.0_0.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.23,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 11,      # number of pins along X axis (width)
        npy = 11,      # number of pins along y axis (length)
        epad = (7.5, 7.5),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-44-1EP_9x9mm_Pitch0.65mm_EP7.5x7.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-48-1EP_5x5mm_P0.35mm_EP3.7x3.7mm': Params(
        #
        # QFN, 48 Pin (https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf (page 38)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.14,      # pin width
        e = 0.35,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 14,      # number of pins along X axis (width)
        npy = 10,      # number of pins along y axis (length)
        epad = (3.7, 3.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_5x5mm_P0.35mm_EP3.7x3.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-48-1EP_6x6mm_P0.4mm_EP4.3x4.3mm': Params(
        #
        # QFN, 48 Pin (https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf (page 38)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,      # body overall length
        E = 6.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.14,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = (4.3, 4.3),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_6x6mm_P0.4mm_EP4.3x4.3mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm': Params(
        #
        # 48-Lead Plastic QFN, 6x6mm, 0.4mm pitch (see https://www.onsemi.com/pub/Collateral/485BA.PDF)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,      # body overall length
        E = 6.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = (4.66, 4.66),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-48-1EP_6x6mm_Pitch0.4mm_EP4.66x4.66mm': Params(
        #
        # 48-Lead Plastic Quad Flat, No Lead Package - 6x6 mm Body [QFN] with thermal vias; see figure 7.2 of https://static.dev.sifive.com/SiFive-FE310-G000-datasheet-v1.0.4.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,      # body overall length
        E = 6.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.14,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = (4.66, 4.66),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_6x6mm_Pitch0.4mm_EP4.66x4.66mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-48-1EP_7x7mm_P0.5mm_EP5.3x5.3mm': Params(
        #
        # QFN, 48 Pin (https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2041_datasheet.pdf (Page 62)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = (5.3, 5.3),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_7x7mm_P0.5mm_EP5.3x5.3mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-48-1EP_7x7mm_P0.5mm_EP5.45x5.45mm': Params(
        #
        # QFN, 48 Pin (http://www.thatcorp.com/datashts/THAT_626x_Datasheet.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = (5.45, 5.45),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_7x7mm_P0.5mm_EP5.45x5.45mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm': Params(
        #
        # QFN, 48 Pin (http://www.st.com/resource/en/datasheet/stm32f042k6.pdf (Page 94)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = (5.6, 5.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-56-1EP_7x7mm_P0.4mm_EP5.7x5.7mm': Params(
        #
        # 56-Lead Plastic Ultra Thin Quad Flat, No Lead Package (MV) - 7x7x0.4 mm Body [UQFN]; (see Cypress Package Package Output Drawing 001-58740)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.14,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 14,      # number of pins along X axis (width)
        npy = 14,      # number of pins along y axis (length)
        epad = (5.7, 5.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-56-1EP_7x7mm_P0.4mm_EP5.7x5.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-56-1EP_8x8mm_P0.5mm_EP4.6x5.3mm': Params(
        #
        # 56-Lead Plastic Quad Flat, No Lead Package (ML) - 8x8x0.9 mm Body [QFN]; (see http://www.cypress.com/file/138911/download)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 14,      # number of pins along X axis (width)
        npy = 14,      # number of pins along y axis (length)
        epad = (5.3, 4.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-56-1EP_8x8mm_P0.5mm_EP4.6x5.3mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-56-1EP_8x8mm_P0.5mm_EP5.6x5.6mm': Params(
        #
        # QFN, 56 Pin (http://www.ti.com/lit/ds/symlink/tlc5957.pdf#page=23 (page 23f)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 14,      # number of pins along X axis (width)
        npy = 14,      # number of pins along y axis (length)
        epad = (5.6, 5.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-56-1EP_8x8mm_P0.5mm_EP5.6x5.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-64-1EP_9x9mm_P0.5mm_EP4.7x4.7mm': Params(
        #
        # QFN, 64 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/60001477A.pdf (page 1083)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.14,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 16,      # number of pins along X axis (width)
        npy = 16,      # number of pins along y axis (length)
        epad = (4.7, 4.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_P0.5mm_EP4.7x4.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-64-1EP_9x9mm_P0.5mm_EP5.4x5.4mm': Params(
        #
        # QFN, 64 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/70593d.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 16,      # number of pins along X axis (width)
        npy = 16,      # number of pins along y axis (length)
        epad = (5.4, 5.4),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_P0.5mm_EP5.4x5.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-64-1EP_9x9mm_P0.5mm_EP6x6mm': Params(
        #
        # QFN, 64 Pin (http://www.ti.com/lit/ds/symlink/tusb8041.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 16,      # number of pins along X axis (width)
        npy = 16,      # number of pins along y axis (length)
        epad = (6.0, 6.0),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_P0.5mm_EP6x6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-64-1EP_9x9mm_P0.5mm_EP7.25x7.25mm': Params(
        #
        # 64-Lead Plastic Quad Flat No-Lead Package, 9x9mm Body (see Atmel Appnote 8826)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 16,      # number of pins along X axis (width)
        npy = 16,      # number of pins along y axis (length)
        epad = (7.25, 7.25),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_P0.5mm_EP7.25x7.25mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-64-1EP_9x9mm_P0.5mm_EP7.3x7.3mm': Params(
        #
        # QFN, 64 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/00002304A.pdf (page 43)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 16,      # number of pins along X axis (width)
        npy = 16,      # number of pins along y axis (length)
        epad = (7.3, 7.3),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_P0.5mm_EP7.3x7.3mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-64-1EP_9x9mm_P0.5mm_EP7.5x7.5mm': Params(
        #
        # QFN, 64 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/doc7593.pdf (page 432)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.13,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 16,      # number of pins along X axis (width)
        npy = 16,      # number of pins along y axis (length)
        epad = (7.5, 7.5),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_P0.5mm_EP7.5x7.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'QFN-64-1EP_9x9mm_P0.5mm_EP7.65x7.65mm': Params(
        #
        # QFN, 64 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2549-8-bit-AVR-Microcontroller-ATmega640-1280-1281-2560-2561_datasheet.pdf (page 415)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,      # body overall length
        E = 9.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 16,      # number of pins along X axis (width)
        npy = 16,      # number of pins along y axis (length)
        epad = (7.65, 7.65),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'QFN-64-1EP_9x9mm_P0.5mm_EP7.65x7.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'Qorvo_DFN-8-1EP_2x2mm_P0.5mm': Params(
        #
        # DFN 8 2x2mm, 0.5mm http://www.qorvo.com/products/d/da000896
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Qorvo_DFN-8-1EP_2x2mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'ROHM_DFN0604-3': Params(
        #
        # DFN package size 0604 3 pins
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 0.4,      # body overall length
        E = 0.6,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.05,      # pin width
        e = 0.15,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = (2,4,6), #no pin excluded
        modelName = 'ROHM_DFN0604-3',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm': Params(
        #
        # 20-Lead Plastic Quad Flat, No Lead Package - 3x3 mm Body [QFN] with corner pads; see figure 8.2 of https://www.silabs.com/documents/public/data-sheets/efm8bb1-datasheet.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'ST_UFQFPN-20_3x3mm_P0.5mm': Params(
        #
        # UFQFPN 20-lead, 3 x 3 mm, 0.5 mm pitch, ultra thin fine pitch quad flat package (http://www.st.com/resource/en/datasheet/stm8s003f3.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 5,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'ST_UFQFPN-20_3x3mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'ST_UQFN-6L_1.5x1.7mm_Pitch0.5mm': Params(
        #
        # ST UQFN 6 pin 0.5mm Pitch http://www.st.com/resource/en/datasheet/ecmf02-2amx6.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 1.7,      # body overall length
        E = 1.5,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'ST_UQFN-6L_1.5x1.7mm_Pitch0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'TDFN-12_2x3mm_P0.5mm': Params(
        #
        # TDFN, 12 Pads, No exposed, http://www.st.com/resource/en/datasheet/stm6600.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'TDFN-12_2x3mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm': Params(
        #
        # 8-lead plastic dual flat, 2x3x0.75mm size, 0.5mm pitch (http://ww1.microchip.com/downloads/en/DeviceDoc/8L_TDFN_2x3_MN_C04-0129E-MN.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.65, 1.8),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm': Params(
        #
        # TQFN, 16 Pin (https://www.ti.com/lit/ds/symlink/tpa6132a2.pdf)
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.40,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A2 = 0.75,       # body overall height
        b = 0.24,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (1.6, 1.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'TQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'TQFN-20-1EP_5x5mm_P0.65mm_EP3.1x3.1mm': Params(
        #
        # TQFN, 16 Pin (https://www.ti.com/lit/ds/symlink/tpa6132a2.pdf)
        # Maxim T2055-3 (https://pdfserv.maximintegrated.com/package_dwgs/21-0140.PDF)
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.55,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.35,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.02,      # body-board separation
        A2 = 0.75,       # body overall height
        b = 0.30,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'rounded',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 5,      # number of pins along y axis (length)
        epad = (3.1, 3.1),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'TQFN-20-1EP_5x5mm_P0.65mm_EP3.1x3.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'TQFN-24-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_PullBack': Params(
        #
        # TQFN, 24 Pin (https://ams.com/documents/20143/36005/AS1115_DS000206_1-00.pdf/3d3e6d35-b184-1329-adf9-2d769eb2404f), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.16666666666666666,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (2.8, 2.8),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'TQFN-24-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_PullBack',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'UQFN-10_1.3x1.8mm_P0.4mm': Params(
        #
        # UQFN, 10 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/00001725D.pdf (Page 9)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 1.8,      # body overall length
        E = 1.3,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.14,      # pin width
        e = 0.4,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 2,      # number of pins along X axis (width)
        npy = 3,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-10_1.3x1.8mm_P0.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'UQFN-10_1.6x2.1mm_P0.5mm': Params(
        #
        # UQFN, 10 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/00001725D.pdf (Page 12)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.1,      # body overall length
        E = 1.6,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.3,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 2,      # number of pins along X axis (width)
        npy = 3,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'UQFN-10_1.6x2.1mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'VQFN-20-1EP_3x3mm_P0.45mm_EP1.55x1.55mm': Params(
        #
        # VQFN, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/doc8246.pdf (page 264)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.13,      # pin width
        e = 0.45,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 5,      # number of pins along X axis (width)
        npy = 5,      # number of pins along y axis (length)
        epad = (1.55, 1.55),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'VQFN-20-1EP_3x3mm_P0.45mm_EP1.55x1.55mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm': Params(
        #
        # VQFN, 24 Pin (http://www.ti.com/lit/ds/symlink/msp430f1101a.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (2.45, 2.45),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm': Params(
        #
        # VQFN, 28 Pin (http://www.ti.com/lit/ds/symlink/lm5175.pdf (Page 37)), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (3.55, 2.55),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'VQFN-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm': Params(
        #
        # VQFN, 48 Pin (https://www.ti.com/lit/ds/symlink/cc430f5137.pdf (Page 128)),
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.4,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,      # body overall length
        E = 7.0,      # body overall width
        A1 = 0.05,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.24,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 12,      # number of pins along X axis (width)
        npy = 12,      # number of pins along y axis (length)
        epad = (4.1, 4.1),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'VQFN-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm': Params(
        #
        # WDFN, 12 Pin (https://www.diodes.com/assets/Datasheets/PAM2306.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.14,      # pin width
        e = 0.45,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (2.5, 1.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WDFN-8_2.2x2mm_P0.5mm_1EP': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WDFN-8_2.2x2mm_P0.5mm_1EP',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm': Params(
        #
        # WDFN, 8 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/8L_TDFN_2x3_MNY_C04-0129E-MNY.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.4, 1.3),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WDFN-8-1EP_4x3mm_P0.65mm_EP2.4x1.8mm': Params(
        #
        # WDFN, 8 Pin (https://www.onsemi.com/pub/Collateral/LC709203F-D.PDF)
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.5,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.05,      # body-board separation
        A2 = 0.8,       # body overall height
        b = 0.25,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = (1.8, 2.4),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WDFN-8-1EP_4x3mm_P0.65mm_EP2.4x1.8mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WDFN-8_2x2mm_P0.5mm': Params(
        #
        # DFN8 2x2, 0.5P; No exposed pad (http://www.onsemi.com/pub/Collateral/NCP4308-D.PDF)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,      # body overall length
        E = 2.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 0,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WDFN-8_2x2mm_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WQFN-14-1EP_2.5x2.5mm_P0.5mm_EP1.45x1.45mm': Params(
        #
        # 14-Lead Quad Flat, No-Lead, 2.5x2.5x0.75mm body, http://www.onsemi.com/pub/Collateral/510BR.PDF
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 2.5,      # body overall length
        E = 2.5,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 3,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (1.45, 1.45),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WQFN-14-1EP_2.5x2.5mm_P0.5mm_EP1.45x1.45mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm': Params(
        #
        # 16-Lead Quad Flat, No-Lead, 3x3x0.8mm body, https://www.ti.com/lit/ds/symlink/tpa6132a2.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.4,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.05,      # body-board separation
        A2 = 0.75,       # body overall height
        b = 0.24,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (1.6, 1.6),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm': Params(
        #
        # 16-Lead Quad Flat, No-Lead, 3x3x0.8mm body, http://www.onsemi.com/pub/Collateral/510BS.PDF
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,      # body overall length
        E = 3.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 0.5,       # body overall height
        b = 0.21,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = (1.75, 1.75),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WQFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm': Params(
        #
        # 16-Lead Plastic Quad Flat, No Lead - 4x4x0.75 mm Body [WQFN]; Thermal pad; (http://www.ti.com/lit/ds/symlink/drv8833.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.65,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 4,      # number of pins along X axis (width)
        npy = 4,      # number of pins along y axis (length)
        epad = None,    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WQFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WQFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,      # body overall length
        E = 4.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.2,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 6,      # number of pins along X axis (width)
        npy = 6,      # number of pins along y axis (length)
        epad = (2.7, 2.7),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WQFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm': Params(
        #
        # QFN, 32-Leads, Body 5x5x0.8mm, Pitch 0.5mm, Thermal Pad 3.1x3.1mm; (see Texas Instruments LM25119 http://www.ti.com/lit/ds/symlink/lm25119.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        #
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,         # Fillet radius for pin edges
        L = 0.25,       # pin top flat part length (including fillet radius)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.5,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,      # body overall length
        E = 5.0,      # body overall width
        A1 = 0.1,      # body-board separation
        A2 = 1.0,       # body overall height
        b = 0.17,      # pin width
        e = 0.5,       # pin (center-to-center) distance
        m = 0.0,        # margin between pins and body
        ps = 'square',  # rounded, square pads
        npx = 8,      # number of pins along X axis (width)
        npy = 8,      # number of pins along y axis (length)
        epad = (3.1, 3.1),    # e Pad #epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes/',
        ),

    'AMS_LGA-20_4.7x4.5mm_P0.65mm': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is AMS_LGA-20_4.7x4.5mm_P0.65mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.3,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.5,         # body length
        E = 4.7,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.26,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 5,           # number of pins along X axis (width)
        npy = 5,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'AMS_LGA-20_4.7x4.5mm_P0.65mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'Bosch_LGA-14_3x2.5mm_P0.5mm': Params(
        #
        # LGA-14 Bosch https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMI160-DS000-07.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Bosch_LGA-14_3x2.5mm_P0.5mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.5,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 2.5,         # body length
        E = 3.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.25,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 4,           # number of pins along X axis (width)
        npy = 3,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Bosch_LGA-14_3x2.5mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.5,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 2.5,         # body length
        E = 2.5,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.25,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 0,           # number of pins along X axis (width)
        npy = 4,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering': Params(
        #
        # LGA-8, https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMP280-DS001-18.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.5,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,         # body length
        E = 2.5,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.25,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 0,           # number of pins along X axis (width)
        npy = 4,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering': Params(
        #
        # Bosch  LGA, 8 Pin (https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME680-DS001-00.pdf#page=44), generated with kicad-footprint-generator ipc_lga_layoutBorder_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.5,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,         # body length
        E = 3.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.25,          # pin width
        e = 0.8,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 0,           # number of pins along X axis (width)
        npy = 4,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Bosch_LGA-8_3x3mm_P0.8mm_ClockwisePinNumbering',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y': Params(
        #
        # LGA, 14 Pin (http://www.st.com/resource/en/datasheet/lis2dh.pdf), generated with kicad-footprint-generator ipc_lga_layoutBorder_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,         # body length
        E = 2.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.14,          # pin width
        e = 0.35,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 4,           # number of pins along X axis (width)
        npy = 3,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y': Params(
        #
        # LGA, 14 Pin (http://www.st.com/resource/en/datasheet/lsm6ds3.pdf), generated with kicad-footprint-generator ipc_lga_layoutBorder_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.4,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 2.5,         # body length
        E = 3.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 4,           # number of pins along X axis (width)
        npy = 3,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y': Params(
        #
        # LGA, 14 Pin (http://www.st.com/resource/en/datasheet/lsm303dlhc.pdf), generated with kicad-footprint-generator ipc_lga_layoutBorder_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.6,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,         # body length
        E = 3.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.32,          # pin width
        e = 0.8,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 6,           # number of pins along X axis (width)
        npy = 1,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'LGA-8_3x5mm_P1.25mm': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is LGA-8_3x5mm_P1.25mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.95,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,         # body length
        E = 3.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.39,          # pin width
        e = 1.25,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 4,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'LGA-8_3x5mm_P1.25mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'Linear_LGA-133_15.0x15.0_Layout12x12_P1.27mm': Params(
        #
        # Analog Devices (Linear Tech), 133-pin LGA uModule, 15.0x15.0x4.32mm, https://www.analog.com/media/en/technical-documentation/data-sheets/4637fc.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Linear_LGA-133_15.0x15.0_Layout12x12_P1.27mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.5,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,        # first pin indicator radius
        fp_d = 0.5,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 15.0,         # body length
        E = 15.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.5,          # pin width
        e = 1.27,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 12,           # number of pins along X axis (width)
        npy = 12,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Linear_LGA-133_15.0x15.0_Layout12x12_P1.27mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'Texas_SIL0010A_MicroSiP-10-1EP_3.8x3mm_P0.6mm_EP0.7x2.9mm': Params(
        #
        # Texas SIL0010A MicroSiP, 10 Pin (http://www.ti.com/lit/ml/mpds579b/mpds579b.pdf), generated with kicad-footprint-generator ipc_lga_layoutBorder_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_SIL0010A_MicroSiP-10-1EP_3.8x3mm_P0.6mm_EP0.7x2.9mm_ThermalVias.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.8,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,        # first pin indicator radius
        fp_d = 0.3,        # first pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,         # body length
        E = 3.8,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.24,          # pin width
        e = 0.6,          # pin (center-to-center) distance
        m = 0.1,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 5,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = (2.5, 0.7),       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_SIL0010A_MicroSiP-10-1EP_3.8x3mm_P0.6mm_EP0.7x2.9mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_LGA.3dshapes',      # destination directory
        ),

    'Infineon_MLPQ-16-14-1EP_4x4mm_P0.5mm': Params(
        #
        # MLPQ 32 leads, 7x7mm, 0.127mm stencil (https://www.infineon.com/dgdl/Infineon-AN1170-AN-v05_00-EN.pdf?fileId=5546d462533600a40153559ac3e51134)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Infineon_MLPQ-16-14-1EP_4x4mm_P0.5mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.15,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 4,           # number of pins along X axis (width)
        npy = 4,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = (10, 15),          # pin excluded
        modelName = 'Infineon_MLPQ-16-14-1EP_4x4mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm': Params(
        #
        # MLPQ 48 leads, 7x7mm (https://www.infineon.com/dgdl/irs2093mpbf.pdf?fileId=5546d462533600a401535675fb892793)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,         # body length
        E = 7.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 12,           # number of pins along X axis (width)
        npy = 12,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_R-PWQFN-N28_EP2.1x3.1mm': Params(
        #
        # QFN, 28 Pin (http://www.ti.com/lit/ds/symlink/tps51363.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_R-PWQFN-N28_EP2.1x3.1mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.5,         # body length
        E = 3.5,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 9,           # number of pins along X axis (width)
        npy = 5,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_R-PWQFN-N28_EP2.1x3.1mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_RGE0024H_EP2.7x2.7mm': Params(
        #
        # Texas  QFN, 24 Pin (http://www.ti.com/lit/ds/symlink/tlc5971.pdf#page=42&zoom=200,-13,779), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_RGE0024H_EP2.7x2.7mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 6,           # number of pins along X axis (width)
        npy = 6,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_RGE0024H_EP2.7x2.7mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PVQFN-N16_EP2.7x2.7mm': Params(
        #
        # QFN, 16 Pin (http://www.ti.com/lit/ds/symlink/msp430g2001.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N16_EP2.7x2.7mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.25,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 4,           # number of pins along X axis (width)
        npy = 4,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PVQFN-N16_EP2.7x2.7mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PVQFN-N20_EP2.4x2.4mm': Params(
        #
        # QFN, 20 Pin (http://www.ti.com/lit/ds/symlink/cc1101.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N20_EP2.4x2.4mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 5,           # number of pins along X axis (width)
        npy = 5,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PVQFN-N20_EP2.4x2.4mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'QFN-20-1EP_4x4mm_P0.5mm': Params(
        #
        # 20-Pin Plastic Quad Flatpack No-Lead Package, Body 4.0x4.0x0.9mm, Pad 3.52x2.62mm, Texas Instruments (see http://www.ti.com/lit/gpn/drv8662)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N20_EP2.7x2.7mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 5,           # number of pins along X axis (width)
        npy = 5,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'QFN-20-1EP_4x4mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PVQFN-N24_EP2.1x2.1mm': Params(
        #
        # QFN, 24 Pin (http://www.ti.com/lit/ds/symlink/msp430fr5720.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N24_EP2.1x2.1mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 4.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 6,           # number of pins along X axis (width)
        npy = 6,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PVQFN-N24_EP2.1x2.1mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PVQFN-N32_EP3.45x3.45mm': Params(
        #
        # QFN, 32 Pin (http://www.ti.com/lit/ds/symlink/msp430f1122.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N32_EP3.45x3.45mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,         # body length
        E = 5.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 8,           # number of pins along X axis (width)
        npy = 8,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PVQFN-N32_EP3.45x3.45mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PVQFN-N36': Params(
        #
        # 36 pin S-PVQFN Texas http://www.ti.com/lit/ds/slvsba5d/slvsba5d.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N36.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,         # body length
        E = 6.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 9,           # number of pins along X axis (width)
        npy = 9,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PVQFN-N36',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'QFN-40-1EP_6x6mm_P0.5mm': Params(
        #
        # 40-Pin Plastic Quad Flatpack No-Lead Package, Body 6.0x6.0x0.9mm, Pad 2.9x2.9mm, Texas Instruments (see http://www.ti.com/lit/ds/symlink/msp430fr5731.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N40_EP2.9x2.9mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 6.0,         # body length
        E = 6.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.25,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 10,           # number of pins along X axis (width)
        npy = 10,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'QFN-40-1EP_6x6mm_P0.5mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PVQFN-N48_EP5.15x5.15mm': Params(
        #
        # QFN, 48 Pin (http://www.ti.com/lit/ds/symlink/msp430f5232.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N48_EP5.15x5.15mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 7.0,         # body length
        E = 7.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 12,           # number of pins along X axis (width)
        npy = 12,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PVQFN-N48_EP5.15x5.15mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PVQFN-N64_EP4.25x4.25mm': Params(
        #
        # QFN, 64 Pin (http://www.ti.com/lit/ds/symlink/msp430f5217.pdf), generated with kicad-footprint-generator ipc_dfn_qfn_generator.py
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PVQFN-N64_EP4.25x4.25mm.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,         # body length
        E = 9.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 16,           # number of pins along X axis (width)
        npy = 16,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PVQFN-N64_EP4.25x4.25mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PWQFN-N20': Params(
        #
        # 20-Pin Plastic Quad Flatpack No-Lead Package, Body 3.0x3.0x0.8mm, Texas Instruments (http://www.ti.com/lit/ds/symlink/tps22993.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PWQFN-N20.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 3.0,         # body length
        E = 3.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.15,          # pin width
        e = 0.4,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 5,           # number of pins along X axis (width)
        npy = 5,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PWQFN-N20',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_S-PWSON-N6': Params(
        #
        # 6-Lead Plastic Dual Flat 2x2mm S-PWSON-N6 DFN Texas Instruments http://www.ti.com/lit/ds/symlink/tps717.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_S-PWSON-N6.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 2.0,         # body length
        E = 2.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.25,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 3,           # number of pins along X axis (width)
        npy = 0,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_S-PWSON-N6',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_VQFN-RGR-20-1EP_3.5x3.5mm_Pitch0.5mm': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_VQFN-RGR-20.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 3.5,         # body length
        E = 3.5,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.5,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 5,           # number of pins along X axis (width)
        npy = 5,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_VQFN-RGR-20-1EP_3.5x3.5mm_Pitch0.5mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_VQFN-RGW-20-1EP_5x5mm_Pitch0.65mm': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_VQFN-RGW-20.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 5.0,         # body length
        E = 5.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.3,          # pin width
        e = 0.65,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 5,           # number of pins along X axis (width)
        npy = 5,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_VQFN-RGW-20-1EP_5x5mm_Pitch0.65mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),

    'Texas_WQFN-MR-100': Params(
        #
        #
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_WQFN-MR-100_3x3-DapStencil.kicad_mod
        #
        c = 0.1,           # pin thickness, body center part height
#        K = 0.2,         # Fillet radius for pin edges
        L = 0.2,         # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.5,          # First pin indicator distance from edge
        fp_z = 0.02,       # first pin indicator depth
        ef = 0.0,          # fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.25,        # 0.45 chamfer of the epad 1st pin corner
        D = 9.0,         # body length
        E = 9.0,          # body overall width
        A1 = 0.03,          # body-board separation
        A2 = 0.75,          # body-board separation
        b = 0.2,          # pin width
        e = 0.6,          # pin (center-to-center) distance
        m = 0.0,          # margin between pins and body
        ps = 'square',          # rounded, square pads
        npx = 13,           # number of pins along X axis (width)
        npy = 13,           # number of pins along y axis (length)
        epad = None,       # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_WQFN-MR-100',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_DFN_QFN.3dshapes',      # destination directory
        ),
    'Texas_X2SON-4-1EP_1.1x1.4mm_P0.5mm_EP0.8x0.6mm': Params(
        #
        # Texas X2SON-4, DMR0004A, (http://www.ti.com/lit/ds/symlink/drv5032.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        #
        # The foot print that uses this 3D model is Texas_X2SON-4-1EP_1.1x1.4mm_P0.5mm_EP0.8x0.6mm.kicad_mod
        #
        c = 0.2,           # pin thickness, body center part height
#        K = 0.2,           # Fillet radius for pin edges
        L = 0.22,          # pin bottom flat part length (including corner arc)
        fp_s = 1,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,        # First pin indicator radius
        fp_d = 0.1,       # First pin indicator distance from edge
        fp_z = 0.02,       # First pin indicator depth
        ef = 0.0,          # Fillet of edges  Note: bigger bytes model with fillet
#        cc1 = 0.25,        # 0.45 chamfer of the 1st pin corner
        cce = 0.15,        # 0.45 chamfer of the epad 1st pin corner
        D = 1.4,           # body length
        E = 1.1,           # body overall width
        A1 = 0.025,        # body-board separation
        A2 = 0.35,         # body height
        b = 0.2,           # pin width
        e = 0.5,           # pin (center-to-center) distance
        m = 0.0,           # margin between pins and body
        ps = 'square',     # rounded, square pads
        npx = 0,           # number of pins along X axis (width)
        npy = 2,           # number of pins along y axis (length)
        epad = (0.6, 0.8), # e Pad
        excluded_pins = None,          # pin excluded
        modelName = 'Texas_X2SON-4-1EP_1.1x1.4mm_P0.5mm_EP0.8x0.6mm',            # modelName
        rotation = -90,      # rotation if required
        dest_dir_prefix = '../Package_SON.3dshapes',      # destination directory
        ),

}

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
footprints_dir_SSOP="Housings_SSOP.pretty"
##footprints_dir=None #to exclude importing of footprints


all_params_ssop = {        
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
kicad_naming_params_ssop = {  
    'ETSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ds/symlink/lm5005.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.1,             # pin thickness, body center part height
        R1 = 0.09,             # pin upper corner, inner radius
        R2 = 0.09,             # pin lower corner, inner radius
        S = 0.3,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.0,            # body height
        b = 0.25,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 10,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (4.2,3.0),          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'ETSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'HTSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm_ThermalPad': Params( # from http://www.ti.com/lit/ml/mhts001g/mhts001g.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.09,             # pin upper corner, inner radius
        R2 = 0.09,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.1,            # body height
        b = 0.25,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 10,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (6.0,3.5),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'HTSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm_ThermalPad',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'HTSSOP-28_4.4x9.7mm_Pitch0.65mm_ThermalPad': Params( # from http://www.ti.com/lit/ml/mpds033b/mpds033b.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.09,             # pin upper corner, inner radius
        R2 = 0.09,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.1,            # body height
        b = 0.25,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 14,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (9.0,3.5),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'HTSSOP-28_4.4x9.7mm_Pitch0.65mm_ThermalPad',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-8_3x3mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081660_G_MS8.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.15,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-8_3x3mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-8-1EP_3x3mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081662_K_MS8E.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (1.88,1.68),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-8-1EP_3x3mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-10_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081661_F_MS.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.23,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 5,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-10_3x3mm_Pitch0.5mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-10-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081664_I_MSE.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.23,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 5,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (1.88,1.68),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-10-1EP_3x3mm_Pitch0.5mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-12_3x4mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081668_A_MS12.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 6,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-12_3x4mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-12-1EP_3x4mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081666_G_MSE12.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 6,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (2.845,1.651),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-12-1EP_3x4mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-16_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081669_A_MS16.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-16_3x4mm_Pitch0.5mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-16-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081667_F_MSE16.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (2.84,1.65),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'MSOP-16-1EP_3x4mm_Pitch0.5mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-12-16_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081871_D_MSE16%2812%29.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = (2,4,13,15), # no pin excluded
        modelName = 'MSOP-12-16_3x4mm_Pitch0.5mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'MSOP-12-16-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081871_D_MSE16%2812%29.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (2.84,1.65),          # ePad is guessed from datasheet
        excluded_pins = (2,4,13,15), # no pin excluded
        modelName = 'MSOP-12-16-1EP_3x4mm_Pitch0.5mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'OnSemi_Micro8': Params( # from https://www.onsemi.com/pub/Collateral/846A-02.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,             # body height
        b = 0.33,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'OnSemi_Micro8',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'PSOP-44_16.9x27.17mm_Pitch1.27mm': Params( # from http://pdf.datasheetcatalog.com/datasheet/macronix/MX29F800TMI-90.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.20,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.5,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,           # first pin indicator radius
        fp_d = 0.4,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 28.5,             # body length
        E1 = 12.60,             # body width
        E = 16.03,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.69,             # body height
        b = 0.41,             # pin width
        e = 1.27,            # pin (center-to-center) distance
        npx = 22,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        modelName = 'PSOP-44_16.9x27.17mm_Pitch1.27mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'QSOP-16_3.9x4.9mm_Pitch0.635mm': Params( # from http://www.onsemi.com/pub/Collateral/492-01.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.22,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.05,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,             # body length
        E1 = 3.9,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.17,            # body-board separation
        A2 = 1.25,            # body height
        b = 0.25,             # pin width
        e = 0.635,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'QSOP-16_3.9x4.9mm_Pitch0.635mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'QSOP-24_3.9x8.7mm_Pitch0.635mm': Params( # from http://www.onsemi.com/pub/Collateral/492B-01.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.22,             # pin thickness, body center part height
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
        D1 = 8.65,             # body length
        E1 = 3.9,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.17,            # body-board separation
        A2 = 1.55,            # body height
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
    'SOP-4_4.4x2.8mm_Pitch1.27mm': Params( # from http://www.vishay.com/docs/49447/49447.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
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
        D1 = 2.8,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.0,            # body height
        b = 0.4,             # pin width
        e = 1.27,            # pin (center-to-center) distance
        npx = 2,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SOP-4_4.4x2.8mm_Pitch1.27mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SOP-16_4.4x10.4mm_Pitch1.27mm': Params( # from http://www.vishay.com/docs/49447/49447.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.2,             # pin thickness, body center part height
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
        D1 = 10.4,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.0,            # body height
        b = 0.4,             # pin width
        e = 1.27,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SOP-16_4.4x10.4mm_Pitch1.27mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-8_2.95x2.8mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds049b/mpds049b.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.1,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 2.95,             # body length
        E1 = 2.8,             # body width
        E = 4.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.05,            # body-board separation
        A2 = 1.3,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SSOP-8_2.95x2.8mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-14_5.3x6.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/msso002e/msso002e.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.17,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.2,             # body length
        E1 = 5.3,             # body width
        E = 7.8,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.0,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 7,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SSOP-14_5.3x6.2mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-16_3.9x4.9mm_Pitch0.635mm': Params( # from http://docs-asia.electrocomponents.com/webdocs/0156/0900766b80156779.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.10,          # top part of body is that much smaller
        c = 0.2,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.05,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,             # body length
        E1 = 3.9,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.75,            # body height
        b = 0.25,             # pin width
        e = 0.635,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SSOP-16_3.9x4.9mm_Pitch0.635mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-16_4.4x5.2mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/565AM.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
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
        D1 = 5.2,             # body length
        E1 = 4.4,             # body width
        E = 6.5,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.3,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SSOP-16_4.4x5.2mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-16_5.3x6.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds507/mpds507.pdf
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
        D1 = 6.2,             # body length
        E1 = 5.3,             # body width
        E = 7.8,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.0,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SSOP-16_5.3x6.2mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-20_4.4x6.5mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/565AM.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
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
        D1 = 6.5,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.3,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 10,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        modelName = 'SSOP-20_4.4x6.5mm_Pitch0.65mm',
        rotation = -90,       # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-20_5.3x7.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds508/mpds508.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
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
        A2 = 2.0,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SSOP-20_5.3x7.2mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-24_3.9x8.7mm_Pitch0.635mm': Params( # from http://cds.linear.com/docs/en/packaging/05081641_B_GN24.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.22,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 8.7,       # body length
        E1 = 3.9,       # body width
        E = 6.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.55,  # body height
        b = 0.25,  # pin width
        e = 0.635,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SSOP-24_3.9x8.7mm_Pitch0.635mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-24_5.3x8.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds509/mpds509.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 8.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.0,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SSOP-24_5.3x8.2mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-28_5.3x10.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds509/mpds509.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.0,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SSOP-28_5.3x10.2mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-48_7.5x15.9mm_Pitch0.635mm': Params( # from http://www.ti.com/lit/ml/mpds490/mpds490.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 15.9,       # body length
        E1 = 7.5,       # body width
        E = 10.35,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.79,  # body height
        b = 0.223,  # pin width
        e = 0.635,  # pin (center-to-center) distance
        npx = 24,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SSOP-48_7.5x15.9mm_Pitch0.635mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SSOP-56_7.5x18.5mm_Pitch0.635mm': Params( # from http://www.ti.com/lit/ml/mpds491/mpds491.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 18.5,       # body length
        E1 = 7.5,       # body width
        E = 10.35,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.79,  # body height
        b = 0.223,  # pin width
        e = 0.635,  # pin (center-to-center) distance
        npx = 28,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SSOP-56_7.5x18.5mm_Pitch0.635mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSOP-I-48_12x18.4mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/950AD.PDF
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 18.4,       # body width
        E = 20.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.2,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 24,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSOP-I-48_12x18.4mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSOP-II-32_21.0x10.2mm_Pitch1.27mm': Params( # from http://www.topline.tv/drawings/pdf/TSOP-T2/TSOP32T50-T2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 21.0,       # body length
        E1 = 10.16,       # body width
        E = 11.76,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.15,  # body-board separation
        A2 = 1.2,  # body height
        b = 0.4,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSOP-II-32_21.0x10.2mm_Pitch1.27mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-8_3x3mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT505-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 3.0,       # body length
        E1 = 3.0,       # body width
        E = 4.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-8_3x3mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-8_4.4x3mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT530-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 3.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-8_4.4x3mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-10_3x3mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT552-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 3.0,       # body length
        E1 = 3.0,       # body width
        E = 4.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.23,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 5,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-10_3x3mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-14_4.4x5mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT402-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 7,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-14_4.4x5mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-16_4.4x5mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT403-3.pdf
        the = 10.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.0, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-16_4.4x5mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-16-1EP_4.4x5mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/948AP.PDF
        the = 10.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.0, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (2.74,2.74), # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-16-1EP_4.4x5mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-20_4.4x6.5mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/948AP.PDF
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 6.5,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-20_4.4x6.5mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),  
    'TSSOP-24_4.4x7.8mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT355-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 7.8,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.87,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-24_4.4x7.8mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-28_4.4x9.7mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT361-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-28_4.4x9.7mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-32_6.1x11mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT361-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 11.0,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-32_6.1x11mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-38_4.4x9.7mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT510-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 19,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-38_4.4x9.7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-44_4.4x11.2mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mpds350b/mpds350b.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 11.1,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 22,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-44_4.4x11.2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-48_6.1x12.5mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mpds350b/mpds350b.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 12.5,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 24,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-48_6.1x12.5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'TSSOP-56_6.1x14mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT364-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
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
        D1 = 14.0,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.95,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 28,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='TSSOP-56_6.1x14mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'VSO-40_7.6x15.4mm_Pitch0.762mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT158-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.4,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 15.4,       # body length
        E1 = 7.6,       # body width
        E = 11.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.35,  # body height
        b = 0.36,  # pin width
        e = 0.762,  # pin (center-to-center) distance
        npx = 20,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='VSO-40_7.6x15.4mm_Pitch0.762mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'VSO-56_11.1x21.5mm_Pitch0.75mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT190-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.6,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 21.5,       # body length
        E1 = 11.0,       # body width
        E = 15.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.9,  # body height
        b = 0.36,  # pin width
        e = 0.75,  # pin (center-to-center) distance
        npx = 28,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='VSO-56_11.1x21.5mm_Pitch0.75mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'VSSOP-8_2.3x2mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT765-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.05,       # pin upper corner, inner radius
        R2 = 0.05,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 2.0,       # body length
        E1 = 2.3,       # body width
        E = 3.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.75,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='VSSOP-8_2.3x2mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'VSSOP-8_2.4x2.1mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT765-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.05,       # pin upper corner, inner radius
        R2 = 0.05,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 2.1,       # body length
        E1 = 2.4,       # body width
        E = 3.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.75,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='VSSOP-8_2.4x2.1mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
    'SOP-4_3.8x4.1mm_Pitch2.54mm': Params( # from http://www.ixysic.com/home/pdfs.nsf/www/CPC1017N.pdf/$file/CPC1017N.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.15,       # pin upper corner, inner radius
        R2 = 0.15,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 4.089,       # body length
        E1 = 3.81,       # body width
        E = 6.096,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.0,  # body height
        b = 0.381,  # pin width
        e = 2.54,  # pin (center-to-center) distance
        npx = 2,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName ='SOP-4_3.8x4.1mm_Pitch2.54mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SSOP'
        ),
}
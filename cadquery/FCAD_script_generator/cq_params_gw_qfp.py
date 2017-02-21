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


destination_dir="./generated_gw/"
# destination_dir="./"


all_params_qfp = {
    'AKA': Params( # 4x4, pitch 0.65 20pin 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 4.0,       # body length
        E1 = 4.0,       # body width
        E = 5.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 5,   # number of pins along X axis (width)
        npy = 5,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp20_4x4_p032', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'ABD': Params( # 7x7, 0.4 pitch, 64 pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 8.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,   # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp32_7x7_p04', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'AFB': Params( # 20x20, 0.5 pitch, 144pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 21.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,   # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp64_20x20_p05', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'ACB': Params( # 10x10, 0.8 pitch, 44 pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 11.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.37,  # pin width
        e = 0.8,   # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp44_10x10_p08', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'ACC': Params( # 10x10, 0.65 pitch, 52 pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 11.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp52_10x10_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'ACE': Params( # 10x10, 0.4 pitch, 80 pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 11.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp80_10x10_p04', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'ADC': Params( # 12x12, 0.65 pitch, 64 pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 13.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp64_12x12_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'ADD': Params( # 12x12, 0.5 pitch, 80 pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 13.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp80_12x12_p05', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'AEC': Params( # 14x14, 0.65 pitch, 80 pins, 1mm height
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 15.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp80_14x14_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'MCP100': Params( # 14x14, 0.5 pitch, 100 pins, 1.0mm height  LQFP100 p05 microchip maui
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.45, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation  maui to check
        A2 = 0.9,  # body height
        b = 0.20,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp100_14x14_p05', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'MCP64': Params( # 10x10, 0.5 pitch, 64 pins, 1.2mm height  LQFP64 p05 microchip maui
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.45, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation  maui to check
        A2 = 1.1,  # body height
        b = 0.20,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'qfp64_10x10_p05', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
}

kicad_naming_params_qfp = {
    'LQFP-32_5x5mm_Pitch0.5mm': Params(
    #from http://www.nxp.com/documents/outline_drawing/SOT401-1.pdf    
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 5.0,       # body width
        E = 7.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 8,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-32_5x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-32-1EP_5x5mm_Pitch0.5mm': Params(
    #from http://www.nxp.com/documents/outline_drawing/SOT401-1.pdf    
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 5.0,       # body width
        E = 7.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 8,   # number of pins along y axis (length)
        epad = (3.45,3.45), # e Pad
        modelName = 'LQFP-32-1EP_5x5mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-32_7x7mm_Pitch0.8mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT358-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, #0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 8,   # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-32_7x7mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-36_7x7mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub_link/Collateral/561AV.PDF
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.7,  # body height
        b = 0.3,  # pin width
        e = 0.65,   # pin (center-to-center) distance
        npx = 9,  # number of pins along X axis (width)
        npy = 9,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-36_7x7mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-44_10x10mm_Pitch0.8mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT389-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.40,  # pin width
        e = 0.8,   # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-44_10x10mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-48_7x7mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT313-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,   # pin (center-to-center) distance
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-48_7x7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-52_10x10mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1671-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-52_10x10mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-52-1EP_10x10mm_Pitch0.65mm': Params(
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 13,  # number of pins along X axis (width)
        npy = 13,  # number of pins along y axis (length)
        epad = (4.8,4.8), # e Pad
        modelName = 'LQFP-52-1EP_10x10mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-64_7x7mm_Pitch0.4mm': Params( # http://www.nxp.com/documents/outline_drawing/SOT414-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-64_7x7mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-64_10x10mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT314-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-64_10x10mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-64-1EP_10x10mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT314-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = (6.5,6.5), # e Pad
        modelName = 'LQFP-64-1EP_10x10mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-64_14x14mm_Pitch0.8mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT791-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.37,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-64_14x14mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-80_12x12mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT315-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 14.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.2,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-80_12x12mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-100_14x14mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT407-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-100_14x14mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-128_14x14mm_Pitch0.4mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT315-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 32,  # number of pins along X axis (width)
        npy = 32,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-128_14x14mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-128_14x20mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT425-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 38,  # number of pins along X axis (width)
        npy = 26,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-128_14x20mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-144_20x20mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT486-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-144_20x20mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-160_24x24mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT435-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 24.0,       # body length
        E1 = 24.0,       # body width
        E = 26.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 40,  # number of pins along X axis (width)
        npy = 40,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-160_24x24mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-176_20x20mm_Pitch0.4mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT1017-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 44,  # number of pins along X axis (width)
        npy = 44,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-176_20x20mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
         ),
    'LQFP-176_24x24mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT506-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 24.0,       # body length
        E1 = 24.0,       # body width
        E = 26.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 44,  # number of pins along X axis (width)
        npy = 44,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-176_24x24mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-208_28x28mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT459-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 28.0,       # body length
        E1 = 28.0,       # body width
        E = 30.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 52,  # number of pins along X axis (width)
        npy = 52,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-208_28x28mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'LQFP-216_24x24mm_Pitch0.4mm': Params( # from https://www.renesas.com/en-in/package-image/pdf/outdrawing/p216gm-40-gby.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 24.0,       # body length
        E1 = 24.0,       # body width
        E = 26.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.4,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 54,  # number of pins along X axis (width)
        npy = 54,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'LQFP-216_24x24mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'PQFP-80_14x20mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ds/symlink/tl16pir552.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 14.0,       # body width
        E = 17.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.7,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 24,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'PQFP-80_14x20mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'PQFP-100_14x20mm_Pitch0.65mm': Params( # from http://pdf1.alldatasheet.com/datasheet-pdf/view/181852/STMICROELECTRONICS/PQFP100.html
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 20.0,       # body width
        E = 23.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 3.4,  # body height
        b = 0.31,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 30,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'PQFP-100_14x20mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'PQFP-256_28x28mm_Pitch0.4mm': Params( # from http://www.topline.tv/drawings/pdf/qfp/QFP256T15.7-2.6.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 28.0,       # body length
        E1 = 28.0,       # body width
        E = 30.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.5,  # body-board separation
        A2 = 3.5,  # body height
        b = 0.2,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 64,  # number of pins along X axis (width)
        npy = 64,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'PQFP-256_28x28mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-32_7x7mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ml/mpqf112/mpqf112.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.37,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 8,  # number of pins along X axis (width)
        npy = 8,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-32_7x7mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-44_10x10mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ml/mpqf075/mpqf075.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-44_10x10mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-44-1EP_10x10mm_Pitch0.8mm': Params( # from http://www.ti.com/lit/ml/mpqf074c/mpqf074c.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 11,  # number of pins along X axis (width)
        npy = 11,  # number of pins along y axis (length)
        epad = (4.5,4.5), # e Pad
        modelName = 'TQFP-44-1EP_10x10mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-48_7x7mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf019a/mtqf019a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-48_7x7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-48-1EP_7x7mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf019a/mtqf019a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 12,  # number of pins along X axis (width)
        npy = 12,  # number of pins along y axis (length)
        epad = (3.5,3.5), # e Pad
        modelName = 'TQFP-48-1EP_7x7mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-64_7x7mm_Pitch0.4mm': Params( # from http://www.ti.com/lit/ml/mpqf039a/mpqf039a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.0,       # body length
        E1 = 7.0,       # body width
        E = 9.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.16,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-64_7x7mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-64_10x10mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf006a/mtqf006a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.0,       # body length
        E1 = 10.0,       # body width
        E = 12.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-64_10x10mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-64_14x14mm_Pitch0.8mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.37,  # pin width
        e = 0.8,  # pin (center-to-center) distance
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-64_14x14mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-80_12x12mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mtqf009a/mtqf009a.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 14.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-80_12x12mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-80_14x14mm_Pitch0.65mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.32,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-80_14x14mm_Pitch0.65mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-100_12x12mm_Pitch0.4mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 12.0,       # body width
        E = 14.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-100_12x12mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-100_14x14mm_Pitch0.5mm': Params( # from http://ww1.microchip.com/downloads/en/PackagingSpec/00049AR.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 25,  # number of pins along X axis (width)
        npy = 25,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-100_14x14mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-120_14x14mm_Pitch0.4mm': Params( # from http://www.ti.com/lit/ml/mpqf012/mpqf012.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 30,  # number of pins along X axis (width)
        npy = 30,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-120_14x14mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-128_14x14mm_Pitch0.4mm': Params( # from http://www.ti.com/lit/ml/mpqf013/mpqf013.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 14.0,       # body width
        E = 16.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 32,  # number of pins along X axis (width)
        npy = 32,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-128_14x14mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
    'TQFP-144_16x16mm_Pitch0.4mm': Params( # from http://ww1.microchip.com/downloads/en/DeviceDoc/70616g.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 16.0,       # body length
        E1 = 16.0,       # body width
        E = 18.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.18,  # pin width
        e = 0.4,  # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-144_16x16mm_Pitch0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
	'TQFP-144_20x20mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mpqf082/mpqf082.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.1,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 20.0,       # body length
        E1 = 20.0,       # body width
        E = 22.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 36,  # number of pins along X axis (width)
        npy = 36,  # number of pins along y axis (length)
        epad = None, # e Pad
        modelName = 'TQFP-144_20x20mm_Pitch0.5mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'qfp'
        ),
}
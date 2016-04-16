# -*- coding: utf8 -*-
# !/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

# file of parametric definitions

from collections import namedtuple
import cq_params_gw_soic  # modules parameters
from cq_params_gw_soic import *

# destination_dir="./generated_gw/"
# destination_dir="./"
# case_color = (0.1, 0.1, 0.1)
# pins_color = (0.9, 0.9, 0.9)


all_params_ssop = {
    'SSOP_20': Params(       # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=7.2,                  # body length
        E1=5.3,                  # body width
        E=7.8,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.1,                  # body-board separation
        A2=1.9,                  # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=10,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_20_53x72_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',  # dest dir
        exclude=None,            # pins to exclude
        excludei=None            # pins to exclude
    ),
    'SSOP_20_Pad': Params(   # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=7.2,                  # body length
        E1=5.3,                  # body width
        E=7.8,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=10,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=(5.0, 3.0),         # e Pad
        modelName='ssop_20_53x72_pad_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_24_Pad': Params(   # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=8.2,                  # body length
        E1=5.3,                  # body width
        E=7.8,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=12,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=(5.0, 3.0),         # e Pad
        modelName='ssop_24_82x53_pad_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_24': Params(       # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=8.2,                  # body length
        E1=5.3,                  # body width
        E=7.8,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=12,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_24_82x53_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_24_N': Params(     # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=8.6,                  # body length
        E1=3.9,                  # body width
        E=6,                     # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.635,                 # pin (center-to-center) distance
        npx=12,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_24_N_39x86_p0635',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_8': Params(        # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=3.5,                  # body length
        E1=4.4,                  # body width
        E=6.4,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=4,                   # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_8_35x44_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_14': Params(       # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=5,                    # body length
        E1=4.4,                  # body width
        E=6.4,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=7,                   # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_14_5x44_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_16': Params(       # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=5.9,                  # body length
        E1=5.3,                  # body width
        E=7.8,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=8,                   # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_16_59x53_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_16_N': Params(     # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=4.9,                  # body length
        E1=3.9,                  # body width
        E=6,                     # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.635,                 # pin (center-to-center) distance
        npx=8,                   # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_16_N_49x39_p0635',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_28': Params(       # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=10,                   # body length
        E1=5.3,                  # body width
        E=7.8,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.35,                  # pin width
        e=0.65,                  # pin (center-to-center) distance
        npx=14,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_53x10_p065',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_44': Params(       # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=17.83,                # body length
        E1=7.5,                  # body width
        E=10.33,                 # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.2575,                # pin width
        e=0.8,                   # pin (center-to-center) distance
        npx=22,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_44_178x103_p08',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_44_p08': Params(   # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=17.83,                # body length
        E1=7.5,                  # body width
        E=10.33,                 # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.2575,                # pin width
        e=0.8,                   # pin (center-to-center) distance
        npx=22,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_44_178x103_p08',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
    'SSOP_48': Params(       # 5.6x7.2, pitch 0.65 20pin 2.0mm height
        the=12.0,                # body angle in degrees
        tb_s=0.15,               # top part of body is that much smaller
        c=0.1,                   # pin thickness, body center part height
        R1=0.1,                  # pin upper corner, inner radius
        R2=0.1,                  # pin lower corner, inner radius
        S=0.2,
        fp_r=0.5,                # first pin indicator radius
        fp_d=0.2,                # first pin indicator distance from edge
        fp_z=0.1,                # first pin indicator depth
        ef=0.00,                 # fillet of edges
        cc1=0.0,                 # 0.45 chamfer of the 1st pin corner
        D1=12.8,                 # body length
        E1=5.3,                  # body width
        E=7.8,                   # body overall width  E=E1+2*(S+L+c)
        A1=0.001,                # body-board separation
        A2=1.999,                # body height
        b=0.2575,                # pin width
        e=0.5,                   # pin (center-to-center) distance
        npx=24,                  # number of pins along X axis (width)
        npy=0,                   # number of pins along y axis (length)
        epad=None,               # e Pad
        modelName='ssop_48_128x53_p05',
        rotation=0,              # rotation if required
        dest_dir_prefix='ssop',
        exclude=None,
        excludei=None
    ),
}

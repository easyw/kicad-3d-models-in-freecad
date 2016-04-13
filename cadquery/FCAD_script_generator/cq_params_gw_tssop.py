# -*- coding: utf8 -*-
# !/usr/bin/python
#
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
# case_color=(0.1, 0.1, 0.1)
# pins_color=(0.9, 0.9, 0.9)


all_params_tssop = {
    'TSSOP_14': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=5.0,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=7,            # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=None,        # e Pad
        modelName='tssop_14_50x44_p065',
        rotation=0,       # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_14_EP': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=5.0,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=7,            # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=(2.74, 2.74),  # e Pad
        modelName='tssop_14_EP_50x44_p065',
        rotation=0,       # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_16': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=5.0,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=8,            # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=None,        # e Pad
        modelName='tssop_16_50x44_p065',
        rotation=0,       # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_16': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=5.0,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=8,            # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=(2.74, 2.74),  # e Pad
        modelName='tssop_16_EP_50x44_p065',
        rotation=0,       # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_20': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=6.5,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=10,           # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=None,        # e Pad
        modelName='tssop_20_65x44_p065',
        rotation=0,       # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_20_EP': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=6.5,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=10,           # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=(4.2, 3),     # e Pad
        modelName='tssop_20_EP_65x44_p065',
        rotation=0,       # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_24': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=7.8,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=12,           # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=None,        # e Pad
        modelName='tssop_24_78x44_p065',
        rotation=0,       # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_24_EP': Params(
        the=12.0,         # body angle in degrees
        tb_s=0.15,        # top part of body is that much smaller
        c=0.1,            # pin thickness, body center part height
        R1=0.1,           # pin upper corner, inner radius
        R2=0.1,           # pin lower corner, inner radius
        S=0.3,            # pin top flat part length (excluding corner arc)
        fp_r=0.65,        # first pin indicator radius
        fp_d=0.25,        # first pin indicator distance from edge
        fp_z=0.15,        # first pin indicator depth
        ef=0.05,          # fillet of edges
        cc1=0.0,          # 0.45 chamfer of the 1st pin corner
        D1=7.8,           # body length
        E1=4.4,           # body width
        E=6.4,            # body overall width  E=E1+2*(S+L+c)
        A1=0.1,           # body-board separation
        A2=1.1,           # body height
        b=0.25,           # pin width
        e=0.65,           # pin (center-to-center) distance
        npx=12,           # number of pins along X axis (width)
        npy=0,            # number of pins along y axis (length)
        epad=(3.25, 2.74),  # e Pad
        modelName='tssop_24_EP_78x44_p065',
        rotation=0,        # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_28_EP': Params(
        the=12.0,          # body angle in degrees
        tb_s=0.15,         # top part of body is that much smaller
        c=0.1,             # pin thickness, body center part height
        R1=0.1,            # pin upper corner, inner radius
        R2=0.1,            # pin lower corner, inner radius
        S=0.3,             # pin top flat part length (excluding corner arc)
        fp_r=0.65,         # first pin indicator radius
        fp_d=0.25,         # first pin indicator distance from edge
        fp_z=0.15,         # first pin indicator depth
        ef=0.05,           # fillet of edges
        cc1=0.0,           # 0.45 chamfer of the 1st pin corner
        D1=9.7,            # body length
        E1=4.4,            # body width
        E=6.4,             # body overall width  E=E1+2*(S+L+c)
        A1=0.1,            # body-board separation
        A2=1.1,            # body height
        b=0.25,            # pin width
        e=0.65,            # pin (center-to-center) distance
        npx=14,            # number of pins along X axis (width)
        npy=0,             # number of pins along y axis (length)
        epad=(4.75, 2.74),  # e Pad
        modelName='tssop_28_EP_97x44_p065',
        rotation=0,        # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_28_EPE': Params(
        the=12.0,          # body angle in degrees
        tb_s=0.15,         # top part of body is that much smaller
        c=0.1,             # pin thickness, body center part height
        R1=0.1,            # pin upper corner, inner radius
        R2=0.1,            # pin lower corner, inner radius
        S=0.3,             # pin top flat part length (excluding corner arc)
        fp_r=0.65,         # first pin indicator radius
        fp_d=0.25,         # first pin indicator distance from edge
        fp_z=0.15,         # first pin indicator depth
        ef=0.05,           # fillet of edges
        cc1=0.0,           # 0.45 chamfer of the 1st pin corner
        D1=9.7,            # body length
        E1=4.4,            # body width
        E=6.4,             # body overall width  E=E1+2*(S+L+c)
        A1=0.1,            # body-board separation
        A2=1.1,            # body height
        b=0.25,            # pin width
        e=0.65,            # pin (center-to-center) distance
        npx=14,            # number of pins along X axis (width)
        npy=0,             # number of pins along y axis (length)
        epad=(7.56, 3.05),  # e Pad
        modelName='tssop_28_EPE_97x44_p065',
        rotation=0,        # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_28': Params(
        the=12.0,          # body angle in degrees
        tb_s=0.15,         # top part of body is that much smaller
        c=0.1,             # pin thickness, body center part height
        R1=0.1,            # pin upper corner, inner radius
        R2=0.1,            # pin lower corner, inner radius
        S=0.3,             # pin top flat part length (excluding corner arc)
        fp_r=0.65,         # first pin indicator radius
        fp_d=0.25,         # first pin indicator distance from edge
        fp_z=0.15,         # first pin indicator depth
        ef=0.05,           # fillet of edges
        cc1=0.0,           # 0.45 chamfer of the 1st pin corner
        D1=9.7,            # body length
        E1=4.4,            # body width
        E=6.4,             # body overall width  E=E1+2*(S+L+c)
        A1=0.1,            # body-board separation
        A2=1.1,            # body height
        b=0.25,            # pin width
        e=0.65,            # pin (center-to-center) distance
        npx=14,            # number of pins along X axis (width)
        npy=0,             # number of pins along y axis (length)
        epad=None,         # e Pad
        modelName='tssop_28_97x44_p065',
        rotation=0,        # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_38': Params(
        the=12.0,     # body angle in degrees
        tb_s=0.15,    # top part of body is that much smaller
        c=0.1,        # pin thickness, body center part height
        R1=0.1,       # pin upper corner, inner radius
        R2=0.1,       # pin lower corner, inner radius
        S=0.3,        # pin top flat part length (excluding corner arc)
        fp_r=0.65,    # first pin indicator radius
        fp_d=0.25,    # first pin indicator distance from edge
        fp_z=0.15,    # first pin indicator depth
        ef=0.05,      # fillet of edges
        cc1=0.0,      # 0.45 chamfer of the 1st pin corner
        D1=9.7,       # body length
        E1=4.4,       # body width
        E=6.4,        # body overall width  E=E1+2*(S+L+c)
        A1=0.1,       # body-board separation
        A2=1.1,       # body height
        b=0.25,       # pin width
        e=0.5,        # pin (center-to-center) distance
        npx=19,       # number of pins along X axis (width)
        npy=0,        # number of pins along y axis (length)
        epad=None,    # e Pad
        modelName='tssop_38_97x44_p050',
        rotation=0,   # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_38_EP': Params(
        the=12.0,     # body angle in degrees
        tb_s=0.15,    # top part of body is that much smaller
        c=0.1,        # pin thickness, body center part height
        R1=0.1,       # pin upper corner, inner radius
        R2=0.1,       # pin lower corner, inner radius
        S=0.3,        # pin top flat part length (excluding corner arc)
        fp_r=0.65,    # first pin indicator radius
        fp_d=0.25,    # first pin indicator distance from edge
        fp_z=0.15,    # first pin indicator depth
        ef=0.05,      # fillet of edges
        cc1=0.0,      # 0.45 chamfer of the 1st pin corner
        D1=9.7,       # body length
        E1=4.4,       # body width
        E=6.4,        # body overall width  E=E1+2*(S+L+c)
        A1=0.1,       # body-board separation
        A2=1.1,       # body height
        b=0.25,       # pin width
        e=0.5,        # pin (center-to-center) distance
        npx=19,       # number of pins along X axis (width)
        npy=0,        # number of pins along y axis (length)
        epad=None,    # e Pad
        modelName='tssop_38_EP_97x44_p050',
        rotation=0,   # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_48': Params(
        the=12.0,     # body angle in degrees
        tb_s=0.15,    # top part of body is that much smaller
        c=0.1,        # pin thickness, body center part height
        R1=0.1,       # pin upper corner, inner radius
        R2=0.1,       # pin lower corner, inner radius
        S=0.3,        # pin top flat part length (excluding corner arc)
        fp_r=0.65,    # first pin indicator radius
        fp_d=0.25,    # first pin indicator distance from edge
        fp_z=0.15,    # first pin indicator depth
        ef=0.05,      # fillet of edges
        cc1=0.0,      # 0.45 chamfer of the 1st pin corner
        D1=12.5,      # body length
        E1=6.1,       # body width
        E=8.1,        # body overall width  E=E1+2*(S+L+c)
        A1=0.1,       # body-board separation
        A2=1.1,       # body height
        b=0.25,       # pin width
        e=0.5,        # pin (center-to-center) distance
        npx=24,       # number of pins along X axis (width)
        npy=0,        # number of pins along y axis (length)
        epad=None,    # e Pad
        modelName='tssop_48_125x61_p050',
        rotation=0,   # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
    'TSSOP_56': Params(
        the=12.0,     # body angle in degrees
        tb_s=0.15,    # top part of body is that much smaller
        c=0.1,        # pin thickness, body center part height
        R1=0.1,       # pin upper corner, inner radius
        R2=0.1,       # pin lower corner, inner radius
        S=0.3,        # pin top flat part length (excluding corner arc)
        fp_r=0.65,    # first pin indicator radius
        fp_d=0.25,    # first pin indicator distance from edge
        fp_z=0.15,    # first pin indicator depth
        ef=0.05,      # fillet of edges
        cc1=0.0,      # 0.45 chamfer of the 1st pin corner
        D1=14.0,      # body length
        E1=6.1,       # body width
        E=8.1,        # body overall width  E=E1+2*(S+L+c)
        A1=0.1,       # body-board separation
        A2=1.1,       # body height
        b=0.25,       # pin width
        e=0.5,        # pin (center-to-center) distance
        npx=28,       # number of pins along X axis (width)
        npy=0,        # number of pins along y axis (length)
        epad=None,    # e Pad
        modelName='tssop_56_140x61_p050',
        rotation=0,   # rotation if required
        dest_dir_prefix='tssop',
        exclude=None,
        excludei=None
        ),
}

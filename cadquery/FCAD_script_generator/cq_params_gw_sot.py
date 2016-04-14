# -*- coding: utf8 -*-
#!/usr/bin/python
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
# case_color=(0.1, 0.1, 0.1)
# pins_color=(0.9, 0.9, 0.9)


all_params_sot = {
    'SOT23_3': Params(  # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=3.0,             # body length
        E1=1.3,             # body width
        E=2.35,             # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.40,             # pin width
        e=0.95,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot23_3_24x30_p095',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=(1,),
        excludei=(0, 2,)
    ),
    'SOT23_5': Params(  # 1.8x3.1, pitch 0.95 5pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.05,             # pin top flat part length (excluding corner arc)
        fp_r=0.25,          # first pin indicator radius
        fp_d=0.1,           # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.9,             # body length
        E1=1.63,            # body width
        E=2.8,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.40,             # pin width
        e=0.95,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot23_5_16x28_p095',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=(1,)
    ),
    'SOT23_6': Params(  # 1.8x3.1, pitch 0.95 5pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.05,             # pin top flat part length (excluding corner arc)
        fp_r=0.25,          # first pin indicator radius
        fp_d=0.1,           # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.9,             # body length
        E1=1.63,            # body width
        E=2.8,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.40,             # pin width
        e=0.95,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot23_6_16x28_p095',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'SOT23_8': Params(  # 1.8x3.1, pitch 0.95 5pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.05,             # pin top flat part length (excluding corner arc)
        fp_r=0.25,          # first pin indicator radius
        fp_d=0.1,           # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.9,             # body length
        E1=1.63,            # body width
        E=2.8,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.30,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=4,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot23_8_16x28_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'TSOT23_3': Params(  # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=3.0,             # body length
        E1=1.3,             # body width
        E=2.35,             # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=0.85,            # body height
        b=0.40,             # pin width
        e=0.95,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='tsot23_3_24x30_p095',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=(1,),
        excludei=(0, 2,)
    ),
    'TSOT23_5': Params(  # 1.8x3.1, pitch 0.95 5pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.05,             # pin top flat part length (excluding corner arc)
        fp_r=0.25,          # first pin indicator radius
        fp_d=0.1,           # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.9,             # body length
        E1=1.63,            # body width
        E=2.8,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=0.85,            # body height
        b=0.40,             # pin width
        e=0.95,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='tsot23_5_16x28_p095',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=(1,)
    ),
    'TSOT23_6': Params(  # 1.8x3.1, pitch 0.95 5pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.05,             # pin top flat part length (excluding corner arc)
        fp_r=0.25,          # first pin indicator radius
        fp_d=0.1,           # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.9,             # body length
        E1=1.63,            # body width
        E=2.8,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=0.85,            # body height
        b=0.40,             # pin width
        e=0.95,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='tsot23_6_16x28_p095',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'TSOT23_8': Params(  # 1.8x3.1, pitch 0.95 5pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.05,             # pin top flat part length (excluding corner arc)
        fp_r=0.25,          # first pin indicator radius
        fp_d=0.1,           # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.9,             # body length
        E1=1.63,            # body width
        E=2.8,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=0.85,            # body height
        b=0.30,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=4,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='tsot23_8_16x28_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'SOT23_8': Params(  # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.05,             # pin top flat part length (excluding corner arc)
        fp_r=0.25,          # first pin indicator radius
        fp_d=0.1,           # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=3.1,             # body length
        E1=1.8,             # body width
        E=2.9,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.35,            # body height
        b=0.40,             # pin width
        e=0.95,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot23_8_18x29_p095',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'SC70_3': Params(   # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.2,             # body length
        E1=1.35,            # body width
        E=2.2,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.35,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sc70_3_22x22_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=(1,),
        excludei=(0, 2,)
    ),
    'SC70_5': Params(   # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.2,             # body length
        E1=1.35,            # body width
        E=2.2,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.35,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sc70_5_22x22_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=(1,)
    ),
    'SC70_6': Params(   # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.2,             # body length
        E1=1.35,            # body width
        E=2.2,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.35,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sc70_6_22x22_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'SOT323': Params(   # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.1,             # body length
        E1=1.2,             # body width
        E=2.3,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.30,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot323_21x23_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=(1,),
        excludei=(0, 2,)
    ),
    'SOT323_6': Params(  # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2.1,             # body length
        E1=1.2,             # body width
        E=2.3,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=1.1,             # body height
        b=0.30,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot323_6_21x23_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'SOT563': Params(   # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=1.6,             # body length
        E1=1.2,             # body width
        E=1.6,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=0.6,             # body height
        b=0.20,             # pin width
        e=0.5,              # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot563_16x16_p05',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
    'SOT363': Params(   # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the=8.0,            # body angle in degrees
        tb_s=0.05,          # top part of body is that much smaller
        c=0.15,             # pin thickness, body center part height
        R1=0.1,             # pin upper corner, inner radius
        R2=0.1,             # pin lower corner, inner radius
        S=0.00,             # pin top flat part length (excluding corner arc)
        fp_r=0.15,          # first pin indicator radius
        fp_d=0.08,          # first pin indicator distance from edge
        fp_z=0.03,          # first pin indicator depth
        ef=0.02,            # 0.02,      # fillet of edges
        cc1=0.0,            # 0.45 chamfer of the 1st pin corner
        D1=2,               # body length
        E1=1.25,            # body width
        E=2.1,              # body overall width  E=E1+2*(S+L+c)
        A1=0.1,             # body-board separation
        A2=0.95,            # body height
        b=0.20,             # pin width
        e=0.65,             # pin (center-to-center) distance
        npx=3,              # number of pins along X axis (width)
        npy=0,              # number of pins along y axis (length)
        epad=None,          # e Pad
        modelName='sot323_16x16_p065',
        rotation=0,         # rotation if required
        dest_dir_prefix='sot',
        exclude=None,
        excludei=None
    ),
}

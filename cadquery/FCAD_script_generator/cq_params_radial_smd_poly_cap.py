# -*- coding: utf8 -*-
# !/usr/bin/python
#
# This is derived from a cadquery script to make models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

# file of parametric definitions

from collections import namedtuple

destination_dir = "/generated_cap/"

# body color
base_color = (39, 39, 39)
body_color = (220, 220, 220)
mark_color = (190, 15, 15)
pins_color = (240, 240, 240)

# Parametric Values
Params = namedtuple("Params", [
    'L',   # overall height
    'D',   # diameter
    'A',   # base width (x&y)
    'H',   # max width (x) with pins
    'P',   # distance between pins
    'W',   # pin width
    'modelName',  # modelName
    'rotation',   # rotation if required
    'dest_dir_prefix'  # destination dir prefix
])

all_params_radial_smd_poly_cap = {  # Aluminum SMD capacitors
    "G_D100_L100": Params(  # note L model height
        L=10.2,    # overall height
        D=10.,     # diameter
        A=10.3,    # base width (x&y)
        H=12.,     # max width (x) with pins
        P=4.6,     # distance between pins
        W=0.9,     # pin width
        modelName='c_el_poly_G_D100_L100',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "F_D80_L100": Params(  # note L model height
        L=10.2,    # overall height
        D=8.,     # diameter
        A=8.3,    # base width (x&y)
        H=10.,     # max width (x) with pins
        P=3.1,     # distance between pins
        W=0.9,     # pin width
        modelName='c_el_poly_F_D80_L100',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "E_D80_L62": Params(  # note L model height
        L=6.2,    # overall height
        D=8.,     # diameter
        A=8.3,    # base width (x&y)
        H=9.5,     # max width (x) with pins
        P=2.2,     # distance between pins
        W=0.65,     # pin width
        modelName='c_el_poly_E_D80_L62',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "D8_D63_L77": Params(  # note L model height
        L=7.7,    # overall height
        D=6.3,     # diameter
        A=6.6,    # base width (x&y)
        H=7.8,     # max width (x) with pins
        P=1.8,     # distance between pins
        W=0.65,     # pin width
        modelName='c_el_poly_D8_D63_L77',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "D_D63_L54": Params(  # note L model height
        L=5.4,    # overall height
        D=6.3,     # diameter
        A=6.6,    # base width (x&y)
        H=7.8,     # max width (x) with pins
        P=1.8,     # distance between pins
        W=0.65,     # pin width
        modelName='c_el__poly_D_D63_L54',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "C_D50_L54": Params(  # note L model height
        L=5.4,    # overall height
        D=5.0,     # diameter
        A=5.3,    # base width (x&y)
        H=6.5,     # max width (x) with pins
        P=1.5,     # distance between pins
        W=0.65,     # pin width
        modelName='c_el_poly_C_D50_L54',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "B_D40_L54": Params(  # note L model height
        L=5.4,    # overall height
        D=4.0,     # diameter
        A=4.3,    # base width (x&y)
        H=5.5,     # max width (x) with pins
        P=1.0,     # distance between pins
        W=0.65,     # pin width
        modelName='c_el_poly_B_D40_L54',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "A_D30_L54": Params(  # note L model height
        L=5.4,    # overall height
        D=3.0,     # diameter
        A=3.3,    # base width (x&y)
        H=4.5,     # max width (x) with pins
        P=0.6,     # distance between pins
        W=0.55,     # pin width
        modelName='c_el_poly_A_D30_L54',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "H_D125_L135": Params(  # note L model height
        L=13.5,    # overall height
        D=12.5,     # diameter
        A=13.5,    # base width (x&y)
        H=15.0,     # max width (x) with pins
        P=4.4,     # distance between pins
        W=0.9,     # pin width
        modelName='c_el_poly_H_D125_L135',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "J_D100_L135": Params(  # note L model height
        L=13.5,    # overall height
        D=10.0,     # diameter
        A=10.3,    # base width (x&y)
        H=12.0,     # max width (x) with pins
        P=4.6,     # distance between pins
        W=0.9,     # pin width
        modelName='c_el_poly_J_D100_L135',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "K_D100_L165": Params(  # note L model height
        L=16.5,    # overall height
        D=10.0,     # diameter
        A=10.3,    # base width (x&y)
        H=12.0,     # max width (x) with pins
        P=4.6,     # distance between pins
        W=0.9,     # pin width
        modelName='c_el_poly_K_D100_L165',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "L_D125_L165": Params(  # note L model height
        L=16.5,    # overall height
        D=12.5,     # diameter
        A=13.5,    # base width (x&y)
        H=15.0,     # max width (x) with pins
        P=4.7,     # distance between pins
        W=0.9,     # pin width
        modelName='c_el_poly_L_D125_L165',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "P_D160_L165": Params(  # note L model height
        L=16.5,    # overall height
        D=16.0,     # diameter
        A=17.0,    # base width (x&y)
        H=15.0,     # max width (x) with pins
        P=6.7,     # distance between pins
        W=1.2,     # pin width
        modelName='c_el_poly_P_D160_L165',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "R_D180_L165": Params(  # note L model height
        L=16.5,    # overall height
        D=18.0,     # diameter
        A=19.0,    # base width (x&y)
        H=21.0,     # max width (x) with pins
        P=6.7,     # distance between pins
        W=1.2,     # pin width
        modelName='c_el_poly_R_D180_L165',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "S_D180_L215": Params(  # note L model height
        L=21.5,    # overall height
        D=18.0,     # diameter
        A=19.0,    # base width (x&y)
        H=21.0,     # max width (x) with pins
        P=6.7,     # distance between pins
        W=1.2,     # pin width
        modelName='c_el_poly_S_D180_L215',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
    "U_D160_L215": Params(  # note L model height
        L=21.5,    # overall height
        D=16.0,     # diameter
        A=17.0,    # base width (x&y)
        H=19.0,     # max width (x) with pins
        P=6.7,     # distance between pins
        W=1.2,     # pin width
        modelName='c_el_poly_U_D160_L215',  # modelName
        rotation=-90,  # rotation if required
        dest_dir_prefix='cap_El_smd_poly'
    ),
}

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

destination_dir="/Capacitors_Radial_SMD"
# destination_dir="./"

Params = namedtuple("Params", [
    'L',   # overall height
    'D',   # diameter
    'A',   # base width (x&y)
    'H',   # max width (x) with pins
    'P',   # distance between pins
    'W',   # pin width
    'modelName', # modelName
    'rotation',  # rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_radial_smd_cap = {# Aluminum SMD capacitors
        # Dimensions per http://industrial.panasonic.com/lecs/www-data/pdf/ABA0000/ABA0000PE369.pdf
    "G_D100_L100" : Params( # note L model height
        L         =10.2,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        modelName = 'c_el_G_D100_L100', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "F_D80_L100" : Params( # note L model height
        L         =10.2,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =10.,     # max width (x) with pins
        P         =3.1,     # distance between pins
        W         =0.9,     # pin width
        modelName = 'c_el_F_D80_L100', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "E_D80_L62" : Params( # note L model height
        L         =6.2,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'c_el_E_D80_L62', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "D8_D63_L77" : Params( # note L model height
        L         =7.7,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'c_el_D8_D63_L77', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "D_D63_L54" : Params( # note L model height
        L         =5.4,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'c_el_D_D63_L54', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "C_D50_L54" : Params( # note L model height
        L         =5.4,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base I haven't found a black but lighter material on Mario material specswidth (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'c_el_C_D50_L54', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "B_D40_L54" : Params( # note L model height
        L         =5.4,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'c_el_B_D40_L54', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
}

kicad_naming_params_radial_smd_cap = {# Aluminum SMD capacitors
    "CP_Elec_3x53" : Params( # note L model height
        L         =5.3,    # overall height
        D         =3.,     # diameter
        A         =3.3,    # base width (x&y)
        H         =3.8,     # max width (x) with pins
        P         =0.8,     # distance between pins
        W         =0.45,     # pin width
        modelName = 'CP_Elec_3x5.3', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_4x45" : Params( # note L model height
        L         =4.5,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_4x4.5', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_4x53" : Params( # note L model height
        L         =5.3,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_4x5.3', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_4x57" : Params( # note L model height
        L         =5.7,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_4x5.7', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_4x58" : Params( # note L model height
        L         =5.8,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_4x5.8', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_5x45" : Params( # note L model height
        L         =4.5,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_5x4.5', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_5x53" : Params( # note L model height
        L         =5.3,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_5x5.3', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_5x57" : Params( # note L model height
        L         =5.7,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_5x5.7', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_5x58" : Params( # note L model height
        L         =5.8,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_5x5.8', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    
    "CP_Elec_63x45" : Params( # note L model height
        L         =4.5,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_6.3x4.5', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_6.3x53" : Params( # note L model height
        L         =5.3,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_6.3x5.3', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_63x57" : Params( # note L model height
        L         =5.7,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_6.3x5.7', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_63x58" : Params( # note L model height
        L         =5.8,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_6.3x5.8', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_63x77" : Params( # note L model height
        L         =7.7,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_6.3x7.7', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_8x54" : Params( # note L model height
        L         =5.4,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_8x5.4', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_8x65" : Params( # note L model height
        L         =6.5,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_8x6.5', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_8x67" : Params( # note L model height
        L         =6.7,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_8x6.7', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_8x10" : Params( # note L model height
        L         =10,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_8x10', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_8x105" : Params( # note L model height
        L         =10.5,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        modelName = 'CP_Elec_8x10.5', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_10x77" : Params( # note L model height
        L         =7.7,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        modelName = 'CP_Elec_10x7.7', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_10x10" : Params( # note L model height
        L         =10,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        modelName = 'CP_Elec_10x10', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
    "CP_Elec_10x105" : Params( # note L model height
        L         =10.5,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        modelName = 'CP_Elec_10x10.5', #modelName
        rotation  = 0, # rotation if required
        dest_dir_prefix = 'cap_El_smd'
    ),
}
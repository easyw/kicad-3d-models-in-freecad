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

destination_dir="/generated_cap/"
# destination_dir="./"

# body color
base_color = (39,39,39)
body_color = (220,220,220)
mark_color = (39,39,39)
pins_color = (240, 240, 240)


### Parametric Values
##
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
        A         =5.3,    # base width (x&y)
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
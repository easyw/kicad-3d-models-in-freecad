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

destination_dir="generated_cap"
# destination_dir="./"

Params = namedtuple("Params", [
    'L' ,  # overall height
    'D' ,  # body diameter
    'd' ,  # lead diameter
    'F' ,  # lead separation (center to center)
    'll',  # lead length
    'la',  # extra lead length of the anode
    'bs',  # board separation
    'modelName', # modelName
    'rotation',  # rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_radial_th_cap = {# Aluminum TH capacitors
        # Dimensions per http://industrial.panasonic.com/lecs/www-data/pdf/ABA0000/ABA0000PE369.pdf
    "L16_D5_p05" : Params(
        L = 16.,
        D = 5.,
        d = 0.5,
        F = 2.,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        modelName = 'c_el_th_L16_D5_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_th'
    ),
    "L10_D5_p05" : Params(
        L = 10.,
        D = 5.,
        d = 0.5,
        F = 2.,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        modelName = 'c_el_th_L10_D5_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_th'
    ),
    "L11_5_D08_p05" : Params(
        L = 11.5,
        D = 8.,
        d = 0.6,
        F = 3.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        modelName = 'c_el_th_L11_5_D08_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_th'
    ),
    "L18_D15_p075" : Params(
        L = 18,
        D = 15.,
        d = 0.8,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        modelName = 'c_el_th_L11_5_D08_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_th'
    ),
    "L18_D20_p075" : Params(
        L = 18,
        D = 20.,
        d = 0.8,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        modelName = 'c_el_th_L11_5_D08_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_th'
    ),
    "L35_D12_5_p05" : Params(
        L = 35,
        D = 12.5,
        d = 0.8,
        F = 5.,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        modelName = 'c_el_th_L11_5_D08_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = 'cap_El_th'
    ),
}

kicad_naming_params_radial_smd_cap = {# Aluminum TH capacitors
    }
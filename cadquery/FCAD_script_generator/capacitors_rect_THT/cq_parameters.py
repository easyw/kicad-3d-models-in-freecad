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

destination_dir="/Capacitors_Rect_THT"
# destination_dir="./"

Params = namedtuple("Params", [
    'A' ,  # body height
    'L' ,  # body length
    'W' ,  # body width
    'd' ,  # lead diameter
    'F' ,  # lead separation (center to center)
    'll',  # lead length
    'bs',  # board separation
    'modelName', # modelName
    'rotation',  # rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_rect_th_cap = {# Aluminum TH capacitors
}

kicad_naming_params_rect_th_cap = {
    "C_Rect_L4.0mm_W2.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        A = 10.0,
        L = 4.0,
        W = 2.5,
        d = 0.5,
        F = 2.5,
        ll = 2.0,
        bs = 0.,
        modelName = 'C_Rect_L4.0mm_W2.5mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
}   
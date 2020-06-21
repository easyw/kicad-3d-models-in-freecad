# -*#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

from collections import namedtuple

destination_dir="/C_Disc_THT"
# destination_dir="./"

Params = namedtuple("Params", [
    'L' ,  # body length
    'W' ,  # body Diameter
    'd' ,  # lead diameter
    'F' ,  # lead separation (center to center)
    'll',  # lead length
    'bs',  # board separation
    'suffix', # modelName
    'rotation',  # rotation if require
])

all_params_c_disc_th_cap = {#
}

kicad_naming_params_c_disc_th_cap = {
    "C_Disc_D12.0mm_W4.4mm_P7.75mm" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        W = 4.40, # Body Width
        d = 0.90, # Lead Diameter
        F = 7.75, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D3.0mm_W2.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 3.00, # Body Length
        W = 2.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D6.0mm_W4.4mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 6.00, # Body Length
        W = 4.40, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D7.5mm_W4.4mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 7.50, # Body Length
        W = 4.40, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D5.0mm_W2.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 5.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D5.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 5.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D6.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 6.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D7.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 7.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D8.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 8.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D9.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 9.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D10.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 10.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D3.0mm_W1.6mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 3.00, # Body Length
        W = 1.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D3.4mm_W2.1mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 3.40, # Body Length
        W = 2.10, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D3.8mm_W2.6mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 3.80, # Body Length
        W = 2.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D4.3mm_W1.9mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 4.30, # Body Length
        W = 1.90, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D4.7mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 4.70, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D5.1mm_W3.2mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 5.10, # Body Length
        W = 3.20, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D7.5mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 7.50, # Body Length
        W = 2.50, # Body Width
        d = 0.70, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D7.5mm_W5.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 7.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D7.5mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 7.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D7.5mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 7.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D8.0mm_W5.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 8.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D8.0mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 8.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D8.0mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 8.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D9.0mm_W5.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 9.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D9.0mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 9.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D9.0mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 9.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D10.5mm_W5.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 10.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D10.5mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 10.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D10.5mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 10.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D11.0mm_W5.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 11.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D11.0mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 11.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D11.0mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 11.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D12.5mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 12.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D12.5mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 12.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D14.5mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 14.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D14.5mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 14.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D16.0mm_W5.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 16.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Disc_D16.0mm_W5.0mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        L = 16.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),
}

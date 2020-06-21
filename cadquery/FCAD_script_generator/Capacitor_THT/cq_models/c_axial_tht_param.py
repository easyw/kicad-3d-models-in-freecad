#!/usr/bin/python
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

destination_dir="/Capacitors_Axial_THT"
# destination_dir="./"

Params = namedtuple("Params", [
    'L' ,  # body length
    'D' ,  # body Diameter
    'd' ,  # lead diameter
    'F' ,  # lead separation (center to center)
    'll',  # lead length
    'bs',  # board separation
    'rotation',  # rotation if required
])

all_params_c_axial_th_cap = {#
}

kicad_naming_params_c_axial_th_cap = {
    "C_Axial_L3.8mm_D2.6mm_P7.50mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 3.80, # Body Length
        D = 2.60, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L3.8mm_D2.6mm_P10.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 3.80, # Body Length
        D = 2.60, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L3.8mm_D2.6mm_P12.50mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 3.80, # Body Length
        D = 2.60, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 12.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L3.8mm_D2.6mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 3.80, # Body Length
        D = 2.60, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L5.1mm_D3.1mm_P7.50mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 5.10, # Body Length
        D = 3.10, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L5.1mm_D3.1mm_P10.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 5.10, # Body Length
        D = 3.10, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L5.1mm_D3.1mm_P12.50mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 5.10, # Body Length
        D = 3.10, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 12.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L5.1mm_D3.1mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 5.10, # Body Length
        D = 3.10, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D6.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 6.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D6.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 6.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D7.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 7.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D7.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 7.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D8.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 8.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D8.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 8.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D9.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 9.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D9.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 9.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D10.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 10.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D10.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 10.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L17.0mm_D6.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 17.00, # Body Length
        D = 6.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L17.0mm_D6.5mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 17.00, # Body Length
        D = 6.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L17.0mm_D7.0mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 17.00, # Body Length
        D = 7.00, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L17.0mm_D7.0mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 17.00, # Body Length
        D = 7.00, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L19.0mm_D7.5mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 19.00, # Body Length
        D = 7.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L19.0mm_D8.0mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 19.00, # Body Length
        D = 8.00, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L19.0mm_D9.0mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 19.00, # Body Length
        D = 9.00, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L19.0mm_D9.5mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 19.00, # Body Length
        D = 9.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L22.0mm_D9.5mm_P27.50mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 22.00, # Body Length
        D = 9.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L22.0mm_D10.5mm_P27.50mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 22.00, # Body Length
        D = 10.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D6.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 6.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D6.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 6.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D7.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 7.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D7.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 7.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D8.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 8.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D8.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 8.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D9.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 9.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "C_Axial_L12.0mm_D9.5mm_P20.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 12.00, # Body Length
        D = 9.50, # Body Diameter
        d = 0.50, # Lead Diameter
        F = 20.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

}

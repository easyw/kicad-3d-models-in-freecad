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

destination_dir="/CP_Axial_THT"
# destination_dir="./"

Params = namedtuple("Params", [
    'L',  # overall height
    'D',  # body diameter
    'd',  # lead diameter
    'F',  # lead separation (center to center)
    'll',  # lead length
    'bs',  # board separation
    'rotation',  # rotation if required
])

all_params_radial_th_cap = {# Aluminum TH capacitors

}
kicad_naming_params_axial_th_cap = {
    "CP_Axial_L10.0mm_D4.5mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 10.00, # Body Length
        D = 4.50, # Body Diameter
        d = 0.70, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L10.0mm_D6.0mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 10.00, # Body Length
        D = 6.00, # Body Diameter
        d = 0.70, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L11.0mm_D8.0mm_P15.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 11.00, # Body Length
        D = 8.00, # Body Diameter
        d = 0.70, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L18.0mm_D6.5mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 18.00, # Body Length
        D = 6.50, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L18.0mm_D8.0mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 18.00, # Body Length
        D = 8.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L18.0mm_D10.0mm_P25.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 18.00, # Body Length
        D = 10.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 25.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L25.0mm_D10.0mm_P30.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 25.00, # Body Length
        D = 10.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 30.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L30.0mm_D10.0mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 30.00, # Body Length
        D = 10.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L30.0mm_D12.5mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 30.00, # Body Length
        D = 12.50, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L30.0mm_D15.0mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 30.00, # Body Length
        D = 15.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L30.0mm_D18.0mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 30.00, # Body Length
        D = 18.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L38.0mm_D18.0mm_P44.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 38.00, # Body Length
        D = 18.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 44.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L38.0mm_D21.0mm_P44.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 38.00, # Body Length
        D = 21.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 44.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L42.0mm_D23.0mm_P45.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 42.00, # Body Length
        D = 23.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 45.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L55.0mm_D23.0mm_P60.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 55.00, # Body Length
        D = 23.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 60.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L67.0mm_D23.0mm_P75.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 67.00, # Body Length
        D = 23.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 75.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L80.0mm_D23.0mm_P85.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 80.00, # Body Length
        D = 23.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 85.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L93.0mm_D23.0mm_P100.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 93.00, # Body Length
        D = 23.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 100.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L42.0mm_D26.0mm_P45.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 42.00, # Body Length
        D = 26.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 45.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L55.0mm_D26.0mm_P60.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 55.00, # Body Length
        D = 26.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 60.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L67.0mm_D26.0mm_P75.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 67.00, # Body Length
        D = 26.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 75.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L80.0mm_D26.0mm_P85.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 80.00, # Body Length
        D = 26.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 85.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L93.0mm_D26.0mm_P100.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 93.00, # Body Length
        D = 26.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 100.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L42.0mm_D29.0mm_P45.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 42.00, # Body Length
        D = 29.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 45.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L55.0mm_D29.0mm_P60.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 55.00, # Body Length
        D = 29.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 60.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L67.0mm_D29.0mm_P75.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 67.00, # Body Length
        D = 29.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 75.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L80.0mm_D29.0mm_P85.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 80.00, # Body Length
        D = 29.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 85.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L93.0mm_D29.0mm_P100.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 93.00, # Body Length
        D = 29.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 100.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L42.0mm_D32.0mm_P45.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 42.00, # Body Length
        D = 32.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 45.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L55.0mm_D32.0mm_P60.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 55.00, # Body Length
        D = 32.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 60.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L67.0mm_D32.0mm_P75.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 67.00, # Body Length
        D = 32.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 75.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L80.0mm_D32.0mm_P85.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 80.00, # Body Length
        D = 32.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 85.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L93.0mm_D32.0mm_P100.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 93.00, # Body Length
        D = 32.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 100.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L42.0mm_D35.0mm_P45.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 42.00, # Body Length
        D = 35.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 45.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L55.0mm_D35.0mm_P60.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 55.00, # Body Length
        D = 35.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 60.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L67.0mm_D35.0mm_P75.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 67.00, # Body Length
        D = 35.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 75.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L80.0mm_D35.0mm_P85.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 80.00, # Body Length
        D = 35.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 85.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L93.0mm_D35.0mm_P100.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 93.00, # Body Length
        D = 35.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 100.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L20.0mm_D10.0mm_P26.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 20.00, # Body Length
        D = 10.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 26.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L29.0mm_D10.0mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 29.00, # Body Length
        D = 10.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L20.0mm_D13.0mm_P26.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 20.00, # Body Length
        D = 13.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 26.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L29.0mm_D13.0mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 29.00, # Body Length
        D = 13.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L37.0mm_D13.0mm_P43.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 37.00, # Body Length
        D = 13.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 43.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L29.0mm_D16.0mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 29.00, # Body Length
        D = 16.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L37.0mm_D16.0mm_P43.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 37.00, # Body Length
        D = 16.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 43.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L40.0mm_D16.0mm_P48.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 40.00, # Body Length
        D = 16.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 48.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L26.5mm_D20.0mm_P33.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 26.50, # Body Length
        D = 20.00, # Body Diameter
        d = 1.10, # Lead Diameter
        F = 33.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L29.0mm_D20.0mm_P35.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 29.00, # Body Length
        D = 20.00, # Body Diameter
        d = 1.10, # Lead Diameter
        F = 35.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L34.5mm_D20.0mm_P41.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 34.50, # Body Length
        D = 20.00, # Body Diameter
        d = 1.10, # Lead Diameter
        F = 41.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L37.0mm_D20.0mm_P43.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 37.00, # Body Length
        D = 20.00, # Body Diameter
        d = 1.10, # Lead Diameter
        F = 43.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L42.5mm_D20.0mm_P49.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 42.50, # Body Length
        D = 20.00, # Body Diameter
        d = 1.10, # Lead Diameter
        F = 49.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L46.0mm_D20.0mm_P52.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 46.00, # Body Length
        D = 20.00, # Body Diameter
        d = 1.10, # Lead Diameter
        F = 52.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L11.0mm_D5.0mm_P18.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 11.00, # Body Length
        D = 5.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 18.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L11.0mm_D6.0mm_P18.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 11.00, # Body Length
        D = 6.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 18.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),

    "CP_Axial_L21.0mm_D8.0mm_P28.00mm_Horizontal" : Params(# from Jan Kriege's 3d models
        L = 21.00, # Body Length
        D = 8.00, # Body Diameter
        d = 0.90, # Lead Diameter
        F = 28.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        rotation = 0, # Rotation
    ),
}

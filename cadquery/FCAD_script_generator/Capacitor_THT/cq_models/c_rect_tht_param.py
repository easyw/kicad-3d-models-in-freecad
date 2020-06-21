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

destination_dir="/Capacitors_Rect_THT"
# destination_dir="./"

body_color_key_mks = "red body"
body_color_key_mkt = "grey body"
pins_color_key = "metal grey pins"

color_keys_mks = [
    body_color_key_mks,
    pins_color_key,
]

color_keys_mkt = [
    body_color_key_mkt,
    pins_color_key,
]

Params = namedtuple("Params", [
    'H' ,  # body height
    'L' ,  # body length
    'W' ,  # body width can be an array for multiple models
    'd' ,  # lead diameter
    'F' ,  # lead separation (center to center)
    'll',  # lead length
    'bs',  # board separation
    'series', # series 'MKS' or 'MKT'
    'color_keys', # what colors should be used
    'suffix', # model name suffix
    'rotation',  # rotation if required
])

all_params_rect_th_cap = {# Aluminum TH capacitors
}

kicad_naming_params_rect_th_cap = {
    "C_Rect_L13.0mm_W3.0mm_P10.00mm_FKS3_FKP3_MKS4" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.00, # Body Length
        W = 3.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L13.0mm_W4.0mm_P10.00mm_FKS3_FKP3_MKS4" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.00, # Body Length
        W = 4.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L13.5mm_W4.0mm_P10.00mm_FKS3_FKP3_MKS4" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.50, # Body Length
        W = 4.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L13.0mm_W5.0mm_P10.00mm_FKS3_FKP3_MKS4" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.00, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L13.5mm_W5.0mm_P10.00mm_FKS3_FKP3_MKS4" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.50, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L13.0mm_W6.0mm_P10.00mm_FKS3_FKP3_MKS4" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.00, # Body Length
        W = 6.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L13.0mm_W8.0mm_P10.00mm_FKS3_FKP3_MKS4" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.00, # Body Length
        W = 8.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.0mm_W3.0mm_P7.50mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 8.50, # Body Height
        L = 10.00, # Body Length
        W = 3.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.0mm_W4.0mm_P7.50mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 8.50, # Body Height
        L = 10.00, # Body Length
        W = 4.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L18.0mm_W5.0mm_P15.00mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 18.00, # Body Length
        W = 5.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L18.0mm_W6.0mm_P15.00mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 18.00, # Body Length
        W = 6.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L18.0mm_W7.0mm_P15.00mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 18.00, # Body Length
        W = 7.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L18.0mm_W8.0mm_P15.00mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 18.00, # Body Length
        W = 8.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L18.0mm_W9.0mm_P15.00mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 18.00, # Body Length
        W = 9.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L18.0mm_W11.0mm_P15.00mm_FKS3_FKP3" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 18.00, # Body Length
        W = 11.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS3_FKP3', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L19.0mm_W5.0mm_P15.00mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 19.00, # Body Length
        W = 5.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L19.0mm_W6.0mm_P15.00mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 19.00, # Body Length
        W = 6.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L19.0mm_W7.0mm_P15.00mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 19.00, # Body Length
        W = 7.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L19.0mm_W8.0mm_P15.00mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 19.00, # Body Length
        W = 8.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L19.0mm_W9.0mm_P15.00mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 19.00, # Body Length
        W = 9.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L19.0mm_W11.0mm_P15.00mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 19.00, # Body Length
        W = 11.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L26.5mm_W5.0mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 26.50, # Body Length
        W = 5.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L26.5mm_W6.0mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 26.50, # Body Length
        W = 6.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L26.5mm_W7.0mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 26.50, # Body Length
        W = 7.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L26.5mm_W8.5mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 26.50, # Body Length
        W = 8.50, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L26.5mm_W10.5mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 26.50, # Body Length
        W = 10.50, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L26.5mm_W11.5mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 26.50, # Body Length
        W = 11.50, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L28.0mm_W8.0mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 28.00, # Body Length
        W = 8.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L28.0mm_W10.0mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 28.00, # Body Length
        W = 10.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L28.0mm_W12.0mm_P22.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 28.00, # Body Length
        W = 12.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L31.5mm_W9.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 31.50, # Body Length
        W = 9.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L31.5mm_W11.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 31.50, # Body Length
        W = 11.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L31.5mm_W13.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 31.50, # Body Length
        W = 13.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L31.5mm_W15.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 31.50, # Body Length
        W = 15.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L31.5mm_W17.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 31.50, # Body Length
        W = 17.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L31.5mm_W20.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 31.50, # Body Length
        W = 20.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L33.0mm_W13.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 33.00, # Body Length
        W = 13.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L33.0mm_W15.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 33.00, # Body Length
        W = 15.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L33.0mm_W20.0mm_P27.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 33.00, # Body Length
        W = 20.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W9.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 9.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W11.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 11.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W13.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 13.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W15.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 15.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W17.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 17.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W19.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 19.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W20.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 20.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W24.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 24.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W31.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 31.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W35.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 35.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L41.5mm_W40.0mm_P37.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 44.00, # Body Height
        L = 41.50, # Body Length
        W = 40.00, # Body Width
        d = 1.10, # Lead Diameter
        F = 37.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L27.0mm_W9.0mm_P22.00mm" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 27.00, # Body Length
        W = 9.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 22.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L27.0mm_W9.0mm_P23.00mm" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 27.00, # Body Length
        W = 9.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 23.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L27.0mm_W11.0mm_P22.00mm" : Params(# from Jan Kriege's 3d models
        H = 21.00, # Body Height
        L = 27.00, # Body Length
        W = 11.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 22.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L32.0mm_W15.0mm_P27.00mm" : Params(# from Jan Kriege's 3d models
        H = 26.00, # Body Height
        L = 32.00, # Body Length
        W = 15.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 27.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L4.0mm_W2.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 4.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.5mm_W6.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.50, # Body Length
        W = 6.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W2.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 2.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W2.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W3.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 3.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W4.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 4.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W6.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 6.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W6.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 6.50, # Body Width
        d = 0.60, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L4.6mm_W5.5mm_P2.50mm_MKS02_FKP02" : Params(# from Jan Kriege's 3d models
        H = 7.00, # Body Height
        L = 4.60, # Body Length
        W = 5.50, # Body Width
        d = 0.40, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS02_FKP02', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L4.6mm_W4.6mm_P2.50mm_MKS02_FKP02" : Params(# from Jan Kriege's 3d models
        H = 7.00, # Body Height
        L = 4.60, # Body Length
        W = 4.60, # Body Width
        d = 0.40, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS02_FKP02', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L4.6mm_W3.8mm_P2.50mm_MKS02_FKP02" : Params(# from Jan Kriege's 3d models
        H = 7.00, # Body Height
        L = 4.60, # Body Length
        W = 3.80, # Body Width
        d = 0.40, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS02_FKP02', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L4.6mm_W3.0mm_P2.50mm_MKS02_FKP02" : Params(# from Jan Kriege's 3d models
        H = 7.00, # Body Height
        L = 4.60, # Body Length
        W = 3.00, # Body Width
        d = 0.40, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS02_FKP02', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L4.6mm_W2.0mm_P2.50mm_MKS02_FKP02" : Params(# from Jan Kriege's 3d models
        H = 7.00, # Body Height
        L = 4.60, # Body Length
        W = 2.00, # Body Width
        d = 0.40, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS02_FKP02', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W2.5mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W3.0mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 3.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W3.5mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 3.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W4.5mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 4.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W5.5mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 5.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W7.2mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 7.20, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W8.5mm_P5.00mm_FKP2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 8.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKP2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W11.0mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 11.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.2mm_W2.5mm_P5.00mm_FKS2_FKP2_MKS2_MKP2" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 7.20, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_FKS2_FKP2_MKS2_MKP2', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.0mm_W2.5mm_P7.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 10.00, # Body Length
        W = 2.50, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.0mm_W3.0mm_P7.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 10.00, # Body Length
        W = 3.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.0mm_W4.0mm_P7.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 10.00, # Body Length
        W = 4.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.3mm_W4.5mm_P7.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 10.30, # Body Length
        W = 4.50, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.3mm_W5.0mm_P7.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 10.30, # Body Length
        W = 5.00, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.3mm_W5.7mm_P7.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 10.30, # Body Length
        W = 5.70, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.3mm_W7.2mm_P7.50mm_MKS4" : Params(# from Jan Kriege's 3d models
        H = 9.00, # Body Height
        L = 10.30, # Body Length
        W = 7.20, # Body Width
        d = 0.70, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '_MKS4', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W2.5mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 2.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W2.6mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 2.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W2.7mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 2.70, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W3.2mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 3.20, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W3.3mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 3.30, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W3.4mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 3.40, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W3.6mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 3.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W3.8mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 3.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W3.9mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 3.90, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W4.0mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 4.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W4.2mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 4.20, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W4.9mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 4.90, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W5.1mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 5.10, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W5.7mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 5.70, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W6.4mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 6.40, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W6.7mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 6.70, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W7.7mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 7.70, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W8.5mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 8.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W9.5mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 9.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L9.0mm_W9.8mm_P7.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 8.00, # Body Height
        L = 9.00, # Body Length
        W = 9.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W2.8mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 2.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W3.4mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 3.40, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W3.5mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 3.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W4.2mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 4.20, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W4.3mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 4.30, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W5.1mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 5.10, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W5.3mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 5.30, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W6.3mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 6.30, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W6.4mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 6.40, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W7.3mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 7.30, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.0mm_W8.8mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.00, # Body Length
        W = 8.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W2.0mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 2.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W5.0mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 5.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W2.6mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 2.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W2.8mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 2.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W3.2mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 3.20, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W3.5mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 3.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W3.6mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 3.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W4.0mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 4.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W4.3mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 4.30, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W4.5mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 4.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W5.1mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 5.10, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W5.2mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 5.20, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W5.6mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 5.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W6.4mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 6.40, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W6.6mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 6.60, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W6.9mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 6.90, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W7.3mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 7.30, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W7.5mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 7.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W7.8mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 7.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W8.0mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 8.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W8.8mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 8.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W9.5mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 9.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L11.5mm_W9.8mm_P10.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 11.50, # Body Length
        W = 9.80, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W4.7mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 4.70, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W4.9mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 4.90, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W5.0mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 5.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W6.0mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 6.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W7.0mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 7.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W7.3mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 7.30, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W8.7mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 8.70, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W8.9mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 8.90, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W9.0mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 9.00, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W9.2mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 9.20, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W10.7mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 10.70, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W10.9mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 10.90, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W11.2mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 11.20, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W11.8mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 11.80, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W13.5mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 13.50, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W13.7mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 13.70, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L16.5mm_W13.9mm_P15.00mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 14.00, # Body Height
        L = 16.50, # Body Length
        W = 13.90, # Body Width
        d = 0.80, # Lead Diameter
        F = 15.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W7.0mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 7.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W8.3mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 8.30, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W8.6mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 8.60, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W10.1mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 10.10, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W10.3mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 10.30, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W10.9mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 10.90, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W12.2mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 12.20, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W12.6mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 12.60, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L24.0mm_W12.8mm_P22.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 15.00, # Body Height
        L = 24.00, # Body Length
        W = 12.80, # Body Width
        d = 0.90, # Lead Diameter
        F = 22.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W7.6mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 7.60, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W7.8mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 7.80, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W7.9mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 7.90, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W9.1mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 9.10, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W9.6mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 9.60, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W11.0mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 11.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W11.9mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 11.90, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W12.2mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 12.20, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W13.0mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 13.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W13.8mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 13.80, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W14.2mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 14.20, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L29.0mm_W16.0mm_P27.50mm_MKT" : Params(# from Jan Kriege's 3d models
        H = 19.00, # Body Height
        L = 29.00, # Body Length
        W = 16.00, # Body Width
        d = 0.90, # Lead Diameter
        F = 27.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKT', # 'MKS' or 'MKT'
        color_keys = color_keys_mkt,
        suffix = '_MKT', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L7.0mm_W3.5mm_P2.50mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 7.00, # Body Length
        W = 3.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L10.0mm_W5.0mm_P5.00mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 10.00, # Body Length
        W = 5.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 7.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),

    "C_Rect_L13.0mm_W6.5mm_P7.50mm_P10.00mm" : Params(# from Jan Kriege's 3d models
        H = 10.00, # Body Height
        L = 13.00, # Body Length
        W = 6.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 10.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.0, # Board Seperation
        series = 'MKS', # 'MKS' or 'MKT'
        color_keys = color_keys_mks,
        suffix = '', # Modelname
        rotation = 0, # Rotation
    ),
}

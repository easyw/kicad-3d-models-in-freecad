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

import collections
from collections import namedtuple

destination_dir="/Package_DIP.3dshapes"
# destination_dir="./"
old_footprints_dir="Housings_DIP.pretty"
footprints_dir="Package_DIP.pretty"
##footprints_dir=None #to exclude importing of footprints

##enabling optional/default values to None
def namedtuple_with_defaults(typename, field_names, default_values=()):

    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


Params =namedtuple_with_defaults ("Params", [
    'D',            # package length
    'E1',           # package width
    'E',            # package shoulder-to-shoulder width
    'A1',           # package board seperation
    'A2',           # package height

    'b1',           # pin width
    'b',            # pin tip width
    'e',            # pin center to center distance (pitch)

    'npins',        # number of pins
    'modelName',    #modelName
    'rotation',     #rotation if required
    'type',         # THT and/or SMD
    'corner',       # Chamfer or corner
    'excludepins'   # Which pins should be excluded
])

all_params = {
    'DIP-8_W7.62mm': Params(
    #
    #
    #
    D  = 9.27,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 8,  # number of pins
    modelName   = 'DIP-8_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-4_W7.62mm': Params(
    #
    #
    #
    D  = 4.93,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 4,  # number of pins
    modelName   = 'DIP-4_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-4_W10.16mm': Params(
    #
    #
    #
    D  = 4.93,  # package length
    E1 = 6.35,  # package width
    E  = 10.41,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 4,  # number of pins
    modelName   = 'DIP-4_W10.16mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'chamfer',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-5-6_W7.62mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'DIP-5-6_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [5],  # pins to exclude
    ),

    'DIP-5-6_W10.16mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 6.35,  # package width
    E  = 10.41,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'DIP-5-6_W10.16mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'chamfer',  # Chamfer or corner
    excludepins = [5],  # pins to exclude
    ),

    'DIP-6_W7.62mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'DIP-6_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-6_W10.16mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 6.35,  # package width
    E  = 10.41,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'DIP-6_W10.16mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'chamfer',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-8_W10.16mm': Params(
    #
    #
    #
    D  = 9.27,  # package length
    E1 = 6.35,  # package width
    E  = 10.41,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 8,  # number of pins
    modelName   = 'DIP-8_W10.16mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'chamfer',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-14_W7.62mm': Params(
    #
    #
    #
    D  = 19.05,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 14,  # number of pins
    modelName   = 'DIP-14_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-16_W7.62mm': Params(
    #
    #
    #
    D  = 19.18,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 16,  # number of pins
    modelName   = 'DIP-16_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-18_W7.62mm': Params(
    #
    #
    #
    D  = 22.86,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 18,  # number of pins
    modelName   = 'DIP-18_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-20_W7.62mm': Params(
    #
    #
    #
    D  = 26.16,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 20,  # number of pins
    modelName   = 'DIP-20_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-22_W7.62mm': Params(
    #
    #
    #
    D  = 27.94,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 22,  # number of pins
    modelName   = 'DIP-22_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-24_W7.62mm': Params(
    #
    #
    #
    D  = 31.75,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 24,  # number of pins
    modelName   = 'DIP-24_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-22_W10.16mm': Params(
    #
    #
    #
    D  = 27.94,  # package length
    E1 = 9.17,  # package width
    E  = 10.41,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 22,  # number of pins
    modelName   = 'DIP-22_W10.16mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-24_W10.16mm': Params(
    #
    #
    #
    D  = 31.75,  # package length
    E1 = 9.17,  # package width
    E  = 10.41,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 24,  # number of pins
    modelName   = 'DIP-24_W10.16mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-28_W7.62mm': Params(
    #
    #
    #
    D  = 35.56,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 28,  # number of pins
    modelName   = 'DIP-28_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-24_W15.24mm': Params(
    #
    #
    #
    D  = 31.75,  # package length
    E1 = 13.46,  # package width
    E  = 15.49,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 24,  # number of pins
    modelName   = 'DIP-24_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-28_W15.24mm': Params(
    #
    #
    #
    D  = 35.56,  # package length
    E1 = 13.46,  # package width
    E  = 15.49,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 28,  # number of pins
    modelName   = 'DIP-28_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-32_W7.62mm': Params(
    #
    #
    #
    D  = 41.4,  # package length
    E1 = 6.35,  # package width
    E  = 7.87,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 32,  # number of pins
    modelName   = 'DIP-32_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-32_W15.24mm': Params(
    #
    #
    #
    D  = 41.4,  # package length
    E1 = 13.46,  # package width
    E  = 15.49,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 32,  # number of pins
    modelName   = 'DIP-32_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-40_W15.24mm': Params(
    #
    #
    #
    D  = 50.8,  # package length
    E1 = 13.46,  # package width
    E  = 15.49,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 40,  # number of pins
    modelName   = 'DIP-40_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-48_W15.24mm': Params(
    #
    #
    #
    D  = 61.47,  # package length
    E1 = 13.46,  # package width
    E  = 15.49,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 48,  # number of pins
    modelName   = 'DIP-48_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-64_W15.24mm': Params(
    #
    #
    #
    D  = 82.8,  # package length
    E1 = 13.46,  # package width
    E  = 15.49,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 64,  # number of pins
    modelName   = 'DIP-64_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-64_W22.86mm': Params(
    #
    #
    #
    D  = 57.66,  # package length
    E1 = 17.02,  # package width
    E  = 19.3,  # package shoulder-to-shoulder width
    A1 = 0.51,  # package board seperation
    A2 = 3.81,  # package height
    b1 = 1.02,  # pin width
    b  = 0.46,  # pin tip width
    e  = 1.78,  # pin center to center distance (pitch)
    npins       = 64,  # number of pins
    modelName   = 'DIP-64_W22.86mm',  # modelName
    rotation    = 0,  # rotation if required
    type        = 'tht',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-4_W7.62mm': Params(
    #
    #
    #
    D  = 4.93,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 4,  # number of pins
    modelName   = 'SMDIP-4_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-4_W9.53mm': Params(
    #
    #
    #
    D  = 4.93,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 4,  # number of pins
    modelName   = 'SMDIP-4_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-4_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 4.93,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 4,  # number of pins
    modelName   = 'SMDIP-4_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-4_W11.48mm': Params(
    #
    #
    #
    D  = 4.93,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 4,  # number of pins
    modelName   = 'SMDIP-4_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-6_W7.62mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'SMDIP-6_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-6_W9.53mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'SMDIP-6_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-6_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'SMDIP-6_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-6_W11.48mm': Params(
    #
    #
    #
    D  = 7.05,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 6,  # number of pins
    modelName   = 'SMDIP-6_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-8_W7.62mm': Params(
    #
    #
    #
    D  = 9.27,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 8,  # number of pins
    modelName   = 'SMDIP-8_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-8_W9.53mm': Params(
    #
    #
    #
    D  = 9.27,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 8,  # number of pins
    modelName   = 'SMDIP-8_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-8_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 9.27,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 8,  # number of pins
    modelName   = 'SMDIP-8_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-8_W11.48mm': Params(
    #
    #
    #
    D  = 9.27,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 8,  # number of pins
    modelName   = 'SMDIP-8_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-10_W7.62mm': Params(
    #
    #
    #
    D  = 12.25,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 10,  # number of pins
    modelName   = 'SMDIP-10_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-10_W9.53mm': Params(
    #
    #
    #
    D  = 12.25,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 10,  # number of pins
    modelName   = 'SMDIP-10_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-10_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 12.25,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 10,  # number of pins
    modelName   = 'SMDIP-10_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-10_W11.48mm': Params(
    #
    #
    #
    D  = 12.25,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 10,  # number of pins
    modelName   = 'SMDIP-10_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-12_W7.62mm': Params(
    #
    #
    #
    D  = 15.24,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 12,  # number of pins
    modelName   = 'SMDIP-12_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-12_W9.53mm': Params(
    #
    #
    #
    D  = 15.24,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 12,  # number of pins
    modelName   = 'SMDIP-12_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-12_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 15.24,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 12,  # number of pins
    modelName   = 'SMDIP-12_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-12_W11.48mm': Params(
    #
    #
    #
    D  = 15.24,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 12,  # number of pins
    modelName   = 'SMDIP-12_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-14_W7.62mm': Params(
    #
    #
    #
    D  = 19.05,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 14,  # number of pins
    modelName   = 'SMDIP-14_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-14_W9.53mm': Params(
    #
    #
    #
    D  = 19.05,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 14,  # number of pins
    modelName   = 'SMDIP-14_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-14_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 19.05,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 14,  # number of pins
    modelName   = 'SMDIP-14_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-14_W11.48mm': Params(
    #
    #
    #
    D  = 19.05,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 14,  # number of pins
    modelName   = 'SMDIP-14_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-16_W7.62mm': Params(
    #
    #
    #
    D  = 19.18,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 16,  # number of pins
    modelName   = 'SMDIP-16_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-16_W9.53mm': Params(
    #
    #
    #
    D  = 19.18,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 16,  # number of pins
    modelName   = 'SMDIP-16_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-16_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 19.18,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 16,  # number of pins
    modelName   = 'SMDIP-16_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-16_W11.48mm': Params(
    #
    #
    #
    D  = 19.18,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 16,  # number of pins
    modelName   = 'SMDIP-16_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-18_W7.62mm': Params(
    #
    #
    #
    D  = 22.86,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 18,  # number of pins
    modelName   = 'SMDIP-18_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-18_W9.53mm': Params(
    #
    #
    #
    D  = 22.86,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 18,  # number of pins
    modelName   = 'SMDIP-18_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-18_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 22.86,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 18,  # number of pins
    modelName   = 'SMDIP-18_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-18_W11.48mm': Params(
    #
    #
    #
    D  = 22.86,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 18,  # number of pins
    modelName   = 'SMDIP-18_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-20_W7.62mm': Params(
    #
    #
    #
    D  = 26.16,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 20,  # number of pins
    modelName   = 'SMDIP-20_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-20_W9.53mm': Params(
    #
    #
    #
    D  = 26.16,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 20,  # number of pins
    modelName   = 'SMDIP-20_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-20_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 26.16,  # package length
    E1 = 8.4,  # package width
    E  = 9.25,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 20,  # number of pins
    modelName   = 'SMDIP-20_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-20_W11.48mm': Params(
    #
    #
    #
    D  = 26.16,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 20,  # number of pins
    modelName   = 'SMDIP-20_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-22_W7.62mm': Params(
    #
    #
    #
    D  = 27.94,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 22,  # number of pins
    modelName   = 'SMDIP-22_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-22_W9.53mm': Params(
    #
    #
    #
    D  = 27.94,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 22,  # number of pins
    modelName   = 'SMDIP-22_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-22_W9.53mm_Clearance8mm': Params(
    #
    #
    #
    D  = 27.94,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 22,  # number of pins
    modelName   = 'SMDIP-22_W9.53mm_Clearance8mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-22_W11.48mm': Params(
    #
    #
    #
    D  = 27.94,  # package length
    E1 = 7.0,  # package width
    E  = 10.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 22,  # number of pins
    modelName   = 'SMDIP-22_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-24_W7.62mm': Params(
    #
    #
    #
    D  = 31.75,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 24,  # number of pins
    modelName   = 'SMDIP-24_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-24_W9.53mm': Params(
    #
    #
    #
    D  = 31.75,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 24,  # number of pins
    modelName   = 'SMDIP-24_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-24_W11.48mm': Params(
    #
    #
    #
    D  = 31.75,  # package length
    E1 = 8.8,  # package width
    E  = 10.4,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 24,  # number of pins
    modelName   = 'SMDIP-24_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-24_W15.24mm': Params(
    #
    #
    #
    D  = 31.75,  # package length
    E1 = 13.0,  # package width
    E  = 14.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 24,  # number of pins
    modelName   = 'SMDIP-24_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-28_W15.24mm': Params(
    #
    #
    #
    D  = 35.56,  # package length
    E1 = 13.0,  # package width
    E  = 14.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 28,  # number of pins
    modelName   = 'SMDIP-28_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-32_W7.62mm': Params(
    #
    #
    #
    D  = 41.4,  # package length
    E1 = 5.5,  # package width
    E  = 7.5,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 32,  # number of pins
    modelName   = 'SMDIP-32_W7.62mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-32_W9.53mm': Params(
    #
    #
    #
    D  = 41.4,  # package length
    E1 = 7.0,  # package width
    E  = 8.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 32,  # number of pins
    modelName   = 'SMDIP-32_W9.53mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-32_W11.48mm': Params(
    #
    #
    #
    D  = 41.4,  # package length
    E1 = 8.8,  # package width
    E  = 10.4,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 32,  # number of pins
    modelName   = 'SMDIP-32_W11.48mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-32_W15.24mm': Params(
    #
    #
    #
    D  = 41.4,  # package length
    E1 = 13.0,  # package width
    E  = 14.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 32,  # number of pins
    modelName   = 'SMDIP-32_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-40_W15.24mm': Params(
    #
    #
    #
    D  = 50.8,  # package length
    E1 = 13.0,  # package width
    E  = 14.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 40,  # number of pins
    modelName   = 'SMDIP-40_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-40_W25.24mm': Params(
    #
    #
    #
    D  = 50.8,  # package length
    E1 = 23.0,  # package width
    E  = 24.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 40,  # number of pins
    modelName   = 'SMDIP-40_W25.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-42_W15.24mm': Params(
    #
    #
    #
    D  = 53.34,  # package length
    E1 = 13.0,  # package width
    E  = 14.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 42,  # number of pins
    modelName   = 'SMDIP-42_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-48_W15.24mm': Params(
    #
    #
    #
    D  = 61.47,  # package length
    E1 = 13.0,  # package width
    E  = 14.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 48,  # number of pins
    modelName   = 'SMDIP-48_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'SMDIP-64_W15.24mm': Params(
    #
    #
    #
    D  = 82.8,  # package length
    E1 = 13.0,  # package width
    E  = 14.0,  # package shoulder-to-shoulder width
    A1 = 0.38,  # package board seperation
    A2 = 3.3,  # package height
    b1 = 1.52,  # pin width
    b  = 0.46,  # pin tip width
    e  = 2.54,  # pin center to center distance (pitch)
    npins       = 64,  # number of pins
    modelName   = 'SMDIP-64_W15.24mm',  # modelName
    rotation    = 90,  # rotation if required
    type        = 'smd',  # THT and/or SMD
    corner      = 'fillet',  # Chamfer or corner
    excludepins = [0],  # pins to exclude
    ),

    'DIP-10_W10.16mm': Params(
        #
        # 10-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-10_W10.16mm.kicad_mod
        # 
        D  = 12.7,         # body length
        E1 = 8.26,         # body width
        E = 10.16,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 10,          # number of pins
        modelName = 'DIP-10_W10.16mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-10_W7.62mm': Params(
        #
        # 10-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-10_W7.62mm.kicad_mod
        # 
        D  = 12.7,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 10,          # number of pins
        modelName = 'DIP-10_W7.62mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-10_W7.62mm_SMDSocket': Params(
        #
        # 10-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-10_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 12.82,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 10,          # number of pins
        modelName = 'DIP-10_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-10_W8.89mm_SMDSocket': Params(
        #
        # 10-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-10_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 12.82,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 10,          # number of pins
        modelName = 'DIP-10_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-12_W10.16mm': Params(
        #
        # 12-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-12_W10.16mm.kicad_mod
        # 
        D  = 15.24,         # body length
        E1 = 8.26,         # body width
        E = 10.16,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 12,          # number of pins
        modelName = 'DIP-12_W10.16mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-12_W7.62mm': Params(
        #
        # 12-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-12_W7.62mm.kicad_mod
        # 
        D  = 15.24,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 12,          # number of pins
        modelName = 'DIP-12_W7.62mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-12_W7.62mm_SMDSocket': Params(
        #
        # 12-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-12_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 15.36,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 12,          # number of pins
        modelName = 'DIP-12_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-12_W8.89mm_SMDSocket': Params(
        #
        # 12-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-12_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 15.36,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 12,          # number of pins
        modelName = 'DIP-12_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-14_W10.16mm': Params(
        #
        # 14-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-14_W10.16mm.kicad_mod
        # 
        D  = 17.78,         # body length
        E1 = 8.26,         # body width
        E = 10.16,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 14,          # number of pins
        modelName = 'DIP-14_W10.16mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-14_W7.62mm_SMDSocket': Params(
        #
        # 14-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-14_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 17.9,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 14,          # number of pins
        modelName = 'DIP-14_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-14_W8.89mm_SMDSocket': Params(
        #
        # 14-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-14_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 17.9,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 14,          # number of pins
        modelName = 'DIP-14_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-16_W10.16mm': Params(
        #
        # 16-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-16_W10.16mm.kicad_mod
        # 
        D  = 20.32,         # body length
        E1 = 8.26,         # body width
        E = 10.16,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 16,          # number of pins
        modelName = 'DIP-16_W10.16mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-16_W7.62mm_SMDSocket': Params(
        #
        # 16-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-16_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 20.44,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 16,          # number of pins
        modelName = 'DIP-16_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-16_W8.89mm_SMDSocket': Params(
        #
        # 16-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-16_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 20.44,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 16,          # number of pins
        modelName = 'DIP-16_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-18_W7.62mm_SMDSocket': Params(
        #
        # 18-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-18_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 22.98,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 18,          # number of pins
        modelName = 'DIP-18_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-18_W8.89mm_SMDSocket': Params(
        #
        # 18-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-18_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 22.98,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 18,          # number of pins
        modelName = 'DIP-18_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-20_W7.62mm_SMDSocket': Params(
        #
        # 20-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-20_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 25.52,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 20,          # number of pins
        modelName = 'DIP-20_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-20_W8.89mm_SMDSocket': Params(
        #
        # 20-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-20_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 25.52,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 20,          # number of pins
        modelName = 'DIP-20_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-22_W10.16mm_SMDSocket': Params(
        #
        # 22-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-22_W10.16mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 28.06,         # body length
        E1 = 8.66,         # body width
        E = 10.16,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 22,          # number of pins
        modelName = 'DIP-22_W10.16mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-22_W11.43mm_SMDSocket': Params(
        #
        # 22-lead though-hole mounted DIP package, row spacing 11.43 mm (450 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-22_W11.43mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 28.06,         # body length
        E1 = 9.93,         # body width
        E = 11.43,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 22,          # number of pins
        modelName = 'DIP-22_W11.43mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-22_W7.62mm_SMDSocket': Params(
        #
        # 22-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-22_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 28.06,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 22,          # number of pins
        modelName = 'DIP-22_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-22_W8.89mm_SMDSocket': Params(
        #
        # 22-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-22_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 28.06,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 22,          # number of pins
        modelName = 'DIP-22_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-24_W10.16mm_SMDSocket': Params(
        #
        # 24-lead though-hole mounted DIP package, row spacing 10.16 mm (400 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-24_W10.16mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 30.6,         # body length
        E1 = 8.66,         # body width
        E = 10.16,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 24,          # number of pins
        modelName = 'DIP-24_W10.16mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-24_W11.43mm_SMDSocket': Params(
        #
        # 24-lead though-hole mounted DIP package, row spacing 11.43 mm (450 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-24_W11.43mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 30.6,         # body length
        E1 = 9.93,         # body width
        E = 11.43,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 24,          # number of pins
        modelName = 'DIP-24_W11.43mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-24_W15.24mm': Params(
        #
        # 24-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-24_W15.24mm.kicad_mod
        # 
        D  = 30.48,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 24,          # number of pins
        modelName = 'DIP-24_W15.24mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-24_W15.24mm_SMDSocket': Params(
        #
        # 24-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-24_W15.24mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 30.6,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 24,          # number of pins
        modelName = 'DIP-24_W15.24mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-24_W16.51mm_SMDSocket': Params(
        #
        # 24-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-24_W16.51mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 30.6,         # body length
        E1 = 15.01,         # body width
        E = 16.51,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 24,          # number of pins
        modelName = 'DIP-24_W16.51mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-24_W7.62mm_SMDSocket': Params(
        #
        # 24-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-24_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 30.6,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 24,          # number of pins
        modelName = 'DIP-24_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-24_W8.89mm_SMDSocket': Params(
        #
        # 24-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-24_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 30.6,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 24,          # number of pins
        modelName = 'DIP-24_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-28_W15.24mm_SMDSocket': Params(
        #
        # 28-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-28_W15.24mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 35.68,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 28,          # number of pins
        modelName = 'DIP-28_W15.24mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-28_W16.51mm_SMDSocket': Params(
        #
        # 28-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-28_W16.51mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 35.68,         # body length
        E1 = 15.01,         # body width
        E = 16.51,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 28,          # number of pins
        modelName = 'DIP-28_W16.51mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-28_W7.62mm_SMDSocket': Params(
        #
        # 28-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-28_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 35.68,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 28,          # number of pins
        modelName = 'DIP-28_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-28_W8.89mm_SMDSocket': Params(
        #
        # 28-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-28_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 35.68,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 28,          # number of pins
        modelName = 'DIP-28_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-32_W15.24mm_SMDSocket': Params(
        #
        # 32-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-32_W15.24mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 40.76,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 32,          # number of pins
        modelName = 'DIP-32_W15.24mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-32_W16.51mm_SMDSocket': Params(
        #
        # 32-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-32_W16.51mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 40.76,         # body length
        E1 = 15.01,         # body width
        E = 16.51,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 32,          # number of pins
        modelName = 'DIP-32_W16.51mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-40_W15.24mm_SMDSocket': Params(
        #
        # 40-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-40_W15.24mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 50.92,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 40,          # number of pins
        modelName = 'DIP-40_W15.24mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-40_W16.51mm_SMDSocket': Params(
        #
        # 40-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-40_W16.51mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 50.92,         # body length
        E1 = 15.01,         # body width
        E = 16.51,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 40,          # number of pins
        modelName = 'DIP-40_W16.51mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-40_W25.4mm': Params(
        #
        # 40-lead though-hole mounted DIP package, row spacing 25.4 mm (1000 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-40_W25.4mm.kicad_mod
        # 
        D  = 50.8,         # body length
        E1 = 23.9,         # body width
        E = 25.4,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 40,          # number of pins
        modelName = 'DIP-40_W25.4mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-40_W25.4mm_SMDSocket': Params(
        #
        # 40-lead though-hole mounted DIP package, row spacing 25.4 mm (1000 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-40_W25.4mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 50.92,         # body length
        E1 = 23.9,         # body width
        E = 25.4,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 40,          # number of pins
        modelName = 'DIP-40_W25.4mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-40_W25.4mm_Socket': Params(
        #
        # 40-lead though-hole mounted DIP package, row spacing 25.4 mm (1000 mils), Socket
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-40_W25.4mm_Socket.kicad_mod
        # 
        D  = 50.92,         # body length
        E1 = 23.9,         # body width
        E = 25.4,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 40,          # number of pins
        modelName = 'DIP-40_W25.4mm_Socket',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-40_W26.67mm_SMDSocket': Params(
        #
        # 40-lead though-hole mounted DIP package, row spacing 26.67 mm (1050 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-40_W26.67mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 50.92,         # body length
        E1 = 25.17,         # body width
        E = 26.67,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 40,          # number of pins
        modelName = 'DIP-40_W26.67mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-42_W15.24mm': Params(
        #
        # 42-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-42_W15.24mm.kicad_mod
        # 
        D  = 53.34,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 42,          # number of pins
        modelName = 'DIP-42_W15.24mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-42_W15.24mm_SMDSocket': Params(
        #
        # 42-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-42_W15.24mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 53.46,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 42,          # number of pins
        modelName = 'DIP-42_W15.24mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-42_W15.24mm_Socket': Params(
        #
        # 42-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), Socket
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-42_W15.24mm_Socket.kicad_mod
        # 
        D  = 53.46,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 42,          # number of pins
        modelName = 'DIP-42_W15.24mm_Socket',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-42_W16.51mm_SMDSocket': Params(
        #
        # 42-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-42_W16.51mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 53.46,         # body length
        E1 = 15.01,         # body width
        E = 16.51,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 42,          # number of pins
        modelName = 'DIP-42_W16.51mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-48_W15.24mm_SMDSocket': Params(
        #
        # 48-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-48_W15.24mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 61.08,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 48,          # number of pins
        modelName = 'DIP-48_W15.24mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-48_W16.51mm_SMDSocket': Params(
        #
        # 48-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-48_W16.51mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 61.08,         # body length
        E1 = 15.01,         # body width
        E = 16.51,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 48,          # number of pins
        modelName = 'DIP-48_W16.51mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-4_W7.62mm_SMDSocket': Params(
        #
        # 4-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-4_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 5.2,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 4,          # number of pins
        modelName = 'DIP-4_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-4_W8.89mm_SMDSocket': Params(
        #
        # 4-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-4_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 5.2,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 4,          # number of pins
        modelName = 'DIP-4_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-5-6_W7.62mm_SMDSocket': Params(
        #
        # 5-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-5-6_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 7.74,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 6,          # number of pins
        modelName = 'DIP-5-6_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [5],          # pin excluded
        ),

    'DIP-5-6_W7.62mm_Socket': Params(
        #
        # 5-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), Socket
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-5-6_W7.62mm_Socket.kicad_mod
        # 
        D  = 7.74,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 6,          # number of pins
        modelName = 'DIP-5-6_W7.62mm_Socket',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [5],          # pin excluded
        ),

    'DIP-5-6_W8.89mm_SMDSocket': Params(
        #
        # 5-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-5-6_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 7.74,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 6,          # number of pins
        modelName = 'DIP-5-6_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [5],          # pin excluded
        ),

    'DIP-64_W15.24mm_SMDSocket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W15.24mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 13.74,         # body width
        E = 15.24,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W15.24mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W16.51mm_SMDSocket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 16.51 mm (650 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W16.51mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 15.01,         # body width
        E = 16.51,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W16.51mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W22.86mm': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 22.86 mm (900 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W22.86mm.kicad_mod
        # 
        D  = 81.28,         # body length
        E1 = 21.36,         # body width
        E = 22.86,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W22.86mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W22.86mm_SMDSocket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 22.86 mm (900 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W22.86mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 21.36,         # body width
        E = 22.86,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W22.86mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W22.86mm_Socket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 22.86 mm (900 mils), Socket
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W22.86mm_Socket.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 21.36,         # body width
        E = 22.86,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W22.86mm_Socket',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W24.13mm_SMDSocket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 24.13 mm (950 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W24.13mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 22.63,         # body width
        E = 24.13,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W24.13mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W25.4mm': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 25.4 mm (1000 mils)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W25.4mm.kicad_mod
        # 
        D  = 81.28,         # body length
        E1 = 23.9,         # body width
        E = 25.4,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W25.4mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W25.4mm_SMDSocket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 25.4 mm (1000 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W25.4mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 23.9,         # body width
        E = 25.4,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W25.4mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W25.4mm_Socket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 25.4 mm (1000 mils), Socket
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W25.4mm_Socket.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 23.9,         # body width
        E = 25.4,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W25.4mm_Socket',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-64_W26.67mm_SMDSocket': Params(
        #
        # 64-lead though-hole mounted DIP package, row spacing 26.67 mm (1050 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-64_W26.67mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 81.4,         # body length
        E1 = 25.17,         # body width
        E = 26.67,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 64,          # number of pins
        modelName = 'DIP-64_W26.67mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-6_W7.62mm_SMDSocket': Params(
        #
        # 6-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-6_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 7.74,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 6,          # number of pins
        modelName = 'DIP-6_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-6_W8.89mm_SMDSocket': Params(
        #
        # 6-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-6_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 7.74,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 6,          # number of pins
        modelName = 'DIP-6_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-8-N6_W7.62mm': Params(
        #
        # 8-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), missing pin 6
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-8-N6_W7.62mm.kicad_mod
        # 
        D  = 10.16,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'DIP-8-N6_W7.62mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [6],          # pin excluded
        ),

    'DIP-8-N7_W7.62mm': Params(
        #
        # 8-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), missing pin 7
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-8-N7_W7.62mm.kicad_mod
        # 
        D  = 10.16,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'DIP-8-N7_W7.62mm',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [7],          # pin excluded
        ),

    'DIP-8_W7.62mm_SMDSocket': Params(
        #
        # 8-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), SMDSocket, SmallPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-8_W7.62mm_SMDSocket_SmallPads.kicad_mod
        # 
        D  = 10.28,         # body length
        E1 = 6.12,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'DIP-8_W7.62mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'DIP-8_W8.89mm_SMDSocket': Params(
        #
        # 8-lead though-hole mounted DIP package, row spacing 8.89 mm (350 mils), SMDSocket, LongPads
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is DIP-8_W8.89mm_SMDSocket_LongPads.kicad_mod
        # 
        D  = 10.28,         # body length
        E1 = 7.39,         # body width
        E = 8.89,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'DIP-8_W8.89mm_SMDSocket',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'PowerIntegrations_PDIP-8B': Params(
        #
        # Power Integrations variant of 8-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), LongPads, see https://www.power.com/sites/default/files/product-docs/lnk520.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_PDIP-8B.kicad_mod
        # 
        D  = 10.28,         # body length
        E1 = 4.5,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'PowerIntegrations_PDIP-8B',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [6],          # pin excluded
        ),

    'PowerIntegrations_PDIP-8C': Params(
        #
        # Power Integrations variant of 8-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), LongPads, see https://ac-dc.power.com/sites/default/files/product-docs/tinyswitch-iii_family_datasheet.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_PDIP-8C.kicad_mod
        # 
        D  = 10.28,         # body length
        E1 = 4.5,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'PowerIntegrations_PDIP-8C',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [3],          # pin excluded
        ),

    'PowerIntegrations_SDIP-10C': Params(
        #
        # PowerIntegrations variant of 10-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), LongPads, see https://www.power.com/sites/default/files/product-docs/tophx_family_datasheet.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_SDIP-10C.kicad_mod
        # 
        D  = 12.82,         # body length
        E1 = 4.5,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 10,          # number of pins
        modelName = 'PowerIntegrations_SDIP-10C',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [4],          # pin excluded
        ),

    'PowerIntegrations_SMD-8': Params(
        #
        # PowerIntegrations variant of 8-lead surface-mounted (SMD) DIP package, row spacing 7.62 mm (300 mils), see https://www.power.com/sites/default/files/product-docs/lnk520.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_SMD-8.kicad_mod
        # 
        D  = 10.24,         # body length
        E1 = 4.9,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'PowerIntegrations_SMD-8',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [0],          # pin excluded
        ),

    'PowerIntegrations_SMD-8B': Params(
        #
        # PowerIntegrations variant of 8-lead surface-mounted (SMD) DIP package, row spacing 7.62 mm (300 mils), see https://www.power.com/sites/default/files/product-docs/lnk520.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_SMD-8B.kicad_mod
        # 
        D  = 10.24,         # body length
        E1 = 4.9,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'PowerIntegrations_SMD-8B',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [6],          # pin excluded
        ),

    'PowerIntegrations_SMD-8C': Params(
        #
        # PowerIntegrations variant of 8-lead surface-mounted (SMD) DIP package, row spacing 7.62 mm (300 mils), see https://ac-dc.power.com/sites/default/files/product-docs/tinyswitch-iii_family_datasheet.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is PowerIntegrations_SMD-8C.kicad_mod
        # 
        D  = 10.24,         # body length
        E1 = 4.9,         # body width
        E = 7.62,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 8,          # number of pins
        modelName = 'PowerIntegrations_SMD-8C',            # modelName
        rotation = 90,      # rotation if required
        type = 'smd',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [3],          # pin excluded
        ),

    'Toshiba_11-7A9': Params(
        #
        # Toshiba 11-7A9 package, like 6-lead dip package with missing pin 5, row spacing 7.62 mm (300 mils), https://toshiba.semicon-storage.com/info/docget.jsp?did=1421&prodName=TLP3021(S)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Toshiba_11-7A9.kicad_mod
        # 
        D  = 7.86,         # body length
        E1 = 5.54,         # body width
        E = 7.86,          # body overall width
        A1 = 0.38,          # body-board separation
        A2 = 3.3,          # body height
        b1 = 1.52,          # pin width
        b  = 0.46,          # pin tip width
        e = 2.54,          # body-board separation
        npins = 6,          # number of pins
        modelName = 'Toshiba_11-7A9',            # modelName
        rotation = 90,      # rotation if required
        type = 'tht',          # tht, smd or thtsmd
        corner = 'fillet',          # chamfer or fillet
        excludepins = [5],          # pin excluded
        ),

}

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

}

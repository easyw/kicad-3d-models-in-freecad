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

destination_dir="/Inductors_SMD.3dshapes"

#destination_dir="generated_cap"

### Parametric Values
##
Params = namedtuple("Params", [
    'L',   # package length
    'W',   # package width
    'T',   # package height

    'pb',   # pin band
    'pt',   # pin thickness

    'ef',    # fillet of edges
    'modelName', # modelName
    'rotation' # rotation if required
])

all_params_chip_inductor = {
}

kicad_naming_params_chip_inductor = {
    "L_0201" : Params( 
        L = 0.60,  # package length 
        W = 0.30,  # package width 
        T = 0.30,  # package height 
 
        pb = 0.15,  # pin band 
        pt = 0.01,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'L_0201',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "L_0402" : Params( 
        L = 1.0,  # package length 
        W = 0.5,  # package width 
        T = 0.5,  # package height 
 
        pb = 0.25,  # pin band 
        pt = 0.015,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'L_0402',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "L_0603" : Params(
        L = 1.6,  # package length
        W = 0.8,  # package width
        T = 0.8,  # package height

        pb = 0.4,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'L_0603',  # Model Name
        rotation = 0   # rotation
    ),
    "L_0805" : Params(
        L = 2.00,  # package length
        W = 1.25,  # package width
        T = 1.25,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'L_0805',  # Model Name
        rotation = 0   # rotation
    ),
    "L_1206" : Params(
        L = 3.2,  # package length
        W = 1.6,  # package width
        T = 0.85,  # package height

        pb = 0.6,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'L_1206',  # Model Name
        rotation = 0   # rotation
    ),
    "L_1210" : Params( 
        L = 3.2,  # package length 
        W = 2.5,  # package width 
        T = 0.9,  # package height 
 
        pb = 0.6,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'L_1210',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "L_1806" : Params( 
        L = 4.5,  # package length 
        W = 1.6,  # package width 
        T = 1.6,  # package height 
 
        pb = 0.7,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'L_1806',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "L_1812" : Params( # from http://katalog.we-online.de/pbs/datasheet/7427925.pdf
        L = 4.5,  # package length 
        W = 3.2,  # package width 
        T = 1.5,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'L_1812',  # Model Name 
        rotation = 0   # rotation 
    ), 
}

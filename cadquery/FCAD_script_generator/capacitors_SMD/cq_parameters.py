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

destination_dir="/Capacitors_SMD"

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

all_params_chip_cap = {
    "0201_h03" : Params( 
        L = 0.60,  # package length 
        W = 0.30,  # package width 
        T = 0.30,  # package height 
 
        pb = 0.15,  # pin band 
        pt = 0.01,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_0201',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "0402_h05" : Params( 
        L = 1.0,  # package length 
        W = 0.5,  # package width 
        T = 0.5,  # package height 
 
        pb = 0.25,  # pin band 
        pt = 0.015,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_0402',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "0603_h078" : Params(
        L = 1.60,  # package length
        W = 0.81,  # package width
        T = 0.78,  # package height

        pb = 0.25,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'C_0602',  # Model Name
        rotation = 0   # rotation
    ),
    "0805_h078" : Params(
        L = 2.00,  # package length
        W = 1.25,  # package width
        T = 0.78,  # package height

        pb = 0.35,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'C_0805',  # Model Name
        rotation = 0   # rotation
    ),
    "1206_h078" : Params(
        L = 3.05,  # package length
        W = 1.52,  # package width
        T = 0.78,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'C_1206',  # Model Name
        rotation = 0   # rotation
    ),
     "1210_h25" : Params( 
        L = 3.2,  # package length 
        W = 2.5,  # package width 
        T = 2.5,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_1210',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "1812_h25" : Params( 
        L = 4.5,  # package length 
        W = 3.2,  # package width 
        T = 2.5,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_1812',  # Model Name 
        rotation = 0   # rotation 
    ), 
        "2220_h25" : Params( 
        L = 5.7,  # package length 
        W = 5.0,  # package width 
        T = 2.5,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_2220',  # Model Name 
        rotation = 0   # rotation 
    ), 
}

kicad_naming_params_chip_cap = {
    "0201" : Params( 
        L = 0.60,  # package length 
        W = 0.30,  # package width 
        T = 0.30,  # package height 
 
        pb = 0.15,  # pin band 
        pt = 0.01,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_0201',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "0402" : Params( 
        L = 1.0,  # package length 
        W = 0.5,  # package width 
        T = 0.5,  # package height 
 
        pb = 0.25,  # pin band 
        pt = 0.015,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_0402',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "0603" : Params(
        L = 1.60,  # package length
        W = 0.81,  # package width
        T = 0.78,  # package height

        pb = 0.25,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'C_0603',  # Model Name
        rotation = 0   # rotation
    ),
    "0805" : Params(
        L = 2.00,  # package length
        W = 1.25,  # package width
        T = 0.78,  # package height

        pb = 0.35,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'C_0805',  # Model Name
        rotation = 0   # rotation
    ),
    "1206" : Params(
        L = 3.05,  # package length
        W = 1.52,  # package width
        T = 0.78,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'C_1206',  # Model Name
        rotation = 0   # rotation
    ),
    "1210" : Params( 
        L = 3.2,  # package length 
        W = 2.5,  # package width 
        T = 2.5,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_1210',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "1812" : Params( 
        L = 4.5,  # package length 
        W = 3.2,  # package width 
        T = 2.5,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_1812',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "1825" : Params( 
        L = 4.5,  # package length 
        W = 6.4,  # package width 
        T = 2,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_1825',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "2220" : Params( 
        L = 5.7,  # package length 
        W = 5.0,  # package width 
        T = 2.5,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_2220',  # Model Name 
        rotation = 0   # rotation 
    ), 
    "2225" : Params( 
        L = 5.6,  # package length 
        W = 6.4,  # package width 
        T = 1.6,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.02,   # pin thickness 
 
        ef = 0.025, # fillet of edges 
        modelName = 'C_2225',  # Model Name 
        rotation = 0   # rotation 
    ), 
}

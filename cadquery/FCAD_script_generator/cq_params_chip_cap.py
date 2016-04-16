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

#case_color = (139, 69, 19)  #  saddle brown
case_color = (139, 119, 101)  # peach puff 4
pins_color = (230, 230, 230)
destination_dir="/generated_cap"

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

all_params = {
"01005_h02" : Params(
        L = 0.40,  # package length
        W = 0.20,  # package width
        T = 0.20,  # package height

        pb = 0.1,  # pin band
        pt = 0.01,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_01005_h02',  # Model Name
        rotation = 0   # rotation
    ),
"0201_h03" : Params(
        L = 0.60,  # package length
        W = 0.30,  # package width
        T = 0.30,  # package height

        pb = 0.15,  # pin band
        pt = 0.01,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_0201_h03',  # Model Name
        rotation = 0   # rotation
    ),
"0402_h05" : Params(
        L = 1.0,  # package length
        W = 0.5,  # package width
        T = 0.5,  # package height

        pb = 0.25,  # pin band
        pt = 0.015,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_0402_h05',  # Model Name
        rotation = 0   # rotation
    ),
    "0603_h078" : Params(
        L = 1.60,  # package length
        W = 0.81,  # package width
        T = 0.78,  # package height

        pb = 0.25,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_0603_h078',  # Model Name
        rotation = 0   # rotation
    ),
    "0805_h078" : Params(
        L = 2.00,  # package length
        W = 1.25,  # package width
        T = 0.78,  # package height

        pb = 0.35,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_0805_h078',  # Model Name
        rotation = 0   # rotation
    ),
    "0508_h078" : Params(
        L = 1.25,  # package length
        W = 2.00,  # package width
        T = 0.78,  # package height

        pb = 0.35,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_0508_h078',  # Model Name
        rotation = 0   # rotation
    ),
    "1206_h078" : Params(
        L = 3.2,  # package length
        W = 1.6,  # package width
        T = 0.78,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_1206_h078',  # Model Name
        rotation = 0   # rotation
    ),
     "1210_h25" : Params(
        L = 3.2,  # package length
        W = 2.5,  # package width
        T = 2.5,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_1210_h025',  # Model Name
        rotation = 0   # rotation
    ),
    "1812_h25" : Params(
        L = 4.5,  # package length
        W = 3.2,  # package width
        T = 2.5,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_1812_h25',  # Model Name
        rotation = 0   # rotation
    ),
        "2220_h25" : Params(
        L = 5.7,  # package length
        W = 5.0,  # package width
        T = 2.5,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_2220_h25',  # Model Name
        rotation = 0   # rotation
    ),

}
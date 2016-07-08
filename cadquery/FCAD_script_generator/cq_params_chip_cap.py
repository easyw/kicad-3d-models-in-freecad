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
    "1206_h078" : Params(
        L = 3.05,  # package length
        W = 1.52,  # package width
        T = 0.78,  # package height

        pb = 0.5,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'c_1206_h078',  # Model Name
        rotation = 0   # rotation
    ),
}
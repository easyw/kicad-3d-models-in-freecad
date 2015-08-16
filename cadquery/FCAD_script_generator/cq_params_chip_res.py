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

# case_color = (139, 69, 19)  #  saddle brown
# case_color = (139, 119, 101)  # peach puff 4
top_color = (25, 25, 25)  # black
case_color = (255, 255, 255)  # white
pins_color = (230, 230, 230)
destination_dir="/generated_res"

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
    "0402_h040" : Params(
        L = 1.07,  # package length
        W = 0.55,  # package width
        T = 0.40,  # package height

        pb = 0.32,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.02, # fillet of edges
        modelName = 'r_0402_h040',  # Model Name
        rotation = 0   # rotation
    ),
    "0603_h045" : Params(
        L = 1.55,  # package length
        W = 0.85,  # package width
        T = 0.45,  # package height

        pb = 0.40,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.020, # fillet of edges
        modelName = 'r_0603_h078',  # Model Name
        rotation = 0   # rotation
    ),
    "0805_h050" : Params(
        L = 2.00,  # package length
        W = 1.25,  # package width
        T = 0.50,  # package height

        pb = 0.40,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.020, # fillet of edges
        modelName = 'r_0805_h078',  # Model Name
        rotation = 0   # rotation
    ),
    "1206_h055" : Params(
        L = 3.20,  # package length
        W = 1.60,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'r_1206_h078',  # Model Name
        rotation = 0   # rotation
    ),
}
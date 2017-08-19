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

destination_dir="/LED_Chip_SMD"

### Parametric Values
##
Params = namedtuple("Params", [
    'L',   # package length
    'W',   # package width
    'T',   # package height

    'pb',   # pin band
    'pt',   # pin thickness
    'ph',    # pin height

    'pintype',   # can be 'concave' or 'convex'
    'ef',    # fillet of edges
    'modelName', # modelName
    'rotation' # rotation if required
])

all_params_res = {
    "0402_h040" : Params(
        L = 1.07,  # package length
        W = 0.55,  # package width
        T = 0.40,  # package height

        pb = 0.32,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.40,  # pin height

        pintype = 'concave',
        ef = 0.02, # fillet of edges
        modelName = 'r_0402_h040',  # Model Name
        rotation = 0   # rotation
    ),
}   

kicad_naming_params_res = {
    "LED_0402" : Params( # from http://www.produktinfo.conrad.com/datenblaetter/1000000-1099999/001050370-da-01-en-SMD_CHIPLED_GE_0402_KPHHS_1005SYCK.pdf
        L = 1.0,  # package length
        W = 0.5,  # package width
        T = 0.5,  # package height

        pb = 0.15,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.2,  # pin height

        pintype = 'convex',
        ef = 0.02, # fillet of edges
        modelName = 'LED_0402',  # Model Name
        rotation = 180   # rotation
    ),
    "LED_0603" : Params(
        L = 1.6,  # package length
        W = 0.8,  # package width
        T = 1.1,  # package height

        pb = 0.3,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.5,  # pin height

        pintype = 'convex',
        ef = 0.02, # fillet of edges
        modelName = 'LED_0603',  # Model Name
        rotation = 180   # rotation
    ),
    "LED_0606" : Params(
        L = 1.6,  # package length
        W = 1.6,  # package width
        T = 1.1,  # package height

        pb = 0.3,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.5,  # pin height

        pintype = 'convex',
        ef = 0.02, # fillet of edges
        modelName = 'LED_0606',  # Model Name
        rotation = 180   # rotation
    ),
    "LED_0805" : Params( # from http://www.kingbrightusa.com/images/catalog/SPEC/AP2012CGCK.pdf
        L = 2.0,  # package length
        W = 1.25,  # package width
        T = 1.1,  # package height

        pb = 0.35,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.5,  # pin height

        pintype = 'convex',
        ef = 0.02, # fillet of edges
        modelName = 'LED_0805',  # Model Name
        rotation = 180   # rotation
    ),
    "LED_1206" : Params( # from http://www.kingbrightusa.com/images/catalog/SPEC/AP3216CGCK.pdf
        L = 3.2,  # package length
        W = 1.6,  # package width
        T = 1.1,  # package height

        pb = 0.6,  # pin band
        pt = 0.025,   # pin thickness
        ph = 0.5,  # pin height

        pintype = 'convex',
        ef = 0.02, # fillet of edges
        modelName = 'LED_1206',  # Model Name
        rotation = 180   # rotation
    ),
}   

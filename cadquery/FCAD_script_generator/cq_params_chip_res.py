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

all_params_res = {
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
        modelName = 'r_1206_h055',  # Model Name
        rotation = 0   # rotation
    ),
    "2010_h084" : Params(
        L = 5.33,  # package length
        W = 2.54,  # package width
        T = 0.84,  # package height

        pb = 0.51,  # pin band
        pt = 0.04,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'r_2010_h084',  # Model Name
        rotation = 0   # rotation
    ),    
}   

kicad_naming_params_res = {
    "R_0201" : Params(
        L = 0.63,  # package length
        W = 0.33,  # package width
        T = 0.23,  # package height

        pb = 0.15,  # pin band
        pt = 0.02,   # pin thickness

        ef = 0.02, # fillet of edges
        modelName = 'R_0201',  # Model Name
        rotation = 0   # rotation
    ),
    "R_0402" : Params(
        L = 1.07,  # package length
        W = 0.55,  # package width
        T = 0.40,  # package height

        pb = 0.32,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.02, # fillet of edges
        modelName = 'R_0402',  # Model Name
        rotation = 0   # rotation
    ),
    "R_0603" : Params(
        L = 1.55,  # package length
        W = 0.85,  # package width
        T = 0.45,  # package height

        pb = 0.40,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.020, # fillet of edges
        modelName = 'R_0603',  # Model Name
        rotation = 0   # rotation
    ),
    "R_0603_h" : Params(
        L = 1.55,  # package length
        W = 0.85,  # package width
        T = 0.45,  # package height

        pb = 0.40,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.020, # fillet of edges
        modelName = 'R_0603_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
    "R_0805" : Params(
        L = 2.00,  # package length
        W = 1.25,  # package width
        T = 0.50,  # package height

        pb = 0.40,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.020, # fillet of edges
        modelName = 'R_0805',  # Model Name
        rotation = 0   # rotation
    ),
    "R_0805_h" : Params(
        L = 2.00,  # package length
        W = 1.25,  # package width
        T = 0.50,  # package height

        pb = 0.40,  # pin band
        pt = 0.025,   # pin thickness

        ef = 0.020, # fillet of edges
        modelName = 'R_0805_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1206" : Params(
        L = 3.20,  # package length
        W = 1.60,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1206',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1206_h" : Params(
        L = 3.20,  # package length
        W = 1.60,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1206_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1210" : Params(
        L = 3.20,  # package length
        W = 2.5,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1210',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1210_h" : Params(
        L = 3.20,  # package length
        W = 2.5,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1210_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1218" : Params(
        L = 3.20,  # package length
        W = 4.8,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1218',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1218_h" : Params(
        L = 3.20,  # package length
        W = 4.8,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1218_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1508_w" : Params(
        L = 2.0,  # package length
        W = 3.75,  # package width
        T = 0.50,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1508_Wide',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1812" : Params(
        L = 4.5,  # package length
        W = 3.2,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1812',  # Model Name
        rotation = 0   # rotation
    ),
    "R_1812_h" : Params(
        L = 4.5,  # package length
        W = 3.2,  # package width
        T = 0.55,  # package height

        pb = 0.5,  # pin band
        pt = 0.03,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_1812_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
    "R_2010" : Params(
        L = 5.33,  # package length
        W = 2.54,  # package width
        T = 0.84,  # package height

        pb = 0.51,  # pin band
        pt = 0.04,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_2010',  # Model Name
        rotation = 0   # rotation
    ),
    "R_2010_h" : Params(
        L = 5.33,  # package length
        W = 2.54,  # package width
        T = 0.84,  # package height

        pb = 0.51,  # pin band
        pt = 0.04,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_2010_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
    "R_2512" : Params(
        L = 6.4,  # package length
        W = 3.2,  # package width
        T = 0.6 ,  # package height

        pb = 0.51,  # pin band
        pt = 0.04,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_2512',  # Model Name
        rotation = 0   # rotation
    ),  
    "R_2512_h" : Params(
        L = 6.4,  # package length
        W = 3.2,  # package width
        T = 0.6 ,  # package height

        pb = 0.51,  # pin band
        pt = 0.04,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_2512_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),  
    "R_2816" : Params(
        L = 6.4,  # package length
        W = 4.2,  # package width
        T = 0.65 ,  # package height

        pb = 0.51,  # pin band
        pt = 0.04,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_2816',  # Model Name
        rotation = 0   # rotation
    ),
    "R_2816_h" : Params(
        L = 6.4,  # package length
        W = 4.2,  # package width
        T = 0.65 ,  # package height

        pb = 0.51,  # pin band
        pt = 0.04,   # pin thickness

        ef = 0.025, # fillet of edges
        modelName = 'R_2816_HandSoldering',  # Model Name
        rotation = 0   # rotation
    ),
}   

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

destination_dir="/Resistor_array_SMD"

### Parametric Values
##
Params = namedtuple("Params", [
    'L',   # package length
    'W',   # package width
    'T',   # package height

    'pb',   # pin band
    'pt',   # pin thickness

    'A1',   # pin width

    'P',   # pin pitch
    'np',   # number of resistors

    'ef',    # fillet of edges
    'concave',   # true for Concave, false for Convex
    'excluded_pins', #pins to exclude
    'modelName', # modelName
    'rotation' # rotation if required
])

kicad_naming_params_res = {
    "R_Array_Concave_2x0603" : Params( # from http://www.vishay.com/docs/31047/cra06p.pdf
        L = 1.6,  # package length
        W = 1.6,  # package width
        T = 0.6,  # package height
        pb = 0.3, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.4, #pin witdh
        P = 0.8, #pin pitch
        np = 2, #number of resistors
        ef = 0.02, # fillet of edges
        concave = True, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Concave_2x0603',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Concave_4x0402" : Params( # from http://www.vishay.com/docs/31048/cra04p.pdf
        L = 2.0,  # package length
        W = 1.0,  # package width
        T = 0.45,  # package height
        pb = 0.2, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.32, #pin witdh
        P = 0.5, #pin pitch
        np = 4, #number of resistors
        ef = 0.02, # fillet of edges
        concave = True, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Concave_4x0402',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Concave_4x0603" : Params( # from http://www.vishay.com/docs/31047/cra06p.pdf
        L = 3.2,  # package length
        W = 1.6,  # package width
        T = 0.6,  # package height
        pb = 0.3, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.4, #pin witdh
        P = 0.8, #pin pitch
        np = 4, #number of resistors
        ef = 0.02, # fillet of edges
        concave = True, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Concave_4x0603',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_2x0402" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 1.0,  # package length
        W = 1.0,  # package width
        T = 0.35,  # package height
        pb = 0.20, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.3, #pin witdh
        P = 0.5, #pin pitch
        np = 2, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_2x0402',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_2x0603" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 1.6,  # package length
        W = 1.6,  # package width
        T = 0.50,  # package height
        pb = 0.25, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.4, #pin witdh
        P = 0.8, #pin pitch
        np = 2, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_2x0603',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_2x1206" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 2.6,  # package length
        W = 3.1,  # package width
        T = 0.55,  # package height
        pb = 0.5, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.8, #pin witdh
        P = 1.27, #pin pitch
        np = 2, #number of resistors
        ef = 0.04, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_2x1206',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_4x0402" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 2.0,  # package length
        W = 1.0,  # package width
        T = 0.35,  # package height
        pb = 0.20, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.3, #pin witdh
        P = 0.5, #pin pitch
        np = 4, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_4x0402',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_4x0603" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 3.2,  # package length
        W = 1.6,  # package width
        T = 0.50,  # package height
        pb = 0.25, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.4, #pin witdh
        P = 0.8, #pin pitch
        np = 4, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_4x0603',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_4x1206" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 5.4,  # package length
        W = 3.1,  # package width
        T = 0.55,  # package height
        pb = 0.5, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.8, #pin witdh
        P = 1.27, #pin pitch
        np = 4, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_4x1206',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_5x0603" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 3.2,  # package length
        W = 1.6,  # package width
        T = 0.50,  # package height
        pb = 0.3, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.32, #pin witdh
        P = 0.64, #pin pitch
        np = 5, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_5x0603',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_5x1206" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 6.4,  # package length
        W = 3.1,  # package width
        T = 0.55,  # package height
        pb = 0.5, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.8, #pin witdh
        P = 1.27, #pin pitch
        np = 5, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_5x1206',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_8x0602" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 3.8,  # package length
        W = 1.6,  # package width
        T = 0.45,  # package height
        pb = 0.3, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.3, #pin witdh
        P = 0.5, #pin pitch
        np = 8, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_8x0602',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Cat16-2" : Params( # from https://www.bourns.com/pdfs/CATCAY.pdf
        L = 1.6,  # package length
        W = 1.6,  # package width
        T = 0.5,  # package height
        pb = 0.3, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.4, #pin witdh
        P = 0.8, #pin pitch
        np = 2, #number of resistors
        ef = 0.02, # fillet of edges
        concave = True, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Cat16-2',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Cat16-4" : Params( # from https://www.bourns.com/pdfs/CATCAY.pdf
        L = 3.2,  # package length
        W = 1.6,  # package width
        T = 0.5,  # package height
        pb = 0.3, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.4, #pin witdh
        P = 0.8, #pin pitch
        np = 4, #number of resistors
        ef = 0.02, # fillet of edges
        concave = True, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Cat16-4',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Cat16-8" : Params( # from https://www.bourns.com/pdfs/CATCAY.pdf
        L = 6.4,  # package length
        W = 1.6,  # package width
        T = 0.5,  # package height
        pb = 0.3, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.4, #pin witdh
        P = 0.8, #pin pitch
        np = 8, #number of resistors
        ef = 0.02, # fillet of edges
        concave = True, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Cat16-8',  # Model Name
        rotation = 0   # rotation
    ),
    "R_Array_Convex_4x0402" : Params( # from http://www.rohm.com/web/global/datasheet/MNR12E0APF/mnr-e
        L = 2.0,  # package length
        W = 1.0,  # package width
        T = 0.35,  # package height
        pb = 0.25, # pin band
        pt = 0.025, # pin thickness
        A1 = 0.3, #pin witdh
        P = 0.5, #pin pitch
        np = 4, #number of resistors
        ef = 0.02, # fillet of edges
        concave = False, # true for Concave, false for Convex
        excluded_pins = None, #no pin excluded
        modelName = 'R_Array_Convex_4x0402',  # Model Name
        rotation = 0   # rotation
    ),

}   

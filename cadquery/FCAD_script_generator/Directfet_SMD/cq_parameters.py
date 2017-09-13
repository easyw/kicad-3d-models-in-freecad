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

destination_dir="/DirecFETs"

#destination_dir="generated_cap"

### Parametric Values
##
Params = namedtuple("Params", [
    'A',   # package length
    'B',   # package width
    'C',   # wing width
    'D',   # wing length

    'M',   # package height
    'P',   # die and body height over board
    'R',   # pad height over board

    'die',  # die (sizex, sizey)
    'pads',

    'modelName', # modelName
    'rotation' # rotation if required
])

all_params_DirecFETs = {

}

kicad_naming_params_DirecFETs = {
    "DirectFET_L8" : Params( # from https://www.infineon.com/dgdl/irf7749l1pbf.pdf?fileId=5546d462533600a4015356043d6b1ca0
        A = 9.1,  # package length 
        B = 7.0,  # package width 
        C = 5.95,   # wing width
        D = 0.6,   # wing length

        M = 0.7,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (6.7,5.7), # die size
        pads = ([0.7,1.3,-2.4,0],
                [1.1,0.85,-1,-0.575],
                [1.1,0.85,-1,-1.725],
                [1.1,0.85,-1,0.575],
                [1.1,0.85,-1,1.725],
                [1.1,0.85,1.8,-0.575],
                [1.1,0.85,1.8,-1.725],
                [1.1,0.85,1.8,0.575],
                [1.1,0.85,1.8,1.725]),

        modelName = 'DirectFET_L8',  # Model Name 
        rotation = 0   # rotation 
    ), 
}

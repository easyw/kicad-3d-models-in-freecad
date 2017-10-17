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
    "DirectFET_ME" : Params( # from http://www.irf.com/technical-info/appnotes/an-1035.pdf
        A = 6.3,  # package length 
        B = 4.9,  # package width 
        C = 3.9,   # wing width
        D = 0.4,   # wing length
        M = 0.65,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (4.5,3.9), # die size
        pads = ([0.6,1.1,-1.55, 0.95],
                [0.6,1.3,-1.55, -0.85],
                [0.95,1.3,-0.175,-0.85],
                [0.95,1.3,-0.175,0.85],
                [0.95,1.3,1.375,-0.85],
                [0.95,1.3,1.375,0.85]),
        modelName = 'DirectFET_ME',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_MN" : Params( # from https://www.infineon.com/dgdl/irf6646pbf.pdf?fileId=5546d462533600a4015355ec5f071a55
        A = 6.3,  # package length 
        B = 4.9,  # package width 
        C = 3.9,   # wing width
        D = 0.4,   # wing length
        M = 0.65,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (4.5,3.9), # die size
        pads = ([0.85,0.95,-1.125,0],
                [1.45,0.95,0.695,-0.7],
                [1.45,0.95,0.695,0.7]),
        modelName = 'DirectFET_MN',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_MP" : Params( # from https://www.infineon.com/dgdl/irf6633pbf.pdf?fileId=5546d462533600a4015355e8dfe91a3b
        A = 6.3,  # package length 
        B = 4.9,  # package width 
        C = 3.9,   # wing width
        D = 0.4,   # wing length
        M = 0.65,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (4.5,3.9), # die size
        pads = ([0.65,0.65,-0.8,0],
                [0.825,0.6,0.59,-0.415],
                [0.825,0.6,0.59,0.415]),
        modelName = 'DirectFET_MP',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_MT" : Params( # from DirectFET MT https://www.infineon.com/dgdl/irf6613pbf.pdf?fileId=5546d462533600a4015355e82b9b1a0d
        A = 6.3,  # package length 
        B = 4.9,  # package width 
        C = 3.9,   # wing width
        D = 0.4,   # wing length
        M = 0.65,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (4.5,3.9), # die size
        pads = ([0.85,0.95,-1.405,0],
                [1.85,1.05,0.695,-0.825],
                [1.85,1.05,0.695,0.825]),
        modelName = 'DirectFET_MT',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_MX" : Params( # from https://www.infineon.com/dgdl/irf8302mpbf.pdf?fileId=5546d462533600a40153560d16e41d5b
        A = 6.3,  # package length 
        B = 4.9,  # package width 
        C = 3.9,   # wing width
        D = 0.4,   # wing length
        M = 0.65,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (4.5,3.9), # die size
        pads = ([0.75,0.75,-1.45,0],
                [1.45,0.87,0.3,-0.61],
                [1.45,0.87,0.3,0.61]),
        modelName = 'DirectFET_MX',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_MZ" : Params( # from https://www.infineon.com/dgdl/irf6668pbf.pdf?fileId=5546d462533600a4015355ec96b91a64
        A = 6.3,  # package length 
        B = 4.9,  # package width 
        C = 3.9,   # wing width
        D = 0.4,   # wing length
        M = 0.65,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (4.5,3.9), # die size
        pads = ([0.75,0.75,-1.2,0],
                [1.0,0.7,0.325,-0.475],
                [1.0,0.7,0.325,0.475]),
        modelName = 'DirectFET_MZ',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_S1" : Params( # from https://www.infineon.com/dgdl/irf6810spbf.pdf?fileId=5546d462533600a4015355f0ab331ab4https://www.infineon.com/dgdl/irf6810spbf.pdf?fileId=5546d462533600a4015355f0ab331ab4https://www.infineon.com/dgdl/irf6810spbf.pdf?fileId=5546d462533600a4015355f0ab331ab4
        A = 4.80,  # package length 
        B = 3.85,  # package width 
        C = 2.8,   # wing width
        D = 0.4,   # wing length
        M = 0.565,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (2.95,2.8), # die size
        pads = ([0.55,0.65,-0.9,0],
                [0.55,1.15,0.0,0.0]),
        modelName = 'DirectFET_S1',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_S2" : Params( # from https://www.infineon.com/dgdl/Infineon-AN-1035-AN-v29_00-EN.pdf?fileId=5546d462533600a40153559159020f76
        A = 4.80,  # package length 
        B = 3.85,  # package width 
        C = 2.8,   # wing width
        D = 0.4,   # wing length
        M = 0.565,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (2.95,2.8), # die size
        pads = ([0.55,0.65,-0.9,0],
                [0.55,1.15,0.0,0.0],
                [0.55,1.15,0.9,0.0]),
        modelName = 'DirectFET_S2',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_SH" : Params( # from https://www.infineon.com/dgdl/irf6655pbf.pdf?fileId=5546d462533600a4015355ec76961a5bhttps://www.infineon.com/dgdl/irf6655pbf.pdf?fileId=5546d462533600a4015355ec76961a5bhttps://www.infineon.com/dgdl/irf6655pbf.pdf?fileId=5546d462533600a4015355ec76961a5b
        A = 4.80,  # package length 
        B = 3.85,  # package width 
        C = 2.8,   # wing width
        D = 0.4,   # wing length
        M = 0.565,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (2.95,2.8), # die size
        pads = ([0.55,0.65,-0.695,0],
                [0.7,0.9,0.635,0]),
        modelName = 'DirectFET_SH',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_SJ" : Params( # from https://www.infineon.com/dgdl/irf6810spbf.pdf?fileId=5546d462533600a4015355f0ab331ab4
        A = 4.80,  # package length 
        B = 3.85,  # package width 
        C = 2.8,   # wing width
        D = 0.4,   # wing length
        M = 0.565,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (2.95,2.8), # die size
        pads = ([0.65,0.65,-0.7,0],
                [0.75,0.75,0.65,-0.475],
                [0.75,0.75,0.65, 0.475]),
        modelName = 'DirectFET_SJ',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_SQ" : Params( # from https://www.infineon.com/dgdl/irf8327spbf.pdf?fileId=5546d462533600a40153560d40c41d65
        A = 4.80,  # package length 
        B = 3.85,  # package width 
        C = 2.8,   # wing width
        D = 0.4,   # wing length
        M = 0.565,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (2.95,2.8), # die size
        pads = ([0.55,0.85,-0.8,0],
                [0.95,0.85,0.5,0]),
        modelName = 'DirectFET_SQ',  # Model Name 
        rotation = 0   # rotation 
    ),
    "DirectFET_ST" : Params( # from https://www.infineon.com/dgdl/irf8327spbf.pdf?fileId=5546d462533600a40153560d40c41d65
        A = 4.80,  # package length 
        B = 3.85,  # package width 
        C = 2.8,   # wing width
        D = 0.4,   # wing length
        M = 0.565,   # package height
        P = 0.13,   # die and body height over board
        R = 0.05,   # pad height over board
        
        die = (2.95,2.8), # die size
        pads = ([0.65,0.65,-0.76,0],
                [0.82,0.6,0.63,-0.415],
                [0.82,0.6,0.63,0.415]),
        modelName = 'DirectFET_ST',  # Model Name 
        rotation = 0   # rotation 
    ),
}

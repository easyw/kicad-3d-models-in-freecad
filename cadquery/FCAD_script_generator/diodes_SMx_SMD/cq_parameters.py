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

destination_dir="/Diodes_SMD"
# destination_dir="./"

ma_deg = 8

Params = namedtuple("Params", [
    'L',    # body overall length (including terminals)
    'W',    # body overall width
    'H',    # body overall height
    'F',    # width of each termination
    'S',    # length of each termination
    'T',    # thickness of termination metal
    'G',    # length of bump underneath body
    'pml',  # pin mark lenght
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

kicad_naming_params_tantalum = {
    'D_SMA': Params( # from http://www.galco.com/techdoc/vish/10mq100n_ds.pdf
        L = 5.0,
        W = 2.7,
        H = 2.22,
        F = 1.5,
        S = 1.14,
        T = 0.22,
        G = 2.2,
        pml = 0.6,
        modelName = 'D_SMA', #modelName
        rotation = 90, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
    'D_SMB': Params( # from http://www.vishay.com/docs/95017/smb.pdf
        L = 5.3,
        W = 3.55,
        H = 2.15,
        F = 2.0,
        S = 1.03,
        T = 0.22,
        G = 2.6,
        pml = 0.6,
        modelName = 'D_SMB', #modelName
        rotation = 90, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
    'D_SMC': Params( # from http://www.vishay.com/docs/95023/smc.pdf
        L = 8.0,
        W = 5.9,
        H = 2.31,
        F = 3.0,
        S = 1.14,
        T = 0.22,
        G = 5.0,
        pml = 0.6,
        modelName = 'D_SMC', #modelName
        rotation = 90, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
}

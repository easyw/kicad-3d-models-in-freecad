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

destination_dir="/CP_Tantal_THT"
# destination_dir="./"

Params = namedtuple("Params", [
    'L' ,  # body length
    'W' ,  # body Diameter
    'd' ,  # lead diameter
    'F' ,  # lead separation (center to center)
    'll',  # lead length
    'bs',  # board separation
    'modelName', # modelName
    'rotation',  # rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_c_axial_th_cap = {# 
}

kicad_naming_params_c_axial_th_cap = {
    "CP_Radial_Tantal_D4.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 4.50, # Body Length
        W = 4.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D4.5mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D4.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 4.50, # Body Length
        W = 4.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D4.5mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D5.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 5.00, # Body Length
        W = 5.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D5.0mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D5.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 5.00, # Body Length
        W = 5.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D5.0mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D5.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 5.50, # Body Length
        W = 5.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D5.5mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D5.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 5.50, # Body Length
        W = 5.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D5.5mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D6.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 6.00, # Body Length
        W = 6.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D6.0mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D6.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 6.00, # Body Length
        W = 6.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D6.0mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D7.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 7.00, # Body Length
        W = 7.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D7.0mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D7.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 7.00, # Body Length
        W = 7.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D7.0mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D8.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 8.00, # Body Length
        W = 8.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D8.0mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D8.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 8.00, # Body Length
        W = 8.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D8.0mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D9.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 9.00, # Body Length
        W = 9.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D9.0mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D9.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 9.00, # Body Length
        W = 9.00, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D9.0mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D10.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 10.50, # Body Length
        W = 10.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 2.50, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D10.5mm_P2.50mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),

    "CP_Radial_Tantal_D10.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 10.50, # Body Length
        W = 10.50, # Body Width
        d = 0.50, # Lead Diameter
        F = 5.00, # Lead Seperation
        ll = 2.0, # Lead Length
        bs = 0.1, # Board Seperation
        modelName = 'CP_Radial_Tantal_D10.5mm_P5.00mm', # Modelname
        rotation = 0, # Rotation
        dest_dir_prefix = '../Capacitors_THT.3dshapes/', # Destination
    ),
}   
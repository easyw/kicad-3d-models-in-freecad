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

destination_dir="/Standoff.3dshapes"

Params = namedtuple("Params", [
    'OD', # Outer Diameter, Flat side to flatside for HEX
    'ID', # Inner Diameter
    'H', # Height of standoff
    'shape', # Shape can be 'Round' or 'Hex'
    'modelName', # modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

kicad_naming_params_standoff = {
    'FF_9.0mm_D5.0': Params(	#from http://katalog.we-online.de
        OD = 5.0, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 9.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        modelName = 'FF_9.0mm_D5.0', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'Standoff_Height_13.0mm_HEX': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 13.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        modelName = 'Standoff_Height_13.0mm_HEX', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'Standoff_Height_20.0mm_HEX': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 4.0, # Outer Diameter, Flat side to flatside for HEX
        ID = 2.0, # Inner Diameter
        H = 20.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        modelName = 'Standoff_Height_20.0mm_HEX', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'FF_29.0mm_D5.0': Params(	#from http://katalog.we-online.de
        OD = 5.0, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 29.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        modelName = 'FF_29.0mm_D5.0', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
}
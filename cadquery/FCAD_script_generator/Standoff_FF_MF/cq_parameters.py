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
    'stud_H',  # height of Stud 0.0 means NO Stud
    'modelName', # modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

   
kicad_naming_params_standoff = {
    'FF_9.0mm_D5.0': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.0, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 9.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'FF_9.0mm_D5.0', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'Standoff_Height_13.0mm_HEX': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 13.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'Standoff_Height_13.0mm_HEX', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'Standoff_Height_20.0mm_HEX': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 4.0, # Outer Diameter, Flat side to flatside for HEX
        ID = 2.0, # Inner Diameter
        H = 20.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'Standoff_Height_20.0mm_HEX', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'M3x9_FF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 9.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x9_FF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'M3x10_FF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 10.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x10_FF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'M3x12_FF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 12.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x12_FF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'M3x14_FF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 10.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x14_FF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'M3x14_MF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 14.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 6.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x14_MF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),    
    'M3x15_FF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 10.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x15_FF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'M3x15_MF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 15.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 6.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x15_MF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),    
    'M3x19_FF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 19.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x19_FF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
    'M3x29_FF_D5.5': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        OD = 5.5, # Outer Diameter, Flat side to flatside for HEX
        ID = 3.0, # Inner Diameter
        H = 29.0, # Height of standoff
        shape = 'Hex', # Shape can be 'Round' or 'Hex'
        stud_H = 0.0,  # height of Stud 0.0 means NO Stud
        modelName = 'M3x29_FF_D5.5', # Modelname
        rotation = -90, #rotation if required
        dest_dir_prefix = '../Spacers/', # Destination
    ),
}


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

import collections
from collections import namedtuple

footprints_dir="TerminalBlock_Altech.pretty"

##enabling optional/default values to None
def namedtuple_with_defaults(typename, field_names, default_values=()):

    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T

Params = namedtuple_with_defaults("Params", [
	'manufacture',		# Manufacture
	'serie',		    # ModelName
	'W',			   	# package width
	'H',				# package height
	'WD',				# > Y distance form pin center to package edge
	'A1',				# package board seperation
    'pin_number',       # Pin number serie
    'PE',               # Distance from edge to pin
    'PS',               # Pin distance
    'PD',               # Pin diameter
    'PL',               # Pin length
    'PF',               # Pin form
    'SW',               # Blender width
    'rotation',         # Rotation
    'body_color_key',   # Body colour
    'pin_color_key',    # Pin colour
	'dest_dir_prefix'	# Destination directory
])

all_params = {

    'AK300': Params(   # ModelName
        #
        #
        #
        manufacture = 'Altech', # Manufacture name
        serie = 'AK300',        # Model name
        W  = 12.5,              # Package width
        H  = 12.5,              # Package height
        WD  = 6.5,              # > Y distance form pin center to package edge
        A1 = 0.1,               # package board seperation
#        pin_number = [ 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],  # Which pin configuration
        pin_number = [ 2,3],  # Which pin configuration
        PE = 2.5,               # Distance from edge to pin
        PS = 5.0,               # Distance between pins
        PD = [1.0, 0.8],        # Pin size, [1.0] diameter 1 mm, [1.0, 0.8] rectangle 1.0x0.8
        PL = 4.5,               # Pin length
        PF = 'rect',            # Pin form 'round' or 'rect'
        SW = 2.7,               # Blender width
        rotation = 0,           # Rotation if required
        body_color_key  = 'black body',         # Body color
        pin_color_key   = 'metal grey pins',    # Pin color
        dest_dir_prefix    = 'TerminalBlock_Altech.3dshapes'  # Destination directory
        ),

        
    'MKDS_1_5': Params(   # ModelName
        #
        #
        #
        manufacture = 'TerminalBlock_Phoenix', # Manufacture name
        serie = 'MKDS-1,5', # Model name
        W  = 9.8,               # Package width
        H  = 13.8,              # Package height
        WD  = 4.6,              # > Y distance form pin center to package edge
        A1 = 0.1,               # package board seperation
        pin_number = [ 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],  # Which pin configuration
        PE = 2.54,              # Distance from edge to pin
        PS = 5.08,              # Distance between pins
        PD = [1.0, 0.8],        # Pin size, [1.0] diameter 1 mm, [1.0, 0.8] rectangle 1.0x0.8
        PL = 3.5,               # Pin length
        PF = 'rect',            # Pin form 'round' or 'rect'
        SW = 2.7,               # Blender width
        rotation = 0,           # Rotation if required
        body_color_key  = 'green body',         # Body color
        pin_color_key   = 'metal grey pins',    # Pin color
        dest_dir_prefix    = 'TerminalBlock_Phoenix.3dshapes'  # Destination directory
        ),

}

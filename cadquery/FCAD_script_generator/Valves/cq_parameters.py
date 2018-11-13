
# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#

## file of parametric definitions

import collections
from collections import namedtuple

destination_dir="/Valve.3dshapes"
# destination_dir="./"
old_footprints_dir="Valve.pretty"
footprints_dir="Valve.pretty"
##footprints_dir=None #to exclude importing of footprints

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
	'modelName',		    # modelName
	'D',				    # package diameter
	'E',			   	    # body height
	'A1',				    # package height
	'b',				    # pin width
    'center',               # Body center
    'npthhole',             # NPTH holes
    'ph',                   # Pin length
	'pin',		            # Pins
	'pintype',		        # Pin type, 'tht', 'smd'
	'serie',			    # The component serie
	'body_top_color_key',	# Top color
	'body_color_key',	    # Body colour
	'pin_color_key',	    # Pin color
    'npth_pin_color_key',   # NPTH Pin color
	'rotation',	            # Rotation if required
	'dest_dir_prefix'	    # Destination directory
])


all_params = {

    'Valve_ECC-83-1': Params(
        #
        # Valve
        # This model have been auto generated based on the foot print file
        # A number of parameters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Valve_ECC-83-1.kicad_mod
        # 
        modelName = 'Valve_ECC-83-1',   # modelName
        D = 20.00,                  # Body diameter
        E = 49.20,                  # Body height
        A1 = 0.03,                  # Body-board separation
        b = 1.00,                   # Pin width
        center = (-3.455, 4.75),    # Body center
        npthhole = None,              # NPTH hole [(x, y, length)]
        ph = 6.4,                   # Pin length
        pin = [(0.0, 0.0), (2.15, -2.93), (2.15, -6.58), (0, -9.51), (-3.45, -10.65), (-6.91, -9.51), (-9.06, -6.58), (-9.06, -2.97), (-6.91, 0) ],          # Pins
        pintype = 'tht',            # Pin type, 'tht', 'smd'
        serie = 'ECC',              # 
        body_top_color_key = 'metal silver',   # Top color
        body_color_key = 'led blue',        # Body color
        pin_color_key = 'metal grey pins',  # Pin color
        npth_pin_color_key = 'grey body',   # NPTH Pin color
        rotation = 0,                       # Rotation if required
        dest_dir_prefix = '../Valve.3dshapes',      # destination directory
        ),


    'Valve_ECC-83-2': Params(
        #
        # Valve
        # This model have been auto generated based on the foot print file
        # A number of parameters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Valve_ECC-83-2.kicad_mod
        # 
        modelName = 'Valve_ECC-83-2',   # modelName
        D = 20.00,                  # Body diameter
        E = 49.20,                  # Body height
        A1 = 0.03,                  # Body-board separation
        b = 1.00,                   # Pin width
        center = (-3.455, 4.75),    # Body center
        npthhole = [(-3.45, -4.75, 3.0, 6.4)],              # NPTH hole [(x, y, diameter, length)] or None
        ph = 6.4,                   # Pin length
        pin = [(0.0, 0.0), (2.15, -2.93), (2.15, -6.58), (0, -9.51), (-3.45, -10.65), (-6.91, -9.51), (-9.06, -6.58), (-9.06, -2.97), (-6.91, 0) ],          # Pins
        pintype = 'tht',            # Pin type, 'tht', 'smd'
        serie = 'ECC',              # 
        body_top_color_key = 'metal silver',   # Top color
        body_color_key = 'led blue',        # Body color
        pin_color_key = 'metal grey pins',  # Pin color
        npth_pin_color_key = 'grey body',   # NPTH Pin color
        rotation = 0,                       # Rotation if required
        dest_dir_prefix = '../Valve.3dshapes',      # destination directory
        ),

    'Valve_EURO': Params(
        #
        # Valve
        # This model have been auto generated based on the foot print file
        # A number of parameters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Valve_EURO.kicad_mod
        # 
        modelName = 'Valve_EURO',   # modelName
        D = 18.84,                  # Body diameter
        E = 49.20,                  # Body height
        A1 = 0.03,                  # Body-board separation
        b = 1.00,                   # Pin width
        center = (1.5, -8.48),    # Body center
        npthhole = [(1.5, 8.48, 4.0, 6.4)],              # NPTH hole [(x, y, diameter, length)] or None
        ph = 6.4,                   # Pin length
        pin = [(0.0, 0.0), (9.5, 8.48), (0, 16.97), (-6.5, 8.48), (1.5, 8.48) ],          # Pins
        pintype = 'tht',            # Pin type, 'tht', 'smd'
        serie = 'ECC',              # 
        body_top_color_key = 'metal silver',   # Top color
        body_color_key = 'led blue',        # Body color
        pin_color_key = 'metal grey pins',  # Pin color
        npth_pin_color_key = 'grey body',   # NPTH Pin color
        rotation = 0,                       # Rotation if required
        dest_dir_prefix = '../Valve.3dshapes',      # destination directory
        ),

    'Valve_Mini_P': Params(
        #
        # Valve
        # This model have been auto generated based on the foot print file
        # A number of parameters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Valve_Mini_P.kicad_mod
        # 
        modelName = 'Valve_Mini_P', # modelName
        D = 17.44,                  # Body diameter
        E = 49.20,                  # Body height
        A1 = 0.03,                  # Body-board separation
        b = 0.80,                   # Pin width
        center = (-6.35, 2.54),     # Body center
        npthhole = None,            # NPTH hole [(x, y, diameter, length)] or None
        ph = 6.4,                   # Pin length
        pin = [(0.0, 0.0), (0, -5.08), (-3.81, -8.89), (-8.89, -8.89), (-12.7, -5.08), (-12.7, 0), (-8.89, 3.81) ],          # Pins
        pintype = 'tht',            # Pin type, 'tht', 'smd'
        serie = 'ECC',              # 
        body_top_color_key = 'metal silver',   # Top color
        body_color_key = 'led blue',        # Body color
        pin_color_key = 'metal grey pins',  # Pin color
        npth_pin_color_key = 'grey body',   # NPTH Pin color
        rotation = 0,                       # Rotation if required
        dest_dir_prefix = '../Valve.3dshapes',      # destination directory
        ),

    'Valve_Noval_P': Params(
        #
        # Valve
        # This model have been auto generated based on the foot print file
        # A number of parameters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Valve_Noval_P.kicad_mod
        # 
        modelName = 'Valve_Noval_P', # modelName
        D = 22.61,                  # Body diameter
        E = 65.00,                  # Body height
        A1 = 0.03,                  # Body-board separation
        b = 0.80,                   # Pin width
        center = (-7.62, 5.08),     # Body center
        npthhole = None,            # NPTH hole [(x, y, diameter, length)] or None
        ph = 6.4,                   # Pin length
        pin = [(0.0, 0.0), (0, -5.08), (0, -10.16), (-5.08, -12.7), (-10.16, -12.7), (-15.24, -10.16), (-15.24, -5.08), (-15.24, 0), (-10.16, 2.54) ],          # Pins
        pintype = 'tht',            # Pin type, 'tht', 'smd'
        serie = 'ECC',              # 
        body_top_color_key = 'metal silver',   # Top color
        body_color_key = 'led blue',        # Body color
        pin_color_key = 'metal grey pins',  # Pin color
        npth_pin_color_key = 'grey body',   # NPTH Pin color
        rotation = 0,                       # Rotation if required
        dest_dir_prefix = '../Valve.3dshapes',      # destination directory
        ),

    'Valve_Octal': Params(
        #
        # Valve
        # This model have been auto generated based on the foot print file
        # A number of parameters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is Valve_Octal.kicad_mod
        # 
        modelName = 'Valve_Octal', # modelName
        D = 27.58,                  # Body diameter
        E = 49.20,                  # Body height
        A1 = 0.03,                  # Body-board separation
        b = 1.70,                   # Pin width
        center = (-7.62, 7.62),     # Body center
        npthhole = [(-7.62, -7.62, 5.4, 6.4)],            # NPTH hole [(x, y, diameter, length)] or None
        ph = 6.4,                   # Pin length
        pin = [(0.0, 0.0), (2.54, -7.62), (0, -15.24), (-7.62, -17.78), (-15.24, -15.24), (-17.78, -7.62), (-15.24, 0), (-7.62, 2.54) ],          # Pins
        pintype = 'tht',            # Pin type, 'tht', 'smd'
        serie = 'ECC',              # 
        body_top_color_key = 'metal silver',   # Top color
        body_color_key = 'led blue',        # Body color
        pin_color_key = 'metal grey pins',  # Pin color
        npth_pin_color_key = 'grey body',   # NPTH Pin color
        rotation = 0,                       # Rotation if required
        dest_dir_prefix = '../Valve.3dshapes',      # destination directory
        ),

}


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

destination_dir="/Varistor.3dshapes"
# destination_dir="./"
old_footprints_dir="Varistor.pretty"
footprints_dir="Varistor.pretty"
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
	'modelName',		#modelName
	'D',				# package length
	'E',			   	# body overall width
	'A1',				# package height
	'b',				# pin width
    'ph',               # Pin length
	'pin',		        # Pins
	'pintype',		    # Pin type, 'tht', 'smd'
	'serie',			# The component serie
	'body_color_key',	# Body colour
	'pin_color_key',	# Pin color
	'rotation',	        # Rotation if required
	'dest_dir_prefix'	# Destination directory
])


all_params = {

    'RV_Disc_D12mm_W3.9mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 3.9mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W3.9mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W3.9mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 3.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4.2mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4.2mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4.2mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4.2mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.63333)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4.3mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4.3mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4.3mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4.3mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4.4mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4.4mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4.4mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4.4mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.775)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4.5mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4.5mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4.5mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4.5mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4.6mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4.6mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4.6mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4.6mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.6,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.2)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4.7mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4.7mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4.7mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4.7mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4.8mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4.8mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4.8mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4.8mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.05)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W4mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 4mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W4mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W4mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.45)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W5.1mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 5.1mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W5.1mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W5.1mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 5.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W5.4mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 5.4mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W5.4mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W5.4mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 5.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W5.8mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 5.8mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W5.8mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W5.8mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 5.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.7)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W5mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 5mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W5mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W5mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 5.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.2)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W6.1mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 6.1mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W6.1mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W6.1mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 6.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W6.2mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 6.2mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W6.2mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W6.2mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 6.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W6.3mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 6.3mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W6.3mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W6.3mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 6.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.1)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W6.7mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 6.7mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W6.7mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W6.7mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 6.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W7.1mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 7.1mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W7.1mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W7.1mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 7.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.7)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W7.5mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 7.5mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W7.5mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W7.5mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 7.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 4.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D12mm_W7.9mm_P7.5mm': Params(
        #
        # Varistor, diameter 12mm, width 7.9mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D12mm_W7.9mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D12mm_W7.9mm_P7.5mm',            # modelName
        D = 12.0,         # body length
        E = 7.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 4.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W11mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 11mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W11mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W11mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 11.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 6.7)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W3.9mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 3.9mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W3.9mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W3.9mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 3.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.2mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.2mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.2mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.2mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.7)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.3mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.3mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.3mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.3mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.4mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.4mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.4mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.4mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.86667)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.5mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.5mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.5mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.5mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.6mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.6mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.6mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.6mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.6,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.05)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.7mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.7mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.7mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.7mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.8mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.8mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.8mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.8mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4.9mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4.9mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4.9mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4.9mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.2)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W4mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 4mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W4mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W4mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.45)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W5.2mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 5.2mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W5.2mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W5.2mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 5.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W5.4mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 5.4mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W5.4mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W5.4mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 5.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W5.9mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 5.9mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W5.9mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W5.9mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 5.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.7)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W5mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 5mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W5mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W5mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 5.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.2)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W6.1mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 6.1mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W6.1mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W6.1mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 6.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 2.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W6.3mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 6.3mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W6.3mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W6.3mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 6.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W6.4mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 6.4mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W6.4mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W6.4mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 6.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.1)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W6.8mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 6.8mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W6.8mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W6.8mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 6.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W7.2mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 7.2mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W7.2mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W7.2mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 7.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 3.7)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W7.5mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 7.5mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W7.5mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W7.5mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 7.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 4.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D15.5mm_W8mm_P7.5mm': Params(
        #
        # Varistor, diameter 15.5mm, width 8mm, pitch 7.5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D15.5mm_W8mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D15.5mm_W8mm_P7.5mm',            # modelName
        D = 15.5,         # body length
        E = 8.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.72,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 4.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D16.5mm_W6.7mm_P7.5mm': Params(
        #
        # Varistor, diameter 16.5mm, width 6.7mm, pitch 5mm, https://katalog.we-online.de/pbs/datasheet/820542711.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D16.5mm_W6.7mm_P7.5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D16.5mm_W6.7mm_P7.5mm',            # modelName
        D = 16.5,         # body length
        E = 6.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.81,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (7.5, 1.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W11.4mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 11.4mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W11.4mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W11.4mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 11.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 6.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W4.3mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 4.3mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W4.3mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W4.3mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 4.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 1.5)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W4.4mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 4.4mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W4.4mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W4.4mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 4.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 1.6)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W4.5mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 4.5mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W4.5mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W4.5mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 4.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 1.55)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W4.6mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 4.6mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W4.6mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W4.6mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 4.6,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 1.7)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W4.7mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 4.7mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W4.7mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W4.7mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 4.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 1.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W4.8mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 4.8mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W4.8mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W4.8mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 4.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 1.95)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W4.9mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 4.9mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W4.9mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W4.9mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 4.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.1)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W5.1mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 5.1mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W5.1mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W5.1mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 5.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.15)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W5.3mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 5.3mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W5.3mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W5.3mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 5.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.2)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W5.4mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 5.4mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W5.4mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W5.4mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 5.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.35)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W5.6mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 5.6mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W5.6mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W5.6mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 5.6,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W5.8mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 5.8mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W5.8mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W5.8mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 5.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.6)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W5mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 5mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W5mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W5mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 5.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W6.3mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 6.3mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W6.3mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W6.3mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 6.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 2.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W6.5mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 6.5mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W6.5mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W6.5mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 6.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 3.1)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W6.7mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 6.7mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W6.7mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W6.7mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 6.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 3.1)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W6.8mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 6.8mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W6.8mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W6.8mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 6.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 3.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W7.1mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 7.1mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W7.1mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W7.1mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 7.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 3.5)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W7.5mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 7.5mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W7.5mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W7.5mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 7.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 3.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W7.9mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 7.9mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W7.9mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W7.9mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 7.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 4.2)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D21.5mm_W8.4mm_P10mm': Params(
        #
        # Varistor, diameter 21.5mm, width 8.4mm, pitch 10mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D21.5mm_W8.4mm_P10mm.kicad_mod
        # 
        modelName = 'RV_Disc_D21.5mm_W8.4mm_P10mm',            # modelName
        D = 21.5,         # body length
        E = 8.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.9,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (10.0, 4.5)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W3.4mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 3.4mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W3.4mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W3.4mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 3.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W3.5mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 3.5mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W3.5mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W3.5mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 3.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W3.6mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 3.6mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W3.6mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W3.6mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 3.6,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.46667)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W3.7mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 3.7mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W3.7mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W3.7mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 3.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.65)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W3.8mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 3.8mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W3.8mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W3.8mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 3.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W3.9mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 3.9mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W3.9mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W3.9mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 3.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W4.2mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 4.2mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W4.2mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W4.2mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 4.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W4.3mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 4.3mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W4.3mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W4.3mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 4.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W4.5mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 4.5mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W4.5mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W4.5mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 4.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.1)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W4.8mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 4.8mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W4.8mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W4.8mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 4.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W4mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 4mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W4mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W4mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W5.1mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 5.1mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W5.1mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W5.1mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 5.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.5)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W5.4mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 5.4mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W5.4mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W5.4mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 5.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W5.5mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 5.5mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W5.5mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W5.5mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 5.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D7mm_W5.7mm_P5mm': Params(
        #
        # Varistor, diameter 7mm, width 5.7mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D7mm_W5.7mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D7mm_W5.7mm_P5mm',            # modelName
        D = 7.0,         # body length
        E = 5.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 3.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W3.3mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 3.3mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W3.3mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W3.3mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 3.3,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.2)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W3.4mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 3.4mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W3.4mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W3.4mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 3.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.25)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W3.5mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 3.5mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W3.5mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W3.5mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 3.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W3.6mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 3.6mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W3.6mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W3.6mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 3.6,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.4)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W3.7mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 3.7mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W3.7mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W3.7mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 3.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.5)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W3.8mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 3.8mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W3.8mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W3.8mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 3.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W3.9mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 3.9mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W3.9mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W3.9mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 3.9,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.6)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W4.1mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 4.1mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W4.1mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W4.1mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 4.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W4.2mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 4.2mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W4.2mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W4.2mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 4.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W4.4mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 4.4mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W4.4mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W4.4mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 4.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W4.5mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 4.5mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W4.5mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W4.5mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 4.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.1)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W4.8mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 4.8mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W4.8mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W4.8mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 4.8,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.3)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W4mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 4mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W4mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W4mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 4.0,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.9)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W5.2mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 5.2mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W5.2mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W5.2mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 5.2,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.5)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W5.4mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 5.4mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W5.4mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W5.4mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 5.4,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W5.5mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 5.5mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W5.5mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W5.5mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 5.5,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 2.8)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W5.7mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 5.7mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W5.7mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W5.7mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 5.7,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.54,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 3.0)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

    'RV_Disc_D9mm_W6.1mm_P5mm': Params(
        #
        # Varistor, diameter 9mm, width 6.1mm, pitch 5mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A2
        # 
        # The foot print that uses this 3D model is RV_Disc_D9mm_W6.1mm_P5mm.kicad_mod
        # 
        modelName = 'RV_Disc_D9mm_W6.1mm_P5mm',            # modelName
        D = 9.0,         # body length
        E = 6.1,          # body overall width
        A1 = 0.03,         # body-board separation
        b = 0.63,          # pin width
        ph = 3.0,          # pin length
        pin = [(0.0, 0.0), (5.0, 1.5)],          # Pins
        pintype = 'tht',          # Pin type, 'tht', 'smd'
        serie = 'RV_Disc',        # 
        body_color_key = 'blue body',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '../Varistor.3dshapes',      # destination directory
        ),

}


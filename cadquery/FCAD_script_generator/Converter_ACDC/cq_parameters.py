
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

destination_dir="/Converter_DCDC.3dshapes"
# destination_dir="./"
old_footprints_dir="Converter_DCDC.pretty"
footprints_dir="Converter_DCDC.pretty"
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
	'roundbelly',		# If belly of caseing should be round (or flat)
	'L',				# package length
	'W',			   	# package width
	'H',				# package height
	'rim',				# If a rim should be added to the belly
	'pinpadsize',		# pin diameter or pad size
	'pinpadh',			# pin length, pad height
	'pintype',			# Casing type
	'rotation',			# Rotation if required
	'pin1corner',		# Left upp corner relationsship to pin 1
	'pin',				# pin pitch
	'A1',				# package board seperation
	'corner',			# If top should be cut
	'show_top',			# If top should be visible or not
	'body_color_key',	# Body colour
	'body_top_color_key',	# Body top colour
	'pin_color_key',	# Pin colour
	'dest_dir_prefix'	# Destination directory
])

all_params = {
    
    'Converter_ACDC_Hahn_HS-400xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_Hahn_HS-400xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 32.8,  # Package length
        W  = 27.8,  # Package width
        H  = 25.8,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (20.0, 0.0), (15.0, 20.0), (5.0, 20.0)),  # Pin placement
        pin1corner = (-6.4, -3.9),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_MeanWell_IRM-02-xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell_IRM-02-xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 33.7,  # Package length
        W  = 22.2,  # Package width
        H  = 15.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 15.2), (28.0, 0.0), (28.0, 7.6)),  # Pin placement
        pin1corner = (-2.85, -3.5),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 0.6,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_MeanWell_IRM-02-xx_SMD': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell_IRM-02-xx_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 22.2,  # Package length
        W  = 33.7,  # Package width
        H  = 16.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((-13.2, -13.97), (-13.2, -8.89), (-13.2, -3.81), (-13.2, 6.35), (-13.2, 8.89), (-13.2, 11.43), (-13.2, 13.97), (13.2, -13.97), (13.2, -8.89), (13.2, -3.81), (13.2, 6.35), (13.2, 8.89), (13.2, 11.43), (13.2, 13.97)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 0.4,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_MeanWell_IRM-03-xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell_IRM-03-xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 24.0,  # Package length
        W  = 37.0,  # Package width
        H  = 15.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 5.08), (0.0, 30.48), (17.78, 30.48), (17.78, 25.4)),  # Pin placement
        pin1corner = (-3.11, -3.26),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 0.6,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_MeanWell_IRM-03-xx_SMD': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell_IRM-03-xx_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 24.0,  # Package length
        W  = 37.0,  # Package width
        H  = 16.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((-14.45, -15.24), (-14.45, -10.16), (-14.45, -5.08), (-14.45, 7.62), (-14.45, 10.16), (-14.45, 12.7), (-14.45, 15.24), (14.45, -15.24), (14.45, -10.16), (14.45, -5.08), (14.45, 7.62), (14.45, 10.16), (14.45, 12.7), (14.45, 15.24)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 0.4,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_MeanWell_IRM-20-xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell_IRM-20-xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 52.4,  # Package length
        W  = 27.2,  # Package width
        H  = 24.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 20.8), (45.0, 20.8), (45.0, 12.8)),  # Pin placement
        pin1corner = (-3.4, -3.2),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 1.04,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_Vigortronix_VTX-214-010-xxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_Vigortronix_VTX-214-010-xxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 36.0,  # Package length
        W  = 56.0,  # Package width
        H  = 25.5,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (12.0, 0.0), (0.0, 48.0), (5.0, 48.0)),  # Pin placement
        pin1corner = (-12.0, -4.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'orange body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_Vigortronix_VTX-214-015-1xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_Vigortronix_VTX-214-015-1xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 55.0,  # Package length
        W  = 45.0,  # Package width
        H  = 24.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 17.5), (0.0, 35.0), (47.0, 27.5), (47.0, 7.5)),  # Pin placement
        pin1corner = (-4.0, -4.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 5.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'orange body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_TRACO_TMLM-04_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMLM-04_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 36.5,  # Package length
        W  = 27.0,  # Package width
        H  = 17.1,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (21.5, 0.0), (25.25, 0.0), (29.0, 0.0), (29.0, 21.0), (21.5, 21.0), (0.0, 21.0)),  # Pin placement
        pin1corner = (-3.75, -3.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.0,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_TRACO_TMLM-05_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMLM-05_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 50.08,  # Package length
        W  = 25.4,  # Package width
        H  = 15.16,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 10.16), (45.72, 10.16), (45.72, -10.16)),  # Pin placement
        pin1corner = (-2.54, -12.26),  # Left upp corner relationsship to pin 1
        pinpadh    = 8.0,  # Pin length, pad height
        pinpadsize = 1.04,  # Pin diameter or pad size
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_TRACO_TMLM-10-20_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMLM-10-20_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 52.4,  # Package length
        W  = 27.2,  # Package width
        H  = 23.5,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 10.16), (45.72, 10.16), (45.72, -10.16)),  # Pin placement
        pin1corner = (-2.54, -12.26),  # Left upp corner relationsship to pin 1
        pinpadh    = 8.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_RECOM_RAC04-xxSGx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_RECOM_RAC04-xxSGx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 24.0,  # Package length
        W  = 37.0,  # Package width
        H  = 15.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0, 5.08), (0, 30.48), (17.78, 30.48), (17.78, 25.4)),  # Pin placement
        pin1corner = (-3.11, -3.26),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 0.6,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_HiLink_HLK-PMxx': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_HiLink_HLK-PMxx',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 34.0,  # Package length
        W  = 20.2,  # Package width
        H  = 15.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0, -5.0), (29.4, -10.2), (29.4, 5.2)),  # Pin placement
        pin1corner = (-2.3, -12.6),  # Left upp corner relationsship to pin 1
        pinpadh    = 5.0,  # Pin length, pad height
        pinpadsize = 0.9,  # Pin diameter or pad size
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),
}


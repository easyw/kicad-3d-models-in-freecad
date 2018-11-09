
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
    
    'Converter_DCDC_Cincon_EC5BExx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC5BExx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (12.7, 20.32)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Cincon_EC5BExx_Dual_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC5BExx_Dual_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (12.7, 20.32), (2.54, 20.32), (12.7, 0.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Cincon_EC6Cxx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC6Cxx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 50.8,  # Package length
        W  = 50.8,  # Package width
        H  = 24.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 15.24), (0.0, 22.86), (45.72, 5.08), (45.72, 15.24), (45.72, 25.4)),  # Pin placement
        pin1corner = (-2.54, -5.08),  # Left upp corner relationsship to pin 1
        pinpadh    = 5.6,  # Pin length, pad height
        pinpadsize = 1.02,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Cincon_EC6Cxx_Dual-Triple_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC6Cxx_Dual-Triple_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 50.8,  # Package length
        W  = 50.8,  # Package width
        H  = 24.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 15.24), (0.0, 22.86), (45.72, 5.08), (45.72, 15.24), (45.72, 25.4), (45.72, 35.56)),  # Pin placement
        pin1corner = (-2.54, -5.08),  # Left upp corner relationsship to pin 1
        pinpadh    = 5.6,  # Pin length, pad height
        pinpadsize = 1.02,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Bothhand_CFUSxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Bothhand_CFUSxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 16.8,  # Package length
        W  = 32.6,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 22.86), (0.0, 25.4), (0.0, 27.94), (15.24, 27.94), (15.24, 25.4), (15.24, 22.86), (15.24, 0.0)),  # Pin placement
        pin1corner = (-0.78, -2.65),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Bothhand_CFUSxxxxEH_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Bothhand_CFUSxxxxEH_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 16.8,  # Package length
        W  = 32.6,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 22.86), (0.0, 25.4), (0.0, 27.94), (15.24, 27.94), (15.24, 25.4), (15.24, 22.86), (15.24, 5.08), (15.24, 0.0)),  # Pin placement
        pin1corner = (-0.78, -2.65),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Bothhand_CFUDxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Bothhand_CFUDxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 16.8,  # Package length
        W  = 32.6,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 22.86), (0.0, 25.4), (0.0, 27.94), (15.24, 27.94), (15.24, 25.4), (15.24, 22.86), (15.24, 17.78), (15.24, 12.7), (15.24, 0.0)),  # Pin placement
        pin1corner = (-0.78, -2.65),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.5,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_MeanWell_NID30_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_MeanWell_NID30_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 10.7,  # Package length
        W  = 50.8,  # Package width
        H  = 13.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 2.54), (0.0, 5.08), (0.0, 7.62), (0.0, 10.16), (0.0, 35.56), (0.0, 38.1), (0.0, 40.64), (0.0, 43.18), (0.0, 45.72), (0.0, 48.26)),  # Pin placement
        pin1corner = (-4.0, -0.92),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.5,  # Pin length, pad height
        pinpadsize = 0.64,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_MeanWell_NID60_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_MeanWell_NID60_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 10.7,  # Package length
        W  = 50.8,  # Package width
        H  = 26.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 2.54), (0.0, 5.08), (0.0, 7.62), (0.0, 10.16), (0.0, 35.56), (0.0, 38.1), (0.0, 40.64), (0.0, 43.18), (0.0, 45.72), (0.0, 48.26)),  # Pin placement
        pin1corner = (-4.0, -1.2),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.5,  # Pin length, pad height
        pinpadsize = 0.64,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Murata_NCS1SxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_NCS1SxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 21.87,  # Package length
        W  = 8.2,  # Package width
        H  = 11.3,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0), (12.7, 0.0), (15.24, 0.0)),  # Pin placement
        pin1corner = (-2.27, -3.195),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_muRata_CRE1xxxxxx3C_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_muRata_CRE1xxxxxx3C_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 6.1,  # Package length
        W  = 11.53,  # Package width
        H  = 7.62,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 2.54), (0.0, 5.08), (0.0, 7.62)),  # Pin placement
        pin1corner = (-1.25, -2.07),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_muRata_CRE1xxxxxxDC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_muRata_CRE1xxxxxxDC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 9.9,  # Package length
        W  = 11.6,  # Package width
        H  = 6.9,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 7.62), (7.62, 7.62), (7.62, 2.54)),  # Pin placement
        pin1corner = (-1.3, -2.1),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_muRata_CRE1xxxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_muRata_CRE1xxxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 6.1,  # Package length
        W  = 11.53,  # Package width
        H  = 10.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 2.54), (0.0, 5.08), (0.0, 7.62)),  # Pin placement
        pin1corner = (-1.25, -2.07),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_muRata_NMAxxxxDC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_muRata_NMAxxxxDC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 9.8,  # Package length
        W  = 19.5,  # Package width
        H  = 6.8,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 15.24), (7.62, 15.24), (7.62, 12.7), (7.62, 7.62), (7.62, 0.0)),  # Pin placement
        pin1corner = (-1.22, -2.23),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_muRata_NMAxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_muRata_NMAxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 6.0,  # Package length
        W  = 19.5,  # Package width
        H  = 10.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 2.54), (0.0, 7.62), (0.0, 10.16), (0.0, 12.7)),  # Pin placement
        pin1corner = (-4.77, -2.03),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_muRata_NXE2SxxxxMC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_muRata_NXE2SxxxxMC_THT',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 10.41,  # Package length
        W  = 12.7,  # Package width
        H  = 4.41,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((-4.7, -3.81), (-4.7, -1.27), (-4.7, 3.81), (4.7, 3.81), (4.7, -3.81)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 0.2,  # Pin length, pad height
        pinpadsize = 0.61,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_RECOM_R-78B-2.0_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78B-2.0_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 11.5,  # Package length
        W  = 8.5,  # Package width
        H  = 17.5,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0)),  # Pin placement
        pin1corner = (-3.21, -2.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.64,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_RECOM_R-78E-0.5_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78E-0.5_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 11.6,  # Package length
        W  = 8.5,  # Package width
        H  = 10.4,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0)),  # Pin placement
        pin1corner = (-3.31, -6.5),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_RECOM_R-78HB-0.5_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78HB-0.5_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 11.5,  # Package length
        W  = 8.5,  # Package width
        H  = 17.5,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0)),  # Pin placement
        pin1corner = (-3.21, -2.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.7,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_RECOM_R-78S-0.1_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78S-0.1_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 11.6,  # Package length
        W  = 8.5,  # Package width
        H  = 10.4,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0), (7.62, 0.0)),  # Pin placement
        pin1corner = (-2.0, -6.5),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.7,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_RECOM_R-78HB-0.5L_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78HB-0.5L_THT',  # Model name
        pintype   = 'tht_n',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 11.5,  # Package length
        W  = 17.5,  # Package width
        H  = 8.5,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0)),  # Pin placement
        pin1corner = (-3.21, -19.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.7,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_RECOM_R5xxxDA_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R5xxxDA_THT',  # Model name
        pintype   = 'tht_n',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 32.2,  # Package length
        W  = 15.0,  # Package width
        H  = 9.1,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0), (7.62, 0.0), (10.16, 0.0), (12.7, 0.0), (15.24, 0.0), (17.78, 0.0), (20.32, 0.0), (22.86, 0.0), (25.4, 0.0), (27.94, 0.0)),  # Pin placement
        pin1corner = (-2.1, -17.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.1,  # Pin length, pad height
        pinpadsize = 0.7,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_RECOM_R5xxxPA_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R5xxxPA_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 32.2,  # Package length
        W  = 9.1,  # Package width
        H  = 15.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0), (7.62, 0.0), (10.16, 0.0), (12.7, 0.0), (15.24, 0.0), (17.78, 0.0), (20.32, 0.0), (22.86, 0.0), (25.4, 0.0), (27.94, 0.0)),  # Pin placement
        pin1corner = (-2.1, -0.8),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.0,  # Pin length, pad height
        pinpadsize = 0.7,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMR-1SM_SMD': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR-1SM_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 13.7,  # Package length
        W  = 18.9,  # Package width
        H  = 8.45,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((-8.075, -7.62), (-8.075, -5.08), (-8.075, 5.08), (-8.075, 7.62), (8.075, -7.62), (8.075, 5.08), (8.075, 7.62)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left upp corner relationsship to pin 1
        pinpadh    = 0.2,  # Pin length, pad height
        pinpadsize = 1.2,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMR-1-xxxx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR-1-xxxx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 17.0,  # Package length
        W  = 7.62,  # Package width
        H  = 11.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (7.62, 0.0), (12.7, 0.0)),  # Pin placement
        pin1corner = (-2.3, -2.5),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.2,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMR-1-xxxx_Dual_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR-1-xxxx_Dual_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 17.0,  # Package length
        W  = 7.62,  # Package width
        H  = 11.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (7.62, 0.0), (10.16, 0.0), (12.7, 0.0)),  # Pin placement
        pin1corner = (-2.3, -2.5),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.2,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMR-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 21.8,  # Package length
        W  = 9.2,  # Package width
        H  = 11.0,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0), (10.16, 0.0), (12.7, 0.0), (15.24, 0.0), (17.78, 0.0)),  # Pin placement
        pin1corner = (-2.0, -3.2),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.0,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TSR-1_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSR-1_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 11.7,  # Package length
        W  = 7.6,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (2.54, 0.0), (5.08, 0.0)),  # Pin placement
        pin1corner = (-3.3, -5.6),  # Left upp corner relationsship to pin 1
        pinpadh    = 4.0,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'red body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEN10-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN10-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (12.7, 20.32)),  # Pin placement
        pin1corner = (-10.12, -15.2),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEN10-xxxx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN10-xxxx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (12.7, 20.32)),  # Pin placement
        pin1corner = (-10.12, -15.2),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEN10-xxxx_Dual_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN10-xxxx_Dual_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (2.54, 20.32), (12.7, 20.32)),  # Pin placement
        pin1corner = (-10.12, -15.2),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEN20-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (2.54, 20.32), (12.7, 20.32), (12.7, 0.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEN20-xxxx-N4_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx-N4_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (12.7, 20.32), (12.7, 0.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEN20-xxxx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (12.7, 20.32), (12.7, 0.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEN20-xxxx_Dual_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx_Dual_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (5.08, 0.0), (-7.62, 20.32), (2.54, 20.32), (12.7, 20.32), (12.7, 0.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        pinpadh    = 6.0,  # Pin length, pad height
        pinpadsize = 1.0,  # Pin diameter or pad size
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_XP_POWER_JTExxxxDxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER_JTExxxxDxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 20.32,  # Package length
        W  = 31.75,  # Package width
        H  = 10.4,  # Package height
        A1 = 0.1,  # Package board seperation
        pin = ((0.0, 0.0), (0.0, 17.78), (0.0, 22.86), (15.24, 22.86), (15.24, 17.78), (15.24, 0.0), (0.0, 2.54), (15.24, 2.54)),  # Pin placement
        pin1corner = (-2.54, -4.445),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.05,  # Pin length, pad height
        pinpadsize = 0.5,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = '../Converter_DCDC.3dshapes'  # Destination directory
        ),

}


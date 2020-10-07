
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

class LICENCE_Info():

    ############################################################################
    # Licence information of the generated models.
    #################################################################################################
    STR_licAuthor = "kicad StepUp"
    STR_licEmail = "ksu"
    STR_licOrgSys = "kicad StepUp"
    STR_licPreProc = "OCC"
    STR_licOrg = "FreeCAD"
    LIST_license = ["",]

import collections
from collections import namedtuple

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
    'modelName',        #modelName
    'roundbelly',       # If belly of caseing should be round (or flat)
    'L',                # package length
    'W',                # package width
    'H',                # package height
    'rim',              # If a rim should be added to the belly
    'pinpadsize',       # pin diameter or pad size
    'pinpadh',          # pin length, pad height
    'pintype',          # Casing type
    'rotation',         # Rotation if required
    'pin1corner',       # Left upp corner relationsship to pin 1
    'pin',              # pin pitch
    'A1',               # package board separation
    'corner',           # If top should be cut
    'show_top',         # If top should be visible or not
    'body_color_key',   # Body colour
    'body_top_color_key',   # Body top colour
    'pin_color_key',    # Pin colour
    'dest_dir_prefix'   # Destination directory
])

p = 2.54                # no typo error
pm= 2
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',20.0, 0.0, 1.0, 3.5), ('round',15.0, 20.0, 1.0, 3.5), ('round',5.0, 20.0,  1.0, 3.5)),  # Pin placement
        pin1corner = (-6.4, -3.9),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',0.0, 15.2, 1.0, 3.5), ('round',28.0, 0.0, 1.0, 3.5), ('round',28.0, 7.6, 1.0, 3.5)),  # Pin placement
        pin1corner = (-2.85, -3.5),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('smd',-13.2, -13.97, 1.0, 0.4), ('smd',-13.2, -8.89, 1.0, 0.4), ('smd',-13.2, -3.81, 1.0, 0.4), ('smd',-13.2, 6.35, 1.0, 0.4), ('smd',-13.2, 8.89, 1.0, 0.4),\
               ('smd',-13.2, 11.43, 1.0, 0.4), ('smd',-13.2, 13.97, 1.0, 0.4), ('smd',13.2, -13.97, 1.0, 0.4), ('smd',13.2, -8.89, 1.0, 0.4), ('smd',13.2, -3.81, 1.0, 0.4),\
               ('smd',13.2, 6.35, 1.0, 0.4), ('smd',13.2, 8.89, 1.0, 0.4), ('smd',13.2, 11.43, 1.0, 0.4), ('smd',13.2, 13.97, 1.0, 0.4)),  # Pin placement
        pin1corner = (1.0, 3.5),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 3.5), ('round', 0.0, 5.08, 1.0, 3.5), ('round', 0.0, 30.48, 1.0, 3.5), ('round', 17.78, 30.48, 1.0, 3.5), ('round', 17.78, 25.4, 1.0, 3.5)),  # Pin placement
        pin1corner = (-3.11, -3.26),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('smd',-14.45, -15.24, 1.0, 0.4), ('smd',-14.45, -10.16, 1.0, 0.4), ('smd',-14.45, -5.08, 1.0, 0.4), ('smd',-14.45, 7.62, 1.0, 0.4), ('smd',-14.45, 10.16, 1.0, 0.4),
               ('smd',-14.45, 12.7, 1.0, 0.4), ('smd',-14.45, 15.24, 1.0, 0.4), ('smd',14.45, -15.24, 1.0, 0.4), ('smd',14.45, -10.16, 1.0, 0.4), ('smd',14.45, -5.08, 1.0, 0.4),
               ('smd',14.45, 7.62, 1.0, 0.4), ('smd',14.45, 10.16, 1.0, 0.4), ('smd',14.45, 12.7, 1.0, 0.4), ('smd',14.45, 15.24, 1.0, 0.4)),  # Pin placement
        pin1corner = (1.0, 3.5),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',0.0, 20.8, 1.0, 3.5), ('round',45.0, 20.8, 1.0, 3.5), ('round',45.0, 12.8, 1.0, 3.5)),  # Pin placement
        pin1corner = (-3.4, -3.2),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',12.0, 0.0, 1.0, 3.5), ('round',0.0, 48.0, 1.0, 3.5), ('round',5.0, 48.0, 1.0, 3.5)),  # Pin placement
        pin1corner = (-12.0, -4.0),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'orange body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',0.0, 17.5, 1.0, 3.5), ('round',0.0, 35.0, 1.0, 3.5), ('round',47.0, 27.5, 1.0, 3.5), ('round',47.0, 7.5, 1.0, 3.5)),  # Pin placement
        pin1corner = (-4.0, -4.0),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'orange body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',21.5, 0.0, 1.0, 3.5), ('round',25.25, 0.0, 1.0, 3.5), ('round',29.0, 0.0, 1.0, 3.5), ('round',29.0, 21.0, 1.0, 3.5), ('round',21.5, 21.0, 1.0, 3.5), ('round',0.0, 21.0, 1.0, 3.5)),  # Pin placement
        pin1corner = (-3.75, -3.0),  # Left upp corner relationsship to pin 1
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),


    'Converter_ACDC_TRACO_TMLM-05_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMLM-05_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 50.08, # Package length
        W  = 25.4,  # Package width
        H  = 15.16, # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',0.0, 10.16, 1.0, 3.5), ('round',45.72, 10.16, 1.0, 3.5), ('round',45.72, -10.16, 1.0, 3.5)),  # Pin placement
        pin1corner = (-2.54, -12.26),  # Left upp corner relationsship to pin 1
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',0.0, 10.16, 1.0, 3.5), ('round',45.72, 10.16, 1.0, 3.5), ('round',45.72, -10.16, 1.0, 3.5)),  # Pin placement
        pin1corner = (-2.54, -12.26),  # Left upp corner relationsship to pin 1
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
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
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 3.5), ('round', 0, 5.08, 1.0, 3.5), ('round', 0, 30.48, 1.0, 3.5), ('round', 17.78, 30.48, 1.0, 3.5), ('round', 17.78, 25.4, 1.0, 3.5)),  # Pin placement
        pin1corner = (-3.11, -3.26),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_HiLink_HLK-PMxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_HiLink_HLK-PMxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 34.0,  # Package length
        W  = 20.2,  # Package width
        H  = 15.0,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5), ('round',0, 5.0, 1.0, 3.5), ('round',29.4, 10.2, 1.0, 3.5), ('round',29.4, -5.2, 1.0, 3.5)),  # Pin placement
        pin1corner = (-2.3, -7.5),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Cincon_EC5BExx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC5BExx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 3.5), ('round', 5.08, 0.0, 1.0, 3.5), ('round', -7.62, 20.32, 1.0, 3.5), ('round', 12.7, 20.32, 1.0, 3.5)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_Cincon_EC5BExx_Dual_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC5BExx_Dual_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 3.5), ('round', 5.08, 0.0, 1.0, 3.5), ('round', -7.62, 20.32, 1.0, 3.5), ('round', 12.7, 20.32, 1.0, 3.5), ('round', 2.54, 20.32, 1.0, 3.5), ('round', 12.7, 0.0, 1.0, 3.5)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Cincon_EC6Cxx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC6Cxx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 50.8,  # Package length
        W  = 50.8,  # Package width
        H  = 24.0,  # Package height
        A1 = 0.1,   # Package board separation
        pin = (('round', 0.0, 0.0, 1.02, 5.6), ('round', 0.0, 15.24, 1.02, 5.6), ('round', 0.0, 22.86, 1.02, 5.6), ('round', 45.72, 5.08, 1.02, 5.6), ('round', 45.72, 15.24, 1.02, 5.6), ('round', 45.72, 25.4, 1.02, 5.6)),  # Pin placement
        pin1corner = (-2.54, -5.08),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Cincon_EC6Cxx_Dual-Triple_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Cincon_EC6Cxx_Dual-Triple_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 50.8,  # Package length
        W  = 50.8,  # Package width
        H  = 24.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.02, 5.6), ('round', 0.0, 15.24, 1.02, 5.6), ('round', 0.0, 22.86, 1.02, 5.6), ('round', 45.72, 5.08, 1.02, 5.6), ('round', 45.72, 15.24, 1.02, 5.6), ('round', 45.72, 25.4, 1.02, 5.6), ('round', 45.72, 35.56, 1.02, 5.6)),  # Pin placement
        pin1corner = (-2.54, -5.08),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Bothhand_CFUSxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Bothhand_CFUSxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 16.8,  # Package length
        W  = 32.6,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 3.5), ('round', 0.0, 22.86, 0.5, 3.5), ('round', 0.0, 25.4, 0.5, 3.5), ('round', 0.0, 27.94, 0.5, 3.5), ('round', 15.24, 27.94, 0.5, 3.5), ('round', 15.24, 25.4, 0.5, 3.5), ('round', 15.24, 22.86, 0.5, 3.5), ('round', 15.24, 0.0, 0.5, 3.5)),  # Pin placement
        pin1corner = (-0.78, -2.65),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Bothhand_CFUSxxxxEH_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Bothhand_CFUSxxxxEH_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 16.8,  # Package length
        W  = 32.6,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 3.5), ('round', 0.0, 22.86, 0.5, 3.5), ('round', 0.0, 25.4, 0.5, 3.5), ('round', 0.0, 27.94, 0.5, 3.5), ('round', 15.24, 27.94, 0.5, 3.5), ('round', 15.24, 25.4, 0.5, 3.5), ('round', 15.24, 22.86, 0.5, 3.5), ('round', 15.24, 5.08, 0.5, 3.5), ('round', 15.24, 0.0, 0.5, 3.5)),  # Pin placement
        pin1corner = (-0.78, -2.65),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Bothhand_CFUDxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Bothhand_CFUDxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 16.8,  # Package length
        W  = 32.6,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 3.5), ('round', 0.0, 22.86, 0.5, 3.5), ('round', 0.0, 25.4, 0.5, 3.5), ('round', 0.0, 27.94, 0.5, 3.5), ('round', 15.24, 27.94, 0.5, 3.5), ('round', 15.24, 25.4, 0.5, 3.5), ('round', 15.24, 22.86, 0.5, 3.5), ('round', 15.24, 17.78, 0.5, 3.5), ('round', 15.24, 12.7, 0.5, 3.5), ('round', 15.24, 0.0, 0.5, 3.5)),  # Pin placement
        pin1corner = (-0.78, -2.65),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_MeanWell_NID30_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_MeanWell_NID30_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 10.7,  # Package length
        W  = 50.8,  # Package width
        H  = 13.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.64, 4.5), ('round', 0.0, 2.54, 0.64, 4.5), ('round', 0.0, 5.08, 0.64, 4.5), ('round', 0.0, 7.62, 0.64, 4.5), ('round', 0.0, 10.16, 0.64, 4.5), ('round', 0.0, 35.56, 0.64, 4.5), ('round', 0.0, 38.1, 0.64, 4.5), ('round', 0.0, 40.64, 0.64, 4.5), ('round', 0.0, 43.18, 0.64, 4.5), ('round', 0.0, 45.72, 0.64, 4.5), ('round', 0.0, 48.26, 0.64, 4.5)),  # Pin placement
        pin1corner = (-4.0, -0.92),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_MeanWell_NID60_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_MeanWell_NID60_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 10.7,  # Package length
        W  = 50.8,  # Package width
        H  = 26.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.64, 4.5), ('round', 0.0, 2.54, 0.64, 4.5), ('round', 0.0, 5.08, 0.64, 4.5), ('round', 0.0, 7.62, 0.64, 4.5), ('round', 0.0, 10.16, 0.64, 4.5), ('round', 0.0, 35.56, 0.64, 4.5), ('round', 0.0, 38.1, 0.64, 4.5), ('round', 0.0, 40.64, 0.64, 4.5), ('round', 0.0, 43.18, 0.64, 4.5), ('round', 0.0, 45.72, 0.64, 4.5), ('round', 0.0, 48.26, 0.64, 4.5)),  # Pin placement
        pin1corner = (-4.0, -1.2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_MEE1SxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_MEE1SxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.53, # Package length
        W  = 6.1,   # Package width
        H  = 10.0,  # Package height
        A1 = 0.02,  # Package board separation
        rim = (0.4, 0.4, 0.4), # No rim
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1), ('rect', 2.54, 0.0, 0.5, 0.25, 4.1), ('rect', 5.08, 0.0, 0.5, 0.25, 4.1), ('rect', 7.62, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-2.08, -4.97),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = -90,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_MEE3SxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_MEE3SxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 14.15, # Package length
        W  = 8.15,  # Package width
        H  = 10.15, # Package height
        A1 = 0.02,  # Package board separation
        rim = (0.4, 0.4, 0.4), # No rim
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1), ('rect', 2.54, 0.0, 0.5, 0.25, 4.1), ('rect', 5.08, 0.0, 0.5, 0.25, 4.1), ('rect', 7.62, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-3.265, -6.925),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = -90,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_NCS1SxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_NCS1SxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.87, # Package length
        W  = 8.2,   # Package width
        H  = 11.3,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 4.1), ('round', 2.54, 0.0, 0.5, 4.1), ('round', 5.08, 0.0, 0.5, 4.1), ('round', 12.7, 0.0, 0.5, 4.1), ('round', 15.24, 0.0, 0.5, 4.1)),  # Pin placement
        pin1corner = (-2.27, -3.195),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_CRE1xxxxxx3C_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_CRE1xxxxxx3C_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 6.1,   # Package length
        W  = 11.53, # Package width
        H  = 7.62,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 4.1), ('round', 0.0, 2.54, 0.5, 4.1), ('round', 0.0, 5.08, 0.5, 4.1), ('round', 0.0, 7.62, 0.5, 4.1)),  # Pin placement
        pin1corner = (-1.25, -2.07),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_CRE1xxxxxxDC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_CRE1xxxxxxDC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 9.9,   # Package length
        W  = 11.6,  # Package width
        H  = 6.9,   # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 4.1), ('round', 0.0, 7.62, 0.5, 4.1), ('round', 7.62, 7.62, 0.5, 4.1), ('round', 7.62, 2.54, 0.5, 4.1)),  # Pin placement
        pin1corner = (-1.3, -2.1),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_CRE1xxxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_CRE1xxxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 6.1,   # Package length
        W  = 11.53, # Package width
        H  = 10.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 4.1), ('round', 0.0, 2.54, 0.5, 4.1), ('round', 0.0, 5.08, 0.5, 4.1), ('round', 0.0, 7.62, 0.5, 4.1)),  # Pin placement
        pin1corner = (-1.25, -2.07),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_NMAxxxxDC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_NMAxxxxDC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 9.8,   # Package length
        W  = 19.5,  # Package width
        H  = 6.8,   # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 4.1), ('round', 0.0, 15.24, 0.5, 4.1), ('round', 7.62, 15.24, 0.5, 4.1), ('round', 7.62, 12.7, 0.5, 4.1), ('round', 7.62, 7.62, 0.5, 4.1), ('round', 7.62, 0.0, 0.5, 4.1)),  # Pin placement
        pin1corner = (-1.22, -2.23),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_NMAxxxxSC_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_NMAxxxxSC_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 6.0,   # Package length
        W  = 19.5,  # Package width
        H  = 10.0,  # Package height
        A1 = 0.1,   # Package board separation
        pin = (('round', 0.0, 0.0, 0.5, 4.1), ('round', 0.0, 2.54, 0.5, 4.1), ('round', 0.0, 7.62, 0.5, 4.1), ('round', 0.0, 10.16, 0.5, 4.1), ('round', 0.0, 12.7, 0.5, 4.1)),  # Pin placement
        pin1corner = (-4.77, -2.03),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_NXE2SxxxxMC_SMD': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Murata_NXE2SxxxxMC_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd'
        L  = 10.41, # Package length
        W  = 12.7,  # Package width
        H  = 4.41,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('smd', -4.7, -3.81, 0.61, 0.2), ('smd', -4.7, -1.27, 0.61, 0.2), ('smd', -4.7, 3.81, 0.61, 0.2), ('smd', 4.7, 3.81, 0.61, 0.2), ('smd', 4.7, -3.81, 0.61, 0.2)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_R-78B-2.0_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78B-2.0_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.5,  # Package length
        W  = 8.5,   # Package width
        H  = 17.5,  # Package height
        rim = None, # No rim
        A1 = 0.1,   # Package board separation
        pin = (('round', 0.0, 0.0, 0.64, 4.1), ('round', 2.54, 0.0, 0.64, 4.1), ('round', 5.08, 0.0, 0.64, 4.1)),  # Pin placement
        pin1corner = (-3.21, -2.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_R-78E-0.5_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78E-0.5_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.6,  # Package length
        W  = 8.5,   # Package width
        H  = 10.4,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 4.1), ('round', 2.54, 0.0, 0.5, 4.1), ('round', 5.08, 0.0, 0.5, 4.1)),  # Pin placement
        pin1corner = (-3.31, -6.5),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_R-78HB-0.5_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78HB-0.5_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.5,  # Package length
        W  = 8.5,   # Package width
        H  = 17.5,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.7, 4.1), ('round', 2.54, 0.0, 0.7, 4.1), ('round', 5.08, 0.0, 0.7, 4.1)),  # Pin placement
        pin1corner = (-3.21, -2.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_R-78S-0.1_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78S-0.1_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.6,  # Package length
        W  = 8.5,   # Package width
        H  = 10.4,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.7, 4.1), ('round', 2.54, 0.0, 0.7, 4.1), ('round', 5.08, 0.0, 0.7, 4.1), ('round', 7.62, 0.0, 0.7, 4.1)),  # Pin placement
        pin1corner = (-2.0, -6.5),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_R-78HB-0.5L_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R-78HB-0.5L_THT',  # Model name
        pintype   = 'tht_n',  # Pin type, 'tht', 'smd'
        L  = 11.5,  # Package length
        W  = 17.5,  # Package width
        H  = 8.5,   # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.7, 4.1), ('round', 2.54, 0.0, 0.7, 4.1), ('round', 5.08, 0.0, 0.7, 4.1)),  # Pin placement
        pin1corner = (-3.21, -19.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_R5xxxDA_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R5xxxDA_THT',  # Model name
        pintype   = 'tht_n',  # Pin type, 'tht', 'smd'
        L  = 32.2,  # Package length
        W  = 15.0,  # Package width
        H  = 9.1,   # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.7, 4.1), ('round', 2.54, 0.0, 0.7, 4.1), ('round', 5.08, 0.0, 0.7, 4.1), ('round', 7.62, 0.0, 0.7, 4.1), ('round', 10.16, 0.0, 0.7, 4.1), ('round', 12.7, 0.0, 0.7, 4.1), ('round', 15.24, 0.0, 0.7, 4.1), ('round', 17.78, 0.0, 0.7, 4.1), ('round', 20.32, 0.0, 0.7, 4.1), ('round', 22.86, 0.0, 0.7, 4.1), ('round', 25.4, 0.0, 0.7, 4.1), ('round', 27.94, 0.0, 0.7, 4.1)),  # Pin placement
        pin1corner = (-2.1, -17.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_R5xxxPA_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_R5xxxPA_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 32.2,  # Package length
        W  = 9.1,   # Package width
        H  = 15.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.7, 4.0), ('round', 2.54, 0.0, 0.7, 4.0), ('round', 5.08, 0.0, 0.7, 4.0), ('round', 7.62, 0.0, 0.7, 4.0), ('round', 10.16, 0.0, 0.7, 4.0), ('round', 12.7, 0.0, 0.7, 4.0), ('round', 15.24, 0.0, 0.7, 4.0), ('round', 17.78, 0.0, 0.7, 4.0), ('round', 20.32, 0.0, 0.7, 4.0), ('round', 22.86, 0.0, 0.7, 4.0), ('round', 25.4, 0.0, 0.7, 4.0), ('round', 27.94, 0.0, 0.7, 4.0)),  # Pin placement
        pin1corner = (-2.1, -0.8),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR-1SM_SMD': Params(   # ModelName
        #
        # reminder: for pintype='smd', (0,0) is the center of the device
        #
        modelName = 'Converter_DCDC_TRACO_TMR-1SM_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd'
        L  = 13.7,  # Package length
        W  = 18.9,  # Package width
        H  = 8.45,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('smd', -8.075, -3*p, 1.0, 0.4),
               ('smd', -8.075, -2*p, 1.0, 0.4),
               ('smd', -8.075,  2*p, 1.0, 0.4),
               ('smd', -8.075,  3*p, 1.0, 0.4),
               ('smd',  8.075, -3*p, 1.0, 0.4),
               ('smd',  8.075,  2*p, 1.0, 0.4),
               ('smd',  8.075,  3*p, 1.0, 0.4)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left up corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR1-xx1x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR1-xx1x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 17.0,  # Package length
        W  = 7.62,  # Package width
        H  = 11.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = (1, 3, 0.5), # No rim
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.15, -2.5+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR1-xx2x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR1-xx2x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 17.0,  # Package length
        W  = 7.62,  # Package width
        H  = 11.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = (1, 3, 0.5), # No rim
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, -2.5-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR-xxxx_THT': Params(   # ModelName   TRACO TMR 2
        #
        #  footprint silk with Y error size
        #
        modelName = 'Converter_DCDC_TRACO_TMR-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.2,    # Package width
        H  = 11.1,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.2/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.0)),  # Pin placement
        pin1corner = (-2.0, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TSR-1_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSR-1_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.7,  # Package length
        W  = 7.6,   # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 4.0), ('round', 2.54, 0.0, 0.5, 4.0), ('round', 5.08, 0.0, 0.5, 4.0)),  # Pin placement
        pin1corner = (-3.3, -5.6),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'red body',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEN10-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN10-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 6.0), ('round', 5.08, 0.0, 1.0, 6.0), ('round', -7.62, 20.32, 1.0, 6.0), ('round', 12.7, 20.32, 1.0, 6.0)),  # Pin placement
        pin1corner = (-10.12, -15.2),  # Left upp corner relationsship to pin 1
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEN10-xxxx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN10-xxxx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 6.0), ('round', 5.08, 0.0, 1.0, 6.0), ('round', -7.62, 20.32, 1.0, 6.0), ('round', 12.7, 20.32, 1.0, 6.0)),  # Pin placement
        pin1corner = (-10.12, -15.2),  # Left upp corner relationsship to pin 1
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEN10-xxxx_Dual_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN10-xxxx_Dual_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 6.0), ('round', 5.08, 0.0, 1.0, 6.0), ('round', -7.62, 20.32, 1.0, 6.0), ('round', 2.54, 20.32, 1.0, 6.0), ('round', 12.7, 20.32, 1.0, 6.0)),  # Pin placement
        pin1corner = (-10.12, -15.2),  # Left upp corner relationsship to pin 1
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEN20-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 6.0), ('round', 5.08, 0.0, 1.0, 6.0), ('round', -7.62, 20.32, 1.0, 6.0), ('round', 2.54, 20.32, 1.0, 6.0), ('round', 12.7, 20.32, 1.0, 6.0), ('round', 12.7, 0.0, 1.0, 6.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEN20-xxxx-N4_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx-N4_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 6.0), ('round', 5.08, 0.0, 1.0, 6.0), ('round', -7.62, 20.32, 1.0, 6.0), ('round', 12.7, 20.32, 1.0, 6.0), ('round', 12.7, 0.0, 1.0, 6.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEN20-xxxx_Single_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx_Single_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 6.0), ('round', 5.08, 0.0, 1.0, 6.0), ('round', -7.62, 20.32, 1.0, 6.0), ('round', 12.7, 20.32, 1.0, 6.0), ('round', 12.7, 0.0, 1.0, 6.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEN20-xxxx_Dual_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEN20-xxxx_Dual_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 50.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 1.0, 6.0), ('round', 5.08, 0.0, 1.0, 6.0), ('round', -7.62, 20.32, 1.0, 6.0), ('round', 2.54, 20.32, 1.0, 6.0), ('round', 12.7, 20.32, 1.0, 6.0), ('round', 12.7, 0.0, 1.0, 6.0)),  # Pin placement
        pin1corner = (-10.16, -15.24),  # Left upp corner relationsship to pin 1
        show_top   = True,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'metal grey pins',  # Body color
        body_top_color_key = 'red body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER_JTExxxxDxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER_JTExxxxDxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 20.32, # Package length
        W  = 31.75, # Package width
        H  = 10.4,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.5, 3.05), ('round', 0.0, 17.78, 0.5, 3.05), ('round', 0.0, 22.86, 0.5, 3.05), ('round', 15.24, 22.86, 0.5, 3.05), ('round', 15.24, 17.78, 0.5, 3.05), ('round', 15.24, 0.0, 0.5, 3.05), ('round', 0.0, 2.54, 0.5, 3.05), ('round', 15.24, 2.54, 0.5, 3.05)),  # Pin placement
        pin1corner = (-2.54, -4.445),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER_ISU02-Series_SMD': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER_ISU02-Series_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd'
        L  = 14.9,  # Package length
        W  = 19.0,  # Package width
        H  = 8.50,  # Package height
        A1 = 0.2,   # Package board separation
        rim = None, # No rim
        pin = (('smd', -8.075, -7.62, 1.2, 0.2), ('smd', -8.075, -5.08, 1.2, 0.2), ('smd', -8.075, 5.08, 1.2, 0.2), ('smd', -8.075, 7.62, 1.2, 0.2), ('smd', 8.075, -7.62, 1.2, 0.2), ('smd', 8.075, 5.08, 1.2, 0.2), ('smd', 8.075, 7.62, 1.2, 0.2)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Artesyn_ATA-Series_SMD': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_Artesyn_ATA-Series_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd'
        L  = 13.7,  # Package length
        W  = 24.0,  # Package width
        H  = 8.0,   # Package height
        A1 = 0.25,  # Package board separation
        rim = None, # No rim
        pin = (('smd', -8.25, -8.89, 1.2, 0.2), ('smd', -8.25, -6.35, 1.2, 0.2), ('smd', -8.25, 6.35, 1.2, 0.2), ('smd', -8.25, 8.89, 1.2, 0.2), ('smd', 8.25, 8.89, 1.2, 0.2), ('smd', 8.25, 6.35, 1.2, 0.2), ('smd', 8.25, -8.89, 1.2, 0.2)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IA48xxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IA48xxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 7.20-0.5,   # Package length
        W  = 19.30-0.5,  # Package width
        H  = 10.16,      # Package height
        A1 = 0.01,       # Package board separation
        rim = (0.0, 0.5, 0.5),  # If a rim should be created at the bottom
        pin = (('round', 0.0, 0.0, 0.51, 3.05), ('round', 0.0, 2.54, 0.51, 3.05), ('round', 0.0, 7.62, 0.51, 3.05), ('round', 0.0, 10.16, 0.51, 3.05), ('round', 0.0, 12.70, 0.51, 3.05)),  # Pin placement
        pin1corner = (-5.80+0.5, -1.53),  # Left upp corner relationsship to pin 1
        pinpadh    = 3.05,  # Pin length, pad height
        pinpadsize = 0.51,  # Pin diameter or pad size
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IAxxxxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IAxxxxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 6.09-0.5,   # Package length
        W  = 19.30-0.5,  # Package width
        H  = 10.16,      # Package height
        A1 = 0.01,       # Package board separation
        rim = (0.0, 0.5, 0.5),  # If a rim should be created at the bottom
        pin = (('round', 0.0, 0.0, 0.51, 3.05), ('round', 0.0, 2.54, 0.51, 3.05), ('round', 0.0, 7.62, 0.51, 3.05), ('round', 0.0, 10.16, 0.51, 3.05), ('round', 0.0, 12.70, 0.51, 3.05)),  # Pin placement
        pin1corner = (-4.69+0.5, -1.53),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IAxxxxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IAxxxxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 10.16-0.5,  # Package length
        W  = 20.32-0.5,  # Package width
        H  = 6.35-0.5,   # Package height
        A1 = 0.01,       # Package board separation
        rim = None, # No rim
        pin = (('round', 0.0, 0.0, 0.51, 2.79), ('round', 0.0, 15.24, 0.51, 2.79), ('round', 7.62, 0.0, 0.51, 2.79), ('round', 7.62, 7.62, 0.51, 2.79), ('round', 7.62, 12.70, 0.51, 2.79), ('round', 7.62, 15.24, 0.51, 2.79)),  # Pin placement
        pin1corner = (-1.27+0.25, -2.54+0.25),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IA48xxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IA48xxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 10.16-0.5,  # Package length
        W  = 20.32-0.5,  # Package width
        H  = 6.88-0.5,   # Package height
        A1 = 0.01,       # Package board separation
        rim = None,      # No rim
        pin = (('round', 0.0, 0.0, 0.51, 2.79), ('round', 0.0, 15.24, 0.51, 2.79), ('round', 7.62, 0.0, 0.51, 2.79), ('round', 7.62, 7.62, 0.51, 2.79), ('round', 7.62, 12.70, 0.51, 2.79), ('round', 7.62, 15.24, 0.51, 2.79)),  # Pin placement
        pin1corner = (-1.27+0.25, -2.54+0.25),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IHxxxxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IHxxxxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 7.2-0.5,    # Package length
        W  = 19.5-0.5,   # Package width
        H  = 10.16,      # Package height
        A1 = 0.01,       # Package board separation
        rim = (0.0, 0.38, 0.38),  # If a rim should be created at the bottom
        pin = (('round', 0.0, 0.0, 0.5, 3.00), ('round', 0.0, 2.54, 0.5, 3.00), ('round', 0.0, 7.62, 0.5, 3.00), ('round', 0.0, 10.16, 0.5, 3.00), ('round', 0.0, 12.70, 0.5, 3.00)),  # Pin placement
        pin1corner = (-5.95+0.5, -2.29),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IHxxxxSH_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IHxxxxSH_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 7.62-0.5,   # Package length
        W  = 19.5-0.5,   # Package width
        H  = 10.16-0.5,  # Package height
        A1 = 0.01,       # Package board separation
        rim = (0.0, 0.38, 0.38),  # If a rim should be created at the bottom
        pin = (('round', 0.0, 0.0, 0.5, 3.00), ('round', 0.0, 2.54, 0.5, 3.00), ('round', 0.0, 10.16, 0.5, 3.00), ('round', 0.0, 12.70, 0.5, 3.00), ('round', 0.0, 15.24, 0.5, 3.00)),  # Pin placement
        pin1corner = (-6.37+0.5, -2.29),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IHxxxxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IHxxxxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 10.16-0.5,  # Package length
        W  = 20.32-0.5,  # Package width
        H  = 6.88,       # Package height
        A1 = 0.01,       # Package board separation
        rim = None,      # No rim
        pin = (('round', 0.0, 0.0, 0.51, 2.79), ('round', 0.0, 15.24, 0.51, 2.79), ('round', 7.62, 0.0, 0.51, 2.79), ('round', 7.62, 7.62, 0.51, 2.79), ('round', 7.62, 12.70, 0.51, 2.79), ('round', 7.62, 15.24, 0.51, 2.79)),  # Pin placement
        pin1corner = (-1.27+0.25, -2.54+0.25),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-IHxxxxDH_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-IHxxxxDH_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 10.16-0.5,  # Package length
        W  = 20.32-0.5,  # Package width
        H  = 6.88,       # Package height
        A1 = 0.01,       # Package board separation
        rim = None,      # No rim
        pin = (('round', 0.0, 0.0, 0.51, 2.79), ('round', 0.0, 15.24, 0.51, 2.79), ('round', 7.62, 0.0, 0.51, 2.79), ('round', 7.62, 10.16, 0.51, 2.79), ('round', 7.62, 12.70, 0.51, 2.79), ('round', 7.62, 15.24, 0.51, 2.79)),  # Pin placement
        pin1corner = (-1.27+0.25, -2.54+0.25),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-ITQxxxxS-H_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-ITQxxxxS-H_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 9.20,   # Package length
        W  = 21.85,  # Package width
        H  = 10.65,  # Package height
        A1 = 0.01,   # Package board separation
        rim = (0.0, 0.38, 0.38),  # If a rim should be created at the bottom
        pin = (('round', 0.0, 0.0, 0.5, 3.00), ('round', 0.0, 2.54, 0.5, 3.00), ('round', 0.0, 5.08, 0.5, 3.00), ('round', 0.0, 12.70, 0.5, 3.00), ('round', 0.0, 15.24, 0.5, 3.00), ('round', 0.0, 17.78, 0.5, 3.00)),  # Pin placement
        pin1corner = (-6.00, -2.035),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-ITxxxxxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-ITxxxxxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 9.20,   # Package length
        W  = 21.85,  # Package width
        H  = 10.65,  # Package height
        A1 = 0.01,   # Package board separation
        rim = (0.0, 0.38, 0.38),  # If a rim should be created at the bottom
        pin = (('round', 0.0, 0.0, 0.5, 3.00), ('round', 0.0, 2.54, 0.5, 3.00), ('round', 0.0, 5.08, 0.5, 3.00), ('round', 0.0, 10.16, 0.5, 3.00), ('round', 0.0, 12.70, 0.5, 3.00), ('round', 0.0, 15.24, 0.5, 3.00), ('round', 0.0, 17.78, 0.5, 3.00)),  # Pin placement
        pin1corner = (-6.00, -2.035),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER-ITXxxxxSA_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER-ITXxxxxSA_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 9.20,  # Package length
        W  = 21.85, # Package width
        H  = 10.65, # Package height
        A1 = 0.01,  # Package board separation
        rim = (0.0, 0.38, 0.38),  # If a rim should be created at the bottom
        pin = (('round', 0.0, 0.0, 0.5, 3.00), ('round', 0.0, 2.54, 0.5, 3.00), ('round', 0.0, 12.70, 0.5, 3.00), ('round', 0.0, 15.24, 0.5, 3.00), ('round', 0.0, 17.78, 0.5, 3.00)),  # Pin placement
        pin1corner = (-6.00, -2.035),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,     # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_Murata_MGJ2DxxxxxxSC_THT': Params(   # ModelName
        #
        # https://power.murata.com/pub/data/power/ncl/kdc_mgj2.pdf
        #
        modelName = 'Converter_DCDC_Murata_MGJ2DxxxxxxSC_THT',  # Model name
        pintype   = 'tht',      # Pin type, 'tht', 'smd'
        L  = 19.50,             # Package length
        W  = 9.80,              # Package width
        H  = 12.50,             # Package height
        A1 = 0.01,              # Package board separation
        rim = (0.0, 0.4, 0.4),  # If a rim should be created at the bottom
        pin = (('rect', 0.0, 0.0,  0.25, 0.5, 4.1),
               ('rect', 2.54,0.0,  0.25, 0.5, 4.1),
               ('rect', 10.16,0.0, 0.25, 0.5, 4.1),
               ('rect', 12.70,0.0, 0.25, 0.5, 4.1),
               ('rect', 15.24,0.0, 0.25, 0.5, 4.1)),  # Pin placement
        pin1corner = (-2.13, -2.67),  # Left upp corner relationsship to pin 1
        show_top   = False,     # If top should be visible or not
        corner     = 'fillet',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,         # If belly of caseing should be round (or flat)
        rotation   = 0.0,       # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',      # Body color
        body_top_color_key = 'black body',      # Body top color
        pin_color_key      = 'metal grey pins', # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_THD_15-xxxxWIN_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_THD_15-xxxxWIN_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 20.3,  # Package length
        W  = 31.8,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (
              ('round', 0*p, 0*p, 0.5, 3.8),
              ('round', 0*p, 1*p, 0.5, 3.8),
              ('round', 0*p, 2*p, 0.5, 3.8),
              ('round', 0*p, 8*p, 0.5, 3.8),
              ('round', 0*p,10*p, 0.5, 3.8),
              ('round', 6*p, 1*p, 0.5, 3.8),
              ('round', 6*p, 2*p, 0.5, 3.8),
              ('round', 6*p, 8*p, 0.5, 3.8),
              ('round', 6*p,10*p, 0.5, 3.8)),  # Pin placement
        pin1corner = (-2.5, -2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'white body',  # Body color
        body_top_color_key = 'white body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_MeanWell_IRM-05-xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell_IRM-05-xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 45.7 , # Package length
        W  = 25.4,  # Package width
        H  = 21.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.04, 3.5),
               ('round',0.0 , 10.75, 1.04, 3.5),
               ('round',38.5, 10.75-8, 1.04, 3.5),
               ('round',38.5, 10.75, 1.04, 3.5)),  # Pin placement
        pin1corner = (-3.6, -25.4+10.75+3.45),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_MeanWell-IRM-10-xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell-IRM-10-xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 45.7 , # Package length
        W  = 25.4,  # Package width
        H  = 21.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.04, 3.5),
               ('round',0.0 , 10.75, 1.04, 3.5),
               ('round',38.5, 10.75-8, 1.04, 3.5),
               ('round',38.5, 10.75, 1.04, 3.5)),  # Pin placement
        pin1corner = (-3.6, -25.4+10.75+3.45),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_MeanWell_IRM-60-xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_MeanWell_IRM-60-xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 87.0 , # Package length
        W  = 52.0,  # Package width
        H  = 29.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 3.5),
               ('round',0.0 , 6.75, 1.0, 3.5),
               ('round',76.0, -5+40.75, 2.0, 3.5),
               ('round',76.0, -5+40.75+5.5, 2.0, 3.5)),  # Pin placement
        pin1corner = (-5.7, -5.0 ),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_RECOM_RAC04-xxSK_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_RECOM_RAC05-xxSK_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 25.4,  # Package length
        W  = 25.4,  # Package width
        H  = 16.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = ( ('round', 0.0, 0.0, 0.51, 5.0),
                ('round', 0, 3.90, 0.51, 5.0),
                ('round', -20.76, 3.90+1.29, 0.51, 5.0),
                ('round', -20.76, 3.90+1.29-10.16, 0.51, 5.0),
                ('round', -20.76, 3.90+1.29-21.59, 0.51, 5.0)),  # Pin placement
        pin1corner = ( -25.4+2.70, -25.4+3.90+3.13),  # Left upp corner relationsship to pin 1
        show_top   = 0,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_TRACO_TMG-15xxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMG-15xxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 41.2,  # Package length
        W  = 27.2,  # Package width
        H  = 19.1,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 8.0),
               ('round',0.0, 19.0, 1.0, 8.0),
               ('round',33., 0.0, 1.0, 8.0),
               ('round',33.0, 12.7, 1.0, 8.0)),  # Pin placement
        pin1corner = (-4.1, -3.4),  # Left upp corner relationsship to pin 1
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_TRACO_TMG-7xxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMG-7xxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 27.4,  # Package length
        W  = 27.4,  # Package width
        H  = 18.7,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 0.6, 4.0),
               ('round',0.0, 5.0, 0.6, 4.0),
               ('round',20.8, 0.0, 0.6, 4.0),
               ('round',20.8, 10.2, 0.6, 4.0)),  # Pin placement
        pin1corner = (-4.1, -3.4),  # Left upp corner relationsship to pin 1
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_TRACO_TMG-30xxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMG-30xxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 64.0,  # Package length
        W  = 45.0,  # Package width
        H  = 23.5,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 8.0),
               ('round',0.0, 17.5, 1.0, 8.0),
               ('round',54.0, -10.0, 1.0, 8.0),
               ('round',54.0, 10.0, 1.0, 8.0)),  # Pin placement
        pin1corner = (-4.0, -22.5),  # Left upp corner relationsship to pin 1
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_TRACO_TMG-50xxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_TRACO_TMG-50xxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd', 'thtsmd' or 'tht_n'
        L  = 74.1,  # Package length
        W  = 54.1,  # Package width
        H  = 21.8,  # Package height
        A1 = 0.1,   # Package board seperation
        rim = None, # No rim
        pin = (('round',0.0, 0.0, 1.0, 8.0),
               ('round',0.0, 20.0, 1.0, 8.0),
               ('round',62.0, -27.05+15.55, 1.0, 8.0),
               ('round',62.0, -27.05+15.55+23, 1.0, 8.0)),  # Pin placement
        pin1corner = (-6.05, -27.5),  # Left upp corner relationsship to pin 1
        show_top   = 1,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_RECOM_RPA60-xxxxSFW_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_RECOM_RPA60-xxxxSFW_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 10*p,  # Package length
        W  = 20*p,  # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round',  0*p,  0*p, 1.0, 5.6),
               ('round',  2*p,  0*p, 1.0, 5.6),
               ('round',  6*p,  0*p, 1.0, 5.6),
               ('round',  7*p, 18*p, 1.0, 5.6),
               ('round',  3*p, 18*p, 1.0, 5.6),
               ('round', -1*p, 18*p, 1.0, 5.6)),  # Pin placement
        pin1corner = (-2*p, -1*p),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TDN_5-xxxxWISM_SMD': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TDN_5-xxxxWISM_SMD',  # Model name
        pintype   = 'smd',  # Pin type, 'tht', 'smd'
        W  = 13.2,  # Package length
        L  = 9.1,   # Package width
        H  = 10.2,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('smd',  3+0.3, -7.1, 0.6, 0.25),
               ('smd', -1+0.3, -7.1, 0.6, 0.25),
               ('smd', -3+0.3, -7.1, 0.6, 0.25),
               ('smd',  1+0.3,  7.1, 0.6, 0.25),
               ('smd', -1+0.3,  7.1, 0.6, 0.25),
               ('smd', -3+0.3,  7.1, 0.6, 0.25)),  # Pin placement
        pin1corner = (0.0, 0.0),  # Left up corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 1,  # If belly of caseing should be round (or flat)
        rotation   = 0.0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR-2xxxxWI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR-2xxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.95,  # Package length
        W  = 9.25,   # Package width
        H  = 12.45,  # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.25/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 7*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 8*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.0, -3.0+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_XP_POWER_JTDxxxxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_XP_POWER_JTDxxxxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 25.4,  # Package length
        W  = 40.64, # Package width
        H  = 10.4,  # Package height
        A1 = 0.1,   # Package board separation
        rim = (0.4, 0.4, 0.5),
        pin = (('round', 0*p, 0*p, 1.0, 6.0),
               ('round', 2*p, 0*p, 1.0, 6.0),
               ('round', 5*p, 0*p, 1.0, 6.0),
               ('round',-3*p, 8*p, 1.0, 6.0),
               ('round', 1*p, 8*p, 1.0, 6.0),
               ('round', 5*p, 8*p, 1.0, 6.0)),  # Pin placement
        pin1corner = (-4*p, -4*p),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_ACDC_RECOM_RAC20-xxDK_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_ACDC_RECOM_RAC20-xxDK_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 52.5,  # Package length
        W  = 27.4,  # Package width
        H  = 23.0,  # Package height
        A1 = 0.1,   # Package board separation
        rim = None, # No rim
        pin = (('round',  0*p,  0*p, 1.0, 6.0),
               ('round',  0*p,  8*p, 1.0, 6.0),
               ('round',  18*p, 0*p, 1.0, 6.0),
               ('round',  18*p, 4*p, 1.0, 6.0),
               ('round',  18*p, 8*p, 1.0, 6.0)),  # Pin placement
        pin1corner = (-3.39, -3.50),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_ACDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TBA1-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TBA1-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.68,   # Package length
        W  = 6.0,     # Package width
        H  = 9.65+0.5,# Package height
        A1 = 0.1,     # Package board separation
        rim = (0.5, 2.999, 0.5), #nasty bug here if the two rim touches (W=6mm, 2.99+2.99 is ok)
        pin = (
               ('rect', 0*p, 0.0, 0.5, 0.25, 3.05),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.05),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.05),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.05),
               ),  # Pin placement
        pin1corner = (-2.03, 1.35-6.0 ),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TBA1-xx1xE_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TBA1-xx1xE_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.50,  # Package length
        W  = 6.0,    # Package width
        H  = 9.5+0.5,# Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 2.999, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.40, -1.35),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TBA1-xx2xE_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TBA1-xx2xE_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.50,  # Package length
        W  = 6.0,    # Package width
        H  = 9.5+0.5,# Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 2.999, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.40, -1.35),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TBA1-xx1xHI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TBA1-xx1xHI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.50,  # Package length
        W  = 6.0,    # Package width
        H  = 9.5+0.5,# Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 2.999, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.40, -1.35),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TBA1-xx2xHI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TBA1-xx2xHI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.50,  # Package length
        W  = 6.0,    # Package width
        H  = 9.5+0.5,# Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 2.999, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.40, -1.35),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TBA2-xx1x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TBA2-xx1x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.55,  # Package length
        W  = 7.6,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.45, 3.78, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.40, -1.35),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TBA2-xx2x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TBA2-xx2x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.55,  # Package length
        W  = 7.6,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.45, 3.78, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.40, -1.35),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMA05xxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA05xxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.049, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMA05xxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA05xxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.049, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMA12xxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA12xxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.049, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMA12xxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA12xxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.049, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMA15xxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA15xxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.549, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMA15xxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA15xxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.549, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMA24xxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA24xxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.549, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMA24xxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMA24xxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.549, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMAPxxxxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMAPxxxxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.549, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.8-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMAPxxxxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMAPxxxxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.10,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.549, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.10, -1.8-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMExxxxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMExxxxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.5,    # Package length
        W  = 6.1,     # Package width
        H  = 10.2,    # Package height
        A1 = 0.1,     # Package board separation
        rim = (0.5, 3.0399, 0.5), #nasty bug here if the two rim touches (W=6mm, 2.99+2.99 is ok)
        pin = (
               ('rect', 0*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.2),
               ),  # Pin placement
        pin1corner = (-2.03, -4.2-0.25/2  ),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TME24xxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TME24xxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.5,    # Package length
        W  = 7.1,     # Package width
        H  = 10.2,    # Package height
        A1 = 0.1,     # Package board separation
        rim = (0.5, 3.54, 0.5),
        pin = (
               ('rect', 0*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.2),
               ),  # Pin placement
        pin1corner = (-2.03, -5.2-0.25/2 ),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMHxxxxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMHxxxxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.50,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.749, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.30, -1.25-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMHxxxxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMHxxxxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.50,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 3.749, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.0)),  # Pin placement
        pin1corner = (-2.30, -1.25-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR2-xxxxE_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR2-xxxxE_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.3,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.3/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 7*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.0, -2.7+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR2-xxxxWIN_THT': Params(   # ModelName
        #
        # equivalent to TMR2-xxxxWI
        #
        modelName = 'Converter_DCDC_TRACO_TMR2-xxxxWIN_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.3,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.3/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 7*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.0, -2.7+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR3-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR3-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.2,    # Package width
        H  = 11.1,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.2/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.0)),  # Pin placement
        pin1corner = (-2.0, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR3-xxxxE_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR3-xxxxE_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.3,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.3/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 7*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.0, -2.7+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR3-xxxxHI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR3-xxxxHI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.2,    # Package width
        H  = 11.1,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.2/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.0)),  # Pin placement
        pin1corner = (-2.0, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR3-xxxxWI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR3-xxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.2,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.2/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.0),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.0),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.0)),  # Pin placement
        pin1corner = (-2.0, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMR3-xxxxWIE_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR3-xxxxWIE_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.3,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.3/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 2*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 7*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.0, -2.7+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR6-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMR6-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-2.0, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMR6-xxxxWI_THT': Params(   # ModelName
        #
        # = TMR6
        #
        modelName = 'Converter_DCDC_TRACO_TMR6-xxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-2.0, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMV-xxxxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV-xxxxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 6.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, +4.75 -6.1 -0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMV-xxxxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV-xxxxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 6.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, +4.75 -6.1 -0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMV-24xxS_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV-24xxS_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, +4.75 -7.1 -0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMV-24xxD_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV-24xxD_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, +4.75 -7.1 -0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMV2-xxxxSHI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV2-xxxxSHI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, -1.55 -0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TMV2-xxxxDHI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV2-xxxxDHI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, -1.55 -0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMV-xxxxxEN_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV-xxxxEN_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 22.0,   # Package length
        W  = 7.5,    # Package width
        H  = 12.5,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.5/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-3.5, -2 +0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TMV-xxxxDEN_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TMV-xxxxDEN_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 22.0,   # Package length
        W  = 7.5,    # Package width
        H  = 12.5,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.5/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-3.5, -2 +0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TRV1-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRV1-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 6.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.35, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRV1-24xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRV1-24xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 6*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.35, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRV1-xx1xM_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRV1-xx1xM_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.6,   # Package length
        W  = 9.9,    # Package width
        H  = 12.5,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.9/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 8*pm, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (16.0+1.8-19.6, -2.3),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TRV1-xx2xM_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRV1-xx2xM_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.6,   # Package length
        W  = 9.9,    # Package width
        H  = 12.5,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.9/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 8*pm, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (16.0+1.8-19.6, -2.3),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEC2-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC2-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEC2-xxxxWI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC2-xxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEC3-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC3-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEC3-xxxxWI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC3-xxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRA1-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRA1-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 6.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRA1-24xx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRA1-24xx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.1,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 4*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.3, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRA3-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRA3-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 7.6,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.6/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 3.2),
               ('rect', 1*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 3*p, 0.0, 0.5, 0.25, 3.2),
               ('rect', 5*p, 0.0, 0.5, 0.25, 3.2)),  # Pin placement
        pin1corner = (-2.55, -1.3+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRN1-xx1x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRN1-xx1x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.9,   # Package length
        W  = 7.7,    # Package width
        H  = 11.0,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.7/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*pm+0.8, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*pm+0.8, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (8.8+1.6-11.9,3.7-7.7),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRN1-xx2x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRN1-xx2x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.9,   # Package length
        W  = 7.7,    # Package width
        H  = 11.0,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.7/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*pm+0.8, 0.0, 0.5, 0.25, 4.1),
               ('rect', 3*pm+0.8, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*pm+0.8, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (8.8+1.6-11.9,3.7-7.7),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TRN3-xx1x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRN3-xx1x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.9,   # Package length
        W  = 7.7,    # Package width
        H  = 11.0,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.7/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*pm+0.8, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*pm+0.8, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (8.8+1.6-11.9,3.7-7.7),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TRN3-xx2x_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TRN3-xx2x_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.9,   # Package length
        W  = 7.7,    # Package width
        H  = 11.0,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.7/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*pm, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*pm+0.8, 0.0, 0.5, 0.25, 4.1),
               ('rect', 3*pm+0.8, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*pm+0.8, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (8.8+1.6-11.9,3.7-7.7),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TSN1-xxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSN1-xxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.7,   # Package length
        W  = 7.5,    # Package width
        H  = 16.5,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.5/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.3, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.3, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.3, 4.1)),  # Pin placement
        pin1corner = (-3.3, -7.5+3.1),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TSR05-xxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSR05-xxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.5,   # Package length
        W  = 7.55,   # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.55/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.7, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.7, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.7, 0.25, 4.1)),  # Pin placement
        pin1corner = (-3.3, -7.55+2.0+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TSR06-xxxxxWI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSR06-xxxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 12.0,   # Package length
        W  = 8.6,    # Package width
        H  = 13.4,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 8.6/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (2*p+3.5-12.0, -7.55+2.0+0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TSR1-xxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSR1-xxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.7,   # Package length
        W  = 7.5,    # Package width
        H  = 10.1,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.5/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (2*p+3.3-11.7, -5.5),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TSR1-xxxxE_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSR1-xxxxE_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.6,   # Package length
        W  = 7.5,    # Package width
        H  = 10.1,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.5/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.3, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.3, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.3, 4.1)),  # Pin placement
        pin1corner = (-3.26, -5.45),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TSR2-xxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSR2-xxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 14.0,   # Package length
        W  = 7.5,    # Package width
        H  = 10.1,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.5/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.46, 0.46, 4.1),
               ('rect', 1*p, 0.0, 0.46, 0.46, 4.1),
               ('rect', 2*p, 0.0, 0.46, 0.46, 4.1)),  # Pin placement
        pin1corner = (2*p+4.5-14.0, 3.89-7.5),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TSRN1-xxxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TSRN1-xxxxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.7,   # Package length
        W  = 7.5,    # Package width
        H  = 10.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 7.5/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-3.3, 2.4-7.5),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEA1-0505_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEA1-0505_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 11.68,  # Package length
        W  = 6.0,    # Package width
        H  = 9.65,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 6.0/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 3*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-2.03, 0.9-6.0),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEA1-0505E_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEA1-0505E_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.0,    # Package width
        H  = 9.5,    # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 6.0/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 3*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-2.40, -0.9),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEA1-0505HI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEA1-0505HI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 19.5,   # Package length
        W  = 6.0,    # Package width
        H  = 9.5,    # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 6.0/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (-2.40, -0.9),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


    'Converter_DCDC_TRACO_TEC2-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC2-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEC2-xxxxWI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC2-xxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEC3-xxxx_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC3-xxxx_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),

    'Converter_DCDC_TRACO_TEC3-xxxxWI_THT': Params(   # ModelName
        #
        #
        #
        modelName = 'Converter_DCDC_TRACO_TEC3-xxxxWI_THT',  # Model name
        pintype   = 'tht',  # Pin type, 'tht', 'smd'
        L  = 21.8,   # Package length
        W  = 9.1,    # Package width
        H  = 11.2,   # Package height
        A1 = 0.1,    # Package board separation
        rim = (0.5, 9.1/2 -0.001, 0.5),
        pin = (('rect', 0.0, 0.0, 0.5, 0.25, 4.1),
               ('rect', 1*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 2*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 4*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 5*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 6*p, 0.0, 0.5, 0.25, 4.1),
               ('rect', 7*p, 0.0, 0.5, 0.25, 4.1)),  # Pin placement
        pin1corner = (7*p+2-21.8, -3.2-0.25/2),  # Left upp corner relationsship to pin 1
        show_top   = False,  # If top should be visible or not
        corner     = 'none',  # If top should be cut, 'none', 'chamfer' or 'fillet'
        roundbelly = 0,  # If belly of caseing should be round (or flat)
        rotation   = 0,  # If belly of caseing should be round (or flat)
        body_color_key     = 'black body',  # Body color
        body_top_color_key = 'black body',  # Body top color
        pin_color_key      = 'metal grey pins',  # Pin color
        dest_dir_prefix    = 'Converter_DCDC.3dshapes'  # Destination directory
        ),


}

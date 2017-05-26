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

destination_dir="./generated_pinheaders/"

Params = namedtuple("Params", [
    'p', # pitch (separaration between pins)
    'rows', #number of rows
    'w', #width of plastic base
    'c', # chamfering of plastic base
    'h', # height of plastic base
    'hb', # heigh of plastic base above board for SMD (or to the back of pin for Angled)
    'pw', #pin width (square pins only)
    'pc', #pin end chamfer amount
    'pa', #pin height above board
    'ph', #pin length below board
    'rot', #rotation if required
    'type', #Angled or Straight
])

kicad_naming_params_pin_headers = {
    '254singleH10': Params(		
        p = 2.54,
        w = 2.5,
        rows = 1,
        c = 0.25,
        h = 2.54,
        hb = 0,
        pw = 0.64,
        pc = 0.15,
        pa = 6 + 2.54,
        ph = 3.05,
        rot = -90,
        type = 'Straight',
    ),
    '254single': Params(
        p = 2.54,
        w = 2.5,
        rows = 1,
        c = 0.25,
        h = 2.5,
        hb = 0,
        pw = 0.64,
        pc = 0.15,
        pa = 11,
        ph = 3.3,
        rot = -90,
        type = 'Straight',
    ),
    '254dual': Params(
        p = 2.54,
        w = 5.0,
        rows = 2,
        c = 0.25,
        h = 2.5,
        hb = 0,
        pw = 0.64,
        pc = 0.15,
        pa = 11,
        ph = 3.3,
        rot = -90,
        type = 'Straight',
    ),
    #2.00mm pitch, single row
    #e.g. http://multimedia.3m.com/mws/media/438474O/3mtm-pin-strip-header-ts2156.pdf
    '200single': Params(
        p = 2.00,
        w = 2.0,
        rows = 1,
        c = 0.25,
        h = 1.5,
        hb = 0,
        pw = 0.5,
        pc = 0.1,
        pa = 5.9,
        ph = 2.8,
        rot = -90,
        type = 'Straight',
    ),
    #2.00mm pitch, dual row
    #e.g. http://multimedia.3m.com/mws/media/438474O/3mtm-pin-strip-header-ts2156.pdf
    '200dual': Params(
        p = 2.00,
        w = 4.0,
        rows = 2,
        c = 0.25,
        h = 1.5,
        hb = 0,
        pw = 0.5,
        pc = 0.1,
        pa = 5.9,
        ph = 2.8,
        rot = -90,
        type = 'Straight',
    ),
    #1.27mm pitch, single row
    #e.g. http://www.sullinscorp.com/drawings/71_GRPB___1VWVN-RC,_10957-C.pdf
    '127single': Params(
        p = 1.27,
        w = 2.14,
        rows = 1,
        c = 0.2,
        h = 1.0,
        hb = 0,
        pw = 0.4,
        pc = 0.1,
        pa = 4.0,
        ph = 2.3,
        rot = -90,
        type = 'Straight',
    ),
    #1.27mm pitch, dual row
    #e.g. http://www.sullinscorp.com/drawings/71_GRPB___1VWVN-RC,_10957-C.pdf
    '127dual': Params(
        p = 1.27,
        w = 3.4,
        rows = 2,
        c = 0.2,
        h = 1.0,
        hb = 0,
        pw = 0.4,
        pc = 0.1,
        pa = 4.0,
        ph = 2.3,
        rot = -90,
        type = 'Straight',
    ),
    'Pin_Header_Angled_Pitch2.54mm': Params(		
        p = 2.54,
        w = 5.0,
        rows = 2,
        c = 0.25,
        h = 2.54,
        hb = 1.82,
        pw = 0.64,
        pc = 0.15,
        pa = 6 + 2.5,
        ph = 3.05,
        rot = 0,
        type = 'Angled',
    ),
}
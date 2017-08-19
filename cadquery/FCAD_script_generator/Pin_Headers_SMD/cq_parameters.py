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

destination_dir="/Pin_Headers.3dshapes"

Params = namedtuple("Params", [
    'p', # pitch (separaration between pins)
    'rows', #number of rows
    'w', #width of plastic base
    'h', # height of plastic base
    'hb', # heigh of plastic base above board for SMD
    'pw', #pin width (square pins only)
    'pa', #pin lenght from board to pintip
    'ph', #horizontal pin length
    'pins', #pin range
    'rot', #rotation if required
    'type', #Angled or Straight
])

kicad_naming_params_pin_headers = {
    'Pin_Header_Straight_1xyy_Pitch2.54mm_SMD_Pin1Left': Params(	#http://katalog.we-online.de/em/datasheet/6100xx18321.pdf
        p = 2.54, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.54, #width of plastic base
        h = 2.54, # height of plastic base
        hb = 0.76, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.64, #pin width (square pins only)
        pa = 6 + 3.3, #pin length from board to pintip
        ph = 2.82, #pin length below board
        pins = (2,40), #pin range
        rot = -90, #rotation if required
        type = 'Pin1Left', #Angled or Straight
    ),
    'Pin_Header_Straight_1xyy_Pitch2.54mm_SMD_Pin1Right': Params(    #http://katalog.we-online.de/em/datasheet/6100xx18321.pdf
        p = 2.54, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.54, #width of plastic base
        h = 2.54, # height of plastic base
        hb = 0.76, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.64, #pin width (square pins only)
        pa = 6 + 2.54, #pin lenght from board to pintip
        ph = 2.82, #pin length below board 
        pins = (2,40), #pin range
        rot = -90, #rotation if required
        type = 'Pin1Right', #Angled or Straight
    ),
    'Pin_Header_Straight_2xyy_Pitch2.54mm_SMD': Params( #from http://katalog.we-online.de/em/datasheet/6130xx21121.pdf
        p = 2.54, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 5.08, #width of plastic base
        h = 2.54, # height of plastic base
        hb = 0.76, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.64, #pin width (square pins only)
        pa = 6 + 2.54, #pin lenght from board to pintip
        ph = 2.82, #pin length below board 
        pins = (1,40), #pin range
        rot = -90, #rotation if required
        type = None, #Angled or Straight
    ),

    'Pin_Header_Straight_1xyy_Pitch2.00mm_SMD_Pin1Left': Params(    #http://www.mouser.com/ds/2/4/page_280-282-24683.pdf
        p = 2.00, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.0, #width of plastic base
        h = 1.5, # height of plastic base
        hb = 0.7, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.5, #pin width (square pins only)
        pa = 4 + 2.2, #pin length from board to pintip
        ph = 2.35, #pin length below board
        pins = (2,40), #pin range
        rot = -90, #rotation if required
        type = 'Pin1Left', #Angled or Straight
    ),
    'Pin_Header_Straight_1xyy_Pitch2.00mm_SMD_Pin1Right': Params(    #http://www.mouser.com/ds/2/4/page_280-282-24683.pdf
        p = 2.00, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.0, #width of plastic base
        h = 1.5, # height of plastic base
        hb = 0.7, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.5, #pin width (square pins only)
        pa = 4 + 2.2, #pin lenght from board to pintip
        ph = 2.35, #pin length below board 
        pins = (2,40), #pin range
        rot = -90, #rotation if required
        type = 'Pin1Right', #Angled or Straight
    ),
    'Pin_Header_Straight_2xyy_Pitch2.00mm_SMD': Params( #from http://www.mouser.com/ds/2/4/page_280-282-24683.pdf
        p = 2.00, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 4.00, #width of plastic base
        h = 1.5, # height of plastic base
        hb = 0.7, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.5, #pin width (square pins only)
        pa = 4 + 2.2, #pin lenght from board to pintip
        ph = 2.35, #pin length below board 
        pins = (1,40), #pin range
        rot = -90, #rotation if required
        type = None, #Angled or Straight
    ),

    'Pin_Header_Straight_1xyy_Pitch1.27mm_SMD_Pin1Left': Params(    #https://cdn.harwin.com/pdfs/M50-363.pdf
        p = 1.27, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.1, #width of plastic base
        h = 1.0, # height of plastic base
        hb = 0.5, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.4, #pin width (square pins only)
        pa = 4.5, #pin length from board to pintip
        ph = 2.7, #pin length below board
        pins = (2,40), #pin range
        rot = -90, #rotation if required
        type = 'Pin1Left', #Angled or Straight
    ),
    'Pin_Header_Straight_1xyy_Pitch1.27mm_SMD_Pin1Right': Params(    #https://cdn.harwin.com/pdfs/M50-363.pdf
        p = 1.27, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.1, #width of plastic base
        h = 1.0, # height of plastic base
        hb = 0.5, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.4, #pin width (square pins only)
        pa = 4.5, #pin lenght from board to pintip
        ph = 2.7, #pin length below board 
        pins = (2,40), #pin range
        rot = -90, #rotation if required
        type = 'Pin1Right', #Angled or Straight
    ),
    'Pin_Header_Straight_2xyy_Pitch1.27mm_SMD': Params( #from http://katalog.we-online.de/em/datasheet/6130xx21121.pdf
        p = 1.27, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 3.4, #width of plastic base
        h = 1.0, # height of plastic base
        hb = 0.5, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.4, #pin width (square pins only)
        pa = 4.68, #pin lenght from board to pintip
        ph = 2.315, #pin length below board 
        pins = (1,40), #pin range
        rot = -90, #rotation if required
        type = None, #Angled or Straight
    ),
}
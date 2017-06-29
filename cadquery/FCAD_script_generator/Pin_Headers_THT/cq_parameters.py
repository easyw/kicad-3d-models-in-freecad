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
    'c', # chamfering of plastic base
    'h', # height of plastic base
    'hb', # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
    'pw', #pin width (square pins only)
    'pc', #pin end chamfer amount
    'pa', #pin lenght from bottom of base to pintip
    'ph', #pin length below board 
    'rot', #rotation if required
    'type', #Angled or Straight
])

kicad_naming_params_pin_headers = {
    'Pin_Header_Straight_1xyy_Pitch2.54mm': Params(	#from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
        p = 2.54, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.54, #width of plastic base
        c = 0.25, # chamfering of plastic base
        h = 2.54, # height of plastic base
        hb = 0, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.64, #pin width (square pins only)
        pc = 0.15, #pin end chamfer amount
        pa = 6 + 2.54, #pin lenght from bottom of base to pintip
        ph = 3.0, #pin length below board 
        rot = -90, #rotation if required
        type = 'Straight', #Angled or Straight
    ),
    'Pin_Header_Straight_2xyy_Pitch2.54mm': Params( #from http://katalog.we-online.de/em/datasheet/6130xx21121.pdf
        p = 2.54, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 5.08, #width of plastic base
        c = 0.25, # chamfering of plastic base
        h = 2.54, # height of plastic base
        hb = 0, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.64, #pin width (square pins only)
        pc = 0.15, #pin end chamfer amount
        pa = 6 + 2.54, #pin lenght from bottom of base to pintip
        ph = 3.0, #pin length below board 
        rot = -90, #rotation if required
        type = 'Straight', #Angled or Straight
    ),
    'Pin_Header_Angled_1xyy_Pitch2.54mm': Params( # from http://katalog.we-online.de/em/datasheet/6130xx11021.pdf    
        p = 2.54, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.54, #width of plastic base
        c = 0.25, # chamfering of plastic base
        h = 2.54, # height of plastic base
        hb = 1.5, # heigh of plastic base (or to the middle of pin for Angled)
        pw = 0.64, #pin width (square pins only)
        pc = 0.15, #pin end chamfer amount
        pa = 6 + 2.54, #pin lenght from bottom of base to pintip
        ph = 3.0, #pin length below board to bottom of base 
        rot = -90, #rotation if required
        type = 'Angled', #Angled or Straight
    ),
    'Pin_Header_Angled_2xyy_Pitch2.54mm': Params( # from http://katalog.we-online.de/em/datasheet/6130xx21021.pdf
        p = 2.54, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 5.08, #width of plastic base
        c = 0.25, # chamfering of plastic base
        h = 2.54, # height of plastic base
        hb = 1.5, # heigh of plastic base (or to the middle of pin for Angled)
        pw = 0.64, #pin width (square pins only)
        pc = 0.15, #pin end chamfer amount
        pa = 6 + 2.54, #pin lenght from bottom of base to pintip
        ph = 3.0, #pin length below board to bottom of base 
        rot = -90, #rotation if required
        type = 'Angled', #Angled or Straight
    ),
    'Pin_Header_Straight_1xyy_Pitch2.00mm': Params( #from http://katalog.we-online.de/em/datasheet/6200xx11121.pdf
        p = 2.00, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.00, #width of plastic base
        c = 0.2, # chamfering of plastic base
        h = 2.00, # height of plastic base
        hb = 0, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.5, #pin width (square pins only)
        pc = 0.125, #pin end chamfer amount
        pa = 4.0 + 2.00, #pin lenght from bottom of base to pintip
        ph = 2.8, #pin length below board 
        rot = -90, #rotation if required
        type = 'Straight', #Angled or Straight
    ),
    'Pin_Header_Straight_2xyy_Pitch2.00mm': Params( #from http://katalog.we-online.de/em/datasheet/6200xx21121.pdf
        p = 2.00, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 4.0, #width of plastic base
        c = 0.2, # chamfering of plastic base
        h = 2.00, # height of plastic base
        hb = 0, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.5, #pin width (square pins only)
        pc = 0.125, #pin end chamfer amount
        pa = 4.0 + 2.00, #pin lenght from bottom of base to pintip
        ph = 2.8, #pin length below board 
        rot = -90, #rotation if required
        type = 'Straight', #Angled or Straight
    ),
    'Pin_Header_Angled_1xyy_Pitch2.00mm': Params( # from https://cdn.harwin.com/pdfs/M22-273.pdf
        p = 2.00, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.00, #width of plastic base
        c = 0.2, # chamfering of plastic base
        h = 1.5, # height of plastic base
        hb = 1.5, # heigh of plastic base (or to the middle of pin for Angled)
        pw = 0.5, #pin width (square pins only)
        pc = 0.125, #pin end chamfer amount
        pa = 4.2 + 1.5, #pin lenght from bottom of base to pintip
        ph = 2.4, #pin length below board to bottom of base 
        rot = -90, #rotation if required
        type = 'Angled', #Angled or Straight
    ),
    'Pin_Header_Angled_2xyy_Pitch2.00mm': Params( # from https://cdn.harwin.com/pdfs/M22-274.pdf
        p = 2.00, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 4.0, #width of plastic base
        c = 0.2, # chamfering of plastic base
        h = 1.5, # height of plastic base
        hb = 1.5, # heigh of plastic base (or to the middle of pin for Angled)
        pw = 0.5, #pin width (square pins only)
        pc = 0.125, #pin end chamfer amount
        pa = 4.2 + 1.5, #pin lenght from bottom of base to pintip
        ph = 2.4, #pin length below board to bottom of base 
        rot = -90, #rotation if required
        type = 'Angled', #Angled or Straight
    ),



    'Pin_Header_Straight_1xyy_Pitch1.27mm': Params( #from https://cdn.harwin.com/pdfs/M50-353.pdf
        p = 1.27, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.1, #width of plastic base
        c = 0.127, # chamfering of plastic base
        h = 1.0, # height of plastic base
        hb = 0, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.4, #pin width (square pins only)
        pc = 0.1, #pin end chamfer amount
        pa = 3.0 + 1, #pin lenght from bottom of base to pintip
        ph = 2.3, #pin length below board 
        rot = -90, #rotation if required
        type = 'Straight', #Angled or Straight
    ),
    'Pin_Header_Straight_2xyy_Pitch1.27mm': Params( #from https://cdn.harwin.com/pdfs/HF212-W.pdf
        p = 1.27, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 3.4, #width of plastic base
        c = 0.127, # chamfering of plastic base
        h = 1.0, # height of plastic base
        hb = 0, # heigh of plastic base above board for SMD (or to the middle of pin for Angled)
        pw = 0.4, #pin width (square pins only)
        pc = 0.1, #pin end chamfer amount
        pa = 3.0 + 1, #pin lenght from bottom of base to pintip
        ph = 2.3, #pin length below board 
        rot = -90, #rotation if required
        type = 'Straight', #Angled or Straight
    ),
    'Pin_Header_Angled_1xyy_Pitch1.27mm': Params( # from http://katalog.we-online.de/em/datasheet/6130xx11021.pdf    
        p = 1.27, # pitch (separaration between pins)
        rows = 1, #number of rows
        w = 2.1, #width of plastic base
        c = 0.127, # chamfering of plastic base
        h = 1.0, # height of plastic base
        hb = 0.5, # heigh of plastic base (or to the middle of pin for Angled)
        pw = 0.4, #pin width (square pins only)
        pc = 0.1, #pin end chamfer amount
        pa = 4.0 + 1, #pin lenght from bottom of base to pintip
        ph = 2.4, #pin length below board to bottom of base 
        rot = -90, #rotation if required
        type = 'Angled', #Angled or Straight
    ),
    'Pin_Header_Angled_2xyy_Pitch1.27mm': Params( # from http://katalog.we-online.de/em/datasheet/6130xx21021.pdf
        p = 1.27, # pitch (separaration between pins)
        rows = 2, #number of rows
        w = 3.4, #width of plastic base
        c = 0.127, # chamfering of plastic base
        h = 1.0, # height of plastic base
        hb = 0.5, # heigh of plastic base (or to the middle of pin for Angled)
        pw = 0.4, #pin width (square pins only)
        pc = 0.1, #pin end chamfer amount
        pa = 4.0 + 1, #pin lenght from bottom of base to pintip
        ph = 2.4, #pin length below board to bottom of base 
        rot = -90, #rotation if required
        type = 'Angled', #Angled or Straight
    ),
}
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

destination_dir="/Capacitors_Radial_SMD"
# destination_dir="./"

Params = namedtuple("Params", [
    'L',   # overall height
    'D',   # diameter
    'A',   # base width (x&y)
    'H',   # max width (x) with pins
    'P',   # distance between pins
    'W',   # pin width
    'PM',  # show/hide pin marker
    'rotation',  # rotation if required
])

all_params_radial_smd_cap = {# Aluminum SMD capacitors
        # Dimensions per http://industrial.panasonic.com/lecs/www-data/pdf/ABA0000/ABA0000PE369.pdf 
    "G_D100_L100" : Params( # note L model height
        L         =10.2,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =False,   # show/hide pin marker
        rotation  = -90, # rotation if required
    ),
    "F_D80_L100" : Params( # note L model height
        L         =10.2,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =10.,     # max width (x) with pins
        P         =3.1,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = -90, # rotation if required
    ),
    "E_D80_L62" : Params( # note L model height
        L         =6.2,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = -90, # rotation if required
    ),
    "D8_D63_L77" : Params( # note L model height
        L         =7.7,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = -90, # rotation if required
    ),
    "D_D63_L54" : Params( # note L model height
        L         =5.4,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = -90, # rotation if required
    ),
    "C_D50_L54" : Params( # note L model height
        L         =5.4,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base I haven't found a black but lighter material on Mario material specswidth (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = -90, # rotation if required
    ),
    "B_D40_L54" : Params( # note L model height
        L         =5.4,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = -90, # rotation if required
    ),
}

kicad_naming_params_radial_smd_cap = {# Aluminum SMD capacitors
    "C_Elec_3x5.4" : Params(    # note L model height
        L           =5.4,       # overall height
        D           =3.0,       # diameter
        A           =3.3,       # base width (x&y)
        H           =3.8,       # max width (x) with pins
        P           =0.8,       # distance between pins
        W           =0.45,      # pin width
        PM          =False,     # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_4x5.4" : Params(    # note L model height
        L         =5.4,         # overall height
        D         =4.0,         # diameter
        A         =4.3,         # base width (x&y)
        H         =5.5,         # max width (x) with pins
        P         =1.0,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_4x5.8" : Params(    # note L model height
        L         =5.8,         # overall height
        D         =4.0,         # diameter
        A         =4.3,         # base width (x&y)
        H         =5.5,         # max width (x) with pins
        P         =1.0,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_5x5.4" : Params(    # note L model height
        L         =5.4,         # overall height
        D         =5.0,         # diameter
        A         =5.3,         # base width (x&y)
        H         =6.5,         # max width (x) with pins
        P         =1.5,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_5x5.8" : Params(    # note L model height
        L         =5.8,         # overall height
        D         =5.0,         # diameter
        A         =5.3,         # base width (x&y)
        H         =6.5,         # max width (x) with pins
        P         =1.5,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_6.3x5.4" : Params(  # note L model height
        L         =5.4,         # overall height
        D         =6.3,         # diameter
        A         =6.6,         # base width (x&y)
        H         =7.8,         # max width (x) with pins
        P         =1.8,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_6.3x5.8" : Params(  # note L model height
        L         =5.8,         # overall height
        D         =6.3,         # diameter
        A         =6.6,         # base width (x&y)
        H         =7.8,         # max width (x) with pins
        P         =1.8,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_6.3x7.7" : Params(  # note L model height
        L         =7.7,         # overall height
        D         =6.3,         # diameter
        A         =6.6,         # base width (x&y)
        H         =7.8,         # max width (x) with pins
        P         =1.8,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_8x5.4" : Params(    # note L model height
        L         =5.4,         # overall height
        D         =8.,          # diameter
        A         =8.3,         # base width (x&y)
        H         =9.5,         # max width (x) with pins
        P         =2.2,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_8x6.2" : Params(    # note L model height
        L         =6.2,         # overall height
        D         =8.,          # diameter
        A         =8.3,         # base width (x&y)
        H         =9.5,         # max width (x) with pins
        P         =2.2,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_8x10.2" : Params(   # note L model height
        L         =10.2,        # overall height
        D         =8.,          # diameter
        A         =8.3,         # base width (x&y)
        H         =9.5,         # max width (x) with pins
        P         =2.2,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "C_Elec_10x10.2" : Params(  # note L model height
        L         =10.2,        # overall height
        D         =10.,         # diameter
        A         =10.3,        # base width (x&y)
        H         =11.5,        # max width (x) with pins
        P         =2.2,         # distance between pins
        W         =0.65,        # pin width
        PM        =False,       # show/hide pin marker
        rotation  = 180,        # rotation if required
    ),
    "CP_Elec_3x5.3" : Params( # note L model height
        L         =5.3,    # overall height
        D         =3.,     # diameter
        A         =3.3,    # base width (x&y)
        H         =3.8,     # max width (x) with pins
        P         =0.8,     # distance between pins
        W         =0.45,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_3x5.4" : Params( # note L model height
        L         =5.4,    # overall height
        D         =3.,     # diameter
        A         =3.3,    # base width (x&y)
        H         =3.8,     # max width (x) with pins
        P         =0.8,     # distance between pins
        W         =0.45,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_4x3" : Params( # note L model height
        L         =3.0,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_4x3.9" : Params( # note L model height
        L         =3.9,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_4x4.5" : Params( # note L model height
        L         =4.5,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_4x5.3" : Params( # note L model height
        L         =5.3,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_4x5.4" : Params( # note L model height
        L         =5.4,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_4x5.7" : Params( # note L model height
        L         =5.7,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_4x5.8" : Params( # note L model height
        L         =5.8,    # overall height
        D         =4.0,     # diameter
        A         =4.3,    # base width (x&y)
        H         =5.5,     # max width (x) with pins
        P         =1.0,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_5x3" : Params( # note L model height
        L         =3.0,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_5x3.9" : Params( # note L model height
        L         =3.9,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_5x4.4" : Params( # note L model height
        L         =4.4,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_5x4.5" : Params( # note L model height
        L         =4.5,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_5x5.3" : Params( # note L model height
        L         =5.3,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_5x5.4" : Params( # note L model height
        L         =5.4,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_5x5.7" : Params( # note L model height
        L         =5.7,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_5x5.8" : Params( # note L model height
        L         =5.8,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_5x5.9" : Params( # note L model height
        L         =5.9,    # overall height
        D         =5.0,     # diameter
        A         =5.3,    # base width (x&y)
        H         =6.5,     # max width (x) with pins
        P         =1.5,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    
    "CP_Elec_6.3x3" : Params( # note L model height
        L         =3.0,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x3.9" : Params( # note L model height
        L         =3.9,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x4.5" : Params( # note L model height
        L         =4.5,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x4.9" : Params( # note L model height
        L         =4.9,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x5.2" : Params( # note L model height
        L         =5.2,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x5.3" : Params( # note L model height
        L         =5.3,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x5.4" : Params( # note L model height
        L         =5.4,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x5.4_Nichicon" : Params( # note L model height
        L         =5.4,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),

    "CP_Elec_6.3x5.7" : Params( # note L model height
        L         =5.7,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_6.3x5.8" : Params( # note L model height
        L         =5.8,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_6.3x5.9" : Params( # note L model height
        L         =5.9,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_6.3x7.7" : Params( # note L model height
        L         =7.7,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_6.3x9.9" : Params( # note L model height
        L         =9.9,    # overall height
        D         =6.3,     # diameter
        A         =6.6,    # base width (x&y)
        H         =7.8,     # max width (x) with pins
        P         =1.8,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x5.4" : Params( # note L model height
        L         =5.4,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x6.2" : Params( # note L model height
        L         =6.2,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x6.5" : Params( # note L model height
        L         =6.5,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x6.7" : Params( # note L model height
        L         =6.7,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x6.9" : Params( # note L model height
        L         =6.9,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x10" : Params( # note L model height
        L         =10,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x10.5" : Params( # note L model height
        L         =10.5,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_8x11.9" : Params( # note L model height
        L         =11.9,    # overall height
        D         =8.,     # diameter
        A         =8.3,    # base width (x&y)
        H         =9.5,     # max width (x) with pins
        P         =2.2,     # distance between pins
        W         =0.65,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_10x7.7" : Params( # note L model height
        L         =7.7,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_10x7.9" : Params( # note L model height
        L         =7.9,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_10x10" : Params( # note L model height
        L         =10,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_10x10.5" : Params( # note L model height
        L         =10.5,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_10x12.5" : Params( # note L model height
        L         =12.5,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_10x12.6" : Params( # note L model height
        L         =12.6,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_10x14.3" : Params( # note L model height
        L         =14.3,    # overall height
        D         =10.,     # diameter
        A         =10.3,    # base width (x&y)
        H         =12.,     # max width (x) with pins
        P         =4.6,     # distance between pins
        W         =0.9,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_16x17.5" : Params( # note L model height
        L         =17.5,    # overall height
        D         =16.,     # diameter
        A         =16.6,    # base width (x&y)
        H         =18.6,     # max width (x) with pins
        P         =6.5,     # distance between pins
        W         =1.3,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_16x22" : Params( # note L model height
        L         =22.0,    # overall height
        D         =16.,     # diameter
        A         =16.6,    # base width (x&y)
        H         =18.6,     # max width (x) with pins
        P         =6.5,     # distance between pins
        W         =1.3,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_18x17.5" : Params( # note L model height
        L         =17.5,    # overall height
        D         =18.,     # diameter
        A         =19.,    # base width (x&y)
        H         =21.,     # max width (x) with pins
        P         =6.5,     # distance between pins
        W         =1.3,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
    "CP_Elec_18x22" : Params( # note L model height
        L         =22,    # overall height
        D         =18.,     # diameter
        A         =19.,    # base width (x&y)
        H         =21.,     # max width (x) with pins
        P         =6.5,     # distance between pins
        W         =1.3,     # pin width
        PM        =True,   # show/hide pin marker
        rotation  = 180, # rotation if required
    ),
}
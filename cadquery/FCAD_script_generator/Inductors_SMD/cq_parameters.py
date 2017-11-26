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

destination_dir="/Inductors_SMD.3dshapes"

#destination_dir="generated_cap"

### Parametric Values
##
Params = namedtuple("Params", [
    'L',   # package length
    'W',   # package width
    'T',   # package height

    'pb',   # pin band
    'pt',   # pin thickness

    'series',    # Inductor Series
    'modelName', # modelName
    'rotation' # rotation if required
])

all_params_SMD_inductor = {
}

kicad_naming_params_SMD_inductor = {
    "L_Wuerth_MAPI-1610" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:1
        L = 1.60,  # package length 
        W = 1.60,  # package width 
        T = 1.0,  # package height 
 
        pb = 0.5,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-1610',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-2010" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:2
        L = 2.0,  # package length 
        W = 1.6,  # package width 
        T = 1.0,  # package height 
 
        pb = 0.6,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-2010',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-2506" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:3
        L = 2.5,  # package length 
        W = 2.0,  # package width 
        T = 0.6,  # package height 
 
        pb = 0.7,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-2506',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-2508" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:4
        L = 2.5,  # package length 
        W = 2.0,  # package width 
        T = 0.8,  # package height 
 
        pb = 0.7,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-2508',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-2510" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:5
        L = 2.5,  # package length 
        W = 2.0,  # package width 
        T = 1.0,  # package height 
 
        pb = 0.7,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-2510',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-2512" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:6
        L = 2.5,  # package length 
        W = 2.0,  # package width 
        T = 1.2,  # package height 
 
        pb = 0.7,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-2512',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-3010" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:7
        L = 3.0,  # package length 
        W = 3.0,  # package width 
        T = 1.0,  # package height 
 
        pb = 1.2,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-3010',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-3012" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:8
        L = 3.0,  # package length 
        W = 3.0,  # package width 
        T = 1.2,  # package height 
 
        pb = 1.2,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-3012',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-3015" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:9
        L = 3.0,  # package length 
        W = 3.0,  # package width 
        T = 1.5,  # package height 
 
        pb = 1.2,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-3015',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-3020" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:10
        L = 3.0,  # package length 
        W = 3.0,  # package width 
        T = 2.0,  # package height 
 
        pb = 1.2,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-3020',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-4020" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:11
        L = 3.0,  # package length 
        W = 4.0,  # package width 
        T = 2.0,  # package height 
 
        pb = 1.25,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-4020',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-4030" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:12
        L = 3.0,  # package length 
        W = 4.0,  # package width 
        T = 3.0,  # package height 
 
        pb = 1.25,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-4030',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Wuerth_MAPI-4030" : Params( #from http://katalog.we-online.de/en/pbs/WE-MAPI#vs_t1:2_ct:12
        L = 3.0,  # package length 
        W = 4.0,  # package width 
        T = 3.0,  # package height 
 
        pb = 1.25,  # pin band 
        pt = 0.05,   # pin thickness 
 
        series = 'wuerth_MAPI', # series 
        modelName = 'L_Wuerth_MAPI-4030',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Vishay_IHSM-3825" : Params( #from http://www.mouser.com/ds/2/427/ihsm5832-239823.pdf
        L = 9.65,  # package length 
        W = 6.35,  # package width 
        T = 5.72,  # package height 
 
        pb = (1.91,4.32),  # pin band 
        pt = 0.2,   # pin thickness 
 
        series = 'vishay_IHSM', # series 
        modelName = 'L_Vishay_IHSM-3825',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Vishay_IHSM-4825" : Params( #from https://www.vishay.com/docs/34019/ihsm4825.pdf
        L = 12.19,  # package length 
        W = 6.35,  # package width 
        T = 5.72,  # package height 
 
        pb = (1.91,4.32),  # pin band 
        pt = 0.2,   # pin thickness 
 
        series = 'vishay_IHSM', # series 
        modelName = 'L_Vishay_IHSM-4825',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Vishay_IHSM-5832" : Params( #from https://www.vishay.com/docs/34020/ihsm5832.pdf
        L = 14.73,  # package length 
        W = 8.13,  # package width 
        T = 7.24,  # package height 
 
        pb = (2.54,5.46),  # pin band 
        pt = 0.2,   # pin thickness 
 
        series = 'vishay_IHSM', # series 
        modelName = 'L_Vishay_IHSM-5832',  # Model Name 
        rotation = 0   # rotation 
    ),
    "L_Vishay_IHSM-7832" : Params( #from https://www.vishay.com/docs/34021/ihsm7832.pdf
        L = 19.81,  # package length 
        W = 8.13,  # package width 
        T = 7.24,  # package height 
 
        pb = (2.54,5.46),  # pin band 
        pt = 0.2,   # pin thickness 
 
        series = 'vishay_IHSM', # series 
        modelName = 'L_Vishay_IHSM-7832',  # Model Name 
        rotation = 0   # rotation 
    ),
}
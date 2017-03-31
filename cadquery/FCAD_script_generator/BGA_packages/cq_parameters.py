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

destination_dir="/BGA_packages"
# destination_dir="./"
footprints_dir="Housings_BGA.pretty"
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

Params =namedtuple_with_defaults ("Params", [
    'c',    # pin thickness, body center part height
#    'K',    # Fillet radius for pin edges
    'L',    # pin top flat part length (including fillet radius)
    'fp_r', # first pin indicator radius, set to 0.0 to remove first pin indicator
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges
    'cce',  # chamfer of the epad 1st pin corner
    'D',    # body overall lenght
    'E',    # body overall width
    'A1',   # body-board separation
    'A2',   # body height
    'b',    # pin width
    'e',    # pin (center-to-center) distance
    'sp',   # seating plane (pcb penetration)
    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'excluded_pins', #pins to exclude -> None or "internals"
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefixD2 = params.epad[0]
])
    
kicad_naming_params_qfn = {
    'BGA-48_6x8_8.0x9.0mm_Pitch0.8mm': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 9.0,       # body overall length
        E = 8.0,       # body overall width
        A1 = 0.22,  # body-board separation 
        A2 = 0.77,  # body height
        b = 0.5,  # ball pin width diameter
        e = 0.8,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 8,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        excluded_pins = None, #pins to exclude -> None or "internals"
        modelName = 'BGA-48_6x8_8.0x9.0mm_Pitch0.8mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'BGA-256_pitch1mm_dia0.4mm': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 17.0,       # body overall length
        E = 17.0,       # body overall width
        A1 = 0.4,  # body-board separation 
        A2 = 1.13,  # body height
        b = 0.4,  # ball pin width diameter
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 16,  # number of pins along X axis (width)
        npy = 16,  # number of pins along y axis (length)
        excluded_pins = "internals", #pins to exclude -> None or "internals"
        modelName = 'BGA-256_pitch1mm_dia0.4mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'BGA-400-1mm': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 21.0,       # body overall length
        E = 21.0,       # body overall width
        A1 = 0.3,  # body-board separation 
        A2 = 1.8,  # body height
        b = 0.605,  # ball pin width diameter
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        excluded_pins = "internals", #"internals", #pins to exclude -> None or "internals"
        modelName = 'BGA-400-1mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
    'BGA-1156_34x34_35.0x35.0mm_Pitch1.0mm': Params( # from http://cds.linear.com/docs/en/packaging/05081703_C_DC6.pdf
        c = 0.2,        # pin thickness, body center part height
#        K=0.2,          # Fillet radius for pin edges
        L = 0.4,        # pin top flat part length (including fillet radius)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cce = 0.2,      #0.45 chamfer of the epad 1st pin corner
        D = 35.0,       # body overall length
        E = 35.0,       # body overall width
        A1 = 0.3,  # body-board separation 
        A2 = 1.8,  # body height
        b = 0.605,  # ball pin width diameter
        e = 1.0,  # pin (center-to-center) distance
        sp = 0.0, #seating plane (pcb penetration)
        npx = 34,  # number of pins along X axis (width)
        npy = 34,  # number of pins along y axis (length)
        excluded_pins = "internals", #"internals", #pins to exclude -> None or "internals"
        modelName = 'BGA-1156_34x34_35.0x35.0mm_Pitch1.0mm', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = ''
        ),
}

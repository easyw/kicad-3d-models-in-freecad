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
import cq_parameters_sot  # modules parameters
from cq_parameters_sot import *

destination_dir="/Flatpin_packages"
# destination_dir="./"
footprints_dir_diodes="Diodes_SMD.pretty"
##footprints_dir=None #to exclude importing of footprints

kicad_naming_params_diode = {
        'D_SOD-323F': Params( # from http://www.nxp.com/documents/outline_drawing/SOD323F.pdf
        the = 4.0,      # body angle in degrees
        c = 0.2,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = None, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 1.7,       # body length
        E1 = 1.25,       # body width
        E = 2.05,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.73,  # body height
        b = 0.35,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        modelName = 'D_SOD-323F', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_PowerDI-123': Params( # from http://www.diodes.com/_files/datasheets/ds30497.pdf
        the = 4.0,      # body angle in degrees
        c = 0.2,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = None, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 3.0,       # body length
        E1 = 1.93,       # body width
        E = 2.83,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.02,  # body-board separation
        A2 = 0.98,  # body height
        b = 1.0,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = (1.35, 1.1, 0.0, '-topin', 0.0), # e all_params_sod
        excluded_pins = None, #no pin excluded
        modelName = 'D_PowerDI-123', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_SC-80': Params( # from http://www.infineon.com/dgdl/SCD80-Package_Overview.pdf?fileId=5546d462580663ef0158069ef94f041e
        the = 4.0,      # body angle in degrees
        c = 0.13,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = None, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 1.3,       # body length
        E1 = 0.8,       # body width
        E = 1.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.7,  # body height
        b = 0.3,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        modelName = 'D_SC-80', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_SOD-123F': Params( # from http://www.nxp.com/documents/outline_drawing/SOD123F.pdf
        the = 4.0,      # body angle in degrees
        c = 0.2,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = None, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 2.6,       # body length
        E1 = 1.6,       # body width
        E = 2.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.65,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        modelName = 'D_SOD-123F', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_SOD-523': Params( # from http://www.nxp.com/documents/outline_drawing/SOD523.pdf
        the = 4.0,      # body angle in degrees
        c = 0.14,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = None, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 1.2,       # body length
        E1 = 0.8,       # body width
        E = 1.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.63,  # body height
        b = 0.3,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        modelName = 'D_SOD-523', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_SOD-923': Params( # from https://www.nxp.com/docs/en/package-information/SOD923.pdf
        the = 4.0,      # body angle in degrees
        c = 0.12,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = None, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 0.8,       # body length
        E1 = 0.6,       # body width
        E = 0.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.37,  # body height
        b = 0.2,  # pin width
        e = 0.9,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        modelName = 'D_SOD-923', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
        'D_TUMD2': Params( # from http://rohmfs.rohm.com/en/products/databook/package/spec/discrete/diodepkg.pdf
        the = 4.0,      # body angle in degrees
        c = 0.17,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = None, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 1.9,       # body length
        E1 = 1.3,       # body width
        E = 1.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.02,  # body-board separation
        A2 = 0.6,  # body height
        b = 0.8,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = (0.4, 0.8, 0.0, '-topin', 0.0), #
        excluded_pins = None, #no pin excluded
        modelName = 'D_TUMD2', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '../Diodes_SMD.3dshapes/'
        ),
}
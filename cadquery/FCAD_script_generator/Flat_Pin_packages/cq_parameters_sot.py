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

max_cc1 = 1     # maximum size for 1st pin corner chamfer

destination_dir="/Flatpin_packages"
# destination_dir="./"

Params = namedtuple("Params", [
    'the',  # body angle in degrees
    'c',    # pin thickness, body center part height
# automatic calculated    'L',    # pin bottom flat part length (including corner arc)
    'fp_s',  # True for circular pinmark, False for square pinmark (useful for diodes)
    'fp_r', # first pin indicator radius, set to 0.0 to remove first pin indicator
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges

    'D1',   # body lenght
    'E1',   # body width
    'E',    # body overall width
    'A1',   # body-board separation
    'A2',   # body height

    'b',    # pin width
    'e',    # pin (center-to-center) distance

    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'epad',  # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    'excluded_pins', #pins to exclude
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

kicad_naming_params_sot = {
	'Analog_KS-4': Params( # from http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/sc70ks/ks_4.pdf
        the = 8.0,      # body angle in degrees
        c = 0.15,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.25,       # body length
        E1 = 1.7,       # body width
        E = 2.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.1,  # pin width
        e = 0.1,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        modelName = 'Analog_KS-4', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'SOT'
        ),
}
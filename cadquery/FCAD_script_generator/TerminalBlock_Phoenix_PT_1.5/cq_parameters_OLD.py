# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are based on module library values
# Models are representative

## file of parametric definitions
from collections import namedtuple

destination_dir="/TerminalBlock_Phoenix.3dshapes"

Params = namedtuple("Params", [
    'p',      # pitch
    'n',      # number of terminals
    'h',      # height
    'y',      # width in y direction
    'yb'      # distance from pin to rear of terminal (y)
])

kicad_naming_params_phoenix_pt = {
    'TerminalBlock_Phoenix_PT-1,5-2-5.0-H_1x02_P5.00mm_Horizontal': Params(	
        p = 5.0,
        n = 2,
        h = 11.4
        y = 8.3,
        yb = 4.0,
        color = 'light green'
    ),
}
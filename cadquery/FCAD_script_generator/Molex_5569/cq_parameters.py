# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Adapted for Molex 5569 by timtashpulatov

# file of parametric definitions

from collections import namedtuple

destination_dir = "/Connectors_Molex"

# Parametric Values
#
Params = namedtuple("Params", [
    'N',   # number of pins
    'modelName'  # modelName
])

all_params_molex_5569 = {
    "5569-2A2": Params(
        N=2,
        modelName='Molex_5569-2A2'  # Model Name
        ),
    "5569-4A2": Params(
        N=4,
        modelName='Molex_5569-4A2'  # Model Name
        ),
    "5569-6A2": Params(
       N=6,
       modelName='Molex_5569-6A2'  # Model Name
        ),
    "5569-8A2": Params(
       N=8,
       modelName='Molex_5569-8A2'  # Model Name
       ),
}

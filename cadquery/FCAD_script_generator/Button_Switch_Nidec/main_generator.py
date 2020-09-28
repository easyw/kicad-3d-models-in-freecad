import cadquery as cq
from Helpers import show


__title__ = "make assorted rotary coded switches (type Nidec SH70xx) 3D models"
__author__ = "maurice, hyOzd, Stefan, Terje, mountyrox"
__Comment__ = 'make make assorted rotary coded switches (type Nidec SH70xx) 3D models exported to STEP and VRML'

___ver___ = "1.0.0 21/09/2020"

import sys, os

def reload_lib(lib):
    if (sys.version_info > (3, 0)):
        import importlib
        importlib.reload(lib)
    else:
        reload (lib)


script_dir  = os.path.dirname(os.path.realpath(__file__))
scripts_root = script_dir.split(script_dir.split(os.sep)[-1])[0]

print (script_dir)
sys.path.append(script_dir)
sys.path.append(scripts_root + "_tools")

import cq_model_generator
reload_lib(cq_model_generator)
from cq_model_generator import All, ModelGenerator

import cq_base_model
reload_lib(cq_base_model)

import cq_parameters
reload_lib(cq_parameters)
from cq_parameters import variableParams

import cq_base_model
reload_lib(cq_base_model)

import cq_nidec_SH70xx_models
reload_lib(cq_nidec_SH70xx_models)


series = [
  cq_nidec_SH70xx_models.switchNidecSH70x0x
 ]

family = All # set to All generate all series

options = sys.argv[2:] if len(sys.argv) >= 3 else []
#options = ["7010C"]

if options != []:
    if options[0] in cq_parameters.variableParams().base_params: 
        family = 0  # we only have one item in member series

gen = ModelGenerator(scripts_root, script_dir, saveToKicad=False)
#gen.kicadStepUptools = False
gen.setLicense(ModelGenerator.alt_license)
gen.makeModels(options, series, family, cq_parameters.variableParams())


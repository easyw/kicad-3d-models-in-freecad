# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating PDIP models in X3D format
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are a FreeCAD & cadquery tools                                     *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating DIP socket models in STEP AP214           *
#*   Copyright (c) 2017                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
#* Terje Io https://github.com/terjeio                                      *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Lesser General Public License (LGPL)     *
#*   as published by the Free Software Foundation; either version 2 of      *
#*   the License, or (at your option) any later version.                    *
#*   for detail see the LICENCE text file.                                  *
#*                                                                          *
#*   This program is distributed in the hope that it will be useful,        *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
#*   GNU Library General Public License for more details.                   *
#*                                                                          *
#*   You should have received a copy of the GNU Library General Public      *
#*   License along with this program; if not, write to the Free Software    *
#*   Foundation, Inc.,                                                      *
#*   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           *
#*                                                                          *
#****************************************************************************

__title__ = "make assorted DIP part 3D models"
__author__ = "maurice, hyOzd, Stefan, Terje"
__Comment__ = 'make make assorted DIP part 3D models exported to STEP and VRML for Kicad StepUP script'

___ver___ = "1.0.0 30/11/2017"

#
# 2017-11-25: mods by Terje: made generic in order to support class based model scripts
#

import sys, os

import exportPartToVRML as expVRML
import shaderColors
import re, fnmatch

# maui start
import FreeCAD #, Draft, FreeCADGui
#import ImportGui
import FreeCADGui
Gui = FreeCADGui
#from Gui.Command import *

from cq_base_parameters import CaseType

if FreeCAD.GuiUp:
    from PySide import QtGui

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, saveFCdoc, z_RotateObject, Color_Objects, \
 checkRequirements

import add_license

# Sphinx workaround #1
try:
    QtGui
except NameError:
    QtGui = None
#

try:
    # Gui.SendMsgToActiveView("Run")
#    from Gui.Command import *
    Gui.activateWorkbench("CadQueryWorkbench")
    import cadquery
    cq = cadquery
#    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

# Sphinx workaround #2
try:
    cq
    checkRequirements(cq)
except NameError:
    cq = None
#

#checking requirements

try:
    close_CQ_Example(FreeCAD, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"

global All
All = None

global kicadStepUptools

def clear_console():
    r"""Clears the FreeCAD Report & Python consoles
    """
    mw = Gui.getMainWindow()
    mw.findChild(QtGui.QPlainTextEdit, "Python console").clear()
    mw.findChild(QtGui.QTextEdit, "Report view").clear()

class ModelGenerator:
    r"""A class for creating 3D models

    :param scripts_root: the directory where the script
    :param   script_dir: the directory where the script resides, used for adding script source link in the model files. None to disable
    :param  saveToKicad:  * True: write .step and .wrl files directly to KISYS3DMOD folder if it exists.
                          * False: write to the _3Dmodels folder relative to *scripts_root*
    :type   saveToKicad: ``boolean``
    :param  kicadStepUp:  * True: add footprint to the created models
                          * False: do not add
                          * None: add footprint when creating single footprint
    :type   kicadStepUp: ``boolean``
    """

    alt_license = [
        "*", # this line is replaced with copyright string - do NOT set to empty
        "---",
        "This work is licensed under the Creative Commons CC-BY-SA 4.0 License with the following exception:",
        "To the extent that the creation of electronic designs that use 'Licensed Material'",
        "can be considered to be 'Adapted Material', then the copyright holder waives",
        "article 3 of the license with respect to these designs and any generated files",
        "which use data provided as part of the 'Licensed Material'.",
        "",
        "https://creativecommons.org/licenses/by-sa/4.0/legalcode",
        "---",
        "Please refer to http://kicad-pcb.org/libraries/license/ for further clarification of the exception.",
        "---",
        "",
        "Risk disclaimer:",
        "*USE 3D CAD DATA AT YOUR OWN RISK*",
        "*DO NOT RELY UPON ANY INFORMATION FOUND HERE WITHOUT INDEPENDENT VERIFICATION.*",
    ]

    def __init__(self, scripts_root, script_dir=None, saveToKicad=True, kicadStepUp=None):
        self.script_dir = script_dir
        if self.script_dir == "" or self.script_dir is None:
            self.script_dir = None
        self.models_dir = os.getenv('KISYS3DMOD') if saveToKicad else None
        if self.models_dir is None:
            self.models_dir = scripts_root + "_3Dmodels"
        self.models_src_dir = scripts_root + "_3DmodelsFCStd"
        self.footprints_dir = os.getenv('KISYSMOD')
        if self.footprints_dir is not None and not os.path.isdir(self.footprints_dir):
            self.footprints_dir = None
        self.kicadStepUptools = kicadStepUp
        self.license = None
        self.scriptsource = "https://github.com/easyw/kicad-3d-models-in-freecad/tree/master/cadquery/FCAD_script_generator/"

    def getOptions (self, argv):
        r"""get options from sys.argv ready to use as the *options* parameter for the :func:`makeModels` method

        :param  argv: usually sys.argv
        :type   argv: ``list of str``

        :rtype:  ``list of str``

        """
        return argv[2:] if len(argv) >= 3 else []

    def setLicense(self, license):
        r"""set the license text to be added to the created models, default is to use the text from add_license.py

        :param  license: license text
        :type   license: ``list of str``

        """
        self.license = license

    def setScriptSource(self, url):
        r"""set the url (link) to the root project folder, default is easyw's script source project on github

        .. note:: This will only be added if the default license text is used and if so the script folder name will be automatically appended to the url

        :param  url: script source url
        :type   url: ``str``

        """
        self.scriptsource = "" if url is None else url

    def makeModel(self, models_dir, genericName, model, keepDocument=True, verbose=False):
        r"""Creates a model by calling an instance of a model generator class and writes out the model files

        .. note:: normally this method will be called by :func:`makeModels` but may be used directly

        :param models_dir:
            directory to write the created step and wrl files
        :type models_dir: ``str``

        :param genericName:
            the generic name from the base parameter list, may be used to create the model name
        :type  genericName: ``str``

        :param model:
            an instance of the model class to use
        :type   model: ``class instance`` inherited from :class:`cq_base_model.PartBase`

        :param keepDocument:
            * True: the FreeCAD document will shown after it is created, optionally with kicadStepUptools activated
            * False: the document window will be closed
        :type  keepDocument: ``boolean``

        """

        global kicadStepUptools

        modelName = model.makeModelName(genericName)

        FreeCAD.Console.PrintMessage('\r\n' + modelName)

        if model.make_me != True:
            FreeCAD.Console.PrintMessage(' - not made')
            return

        CheckedmodelName = modelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
        FreeCAD.newDocument(CheckedmodelName)
        FreeCAD.setActiveDocument(CheckedmodelName)
        Gui.ActiveDocument = Gui.getDocument(CheckedmodelName)

        model.make()

        doc = FreeCAD.ActiveDocument
        objs = GetListOfObjects(FreeCAD, doc)

        material_substitutions = {}

        for i in range(0, len(objs)):
            Color_Objects(Gui, objs[i], shaderColors.named_colors[model.color_keys[i]].getDiffuseFloat())
            material_substitutions[Gui.ActiveDocument.getObject(objs[i].Name).DiffuseColor[0][:-1]] = model.color_keys[i]

        if verbose:
            expVRML.say(material_substitutions)
            expVRML.say(model.color_keys)
            expVRML.say(model.offsets)

        doc.Label = CheckedmodelName

        while len(objs) > 1:
            FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
            del objs
            objs = GetListOfObjects(FreeCAD, doc)

        objs[0].Label = CheckedmodelName
        restore_Main_Tools()

        #rotate if required
        if (model.rotation != 0):
            z_RotateObject(doc, model.rotation)

        s = objs[0].Shape
        shape = s.copy()
        shape.Placement = s.Placement;
        shape.translate(model.offsets)
        objs[0].Placement = shape.Placement

        out_dir = models_dir + os.sep + model.destination_dir
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        # Export STEP model
        exportSTEP(doc, modelName, out_dir)

        license_txt = list(add_license.LIST_int_license if self.license is None else self.license) # make a copy to avoid modifying the original
        license_txt.append("")
        license_txt.append("")
        if self.scriptsource != "" and self.script_dir is not None:
            license_txt.append("Generated by script, source at:")
            license_txt.append(self.scriptsource + self.script_dir.split(os.sep)[-1])
            license_txt.append("")

        if verbose:
            expVRML.say("")

        add_license.addLicenseToStep(out_dir + os.sep, modelName + ".step", license_txt, model.licAuthor, model.licEmail, model.licOrgSys, model.licOrg, model.licPreProc)

        # Scale and export Vrml model
        scale = 1.0 / 2.54
        objs = GetListOfObjects(FreeCAD, doc)
        if verbose:
            expVRML.say("######################################################################")
            expVRML.say(objs)
            expVRML.say("######################################################################")
        export_objects, used_color_keys = expVRML.determineColors(Gui, objs, material_substitutions)
        export_file_name = out_dir + os.sep + modelName + '.wrl'
        colored_meshes = expVRML.getColoredMesh(Gui, export_objects, scale)
        expVRML.writeVRMLFile(colored_meshes, export_file_name, used_color_keys, license_txt)

        # Save the doc in native FC format
        out_dir = self.models_src_dir + os.sep + model.destination_dir
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        saveFCdoc(FreeCAD, Gui, doc, modelName, out_dir)

        # Place on footprint for verification
        if keepDocument and model.footprints_dir is not None and self.footprints_dir is not None:

            sys.argv = ["fc", "dummy", self.footprints_dir + os.sep + model.footprints_dir + os.sep + modelName, "savememory"]

            if verbose:
                expVRML.say('Footprint: ' + sys.argv[2])

            if self.kicadStepUptools is None:
                try:
                    import kicadStepUptools
                    expVRML.say("ksu present!")
                    self.kicadStepUptools = True
                    kicadStepUptools.KSUWidget.close()
                    #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
                    #kicadStepUptools.KSUWidget.destroy()
                    #for i in QtGui.qApp.topLevelWidgets():
                    #    if i.objectName() == "kicadStepUp":
                    #        i.deleteLater()
                    #kicadStepUptools.KSUWidget.close()
                except:
                    self.kicadStepUptools = False
                    expVRML.say("ksu not present")

            if not self.kicadStepUptools == False:
                kicadStepUptools.KSUWidget.close()
                reload(kicadStepUptools)
                kicadStepUptools.KSUWidget.close()
                #kicadStepUptools.KSUWidget.setWindowState(QtCore.Qt.WindowMinimized)
                #kicadStepUptools.KSUWidget.destroy()

        #display BBox
        if keepDocument:
            Gui.activateWorkbench("PartWorkbench")
            Gui.SendMsgToActiveView("ViewFit")
            Gui.activeDocument().activeView().viewAxometric()
        else:
            doc=FreeCAD.ActiveDocument
            FreeCAD.closeDocument(doc.Name)

    def makeModels(self, options, series, family, params, kicadStepUptools=None, verbose=False):
        r"""Instantiates model creator classes and calls :func:`makeModel` repeatedly to create model files

        This is the main entry point to use for creating models

        :param options:
            * options[0]:
                * empty - create default model from all *series* when *family* is None, otherwise the default model for a single *series*
                * 'all' - generate all models
                * 'allsmd' - generate all SMD style models
                * 'list' - list all model names
                * regexp - a filter to select the models to create
        :type options: ``str``

        :param series:
            list of part creator classes inherited from :class:`cq_base_model.PartBase`
        :type  series: ``list of classes``

        :param family:
            index into the list of parameter classes (series) None if all
        :type  family: ``integer or None``

        :param params:
            instance of the class used to hold part parameters
        :type  params: ``class instance`` inherited from :class:`cq_base_model.PartBase`

        Example::

            import sys, os

            script_dir  = os.path.dirname(os.path.realpath(__file__))
            scripts_root = script_dir.split(script_dir.split(os.sep)[-1])[0]

            sys.path.append(script_dir)
            sys.path.append(scripts_root + "\_tools")

            import cq_model_generator
            from cq_base_model import *

            class my_part (PartBase)
                ...

            class my_part_params (PartParametersBase)
                ...

            family = 0 # set to None to generate all series

            series = [
              my_part
            ]

            generator = cq_model_generator.ModelGenerator(scripts_root, script_dir)

            options = generator.getOptions(sys.argv)

            generator.make_models(options, series, family, my_part_params())

        """

        clear_console()
        FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

        if verbose:
            expVRML.say(self.models_dir)
            expVRML.say(options)

        models_made = 0

        if len(options) > 0 and not params.base_params.has_key(options[0]):

            models = params.getAllModels(series)

            if options[0] == "list":
                for variant in sorted(models):
                    models_made = models_made + 1
                    expVRML.say(variant + "  ") # added spaces for pasting into .md file
            else:
                buildAllSMD = options[0] == "allsmd"
                qfilter = '*' if options[0] == "all" or options[0] == "allsmd" else options[0]
                qfilter = re.compile(fnmatch.translate(qfilter))
                for variant in models.keys():
                    if qfilter.match(variant):
                        params = models[variant].params
                        model = models[variant].model(params)
                        if (buildAllSMD == False or params.type == CaseType.SMD) and model.make_me:
                            models_made = models_made + 1
                            self.makeModel(self.models_dir, variant, model, keepDocument=False, verbose=verbose)
        else:

            if family == All:

                models = params.getSampleModels(series)

                for variant in models.keys():
                    params = models[variant].params
                    model = models[variant].model(params)
                    if model.make_me:
                        models_made = models_made + 1
                        self.makeModel(self.models_dir, variant, model, keepDocument=True, verbose=verbose)
                    else:
                        FreeCAD.Console.PrintMessage('\r\n' + model.makeModelName(variant) + ' - not made')

            else:

                variant_to_build = "" if len(options)== 0 else options[0]
                if variant_to_build == "":
                    FreeCAD.Console.PrintMessage('No variant name is given! building default variants')
                for i in range(family, family + 1):
                    variant = series[i].default_model if variant_to_build == "" else variant_to_build
                    model = params.getModel(series[i], variant)
                    if model != False:
                        models_made = models_made + 1
                        self.makeModel(self.models_dir, variant, model, keepDocument=True, verbose=verbose)
                    else:
                        FreeCAD.Console.PrintMessage('\r\n' + variant + ' - not made')

        if models_made == 0:
            FreeCAD.Console.PrintMessage('\r\nDone - no models matched the provided filter!')
        else:
            FreeCAD.Console.PrintMessage('\r\nDone - models made: ' + str(models_made))

        sys.argv = [] # clear, running kicadStepUptools changes values

### EOF ###

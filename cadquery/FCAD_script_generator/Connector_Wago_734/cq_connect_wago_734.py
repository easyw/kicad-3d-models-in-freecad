#!/usr/bin/python
# -*- coding: utf8 -*-
#
## Dimensions are from data sheets given in the settings of the corresponding KiCad footprint:
##  http://www.farnell.com/datasheets/2157639.pdf
## Dimensions not given in the data sheet were estimeted from the drawings.
#
# 
## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py all

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are a FreeCAD & cadquery tools                                     *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating Wago connector 3D models in STEP AP214    *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
#*                                                                          *
#*   Copyright (c) 2020                                                     *
#* Mountyrox   https://github.com/mountyrox                                 *
#*                                                                          *
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

import collections
from collections import namedtuple

import cadquery as cq
from Helpers import show

import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui

import shaderColors
import exportPartToVRML as expVRML

# Import cad_tools
import cq_cad_tools
# Reload tools
from cq_cad_tools import reload_lib
reload_lib(cq_cad_tools)

# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, z_RotateObject, Color_Objects, restore_Main_Tools, exportSTEP, saveFCdoc


DestinationDir = "Connector_Wago.3dshapes"


class cqMakerWagoConn734 ():
    r"""A class for creating a 3D model of a Wago connector type 734.
    :param parameter: namedtuple containing the variable parameter for building the 3D model.
    :type  parameter: ``partConnWago734.Params``

    """
    
    def __init__(self, parameter):
        self.num_pins = parameter.num_pins
        self.isVertical = True if parameter.ori == 'Vertical' else False

        # Wago fixed dimensions from data sheet: http://www.farnell.com/datasheets/2157639.pdf
        self.pin_pitch = 3.5
        self.body_height = 10.3
        self.body_width = 8.5
        self.body_lenght = (self.num_pins - 1) * self.pin_pitch + 5.9  # formula from data sheet 
        self.body_thickness_x = 1.0
        self.body_thickness_y = 2.0
        self.body_thickness_z = 2.5
        self.pin_to_body_front = 4.35 if  self.isVertical else 9.3
        self.body_offset_x = 0.15     # 5.9 (see body length) / 2 - 2.8 (pin 1 to left side of body from data sheet)
        self.body_offset_y = (self.body_width / 2.0 - self.pin_to_body_front) if self.isVertical else 0.0  # the y-shift of horizontal connectors will be done after 90 deg rotation
        self.body_offset = (self.body_offset_x, self.body_offset_y, 0.0)
        self.body_guide_notch_width = 2.0  # inner guide notches
        self.body_side_pocket_width = 5.4  # outer pocket at left and right side of housing

        self.rotation = 0
        self.make_me = True

        self.pin_length_below_body = 4.5 if self.isVertical else 3.8
        self.pin_width = 1.0
        self.pin_thickness = 1.0
        self.pin_length = 12.7 if self.isVertical else 8.15
        self.first_pin_pos = (-self.pin_pitch * (self.num_pins / 2.0  - 0.5), 0.0)
        self.pin_pockets_width = 2.8   # pockets at pin positions at the back, front and bottom of housing
        self.pin_length_inside_body = self.pin_length - self.pin_length_below_body if self.isVertical else 8.2


        offsetX = (-self.first_pin_pos[0])
        self.offsets = (offsetX, 0.0, 0.0)

        self.body_color_key = 'white body'      
        self.pin_color_key = 'gold pins' 


    def get_dest_3D_dir(self):
        r"""get the destination directory for the 3D model export

        :rtype: string
        """
        return DestinationDir


    def isValidModel (self):
        """ create the plastic body of the Wago connector
        :rtype: ``solid``
        """
        return self.make_me


    def _union_all(self, objects):
        o = objects[0]
        for i in range(1, len(objects)):
            o = o.union(objects[i])
        return o

    def _mirror(self, obj, pins=None, pitch=None):

        if pins is None:
            pins = self.num_pins // 2

        if pitch is None:
            pitch = self.pin_pitch

        objs = [obj]
        for i in range(2, pins + 1):
            objs.append(obj.translate((-pitch * (i - 1), 0, 0)))

        return self._union_all(objs)

    def __innerPocket (self):
        """ create a body to be used for cutting the inner part of the connector.
        :rtype: ``solid``
        """
        body = cq.Workplane("XY").workplane(offset=self.body_thickness_z)\
            .rect(self.body_lenght - 2.0 * self.body_thickness_x, self.body_width - 2.0 * self.body_thickness_y).extrude(self.body_height)

        l = self.body_guide_notch_width
        w = self.body_thickness_y - 0.4

        # guide notches on front of body
        body_guide_notch = cq.Workplane("XY").workplane(offset=self.body_thickness_z)\
            .rect(l, w).extrude(self.body_height)

        body = body.union(body_guide_notch.translate(((self.body_lenght - l) / 2.0 - self.body_thickness_x,  -((self.body_width + w) / 2.0 - self.body_thickness_y), 1.8 )))
        body = body.union(body_guide_notch.translate((-((self.body_lenght - l) / 2.0 - self.body_thickness_x) + self.pin_pitch/2.0,  -((self.body_width + w) / 2.0 - self.body_thickness_y), 1.8 )))

        # guide notches at sides of body
        body_guide_notch = cq.Workplane("XY").workplane(offset=self.body_thickness_z)\
            .rect(self.body_lenght - 2.0 * self.body_thickness_x + 0.8, l).extrude(self.body_height)
        
        # the side guide notches are correlated to the positions of the pins, thus we must do an inverse shift of the later performed body offset in y-direction
        body = body.translate((0.0, -self.body_offset_y, 0.0))
        
        body = body.union(body_guide_notch)

        return body


    def __outerPocketLeft (self):
        """ create a body to be used for cutting the pockets at outer left side of the connector.
        :rtype: ``solid``
        """
        body_i = cq.Workplane("YZ").workplane(offset=-self.body_lenght / 2.0)\
            .rect(self.body_guide_notch_width, 2.0 * (self.body_height - self.body_thickness_y)).extrude(self.body_thickness_x)

        body_o = cq.Workplane("YZ").workplane(offset=-self.body_lenght / 2.0 + 0.4)\
            .rect(self.body_side_pocket_width, 2.0 * (self.body_height - self.body_thickness_y)).extrude(-self.body_thickness_x)

        return body_i.union(body_o)


    def makePlasticCase (self):
        """ create the plastic body of the Wago connector
        :rtype: ``solid``
        """
        # make the basic body of a vertical connector
        body = cq.Workplane("XY").rect(self.body_lenght, self.body_width).extrude(self.body_height)

        # cut the inner part of the connector and shift the body to place pin 1 at (0,0)
        body = body.cut(self.__innerPocket()).fillet(0.1)\
            .cut(self.__outerPocketLeft())\
            .cut(self.__outerPocketLeft().mirror("YZ"))\
            .translate(self.body_offset)

        # the following unions and cuts are all relative to the positions of the pins and not relative to the center of the body.
        # make a rectangle pad for each pin at the inner bottom of the connector
        pin_pad = cq.Workplane("XY").workplane(offset=self.body_thickness_z)\
            .rect(self.pin_pockets_width, self.pin_pockets_width).extrude(1.0)

        allPads = self._duplicatePins (pin_pad.translate(self.first_pin_pos))

        body = body.union(allPads)

        # make a pocket at each pin position at the back (for vertical orientation of the housing) of the connector housing
        pin_pocket_back = cq.Workplane("XZ")\
            .rect(self.pin_pockets_width, self.body_height * 2.0 - self.body_thickness_y).extrude(self.body_thickness_y)

        allPockets = self._duplicatePins (pin_pocket_back.translate(self.first_pin_pos).translate((0.0, (self.body_height - self.body_thickness_y) / 2.0 + 0.4, 0.0)))
        body = body.cut(allPockets)

        # make a pocket at each pin position at the front (for vertical orientation of the housing) of the connector housing
        pin_pocket_front_a = cq.Workplane("XZ")\
            .rect(self.pin_pockets_width/2.0, self.body_height * 2.0 - self.body_thickness_y).extrude(-self.body_thickness_y)
        pin_pocket_front_b = cq.Workplane("XZ")\
            .rect(self.pin_pockets_width, self.body_height * 2.0 - self.body_thickness_y).extrude(-self.body_thickness_y)\
            .translate((0.0, -1.3, 0.0))
        pin_pocket_front = pin_pocket_front_a.union(pin_pocket_front_b)

        allPockets = self._duplicatePins (pin_pocket_front.translate(self.first_pin_pos).translate((0.0, -(self.body_height - self.body_thickness_y) / 2.0 - 0.6, 0.0)))

        # for connectors with more or equal 3 pins the most left and most right front pocket has haf height only 
        if self.num_pins >= 3:
            # make body to cut the hight of the most left pocket
            body_cut = cq.Workplane("XY").workplane(offset=self.body_height / 2.0)\
                .rect(self.pin_pockets_width, self.body_width*2.0).extrude(self.body_height)\
                .translate(self.first_pin_pos)
            # mirror the upper body to cut the height of the most right pocket 
            body_cut = body_cut.union(body_cut.mirror("YZ"))
            
            allPockets = allPockets.cut(body_cut)

        body = body.cut(allPockets)

        # make pockets at each pin position at the bottom (for vertical orientation of the housing) of the connector housing
        pin_pocket_bottom = cq.Workplane("XY")\
            .rect(self.pin_pockets_width, self.body_width * 2.0).extrude(0.8)
        allPockets = self._duplicatePins (pin_pocket_bottom.translate(self.first_pin_pos))
        body = body.cut(allPockets)

        # if connector is horizontal it must be rotated and shifted
        if not self.isVertical:
            body = body.rotate((0,0,0), (1,0,0), 90.0)\
                .translate((0.0, self.body_height - self.pin_to_body_front, self.body_width / 2.0))

        return body


    def _duplicatePins (self, onePin, noPins=None, pitch=None):
        r"""Duplicates all pins from first pin.

        :param onePin: The first pin of the model
        :type  onePin: ``solid``

        :param codeFormat:
        :type  codeFormat: ``CodeFormat`` default: ``CodeFormat.REAL``
        :return: all pins
        :rtype: ``solid``
        """

        if noPins is None:
            noPins = self.num_pins
        
        if pitch is None:
            pitch = self.pin_pitch

        pins = [onePin]       
        for i in range (1, noPins):
            nextPin = (onePin.translate((pitch * (i), 0, 0)))
            pins.append(nextPin)
        return self._union_all(pins)


    def _make_straight_pin (self):
        """ create a straigth pin centered at (0, 0, -self.pin_length_below_body) for vertical connectors.
        :rtype: ``solid``
        """
        body = cq.Workplane("XY").rect(self.pin_width, self.pin_thickness).extrude(self.pin_length)\
            .edges("<Z").chamfer(1.0, self.pin_width/4.0)\
            .edges(">Z").chamfer(self.pin_width/4.0)\
            .translate((0.0, 0.0, -self.pin_length_below_body))

        return body


    def _make_angled_pin (self):
        """ create an angled pin centered at (0, 0, -self.pin_length_below_body) for horizontal connectors.
        :rtype: ``solid``
        """
        r_mean = self.pin_thickness * 0.75  # center pin radius
        
        # path for a sweep 
        path = cq.Workplane("YZ").lineTo(0.0, self.pin_length - r_mean)\
            .radiusArc((-r_mean, self.pin_length), -r_mean)\
            .lineTo(-self.pin_length_inside_body, self.pin_length+0.0)     
       

        body = cq.Workplane("XY").rect(self.pin_width, self.pin_thickness).sweep(path)\
            .edges("<Z").edges(">X").chamfer(self.pin_width/4.0, 1.0)\
            .edges("<Z").edges("<X").chamfer(self.pin_width/4.0, 1.0)\
            .edges("<Z").edges("<Y").chamfer(1.0, self.pin_width/4.0)\
            .edges("<Z").edges(">Y").chamfer(self.pin_width/4.0, 1.0)\
            .edges("<Y").chamfer(self.pin_width/4.0)\
            .translate((0.0, 0.0, -self.pin_length_below_body))
            # I don't know why the <Z chamfer must be done in four steps with mixed parameter. In function _make_straight_pin it worked with one command????
        return body


    def make_pins(self):
        r"""Creates all pins of the connector depending on the value of ``ori`` (``Vertical`` or ``Horizontal``) defined in ``parameter``.
        :rtype: ``solid`` of all pins
        """
        # make first pin, depending on the orientation of connector
        firstPin = self._make_straight_pin () if self.isVertical else self._make_angled_pin ()
        allPins = self._duplicatePins (firstPin.translate(self.first_pin_pos))        

        return (allPins)


    def make_3D_model(self):
        """ create a 3D model of a WAGO serie 734 connector.  Two parts will be created: plastic body, pins.

        This function will be called from the main_generator script.
        :return: list of the materials used for the 3D model
        :rtype: ``dictionary`` 
        """
        destination_dir = self.get_dest_3D_dir()
        
        case = self.makePlasticCase()
        pins = self.make_pins()
        show(case)
        show(pins)
     
        doc = FreeCAD.ActiveDocument
        objs = GetListOfObjects(FreeCAD, doc)

     
        body_color = shaderColors.named_colors[self.body_color_key].getDiffuseFloat()
        pin_color = shaderColors.named_colors[self.pin_color_key].getDiffuseFloat()

        # must be the same order of the above show(..) calls
        Color_Objects(Gui, objs[0], body_color)
        Color_Objects(Gui, objs[1], pin_color)

        col_body = Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
        col_pin = Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
        
        material_substitutions={
            col_body[:-1]:self.body_color_key,
            col_pin[:-1]:self.pin_color_key,
        }
        
        expVRML.say(material_substitutions)

        # fuse all parts of model
        while len(objs) > 1:
                FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
                del objs
                objs = GetListOfObjects(FreeCAD, doc)

        #rotate if required
        if (self.rotation != 0):
            z_RotateObject(doc, self.rotation)

        s = objs[0].Shape
        shape = s.copy()
        shape.Placement = s.Placement;
        shape.translate(self.offsets)
        objs[0].Placement = shape.Placement

        return material_substitutions



class partConnWago734():

    Params = namedtuple("Params", [
        'modelName',		 # modelName, must correspond to 3D file name defined in KiCad footprint
        'num_pins',          # number of pins
        'ori'                # Orientation : Vertical or Horizontal
    ])


    def __init__(self):
        self._createAllParams ()



    def _createPartName (self, num_pin, ori):
        """ create the name of the Wago connector, depending on the number of pins and type of orientation.
        :param num_pin: number of pins of connector
        :type num_pin: ``int``
        :param ori: Orientation of connecto. Valid values: ``Vertical`` or ``Horizontal``
        :type ori: ``string``

        :rtype: ``string``
        """
        serie = 130 if ori == 'Vertical' else 160
        return "Wago_734-{0}_1x{1:02d}_P3.50mm_{2}".format (serie + num_pin, num_pin, ori)

    def _createAllParams (self):
        """ create a dictionary ``partConnWago734.all_params`` of all models to make. The key value is the file name of the Wago connector, 
        the value is a namedtuple of type ``partConnWago734.Params``.

        :rtype: No return value
        """
        invalidPinNumber = [15, 17, 19, 21, 22, 23]
        self.all_params = {}
        for ori in ['Vertical', 'Horizontal']:
            for i in range (2, 25):
                if i not in invalidPinNumber:
                    name = self._createPartName (i, ori)
                    self.all_params [name] = self.Params (modelName = name, num_pins = i, ori = ori)


    def model_exist(self, modelName):
        r"""checks if the model with given name exists. i.e. is part of ``all_params``
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :return: True if model exists, otherwise False
        :rtype: ``boolean``
        """
        for n in self.all_params:
            if n == modelName:
                return True
                
        return False
        
        
    def get_param_list_all(self):
        r"""returns a list of all model variants defined in `all_params``
        
        :rtype: ``list``
        """
        list = []
        for n in self.all_params:
            list.append(n)
        
        return list


    def getModelVariant (self, modelName):
        r"""returns the class for building a 3D model, initialized with the parameters connected to the given modelName.
        
        :param modelName: name of the model as defined in ``all_params``
        :type modelName: ``string``
        :rtype: ``class cqMakerWagoConn734``
        """
        return cqMakerWagoConn734 (self.all_params[modelName]) 


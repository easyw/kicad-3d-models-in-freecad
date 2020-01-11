# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
# This is a
#
## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module
#
## to run the script just do: freecad main_generator.py modelName
## e.g. c:\freecad\bin\freecad main_generator.py DIP8
#
## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script
#
#* These are a FreeCAD & cadquery tools                                     *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating QFP/SOIC/SSOP/TSSOP models in STEP AP214  *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
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

#
# Most of these models are based on 
# http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
#

import cq_common  # modules parameters
from cq_common import *

import sys
import math


class cq_dsub():

    def __init__(self):
        self.body_top_color_key  = 'white body'         # Top color
        self.body_color_key      = 'metal grey pins'    # Body color
        self.pin_color_key       = 'metal grey pins'    # Pin color
        self.npth_pin_color_key  = 'black body'         # NPTH Pin color

    def set_colors(self, params):
        if params.body_top_color_key != None:
            self.body_top_color_key = params.body_top_color_key
        #
        if params.body_color_key != None:
            self.body_color_key = params.body_color_key
        #
        if params.pin_color_key != None:
            self.pin_color_key = params.pin_color_key
        #
        if params.npth_pin_color_key != None:
            self.npth_pin_color_key = params.npth_pin_color_key
        #


    def get_model_name(self, modelID, gender):
        for n in self.all_params:
            if n == modelID:
                if self.all_params[modelID].serie == 3:
                    if gender == 'male':
                        return 'DSUB-' + str(self.all_params[modelID].pin[1]) + '-HD_Male_' + self.all_params[modelID].modelName
                    else:
                        return 'DSUB-' + str(self.all_params[modelID].pin[1]) + '-HD_Female_' + self.all_params[modelID].modelName
                else:
                    if gender == 'male':
                        return 'DSUB-' + str(self.all_params[modelID].pin[1]) + '_Male_' + self.all_params[modelID].modelName
                    else:
                        return 'DSUB-' + str(self.all_params[modelID].pin[1]) + '_Female_' + self.all_params[modelID].modelName
        return 'xxUNKNOWNxxx'


    def get_dest_3D_dir(self, modelID):
        for n in self.all_params:
            if n == modelID:
                if self.all_params[modelID].dest_dir_prefix != None:
                    return self.all_params[modelID].dest_dir_prefix

        return 'Connector_Dsub'


    def model_exist(self, modelID):
        for n in self.all_params:
            if n == modelID:
                return True
                
        return False


    def get_list_all(self):
        list = []
        for n in self.all_params:
            list.append(n)
        
        return list


    def set_rotation(self, params):

        #
        # serie = 2, two lines of pins
        # serie = 3, three lines of pins
        #
        # pin = ['round' ...  The pins are straight down
        # pin = ['round1' ...  The pins are bend 90 degree, this will include a rotation of 90 of the case
        #
        # npthserie = [1]   No black block behind the case
        # npthserie = [2, AA, BB, CC]   A block behind the case, the case is moved a distance of AA, 
        #                               BB is the block size in Y led, 
        #                               CC is the mounting holes distance from pin rom 1
        #                               
        # npthserie = [3, AA]           No black block behind the case, the case is moved a distance of AA
        #
        self.rotatex = 0.0          # Rotation around x-axis if required
        self.rotatey = 0.0          # Rotation around x-axis if required
        self.rotatez = 0.0          # Rotation around y-axis if required
        
        if params.pin[0] == 'round1':
            self.rotatex = 90.0     # Rotation around x-axis if required


    def set_translate(self, params):

        #
        # serie = 2, two lines of pins
        # serie = 3, three lines of pins
        #
        # pin = ['round' ...  The pins are straight down
        # pin = ['round1' ...  The pins are bend 90 degree, this will include a rotation of 90 of the case
        #
        # npthserie = [1]   No black block behind the case
        # npthserie = [2, AA, BB, CC]   A block behind the case, the case is moved a distance of AA, 
        #                               BB is the block size in Y led, 
        #                               CC is the mounting holes distance from pin rom 1
        #                               
        # npthserie = [3, AA]           No black block behind the case, the case is moved a distance of AA
        #
        #
        A, B, C, D, E, F, G = self.get_dsub_size(params)
        ttdz = F / 2.0
        t = params.pin[0]
        pn = params.pin[1]
        serie = params.serie
        pindx = params.pin[2]
        pindy = params.pin[3]
        pind = params.pin[4]
        pinl = params.pin[5]

        if params.pin[0] == 'round':
            self.translate = (0.0, 0.0, 0.0)
        else:
            self.translate = (0.0, 0.0, ttdz)
        
        if params.translate != None:
            if len(params.translate) != 3:
                FreeCAD.Console.PrintMessage('\r\n')
                FreeCAD.Console.PrintMessage('params.translate length is not 3 for model name ' + params.modelName + '\r\n')
                sys.exit()
                
            self.translate = params.translate
            
        dx, dy, dz = self.translate
        ttdx = dx
        ttdy = dy
        ttdz = dz

        if self.gender == 'male':
            if serie == 2:
                if pn == 9:
                    ttdx = (2.0 * pindx)
                elif pn == 15:
                    ttdx = (3.5 * pindx)
                elif pn == 25:
                    ttdx = (6.0 * pindx)
                elif pn == 37:
                    ttdx = (9.0 * pindx)
            elif serie == 3:
                if pn == 15:
                    ttdx = (1.75 * pindx)
                if pn == 25:
                    ttdx = (2.75 * pindx)
                if pn == 26:
                    ttdx = (3.75 * pindx)
                if pn == 37:
                    ttdx = (4.75 * pindx)
                if pn == 44:
                    ttdx = (6.75 * pindx)
                if pn == 62:
                    ttdx = (9.75 * pindx)
                ttdy = pindy


        if self.gender == 'female':
            if serie == 2:
                if pn == 9:
                    ttdx = 0.0 - (2.0 * pindx)
                elif pn == 15:
                    ttdx = 0.0 - (3.5 * pindx)
                elif pn == 25:
                    ttdx = 0.0 - (6.0 * pindx)
                elif pn == 37:
                    ttdx = 0.0 - (9.0 * pindx)
            elif serie == 3:
                if pn == 15 or pn == 25:
                    ttdx = 0.0 - ((int(pn / 6)) * pindx - (pindx / 4.0))
                if pn == 26:
                    ttdx = 0.0 - ((3.75 * pindx) + (0.0))
                if pn == 37:
                    ttdx = 0.0 - ((4.75 * pindx) + (0.0))
                if pn == 44:
                    ttdx = 0.0 - ((6.75 * pindx) + (0.0))
                if pn == 62:
                    ttdx = 0.0 - ((9.75 * pindx) + (0.0))

        #
        if params.npthserie[0] == 2 or params.npthserie[0] == 3:
            ttdy = 0.0 - (params.npthserie[1] - 4.4)
        else:
            if serie == 2:
                ttdy = 0.0 - (pindy / 2.0)
            else:
                ttdy = 0.0 - pindy

        self.translate = (ttdx, ttdy, ttdz)


    def make_3D_model(self, modelID, gender):

        destination_dir = self.get_dest_3D_dir(modelID)
        params = self.all_params[modelID]

        self.gender = gender
        self.set_colors(params)
        self.set_translate(params)
        self.set_rotation(params)
        case_top = self.make_top_DSUB(params)
        show(case_top)
        case = self.make_case_DSUB(params)
        show(case)

        pins = self.make_pin(params)
        show(pins)

        npth_pins = self.make_npth_pins(params)
        
        if npth_pins == None:

            doc = FreeCAD.ActiveDocument
            objs=GetListOfObjects(FreeCAD, doc)

            body_top_color_key = self.body_top_color_key
            body_color_key = self.body_color_key
            pin_color_key = self.pin_color_key

            body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
            body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
            pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()

            Color_Objects(Gui,objs[0],body_top_color)
            Color_Objects(Gui,objs[1],body_color)
            Color_Objects(Gui,objs[2],pin_color)

            col_body_top=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
            col_body=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
            col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
            
            material_substitutions={
                col_body_top[:-1]:body_top_color_key,
                col_body[:-1]:body_color_key,
                col_pin[:-1]:pin_color_key,
            }
        else:
            show(npth_pins)

            doc = FreeCAD.ActiveDocument
            objs=GetListOfObjects(FreeCAD, doc)

            body_top_color_key = self.body_top_color_key
            body_color_key = self.body_color_key
            pin_color_key = self.pin_color_key
            npth_pin_color_key = self.npth_pin_color_key

            body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
            body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
            pin_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()
            npth_pin_color = shaderColors.named_colors[npth_pin_color_key].getDiffuseFloat()

            Color_Objects(Gui,objs[0],body_top_color)
            Color_Objects(Gui,objs[1],body_color)
            Color_Objects(Gui,objs[2],pin_color)
            Color_Objects(Gui,objs[3],npth_pin_color)

            col_body_top=Gui.ActiveDocument.getObject(objs[0].Name).DiffuseColor[0]
            col_body=Gui.ActiveDocument.getObject(objs[1].Name).DiffuseColor[0]
            col_pin=Gui.ActiveDocument.getObject(objs[2].Name).DiffuseColor[0]
            col_npth_pin=Gui.ActiveDocument.getObject(objs[3].Name).DiffuseColor[0]
            
            material_substitutions={
                col_body_top[:-1]:body_top_color_key,
                col_body[:-1]:body_color_key,
                col_pin[:-1]:pin_color_key,
                col_npth_pin[:-1]:npth_pin_color_key
            }
        
        expVRML.say(material_substitutions)
        while len(objs) > 1:
                FuseObjs_wColors(FreeCAD, FreeCADGui, doc.Name, objs[0].Name, objs[1].Name)
                del objs
                objs = GetListOfObjects(FreeCAD, doc)

        return material_substitutions

        
    def get_dsub_size(self, params):
    
        pin = params.pin                # Pin
        serie = params.serie            # Serie
    
        t = pin[0]
        pn = pin[1]
        
        if (serie == 2 or serie == 3) and pn == 9:
                    #     A      B      C       D     E    F   G
            if self.gender == 'female':
                return(16.30, 25.00, 30.80, 19.20, 7.9, 12.50, 3.2)
            else:
                return(16.92, 25.00, 30.80, 19.20, 7.9, 12.50, 3.2)
        #
        #
        if (serie == 2) and pn == 15:
                    #     A      B      C       D     E    F   G
            if self.gender == 'female':
                return(24.60, 33.30, 39.20, 27.70, 7.9, 12.50, 3.2)
            else:
                return(25.50, 33.30, 39.20, 27.70, 7.9, 12.50, 3.2)
        #
        #
        if (serie == 3) and pn == 15:
                    #     A      B      C     D     E    F      G    H
            if self.gender == 'female':
                return(16.30, 25.00, 30.80, 15.80, 8.3, 12.50, 3.3)
            else:
                return(16.92, 25.00, 30.80, 15.80, 8.3, 12.50, 3.3)
        #
        #
        if (serie == 2) and pn == 25:
                    #     A      B      C       D     E    F   G
            if self.gender == 'female':
                return(38.30, 47.10, 53.10, 41.10, 7.9, 12.50, 3.2)
            else:
                return(38.96, 47.10, 53.10, 41.10, 7.9, 12.50, 3.2)
        #
        #
        if (serie == 3) and pn == 26:
                    #     A      B      C       D     E    F   G
            if self.gender == 'female':
                return(24.60, 33.30, 39.20, 24.10, 8.3, 12.50, 3.2)
            else:
                return(25.25, 33.30, 39.20, 24.10, 8.3, 12.50, 3.2)
        #
        #
        if (serie == 2) and pn == 37:
                    #     A      B      C       D     E    F   G
            if self.gender == 'female':
                return(54.80, 63.50, 69.40, 57.30, 8.3, 12.50, 3.2)
            else:
                return(55.42, 63.50, 69.40, 57.30, 8.3, 12.50, 3.2)
        #
        #
        if (serie == 3) and pn == 44:
                    #     A      B      C       D     E    F   G
            if self.gender == 'female':
                return(38.30, 47.10, 53.10, 37.90, 8.3, 12.50, 3.2)
            else:
                return(38.96, 47.10, 53.10, 37.90, 8.3, 12.50, 3.2)
            
        if (serie == 3) and pn == 62:
                    #     A      B      C       D     E    F   G
            if self.gender == 'female':
                return(54.80, 63.50, 69.50, 54.30, 8.3, 12.50, 3.2)
            else:
                return(55.42, 63.50, 69.40, 54.30, 8.3, 12.50, 3.2)

        FreeCAD.Console.PrintMessage('\r\n')
        FreeCAD.Console.PrintMessage('ERROR: Model ID ' + str(modelID) + ' does not exist, exiting')
        FreeCAD.Console.PrintMessage('\r\n')
        sys.exit()

        return None


    def make_npth_pins(self, params):

        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

        ns = npthserie[0]

        if ns == 2:
            A, B, C, D, E, F, G = self.get_dsub_size(params)

            dx, dy, dz = self.translate

            t = pin[0]
            pn = pin[1]
            pindx = pin[2]
            pindy = pin[3]
            pind = pin[4]
            pinl = pin[5]
            np = int(int(pn / 4))

            FW = npthserie[2]
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(C, F).extrude(0.0 - FW)
            case = case.faces(">Y").edges("<X").fillet(1.0)
            case = case.faces(">Y").edges(">X").fillet(1.0)
            #
            # Cut the sides
            case1 = cq.Workplane("XY").workplane(offset=0.0 - 2.0).moveTo(((C / 2.0) - 2.0), 2.5).rect(7.0, F).extrude(0.0 - FW)
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.0 - 2.0).moveTo( 0.0 - ((C / 2.0) - 2.0), 2.5).rect(7.0, F).extrude(0.0 - FW)
            case = case.cut(case1)
            #
            # Cut the holes on front
            case1 = cq.Workplane("XY").workplane(offset=0.5).moveTo((B / 2.0), 0.0).circle((G / 2.0) + 0.1, False).extrude(0.0 - (FW + 1.0))
            case = case.cut(case1)
            case1 = cq.Workplane("XY").workplane(offset=0.5).moveTo(0.0 - (B / 2.0), 0.0).circle((G / 2.0) + 0.1, False).extrude(0.0 - (FW + 1.0))
            case = case.cut(case1)
            #
            # Cut the holes for the pins
            #
            # Distance from back end to center of the hole
            ttx = npthserie[3] + (npthserie[2] -  npthserie[1])
            case1 = cq.Workplane("XZ").workplane(offset=(F / 2.0) + 0.5).moveTo((B / 2.0), (0.0 - FW) + ttx).circle((G / 2.0) , False).extrude(0.0 - (F + 1.0))
            case = case.cut(case1)
            if npthserie[0] > 7.5:
                case1 = cq.Workplane("XZ").workplane(offset=(F / 2.0) + 0.5).moveTo((B / 2.0), (0.0 - FW) + ttx + G / 2.0).circle(G / 2.0, False).extrude(0.0 - (F + 1.0))
                case = case.cut(case1)
            case1 = cq.Workplane("XZ").workplane(offset=(F / 2.0) + 0.5).moveTo((B / 2.0), (0.0 - FW) + ttx + G / 4.0).rect(G, G / 2.0).extrude(0.0 - (F + 1.0))
            case = case.cut(case1)
            #
            #
            # Cut the blocks form sides
            case1 = cq.Workplane("XZ").workplane(offset=(F / 2.0) + 0.5).moveTo(0.0 - (B / 2.0), (0.0 - FW) + ttx).circle(G / 2.0, False).extrude(0.0 - (F + 1.0))
            case = case.cut(case1)
            case1 = cq.Workplane("XZ").workplane(offset=(F / 2.0) + 0.5).moveTo(0.0 - (B / 2.0), (0.0 - FW) + ttx + G / 2.0).circle(G / 2.0, False).extrude(0.0 - (F + 1.0))
            case = case.cut(case1)
            case1 = cq.Workplane("XZ").workplane(offset=(F / 2.0) + 0.5).moveTo(0.0 - (B / 2.0), (0.0 - FW) + ttx + G / 4.0).rect(G, G / 2.0).extrude(0.0 - (F + 1.0))
            case = case.cut(case1)
            #
            #
            case = case.translate((0.0, 0.0, 4.4))      # translate to center of pins
            #
        else:
            # Dummy
            return None

        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return (case)


    def make_center_body(self, params, ttdz, ctd):

        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

#        pin = ['round', 9, 2.77, 2.84, 0.64, 3.9],       # Type of pins

        t = pin[0]
        pn = pin[1]
        pindx = pin[2]
        pindy = pin[3]
        pind = pin[4]
        pinl = pin[5]

        np = int(int(pn / 4))

        pts = []
        A, B, C, D, E, F, G = self.get_dsub_size(params)

        ldx = A - ctd
        ldy = E - ctd

        pts.append((ldx, 0.0))
        pts.append((ldx - (pindx / 2.0), 0.0 - ldy))
        pts.append(((pindx / 2.0), 0.0 - ldy))

        case = cq.Workplane("XY").workplane(offset=0.0).polyline(pts).close().extrude(ttdz)

        case = case.faces(">Y").edges(">X").fillet(1.0)
        case = case.faces(">Y").edges("<X").fillet(1.0)
        case = case.faces("<Y").edges(">X").fillet(1.0)
        case = case.faces("<Y").edges("<X").fillet(1.0)
        case = case.translate((0.0 - (ldx / 2.0), (ldy / 2.0), 0.0))

        return case


    def make_top_DSUB(self, params):

        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

        t = pin[0]
        pn = pin[1]
        pindx = pin[2]
        pindy = pin[3]
        pind = pin[4]
        pinl = pin[5]
        np = int(int(pn / 4))
        A, B, C, D, E, F, G = self.get_dsub_size(params)

        ttdz = 6.0
        if self.gender == 'male':
            ttdz = 2.0

        case = self.make_center_body(params, ttdz, 0.2)
        case = case.translate((0.0, 0.0, 4.8)) # translate to center of pins
        #
        # Add the plate beneath the bulk beneath
        #
        #
        #
        # Add holes if female
        #
        if self.gender == 'female':

            if serie == 2:
                #
                # Make two rows of pins with equal number of pins on each row
                #
                ns = npthserie[0]
                dx, dy, dz = self.translate

                #
                # Make the top row
                #
                np = int(int(pn / 2) + 1)
                x =  (((np / 2.0) * pindx) - (pindx / 2.0))
                y = (E /2.0) - pindy
                tddx = pindx
                if self.gender == 'female':
                    tddx = 0.0 - pindx
                #
                for i in range(0, np):
                    case1 = cq.Workplane("XY").workplane(offset=2.0).moveTo(x, y).circle(pind / 1.5, False).extrude(12.0)
                    case = case.cut(case1)
                    x = x + tddx
                #
                # Make the bottom row
                #
                np = int(int(pn / 2))
                x = (((np / 2.0) * pindx) - (pindx / 2.0))
                y = (E /2.0) - (2.0 * pindy)
                #
                for i in range(0, np):
                    case1 = cq.Workplane("XY").workplane(offset=2.0).moveTo(x, y).circle(pind / 1.5, False).extrude(12.0)
                    case = case.cut(case1)
                    x = x + tddx
            elif serie == 3:
                #
                # Make two rows of pins with equal number of pins on each row
                #
                np = int((pn / 3.0) + 0.48)
                ns = npthserie[0]
                dx, dy, dz = self.translate

                #
                # Make top row
                #
                x =  (((np / 2.0) * pindx)) - (0.75 * pindx)
                y = pindy
                tddx = pindx
                if self.gender == 'female':
                    tddx = 0.0 - pindx
                #
                for i in range(0, np):
                    case1 = cq.Workplane("XY").workplane(offset=8.0).moveTo(x, y).circle(pind / 1.5, False).extrude(12.0)
                    case = case.cut(case1)
                    x = x + tddx
                #
                # Make center row
                #
                x = (((np / 2.0) * pindx)) - (0.25 * pindx)
                y = 0.0
                for i in range(0, np):
                    case1 = cq.Workplane("XY").workplane(offset=8.0).moveTo(x, y).circle(pind / 1.5, False).extrude(12.0)
                    case = case.cut(case1)
                    x = x + tddx
                #
                # Make bottom row
                #
                x =  (((np / 2.0) * pindx)) - (0.75 * pindx)
                np = int(pn) - (2 * np)
                y = 0.0 - pindy
                for i in range(0, np):
                    case1 = cq.Workplane("XY").workplane(offset=8.0).moveTo(x, y).circle(pind / 1.5, False).extrude(12.0)
                    case = case.cut(case1)
                    x = x + tddx
        
        #
        # Add plate at bottom
        # 
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(D - 3.0, E - 1.0).extrude(0.5)
        case = case.union(case1)

        case = case.faces(">Z").chamfer(0.1)

        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)

        return case


    def make_case_DSUB(self, params):

        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

        t = pin[0]
        pn = pin[1]
        pindx = pin[2]
        pindy = pin[3]
        pind = pin[4]
        pinl = pin[5]
        A, B, C, D, E, F, G = self.get_dsub_size(params)

        case = self.make_center_body(params, 5.8, 0.0)
        case1 = self.make_center_body(params, 6.0, 1.0)
        case = case.cut(case1)
        #
        # Add the plate with holes
        #
        ptl = 0.4
        case = case.translate((0.0, 0.0, ptl))
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(C, F).extrude(ptl)
        case2 = cq.Workplane("XY").workplane(offset=ptl + 0.1).moveTo((B / 2.0), 0.0).circle(G / 2.0, False).extrude(0.0 - (ptl + 0.2))
        case1 = case1.cut(case2)
        case2 = cq.Workplane("XY").workplane(offset=ptl + 0.1).moveTo(0.0 - (B / 2.0), 0.0).circle(G / 2.0, False).extrude(0.0 - (ptl + 0.2))
        case1 = case1.cut(case2)
        case1 = case1.faces("<Y").edges("<X").fillet(1.0)
        case1 = case1.faces("<Y").edges(">X").fillet(1.0)
        case1 = case1.faces(">Y").edges(">X").fillet(1.0)
        case1 = case1.faces(">Y").edges("<X").fillet(1.0)
        case1 = case1.faces(">Z").fillet(0.1)
        case1 = case1.faces("<Z").fillet(0.1)
        case = case.union(case1)
        case = case.faces(">Z").edges("<X").chamfer(0.05)

#        if self.gender == 'female':
#            case = case.faces(">Z[2]").edges("not(<X or >X or <Y or >Y)").fillet(0.6)
#        else:
        try:
            case = case.faces(">Z[2]").edges("not(<X or >X or <Y or >Y)").fillet(0.6)
        except:
            try:
                case = case.faces(">Z[1]").edges("not(<X or >X or <Y or >Y)").fillet(0.6)
            except:
                pass


        #
        # Add the metal inside the holes on each sides
        #
        if npthserie[0] == 2:
            case1 = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0 - (B / 2.0), 0.0).circle(G / 2.0 + 0.4, False).extrude(0.0 - 2.20)
            case2 = cq.Workplane("XY").workplane(offset=0.1).moveTo(0.0 - (B / 2.0), 0.0).circle(G / 2.0, False).extrude(0.0 - 2.25)
            case1 = case1.cut(case2)
            case = case.union(case1)
            #
            case1 = cq.Workplane("XY").workplane(offset=0.1).moveTo((B / 2.0), 0.0).circle(G / 2.0 + 0.4, False).extrude(0.0 - 2.20)
            case2 = cq.Workplane("XY").workplane(offset=0.1).moveTo((B / 2.0), 0.0).circle(G / 2.0, False).extrude(0.0 - 2.25)
            case1 = case1.cut(case2)
            case = case.union(case1)

        #
        # Add the bulk beneath
        #
        ptl = 4.0
        case = case.translate((0.0, 0.0, ptl))
        #
        case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(D, E + 2.0).extrude(ptl)
        case1 = case1.faces("<Y").edges("<X").fillet(1.0)
        case1 = case1.faces("<Y").edges(">X").fillet(1.0)
        case1 = case1.faces(">Y").edges("<X").fillet(1.0)
        case1 = case1.faces(">Y").edges(">X").fillet(1.0)
        case1 = case1.faces("<Z").fillet(1.0)
        case = case.union(case1)
        #
        # Move it a little for the ending tops
        #
        case = case.translate((0.0, 0.0, 0.3))

        if self.rotatex > 0.0:
            case = case.rotate((0,0,0), (1,0,0), self.rotatex)

        case = case.translate(self.translate)
        
        return case


    def make_pin_help(self, params, x, y, tddx, np, LD22):
    
        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

        #
        # Make two rows of pins with equal number of pins on each row
        #
        t = pin[0]
        pn = pin[1]
        pindx = pin[2]
        pindy = pin[3]
        pind = pin[4]
        pinl = pin[5]
        A, B, C, D, E, F, G = self.get_dsub_size(params)
        ns = npthserie[0]
        dx, dy, dz = self.translate
        case = None

        #
        for i in range(0, np):
            if t == 'round' or (t == 'round1' and ns == 2):
                case1 = cq.Workplane("XY").workplane(offset=0.4).moveTo(x, y).circle(pind / 2.0, False).extrude(0.0 - (pinl + 0.4))
                case1 = case1.faces("<Z").fillet(pind / 4.0)
            elif t == 'round1':
                r2 = (pind / 2.0) * 4.0
                r = r2 - r2 / math.sqrt(2.0)
                L2 = 0.0 - pinl
                L = 0.0 - (npthserie[1] - 2.0) - y # seating plane
                LD2 = LD22 + r2
                s = LD2 - r2

                path = cq.Workplane("YZ")\
                         .moveTo(0.0, 0.0 - pinl)\
                         .lineTo(0.0, LD2 - (2.0 * r2))\
                         .threePointArc((-r, s - r), (-r2, s))\
                         .lineTo(L, s)
                case1 = cq.Workplane("XY")\
                        .circle((pind / 2.0))\
                        .sweep(path).faces(">Y")\
                        .faces("<Z").fillet(pind / 4.0)\
                        .translate((x, y, 0.0))
                #
                #
            if case == None:
                case = case1
            else:
                case = case.union(case1)

            if (t == 'round' or t == 'round1') and self.gender == 'male':
                #
                # Add the pigs inside the connector if it is a male
                #
                if serie == 2:
                    if t == 'round1':
                        case1 = cq.Workplane("XY").workplane(offset=4.4).moveTo(x, y - (pindy / 2.0)).circle(pind / 2.0, False).extrude(pinl + 2.0)
                    else:
                        case1 = cq.Workplane("XY").workplane(offset=4.4).moveTo(x, y).circle(pind / 2.0, False).extrude(pinl + 2.0)
                else:
                    case1 = cq.Workplane("XY").workplane(offset=4.4).moveTo(x, y).circle(pind / 2.0, False).extrude(pinl + 2.0)
                
                case1 = case1.faces("<Y").fillet(pind / 4.0)
                
                
                if t == 'round1':
                    if self.rotatex > 0.0:
                        case1 = case1.rotate((0,0,0), (1,0,0), self.rotatex)
                        case1 = case1.translate((0.0, 0.0, pindy))

                    case1 = case1.translate((0.0, dy, dz))

                case = case.union(case1)

            x = x + tddx

        return case


    def make_pin_type1(self, params):

        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

        #
        # Make two rows of pins with equal number of pins on each row
        #
        t = pin[0]
        pn = pin[1]
        pindx = pin[2]
        pindy = pin[3]
        pind = pin[4]
        pinl = pin[5]
        np = int(int(pn / 2) + 1)
        A, B, C, D, E, F, G = self.get_dsub_size(params)
        ns = npthserie[0]
        dx, dy, dz = self.translate

        #
        # Make the top row
        #
        x = 0.0
        y = 0.0
        tddx = pindx
        if self.gender == 'female':
            tddx = 0.0 - pindx
        case = self.make_pin_help(params, x, y, tddx, np, (F / 2.0) + (pindy / 2.0))
        #

        #
        # Make the bottom row
        #
        x = 0.0 + (pindx / 2.0)
        if self.gender == 'female':
            x = 0.0 - (pindx / 2.0)
        y = 0.0 - pindy
        #
        np = int(pn) - int(np)
        case1 = self.make_pin_help(params, x, y, tddx, np, (F / 2.0) - (pindy / 2.0))
        
        case = case.union(case1)

        return case


    def make_pin_type2(self, params):

        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

        #
        # Make two rows of pins with equal number of pins on each row
        #
        t = pin[0]
        pn = pin[1]
        pindx = pin[2]
        pindy = pin[3]
        pind = pin[4]
        pinl = pin[5]
        np = int((pn / 3.0) + 0.50)
        A, B, C, D, E, F, G = self.get_dsub_size(params)
        ns = npthserie[0]
        dx, dy, dz = self.translate

        #
        # Make top row
        #
        tddx = pindx
        x = 0.0
        y = 0.0
        if self.gender == 'female':
            tddx = 0.0 - pindx
        #
        case = self.make_pin_help(params, x, y, tddx, np, (F / 2.0) + pindy)
        #
        # Make center row
        #
        x = 0.0 - (pindx / 2.0)
        if self.gender == 'female':
            x = 0.0 + (pindx / 2.0)
        y = 0.0 - pindy
        case1 = self.make_pin_help(params, x, y, tddx, np, (F / 2.0))
        case = case.union(case1)
        #
        # Make bottom row
        #
        np = int(pn) - (2 * np)
        x = 0.0
        if self.gender == 'female':
            tddx = 0.0 - pindx
        y = 0.0 - (2.0 * pindy)
        case1 = self.make_pin_help(params, x, y, tddx, np, (F / 2.0) - pindy)
        case = case.union(case1)
        
        case1 = case1.translate((0.0, 0.0, dz))

        return case


    def make_pin(self, params):

        pin = params.pin                # Pin
        serie = params.serie            # Serie
        npthserie = params.npthserie    # npth serie

#        pin = ['round', 9, 2.77, 2.84, 0.8, 3.9],       # Type of pins
#        pin = ['round1', 9, 2.77, 2.84, 0.64, 3.9, 4.5, 9.40],      # Type of pins

        t = pin[0]
        pn = pin[1]
        pindx = pin[2]
        pindy = pin[3]
        pind = pin[4]
        pinl = pin[5]
        ns = npthserie[0]
        A, B, C, D, E, F, G = self.get_dsub_size(params)
        dx, dy, dz = self.translate
        np = int(int(pn / 4))

        if serie == 2:
            case = self.make_pin_type1(params)
        elif serie == 3:
            case = self.make_pin_type2(params)
        else:
            case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(0.001, False).extrude(0.001)

        if ns == 2:
            #
            # Make the side connectors if the casing have a black plastic behind
            #
            tyr = (npthserie[1] - npthserie[3]) - 2.0
            y = 0.0 - npthserie[3]
            #
            # Make metal contact through PCB
            tx = (B / 2.0)
            case1 = cq.Workplane("XY").workplane(offset=2.5).moveTo(tx, y).rect(2.0, 0.2).extrude(0.0 - (pinl + 4.0))
            case1 = case1.faces("<Z").edges("<X").chamfer(0.8, 0.2)
            case1 = case1.faces("<Z").edges(">X").chamfer(0.2, 0.8)
            case2 = cq.Workplane("XY").workplane(offset=2.3).moveTo(tx, y).rect(0.8, 0.2).extrude(0.0 - (pinl + 4.0))
            case1 = case1.cut(case2)
            #
            # Add the metal upp to the hole
            case2 = cq.Workplane("XY").workplane(offset=2.5).moveTo(tx - 1.0, y + 0.1).rect(2.0, 0.0 - tyr, centered=False).extrude(0.2)
            case2 = case2.faces(">Z").edges(">Y").fillet(0.1)
            case1 = case1.union(case2)
            case2 = cq.Workplane("XY").workplane(offset=2.5).moveTo(tx - 1.0, y + 0.1 - tyr).rect(2.0, 0.2, centered=False).extrude(2.1)
            case1 = case1.union(case2)
            case1 = case1.translate((dx, 0.0, 0.0))
            case = case.union(case1)
            #
            # Make metal contact through PCB
            tx = 0.0 - (B / 2.0)
            case1 = cq.Workplane("XY").workplane(offset=2.5).moveTo(tx, y).rect(2.0, 0.2).extrude(0.0 - (pinl + 4.0))
            case1 = case1.faces("<Z").edges("<X").chamfer(0.8, 0.2)
            case1 = case1.faces("<Z").edges(">X").chamfer(0.2, 0.8)
            case2 = cq.Workplane("XY").workplane(offset=2.5).moveTo(tx, y).rect(0.8, 0.2).extrude(0.0 - (pinl + 4.0))
            case1 = case1.cut(case2)
            #
            # Add the metal upp to the hole
            case2 = cq.Workplane("XY").workplane(offset=2.5).moveTo(tx - 1.0, y + 0.1).rect(2.0, 0.0 - tyr, centered=False).extrude(0.2)
            case2 = case2.faces(">Z").edges(">Y").fillet(0.1)
            case1 = case1.union(case2)
            case2 = cq.Workplane("XY").workplane(offset=2.5).moveTo(tx - 1.0, y + 0.1 - tyr).rect(2.0, 0.2, centered=False).extrude(2.1)
            case1 = case1.union(case2)
            case1 = case1.translate((dx, 0.0, 0.0))
            case = case.union(case1)
            #


        return case

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
        
    Params = namedtuple_with_defaults("Params", [
        'modelName',		    # modelName
        'pin',                  # pin
        'gender',               # gender
        'serie',                # 2 or 3 rows
        'npthserie',            # npth serie
        'npth_pin_color_key',   # NPTH Pin color
        'body_top_color_key',	# Top color
        'body_color_key',	    # Body colour
        'pin_color_key',	    # Pin color
        'rotatex',	            # Rotation around x-axis if required
        'rotatey',	            # Rotation around y-axis if required
        'rotatez',	            # Rotation around z-axis if required
        'translate',            # Translate if required, even pins
        'dest_dir_prefix'	    # Destination directory
    ])


    #
    # serie = 2, two lines of pins
    # serie = 3, three lines of pins
    #
    # pin = ['round' ...  The pins are straight down
    # pin = ['round1' ...  The pins are bend 90 degree, this will include a rotation of 90 of the case
    #
    # npthserie = [1]   No black block behind the case
    # npthserie = [2, AA, BB, CC]   A block behind the case, the case is moved a distance of AA, 
    #                               BB is the block size in Y led, 
    #                               CC is the mounting holes distance from pin rom 1
    #                               
    # npthserie = [3, AA]           No black block behind the case, the case is moved a distance of AA
    #
    all_params = {

        'DSUB_1': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 9, 2.77, 2.54, 0.64, 3.9],      # Type of pins
            serie = 2,                                      # Shape
            npthserie = [3, 11.94],                         # npth shape
            ),

        'DSUB_2': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset4.94mm_Housed_MountingHolesOffset7.48mm',    # Model name
            pin = ['round1', 9, 2.77, 2.84, 0.64, 3.9],      # Type of pins
            serie = 2,                                      # Shape
            npthserie = [2, 7.78, 10.48, 0.3],             # npth shape
            ),
            
        'DSUB_3': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm',    # Model name
            pin = ['round1', 9, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 10.54, 12.34, 1.42],            # npth shape
            ),

        'DSUB_4': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 9, 2.77, 2.54, 0.64, 3.9],      # Type of pins
            serie = 2,                                      # Shape
            npthserie = [3, 12.24 ],                        # npth shape
            ),

        'DSUB_5': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm',    # Model name
            pin = ['round1', 9, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 12.74, 14.54, 1.42],            # npth shape
            ),

        'DSUB_6': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset8.20mm',    # Model name
            pin = ['round1', 9, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.4, 19.20, 9.2],              # npth shape
            ),

        'DSUB_7': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm',    # Model name
            pin = ['round1', 9, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.4, 19.20, 1.42],             # npth shape
            ),

        'DSUB_8': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm',    # Model name
            pin = ['round', 9, 2.77, 2.84, 0.64, 3.9],       # Type of pins
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_9': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm_MountingHoles',    # Model name
            pin = ['round', 9, 2.77, 2.84, 0.64, 3.9],       # Type of pins
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),
            

        'DSUB_30': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm',    # Model name
            pin = ['round1', 15, 2.29, 1.98, 0.64, 3.9],    # Type of pins
            serie = 3,                                      # Shape
            npthserie = [2, 6.99, 8.6, 1.98],               # npth shape
            ),

        'DSUB_31': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset8.35mm_Housed_MountingHolesOffset10.89mm',    # Model name
            pin = ['round1', 15, 2.29, 1.98, 0.64, 3.9],    # Type of pins
            serie = 3,                                      # Shape
            npthserie = [2, 12.31, 13.89, 1.98],            # npth shape
            ),
            
        'DSUB_32': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 15, 2.29, 1.98, 0.64, 3.9],    # Type of pins
            serie = 3,                                      # Shape
            npthserie = [3, 13.36],                         # npth shape
            ),


        'DSUB_33': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x2.54mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 15, 2.29, 2.54, 0.64, 3.9],     # Type of pins
            serie = 3,                                      # Shape
            npthserie = [3, 14.48],                         # npth shape
            ),

        'DSUB_34': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 15, 2.77, 2.54, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [3, 11.94],                         # npth shape
            ),

        'DSUB_35': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset4.94mm_Housed_MountingHolesOffset7.48mm',    # Model name
            pin = ['round1', 15, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 7.78, 10.48, 0.30],             # npth shape
            ),

        'DSUB_36': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm',    # Model name
            pin = ['round1', 15, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.4, 19.2, 1.42],              # npth shape
            ),

        'DSUB_37': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset8.20mm',    # Model name
            pin = ['round1', 15, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.4, 19.2, 9.2],               # npth shape
            ),

        'DSUB_38': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm',    # Model name
            pin = ['round1', 15, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 12.74, 14.54, 1.42],            # npth shape
            ),

        'DSUB_39': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm',            # Model name
            pin = ['round', 15, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_40': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm_MountingHoles',    # Model name
            pin = ['round', 15, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_41': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.29x1.98mm_MountingHoles',     # Model name
            pin = ['round', 15, 2.29, 1.98, 0.64, 3.9],      # Type of pins
            serie = 3,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_42': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 15, 2.77, 2.84, 0.64, 3.9],     # Type of pins
            serie = 2,                                      # Shape
            npthserie = [3, 12.24 ],                        # npth shape
            ),

        'DSUB_43': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm',    # Model name
            pin = ['round1', 15, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 10.54, 12.34, 1.42],            # npth shape
            ),

        'DSUB_44': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 25, 2.77, 2.54, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [3, 11.94],                         # npth shape
            ),

        'DSUB_45': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset4.94mm_Housed_MountingHolesOffset7.48mm',    # Model name
            pin = ['round1', 25, 2.77, 2.84, 0.64, 3.9],    # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 7.78, 10.48, 0.00],             # npth shape
            ),

        'DSUB_46': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm',    # Model name
            pin = ['round1', 25, 2.77, 2.84, 0.64, 3.9],    # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 10.54, 12.34, 1.42],            # npth shape
            ),

        'DSUB_47': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.40mm',    # Model name
            pin = ['round1', 25, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [3, 12.24],                         # npth shape
            ),

        'DSUB_48': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm',    # Model name
            pin = ['round1', 25, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 12.74, 14.54, 1.42],            # npth shape
            ),

        'DSUB_49': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset8.20mm',    # Model name
            pin = ['round1', 25, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.40, 19.20, 9.20],            # npth shape
            ),

        'DSUB_50': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm',    # Model name
            pin = ['round1', 25, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.40, 19.20, 1.42],            # npth shape
            ),

        'DSUB_51': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm',            # Model name
            pin = ['round', 25, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_52': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm_MountingHoles',  # Model name
            pin = ['round', 25, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_60': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm',  # Model name
            pin = ['round1', 26, 2.29, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [2, 6.99, 8.60, 1.98],              # npth shape
            ),

        'DSUB_61': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset8.35mm_Housed_MountingHolesOffset10.89mm',  # Model name
            pin = ['round1', 26, 2.29, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [2, 12.31, 13.89, 1.98],            # npth shape
            ),

        'DSUB_62': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 26, 2.29, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [3, 13.36],                         # npth shape
            ),

        'DSUB_63': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x2.54mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 26, 2.29, 2.54, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [3, 14.48],                         # npth shape
            ),

        'DSUB_64': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.29x1.98mm_MountingHoles',  # Model name
            pin = ['round', 26, 2.29, 1.98, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_70': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.54mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 37, 2.77, 2.54, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [3, 11.04],                         # npth shape
            ),

        'DSUB_71': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset4.94mm_Housed_MountingHolesOffset7.48mm',  # Model name
            pin = ['round1', 37, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 11.04, 13.74, 1.42],            # npth shape
            ),

        'DSUB_72': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm',  # Model name
            pin = ['round1', 37, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 10.54, 12.34, 1.42],            # npth shape
            ),

        'DSUB_73': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 37, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [3, 12.35],                         # npth shape
            ),

        'DSUB_74': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm',  # Model name
            pin = ['round1', 37, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 12.74, 14.54, 1.42],            # npth shape
            ),

        'DSUB_75': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset8.20mm',  # Model name
            pin = ['round1', 37, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.40, 19.20, 9.20],            # npth shape
            ),

        'DSUB_76': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm',  # Model name
            pin = ['round1', 37, 2.77, 2.84, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [2, 17.40, 19.20, 1.42],            # npth shape
            ),

        'DSUB_77': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm',            # Model name
            pin = ['round', 37, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_78': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.77x2.84mm_MountingHoles',  # Model name
            pin = ['round', 37, 2.77, 2.84, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 2,                                      # Shape
            npthserie = [1],                                # npth shape
            ),

        'DSUB_90': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm',  # Model name
            pin = ['round1', 44, 2.29, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [2, 6.99, 8.6, 1.98],               # npth shape
            ),

        'DSUB_91': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset8.35mm_Housed_MountingHolesOffset10.89mm',  # Model name
            pin = ['round1', 44, 2.29, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [2, 12.31, 13.89, 1.98],            # npth shape
            ),

        'DSUB_92': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x1.98mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 44, 2.29, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [3, 13.36],                         # npth shape
            ),

        'DSUB_93': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.29x2.54mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 44, 2.29, 2.54, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [3, 14.48],                         # npth shape
            ),

        'DSUB_94': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.29x1.98mm_MountingHoles',  # Model name
            pin = ['round', 44, 2.29, 1.98, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [1],                                # npth shape
            ),


        'DSUB_100': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.41x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm',  # Model name
            pin = ['round1', 62, 2.41, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [2, 6.99, 8.6, 1.98],               # npth shape
            ),

        'DSUB_101': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.41x1.98mm_EdgePinOffset8.35mm_Housed_MountingHolesOffset10.89mm',  # Model name
            pin = ['round1', 62, 2.41, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [2, 12.31, 13.89, 1.98],            # npth shape
            ),

        'DSUB_102': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.41x1.98mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 62, 2.41, 1.98, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [3, 13.36],                         # npth shape
            ),

        'DSUB_103': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Horizontal_P2.41x2.54mm_EdgePinOffset9.40mm',  # Model name
            pin = ['round1', 62, 2.41, 2.54, 0.64, 3.9],     # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [3, 14.48],                         # npth shape
            ),

        'DSUB_104': Params(
            #
            # http://service.powerdynamics.com/ec/Catalog17/Section%2007.pdf
            # 
            modelName = 'Vertical_P2.41x1.98mm_MountingHoles',  # Model name
            pin = ['round', 62, 2.41, 1.98, 0.64, 3.9],      # Type of pins, type, #pin, x, y, diam, length under pcb, *length above pcb, length form hole), last two is for 90 degree bended
            serie = 3,                                      # Shape
            npthserie = [1],                                # npth shape
            ),
    }

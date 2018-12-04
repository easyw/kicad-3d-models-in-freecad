
# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#

## file of parametric definitions

import collections
from collections import namedtuple

import math

import FreeCAD, Draft, FreeCADGui
import ImportGui
import FreeCADGui as Gui

import shaderColors
import exportPartToVRML as expVRML

## base parametes & model
import collections
from collections import namedtuple

# Import cad_tools
import cq_cad_tools
# Reload tools
reload(cq_cad_tools)
# Explicitly load all needed functions
from cq_cad_tools import FuseObjs_wColors, GetListOfObjects, restore_Main_Tools, \
 exportSTEP, close_CQ_Example, exportVRML, saveFCdoc, z_RotateObject, Color_Objects, \
 CutObjs_wColors, checkRequirements

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
    from Helpers import show
    # CadQuery Gui
except: # catch *all* exceptions
    msg = "missing CadQuery 0.3.0 or later Module!\r\n\r\n"
    msg += "https://github.com/jmwright/cadquery-freecad-module/wiki\n"
    if QtGui is not None:
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    # maui end

#checking requirements

try:
    close_CQ_Example(FreeCAD, Gui)
except: # catch *all* exceptions
    print "CQ 030 doesn't open example file"


class cq_parameters_help():

    def __init__(self):
        x = 0

    def create_pins(self, origo_x, origo_y, A1, pin_number, pin_type, center_pin, h, alpha_delta, rotation):

        alpha = alpha_delta
        if pin_type[0] == 'round':
            x1 = (h * math.sin(alpha)) + origo_x
            y1 = (h * math.cos(alpha)) - origo_y
            pins = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(0 - (0.1 + pin_type[2]))
            pins = pins.faces("<Z").fillet(pin_type[1] / 5.0)
            alpha = alpha + alpha_delta
            for i in range(1, pin_number):
                x1 = (h * math.sin(alpha)) + origo_x
                y1 = (h * math.cos(alpha)) - origo_y
                pint = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(x1, y1).circle(pin_type[1] / 2.0, False).extrude(0 - (0.1 + pin_type[2]))
                pint = pint.faces("<Z").fillet(pin_type[1] / 5.0)
                pins = pins.union(pint)
                alpha = alpha + alpha_delta
                

        alpha = alpha_delta
        if pin_type[0] == 'roundtap':
            xx = (h * math.sin(alpha)) + origo_x
            yy = (h * math.cos(alpha)) - origo_y

            x1 = (pin_type[4] / 2.0)
            y1 = A1
            #
            x2 = (pin_type[4] / 2.0)
            y2 = A1 - (pin_type[3] - (pin_type[5] / 2.0))
            #
            x3 = (pin_type[6] / 2.0)
            y3 = A1 - (pin_type[3])
            #
            x4 = (pin_type[6] / 2.0)
            y4 = A1 - (pin_type[3] + pin_type[5])
            

            pts = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (0 - x4, y4), (0 - x3, y3), (0 - x2, y2), (0 - x1, y1), (x1, y1)]
            pins = cq.Workplane("XZ").workplane(offset=0 - (pin_type[2] / 2.0)).polyline(pts).close().extrude(pin_type[2])
            pins = pins.faces("<Z").edges("<X").fillet(pin_type[6] / 2.3)
            pins = pins.faces("<Z").edges(">X").fillet(pin_type[6] / 2.3)
            pint = cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0 - (2.0 - (pin_type[2] / 2.0))).rect(pin_type[4], 4.0).extrude(pin_type[2])
            pint = pint.faces(">Y").edges(">Z").fillet(pin_type[2] / 1.5)
            pins = pins.union(pint)
            pins = pins.rotate((0,0,0), (0,0,1), 360 - (alpha * (180.0 / math.pi)))
            pins = pins.translate((xx, yy, 0))

            alpha = alpha + alpha_delta
            for i in range(1, pin_number):
                xx = (h * math.sin(alpha)) + origo_x
                yy = (h * math.cos(alpha)) - origo_y

                pine = cq.Workplane("XZ").workplane(offset=0 - (pin_type[2] / 2.0)).polyline(pts).close().extrude(pin_type[2])
                pine = pine.faces("<Z").edges("<X").fillet(pin_type[6] / 2.3)
                pine = pine.faces("<Z").edges(">X").fillet(pin_type[6] / 2.3)
                pinr = cq.Workplane("XY").workplane(offset=A1).moveTo(0, 0 - (2.0 - (pin_type[2] / 2.0))).rect(pin_type[4], 4.0).extrude(pin_type[2])
                pinr = pinr.faces(">Y").edges(">Z").fillet(pin_type[2] / 1.5)
                pine = pine.union(pint)
                pine = pine.rotate((0,0,0), (0,0,1), 360 - (alpha * (180.0 / math.pi)))
                pine = pine.translate((xx, yy, 0))

                pins = pins.union(pine)
                alpha = alpha + alpha_delta
                
        if center_pin != None:
            if center_pin[0] == 'metal':
                pint = cq.Workplane("XY").workplane(offset=A1 + 0.1).moveTo(origo_x, 0 - origo_y).circle(center_pin[1] / 2.0, False).extrude(0 - (0.1 + center_pin[2]))
                pint = pint.faces("<Z").fillet(pin_type[1] / 5.0)
                pins  = pins.union(pint)
        
        if (rotation > 0.01):
            pins = pins.rotate((0,0,0), (0,0,1), rotation)

        return pins

    def create_sadle_shield(self, origo_x, origo_y, A1, sadle, sadle_hole, sadle_shield, rotation):
            
        sadle_z = sadle[0]
        sadle_w = sadle[1]
        sadle_r1 = sadle[2] / 2.0
        sadle_x = sadle[3]
        sadle_r2 = sadle[4] / 2.0
        sadle_a = sadle[5]
        sadle_h = 0.2
        #
        s_d = sadle_shield[0]
        s_h = sadle_shield[1]
        #
        th = 0.1
        case = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(0, 0).circle(s_d / 2.0, False).extrude(s_h)
        case = case.faces(">Z").shell(0.1)
    #    case1 = case1.faces(">Z").fillet(th / 2.1)
        case = case.translate((origo_x, 0.0 - origo_y, 0.0))
        
        if (rotation > 0.01):
            case = case.rotate((0,0,0), (0,0,1), rotation)

        return (case.clean())

    def create_sadle(self, origo_x, origo_y, A1, D, sadle, sadle_hole, rotation):

        #
        # sadle = [6.6, 35.5, 26.5, 14.25, 13.2, 72],        # sadle z pos, length, width, xpos r2, diameter r2, rotation
        #
        sadle_z = sadle[0]
        sadle_w = sadle[1]
        sadle_r1 = sadle[2] / 2.0
        sadle_x = sadle[3]
        sadle_r2 = sadle[4] / 2.0
        sadle_a = sadle[5]
        sadle_h = 0.2
        #
        # 
        case2 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(0, 0).circle(sadle_r1, False).extrude(sadle_h)
        #
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(sadle_x, 0).circle(sadle_r2, False).extrude(sadle_h)
        case2 = case2.union(case21)
        #
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(0 - sadle_x, 0).circle(sadle_r2, False).extrude(sadle_h)
        case2 = case2.union(case21)
        #
        # https://en.wikipedia.org/wiki/Tangent_lines_to_circles
        #
        x1 = sadle_x;
        y1 = 0.0
        r = sadle_r2
        x2 = 0.0
        y2 = 0.0
        R = sadle_r1
        #
        theta = 0 - math.atan((y2 - y1) / (x2 - x1))
        beta = math.asin((R - r) / (math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))))
        alpha = theta - beta
        x3 = x1 + r * math.cos((math.pi / 2.0) - alpha)
        y3 = y1 + r * math.sin((math.pi / 2.0) - alpha)
        x4 = x2 + R * math.cos((math.pi / 2.0) - alpha)
        y4 = y2 + R * math.sin((math.pi / 2.0) - alpha)
        #
        #
        tdx = ((x1 + (x1 - x3) - (0 - x4)) / 2.0)
        ttx = tdx + (0 - x4)
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(ttx, 0).rect(2.0 * tdx, 2.2 * y4).extrude(sadle_h)
        case2 = case2.union(case21)
        #
        tdx = ((x1 + (x1 - x3) - (0 - x4)) / 2.0)
        ttx = 0 - (tdx + (0 - x4))
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(ttx, 0).rect(2.0 * tdx, 2.2 * y4).extrude(sadle_h)
        case2 = case2.union(case21)
        #
        #
        #
        hht = math.sqrt(((x4 - x3)**2) + ((y4 - y3)**2))
        k1 = math.fabs(x4 - x3)
        al = math.asin(k1 / hht)
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z - 0.2).moveTo(0, 0).rect(2.0 * tdx, 2.2 * y4).extrude(sadle_h)
    #        case2 = case2.union(case21)
        #
        #
        #
        x5 = x1 + (x1 - x3)
        ddt = 1.0
        #
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(0, 0).rect(sadle_r1, 2.0 * sadle_r1, centered=False).extrude(sadle_h)
        case21 = case21.rotate((0,0,0), (0,0,1), 90.0 - math.degrees(beta))
        ddtx = ddt * math.cos(90.0 - math.degrees(beta))
        ddty = ddt * math.sin(90.0 - math.degrees(beta))
        case21 = case21.translate((x5, y3, 0.0))
        case2 = case2.cut(case21)
        #
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(0, 0).rect(2.0 * sadle_r1, sadle_r1, centered=False).extrude(sadle_h)
        case21 = case21.rotate((0,0,0), (0,0,1), math.degrees(beta))
        ddtx = ddt * math.cos(math.degrees(beta))
        ddty = ddt * math.sin(math.degrees(beta))
        case21 = case21.translate((0.0 - x5, y3, 0.0))
        case2 = case2.cut(case21)
        #
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(0.0 - sadle_r1 - 4.0, 0).rect(2.0 * sadle_r1, (0.0 - sadle_r1), centered=False).extrude(sadle_h)
        case21 = case21.rotate((0,0,0), (0,0,1), math.degrees(beta))
        ddtx = ddt * math.cos(math.degrees(beta))
        ddty = ddt * math.sin(math.degrees(beta))
        case21 = case21.translate((x5, 0.0 - y3, 0.0))
        case2 = case2.cut(case21)
        #
        case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(0, 0).rect(0.0 - sadle_r1 - 4.0, 2.0 * (0.0 - sadle_r1), centered=False).extrude(sadle_h)
        case21 = case21.rotate((0,0,0), (0,0,1), 90.0 - math.degrees(beta))
        ddtx = ddt * math.cos(90.0 - math.degrees(beta))
        ddty = ddt * math.sin(90.0 - math.degrees(beta))
        case21 = case21.translate((0.0 - x5, 0.0 - y3, 0.0))
        case2 = case2.cut(case21)
        
        for n in sadle_hole:
            sh_x = n[0]
            sh_d = n[1]
            
            case21 = cq.Workplane("XY").workplane(offset=A1 + sadle_z - 0.1).moveTo(sh_x, 0).circle(sh_d / 2.0, False).extrude(sadle_h + 0.2)
            case2 = case2.cut(case21)
        
        case2 = case2.faces(">Z").fillet(sadle_h / 2.1)
        case2 = case2.faces("<Z").fillet(sadle_h / 2.1)
        
        case2 = case2.rotate((0,0,0), (0,0,1), sadle_a)
        case2 = case2.translate((origo_x, 0.0 - origo_y, 0.0))
        
        case9 = cq.Workplane("XY").workplane(offset=A1 + sadle_z).moveTo(origo_x, 0.0 - origo_y).circle((D / 2.0) + 0.1, False).extrude(sadle_h)
        case2 = case2.cut(case9)
        
        if (rotation > 0.01):
            case2 = case2.rotate((0,0,0), (0,0,1), rotation)

        return (case2.clean())

    def make_spigot(self, case, origo_x, origo_y, A1, pin_number, pin_spigot, pin_top_diameter, H, alpha_delta, rotation):

        case1 = case
        
        if pin_spigot != None:
            if pin_spigot[0] == 'round' or pin_spigot[0] == 'tap' :
                pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(2.0, False).extrude(H + 0.2)
                case1 = case1.cut(pint)
                if len(pin_spigot) > 2:
                    pint = cq.Workplane("XY").workplane(offset=A1 + ((3 * H) / 4)).moveTo(origo_x, 0 - origo_y).circle(pin_spigot[2] / 2.0, False).extrude(H)
                    case1 = case1.cut(pint)
            #
            if pin_spigot[0] == 'tap' and len(pin_spigot) > 3:
                x = origo_x - (pin_spigot[3] / 2.0)
                d = pin_spigot[2] / 2.0 + pin_spigot[3]
                pint = cq.Workplane("XY").workplane(offset=A1 + ((3 * H) / 4)).moveTo(0 ,0).rect(0 - d, pin_spigot[3], centered=False).extrude(H)
                pint = pint.rotate((0,0,0), (0,0,1), math.degrees((5.0 * alpha_delta) / 2.0))
                pint = pint.translate((x, 0 - origo_y, 0.0))
                case1 = case1.cut(pint)
     
        if len(pin_top_diameter) > 1:
            h = pin_top_diameter[0] / 2.0
            alpha = alpha_delta
            x1 = (h * math.sin(alpha)) + origo_x
            y1 = (h * math.cos(alpha)) - origo_y
            pint = cq.Workplane("XY").workplane(offset=A1 + (H / 2.0)).moveTo(x1, y1).circle(pin_top_diameter[1] / 2.0, False).extrude(H)
            case1 = case1.cut(pint)
            alpha = alpha + alpha_delta
            for i in range(1, pin_number):
                x1 = (h * math.sin(alpha)) + origo_x
                y1 = (h * math.cos(alpha)) - origo_y
                pint = cq.Workplane("XY").workplane(offset=A1 + (H / 2.0)).moveTo(x1, y1).circle(pin_top_diameter[1] / 2.0, False).extrude(H)
                case1 = case1.cut(pint)
                alpha = alpha + alpha_delta

        if (rotation > 0.01):
            case1 = case1.rotate((0,0,0), (0,0,1), rotation)
               
        return (case1.clean())
        
    def make_body_with_ring_with_cut(self, origo_x, origo_y, A1, D, pin_number, pin_type, pin_spigot, pin_top_diameter, H, alpha_delta, rotation):
            
        ffs = D / 70.0
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).circle(D / 2.0, False).extrude(H)
        #
        # Make ring on the middle of the body
        #
        DDq = 2.0
        #
        TT = D - DDq
        F1 = (H - 2.0) / 2.0
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0 + 6.0, False).extrude(F1 + 0.1)
        case2 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0, False).extrude(F1 + 0.1)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 + F1 + 2.0).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0 + 6.0, False).extrude(H)
        case2 = cq.Workplane("XY").workplane(offset=A1 + F1 + 2.0).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0, False).extrude(H)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        
        #
        # Cut the edges of the socket
        #
        tv = 20
        ti = ((D - TT) / 2.0) + 0.2
        ta = 0 - ((tv * math.pi) / 180.0)
        th = (TT / 2.0) + (ti / 2.0)
        tdx = (th * math.sin(ta))
        tdy = (th * math.cos(ta))

        ttx = origo_x + tdx
        tty = origo_y + tdy

        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(0,0).rect(D, ti).extrude(H + 0.2)
        case1 = case1.rotate((0,0,0), (0,0,1), 360 - tv)
        case1 = case1.translate((ttx, 0 - tty, 0))
        case = case.cut(case1)
        #
        tv = tv + 180
        ti = ((D - TT) / 2.0) + 0.2
        ta = 0 - ((tv * math.pi) / 180.0)
        th = (TT / 2.0) + (ti / 2.0)
        tdx = (th * math.sin(ta))
        tdy = (th * math.cos(ta))

        ttx = origo_x + tdx
        tty = origo_y + tdy

        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(0,0).rect(D, ti).extrude(H + 0.2)
        case1 = case1.rotate((0,0,0), (0,0,1), 360 - tv)
        case1 = case1.translate((ttx, 0 - tty, 0))
        case = case.cut(case1)
        
        caseS = self.make_spigot(case, origo_x, origo_y, A1, pin_number, pin_spigot, pin_top_diameter, H, alpha_delta, rotation)
        #
        # Round top
        #
        caseS = caseS.faces(">Z").fillet(ffs)
        #
        # Round bottom
        #
        caseS = caseS.faces("<Z").fillet(ffs)

        if (rotation > 0.01):
            caseS = caseS.rotate((0,0,0), (0,0,1), rotation)

        return (caseS.clean())
        

    def make_body_with_ring_cricle(self, origo_x, origo_y, A1, D, pin_number, pin_type, pin_spigot, pin_top_diameter, H, alpha_delta, rotation):
            
        
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).circle(D / 2.0, False).extrude(H)
        #
        # Make ring on the middle of the body
        #
        DDq = 4.0
        #
        TT = D - DDq
        F1 = (H - 2.0) / 2.0
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0 + 6.0, False).extrude(F1 + 0.1)
        case2 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0, False).extrude(F1 + 0.1)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 + F1 + 2.0).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0 + 6.0, False).extrude(H)
        case2 = cq.Workplane("XY").workplane(offset=A1 + F1 + 2.0).moveTo(origo_x, 0 - origo_y).circle(TT / 2.0, False).extrude(H)
        case1 = case1.cut(case2)
        case = case.cut(case1)
        
        #
        # Cut circles around the ring
        #
        tx = (D / 2.0) + (2.0 * DDq)
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x + tx, 0 - origo_y).circle(2.5 * DDq, False).extrude(H + 0.2)
        case = case.cut(case1)
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(origo_x - tx, 0 - origo_y).circle(2.5 * DDq, False).extrude(H + 0.2)
        case = case.cut(case1)
        
        caseS = self.make_spigot(case, origo_x, origo_y, A1, pin_number, pin_spigot, pin_top_diameter, H, alpha_delta, rotation)
        #
        # Round bottom
        #
        caseS = caseS.faces("<Z").fillet(D / 70.0)
        #
        # Round top
        #
        caseS = caseS.faces(">Z").fillet(D / 70.0)
        
        if (rotation > 0.01):
            caseS = caseS.rotate((0,0,0), (0,0,1), rotation)

        return (caseS.clean())
        

    def make_body_round(self, origo_x, origo_y, A1, D, pin_number, pin_type, pin_spigot, pin_top_diameter, H, alpha_delta, rotation):
        
        case = cq.Workplane("XY").workplane(offset=A1).moveTo(origo_x, 0 - origo_y).circle(D / 2.0, False).extrude(H)
        
        caseS = self.make_spigot(case, origo_x, origo_y, A1, pin_number, pin_spigot, pin_top_diameter, H, alpha_delta, rotation)
        #
        # Round bottom
        #
        caseS = caseS.faces("<Z").fillet(D / 30.0)
        #
        # Round top
        #
        caseS = caseS.faces(">Z").fillet(D / 50.0)
        
        if (rotation > 0.01):
            caseS = caseS.rotate((0,0,0), (0,0,1), rotation)

        return (caseS.clean())
        
        
        
        
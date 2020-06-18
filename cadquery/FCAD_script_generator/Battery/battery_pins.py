#!/usr/bin/python
# -*- coding: utf-8 -*-

import battery_common
from battery_common import *

import battery_contact
from battery_contact import *
    
def make_pins(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
    cellcnt = params.cellcnt            # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BC = params.BC                      # Blend height
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    pp = None
    A11 = get_body_offset(params)

    for n in pins:
        if n[0] == 'tht':
            xx = n[1]
            yy = n[2]
            dd1 = n[4]
            dd2 = n[5]
            pl = n[6]
            if n[3] == 'round':
                pint = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(xx, 0.0 - yy).circle(dd1 / 2.0, False).extrude(0.0 - (pl + A11))
                pint = pint.faces("<Z").fillet(dd1 / 2.2)
            elif n[3] == 'rect':
                pint = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(xx, 0.0 - yy).rect(dd1, dd2).extrude(0.0 - (pl + A11))
                if (A11 - A1) > 0.1:
                    pine = cq.Workplane("XY").workplane(offset=A1).moveTo(xx, 0.0 - yy).rect(dd1, 2.0 * dd2).extrude((A11 - A1) + 0.2)
                    pint = pint.union(pine)
            elif n[3] == 'rectround':
                pint = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(xx, 0.0 - yy).rect(dd1, dd2).extrude(0.0 - (pl + A11))
                if (A11 - A1) > 0.1:
                    pine = cq.Workplane("XY").workplane(offset=A1).moveTo(xx, 0.0 - yy).rect(dd1, 2.0 * dd2).extrude(A11 + 0.1)
                    pint = pint.union(pine)
                if dd1 < dd2:
                    pint = pint.faces("<Z").edges(">Y").fillet(dd2 / 2.2)
                    pint = pint.faces("<Z").edges("<Y").fillet(dd2 / 2.2)
                else:
                    pint = pint.faces("<Z").edges(">X").fillet(dd1 / 2.2)
                    pint = pint.faces("<Z").edges("<X").fillet(dd1 / 2.2)
            elif n[3] == 'rectbend':
#        pins = [('tht', -06.605, 00.00, 'rectbend', 01.57, 00.20, 03.16, 01.26), ('tht', 06.605, 00.00, 'rectbend', 01.57, 00.20, 03.16, 01.26)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
                bh = n[7]
                dL_3 = pl - (2.0 * bh)
                hddy = dL_3 * math.sin(math.radians(45.0))
                hddx = dL_3 * math.cos(math.radians(45.0))
                pts = []
                pts.append((0.0, 0.0 - dL_3))
                pts.append((0.0 - hddx, 0.0 - dL_3 - hddy))
                pts.append((0.0, 0.0 - dL_3 - (2.0 * hddy)))
                pts.append((0.0, 0.0 - dL_3 - (2.0 * hddy) - 0.2))
                pts.append((0.0 - hddx - 0.2, 0.0 - dL_3 - hddy))
                pts.append((0.0 - dd2, 0.0 - dL_3))
                pts.append((0.0 - dd2, 0.0))
                pint = cq.Workplane("XZ").workplane(offset = 0.0).polyline(pts).close().extrude(dd1)
                
                if pp == None:
                    pint = pint.translate((xx + (dd2 / 2.0), yy + (3.0 * dd2), A1 + A11))
                else:
                    pint = pint.rotate((0,0,0), (0,0,1), 180.0)
                    pint = pint.translate((xx - (dd2 / 2.0), yy - (3.0 * dd2), A1 + A11))
                
                
                
                
                
        elif n[0] == 'smd':
            xx = n[1]
            yy = n[2]
            dd1 = n[4]
            dd2 = n[5]
            if n[3] == 'rect':
                pint = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(xx, yy).rect(dd1, dd2).extrude(0.2)
                if len(n) > 6:
                    dhl2 = n[6]
                    pine = cq.Workplane("XY").workplane(offset=A1 + A11 - 0.1).moveTo(xx, yy).circle(dhl2 / 2.0, False).extrude(0.3)
                    pint = pint.cut(pine)
        
        if pp == None:
            pp = pint
        else:
            pp = pp.union(pint)
 
    #
    # The little ear ontop
    #
    if topear != None:
        for n in topear:
            xx = n[0]
            yy = n[1]
            tw = n[2]
            th = n[3]
            pint = cq.Workplane("XY").workplane(offset=A1 + A11 + H - 0.1).moveTo(xx, yy).rect(1.0, tw).extrude(th)
            pint = pint.faces(">Z").edges(">Y").fillet(tw / 2.2)
            pint = pint.faces(">Z").edges("<Y").fillet(tw / 2.2)
            pine = cq.Workplane("YZ").workplane(offset=xx - 2.0).moveTo(yy, A1 + A11 + H + th - (tw / 1.5)).circle(tw / 4.0, False).extrude(4.0)
            pint = pint.cut(pine)
            pp = pp.union(pint)
    
    if BC != None:
        if BC[0] == 'BC1':
            pint, pint1 = make_battery_contact_BC1(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
        elif BC[0] == 'BC2':
            pint, pint1 = make_battery_contact_BC2(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
        elif BC[0] == 'BC3':
            pint, pint1 = make_battery_contact_BC3(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
        elif BC[0] == 'BC4':
            pint, pint1 = make_battery_contact_BC4(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
        elif BC[0] == 'BC5':
            pint, pint1 = make_battery_contact_BC5(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
        elif BC[0] == 'BC6':
            pint, pint1 = make_battery_contact_BC6(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
        elif BC[0] == 'BC7':
            pint, pint1 = make_battery_contact_BC7(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
        elif BC[0] == 'BC8':
            pint, pint1 = make_battery_contact_BC8(params)
            pp = pp.union(pint)
            pp = pp.union(pint1)
                
    if (rotation > 0.01):
        pp = pp.rotate((0,0,0), (0,0,1), rotation)

    return (pp)


def make_npthpins_S2(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize    # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BC = params.BC                      # Blend height
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)

    # npthpins = ['S2', 15.2, 0.0, 19.00, 1.57, 2.54],  # 'type', x, y, circle diameter, pig diameter, pig height))]

    x1 = npthpins[1]
    y1 = npthpins[2]
    largeradie = npthpins[3] / 2.0
    pinradie = npthpins[4] / 2.0
    pinlength = npthpins[5]
    #
    x = largeradie * math.sin(math.radians(0.0))
    y = 0.0 - largeradie * math.cos(math.radians(0.0))
    pint = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(x1 + x, y1 + y).circle(pinradie, False).extrude(0.0 - pinlength)
    pint = pint.faces("<Z").fillet(pinradie / 2.2)
    
    #
    x = largeradie * math.sin(math.radians(120.0))
    y = 0.0 - largeradie * math.cos(math.radians(120.0))
    pine = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(x1 + x, y1 + y).circle(pinradie, False).extrude(0.0 - pinlength)
    pine = pine.faces("<Z").fillet(pinradie / 2.2)
    pint = pint.union(pine)
    
    #
    x = largeradie * math.sin(math.radians(240.0))
    y = 0.0 - largeradie * math.cos(math.radians(240.0))
    pine = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(x1 + x, y1 + y).circle(pinradie, False).extrude(0.0 - pinlength)
    pine = pine.faces("<Z").fillet(pinradie / 2.2)
    pint = pint.union(pine)
    
    
    return pint

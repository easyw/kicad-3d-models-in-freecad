#!/usr/bin/python
# -*- coding: utf-8 -*-

import battery_common
from battery_common import *
    
import battery_pins
from battery_pins import *


def make_case_Button1(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
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
    #
    #
    x1 = LC[0]
    y1 = LC[1]
    od = LC[2]
    id = LC[3]
    hh = LC[4]
    dd = (od - id) / 2.0
    
    # Base large circle
    case = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(x1, y1).circle(od / 2.0, False).extrude(hh)
    # Cut out the inner circle
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + 1.0).moveTo(x1, y1).circle(id / 2.0, False).extrude(hh + 2.0)
    case = case.cut(case1)
    case = case.faces(">Z").fillet(dd / 4.0)
    
    sx1 = 0.0 - spigot[1]
    sy1 = 0.0 - (spigot[2] / 2.0)
    sw = spigot[2]
    bcw = BC[1]
    # Spigot
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(sx1, sy1).rect(x1, sw, centered=False).extrude(hh)
    # Cut out the spigot
    case2 = cq.Workplane("XY").workplane(offset=A1 + A11 + 1.0).moveTo(sx1 + 1.0, sy1 + (sw - 1.0)).rect(x1, 0.0 - (sw - 2.0), centered=False).extrude(hh + 2.0)
    incase1 = cq.Workplane("XY").workplane(offset=A1 + A11 + 1.0).moveTo(x1, y1).circle(id / 2.0, False).extrude(hh + 2.0)
    #
    case = case.cut(case1)
    case1 = case1.cut(incase1)
    case1 = case1.cut(case2)
    case = case.union(case1)
    #
    

    # Cut out right side, a 90 degree romb
    pts = []
    #
    dh1 = (od + 2.0)
    dy1 = dh1 * math.sin(math.radians(45.0))
    pts.append((dh1, dy1))
    #
    pts.append((dh1, 0.0 - dy1))
    
    case1 = cq.Workplane("XY").workplane(offset = 0.0).polyline(pts).close().extrude(hh + 2.0)
    case1 = case1.translate((x1, y1, A1 + A11 + (hh / 2.0)))
    case = case.cut(case1)
    
    # Remove edges
    case1 = case.faces("<Z").fillet(od / 60.0)
#    case1 = case.faces(">Z").edges("<X").fillet(dd / 4.0)
    
    if npthpins != None:
        for n in npthpins:
            if npthpins[0] == 'S2':
                case1 = make_npthpins_S2(params)
                case = case.union(case1)
            elif n[0] == 'pin':
                    xx = n[1]
                    yy = 0.0 - n[2]
                    if n[3] == 'round':
                        dd = n[3]
                        dl = n[4]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).circle(dd / 2.0, False).extrude(0.0 - (dl + 0.1))
                        pint = pint.faces("<Z").fillet(dl / 2.2)
                        case = case.union(pint)
                    elif n[3] == 'rect':
                        dd1 = n[3]
                        dd2 = n[4]
                        dl = n[5]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).rect(ddl, dd2).extrude(dl + 0.1)
                        if dd1 < dd2:
                            pint = pint.faces("<Z").fillet(ddl / 2.2)
                        else:
                            pint = pint.faces("<Z").fillet(dd2 / 2.2)                        
                        case = case.union(pint)
            elif n[0] == 'hole':
                    xx = n[1]
                    yy = 0.0 - n[2]
                    dd = n[3]
                    dl = n[4]
                    pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).circle(dd / 2.0, False).extrude(0.0 - (dl + 0.1))
                    case = case.cut(pint)
    
    #
    if (rotation >  0.01):
        case = case.rotate((0,0,0), (0,0,1), rotation)
        
    return (case)


def make_case_Button2(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
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
    #
    #
    x1 = LC[0]
    y1 = LC[1]
    od = LC[2]
    id = LC[3]
    hh = LC[4]
    dd = (od - id) / 2.0
    
    # Base large circle
    case = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(x1, y1).circle(od / 2.0, False).extrude(hh)
    
    #
    # Spigot
    #
    if spigot != None:
        if len(spigot) == 2:
            case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0, 0.0).rect(spigot[0], spigot[1]).extrude(H)
            case = case.union(case1)
    
    # Cut out the inner circle
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + 1.0).moveTo(x1, y1).circle(id / 2.0, False).extrude(hh + 2.0)
    case = case.cut(case1)

    #
    # Cut the sides
    #
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0 - (L / 2.0), (W / 2.0)).rect(L, W, centered=False).extrude(H + 2.0)
    case = case.cut(case1)
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0 - (L / 2.0), 0.0 - (W / 2.0)).rect(L, 0.0 - W, centered=False).extrude(H + 2.0)
    case = case.cut(case1)
    
    #
    # Cut the jagged edge on the side
    #
    ll = W / 3.3
    pts = []
    pts.append((ll, ll))
    pts.append((ll + (ll / 2.0), ll))
    pts.append((ll + (ll / 2.0) + ll, 0.0))
    case1 = cq.Workplane("XY").workplane(offset = 0.0).polyline(pts).close().extrude(H + 2.0)
    case1 = case1.translate((0.0 - (ll * 1.25), 0.0 - ((W / 2.0) + (ll / 2.0)), A1 + A11))
    case = case.cut(case1)
    
    case = case.faces("<Z").fillet(od / 100.0)
    case = case.faces(">Z").fillet(od / 100.0)
    
    if npthpins != None:
        for n in npthpins:
            if npthpins[0] == 'S2':
                case1 = make_npthpins_S2(params)
                case = case.union(case1)
            elif n[0] == 'pin':
                    xx = n[1]
                    yy = 0.0 - n[2]
                    if n[3] == 'round':
                        dd = n[3]
                        dl = n[4]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).circle(dd / 2.0, False).extrude(0.0 - (dl + 0.1))
                        pint = pint.faces("<Z").fillet(dl / 2.2)
                        case = case.union(pint)
                    elif n[3] == 'rect':
                        dd1 = n[3]
                        dd2 = n[4]
                        dl = n[5]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).rect(ddl, dd2).extrude(dl + 0.1)
                        if dd1 < dd2:
                            pint = pint.faces("<Z").fillet(ddl / 2.2)
                        else:
                            pint = pint.faces("<Z").fillet(dd2 / 2.2)                        
                        case = case.union(pint)
            elif n[0] == 'hole':
                    xx = n[1]
                    yy = 0.0 - n[2]
                    dd = n[3]
                    dl = n[4]
                    pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).circle(dd / 2.0, False).extrude(0.0 - (dl + 0.1))
                    case = case.cut(pint)


    #
    if (rotation >  0.01):
        case = case.rotate((0,0,0), (0,0,1), rotation)
        
    return (case)


def make_case_Button3(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
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
    #
    #
    x1 = LC[0]
    y1 = LC[1]
    od = LC[2]
    id = LC[3]
    hh = LC[4]
    dd = (od - id) / 2.0
    
    # Base large circle
    case = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(x1, y1).rect(od, W).extrude(hh)
    case = case.faces("<Y").edges("<X").chamfer(1.0)

    #
    # Spigot
    #
    if spigot != None:
        if len(spigot) == 2:
            case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0, 0.0).rect(spigot[0], spigot[1]).extrude(H)
            case = case.union(case1)
    
    # Cut out the inner circle
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + 1.0).moveTo(x1, y1).circle(id / 2.0, False).extrude(hh + 2.0)
    case = case.cut(case1)

    FreeCAD.Console.PrintMessage('make_case_Button2 2\r\n')
    
    #
    # Cut the sides
    #
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0 - (L / 2.0), (W / 2.0)).rect(L, W, centered=False).extrude(H + 2.0)
    case = case.cut(case1)
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0 - (L / 2.0), 0.0 - (W / 2.0)).rect(L, 0.0 - W, centered=False).extrude(H + 2.0)
    case = case.cut(case1)
    
    case = case.faces("<Z").fillet(od / 100.0)
    case = case.faces(">Z").fillet(od / 100.0)
    
    if npthpins != None:
        for n in npthpins:
            if npthpins[0] == 'S2':
                case1 = make_npthpins_S2(params)
                case = case.union(case1)
            elif n[0] == 'pin':
                    xx = n[1]
                    yy = 0.0 - n[2]
                    if n[3] == 'round':
                        dd = n[3]
                        dl = n[4]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).circle(dd / 2.0, False).extrude(0.0 - (dl + 0.1))
                        pint = pint.faces("<Z").fillet(dl / 2.2)
                        case = case.union(pint)
                    elif n[3] == 'rect':
                        dd1 = n[3]
                        dd2 = n[4]
                        dl = n[5]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).rect(ddl, dd2).extrude(dl + 0.1)
                        if dd1 < dd2:
                            pint = pint.faces("<Z").fillet(ddl / 2.2)
                        else:
                            pint = pint.faces("<Z").fillet(dd2 / 2.2)                        
                        case = case.union(pint)
            elif n[0] == 'hole':
                    xx = n[1]
                    yy = 0.0 - n[2]
                    dd = n[3]
                    dl = n[4]
                    pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).circle(dd / 2.0, False).extrude(0.0 - (dl + 0.1))
                    case = case.cut(pint)


    #
    if (rotation >  0.01):
        case = case.rotate((0,0,0), (0,0,1), rotation)
        
    return (case)


def make_case_Button4(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
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
    #
    #
    
    # Dummy
    case = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0, 0.0).rect(0.01, 0.01).extrude(0.01)

    return case
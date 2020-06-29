#!/usr/bin/python
# -*- coding: utf-8 -*-

import battery_common
from battery_common import *

import battery_pins
from battery_pins import *

    
def make_case_Cylinder1(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BS = params.BS                      # If the side should be 'round' or 'chamfer'
    BC = params.BC                      # Blend height
    BM = params.BM                      # Center of body
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)
    
    cellD, cellL = get_battery_size(params)
    h2 = (cellD / 2.0) + 0.5

    
    case = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0, 0.0).rect(L, W).extrude(h2)

    
    sls = cellL
    h2 = (cellD / 2.0) + 0.5
    x2 = 0.0 - (sls / 2.0)
    y2 = (W / 2.0) - (cellD / 2.0)
    z2 = A1 + A11 + h2
    x21 = x2
    #
    if ((2.0 * cellL) < L):
        sls = 2.0 * cellL
        x21 = 0.0 - (sls / 2.0)
    #
    #
    case1 = cq.Workplane("YZ").workplane(offset=x21).moveTo(y2, z2).circle(cellD / 2.0, False).extrude(sls)
    case = case.union(case1)
    #
    y9 = 0.0 - ((W / 2.0) - (cellD / 2.0))
    case1 = cq.Workplane("YZ").workplane(offset=x21).moveTo(y9, z2).circle(cellD / 2.0, False).extrude(sls)
    case = case.union(case1)
    #
    # Make ends
    #
    dx3 = 2.0
    x3 = 0.0 - ((L / 2.0) - (dx3 / 2.0))
    case1 = None
    #
    # Make round ends
    #
    if BS[0] == 'round':
        #
        # End sides should be round
        #
        case1 = cq.Workplane("YZ").workplane(offset=0.0 - (L / 2.0)).moveTo(y2, A1 + A11 + h2).circle(cellD / 2.0, False).extrude(dx3)
        case = case.union(case1)
        case1 = cq.Workplane("YZ").workplane(offset=0.0 - (L / 2.0)).moveTo(y9, A1 + A11 + h2).circle(cellD / 2.0, False).extrude(dx3)
        case = case.union(case1)
        rdx = math.fabs(y9 - y2)
        rx = y9 - y2
        case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + h2 - 0.1).moveTo(0.0 - (L / 2.0), y2).rect(dx3, rx, centered=False).extrude((cellD / 2.0) + 0.1)
        case = case.union(case1)
        #
        dx8 = 2.0
        x8 = (L / 2.0) - dx8
        case1 = cq.Workplane("YZ").workplane(offset=x8).moveTo(y2, A1 + A11 + h2).circle(cellD / 2.0, False).extrude(dx3)
        case = case.union(case1)
        case1 = cq.Workplane("YZ").workplane(offset=x8).moveTo(y9, A1 + A11 + h2).circle(cellD / 2.0, False).extrude(dx3)
        case = case.union(case1)
        case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + h2 - 0.1).moveTo(x8, y2).rect(dx3, rx, centered=False).extrude((cellD / 2.0) + 0.1)
        case = case.union(case1)
        
    else:
        #
        # End sides should be chamfer
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + h2 - 0.1).moveTo(x3, 0.0).rect(dx3, W).extrude(h2)
        case1 = case1.faces(">Z").edges("<Y").chamfer(h2 / 1.01, W / 4.0)
        case1 = case1.faces(">Z").edges(">Y").chamfer(W / 4.0, h2 / 1.01)
        case = case.union(case1)
        #
        dx8 = 2.0
        x8 = (L / 2.0) - (dx8 / 2.0)
        case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + h2 - 0.1).moveTo(x8, 0.0).rect(dx8, W).extrude(h2)
        case1 = case1.faces(">Z").edges("<Y").chamfer(h2 / 1.01, W / 4.0)
        case1 = case1.faces(">Z").edges(">Y").chamfer(W / 4.0, h2 / 1.01)
        case = case.union(case1)
    
    #
    # Cut the top
    #
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + H - 0.01).moveTo(0.0, 0.0).rect(L + 2.0, W + 2.0).extrude(2.0 * H)
    case = case.cut(case1)
    #
    #
    cll = (L - dx3 - dx8)
    z3 = A1 + A11 + (cellD / 2.0) + 0.2
    y7 = 0.0 - (((cellcnt - 1) / 2.0) * cellD)
    d7y = (cellD)
    if cellcnt == 1:
        #
        # Cut the gut at h2 height to get it flat halfway up
        #
        case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + h2).moveTo(0.0, y7).rect(cll, cellD).extrude(H)
        case = case.cut(case1)
        #
        # Cut the gut to equal to a cell
        #
        case1 = cq.Workplane("YZ").workplane(offset=0.0 - (cll / 2.0)).moveTo(y7, z3).circle(cellD / 2.0, False).extrude(cll)
        case = case.cut(case1)
    else:
        #
        for c in range(0, cellcnt):
            #
            # Cut the gut at h2 height to get it flat halfway up
            #
            case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + h2).moveTo(0.0, y7).rect(cll, cellD).extrude(H)
            case = case.cut(case1)

            #
            # Cut the gut to equal to a cell
            #
            case1 = cq.Workplane("YZ").workplane(offset=0.0 - (cll / 2.0)).moveTo(y7, z3).circle(cellD / 2.0, False).extrude(cll)
            case = case.cut(case1)
            y7 = y7 + d7y
    
    #
    # Cut sidde
    #
    ddl = (L // 10)
    
    x5 = 0.0 - ((L / 2.0) - (ddl / 2.0) - dx3)
    case1 = cq.Workplane("XY").workplane(offset=z2).moveTo(x5, W).rect(ddl, 4.0 * W).extrude(H / 2.0)
    case = case.cut(case1)
    #
    ddl = (L // 10)
    x6 = (L / 2.0) - (ddl / 2.0) - dx8
    case1 = cq.Workplane("XY").workplane(offset=z2).moveTo(x6, W).rect(ddl, 4.0 * W).extrude(H / 2.0)
    case = case.cut(case1)
    #
    ddl = (L // 2)
    case1 = cq.Workplane("XY").workplane(offset=z2).moveTo(0.0, 0.0).rect(ddl, 4.0 * W).extrude(H / 2.0)
    case = case.cut(case1)

    if BM != None:
        x1 = BM[0]
        y1 = 0.0 - BM[1]
        case = case.translate((x1, y1, 0.0))
    
    if npthpins != None:
        for n in npthpins:
            if npthpins[0] == 'S2':
                case1 = make_npthpins_S2(params)
                case = case.union(case1)
            elif n[0] == 'pin':
                    xx = n[1]
                    yy = n[2]
                    if n[3] == 'round':
                        dd = n[4]
                        dl = n[5]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, 0.0 - yy).circle(dd / 2.0, False).extrude(0.0 - (dl + 0.1))
                        pint = pint.faces("<Z").fillet(dd / 2.2)
                        case = case.union(pint)
                    elif n[3] == 'rect':
                        dd1 = n[4]
                        dd2 = n[5]
                        dl = n[6]
                        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, 0.0 - yy).rect(ddl, dd2).extrude(dl + 0.1)
                        if dd1 < dd2:
                            pint = pint.faces("<Z").fillet(ddl / 2.2)
                        else:
                            pint = pint.faces("<Z").fillet(dd2 / 2.2)                        
                        case = case.union(pint)
            elif n[0] == 'hole':
                    xx = n[1]
                    yy = n[2]
                    dd = n[3]
                    pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, 0.0 - yy).circle(dd / 2.0, False).extrude((H + A1 + 0.1))
                    case = case.cut(pint)

    return (case)

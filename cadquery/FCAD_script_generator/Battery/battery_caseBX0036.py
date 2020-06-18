#!/usr/bin/python
# -*- coding: utf-8 -*-

import battery_common
from battery_common import *
    
    
def make_case_BX0036(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize    # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)
    #
    #
    p = pins[0]
    x1 = p[1]
    yy = p[2]
    #
    p = pins[1]
    x2 = p[1]
    #
    xx = x1 - ((L - (x2 - x1)) / 2.0)
    
    pts = []
    pts.append((xx, 0.0))
    #
    pts.append((xx, 0.0 + H))
    #
    pts.append((xx + 3.0, 0.0 + H))
    #
    pts.append((xx + 3.0, 0.0 + 11.0))
    #
    pts.append((xx + 3.0 + 6.0, 0.0 + 5.0))
    #
    pts.append((xx + L - (3.0 + 6.0), 0.0 + 5.0))
    #
    pts.append((xx + L - (3.0), 0.0 + 11.0))
    #
    pts.append((xx + L - (3.0), 0.0 + H))
    #
    pts.append((xx + L, 0.0 + H))
    #
    pts.append((xx + L, 0.0))
    #
#    pts.append((xx + 0.0001, A1 + A11))
    
    case = cq.Workplane("XZ").workplane(offset = 0.0 - (W / 2.0)).polyline(pts).close().extrude(W)
    case = case.translate((0.0, 0.0, A1 + A11))

    tx = ((x2 - x1) / 2.0) + x1
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + 3.0).moveTo(tx, yy).rect(L - 6.0, W - 12.0).extrude(H)
    case = case.cut(case1)
    #
    case1 = cq.Workplane("XY").workplane(offset=A1 + A11 + 5.0).moveTo(tx, yy).rect(L - 6.0, W - 2.0).extrude(H)
    case = case.cut(case1)

    case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo((L / 2.0) - 3.0, 0.0 - ((W / 2.0) - 1.5)).rect(6, 3.0).extrude(H)
    case1 = case1.faces(">Z").edges(">Y").chamfer(2.0)
    case = case.union(case1)

    case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo((L / 2.0) + 3.0, ((W / 2.0) - 1.5)).rect(6, 3.0).extrude(H)
    case1 = case1.faces(">Z").edges("<Y").chamfer(2.0)
    case = case.union(case1)

    if cellsize == 'C':
        case1 = cq.Workplane("YZ").workplane(offset=tx - 25.0).moveTo(0.0, (H / 2.0) + 3.0).circle(26.2 / 2.0, False).extrude(50.0)
        case = case.cut(case1)
#        case1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo((L / 2.0) + 3.0, ((W / 2.0) - 1.5)).rect(6, 3.0).extrude(H)
    #
    

    if socket != None:
        if socket[0] == 'S1':
            scd = socket[1]
            scl = socket[2]
            sch = socket[3]
            for n in npthpins:
                xx = n[1]
                yy = n[2]
                dd = n[3]
                #
                pint = cq.Workplane("XY").workplane(offset=A1).moveTo(xx, yy).rect(scl, W).extrude(sch)
                case = case.union(pint)
                pint = cq.Workplane("XY").workplane(offset=A1).moveTo(xx, yy).circle(scd / 2.0, False).extrude(sch)
                case = case.union(pint)
                
    for n in npthpins:
        xx = n[1]
        yy = n[2]
        dd = n[3]
        pint = cq.Workplane("XY").workplane(offset=A1 - 0.1).moveTo(xx, yy).circle(dd / 2.0, False).extrude(H + 0.2)
        case = case.cut(pint)
        
    #
    #
    if (rotation >  0.01):
        case = case.rotate((0,0,0), (0,0,1), rotation)
        
    return (case)

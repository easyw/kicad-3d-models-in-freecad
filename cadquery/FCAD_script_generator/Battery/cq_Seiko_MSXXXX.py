#!/usr/bin/python
# -*- coding: utf-8 -*-

import battery_common
from battery_common import *


def make_case_Seiko_MS621F(params):

    A1 = params.A1              # Body PCB seperation
    D  = params.D               # Battery diameter
    H  = params.H               # Battery height
    PL = params.PL              # Pad length
    PW = params.PW              # Pad width
    RW = params.RW              # Right width
    MT = params.MT              # Metal thickness
    rotation = params.rotation  # Rotation if required

    D2 = D * 0.8
    H2 = 0.075
    D3 = D * 0.78
    H3 = 0.23
    #
    H1 = H - ((2.0 * MT) + H2 + H3) 
    D1 = D

    dh = MT
    #
    # Create body
    #
    case = cq.Workplane("XY").workplane(offset=dh).moveTo(0.0, 0.0).circle(D3 / 2.0, False).extrude(H3)
    case.edges("<Z").fillet(H3 / 2.2)
    dh = dh + H3
    #
    case1 = cq.Workplane("XY").workplane(offset=dh).moveTo(0.0, 0.0).circle(D2 / 2.0, False).extrude(H2)
    case1.edges("<Z").fillet(H2 / 2.2)
    case = case.union(case1)
    dh = dh + H2
    #
    case1 = cq.Workplane("XY").workplane(offset=dh).moveTo(0.0, 0.0).circle(D / 2.0, False).extrude(H1)
    case1.edges("<Z").fillet((H1 / 3.0))
    case1.edges(">Z").fillet(H1 / 20.0)
    case = case.union(case1)
    dh = dh + H1
    
    #
    x = PW / 2.0
    cx = (x - RW) - (D1 / 2.0)

    case = case.translate((cx, 0.0, A1))
    
    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)

    return (case)


def make_pins_Seiko_MS621F(params):

    A1 = params.A1              # Body PCB seperation
    D  = params.D               # Battery diameter
    H  = params.H               # Battery height
    PL = params.PL              # Pad length
    PW = params.PW              # Pad width
    RW = params.RW              # Right width
    RW1 = params.RW1            # Right width 1
    MT = params.MT              # Metal thickness
    rotation = params.rotation  # Rotation if required

    TL = 0.5 # the width of the tounghs
    D2 = D * 0.8
    H2 = 0.075
    D3 = D * 0.78
    H3 = 0.23
    #
    H1 = H - ((2.0 * MT) + H2 + H3) 
    D1 = D
    #
    x = PW / 2.0
    cx = (x - RW) - (D1 / 2.0)

    dh = MT
    
    #
    pts = []
    pts.append((0.0, 0.0 - PL))
    pts.append((D3 * 0.9 + ((D1 - D3) / 2.0) + RW, 0.0 - PL))
    pts.append((D3 * 0.9 + ((D1 - D3) / 2.0) + RW, 0.0 - (PL - TL)))
    pts.append((D3 * 0.9 + ((D1 - D3) / 2.0), 0.0 - (PL - TL)))
    pts.append(((D3 * 0.9 + ((D1 -D3) / 2.0)) - (PL - TL), 0.0))
    pin = cq.Workplane("XY").workplane(offset=0.0).polyline(pts).close().extrude(MT)

    x = 0.0 - (D3 * 0.9 + ((D1 - D3) / 2.0) + RW)
    x = x + (PW / 2.0)
    
    pin = pin.translate((x, (PL / 2.0), A1))
    
    #
    pts = []
    pts.append((0.0, MT))
    pts.append((0.0 - (RW1 - MT), MT))
    pts.append((0.0 - (RW1 - MT), H))
    pts.append((0.0 - (RW1 - MT) - (RW - RW1) - (D1 * 0.6), H))
    pts.append((0.0 - (RW1 - MT) - (RW - RW1) - (D1 * 0.6), H - MT))
    pts.append((0.0 - RW1, H - MT))
    pts.append((0.0 - RW1, 0.0))
    pin1 = cq.Workplane("XZ").workplane(offset=0.0).polyline(pts).close().extrude(PL)

    case21 = cq.Workplane("XY").workplane(offset=0.0 - MT).moveTo(0.0 - (PW / 2.0), 0.0 - 1.5).rect(2.0 * PW, PL).extrude(2.0 * MT)
    pin1 = pin1.cut(case21)

    case21 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - RW1 - (MT / 4.0), 0.0).rect(1.5 * MT, 0.0 - (2.0 * PL), centered=False).extrude(0.0 - PL)
    case21 = case21.rotate((0,0,0), (1, 0, 0), 0.0 - 45.0)
    case21 = case21.translate((0.0, 0.0 - TL, MT))
    pin1 = pin1.cut(case21)

    pin1 = pin1.translate((PW / 2.0, PL / 2.0, A1))
    pin1.faces(">Z").edges(">X").fillet((MT / 2.0))
    pin = pin.union(pin1)
    
    if (rotation != 0):
        pin = pin.rotate((0,0,0), (0,0,1), rotation)

    return (pin)

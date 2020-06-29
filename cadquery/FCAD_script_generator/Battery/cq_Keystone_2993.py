#!/usr/bin/python
# -*- coding: utf-8 -*-

import battery_common
from battery_common import *


def make_case_Keystone_2993(params):

    A1 = params.A1              # Body PCB seperation
    L  = params.L               # Package length
    L1 = params.L1              # Package length 1
    L2 = params.L2              # Package length 2
    W  = params.W               # Package width
    W1 = params.W1              # Package width 1
    MT = params.MT              # Metal thickness
    npthpins = params.npthpins  # npth holes
    rotation = params.rotation  # Rotation if required

    #
    # Create body
    #
    case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L2).extrude(MT)
#    case = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(W, L).extrude(MT)
#    case1 = cq.Workplane("XY").workplane(offset=0.0 - MT).moveTo(0.0 - L2, L - ((L - L2) / 2.0)).rect(W, L).extrude(2.0 * MT)
#    case = case.cut(case1)
#    case1 = cq.Workplane("XY").workplane(offset=0.0 - MT).moveTo(0.0 - L2, 0.0 - (L - ((L - L2) / 2.0))).rect(W, L).extrude(2.0 * MT)
#    case = case.cut(case1)
    
    for n in npthpins:
        x = (0.0 - (W / 2.0)) + n[1]
        y = n[2]
        d = n[3]
        case1 = cq.Workplane("XY").workplane(offset=0.0 - MT).moveTo(x, y).circle(d / 2.0, False).extrude(2.0 * MT)
        case = case.cut(case1)
   
    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)

    return (case)


def make_pins_Keystone_2993(params):

    A1 = params.A1              # Body PCB seperation
    L  = params.L               # Package length
    L1 = params.L1              # Package length 1
    L2 = params.L2              # Package length 2
    W  = params.W               # Package width
    W1 = params.W1              # Package width 1
    MT = params.MT              # Metal thickness
    npthpins = params.npthpins  # npth holes
    rotation = params.rotation  # Rotation if required

    #
    pts = []
    pts.append((0.0, MT))
    pts.append((0.0 - 3.23, MT))
    pts.append((0.0 - 10.80, 2.68))
    pts.append((0.0 - 14.11, 2.11))
    pts.append((0.0 - 14.11, 2.11 - MT))
    pts.append((0.0 - 10.80, 2.68 - MT))
    pts.append((0.0 - 3.23, 0.0))
    pin = cq.Workplane("XZ").workplane(offset=0.0).polyline(pts).close().extrude(L)

    case1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0 - 8.67, 0.0 - (L / 2.0)).rect(10.88, 4.06).extrude(3.0)
    pin = pin.cut(case1)

    pin.faces(">X").edges("<Y").fillet(L1 / 3.0)
    pin.faces(">X").edges(">Y").fillet(L1 / 3.0)
    pin.faces(">Z").edges(">X").fillet(L1 / 5.0)
    pin.faces("<X").edges("#Y").fillet(L1 / 5.0)
     
    pin = pin.translate((W / 2.0, (L / 2.0), A1))

    n = npthpins[2]
    x = (0.0 - (W / 2.0)) + n[1]
    y = n[2]
    d = n[3]
    case1 = cq.Workplane("XY").workplane(offset=0.0 - MT).moveTo(x, y).circle(d / 2.0, False).extrude(2.0 * MT)
    pin = pin.cut(case1)
     
    if (rotation != 0):
        pin = pin.rotate((0,0,0), (0,0,1), rotation)

    return (pin)

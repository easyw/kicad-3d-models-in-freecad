#!/usr/bin/python
# -*- coding: utf-8 -*-

import battery_common
from battery_common import *


def make_battery_contact_BC1(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize    # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BC = params.BC                      # Blend height
    BM = params.BM                      # Center of body
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    cellsize = params.cellsize           # Battery type
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)
    WW = BC[1]
    DX = 0.0
    PX = L
    if BM == None:
#        DX = BC[2]
        if BC != None:
            TX = 0.0 + BC[2]
            PX = L - BC[2]
        else:
            TX = 0.0 + 2.0
            PX = L - 2.0
    else:
        DX = BM[0] - (L / 2.0)
        TX = DX + 2.0
        PX = (DX + L) + 1.5
        
    #
    # Battery contact
    #
    pts = []
    pts.append((0.0, W / 4.0))
    pts.append((3.0, ((2.0 * W) / 3.0)))
    pts.append((1.0, H - 5.0))
    pts.append((1.4, H - 5.0))
    pts.append((3.4, ((2.0 * W) / 3.0)))
    pts.append((0.4, W / 4.0))
    pts.append((0.4, 0.0))
    pint = cq.Workplane("XZ").workplane(offset = 0.0).polyline(pts).close().extrude(WW)
    pint = pint.translate((TX, 1.4, A1 + A11 + 1.0))
    #
    pine = cq.Workplane("XZ").workplane(offset = 0.0).polyline(pts).close().extrude(WW)
    pine = pine.rotate((0,0,0), (0,0,1), 180.0)
    pine = pine.translate((PX - 3.4, 0.0 - 1.6, A1 + A11 + 1.0))
    
    return pint, pine

    
def make_battery_contact_BC2(params):

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
    cellsize = params.cellsize           # Battery type
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
    
    bcw = BC[1]
    bch1 = BC[2]
    
    tdd = (id / 2.0) * 0.3
    
#            BC = ['BC2', 2.0, 1.01],    # Battery contact width, height diff to top

    # Make the circular negative contact
    pint = cq.Workplane("XY").workplane(offset=A1 + A11 + 1.0).moveTo(x1, y1).circle((id / 2.0) * 0.7, False).extrude(0.2)
    pint1 = cq.Workplane("XY").workplane(offset=A1 + A11 + 1.0 - 0.2).moveTo(x1, y1).circle(tdd, False).extrude(0.2 + 0.4)
    pint = pint.cut(pint1)

    ptmh = hh + bch1
    pts = []
    pts.append((0.0, ptmh))
    #
    pts.append((x1 / 1.5, hh / 2.0))
    #
    pts.append((x1 + 4.0, hh / 2.0))
    #
    pts.append((x1 + 5.0, (hh / 2.0) + 1.0))
    #
    pts.append((x1 + 5.1, (hh / 2.0) + 1.0))
    #
    pts.append((x1 + 4.0, (hh / 2.0) - 0.1))
    #
    pts.append((x1 / 1.5, (hh / 2.0) - 0.1))
    #
    pts.append((0.1, (ptmh) - 0.1))
    #
    pts.append((0.1, 0.0))
    #
    pint1 = cq.Workplane("XZ").workplane(offset = 0.0).polyline(pts).close().extrude(bcw)
    pint1 = pint1.translate((0.0, bcw / 2.0, A1 + A11))

    return pint, pint1

    
def make_battery_contact_BC3(params):

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
    cellsize = params.cellsize           # Battery type
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)
    WW = BC[1]
    HW = BC[2]
    cellD, cellL = get_battery_size(params)

    #
    # Battery contact
    #
    hh = H + HW
    
    pts = []
    pts.append((0.0, hh))
    pts.append((1.0, hh))
    pts.append((2.0, ((2.0 * hh) / 3.0)))
    pts.append((2.0, hh / 2.0))
    #
    pts.append((1.9, hh / 2.0))
    pts.append((1.9, ((2.0 * hh) / 3.0)))
    pts.append((1.0, hh - 0.1))
    pts.append((0.1, hh - 0.1))
    pts.append((0.1, 0.0))
    #
    pint = cq.Workplane("XZ").workplane(offset = 0.0).polyline(pts).close().extrude(WW)
    pint = pint.translate((0.0 - ((cellL / 2.0)), (WW / 2.0), A1 + A11))
    #
    pts = []
    pts.append((0.0, hh))
    pts.append((-1.0, hh))
    pts.append((-2.0, ((2.0 * hh) / 3.0)))
    pts.append((-2.0, hh / 2.0))
    #
    pts.append((-1.9, hh / 2.0))
    pts.append((-1.9, ((2.0 * hh) / 3.0)))
    pts.append((-1.0, hh - 0.1))
    pts.append((-0.1, hh - 0.1))
    pts.append((-0.1, 0.0))
    #
    pint1 = cq.Workplane("XZ").workplane(offset = 0.0).polyline(pts).close().extrude(WW)
    pint1 = pint1.translate((((cellL / 2.0)), (WW / 2.0), A1 + A11))
    
    return pint, pint1

    
def make_battery_contact_BC4(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize    # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BC = params.BC                      # Blend height
    BM = params.BM                      # Center of body
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    cellsize = params.cellsize           # Battery type
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)
    cellD, cellL = get_battery_size(params)
    
    bcd = cellD
    #
    # Make ends
    #
    if BC[0] == 'BC4':
        dx3 = 2.0
    else:
        dx3 = (L - cellL) / 2.0

    

    x1 = (L / 2.0) - dx3
    x2 = 0.0 - x1
    y1 = 0.0
    #
    if cellcnt > 1:
        y1 = (cellD * ((cellcnt - 1) / 2.0))
    
    z1 = (A1 + A11) + (cellD / 2.0)
    z2 = (A1 + A11)
    
    tx = 0.25
    x1 = x1
    if BC[1] == 'switchright':
        tx = 0.0 - tx
        x1 = 0.0 - x1
    
    #
    # Dummy
    #
    pint = cq.Workplane("ZY").workplane(offset=A1 + A11 + 0.02).moveTo(0.0, 0.0).circle(0.01, False).extrude(0.01)
    pint1 = cq.Workplane("ZY").workplane(offset=A1 + A11 + 0.02).moveTo(0.0, 0.0).circle(0.01, False).extrude(0.01)
    
    x3 = x1
    for i in range(0, cellcnt):
        sd = bcd / 2.5
        gt = bcd / 15.0
        plw = bcd / 2.0
        x1 = x3
        pinf = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(x1, y1).rect(0.1, plw).extrude((3.0 * H) / 4.0)
        pint1 = pint1.union(pinf)
        while sd > gt:
            pinf = cq.Workplane("ZY").workplane(offset=x1).moveTo(z1, y1).circle(sd, False).extrude(tx)
            if x1 > 0.0:
                pine = cq.Workplane("ZY").workplane(offset=x1 - 0.2).moveTo(z1, y1).circle(sd - gt, False).extrude(tx + 0.2)
            else:
                pine = cq.Workplane("ZY").workplane(offset=x1 + 0.2).moveTo(z1, y1).circle(sd - gt, False).extrude(tx - 0.2)
            pinf = pinf.cut(pine)
            pint = pint.union(pinf)
            x1 = x1 - (tx * 2.0)
            sd = sd - gt
        
        x1 = x3
        if BC[1] == 'switchright' or BC[1] == 'switchleft' :
            tx = 0.0 - tx
            x3 = 0.0 - x3
        y1 = y1 - bcd
    
    if BM != None:
        x1 = BM[0]
        y1 = 0.0 - BM[1]
        pint = pint.translate((x1, y1, 0.0))
        pint1 = pint1.translate((x1, y1, 0.0))
    
    
    return pint, pint1


def make_battery_contact_BC5(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize    # Battery type
    cellcnt = params.cellcnt      # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BC = params.BC                      # Blend height
    BM = params.BM                      # Center of body
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    cellsize = params.cellsize           # Battery type
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)
    cellD, cellL = get_battery_size(params)

    bcd = cellD
    #
    # Make ends
    #
    x1 = LC[0]
    y1 = LC[1]
    od = LC[2]
    id = LC[3]
    hh = LC[4]
    dd = (od - id) / 2.0
    
    pint = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0 - ((id / 2.0) - 0.3), 0.0).rect(0.1, 3.0).extrude(H - 0.2)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.2)).moveTo(0.0 - ((id / 2.0) - 0.8), 0.0).rect(1.0, 3.0).extrude(0.1)
    pint = pint.union(pine)
    
    pint1 = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(((id / 2.0) - 0.3), 0.0).rect(0.1, 3.0).extrude(H - 0.2)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0, 0.0).rect((id / 4.0), 1.0).extrude(0.1)
    pine = pine.faces("<X").edges("<Y").fillet(0.45)
    pine = pine.faces("<X").edges(">Y").fillet(0.45)
    pine = pine.rotate((0,0,0), (0,1,0), 20.0)
    pine = pine.translate((((id / 2.0) - (0.3 + 1.5)), 1.0, 1.5))
    pint1 = pint1.union(pine)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11).moveTo(0.0, 0.0).rect((id / 4.0), 1.0).extrude(0.1)
    pine = pine.faces("<X").edges("<Y").fillet(0.45)
    pine = pine.faces("<X").edges(">Y").fillet(0.45)
    pine = pine.rotate((0,0,0), (0,1,0), 20.0)
    pine = pine.translate((((id / 2.0) - (0.3 + 1.5)), 0.0 - 1.0, 1.5))
    pint1 = pint1.union(pine)

    return pint, pint1


def make_battery_contact_BC6(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellcnt = params.cellcnt            # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BC = params.BC                      # Blend height
    BM = params.BM                      # Center of body
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    cellsize = params.cellsize          # Battery type
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = get_body_offset(params)
    cellD, cellL = get_battery_size(params)

    bcd = cellD
    #
    # Make base
    #
    ty2 = BC[1]
    pint = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.1)).moveTo(0.0, ty2).rect(L + 0.2, W).extrude(0.2)
    
#    L  = 13.21,                                 # Package width
#    W  = 12.07,                                 # Package width
#    H  = 03.18,                                 # Package height
#    LC = [07.14, 5.14],                         # [back side width, distance back end to pad]
#    A1 = 0.1,                                   # package board seperation
#    BC = ['BC6', 1.19],                         # Battery contact type, hole diameter in pad
#    pins = [('smd', -08.03, 00.00, 'rect', 02.86, 3.17), ('smd', 08.03, 00.00, 'rect', 02.86, 3.17)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    #
    # Sides
    #
    #
    # Sides
    #
    SLW = LC[0]

    if (SLW / 2.0) > ((W / 2.0) + BC[1]):
        SLW = W * 0.6

    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.2, SLW).extrude(H)
    pine = pine.translate((0.0 - (L / 2.0), 0.0, A1 + A11))
    pint = pint.union(pine)
    #
    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.2, SLW).extrude(H)
    pine = pine.translate(((L / 2.0), 0.0, A1 + A11))
    pint = pint.union(pine)
    #
    # Back
    #
    ty5 = ty2 - (W / 2.0)
    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(LC[0], 0.2).extrude(H)
    pine = pine.translate((0.0, ty5 + 0.1, A1 + A11))
    pint = pint.union(pine)
    #
    # Front end filled
    #
    ft1 = ((W / 2.0) + ty2) - (SLW / 2.0)
    pint = pint.faces(">Y").edges("<X").fillet(ft1)
    pint = pint.faces(">Y").edges(">X").fillet(ft1)
    #
    # Back end chamfer
    #
    dy3 = W - ((SLW) + ft1)
    y3 = 0.0 - (SLW / 2.0)
    pts = []
    pts.append((0.0 - ((L / 2.0) - (SLW / 2.0) + 0.2), 0.0 - dy3))
    pts.append((0.0, 0.0 - dy3))
    pine = cq.Workplane("XY").workplane(offset = 0.0).polyline(pts).close().extrude(H + 0.4)
    pine = pine.translate(((L / 2.0) + 0.2, y3 - 0.15, A1 + A11))
    pint = pint.cut(pine)
    
    y4 = 0.0 - (SLW / 2.0)
    pts = []
    pts.append((((L / 2.0) - (SLW / 2.0) + 0.2), 0.0 - dy3 - 0.4))
    pts.append((0.0, 0.0 - dy3 - 0.4))
    pine = cq.Workplane("XY").workplane(offset = 0.0).polyline(pts).close().extrude(H + 0.4)
    pine = pine.translate((0.0 - ((L / 2.0) + 0.2), y4 + 0.2, A1 + A11))
    pint = pint.cut(pine)
    
    #
    # Make the '+'
    #
    ty3 = ty5 + 2.0
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, ty3).rect(3.0, 0.5).extrude(H)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, ty3).rect(0.5, 3.0).extrude(H)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, ty3).circle(0.75, False).extrude(H)
    pint = pint.cut(pine)
    #
    # Make the two circles
    #
    ddx = 1.0
    ty3 = ty5 + LC[1]
    tx3 = L / 4.0
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(tx3, ty3).circle(1.5, False).extrude(H)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0 - tx3, ty3).circle(1.5, False).extrude(H)
    pint = pint.cut(pine)
    
    #
    # Cut front
    #
    fy1 = float(cellD) * 0.8
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, fy1).circle(float(cellD) / 2.0, False).extrude(0.8)
    pint = pint.cut(pine)
    #
    # Make the two squares connected to the circles
    #
    hx1 = tx3 - (ddx / 2.0)
    hy1 = ty3
    hd1 = 4.0
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(hx1, hy1).rect(ddx, hd1, centered=False).extrude(H)
    pint = pint.cut(pine)
    #
    hx2 = 0.0 - tx3 - (ddx / 2.0)
    hy2 = ty3
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(hx2, hy2).rect(ddx, hd1, centered=False).extrude(H)
    pint = pint.cut(pine)

    hx3 = hx1
    hy3 = hy1
    pint1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(ddx, hd1, centered=False).extrude(0.2)
    pint1 = pint1.rotate((0,0,0), (1,0,0), 20.0)
    hddy = hd1 * math.sin(math.radians(20.0))
    hddx = hd1 * math.cos(math.radians(20.0))
    pint1 = pint1.translate((hx3, hy3 + 0.3, A1 + A11 + H - hddy - 0.085))

    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(ddx, hd1, centered=False).extrude(0.2)
    pine = pine.rotate((0,0,0), (1,0,0), 20.0)
    pine = pine.translate((hx2, hy2 + 0.3, A1 + A11 + H - hddy - 0.085))
    pint1 = pint1.union(pine)

    return pint, pint1

def make_battery_contact_BC7(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellsize = params.cellsize          # Battery type
    cellcnt = params.cellcnt            # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
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

    bcd = cellD
    #
    # Make base
    #
    ty2 = BC[1]
    pint = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.1)).moveTo(0.0, ty2).rect(L + 0.2, W).extrude(0.2)
    
#    L  = 13.21,                                 # Package width
#    W  = 12.07,                                 # Package width
#    H  = 03.18,                                 # Package height
#    LC = [07.14, 5.14],                         # [back side width, distance back end to pad]
#    A1 = 0.1,                                   # package board seperation
#    BC = ['BC6', 1.19],                         # Battery contact type, hole diameter in pad
#    pins = [('smd', -08.03, 00.00, 'rect', 02.86, 3.17), ('smd', 08.03, 00.00, 'rect', 02.86, 3.17)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    
    #
    # Sides
    #
    SLW = LC[0]
    if LC[0] > (W * 0.4):
        SLW = W * 0.4
    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.2, 2.0 * SLW).extrude(H)
    pine = pine.translate((0.0 - (L / 2.0), 0.0, A1 + A11))
    pint = pint.union(pine)
    #
    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(0.2, 2.0 * SLW).extrude(H)
    pine = pine.translate(((L / 2.0), 0.0, A1 + A11))
    pint = pint.union(pine)
    #
    # Back
    #
    ty5 = ty2 - (W / 2.0)
    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(LC[0], 0.2).extrude(H)
    pine = pine.translate((0.0, ty5 + 0.1, A1 + A11))
    pint = pint.union(pine)

    #
    # Front end filled
    #
    ft1 = (W / 2.0) - SLW + BC[1]
    pint = pint.faces(">Y").edges("<X").fillet(ft1)
    pint = pint.faces(">Y").edges(">X").fillet(ft1)

    #
    # Back end chamfer
    #
    dy3 = W - ((2 * SLW) + ft1)
    y3 = 0.0 - SLW
    pts = []
    pts.append((0.0 - ((L / 2.0) - (SLW / 2.0) + 0.2), 0.0 - dy3))
    pts.append((0.0, 0.0 - dy3))
    pine = cq.Workplane("XY").workplane(offset = 0.0).polyline(pts).close().extrude(H + 0.4)
    pine = pine.translate(((L / 2.0) + 0.2, y3 - 0.15, A1 + A11))
    pint = pint.cut(pine)
    
    y4 = 0.0 - SLW
    pts = []
    pts.append((((L / 2.0) - (SLW / 2.0) + 0.2), 0.0 - dy3 - 0.4))
    pts.append((0.0, 0.0 - dy3 - 0.4))
    pine = cq.Workplane("XY").workplane(offset = 0.0).polyline(pts).close().extrude(H + 0.4)
    pine = pine.translate((0.0 - ((L / 2.0) + 0.2), y4 + 0.2, A1 + A11))
    pint = pint.cut(pine)
    
    #
    # Make the '+'
    #
    ty3 = ty5 + 3.0
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, ty3).rect(3.0, 0.5).extrude(H)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, ty3).rect(0.5, 3.0).extrude(H)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, ty3).circle(0.75, False).extrude(H)
    pint = pint.cut(pine)
    #
    # Make the two circles
    #
    ddx = 3.0
    if L < (ddx * 5.0):
        ddx = L / 5.0
    hd1 = W * 0.4
    
    ty3 = ty5 + LC[1]
    tx3 = L / 4.0
    
    #
    # Cut front
    #
    fy1 = float(cellD) * 0.8
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(0.0, fy1).circle(float(cellD) / 2.0, False).extrude(0.8)
    pint = pint.cut(pine)
    #
    # Make the two squares connected to the circles
    #
    hx1 = tx3 - (ddx / 2.0)
    hd1 = 7.0
    if hd1 > (W / 2.0):
        hd1 = W * 0.4
    hy1 = 0.0
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(hx1, hy1).rect(ddx, hd1, centered=False).extrude(H)
    pint = pint.cut(pine)
    #
    hx2 = 0.0 - tx3 - (ddx / 2.0)
    hy2 = ty3
    hy2 = 0.0
    pine = cq.Workplane("XY").workplane(offset=A1 + A11 + (H - 0.4)).moveTo(hx2, hy2).rect(ddx, hd1, centered=False).extrude(H)
    pint = pint.cut(pine)

    hx3 = hx1
    hy3 = hy1
    pint1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(ddx, hd1, centered=False).extrude(0.2)
    pint1 = pint1.rotate((0,0,0), (1,0,0), 20.0)
    hddy = hd1 * math.sin(math.radians(20.0))
    hddx = hd1 * math.cos(math.radians(20.0))
    pint1 = pint1.translate((hx3, hy3 + 0.3, A1 + A11 + H - hddy - 0.085))

    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).rect(ddx, hd1, centered=False).extrude(0.2)
    pine = pine.rotate((0,0,0), (1,0,0), 20.0)
    pine = pine.translate((hx2, hy2 + 0.3, A1 + A11 + H - hddy - 0.085))
    pint1 = pint1.union(pine)

    return pint, pint1


def make_battery_contact_BC8(params):

    manufacture = params.manufacture    # Model name
    serie = params.serie                # Model name
    cellcnt = params.cellcnt            # Number of battery
    L = params.L                        # Package width
    W = params.W                        # Package width
    H = params.H                        # Package height
    LC = params.LC                      # Large circle [x pos, y pos, outer diameter, inner diameter, height]
    BC = params.BC                      # Blend height
    BM = params.BM                      # Center of body
    A1 = params.A1                      # package board seperation
    pins = params.pins                  # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    cellsize = params.cellsize          # Battery type
    npthpins = params.npthpins          # npth holes
    socket = params.socket              # 'type', centre diameter, length, height
    spigot = params.spigot              # Spigot, distance from edge to pin 1, height
    topear = params.topear              # Top ear
    rotation = params.rotation          # Rotation if required
    modelname = params.modelname        # Model name

    A11 = 0.0
    cellD, cellL = get_battery_size(params)

    bcd = cellD
    #
    # Make base
    #
    dtx = BC[1]
    dty = BC[2]
    sl  = BC[3]
    tdx = BC[4]
    bl = LC[0]
    bldx = (L - bl) / 2.0

    x1 = 0.0
    y1 = 0.0
    pts = []
    x1 = 0.0
    y1 = sl
    pts.append((x1, y1))

    x1 = tdx
    y1 = y1 + ((W - bldx) - sl)
    pts.append((x1, y1))

    x1 = L - tdx
    pts.append((x1, y1))

    x1 = L
    y1 = sl
    pts.append((x1, y1))

    y1 = 0.0
    pts.append((x1, y1))

    x1 = x1 - bldx
    y1 = y1 - bldx
    pts.append((x1, y1))

    x1 = bldx
    pts.append((x1, y1))
    pine = cq.Workplane("XY").workplane(offset = 0.0).polyline(pts).close().extrude(0.2)
    pint = pine.translate((dtx, bldx + dty, 0.0))
    #
    # Make the '+'
    #
    ty3 = dty + 4.0
    pine = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0, ty3).rect(3.0, 0.5).extrude(0.4)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0, ty3).rect(0.5, 3.0).extrude(0.4)
    pint = pint.cut(pine)
    
    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(0.0, 0.0).circle(0.1, False).extrude(1.0)
#    pint = pint.union(pine)
    #
    # Make the two circles
    #
    tx3 = L / 4.0
    pine = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(tx3, ty3).circle(2.0, False).extrude(0.4)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0 - tx3, ty3).circle(2.0, False).extrude(0.4)
    pint = pint.cut(pine)
    #
    # Cut out for lend
    #
    pine = cq.Workplane("XY").workplane(offset = 0.0 - 0.1).moveTo(tx3, ty3 + 4.0).rect(2.5, 7.0).extrude(0.4)
    pint = pint.cut(pine)
    pine = cq.Workplane("XY").workplane(offset = 0.0 - 0.1).moveTo(0.0 - tx3, ty3 + 4.0).rect(2.5, 7.0).extrude(0.4)
    pint = pint.cut(pine)
    #
    # Add the lends going downwards
    #
    pine = cq.Workplane("XY").workplane(offset = 0.0).moveTo(tx3, ty3 + 4.0).rect(2.5, 7.0).extrude(0.2)
    pine = pine.faces("<Y").edges("<X").fillet(1.22)
    pine = pine.faces("<Y").edges(">X").fillet(1.22)
    pine = pine.rotate((0,0,0), (1,0,0), 20.0)
    pine = pine.translate((0.0, 0.32, 0.0 - 1.39))
    pint = pint.union(pine)
    pine = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - tx3, ty3 + 4.0).rect(2.5, 7.0).extrude(0.2)
    pine = pine.faces("<Y").edges("<X").fillet(1.22)
    pine = pine.faces("<Y").edges(">X").fillet(1.22)
    pine = pine.rotate((0,0,0), (1,0,0), 20.0)
    pine = pine.translate((0.0, 0.32, 0.0 - 1.39))
    pint = pint.union(pine)
    #
    # Cut out circle in the middle on front side
    #
    pine = cq.Workplane("XY").workplane(offset=0.0 - 0.1).moveTo(0.0, W).circle(10.0, False).extrude(0.4)
    pint = pint.cut(pine)
    
    #
    # round the two taps on front side
    #
    pint = pint.faces(">Y").edges("<X").fillet(1.22)
    pint = pint.faces(">Y").edges(">X").fillet(1.22)
    
    pint = pint.translate((0.0, 0.0, A1 + A11 + H))
    
    #
    # Make back end
    #
    pine = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0, dty + 0.1).rect(bl, 0.2).extrude(H)
    pine = pine.translate((0.0, 0.0, A1 + A11))
    pint = pint.union(pine)
    #
    # Make left side
    #
    pine = cq.Workplane("XY").workplane(offset = 0.0).moveTo(0.0 - (L / 2.0), (dty + bldx) + (sl / 2.0)).rect(0.2, sl).extrude(H)
    pine = pine.translate((0.1, 0.0, A1 + A11))
    pint = pint.union(pine)
    #
    # Make right side
    #
    pine = cq.Workplane("XY").workplane(offset = 0.0).moveTo((L / 2.0), (dty + bldx) + (sl / 2.0)).rect(0.2, sl).extrude(H)
    pine = pine.translate((0.0 - 0.1, 0.0, A1 + A11))
    pint = pint.union(pine)
    #
    # Make pads
    #
    pin = pins[0]
    x = pin[1]
    y = pin[2]
    w = pin[4]
    h = pin[5]
    pint1 = cq.Workplane("XY").workplane(offset=0.0).moveTo(x, y).rect(w, h).extrude(0.2)

    pin = pins[1]
    x = pin[1]
    y = pin[2]
    w = pin[4]
    h = pin[5]
    pine = cq.Workplane("XY").workplane(offset=0.0).moveTo(x, y).rect(w, h).extrude(0.2)
    pint1 = pint1.union(pine)
    pint1 = pint1.translate((0.0, 0.0, A1 + A11))

    return pint, pint1

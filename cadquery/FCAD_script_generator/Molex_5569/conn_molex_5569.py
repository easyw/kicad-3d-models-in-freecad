# Molex 5569
# Mini-Fit Jr. Header, Dual Row, Right Angle,
# with Snap-in Plastic Peg PCB Lock

import cadquery as cq
from Helpers import show

# Body
body_height = 9.6
body_width = 12.8
body_length = (5.4, 9.6, 13.8, 18.0, 22.2, 26.4, 30.6, 34.8, 39.0)
body_thickness = 0.2     # .faces("<X").shell(body_thickness)
peg_to_front = 6.6
peg_to_back = body_width - peg_to_front
standoff = 0.4

# Lock
# 4.20 for 2-pin connector, 3.40 for 6+ pins

# Peg
peg_dia = 3.00
peg_height = 2.9
peg_to_pin = 7.30

# Cavity
cavity_width = 3.8

# Pin
dia = 1.07        # pin diameter
pitch = 4.2
step = 5.5    # distance between rows
ch = 0.3
pin_length = body_width/2 + 7.30 + 3        # FIXME
pin_height = body_height + standoff + 3.6    # FIXME

bx = -dia/2 - body_width/2  # TODO


def MakeCavity():
    cavity = body.cut(cq.Workplane("XY")
                        .box(body_width, cavity_width, cavity_width)
                        .translate((bx-1, dia/2, dia/2 + pitch))
                      )
    return cavity


def MakeBody(n):
    by = dia/2 + (n-1)*pitch/2
    bz = -pitch + (body_height/2 + pitch/2)
    body = cq.Workplane("XY").box(body_width, body_length[n-1], body_height). \
        translate((bx, by, bz))

    # Lock
    ls = 3.40
    lock_h = 1.4
    ly = -dia/2 + body_height/2 - ls/2
    ly = by
    lz = body_height - pitch/2

    body = body.union(cq.Workplane("XZ")
                        .lineTo(ls, 0).lineTo(ls, lock_h).close().extrude(ls)
                        .translate((-body_width - dia/2,
                                    ly + ls/2,
                                    lz)
                                   )
                      )

    # Add peg
    # body = body.union(cq.Workplane("XY").makeCylinder(peg_dia/2, peg_height))
    px = -peg_to_pin + dia/2
    py = by
    pz = -body_height/2

    if n > 2:
        py = dia/2

    peg = cq.Workplane("XY").circle(peg_dia/2).extrude(peg_height). \
        faces("<Z").chamfer(1).translate((px, py, pz))

    # Add second peg if circuit number is greater than 4 (2 pairs)
    if n > 2:
        py = dia/2 + (n-1)*pitch
        peg = peg.union(cq.Workplane("XY").circle(peg_dia/2).
                        extrude(peg_height).faces("<Z").chamfer(1).
                        translate((px, py, pz)))

    body = body.union(peg)

    # Pin cavities
    for i in range(1, n+1):
        offset = dia/2 + pitch*(i-1)
        body = body.cut(cq.Workplane("XY")
                        .box(body_width, cavity_width, cavity_width)
                        .translate((bx-1, offset, dia/2 + pitch))
                        )
        body = body.cut(cq.Workplane("XY")
                        .box(body_width, cavity_width, cavity_width)
                        .translate((bx-1, offset, dia/2))
                        )

    return body


def MakePin(k):

    h = -pin_height + pitch*k
    l = -pin_length + step*k

    # Begin pin
    pin = cq.Workplane("XY").rect(dia, dia, False) \
            .extrude(h) \
            .faces("<Z").chamfer(ch)

    # Bending
    pin = pin.union(cq.Workplane("XY").rect(dia, dia, False).revolve(90))

    # End pin
    pin = pin.union(cq.Workplane("YZ").rect(dia, dia, False)
                    .extrude(l)
                    .faces("<X").chamfer(ch))
    return pin


def MakePinPair():
    pin = MakePin(1)
    # Make a copy of pin for second row
    pair = pin.union(MakePin(0).translate((step, 0, pitch)))
    return pair


def MakePinPairs(n):
    result = MakePinPair()

    for i in range(1, n):
        result = result.union(MakePinPair().translate((0, i*pitch, 0)))
    return result

pairs = 3

result = MakePinPairs(pairs)
show(result)

body = MakeBody(pairs)
show(body)

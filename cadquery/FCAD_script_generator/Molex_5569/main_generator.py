# Molex 5569
# Mini-Fit Jr. Header, Dual Row, Right Angle,
# with Snap-in Plastic Peg PCB Lock

import FreeCAD as App
import FreeCADGui as Gui

import sys, os
from sys import argv
sys.path.append("../_tools")

scriptdir = os.path.dirname (os.path.realpath(__file__))
sys.path.append(scriptdir)

import cadquery as cq
from Helpers import show

# import cq_parameters
from cq_parameters import all_params_molex_5569


# Body TODO move to cq_parameters
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
cavity_pattern = (0, 1, 1, 0)
cavity_index = 0

# Pin
dia = 1.07        # pin diameter
pitch = 4.2
step = 5.5    # distance between rows
ch = 0.3
pin_length = body_width/2 + 7.30 + 3        # FIXME
pin_height = body_height + standoff + 3.6    # FIXME

bx = -dia/2 - body_width/2  # TODO


def NextCavity():
    global cavity_index
    cavity_index = cavity_index + 1
    if cavity_index > 3:
        cavity_index = 0
    return cavity_index


def MakeBody(n):
    by = dia/2 + (n-1)*pitch/2
    bz = -pitch + (body_height/2 + pitch/2)
    body = cq.Workplane("XY").box(body_width, body_length[n-1], body_height) \
        .translate((bx, by, bz))

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

    global cavity_index
    cavity_index = 0
    # Pin cavities
    for i in range(1, n+1):
        offset = dia/2 + pitch*(i-1)
        cavity = cq.Workplane("XY").box(body_width,
                                        cavity_width, cavity_width)
        if cavity_pattern[cavity_index] < 1:
            cavity = cavity.edges("|X").edges("<Z").chamfer(cavity_width/4)

        cavity = cavity.translate((bx-1, offset, dia/2 + pitch))

        body = body.cut(cavity)

        # Bottom row
        cavity = cq.Workplane("XY").box(body_width,
                                        cavity_width, cavity_width)
        if cavity_pattern[cavity_index] > 0:
            cavity = cavity.edges("|X").edges("<Z").chamfer(cavity_width/4)

        cavity = cavity.translate((bx-1, offset, dia/2))

        body = body.cut(cavity)

        NextCavity()

    # Side rib
    body = body.union(cq.Workplane("ZY").circle(0.4).extrude(body_width)
                        .translate((bx + body_width/2,
                                    by - (body_length[n-1])/2,
                                    bz - body_height/2 + 2.5))
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


def MakePart(params):
    pins = MakePinPairs(params.N/2)
    body = MakeBody(params.N/2)
    return pins, body

variants = all_params_molex_5569.keys()

for variant in variants:
    ModelName = all_params_molex_5569[variant].modelName
    CheckedModelName = ModelName.replace('.', '') \
        .replace('-', '_').replace('(', '').replace(')', '')
    Newdoc = App.newDocument(CheckedModelName)
    App.setActiveDocument(CheckedModelName)
    Gui.ActiveDocument = Gui.getDocument(CheckedModelName)
    pins, body = MakePart(all_params_molex_5569[variant])

    show(pins)
    show(body)

# pairs = 3

# result = MakePinPairs(pairs)
# show(result)

# body = MakeBody(pairs)
# show(body)

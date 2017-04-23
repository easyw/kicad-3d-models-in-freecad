import cadquery as cq
from Helpers import show
from ribbon import Ribbon


LENGTH = 13.85  # Y axis

BODY_LENGTH = 9.25  # Y axis
BODY_WIDTH = 10.0  # X axis
BODY_HEIGHT = 4.4
BODY_WAIST = 2.4  # Z axis distance from PCB to bottom of chamfers

TAB_HEIGHT = 1.27  # Z axis thickness of tab

CHAMFER_1 = 0.5  # horizontal part of top side chamfers
CHAMFER_2 = BODY_HEIGHT - BODY_WAIST  # vertical part of top side chamfers
CHAMFER_3 = 0.2  # horizontal part of bottom front chamfer

TAB_LENGTH = 7.55
TAB_PROJECT = 1.0  # Y axis distance from end of tab to end of body
TAB_TOP_WIDTH = 10.0  # width of part of tab that is outside body
TAB_BOTTOM_WIDTH = 8.5  # width of part of tab that is underneath body
TAB_SMALL = 0.5  # approximation used for tab chamfers and shoulders
TAB_LARGE = 1.5  # approximation used for tab chamfers and shoulders

# Y axis offset of body centre so that whole device is centred on (0, 0)
BODY_OFFSET = (LENGTH / 2.0) - (BODY_LENGTH / 2.0) - TAB_PROJECT

NUM_PINS = 7
PIN_PITCH = 1.27
PIN_WIDTH = 0.6
PIN_THICKNESS = 0.5
PIN_OFFSET = LENGTH / 2.0  # Y axis offset of end of pin
PIN_RADIUS = 0.5
PIN_FAT_WIDTH = PIN_WIDTH + 0.24  # Extra width of wide part on pins
PIN_FAT_LENGTH = 0.75  # Length of wide part on pins
PIN_FAT_CUT = 4.6  # Used to produce wide part of pins

PIN_PROFILE = [
    ('start', {'position': (-PIN_OFFSET, PIN_THICKNESS/2.0),
               'direction': 0.0, 'width': PIN_THICKNESS}),
    ('line', {'length': 2.1 - PIN_RADIUS - PIN_THICKNESS/2.0}),
    ('arc', {'radius': PIN_RADIUS, 'angle': 90.0}),
    ('line', {'length': 0.5}),
    ('arc', {'radius': PIN_RADIUS, 'angle': -90}),
    ('line', {'length': 3})
]

HOLE_DIAMETER = 2.5
HOLE_DEPTH = 0.1

NUDGE = 0.02


body = cq.Workplane("XY").workplane(offset=NUDGE).moveTo(0, BODY_OFFSET)\
    .rect(BODY_WIDTH, BODY_LENGTH).extrude(BODY_HEIGHT)

body = body\
    .faces(">Z").edges(">Y").chamfer(BODY_HEIGHT - TAB_HEIGHT, CHAMFER_1)\
    .faces(">Z").edges("<Y").chamfer(CHAMFER_1, CHAMFER_2)\
    .faces(">Z").edges("<X").chamfer(CHAMFER_1, CHAMFER_2)\
    .faces(">Z").edges(">X").chamfer(CHAMFER_1, CHAMFER_2)\
    .faces("<Z").edges("<Y").chamfer(BODY_WAIST - NUDGE, CHAMFER_3)

body = body.faces(">Z").hole(HOLE_DIAMETER, depth=HOLE_DEPTH)

tab = cq.Workplane("XY")\
    .moveTo(0, BODY_OFFSET + BODY_LENGTH / 2.0 + TAB_PROJECT)\
    .line((TAB_TOP_WIDTH/2.0) - TAB_LARGE, 0)\
    .line(TAB_LARGE, -TAB_SMALL)\
    .line(0, -(TAB_PROJECT - TAB_SMALL))\
    .line(-(TAB_TOP_WIDTH - TAB_BOTTOM_WIDTH)/2.0, 0)\
    .line(0, -(TAB_LENGTH - TAB_PROJECT))\
    .line(-TAB_BOTTOM_WIDTH, 0)\
    .line(0, TAB_LENGTH - TAB_PROJECT)\
    .line(-(TAB_TOP_WIDTH - TAB_BOTTOM_WIDTH)/2.0, 0)\
    .line(0, TAB_PROJECT - TAB_SMALL)\
    .line(TAB_LARGE, TAB_SMALL)\
    .close().extrude(TAB_HEIGHT)

pin = cq.Workplane("YZ")\
    .workplane(offset=-PIN_WIDTH/2.0 - (NUM_PINS - 1) * PIN_PITCH/2.0)
pin = Ribbon(pin, PIN_PROFILE).drawRibbon().extrude(PIN_WIDTH)
pins = pin
for i in range(0, NUM_PINS):
    pins = pins.union(pin.translate((i * PIN_PITCH, 0, 0)))

fat_pin = cq.Workplane("YZ")\
    .workplane(offset=-(PIN_FAT_WIDTH)/2.0 - (NUM_PINS - 1) * PIN_PITCH/2.0)
fat_pin = Ribbon(fat_pin, PIN_PROFILE).drawRibbon().extrude(PIN_FAT_WIDTH)
fat_pins = fat_pin
for i in range(0, NUM_PINS):
    fat_pins = fat_pins.union(fat_pin.translate((i * PIN_PITCH, 0, 0)))

cutter = cq.Workplane("XY").moveTo(0, -PIN_OFFSET)\
    .rect(BODY_WIDTH, PIN_FAT_CUT).extrude(BODY_HEIGHT)
fat_pins = fat_pins.cut(cutter)

cutter = cq.Workplane("XY")\
    .moveTo(0, -PIN_OFFSET + PIN_FAT_CUT + PIN_FAT_LENGTH)\
    .rect(BODY_WIDTH, PIN_FAT_CUT).extrude(BODY_HEIGHT)
fat_pins = fat_pins.cut(cutter)

pins = pins.union(fat_pins)

show(body)
show(tab)
show(pins)

#
# 2018 Joel Holdsworth <joel@airwebreathe.org.uk>
#
# CadQuery Model Generator for the Molex 502250 series FFC/FPC connectors
#

import cadquery as cq

pin_count = 51

pin_row_spacing = 2.875
pitch = 0.3
body_width = 3.53
body_length = 1.8 + pin_count * pitch
body_height = 0.88
body_y_offset = 0.28 + pin_row_spacing/2
slot_length = body_length - 0.6*2
bar_length = body_length - 1.58
body_cut_width = body_width-1.99

#
# Pins
#

odd_pins = [
  cq.Workplane("XY")
    .moveTo(i * pitch - pitch * (pin_count - 1)/2, -pin_row_spacing/2)
    .box(0.12, 0.56, 0.21, centered=(True, True, False))
  for i in range(0, pin_count, 2)]
even_pins = [
  cq.Workplane("XY")
    .moveTo(i * pitch - pitch * (pin_count - 1)/2, pin_row_spacing/2)
    .box(0.15, 0.40, 0.30, centered=(True, True, False))
  for i in range(1, pin_count-1, 2)]
anchor_pins = [
  cq.Workplane("XY")
    .moveTo(d * ((pin_count-1) * pitch / 2 + 0.7),
            -pin_row_spacing/2 + 0.325)
    .box(0.12, 0.55, 0.3, centered=(True, True, False))
  for d in [-1, 1]]

pins = anchor_pins[0]
for p in [anchor_pins[1]] + odd_pins + even_pins:
  pins = pins.union(p)
pins = pins.rotate((0, 0, 0), (1, 0, 0), -90).translate((0, -0.46, 0.0475))
show_object(pins, options={'rgba': (211, 210, 200, 0)})

#
# Body
#

body_outline = cq.Workplane("XY").polyline([
    (0, 0.1),
    (body_length/2-0.745, 0.1),
    (body_length/2-0.745, 0),
    (body_length/2, 0),
    (body_length/2, 0.45),
    (body_length/2-0.28, 0.45),
    (body_length/2-0.28, 0.815),
    (body_length/2, 0.815),
    (body_length/2, 3.53),
    (body_length/2-0.30, 3.53),
    (body_length/2-0.30, 3.28),
    (0, 3.28)
]).mirrorY()

body = body_outline.extrude(body_height) \
  .cut(cq.Workplane("XY", origin=(0, 0, body_height))
    .moveTo(-slot_length/2, body_width-body_cut_width)
    .rect(slot_length, body_cut_width, centered=False)
    .extrude(0.26-body_height)
  ).cut(cq.Workplane("XZ")
    .moveTo(-slot_length/2, 0.26)
    .rect(slot_length, 0.28, centered=False)
    .extrude(-body_width)
  ).translate((0, -body_y_offset, 0.02)).rotate((0, 0, 0), (1, 0, 0), -90) \
  .translate((0, -0.46, 0.0475))
show_object(body, options={'rgba': (229, 226, 201, 0)})

#
# Latch Bar
#

bar = cq.Workplane("YZ").polyline([
    (1.41, 0.89), (0, 0.89), (0, 0.4), (1.4-0.65, 0.4),
    (0.75, 0.15), (1.01, 0.15), (1.41, 0.585), (1.41, 0.89)]) \
  .close() \
  .extrude(bar_length) \
  .translate((-bar_length/2, body_width - body_y_offset - 0.75, 0)) \
  .rotate((0, 0, 0), (1, 0, 0), -90).translate((0, -0.46, 0.0475))
show_object(bar, options={'rgba': (38, 37, 37, 0)})

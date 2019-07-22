# Generated with CadQuery2
# Coloring and checks done in kicad steup
# No offsets

import cadquery as cq

dims = {
    "body": {
        "width": 8.94,
        "depth": 7.32,
        "height": 3.25,
        "radius": 1.25,
        "wall_thickness": 0.345,
        "cavity_depth": 4.8,
        "offset": (0, -1.17, 0)
    },
    "tounge": {
        "width": 6.69,
        "height": 0.7,
        "depth": 4.45,
        "tip_chamfer": 0.5
    },
    "pegs": {
        "diameter": 0.5,
        "length": 0.76,
        "tip_chamfer": 0.1,
        "centers": [
            (5.78/2, -2.63),
            (-5.78/2, -2.63)
        ]
    },
    "pins": {
        "width": 0.2,
        "length": 7.63 - 7.32,
        "height": 0.15,
        "centers": [
            (-6.7/2, 0),
            (-6.1/2, 0),
            (-5.1/2, 0),
            (-4.5/2, 0)
        ]
    },
    "shield": {
        "thickness": 0.3,
        "length": 1,
        "width": (0.8, 1.1),  # (front, back)
        "centers_front": [
            (-8.64/2, 1.06),
            (8.64/2, 1.06)
        ],
        "centers_back": [
            (8.64/2, -3.11),
            (-8.64/2, -3.11)
        ]
    }

}

x = -3.5/2
while x < 0:
    dims["pins"]["centers"].append((x, 0))
    x = dims["pins"]["centers"][-1][0] + 0.5

for i in range(8):
    dims["pins"]["centers"].append((dims["pins"]["centers"][i][0] * -1, 0))


body = cq.Workplane("XZ")\
    .box(
         dims["body"]["width"],
         dims["body"]["height"],
         dims["body"]["depth"],
         centered=(True, False, True))\
    .edges("|Y").fillet(dims["body"]["radius"])\
    .faces("<Y").shell(-dims["body"]["wall_thickness"])\
    .translate(dims["body"]["offset"])

body_back = body.faces("<Y[-2]").workplane()\
    .box(
         dims["body"]["width"],
         dims["body"]["height"],
         dims["body"]["depth"] - dims["body"]["cavity_depth"] - dims["body"]["wall_thickness"],
         centered=(True, True, False),
         combine=False)\
    .edges("|Y").fillet(dims["body"]["radius"])

body = body.union(body_back)
shield_pins_front = body.faces("<Z")\
    .workplane(offset=- dims["body"]["height"]/2)\
    .pushPoints(dims["shield"]["centers_front"])\
    .box(
        dims["shield"]["thickness"],
        dims["shield"]["width"][0],
        dims["shield"]["length"] + dims["body"]["height"]/2,
        centered=(True, True, False),
        combine=True)\

body = body.union(shield_pins_front)\
    .edges("|X and <Z").fillet(dims["shield"]["width"][0]/2 - 0.01)


shield_pins_back = body.faces("<Z[-2]")\
    .workplane(offset=- dims["body"]["height"]/2)\
    .pushPoints(dims["shield"]["centers_back"])\
    .box(
        dims["shield"]["thickness"],
        dims["shield"]["width"][1],
        dims["shield"]["length"] + dims["body"]["height"]/2,
        centered=(True, True, False),
        combine=True)\

body = body.union(shield_pins_back)\
    .edges("|X and <Z").fillet(dims["shield"]["width"][1]/2 - 0.01)

del shield_pins_back
del shield_pins_front
del body_back

tounge = body.faces(">Y[-3]")\
    .box(
        dims["tounge"]["width"],
        dims["tounge"]["height"],
        dims["tounge"]["depth"],
        centered=(True, True, False),
        combine=False)\
    .edges("|Z and <Y").chamfer(dims["tounge"]["tip_chamfer"])

pegs = body.faces("<Z[-3]").workplane().pushPoints(dims["pegs"]["centers"])\
    .circle(dims["pegs"]["diameter"]/2)\
    .extrude(dims["pegs"]["length"], combine=False)\
    .edges("<Z").chamfer(dims["pegs"]["tip_chamfer"])

pins = cq.Workplane("XZ")\
    .workplane(offset=-dims["body"]["depth"]/2 - dims["body"]["offset"][1] - dims["pins"]["length"])\
    .pushPoints(dims["pins"]["centers"])\
    .box(
        dims["pins"]["width"],
        dims["pins"]["height"],
        dims["pins"]["length"],
        centered=(True, False, False),
        combine=True)\

# If CQ1.2, use older show_object syntax
if cq.__version__ == "1.2.0":
    show_object(body, options={"rgba": (200, 200, 200, 0)})
    show_object(tounge, options={"rgba": (103, 103, 103, 0)})
    show_object(pegs, options={"rgba": (103, 103, 103, 0)})
    show_object(pins, options={"rgba": (217, 189, 45, 0)})
    
# >= 2.0 called from command line, export step
elif '__file__' in globals():
    with open("{}.step".format(splitext(basename(__file__))[0]), "w+") as f:
        cq.exporters.exportShape(combined, cq.exporters.ExportTypes.STEP, f)
        
# run in CQ-GUI
else:
    show_object(body, name="body", options = {"color" : "#c8c8c8"})
    show_object(tounge, name="tounge", options = {"color" : "#676767"})
    show_object(pegs, name="pegs", options = {"color" : "#676767"})
    show_object(pins, name="pins", options = {"color" : "#d9bd2d"})

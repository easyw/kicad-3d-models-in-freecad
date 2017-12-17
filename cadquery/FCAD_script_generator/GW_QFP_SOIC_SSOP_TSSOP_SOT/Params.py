from collections import namedtuple

Params = namedtuple("Params", [
    'the',  # body angle in degrees
    'tb_s', # top part of body is that much smaller
    'c',    # pin thickness, body center part height
    'R1',   # pin upper corner, inner radius
    'R2',   # pin lower corner, inner radius
    'S',    # pin top flat part length (excluding corner arc)
# automatic calculated    'L',    # pin bottom flat part length (including corner arc)
    'fp_s',  # True for circular pinmark, False for square pinmark (useful for diodes)
    'fp_r', # first pin indicator radius, set to 0.0 to remove first pin indicator
    'fp_d', # first pin indicator distance from edge
    'fp_z', # first pin indicator depth
    'ef',   # fillet of edges
    'cc1',  # chamfer of the 1st pin corner

    'D1',   # body lenght
    'E1',   # body width
    'E',    # body overall width
    'A1',   # body-board separation
    'A2',   # body height

    'b',    # pin width
    'e',    # pin (center-to-center) distance

    'npx',  # number of pins along X axis (width)
    'npy',  # number of pins along y axis (length)
    'epad',  # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    'excluded_pins', #pins to exclude
    'old_modelName', #modelName
    'modelName', #modelName
    'rotation' #rotation if required
])

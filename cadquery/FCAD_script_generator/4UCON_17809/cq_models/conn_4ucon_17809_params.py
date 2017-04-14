from collections import namedtuple
from conn_4ucon_global_params import generate_footprint_name


Params = namedtuple("Params",[
    'series_name',
    'file_name',
    'num_pins',
    'pin_pitch',
    'pin_y_pitch'
])


def generate_params(num_pins, series_name, pin_pitch, pin_y_pitch):

    return Params(
        series_name=series_name,
        file_name=generate_footprint_name(series_name, num_pins, pin_pitch),
        num_pins=num_pins,
        pin_pitch=pin_pitch,
        pin_y_pitch=pin_y_pitch
    )


all_params = {								
    'ucon_17809_02x02_1.27mm' : generate_params( 4, "17809", 1.27, 2.54),
    'ucon_17809_02x20_1.27mm' : generate_params(40, "17809", 1.27, 2.54),
    'ucon_17809_02x40_1.27mm' : generate_params(80, "17809", 1.27, 2.54)
}


class seriesParams():

# UPDATED

    pin_width = 0.5
    pin_chamfer_long = 0.1
    pin_chamfer_short = 0.1
    pin_height = 5
    pin_inside_distance = 3.685				# (DIMENSION C-DIMENSION A)/2 distance between centre of end pin and end of body

    body_width = 8.88
    body_height = 14.0					# Excluding feet
    body_fillet_radius = 0.5

    foot_height = 1.5
    foot_width = 1.7
    foot_length = 7.62
    foot_inside_distance = 0.5 				# Distance between outside edge of foot and end of body

    marker_x_inside = pin_inside_distance - 1
    marker_y_inside = 1.2
    marker_size = 1.0
    marker_depth = 0.5

    slot_outside_pin = 1.27
    slot_width = 1.9
    slot_chamfer = 0.5

    hole_width = 0.8
    hole_length = 1.46
    hole_offset = 2.52


# OLD

    pin_depth = 3.56					# DIMENSION F depth below bottom surface of base

    body_channel_depth = 0.6
    body_channel_width = 1.5
    body_cutout_length = 1.2
    body_cutout_width = 0.6

    ramp_split_breakpoint = 6				# Above this number of pins, the tab is split into two parts
    ramp_chamfer_x = 0.3
    ramp_chamfer_y = 0.7


calcDim = namedtuple( 'calcDim', ['length', 'slot_length', 'ramp_height', 'ramp_width', 'ramp_offset'])


def dimensions(params):
    length = ((params.num_pins / 2) - 1) * params.pin_pitch + 2 * seriesParams.pin_inside_distance
    slot_length = ((params.num_pins / 2) - 1) * params.pin_pitch + 2 * seriesParams.slot_outside_pin
    ramp_height = 11.7 - seriesParams.body_height
    if params.num_pins > seriesParams.ramp_split_breakpoint:
        ramp_width = params.pin_pitch * 2
        ramp_offset = params.pin_pitch * (params.num_pins -5) / 2
    else:
        ramp_width = (params.num_pins - 1) * params.pin_pitch / 2
        ramp_offset = 0
    return calcDim(length = length, slot_length=slot_length, ramp_height = ramp_height, ramp_width = ramp_width, ramp_offset = ramp_offset)



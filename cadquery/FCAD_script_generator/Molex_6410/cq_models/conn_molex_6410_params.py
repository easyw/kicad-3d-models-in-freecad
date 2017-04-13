from collections import namedtuple
from conn_molex_global_params import generate_footprint_name


Params = namedtuple("Params",[
    'series_name',
    'file_name',
    'num_pins',
    'pin_pitch'
])


def generate_params(num_pins, series_name, pin_pitch):

    return Params(
        series_name=series_name,
        file_name=generate_footprint_name(series_name, num_pins, pin_pitch),
        num_pins=num_pins,
        pin_pitch=pin_pitch
    )


all_params = {								# Molex part number
    'KK_6410_01x02_2.54mm' : generate_params( 2, "KK-6410", 2.54),	# 22-27-2021
    'KK_6410_01x03_2.54mm' : generate_params( 3, "KK-6410", 2.54),	# 22-27-2031
    'KK_6410_01x04_2.54mm' : generate_params( 4, "KK-6410", 2.54),	# 22-27-2041
    'KK_6410_01x05_2.54mm' : generate_params( 5, "KK-6410", 2.54),	# 22-27-2051
    'KK_6410_01x06_2.54mm' : generate_params( 6, "KK-6410", 2.54),	# 22-27-2061
    'KK_6410_01x07_2.54mm' : generate_params( 7, "KK-6410", 2.54),	# 22-27-2071
    'KK_6410_01x08_2.54mm' : generate_params( 8, "KK-6410", 2.54),	# 22-27-2081
    'KK_6410_01x09_2.54mm' : generate_params( 9, "KK-6410", 2.54),	# 22-27-2091
    'KK_6410_01x10_2.54mm' : generate_params(10, "KK-6410", 2.54),	# 22-27-2101
    'KK_6410_01x11_2.54mm' : generate_params(11, "KK-6410", 2.54),	# 22-27-2111
    'KK_6410_01x12_2.54mm' : generate_params(12, "KK-6410", 2.54),	# 22-27-2121
    'KK_6410_01x13_2.54mm' : generate_params(13, "KK-6410", 2.54),	# 22-27-2131
    'KK_6410_01x14_2.54mm' : generate_params(14, "KK-6410", 2.54),	# 22-27-2141
    'KK_6410_01x15_2.54mm' : generate_params(15, "KK-6410", 2.54),	# 22-27-2151
    'KK_6410_01x16_2.54mm' : generate_params(16, "KK-6410", 2.54)	# 22-27-2161
}


class seriesParams():

    pin_width = 0.64
    pin_chamfer_long = 0.25
    pin_chamfer_short = 0.25
    pin_height = 14.22				# DIMENSION C
    pin_depth = 3.56				# DIMENSION F depth below bottom surface of base
    pin_inside_distance = 1.27			# Distance between centre of end pin and end of body

    body_width = 5.8
    body_height = 3.17
    body_channel_depth = 0.6
    body_channel_width = 1.5
    body_cutout_length = 1.2
    body_cutout_width = 0.6

    ramp_split_breakpoint = 6			# Above this number of pins, the tab is split into two parts
    ramp_chamfer_x = 0.3
    ramp_chamfer_y = 0.7


calcDim = namedtuple( 'calcDim', ['length', 'ramp_height', 'ramp_width', 'ramp_offset'])


def dimensions(params):
    length = (params.num_pins-1) * params.pin_pitch + 2 * seriesParams.pin_inside_distance
    ramp_height = 11.7 - seriesParams.body_height
    if params.num_pins > seriesParams.ramp_split_breakpoint:
        ramp_width = params.pin_pitch * 2
        ramp_offset = params.pin_pitch * (params.num_pins -5) / 2
    else:
        ramp_width = (params.num_pins - 1) * params.pin_pitch / 2
        ramp_offset = 0
    return calcDim(length = length, ramp_height = ramp_height, ramp_width = ramp_width, ramp_offset = ramp_offset)



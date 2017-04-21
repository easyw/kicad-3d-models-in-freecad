from collections import namedtuple
from conn_molex_global_params import generate_footprint_name


Params = namedtuple("Params",[
    'series_name',
    'part_name',
    'file_name',
    'num_pins',
    'pin_pitch'
])


def generate_params(num_pins, series_name, part_name, pin_pitch):

    return Params(
        series_name=series_name,
        part_name=part_name,
        file_name=generate_footprint_name(series_name, part_name, num_pins, pin_pitch),
        num_pins=num_pins,
        pin_pitch=pin_pitch
    )


all_params = {
    'molex_55560_2x08' : generate_params(16, '55560', '0161', 0.5),								
    'molex_54722_02x10_0.5mm' : generate_params(20, '54722', '0204', 0.5),								
    'molex_54722_02x11_0.5mm' : generate_params(22, '54722', '0224', 0.5),								
    'molex_54722_02x12_0.5mm' : generate_params(24, '54722', '0244', 0.5),								
    'molex_54722_02x15_0.5mm' : generate_params(30, '54722', '0304', 0.5),								
    'molex_54722_02x17_0.5mm' : generate_params(34, '54722', '0344', 0.5),								
    'molex_54722_02x20_0.5mm' : generate_params(40, '54722', '0404', 0.5),								
    'molex_54722_02x25_0.5mm' : generate_params(50, '54722', '0504', 0.5),								
    'molex_54722_02x30_0.5mm' : generate_params(60, '54722', '0604', 0.5),								
    'molex_54722_02x40_0.5mm' : generate_params(80, '54722', '0804', 0.5)								
}


class seriesParams():

    pin_inside_distance = 0.45 + 0.525				# Distance between centre of end pin and end of body
    pocket_inside_distance = 0.45			 	# Distance between end of pocket and end of body
    # island_inside_distance = (10.1 - 8.0) / 2.0         	# Distance between end of island and end of body

    body_width = 2.83
    body_height = 1.15				
    body_fillet_radius = 0.15
    body_chamfer = 0.1
    pin_housing_height = 0.4

    pocket_width = 1.65
    pocket_base_thickness = 0.2
    pocket_fillet_radius = 0.15

    # island_width = 1.65

    # hole_width = 0.3
    # hole_length = 0.3
    # hole_offset = (body_width + pocket_width) / 4.0

    # rib_width = 0.25
    # rib_depth = 2.0 * body_chamfer

    # slot_height = body_height - 0.05
    # slot_depth = 0.3

    # notch_width = 1.2
    # notch_depth = 0.1
    
    pin_width = 0.15
    pin_thickness = 0.075
    contact_width = 0.2

    contact_thickness = 0.15
    contact_slot_width = 0.3
    top_slot_offset = (body_width + pocket_width) / 4.0
    

    # housing_breakpoint = 29					# Above this number of pins, the body has housings on the side
    # housing_width = 2.0
    # housing_height = 0.575
    # housing_depth = 0.05
    # housing_pitch = 2.5


calcDim = namedtuple( 'calcDim', ['pin_group_width', 'length', 'pocket_length'])


def dimensions(params):
    pin_group_width = ((params.num_pins / 2) - 1) * params.pin_pitch
    length =  pin_group_width + 2 * seriesParams.pin_inside_distance
    pocket_length = length - 2.0 * seriesParams.pocket_inside_distance
    # island_length = length - 2.0 * seriesParams.island_inside_distance
    # rib_group_outer_width = pin_group_width + params.pin_pitch + seriesParams.rib_width
    # slot_width = params.pin_pitch - seriesParams.rib_width
    # if params.num_pins > seriesParams.housing_breakpoint:
        # num_housings = params.num_pins // 10
        # housing_offset = (params.num_pins % 10) * params.pin_pitch / 4.0
    # else:
        # num_housings = housing_offset = 0
    return calcDim(pin_group_width=pin_group_width, length = length, pocket_length=pocket_length)



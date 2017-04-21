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
    'molex_54722_2x08' : generate_params(16, '54722', '0164', 0.5),								
    'molex_54722_2x10' : generate_params(20, '54722', '0204', 0.5),								
    'molex_54722_2x11' : generate_params(22, '54722', '0224', 0.5),								
    'molex_54722_2x12' : generate_params(24, '54722', '0244', 0.5),								
    'molex_54722_2x15' : generate_params(30, '54722', '0304', 0.5),								
    'molex_54722_2x17' : generate_params(34, '54722', '0344', 0.5),								
    'molex_54722_2x20' : generate_params(40, '54722', '0404', 0.5),								
    'molex_54722_2x25' : generate_params(50, '54722', '0504', 0.5),								
    'molex_54722_2x30' : generate_params(60, '54722', '0604', 0.5),								
    'molex_54722_2x40' : generate_params(80, '54722', '0804', 0.5)								
}


class seriesParams():

    pin_inside_distance = 1.05 + 0.5				# Distance between centre of end pin and end of body
    pocket_inside_distance = (10.1 - (8.95 + 0.5)) / 2.0 	# Distance between end of pocket and end of body
    island_inside_distance = (10.1 - 8.0) / 2.0         	# Distance between end of island and end of body

    body_width = 5.0
    body_height = 1.15				
    body_fillet_radius = 0.15
    body_chamfer = 0.1
    pin_recess_height = 0.4

    pocket_width = 2.8
    pocket_base_thickness = 0.2
    pocket_fillet_radius = 0.05

    island_width = 1.65

    hole_width = 0.3
    hole_length = 0.3
    hole_offset = (body_width + pocket_width) / 4.0

    rib_width = 0.25
    rib_depth = 2.0 * body_chamfer

    slot_height = body_height - 0.05
    slot_depth = 0.3

    notch_width = 1.2
    notch_depth = 0.1
    
    pin_width = 0.15
    pin_thickness = 0.075
    pin_minimum_radius = 0.005 + pin_thickness / 2.0
    pin_y_offset = 0.5

    recess_breakpoint = 29					# Above this number of pins, the body has housings on the side
    recess_width = 2.0
    recess_height = 0.575
    recess_depth = 0.05
    recess_pitch = 2.5


calcDim = namedtuple( 'calcDim', ['pin_group_width', 'length', 'pocket_length', 'island_length', 'rib_group_outer_width', 'slot_width', 'num_recesses', 'recess_offset'])


def dimensions(params):
    pin_group_width = ((params.num_pins / 2) - 1) * params.pin_pitch
    length =  pin_group_width + 2 * seriesParams.pin_inside_distance
    pocket_length = length - 2.0 * seriesParams.pocket_inside_distance
    island_length = length - 2.0 * seriesParams.island_inside_distance
    rib_group_outer_width = pin_group_width + params.pin_pitch + seriesParams.rib_width
    slot_width = params.pin_pitch - seriesParams.rib_width
    if params.num_pins > seriesParams.recess_breakpoint:
        num_recesses = params.num_pins // 10
        recess_offset = (params.num_pins % 10) * params.pin_pitch / 4.0
    else:
        num_recesses = recess_offset = 0
    return calcDim(pin_group_width=pin_group_width, length = length, pocket_length=pocket_length,
                   island_length = island_length, rib_group_outer_width=rib_group_outer_width,
                   slot_width=slot_width, num_recesses=num_recesses, recess_offset=recess_offset)



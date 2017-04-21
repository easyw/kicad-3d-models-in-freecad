from collections import namedtuple
from conn_molex_global_params import generate_footprint_name


Params = namedtuple("Params",[
    'series_name',
    'part_name',
    'file_name',
    'num_pins',
    'pin_pitch',
    'lock_positions'
])


def generate_params(num_pins, series_name, part_name, pin_pitch, lock_positions):

    return Params(
        series_name=series_name,
        part_name=part_name,
        file_name=generate_footprint_name(series_name, part_name, num_pins, pin_pitch),
        num_pins=num_pins,
        pin_pitch=pin_pitch,
        lock_positions=lock_positions
    )


all_params = {
    'molex_55560_2x08' : generate_params(16, '55560', '0161', 0.5, ['all']),
    'molex_55560_2x10' : generate_params(20, '55560', '0201', 0.5, ['all']),
    'molex_55560_2x11' : generate_params(22, '55560', '0221', 0.5, ['all']),
    'molex_55560_2x12' : generate_params(24, '55560', '0241', 0.5, ['all']),
    'molex_55560_2x15' : generate_params(30, '55560', '0301', 0.5, ['all']),
    'molex_55560_2x17' : generate_params(34, '55560', '0341', 0.5, [2,3,4,5,7,8,9,10,11,13,14,15,16]),								
    'molex_55560_2x20' : generate_params(40, '55560', '0401', 0.5, [2,3,5,6,8,9,12,13,15,16,18,19]),								
    'molex_55560_2x23' : generate_params(46, '55560', '0461', 0.5, [2,4,8,10,14,16,20,22]),
    'molex_55560_2x25' : generate_params(60, '55560', '0501', 0.5, [2,4,8,10,16,18,22,24]),
    'molex_55560_2x30' : generate_params(60, '55560', '0601', 0.5, [10,21]),
    'molex_55560_2x40' : generate_params(80, '55560', '0801', 0.5, ['none'])
}


class seriesParams():

    pin_inside_distance = 0.45 + 0.525				# Distance between centre of end pin and end of body
    pocket_inside_distance = 0.45			 	# Distance between end of pocket and end of body

    body_width = 2.83
    body_height = 1.15				
    body_fillet_radius = 0.15
    body_chamfer = 0.1
    pin_housing_height = 0.4

    pocket_width = 1.65
    pocket_base_thickness = 0.2
    pocket_fillet_radius = 0.15

    pin_width = 0.15
    pin_thickness = 0.075
    contact_width = 0.2

    contact_thickness = 0.15
    contact_slot_width = 0.3
    top_slot_offset = (body_width + pocket_width) / 4.0
    

calcDim = namedtuple( 'calcDim', ['pin_group_width', 'length', 'pocket_length'])


def dimensions(params):
    pin_group_width = ((params.num_pins / 2) - 1) * params.pin_pitch
    length =  pin_group_width + 2 * seriesParams.pin_inside_distance
    pocket_length = length - 2.0 * seriesParams.pocket_inside_distance
    return calcDim(pin_group_width=pin_group_width, length = length, pocket_length=pocket_length)



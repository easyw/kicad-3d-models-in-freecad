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
    'Molex_Picoflex_90325_04' : generate_params( 4, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_06' : generate_params( 6, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_08' : generate_params( 8, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_10' : generate_params(10, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_12' : generate_params(12, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_14' : generate_params(14, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_16' : generate_params(16, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_18' : generate_params(18, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_20' : generate_params(20, "Picoflex_90325", 1.27),
    'Molex_Picoflex_90325_26' : generate_params(26, "Picoflex_90325", 1.27)	
}


class seriesParams():

    pin_width = 0.64
    pin_chamfer_long = 0.25
    pin_chamfer_short = 0.25
    pin_height =  3.3					# Heaight above bottom surface of base
    pin_depth =   3.3					# Depth below bottom surface of base
    pin_inside_distance = 2.525			# Distance between centre of end pin and end of body

    pig_depth = 2.8                     # Depth below bottom surface of the plastic guidence pin
    pig_height = 6.4                    # Height above bottom surface of the plastic guidence pin


calcDim = namedtuple( 'calcDim', ['length'])


def dimensions(params):
    length = (params.num_pins-1) * params.pin_pitch + 2 * seriesParams.pin_inside_distance
    return calcDim(length = length)



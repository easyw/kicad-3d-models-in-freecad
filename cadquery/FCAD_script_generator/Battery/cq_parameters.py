#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

import collections
from collections import namedtuple

footprints_dir="Battery.pretty"

##enabling optional/default values to None
def namedtuple_with_defaults(typename, field_names, default_values=()):

    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T

Params = namedtuple_with_defaults("Params", [
	'modelname',		    # Model name
	'manufacture',		    # Manufacture
	'serie',		        # ModelName
    'modeltype',            # Model type
    'cellsize',             # Battery type
    'cellcnt',              # Number of battery
    'LC',                   # Large circle
    'spigot',               # Spigot
    'L',                    # Package length
    'L1',                   # Package length 1
    'L2',                   # Package length 2
    'W',                    # Package width
    'W1',                   # Package width 1
    'H',                    # Package height
    'BS',                   # If the side should be 'round' or 'chamfer'
    'BC',                   # Battery contact
    'BM',                   # Center of body
	'A1',				    # package board seperation
    'A2',                   # Belly distance to board
    'D',                    # Diameter
    'PW',                   # Pad width
    'PL',                   # Pad length
    'RW',                   # Right width
    'RW1',                  # Right width 1
    'MT',                   # Metal thickness
    'pins',                 # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
    'npthpins',             # npth holes
    'socket',               # 'type', centre diameter, length, height
    'topear',               # Top ear
    'rotation',             # Rotation if required
    'body_color_key',       # Body color
    'pin_color_key',        # Pin color
    'dest_dir_prefix',      # Destination directory

])

all_params = {

    'BX0036': Params(   # ModelName
        #
        #
        #
        modelname = 'BatteryHolder_Bulgin_BX0036_1xC',
        manufacture = 'Bulgin',     # Model name
        serie = 'BX0036',           # Model name
        modeltype = 'BX0036',       # Model type
        cellsize = 'C',             # Battery type
        cellcnt = 1,                # Number of battery
        L  = 59.1,                  # Package length
        W  = 30.2,                  # Package width
        H  = 32.1,                  # Package height
        BC = ['BC1', 3.0, 1.25],    # Battery contact
        A1 = 0.1,                   # package board seperation
        A2 = 2.00,                  # Belly distance to board
        pins = [('tht', 0.0, 0.0, 'rect', 1.0, 1.0, 4.7), ('tht', 55.60, 0.0, 'rect', 1.0, 1.0, 4.7)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        npthpins = [('S1', 11.9, 0.0, 3.8), ('S1', 43.70, 0.0, 3.8)],   # npth holes
        socket = ['S1', 8.0, 2.0, 2.0],                                 # 'type', centre diameter, length, height
        topear = [(0.0, 0.0, 3.0, 7.0), (55.60, 0.0, 3.0, 7.0)],        # Top ear
        rotation = 0,                                                   # Rotation if required
        body_color_key  = 'black body',                                 # Body color
        pin_color_key   = 'metal grey pins',                            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'                   # Destination directory
        ),


    'Keystone_103': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=719
        #
        modelname = 'BatteryHolder_Keystone_103_1x20mm',
        manufacture = 'Keystone',               # Model name
        serie = '103',                          # Model name
        modeltype = 'Button1',                  # Model type
        cellsize = '20mm',                      # Battery type
        cellcnt = 1,                            # Number of battery
        LC = [15.2, 0.0, 22.76, 20.22, 4.95],   # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        BC = ['BC2', 2.0, 1.01],                # Battery contact width, height diff to top
        A1 = 0.1,                               # package board seperation
        A2 = 2.54,                              # Belly distance to board
        npthpins = ['S2', 15.2, 0.0, 19.00, 1.57, 2.54],    # 'type', x, y, circle diameter, pig diameter, pig height))]
        spigot = ['rect', 1.78, 6.00],                      # Spigot, distance from edge to pin 1, height
        pins = [('tht', 0.0, 0.0, 'rectround', 0.2, 1.2, 4.75), ('tht', 20.49, 0.0, 'rectround', 0.2, 1.2, 4.75)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_104': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=744
        #
        modelname = 'BatteryHolder_Keystone_104_1x23mm',
        manufacture = 'Keystone',               # Model name
        serie = '104',                          # Model name
        modeltype = 'Button1',                  # Model type
        cellsize = '23mm',                      # Battery type
        cellcnt = 1,                            # Number of battery
        LC = [15.2, 0.0, 25.40, 23.14, 4.95],   # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        BC = ['BC2', 2.0, 1.01],                # Battery contact width, height diff to top
        A1 = 0.1,                               # package board seperation
        A2 = 2.54,                              # Belly distance to board
        npthpins = ['S2', 15.2, 0.0, 19.00, 1.57, 2.54],    # 'type', x, y, circle diameter, pig diameter, pig height))]
        spigot = ['rect', 1.3, 5.80],                       # Spigot, distance from edge to pin 1, height
        pins = [('tht', 0.0, 0.0, 'rectround', 0.2, 1.2, 4.75), ('tht', 20.49, 0.0, 'rectround', 0.2, 1.2, 4.75)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_105': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=745
        #
        modelname = 'BatteryHolder_Keystone_105_1x2430',
        manufacture = 'Keystone',               # Model name
        serie = '105',                          # Model name
        modeltype = 'Button1',                  # Model type
        cellsize = '2430',                      # Battery type
        cellcnt = 1,                            # Number of battery
        LC = [15.2, 0.0, 27.76, 25.02, 4.95],   # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        BC = ['BC2', 2.0, 1.01],                # Battery contact width, height diff to top
        A1 = 0.1,                               # package board seperation
        A2 = 2.54,                              # Belly distance to board
        npthpins = ['S2', 15.2, 0.0, 19.00, 1.57, 2.54],    # 'type', x, y, circle diameter, pig diameter, pig height))]
        spigot = ['rect', 1.9, 5.80],                       # Spigot, distance from edge to pin 1, height
        pins = [('tht', 0.0, 0.0, 'rectround', 0.2, 1.2, 4.75), ('tht', 20.49, 0.0, 'rectround', 0.2, 1.2, 4.75)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_106': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=720
        #
        modelname = 'BatteryHolder_Keystone_106_1x20mm',
        manufacture = 'Keystone',               # Model name
        serie = '106',                          # Model name
        modeltype = 'Button1',                  # Model type
        cellsize = '20mm',                      # Battery type
        cellcnt = 1,                            # Number of battery
        LC = [15.2, 0.0, 27.76, 20.22, 4.95],   # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        BC = ['BC2', 2.0, 1.01],                # Battery contact width, height diff to top
        A1 = 0.1,                               # package board seperation
        A2 = 2.54,                              # Belly distance to board
        npthpins = ['S2', 15.2, 0.0, 19.00, 1.57, 2.54],    # 'type', x, y, circle diameter, pig diameter, pig height))]
        spigot = ['rect', 1.9, 5.80],                       # Spigot, distance from edge to pin 1, height
        pins = [('tht', 0.0, 0.0, 'rectround', 0.2, 1.2, 4.75), ('tht', 20.50, 0.0, 'rectround', 0.2, 1.2, 4.75)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                       # Rotation if required
        body_color_key  = 'black body',                     # Body color
        pin_color_key   = 'metal grey pins',                # Pin color
        dest_dir_prefix = 'Battery.3dshapes'       # Destination directory
        ),

    'Keystone_107': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=746
        #
        modelname = 'BatteryHolder_Keystone_107_1x23mm',
        manufacture = 'Keystone',               # Model name
        serie = '107',                          # Model name
        modeltype = 'Button1',                  # Model type
        cellsize = '23mm',                      # Battery type
        cellcnt = 1,                            # Number of battery
        LC = [15.2, 0.0, 27.76, 23.14, 4.95],   # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        BC = ['BC2', 2.0, 1.01],                # Battery contact width, height diff to top
        A1 = 0.1,                               # package board seperation
        A2 = 2.54,                              # Belly distance to board
        npthpins = ['S2', 15.2, 0.0, 19.00, 1.57, 2.54],    # 'type', x, y, circle diameter, pig diameter, pig height))]
        spigot = ['rect', 1.9, 5.80],                       # Spigot, distance from edge to pin 1, height
        pins = [('tht', 0.0, 0.0, 'rectround', 0.2, 1.2, 4.75), ('tht', 20.50, 0.0, 'rectround', 0.2, 1.2, 4.75)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_500': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=710
        #
        modelname = 'BatteryHolder_Keystone_500',
        manufacture = 'Keystone',               # Model name
        serie = '500',                          # Model name
        modeltype = 'Button1',                  # Model type
        cellsize = '12mm',                      # Battery type
        cellcnt = 1,                            # Number of battery
        LC = [09.53, 0.0, 15.06, 12.62, 3.81],  # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        BC = ['BC2', 2.0, 0.76],                # Battery contact width, height diff to top
        A1 = 0.1,                               # package board seperation
        A2 = 2.54,                              # Belly distance to board
        npthpins = ['S2', 09.53, 0.0, 09.53, 1.57, 2.54],   # 'type', x, y, circle diameter, pig diameter, pig height))]
        spigot = ['rect', 2.54, 5.08],                      # Spigot, distance from edge to pin 1, height
        pins = [('tht', 0.0, 0.0, 'rect', 0.2, 0.89, 3.96), ('tht', 9.97, 0.0, 'rect', 0.2, 0.89, 3.96)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_1042_1x18650': Params(   # ModelName
        #
        # http://www.keyelco.com/product.cfm/product_id/918
        #
        modelname = 'BatteryHolder_Keystone_1042_1x18650',
        manufacture = 'Keystone',               # Model name
        serie = '1042',                         # Model name
        modeltype = 'Cylinder1',                # Model type
        cellsize = '18650',                     # Battery type
        cellcnt = 1,                            # Number of battery
        L  = 77.05,                             # Package length
        W  = 20.65,                             # Package width
        H  = 14.86,                             # Package height
        A1 = 0.1,                               # package board seperation
        BS = ['chamfer'],                       # If the side should be 'round' or 'chamfer'
        BC = ['BC4', 'switchright'],            # Battery contact width, length
        BM = [0.0, 0.0],                        # Center of body
        npthpins = [('pin', 27.60, -8.0, 'round', 03.68, 03.43), ('pin', -27.60, 8.0, 'round', 03.68, 03.43), ('pin', -35.82, -8.0, 'round', 1.57, 02.50)],  # 'type', x, y, circle diameter,))]
        pins = [('smd', -40.865, 00.00, 'rect', 04.68, 6.35), ('smd', 40.865, 00.00, 'rect', 04.68, 6.35)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                           # Rotation if required
        body_color_key  = 'black body',         # Body color
        pin_color_key   = 'gold pins',          # Pin color
        dest_dir_prefix = 'Battery.3dshapes'    # Destination directory
        ),

    'Keystone_2466_1xAAA': Params(   # ModelName
        #
        # https://www.keyelco.com/product-pdf.cfm?p=918
        #
        modelname = 'BatteryHolder_Keystone_2466_1xAAA',
        manufacture = 'Keystone',       # Model name
        serie = '2466',                 # Model name
        modeltype = 'Cylinder1',        # Model type
        cellsize = 'AAA',               # Battery type
        cellcnt = 1,                    # Number of battery
        L  = 49.99,                     # Package length
        W  = 13.00,                     # Package width
        H  = 12.70,                     # Package height
        A1 = 0.1,                       # package board seperation
        BS = ['round'],                 # If the side should be 'round' or 'chamfer'
        BC = ['BC4', 'switchright'],    # Battery contact width, length
        BM = [22.35, 0.0],              # Center of body
        pins = [('tht', 0.0, 0.0, 'round', 0.8, 0.8, 05.00), ('tht', 44.7, 0.0, 'round', 0.8, 0.8, 05.00)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_2462_2xAA': Params(   # ModelName
        #
        # https://www.keyelco.com/product-pdf.cfm?p=918
        # https://en.wikipedia.org/wiki/List_of_battery_sizes
        #
        modelname = 'BatteryHolder_Keystone_2462_2xAA',
        manufacture = 'Keystone',       # Model name
        serie = '2462',                 # Model name
        modeltype = 'Cylinder1',        # Model type
        cellsize = 'AA',                # Battery type
        cellcnt = 2,                    # Number of battery
        L  = 59.51,                     # Package length
        W  = 32.92,                     # Package width
        H  = 16.00,                     # Package height
        A1 = 0.1,                       # package board seperation
        BS = ['round'],                 # If the side should be 'round' or 'chamfer'
        BC = ['BC4', 'switchright'],    # Battery contact type, rotated or not
        BM = [27.17, 7.495],            # Center of body
        npthpins = [('hole', 27.165, 0.0, 03.43), ('hole', 27.165, 14.99, 03.43)],  # 'type', x, y, circle diameter,))]
        pins = [('tht', 00.00, 00.00, 'round', 0.8, 0.8, 05.00), ('tht', 00.00, 14.99, 'round', 0.8, 0.8, 05.00)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_2468_2xAAA': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=1033
        #
        modelname = 'BatteryHolder_Keystone_2468_2xAAA',
        manufacture = 'Keystone',       # Model name
        serie = '2468',                 # Model name
        modeltype = 'Cylinder1',        # Model type
        cellsize = 'AAA',               # Battery type
        cellcnt = 2,                    # Number of battery
        L  = 52.98,                     # Package length
        W  = 24.59,                     # Package width
        H  = 13.00,                     # Package height
        A1 = 0.1,                       # package board seperation
        BS = ['round'],                 # If the side should be 'round' or 'chamfer'
        BC = ['BC4', 'switchright'],    # Battery contact type, length
        BM = [23.89, 6.35],             # Center of body
        npthpins = [('hole', 38.608, 3.9624, 03.5), ('hole', 8.636, 8.6995, 03.5)],  # 'type', x, y, circle diameter,))]
        pins = [('tht', 00.00, 00.00, 'round', 0.8, 0.8, 05.00), ('tht', 0.0, 12.70, 'round', 0.8, 0.8, 05.00)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_2479_3xAAA': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=1041
        #
        modelname = 'BatteryHolder_Keystone_2479_3xAAA',
        manufacture = 'Keystone',       # Model name
        serie = '2479',                 # Model name
        modeltype = 'Cylinder1',        # Model type
        cellsize = 'AAA',               # Battery type
        cellcnt = 3,                    # Number of battery
        L  = 52.63,                     # Package length
        W  = 37.49,                     # Package width
        H  = 13.00,                     # Package height
        A1 = 0.1,                       # package board seperation
        BS = ['round'],                 # If the side should be 'round' or 'chamfer'
        BC = ['BC4', 'switchright'],    # Battery contact type, length
        BM = [23.725, 11.75],           # Center of body
        npthpins = [('hole', 23.7236, 0.0, 03.5), ('hole', 23.7236, 23.495, 03.5)],  # 'type', x, y, circle diameter,))]
        pins = [('tht', 00.00, 00.00, 'round', 0.8, 0.8, 04.00), ('tht', 0.0, 12.70, 'round', 0.8, 0.8, 04.00)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'MPD_BC2AAPC_2xAA': Params(   # ModelName
        #
        # http://www.memoryprotectiondevices.com/datasheets/BC2AAPC-datasheet.pdf
        #
        modelname = 'BatteryHolder_MPD_BC2AAPC_2xAA',
        manufacture = 'Keystone',       # Model name
        serie = '2468',                 # Model name
        modeltype = 'Cylinder1',        # Model type
        cellsize = 'AAA',               # Battery type
        cellcnt = 2,                    # Number of battery
        L  = 58.00,                     # Package length
        W  = 30.50,                     # Package width
        H  = 15.00,                     # Package height
        A1 = 0.1,                       # package board seperation
        BS = ['round'],                 # If the side should be 'round' or 'chamfer'
        BC = ['BC4', 'switchright'],    # Battery contact type, length
        BM = [26.16, 6.64],             # Center of body
        npthpins = [('hole', 26.16, 6.63, 03.65)],  # 'type', x, y, circle diameter,))]
        pins = [('tht', 00.00, 00.00, 'round', 0.89, 0.89, 04.00), ('tht', 0.0, 13.60, 'round', 0.89, 0.89, 04.00)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'MPD_BC12AAPC_2xAA': Params(   # ModelName
        #
        # http://www.memoryprotectiondevices.com/datasheets/BC12AAPC-datasheet.pdf
        #
        modelname = 'BatteryHolder_MPD_BC12AAPC_2xAA',
        manufacture = 'Keystone',       # Model name
        serie = 'BC12AAPC',             # Model name
        modeltype = 'Cylinder1',        # Model type
        cellsize = 'AA',                # Battery type
        cellcnt = 1,                    # Number of battery
        L  = 107.8,                     # Package length
        W  = 16.20,                     # Package width
        H  = 13.70,                     # Package height
        A1 = 0.1,                       # package board seperation
        BS = ['round'],                 # If the side should be 'round' or 'chamfer'
        BC = ['BC4', 'switchright'],    # Battery contact width, length
        BM = [51.00, 0.0],              # Center of body
        npthpins = [('hole', 26.15, -4.75, 02.50), ('hole', 26.15, 4.75, 02.50), ('hole', 75.85, -4.75, 02.50), ('hole', 75.85, 4.75, 02.50)],  # 'type', x, y, circle diameter,))]
        pins = [('tht', 0.0, 0.0, 'round', 0.9, 0.9, 04.00), ('tht', 102.00, 0.0, 'round', 0.9, 0.9, 04.00)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'MPD_BH-18650-PC2': Params(   # ModelName
        #
        # http://www.memoryprotectiondevices.com/datasheets/BK-18650-PC2-datasheet.pdf
        #
        modelname = 'BatteryHolder_MPD_BH-18650-PC2',
        manufacture = 'Keystone',       # Model name
        serie = '18650',                # Model name
        modeltype = 'Cylinder1',        # Model type
        cellsize = '18650',             # Battery type
        cellcnt = 1,                    # Number of battery
        L  = 77.7,                      # Package length
        W  = 20.9,                      # Package width
        H  = 21.31,                     # Package height
        A1 = 0.1,                       # package board seperation
        BS = ['chamfer'],               # If the side should be 'round' or 'chamfer'
        BC = ['BC1', 3.0],              # Battery contact type, width
        BM = [35.68, 0.0],              # Center of body
        npthpins = [('hole', 8.645, 0.0, 03.20), ('hole', 64.255, 0.0, 03.20)],  # 'type', x, y, circle diameter,))]
        pins = [('tht', 0.0, 0.0, 'rect', 0.2, 1.52, 3.30), ('tht', 72.90, 0.0, 'rect', 0.2, 1.52, 3.30)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                                   # Rotation if required
        body_color_key  = 'black body',                 # Body color
        pin_color_key   = 'metal grey pins',            # Pin color
        dest_dir_prefix = 'Battery.3dshapes'   # Destination directory
        ),

    'Keystone_1058_1x2032': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=1041
        #
        modelname = 'BatteryHolder_Keystone_1058_1x2032',
        manufacture = 'Keystone',                   # Model name
        serie = '1058',                             # Model name
        modeltype = 'Button2',                      # Model type
        cellsize = '2032',                          # Battery type
        cellcnt = 1,                                # Number of battery
        L  = 28.40,                                 # Package length
        W  = 16.00,                                 # Package width
        H  = 05.08,                                 # Package height
        spigot = [28.4, 7.0],                       # Spigot
        LC = [00.00, 00.00, 22.35, 20.27, 5.08],    # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        A1 = 0.1,                                   # package board seperation
        BC = ['BC5', 'right'],                      # Battery contact type, length
        pins = [('smd', -14.66, 00.00, 'rect', 02.54, 3.51), ('smd', 14.66, 00.00, 'rect', 02.54, 3.51)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                               # Rotation if required
        body_color_key  = 'black body',             # Body color
        pin_color_key   = 'gold pins',              # Pin color
        dest_dir_prefix = 'Battery.3dshapes'        # Destination directory
        ),

    'Keystone_1060_1x2032': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=1041
        #
        modelname = 'BatteryHolder_Keystone_1060_1x2032',
        manufacture = 'Keystone',                   # Model name
        serie = '1060',                             # Model name
        modeltype = 'Button3',                      # Model type
        cellsize = '2032',                          # Battery type
        cellcnt = 1,                                # Number of battery
        L  = 28.40,                                 # Package length
        W  = 16.00,                                 # Package width
        H  = 05.08,                                 # Package height
        spigot = [28.4, 7.0],                       # Spigot
        LC = [00.00, 00.00, 22.00, 20.27, 5.08],    # Large circle [x pos, y pos, outer diameter, inner diameter, height]
        A1 = 0.1,                                   # package board seperation
        BC = ['BC5', 'right'],                      # Battery contact type, length
        pins = [('smd', -14.66, 00.00, 'rect', 02.54, 3.61), ('smd', 14.66, 00.00, 'rect', 02.54, 3.61)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 0,                               # Rotation if required
        body_color_key  = 'black body',             # Body color
        pin_color_key   = 'gold pins',              # Pin color
        dest_dir_prefix = 'Battery.3dshapes'        # Destination directory
        ),

    'Keystone_3000_1x12mm': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=777
        #
        modelname = 'BatteryHolder_Keystone_3000_1x12mm',
        manufacture = 'Keystone',                   # Model name
        serie = '3000',                             # Model name
        modeltype = 'Button4',                      # Model type
        cellsize = 'CR1220',                        # Battery type
        cellcnt = 1,                                # Number of battery
        L  = 13.21,                                 # Package length
        W  = 12.07,                                 # Package width
        H  = 03.18,                                 # Package height
        LC = [07.14, 5.14],                         # [back side width, distance back end to pad]
        A1 = 0.1,                                   # package board seperation
        BC = ['BC6', 0.0],                          # Battery contact type, hole diameter in pad
        pins = [('smd', -08.03, 00.00, 'rect', 02.86, 3.17, 1.19), ('smd', 08.03, 00.00, 'rect', 02.86, 3.17, 1.19)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 180,                             # Rotation if required
        body_color_key  = 'black body',             # Body color
        pin_color_key   = 'metal grey pins',        # Pin color
        dest_dir_prefix = 'Battery.3dshapes'        # Destination directory
        ),

    'Keystone_3008_1x2450': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=786
        #
        modelname = 'BatteryHolder_Keystone_3008_1x2450',
        manufacture = 'Keystone',                   # Model name
        serie = '3008',                             # Model name
        modeltype = 'Button4',                      # Model type
        cellsize = 'CR2450',                        # Battery type
        cellcnt = 1,                                # Number of battery
        L  = 25.40,                                 # Package length
        W  = 22.61,                                 # Package width
        H  = 05.84,                                 # Package height
        LC = [7.57, 15.46],                         # [back side width, distance back end to pad (W - distance to pad)]
        A1 = 0.1,                                   # package board seperation
        BC = ['BC7', -1.515],                        # Battery contact type, hole diameter in pad
        pins = [('smd', -15.24, 00.00, 'rect', 05.08, 05.08, 2.36), ('smd', 15.24, 00.00, 'rect', 05.08, 05.08, 2.36)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 180,                             # Rotation if required
        body_color_key  = 'black body',             # Body color
        pin_color_key   = 'metal grey pins',        # Pin color
        dest_dir_prefix = 'Battery.3dshapes'        # Destination directory
        ),

    'Keystone_3001_1x12mm': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=778
        #
        modelname = 'BatteryHolder_Keystone_3001_1x12mm',
        manufacture = 'Keystone',                   # Model name
        serie = '3000',                             # Model name
        modeltype = 'Button4',                      # Model type
        cellsize = 'CR1220',                        # Battery type
        cellcnt = 1,                                # Number of battery
        L  = 13.21,                                 # Package length
        W  = 12.07,                                 # Package width
        H  = 02.18,                                 # Package height
        LC = [07.14, 6.73],                         # [back side width, distance back end to pad]
        A1 = 0.1,                                   # package board seperation
        BC = ['BC6', -1.39],                        # Battery contact type, 
        pins = [('tht', -06.605, 00.00, 'rectbend', 01.57, 00.20, 03.16, 01.26), ('tht', 06.605, 00.00, 'rectbend', 01.57, 00.20, 03.16, 01.26)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 180,                             # Rotation if required
        body_color_key  = 'black body',             # Body color
        pin_color_key   = 'metal grey pins',        # Pin color
        dest_dir_prefix = 'Battery.3dshapes'        # Destination directory
        ),

    'Keystone_3009_1x2450': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=787
        #
        modelname = 'BatteryHolder_Keystone_3009_1x2450',
        manufacture = 'Keystone',                   # Model name
        serie = '3009',                             # Model name
        modeltype = 'Button4',                      # Model type
        cellsize = 'CR2450',                        # Battery type
        cellcnt = 1,                                # Number of battery
        L  = 25.40,                                 # Package length
        W  = 22.61,                                 # Package width
        H  = 05.08,                                 # Package height
        LC = [07.57, 12.045],                       # [back side width, distance back end to pad]
        A1 = 0.1,                                   # package board seperation
        BC = ['BC7', 00.00],                        # Battery contact type, hole diameter in pad
        pins = [('tht', -12.70, 00.00, 'rectbend', 01.57, 00.20, 03.06, 01.02), ('tht', 12.70, 00.00, 'rectbend', 01.57, 00.20, 03.06, 01.02)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 180,                             # Rotation if required
        body_color_key  = 'black body',             # Body color
        pin_color_key   = 'metal grey pins',        # Pin color
        dest_dir_prefix = 'Battery.3dshapes'        # Destination directory
        ),

    'Keystone_3034_1x20mm': Params(   # ModelName
        #
        # http://www.keyelco.com/product-pdf.cfm?p=798
        #
        modelname = 'BatteryHolder_Keystone_3034_1x20mm',
        manufacture = 'Keystone',                   # Model name
        serie = '3034',                             # Model name
        modeltype = 'Button4',                      # Model type
        cellsize = 'CR2025',                        # Battery type
        cellcnt = 1,                                # Number of battery
        L  = 21.26,                                 # Package length
        W  = 16.12,                                 # Package width
        H  = 04.06,                                 # Package height
        LC = [17.28, 04.85],                        # [back side width, distance back end to pad (W - distance to pad)]
        A1 = 0.1,                                   # package board seperation
        BC = ['BC8', -10.63, -7.39, 09.00, 2.0],         # Battery contact type, hole diameter in pad
        pins = [('smd', -10.985, 00.00, 'rect', 01.27, 05.08), ('smd', 10.985, 00.00, 'rect', 01.27, 05.08)],      # Pins tht/smd, x pos, y pos, 'round/rect', diameter/x size, y size, length
        rotation = 180,                             # Rotation if required
        body_color_key  = 'black body',             # Body color
        pin_color_key   = 'metal grey pins',        # Pin color
        dest_dir_prefix = 'Battery.3dshapes'        # Destination directory
        ),

    'Seiko_MS621F': Params(
        #
        # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
        # A number of parameters have been fixed or guessed, such as A2
        # 
        modelname = 'BatteryHolder_Seiko_MS621F',   # Model name
        A1 = 0.0,                                   # Body PCB seperation
        D = 6.8,                                    # Battery diameter
        H = 2.7,                                    # Battery height
        PW = 1.8,                                   # Pad width
        PL = 2.0,                                   # Pad length
        RW = 2.5,                                   # Right width
        RW1 = 2.2,                                  # Right width 1
        MT = 0.15,                                  # Metal thickness

        rotation = 0,                               # Rotation if required
        body_color_key = 'metal aluminum',          # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        dest_dir_prefix = 'Battery.3dshapes',       # destination directory
        ),

    'Keystone_2993': Params(
        #
        # http://www.belton.co.kr/inc/downfile.php?seq=58&file=pdf
        # A number of parameters have been fixed or guessed, such as A2
        # 
        modelname = 'BatteryHolder_Keystone_2993',  # Model name
        A1 = 0.0,                                   # Body PCB seperation
        L  = 09.14,                                 # Package length
        L1 = 02.54,                                 # Package length 1
        L2 = 02.79,                                 # Package length 2
        W  = 15.88,                                 # Package width
        W1 = 13.97,                                 # Package width 1
        MT = 0.10,                                  # Metal thickness
        npthpins = [('hole', 1.91, 0.0, 0.79), ('hole', 8.26, 0.0, 0.79), ('hole', 14.61, 0.0, 0.79)],  # 'type', x, y, circle diameter,))]

        rotation = 180,                             # Rotation if required
        body_color_key = 'metal grey pins',         # Body color
        pin_color_key = 'metal grey pins',          # Pin color
        dest_dir_prefix = 'Battery.3dshapes',       # destination directory
        ),

}

# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

from collections import namedtuple

destination_dir="/Capacitors_Radial_THT"
# destination_dir="./"

Params = namedtuple("Params", [
    'L' ,  # overall height
    'D' ,  # body diameter
    'd' ,  # lead diameter
    'F' ,  # lead separation (center to center)
    'll',  # lead length
    'la',  # extra lead length of the anode
    'bs',  # board separation
    'pin3', # third pin (width, x offset, y offset)
    'modelName', # modelName
    'rotation',  # rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_radial_th_cap = {# Aluminum TH capacitors
        # Dimensions per http://industrial.panasonic.com/lecs/www-data/pdf/ABA0000/ABA0000PE369.pdf
    "L16_D5_p05" : Params(
        L = 16.,
        D = 5.,
        d = 0.5,
        F = 2.,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'c_el_th_L16_D5_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    "L10_D5_p05" : Params(
        L = 10.,
        D = 5.,
        d = 0.5,
        F = 2.,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'c_el_th_L10_D5_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    "L11_5_D08_p05" : Params(
        L = 11.5,
        D = 8.,
        d = 0.6,
        F = 3.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'c_el_th_L11_5_D08_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    "L18_D15_p075" : Params(
        L = 18,
        D = 15.,
        d = 0.8,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'c_el_th_L18_D15_p075', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    "L18_D20_p075" : Params(
        L = 18,
        D = 20.,
        d = 0.8,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'c_el_th_L18_D20_p075', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    "L35_D12.5_p05" : Params(
        L = 35,
        D = 12.5,
        d = 0.8,
        F = 5.,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'c_el_th_L35_D12.5_p05', #modelName
        rotation  = -90, # rotation if required
        dest_dir_prefix = ''
    ),
    "CP_Radial_D10.0mm_P5.00mm" : Params(
        L = 12.5,
        D = 10.,
        d = 0.6,
        F = 5.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D10.0mm_P5.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = ''
    ),
}

kicad_naming_params_radial_th_cap = {
    "CP_Radial_D4.0mm_P1.50mm" : Params(# from Jan Kriege's 3d models
        L = 4,
        D = 4.,
        d = 0.3,
        F = 1.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D4.0mm_P1.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D4.0mm_P2.00mm" : Params(# from Jan Kriege's 3d models
        L = 4,
        D = 4.,
        d = 0.3,
        F = 2.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D4.0mm_P2.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D5.0mm_P2.00mm" : Params(# from Jan Kriege's 3d models
        L = 5,
        D = 5.,
        d = 0.5,
        F = 2.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D5.0mm_P2.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D5.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 5,
        D = 5.,
        d = 0.5,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D5.0mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D6.3mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 6.3,
        D = 6.3,
        d = 0.5,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D6.3mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D7.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 7.5,
        D = 7.5,
        d = 0.5,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D7.5mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D8.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 8.0,
        D = 8.0,
        d = 0.5,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D8.0mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D8.0mm_P3.50mm" : Params(# from Jan Kriege's 3d models
        L = 8.0,
        D = 8.0,
        d = 0.5,
        F = 3.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D8.0mm_P3.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D8.0mm_P3.50mm" : Params(# from Jan Kriege's 3d models
        L = 8.0,
        D = 8.0,
        d = 0.5,
        F = 3.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D8.0mm_P3.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D8.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 8.0,
        D = 8.0,
        d = 0.5,
        F = 5.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D8.0mm_P5.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D10.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 10.0,
        D = 10.0,
        d = 0.5,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D10.0mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D10.0mm_P3.50mm" : Params(# from Jan Kriege's 3d models
        L = 10.0,
        D = 10.0,
        d = 0.5,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D10.0mm_P3.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D10.0mm_P3.80mm" : Params(# from Jan Kriege's 3d models
        L = 10.0,
        D = 10.0,
        d = 0.7,
        F = 3.8,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D10.0mm_P3.80mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D10.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 10.0,
        D = 10.0,
        d = 0.7,
        F = 5.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D10.0mm_P5.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D10.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 10.0,
        D = 10.0,
        d = 0.7,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D10.0mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D12.5mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 12.5,
        D = 12.5,
        d = 0.9,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D12.5mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D12.5mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 12.5,
        D = 12.5,
        d = 0.9,
        F = 5.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D12.5mm_P5.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D12.5mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 12.5,
        D = 12.5,
        d = 0.9,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D12.5mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D13.0mm_P2.50mm" : Params(# from Jan Kriege's 3d models
        L = 13.0,
        D = 13.0,
        d = 0.9,
        F = 2.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D13.0mm_P2.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D13.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 13.0,
        D = 13.0,
        d = 0.9,
        F = 5.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D13.0mm_P5.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D13.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 13.0,
        D = 13.0,
        d = 0.9,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D13.0mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D14.0mm_P5.00mm" : Params(# from Jan Kriege's 3d models
        L = 14.0,
        D = 14.0,
        d = 0.9,
        F = 5.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D14.0mm_P5.00mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D14.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 14.0,
        D = 14.0,
        d = 0.9,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D14.0mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D16.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 16.0,
        D = 16.0,
        d = 0.9,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D16.0mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D17.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 17.0,
        D = 17.0,
        d = 0.9,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D17.0mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D18.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 18.0,
        D = 18.0,
        d = 0.9,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D18.0mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D18.0mm_P7.50mm" : Params(# from Jan Kriege's 3d models
        L = 18.0,
        D = 18.0,
        d = 0.9,
        F = 7.5,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D18.0mm_P7.50mm', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D22.0mm_P10.00mm_3pin_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 22.0,
        D = 22.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = (2.2,-6.7+10.0/2,-4.75),
        modelName = 'CP_Radial_D22.0mm_P10.00mm_3pin_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D22.0mm_P10.00mm_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 22.0,
        D = 22.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D22.0mm_P10.00mm_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D24.0mm_P10.00mm_3pin_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 24.0,
        D = 24.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = (2.2,-6.7+10.0/2,-4.75),
        modelName = 'CP_Radial_D24.0mm_P10.00mm_3pin_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D24.0mm_P10.00mm_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 24.0,
        D = 24.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D24.0mm_P10.00mm_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D25.0mm_P10.00mm_3pin_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 25.0,
        D = 25.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = (2.2,-6.7+10.0/2,-4.75),
        modelName = 'CP_Radial_D25.0mm_P10.00mm_3pin_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D25.0mm_P10.00mm_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 25.0,
        D = 25.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D25.0mm_P10.00mm_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D26.0mm_P10.00mm_3pin_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 26.0,
        D = 26.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = (2.2,-6.7+10.0/2,-4.75),
        modelName = 'CP_Radial_D26.0mm_P10.00mm_3pin_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D26.0mm_P10.00mm_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 26.0,
        D = 26.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D26.0mm_P10.00mm_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D30.0mm_P10.00mm_3pin_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 30.0,
        D = 30.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = (2.2,-6.7+10.0/2,-4.75),
        modelName = 'CP_Radial_D30.0mm_P10.00mm_3pin_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D30.0mm_P10.00mm_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 30.0,
        D = 30.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D30.0mm_P10.00mm_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D35.0mm_P10.00mm_3pin_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 35.0,
        D = 35.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = (2.2,-6.7+10.0/2,-4.75),
        modelName = 'CP_Radial_D35.0mm_P10.00mm_3pin_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D35.0mm_P10.00mm_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 35.0,
        D = 35.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D35.0mm_P10.00mm_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D40.0mm_P10.00mm_3pin_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 40.0,
        D = 40.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = (2.2,-6.7+10.0/2,-4.75),
        modelName = 'CP_Radial_D40.0mm_P10.00mm_3pin_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),
    "CP_Radial_D40.0mm_P10.00mm_SnapIn" : Params(# from Jan Kriege's 3d models
        L = 40.0,
        D = 40.0,
        d = 1.7,
        F = 10.0,
        ll = 2.0,
        la = 0.0,
        bs = 0.,
        pin3 = None,
        modelName = 'CP_Radial_D40.0mm_P10.00mm_SnapIn', #modelName
        rotation  = 180, # rotation if required
        dest_dir_prefix = '../Capacitors_THT.3dshapes/'
    ),

}   
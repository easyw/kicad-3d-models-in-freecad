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

from Params import *

class SeriesParams():
    # footprint_dir="Housings_SSOP.pretty"
    # lib_name = "Housings_SSOP"

    footprint_dir="Package_SSOP.pretty"
    lib_name = "Package_SSOP"

    body_color_key = "black body"
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"


part_params = {
    'ETSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ds/symlink/lm5005.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.1,             # pin thickness, body center part height
        R1 = 0.09,             # pin upper corner, inner radius
        R2 = 0.09,             # pin lower corner, inner radius
        S = 0.3,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.0,            # body height
        b = 0.25,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 10,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (4.2,3.0),          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'ETSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm',
        modelName = 'ETSSOP-20-1EP_4.4x6.5mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'HTSSOP-14-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3.1mm': Params( # Datasheet: http://www.ti.com/lit/ds/symlink/lm5161.pdf#page=34
                                                                   # Package drawing: http://www.ti.com/lit/ml/mpds370/mpds370.pdf
        the = 14.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.09,             # pin upper corner, inner radius
        R2 = 0.09,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.6,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 5.0,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.1,            # body height
        b = 0.25,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 7,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (3.0,3.1),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'HTSSOP-14-1EP_4.4x5mm_Pitch0.65mm_ThermalPad',
        modelName = 'HTSSOP-14-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3.1mm',
        rotation = -90,       # rotation if required
        ),
    'HTSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm_ThermalPad': Params( # from http://www.ti.com/lit/ml/mhts001g/mhts001g.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.09,             # pin upper corner, inner radius
        R2 = 0.09,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.1,            # body height
        b = 0.25,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 10,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (6.0,3.5),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'HTSSOP-20-1EP_4.4x6.5mm_Pitch0.65mm_ThermalPad',
        modelName = 'HTSSOP-20-1EP_4.4x6.5mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'HTSSOP-28_4.4x9.7mm_Pitch0.65mm_ThermalPad': Params( # from http://www.ti.com/lit/ml/mpds033b/mpds033b.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.09,             # pin upper corner, inner radius
        R2 = 0.09,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 9.7,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.1,            # body height
        b = 0.25,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 14,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (9.0,3.5),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'HTSSOP-28_4.4x9.7mm_Pitch0.65mm_ThermalPad',
        modelName = 'HTSSOP-28-1EP_4.4x9.7mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'MFSOP6-4_4.4x3.6mm_Pitch1.27mm': Params( # from https://toshiba.semicon-storage.com/ap-en/design-support/package/detail.4pin%20MFSOP6.html
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.05,            # pin upper corner, inner radius
        R2 = 0.05,            # pin lower corner, inner radius
        S = 0.25,             # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.15,          # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.6,             # body length
        E1 = 4.4,             # body width
        E = 7.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,             # body-board separation
        A2 = 2.5,             # body height
        b = 0.4,              # pin width
        e = 1.27,             # pin (center-to-center) distance
        npx = 3,              # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = (2, 5), # no pin excluded
        old_modelName = 'MFSOP6-4_4.4x3.6mm_Pitch1.27mm',
        modelName = 'MFSOP6-4_4.4x3.6mm_P1.27mm',
        rotation = -90,       # rotation if required
        ),
    'MFSOP6-5_4.4x3.6mm_Pitch1.27mm': Params( # from https://toshiba.semicon-storage.com/ap-en/design-support/package/detail.5pin%20MFSOP6.html
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.05,            # pin upper corner, inner radius
        R2 = 0.05,            # pin lower corner, inner radius
        S = 0.25,             # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.15,          # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.6,             # body length
        E1 = 4.4,             # body width
        E = 7.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,             # body-board separation
        A2 = 2.5,             # body height
        b = 0.4,              # pin width
        e = 1.27,             # pin (center-to-center) distance
        npx = 3,              # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = (0, 2), # no pin excluded
        old_modelName = 'MFSOP6-5_4.4x3.6mm_Pitch1.27mm',
        modelName = 'MFSOP6-5_4.4x3.6mm_P1.27mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-8_3x3mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081660_G_MS8.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.15,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-8_3x3mm_Pitch0.65mm',
        modelName = 'MSOP-8_3x3mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-8-1EP_3x3mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081662_K_MS8E.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (1.88,1.68),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-8-1EP_3x3mm_Pitch0.65mm',
        modelName = 'MSOP-8-1EP_3x3mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-10_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081661_F_MS.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.23,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 5,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-10_3x3mm_Pitch0.5mm',
        modelName = 'MSOP-10_3x3mm_P0.5mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-10-1EP_3x3mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081664_I_MSE.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.23,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 5,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (1.88,1.68),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-10-1EP_3x3mm_Pitch0.5mm',
        modelName = 'MSOP-10-1EP_3x3mm_P0.5mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-12_3x4mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081668_A_MS12.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 6,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-12_3x4mm_Pitch0.65mm',
        modelName = 'MSOP-12_3x4mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-12-1EP_3x4mm_Pitch0.65mm': Params( # from http://cds.linear.com/docs/en/packaging/05081666_G_MSE12.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 6,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (2.845,1.651),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-12-1EP_3x4mm_Pitch0.65mm',
        modelName = 'MSOP-12-1EP_3x4mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-16_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081669_A_MS16.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-16_3x4mm_Pitch0.5mm',
        modelName = 'MSOP-16_3x4mm_P0.5mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-16-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081667_F_MSE16.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (2.84,1.65),          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'MSOP-16-1EP_3x4mm_Pitch0.5mm',
        modelName = 'MSOP-16-1EP_3x4mm_P0.5mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-12-16_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081871_D_MSE16%2812%29.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = (2,4,13,15), # no pin excluded
        old_modelName = 'MSOP-12-16_3x4mm_Pitch0.5mm',
        modelName = 'MSOP-12-16_3x4mm_P0.5mm',
        rotation = -90,       # rotation if required
        ),
    'MSOP-12-16-1EP_3x4mm_Pitch0.5mm': Params( # from http://cds.linear.com/docs/en/packaging/05081871_D_MSE16%2812%29.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,            # body height
        b = 0.22,             # pin width
        e = 0.5,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = (2.84,1.65),          # ePad is guessed from datasheet
        excluded_pins = (2,4,13,15), # no pin excluded
        old_modelName = 'MSOP-12-16-1EP_3x4mm_Pitch0.5mm',
        modelName = 'MSOP-12-16-1EP_3x4mm_P0.5mm',
        rotation = -90,       # rotation if required
        ),
    'OnSemi_Micro8': Params( # from https://www.onsemi.com/pub/Collateral/846A-02.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.18,             # pin thickness, body center part height
        R1 = 0.05,             # pin upper corner, inner radius
        R2 = 0.05,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,             # body length
        E1 = 3.0,             # body width
        E = 4.9,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 0.85,             # body height
        b = 0.33,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'OnSemi_Micro8',
        modelName = 'OnSemi_Micro8',
        rotation = -90,       # rotation if required
        ),
    'PSOP-44_16.9x27.17mm_Pitch1.27mm': Params( # from http://pdf.datasheetcatalog.com/datasheet/macronix/MX29F800TMI-90.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.20,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.5,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,           # first pin indicator radius
        fp_d = 0.4,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 28.5,             # body length
        E1 = 12.60,             # body width
        E = 16.03,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.69,             # body height
        b = 0.41,             # pin width
        e = 1.27,            # pin (center-to-center) distance
        npx = 22,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad is guessed from datasheet
        excluded_pins = None, # no pin excluded
        old_modelName = 'PSOP-44_16.9x27.17mm_Pitch1.27mm',
        modelName = 'PSOP-44_16.9x27.17mm_P1.27mm',
        rotation = -90,       # rotation if required
        ),
    'QSOP-16_3.9x4.9mm_Pitch0.635mm': Params( # from http://www.onsemi.com/pub/Collateral/492-01.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.22,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.05,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,             # body length
        E1 = 3.9,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.17,            # body-board separation
        A2 = 1.25,            # body height
        b = 0.25,             # pin width
        e = 0.635,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'QSOP-16_3.9x4.9mm_Pitch0.635mm',
        modelName = 'QSOP-16_3.9x4.9mm_P0.635mm',
        rotation = -90,       # rotation if required
        ),
    'QSOP-24_3.9x8.7mm_Pitch0.635mm': Params( # from http://www.onsemi.com/pub/Collateral/492B-01.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.22,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 8.65,             # body length
        E1 = 3.9,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.17,            # body-board separation
        A2 = 1.55,            # body height
        b = 0.25,             # pin width
        e = 0.635,            # pin (center-to-center) distance
        npx = 12,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'QSOP-24_3.9x8.7mm_Pitch0.635mm',
        modelName = 'QSOP-24_3.9x8.7mm_P0.635mm',
        rotation = -90,       # rotation if required
        ),
    'SOP-4_4.4x2.6mm_Pitch1.27mm': Params( # from http://www.vishay.com/docs/83510/tcmt1100.pdf#page=7
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.2,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#       L = 0.60,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 2.60,             # body length
        E1 = 4.40,             # body width
        E = 7.00,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.10,            # body-board separation
        A2 = 2.00,            # body height
        b = 0.4,             # pin width
        e = 1.27,            # pin (center-to-center) distance
        npx = 2,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SOP-4_4.4x2.6mm_Pitch1.27mm',
        modelName = 'SOP-4_4.4x2.6mm_P1.27mm',
        rotation = -90,       # rotation if required
        ),
    'SOP-16_4.4x10.4mm_Pitch1.27mm': Params( # from http://www.vishay.com/docs/49447/49447.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.2,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 10.4,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.0,            # body height
        b = 0.4,             # pin width
        e = 1.27,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SOP-16_4.4x10.4mm_Pitch1.27mm',
        modelName = 'SOP-16_4.4x10.4mm_P1.27mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-8_2.95x2.8mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds049b/mpds049b.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.1,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 2.95,             # body length
        E1 = 2.8,             # body width
        E = 4.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.05,            # body-board separation
        A2 = 1.3,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-8_2.95x2.8mm_Pitch0.65mm',
        modelName = 'SSOP-8_2.95x2.8mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-8_3.9x5.05mm_P1.27mm': Params( # from http://www.fujitsu.com/downloads/MICRO/fsa/pdf/products/memory/fram/MB85RS16-DS501-00014-6v0-E.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,           # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.18,             # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 5.05,            # body length
        E1 = 3.90,            # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.01,            # body-board separation
        A2 = 1.55,            # body height
        b = 0.44,             # pin width
        e = 1.27,             # pin (center-to-center) distance
        npx = 4,              # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-8_3.9x5.05mm_P1.27mm',
        modelName = 'SSOP-8_3.9x5.05mm_P1.27mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-8_5.30x5.24mm_P1.27mm': Params( # from http://www.fujitsu.com/ca/en/Images/MB85RS2MT-DS501-00023-1v0-E.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,           # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.18,             # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,          # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 5.30,            # body length
        E1 = 5.24,            # body width
        E =  7.80,            # body overall width  E=E1+2*(S+L+c)
        A1 = 0.01,            # body-board separation
        A2 = 2.10,            # body height
        b = 0.43,             # pin width
        e = 1.27,             # pin (center-to-center) distance
        npx = 4,              # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-8_5.30x5.24mm_P1.27mm',
        modelName = 'SSOP-8_5.30x5.24mm_P1.27mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-8_3.95x5.21x3.27mm_Pitch1.27mm': Params( # from http://www.ti.com/lit/ml/mpds049b/mpds049b.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.1,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.18,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 5.21,             # body length
        E1 = 3.95,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.01,            # body-board separation
        A2 = 3.27,            # body height
        b = 0.4,             # pin width
        e = 1.27,            # pin (center-to-center) distance
        npx = 4,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-8_3.95x5.21x3.27mm_Pitch1.27mm',
        modelName = 'SSOP-8_3.95x5.21x3.27mm_Pitch1.27mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-14_5.3x6.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/msso002e/msso002e.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.17,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.25,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.2,             # body length
        E1 = 5.3,             # body width
        E = 7.8,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.0,            # body height
        b = 0.3,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 7,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-14_5.3x6.2mm_Pitch0.65mm',
        modelName = 'SSOP-14_5.3x6.2mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-16_3.9x4.9mm_Pitch0.635mm': Params( # from http://docs-asia.electrocomponents.com/webdocs/0156/0900766b80156779.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.10,          # top part of body is that much smaller
        c = 0.2,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.05,           # 0.45 chamfer of the 1st pin corner
        D1 = 4.9,             # body length
        E1 = 3.9,             # body width
        E = 6.0,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.75,            # body height
        b = 0.25,             # pin width
        e = 0.635,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-16_3.9x4.9mm_Pitch0.635mm',
        modelName = 'SSOP-16_3.9x4.9mm_P0.635mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-16_4.4x5.2mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/565AM.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 5.2,             # body length
        E1 = 4.4,             # body width
        E = 6.5,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.3,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-16_4.4x5.2mm_Pitch0.65mm',
        modelName = 'SSOP-16_4.4x5.2mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-16_5.3x6.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds507/mpds507.pdf
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.17,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.2,             # body length
        E1 = 5.3,             # body width
        E = 7.8,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 2.0,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 8,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-16_5.3x6.2mm_Pitch0.65mm',
        modelName = 'SSOP-16_5.3x6.2mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-18_4.4x6.5mm_Pitch0.65mm': Params( # from https://toshiba.semicon-storage.com/us/design-support/package/detail.SSOP18-P-225-0.65.html
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,             # body-board separation
        A2 = 1.3,             # body height
        b = 0.24,             # pin width
        e = 0.65,             # pin (center-to-center) distance
        npx = 9,              # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-18_4.4x6.5mm_Pitch0.65mm',
        modelName = 'SSOP-18_4.4x6.5mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-20_4.4x6.5mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/565AM.PDF
        the = 12.0,           # body angle in degrees
        tb_s = 0.15,          # top part of body is that much smaller
        c = 0.15,             # pin thickness, body center part height
        R1 = 0.1,             # pin upper corner, inner radius
        R2 = 0.1,             # pin lower corner, inner radius
        S = 0.2,              # pin top flat part length (excluding corner arc)
#        L = 0.64,            # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,           # first pin indicator radius
        fp_d = 0.2,           # first pin indicator distance from edge
        fp_z = 0.1,           # first pin indicator depth
        ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
        D1 = 6.5,             # body length
        E1 = 4.4,             # body width
        E = 6.4,              # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,            # body-board separation
        A2 = 1.3,            # body height
        b = 0.22,             # pin width
        e = 0.65,            # pin (center-to-center) distance
        npx = 10,             # number of pins along X axis (width)
        npy = 0,              # number of pins along y axis (length)
        epad = None,          # ePad
        excluded_pins = None, # no pin excluded
        old_modelName = 'SSOP-20_4.4x6.5mm_Pitch0.65mm',
        modelName = 'SSOP-20_4.4x6.5mm_P0.65mm',
        rotation = -90,       # rotation if required
        ),
    'SSOP-20_5.3x7.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds508/mpds508.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.0,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='SSOP-20_5.3x7.2mm_Pitch0.65mm', #modelName
        modelName ='SSOP-20_5.3x7.2mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'SSOP-24_3.9x8.7mm_Pitch0.635mm': Params( # from http://cds.linear.com/docs/en/packaging/05081641_B_GN24.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.15,    # top part of body is that much smaller
        c = 0.22,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 8.7,       # body length
        E1 = 3.9,       # body width
        E = 6.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.55,  # body height
        b = 0.25,  # pin width
        e = 0.635,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='SSOP-24_3.9x8.7mm_Pitch0.635mm', #modelName
        modelName ='SSOP-24_3.9x8.7mm_P0.635mm', #modelName
        rotation = -90, # rotation if required
        ),
    'SSOP-24_5.3x8.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds509/mpds509.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 8.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.0,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='SSOP-24_5.3x8.2mm_Pitch0.65mm', #modelName
        modelName ='SSOP-24_5.3x8.2mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'SSOP-28_5.3x10.2mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ml/mpds509/mpds509.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 10.2,       # body length
        E1 = 5.3,       # body width
        E = 7.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.0,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='SSOP-28_5.3x10.2mm_Pitch0.65mm', #modelName
        modelName ='SSOP-28_5.3x10.2mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'SSOP-48_7.5x15.9mm_Pitch0.635mm': Params( # from http://www.ti.com/lit/ml/mpds490/mpds490.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 15.9,       # body length
        E1 = 7.5,       # body width
        E = 10.35,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.79,  # body height
        b = 0.223,  # pin width
        e = 0.635,  # pin (center-to-center) distance
        npx = 24,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='SSOP-48_7.5x15.9mm_Pitch0.635mm', #modelName
        modelName ='SSOP-48_7.5x15.9mm_P0.635mm', #modelName
        rotation = -90, # rotation if required
        ),
    'SSOP-56_7.5x18.5mm_Pitch0.635mm': Params( # from http://www.ti.com/lit/ml/mpds491/mpds491.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 18.5,       # body length
        E1 = 7.5,       # body width
        E = 10.35,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.79,  # body height
        b = 0.223,  # pin width
        e = 0.635,  # pin (center-to-center) distance
        npx = 28,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='SSOP-56_7.5x18.5mm_Pitch0.635mm', #modelName
        modelName ='SSOP-56_7.5x18.5mm_P0.635mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSOP-I-48_12x18.4mm_Pitch0.5mm': Params( # from http://www.onsemi.com/pub/Collateral/950AD.PDF
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.0,       # body length
        E1 = 18.4,       # body width
        E = 20.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.2,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 24,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSOP-I-48_12x18.4mm_Pitch0.5mm', #modelName
        modelName ='TSOP-I-48_12x18.4mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSOP-II-32_21.0x10.2mm_Pitch1.27mm': Params( # from http://www.topline.tv/drawings/pdf/TSOP-T2/TSOP32T50-T2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 21.0,       # body length
        E1 = 10.16,       # body width
        E = 11.76,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.15,  # body-board separation
        A2 = 1.2,  # body height
        b = 0.4,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSOP-II-32_21.0x10.2mm_Pitch1.27mm', #modelName
        modelName ='TSOP-II-32_21.0x10.2mm_P1.27mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-8_3x3mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT505-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 3.0,       # body length
        E1 = 3.0,       # body width
        E = 4.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-8_3x3mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-8_3x3mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-8_4.4x3mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT530-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 3.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-8_4.4x3mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-8_4.4x3mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-10_3x3mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT552-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 3.0,       # body length
        E1 = 3.0,       # body width
        E = 4.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.23,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 5,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-10_3x3mm_Pitch0.5mm', #modelName
        modelName ='TSSOP-10_3x3mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-14_4.4x5mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT402-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 7,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-14_4.4x5mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-14_4.4x5mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-16_4.4x5mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT403-3.pdf
        the = 10.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.0, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-16_4.4x5mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-16_4.4x5mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-16-1EP_4.4x5mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/948AP.PDF
        the = 10.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.0, #0.45 chamfer of the 1st pin corner
        D1 = 5.0,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 8,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (2.74,2.74), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-16-1EP_4.4x5mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-16-1EP_4.4x5mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-20_4.4x6.5mm_Pitch0.65mm': Params( # from http://www.onsemi.com/pub/Collateral/948AP.PDF
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 6.5,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 10,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-20_4.4x6.5mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-20_4.4x6.5mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-24_4.4x7.8mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT355-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 7.8,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.87,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 12,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-24_4.4x7.8mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-24_4.4x7.8mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-28_4.4x9.7mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT361-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 14,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-28_4.4x9.7mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-28_4.4x9.7mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-32_6.1x11mm_Pitch0.65mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT361-2.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 11.0,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.26,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-32_6.1x11mm_Pitch0.65mm', #modelName
        modelName ='TSSOP-32_6.1x11mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-38_4.4x9.7mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT510-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 9.7,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 19,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-38_4.4x9.7mm_Pitch0.5mm', #modelName
        modelName ='TSSOP-38_4.4x9.7mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-44_4.4x11.2mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mpds350b/mpds350b.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 11.1,       # body length
        E1 = 4.4,       # body width
        E = 6.4,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 22,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-44_4.4x11.2mm_Pitch0.5mm', #modelName
        modelName ='TSSOP-44_4.4x11.2mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-48_6.1x12.5mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ml/mpds350b/mpds350b.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 12.5,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 24,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-48_6.1x12.5mm_Pitch0.5mm', #modelName
        modelName ='TSSOP-48_6.1x12.5mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'TSSOP-56_6.1x14mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT364-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.95,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 28,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='TSSOP-56_6.1x14mm_Pitch0.5mm', #modelName
        modelName ='TSSOP-56_6.1x14mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'VSO-40_7.6x15.4mm_Pitch0.762mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT158-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.4,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 15.4,       # body length
        E1 = 7.6,       # body width
        E = 11.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.35,  # body height
        b = 0.36,  # pin width
        e = 0.762,  # pin (center-to-center) distance
        npx = 20,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='VSO-40_7.6x15.4mm_Pitch0.762mm', #modelName
        modelName ='VSO-40_7.6x15.4mm_P0.762mm', #modelName
        rotation = -90, # rotation if required
        ),
    'VSO-56_11.1x21.5mm_Pitch0.75mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT190-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.6,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.4,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 21.5,       # body length
        E1 = 11.0,       # body width
        E = 15.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.2,  # body-board separation
        A2 = 2.9,  # body height
        b = 0.36,  # pin width
        e = 0.75,  # pin (center-to-center) distance
        npx = 28,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='VSO-56_11.1x21.5mm_Pitch0.75mm', #modelName
        modelName ='VSO-56_11.1x21.5mm_P0.75mm', #modelName
        rotation = -90, # rotation if required
        ),
    'VSSOP-8_3.0x3.0mm_Pitch0.65mm': Params( # from http://www.ti.com/lit/ds/symlink/lm75b.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,      # top part of body is that much smaller
        c = 0.18,        # pin thickness, body center part height
        R1 = 0.05,       # pin upper corner, inner radius
        R2 = 0.05,       # pin lower corner, inner radius
        S = 0.05,        # pin top flat part length (excluding corner arc)
#        L = 0.6,        # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, 		 # 0.05,  # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25,      # 0.45 chamfer of the 1st pin corner
        D1 = 3.0,        # body length
        E1 = 3.0,        # body width
        E  = 4.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.25,       # body-board separation
        A2 = 1.1,        # body height
        b = 0.32,        # pin width
        e = 0.65,        # pin (center-to-center) distance
        npx = 4,         # number of pins along X axis (width)
        npy = 0,         # number of pins along y axis (length)
        epad = None,     # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='VSSOP-8_3.0x3.0mm_Pitch0.65mm', #modelName
        modelName ='VSSOP-8_3.0x3.0mm_P0.65mm', #modelName
        rotation = -90, # rotation if required
        ),
		'VSSOP-8_2.3x2mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT765-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.05,       # pin upper corner, inner radius
        R2 = 0.05,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 2.0,       # body length
        E1 = 2.3,       # body width
        E = 3.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.75,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='VSSOP-8_2.3x2mm_Pitch0.5mm', #modelName
        modelName ='VSSOP-8_2.3x2mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'VSSOP-8_2.4x2.1mm_Pitch0.5mm': Params( # from http://www.nxp.com/documents/outline_drawing/SOT765-1.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.05,       # pin upper corner, inner radius
        R2 = 0.05,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 2.1,       # body length
        E1 = 2.4,       # body width
        E = 3.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.75,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='VSSOP-8_2.4x2.1mm_Pitch0.5mm', #modelName
        modelName ='VSSOP-8_2.4x2.1mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
     'VSSOP-10_3x3mm_P0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/ads1115.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.05,       # pin upper corner, inner radius
        R2 = 0.05,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.05,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 3.0,       # body length
        E1 = 3.0,       # body width
        E = 4.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 5,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='VSSOP-10_3x3mm_Pitch0.5mm', #modelName
        modelName ='VSSOP-10_3x3mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
    'SOP-4_3.8x4.1mm_Pitch2.54mm': Params( # from http://www.ixysic.com/home/pdfs.nsf/www/CPC1017N.pdf/$file/CPC1017N.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.2,        # pin thickness, body center part height
        R1 = 0.15,       # pin upper corner, inner radius
        R2 = 0.15,       # pin lower corner, inner radius
        S = 0.25,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 4.089,       # body length
        E1 = 3.81,       # body width
        E = 6.096,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 2.0,  # body height
        b = 0.381,  # pin width
        e = 2.54,  # pin (center-to-center) distance
        npx = 2,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='SOP-4_3.8x4.1mm_Pitch2.54mm', #modelName
        modelName ='SOP-4_3.8x4.1mm_P2.54mm', #modelName
        rotation = -90, # rotation if required
        ),
    'HTSSOP-56-1EP_6.1x14mm_Pitch0.5mm': Params( # from http://www.ti.com/lit/ds/symlink/drv8301.pdf
        the = 12.0,      # body angle in degrees
        tb_s = 0.1,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.15,       # pin upper corner, inner radius
        R2 = 0.15,       # pin lower corner, inner radius
        S = 0.4,       # pin top flat part length (excluding corner arc)
#        L = 0.6,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.05,     # first pin indicator depth
        ef = 0, # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.25, #0.45 chamfer of the 1st pin corner
        D1 = 14.0,       # body length
        E1 = 6.1,       # body width
        E = 8.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.2,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 28,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (5.825, 3.23), # e Pad
        excluded_pins = None, #no pin excluded
        old_modelName ='HTSSOP-56-1EP_6.1x14mm_Pitch0.5mm', #modelName
        modelName ='HTSSOP-56-1EP_6.1x14mm_P0.5mm', #modelName
        rotation = -90, # rotation if required
        ),
}

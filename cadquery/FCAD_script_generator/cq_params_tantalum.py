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

destination_dir="/generated_cap/"
# destination_dir="./"

# body color
case_color=(244,164,96,0) # SandyBrown
#case_color=(255, 243, 128,0) # Corn Yellow
#case_color=(227,245,84,0)
#case_color = (50, 50, 50)
#pins_color = (230, 230, 230)
pins_color = (205,205,192)
#mark_color = (255,255,255) #white
#mark_color = (255,250,250) #snow
#mark_color = (255,255,240) #ivory
#mark_color = (207, 83, 0 ,0) #ghost white
mark_color = (207, 83, 0 ,0) #rusty orange
#max_cc1 = 1     # maximum size for 1st pin corner chamfer


# Mold angle (degrees) (not specified in datasheet)
ma_deg = 8

Params = namedtuple("Params", [
    'L',    # body overall length (including terminals)
    'W',    # body overall width
    'H',    # body overall height
    'F',    # width of each termination
    'S',    # length of each termination
    'B',    # beveling, measured as horizontal distance from end of cap
    'P',    # height off PCB where cutout begins (anode)
    'R',    # width of cutout (anode)
    'T',    # thickness of termination metal
    'G',    # length of bump underneath body
    'E',    # width of the bump underneath body
    'pml',  # pin mark lenght
    'modelName', #modelName
    'rotation', #rotation if required
    'dest_dir_prefix' #destination dir prefix
])

all_params_tantalum = {
    'A_3216_18': Params( # kemet Tantalum A 3216 H18
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 3.4,
        W = 1.8,
        H = 1.8,
        F = 1.2,
        S = 0.8,
        B = 0.4,
        P = 0.4,
        R = 0.4,
        T = 0.13,
        G = 1.1,
        E = 1.3,
        pml = 0.6,
        modelName = 'Tantalum_A_3216H18', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'B_3528_21': Params( # kemet Tantalum B 3528 H21
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 3.7,
        W = 3.0,
        H = 2.1,
        F = 2.2,
        S = 0.8,
        B = 0.4,
        P = 0.5,
        R = 1.0,
        T = 0.13,
        G = 1.8,
        E = 2.2,
        pml = 0.6,
        modelName = 'Tantalum_B_3528H21', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'C_6032_28': Params( # kemet Tantalum C 6032 H28
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 6.3,
        W = 3.5,
        H = 2.8,
        F = 2.2,
        S = 1.3,
        B = 0.5,
        P = 0.9,
        R = 1.0,
        T = 0.13,
        G = 2.8,
        E = 2.4,
        pml = 0.6,
        modelName = 'Tantalum_C_6032H28', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'D_7343_31': Params( # kemet Tantalum D 7343 H31
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 3.1,
        F = 2.4,
        S = 1.3,
        B = 0.5,
        P = 0.9,
        R = 1.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Tantalum_D_7343H31', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'X_7343_43': Params( # kemet Tantalum X 7343 H43
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 4.3,
        F = 2.4,
        S = 1.3,
        B = 0.5,
        P = 1.7,
        R = 1.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Tantalum_X_7343H43', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'E_7360_38': Params( # kemet Tantalum E 7360 H38
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 6.3,
        H = 3.8,
        F = 4.1,
        S = 1.3,
        B = 0.5,
        P = 1.2,
        R = 2.0,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Tantalum_E_7360H38', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'S_3216_12': Params( # kemet Tantalum S 3216 H12
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 3.4,
        W = 1.8,
        H = 1.2,
        F = 1.2,
        S = 0.8,
        B = 0.0,  #not beveling
        P = 0.0,
        R = 0.4,
        T = 0.13,
        G = 1.1,
        E = 1.3,
        pml = 0.6,
        modelName = 'Tantalum_S_3216H12', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'T_3528_12': Params( # kemet Tantalum T 3528 H12
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 3.7,
        W = 3.0,
        H = 1.2,
        F = 2.2,
        S = 0.8,
        B = 0.0,
        P = 0.0,
        R = 1.0,
        T = 0.13,
        G = 1.8,
        E = 2.2,
        pml = 0.6,
        modelName = 'Tantalum_T_3528H12', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'U_6032_15': Params( # kemet Tantalum U 6032 H15
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 6.3,
        W = 3.5,
        H = 1.5,
        F = 2.2,
        S = 1.3,
        B = 0.0,
        P = 0.0,
        R = 1.0,
        T = 0.13,
        G = 2.8,
        E = 2.4,
        pml = 0.6,
        modelName = 'Tantalum_U_6032H15', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'V_7343_20': Params( # kemet Tantalum W 7443 H20
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 7.6,
        W = 4.6,
        H = 2.0,
        F = 2.4,
        S = 1.3,
        B = 0.0, # not beveling
        P = 0.0, # not notching
        R = 0.9,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Tantalum_V_7443H15', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
    'W_7343_15': Params( # kemet Tantalum W 7343 H15
        # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
        # Length, width, height of the tantalum cap
        L = 7.3,
        W = 4.3,
        H = 1.5,
        F = 2.4,
        S = 1.3,
        B = 0.0,
        P = 0.0,
        R = 0.4,
        T = 0.13,
        G = 3.5,
        E = 3.5,
        pml = 1.2,
        modelName = 'Tantalum_W_7343H15', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = 'cap_tantalum'
        ),
}
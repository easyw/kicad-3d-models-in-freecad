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

use_nominal_size = True

destination_dir_old="/Capacitors_Tantalum_SMD.3dshapes"
destination_dir="/Capacitor_Tantalum_SMD.3dshapes"

rotation_plus_pin1 = 90
rotation_minus_pin1 =-90

rotation = rotation_plus_pin1

model_name_prefix = 'CP'
model_name_format_str_KLC3 = '{prefix:s}_EIA-{code_metric:s}_{code_letter:s}'
model_name_format_str_KLC2 = '{old_name:s}'
model_name_format_str_maui = '{maui_name:s}'

model_name_format_str = model_name_format_str_KLC3
# destination_dir="./"

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
])

# 'EIA-7260-38': Params( # kemet Tantalum E 7260 H38
#     # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
#     # Length, width, height of the tantalum cap
#     L = 7.2,
#     W = 6.0,
#     H = 3.8,
#     F = 4.1,
#     S = 1.3,
#     B = 0.5,
#     P = 1.2,
#     R = 2.0,
#     T = 0.1,
#     G = 3.5,
#     E = 3.5,
#     pml = 1.2
#     ),


all_params = {
    'EIA-1608-08':{
        'modelName_old': 'CP_Tantalum_Case-J_EIA-1608-08', #modelName
        'modelName_maui': 'Tantalum_J_1608H08', #modelName
        'code_metric': '1608-08',
        'code_letter': 'AVX-J',
        'param_nominal': Params(
            # Dimensions per http://catalogs.avx.com/TantalumNiobium.pdf
            # serie TLC
            # Length, width, height of the tantalum cap
            L = 1.6,
            W = 0.85,
            H = 0.75,
            F = 0.85,
            S = 0.05,
            B = 0.0,  #not beveling
            P = 0.0,
            R = 0.0,
            T = 0.10,
            G = 0.5,
            E = 0.8,
            pml = 0.3
            ),
        'param_max': None
    },
    'EIA-1608-10':{
        'modelName_old': 'CP_Tantalum_Case-L_EIA-1608-10', #modelName
        'modelName_maui': 'Tantalum_L_1608H10', #modelName
        'code_metric': '1608-10',
        'code_letter': 'AVX-L',
        'param_nominal': Params(
            # Dimensions per http://catalogs.avx.com/TantalumNiobium.pdf
            # serie TLC
            # Length, width, height of the tantalum cap
            L = 1.6,
            W = 0.85,
            H = 0.85,
            F = 0.85,
            S = 0.05,
            B = 0.0,  #not beveling
            P = 0.0,
            R = 0.0,
            T = 0.10,
            G = 0.5,
            E = 0.8,
            pml = 0.3
            ),
        'param_max': None
    },
    'EIA-2012-12':{
        'modelName_old': 'CP_Tantalum_Case-R_EIA-2012-12', #modelName
        'modelName_maui': 'Tantalum_R_2012H12', #modelName
        'code_metric': '2012-12',
        'code_letter': 'Kemet-R',
        'param_nominal': Params(
            # Length, width, height of the tantalum cap
            L = 2.0,
            W = 1.2,
            H = 1.2,
            F = 0.9,
            S = 0.6,
            B = 0.0,  #not beveling
            P = 0.0,
            R = 0.0,
            T = 0.13,
            G = 0.5,
            E = 0.8,
            pml = 0.4
            ),
        'param_max': None
    },
    'EIA-2012-15':{
        'modelName_old': 'CP_Tantalum_Case-P_EIA-2012-15', #modelName
        'modelName_maui': 'Tantalum_P_2012H15', #modelName
        'code_metric': '2012-15',
        'code_letter': 'AVX-P',
        'param_nominal': Params(
            # Dimensions per http://catalogs.avx.com/TantalumNiobium.pdf
            # serie TLC
            # Length, width, height of the tantalum cap
            L = 2.05,
            W = 1.35,
            H = 1.50,
            F = 1.00,
            S = 0.15,
            B = 0.0,  #not beveling
            P = 0.5,
            R = 0.5,
            T = 0.10,
            G = 0.5,
            E = 0.8,
            pml = 0.3
            ),
        'param_max': None
    },
    'EIA-3216-10':{
        'modelName_old': 'CP_Tantalum_Case-I_EIA-3216-10', #modelName
        'modelName_maui': 'Tantalum_I_3216H10', #modelName
        'code_metric': '3216-10',
        'code_letter': 'Kemet-I',
        'param_nominal': Params( # kemet Tantalum S 3216 H12
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
            pml = 0.6
            ),
        'param_max': None
    },
    'EIA-3216-12':{
        'modelName_old': 'CP_Tantalum_Case-S_EIA-3216-12', #modelName
        'modelName_maui': 'Tantalum_S_3216H12', #modelName
        'code_metric': '3216-12',
        'code_letter': 'Kemet-S',
        'param_nominal': Params( # kemet Tantalum S 3216 H12
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
            pml = 0.6
            ),
        'param_max': Params( # kemet Tantalum S 3216 H12
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
            pml = 0.6
            )
    },
    'EIA-3216-18':{
        'modelName_old': 'CP_Tantalum_Case-A_EIA-3216-18', #modelName
        'modelName_maui': 'Tantalum_A_3216H18', #modelName
        'code_metric': '3216-18',
        'code_letter': 'Kemet-A',
        'param_nominal': Params( # kemet Tantalum A 3216 H18
            # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
            # Length, width, height of the tantalum cap
            L = 3.2,
            W = 1.6,
            H = 1.8,
            F = 1.2,
            S = 0.8,
            B = 0.4,
            P = 0.4,
            R = 0.4,
            T = 0.13,
            G = 1.1,
            E = 1.3,
            pml = 0.6
            ),
        'param_max': Params( # kemet Tantalum A 3216 H18
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
            pml = 0.6
            )
    },
    'EIA-3528-12':{
        'modelName_old': 'CP_Tantalum_Case-T_EIA-3528-12', #modelName
        'modelName_maui': 'Tantalum_T_3528H12', #modelName
        'code_metric': '3528-12',
        'code_letter': 'Kemet-T',
        'param_nominal': Params( # kemet Tantalum T 3528 H12
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
            pml = 0.6
            ),
        'param_max': Params( # kemet Tantalum T 3528 H12
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
            pml = 0.6
            )
    },
    'EIA-3528-15':{
        'modelName_old': 'CP_Tantalum_Case-H_EIA-3528-15', #modelName
        'modelName_maui': 'Tantalum_H_3528H15', #modelName
        'code_metric': '3528-15',
        'code_letter': 'AVX-H',
        'param_nominal': Params(
            # Dimensions per http://catalogs.avx.com/TantalumNiobium.pdf
            # serie TAJ
            # Length, width, height of the tantalum cap
            L = 3.50,
            W = 2.80,
            H = 1.50,
            F = 1.50,
            S = 0.15,
            B = 0.5,
            P = 0.9,
            R = 1.0,
            T = 0.13,
            G = 2.8,
            E = 2.4,
            pml = 0.6
            ),
        'param_max': None
    },
    'EIA-3528-21':{
        'modelName_old': 'CP_Tantalum_Case-B_EIA-3528-21', #modelName
        'modelName_maui': 'Tantalum_B_3528H21', #modelName
        'code_metric': '3528-21',
        'code_letter': 'Kemet-B',
        'param_nominal': Params( # kemet Tantalum B 3528 H21
            # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
            # Length, width, height of the tantalum cap
            L = 3.5,
            W = 2.8,
            H = 2.1,
            F = 2.2,
            S = 0.8,
            B = 0.4,
            P = 0.5,
            R = 1.0,
            T = 0.13,
            G = 1.8,
            E = 2.2,
            pml = 0.6
            ),
        'param_max': Params( # kemet Tantalum B 3528 H21
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
            pml = 0.6
            )
    },
    'EIA-6032-15':{
        'modelName_old': 'CP_Tantalum_Case-U_EIA-6032-15', #modelName
        'modelName_maui': 'Tantalum_U_6032H15', #modelName
        'code_metric': '6032-15',
        'code_letter': 'Kemet-U',
        'param_nominal':Params( # kemet Tantalum U 6032 H15
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
            pml = 0.6
            ),
        'param_max': Params( # kemet Tantalum U 6032 H15
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
            pml = 0.6
            )
    },
    'EIA-6032-20':{
        'modelName_old': 'CP_Tantalum_Case-F_EIA-6032-20', #modelName
        'modelName_maui': 'Tantalum_F_6032H20', #modelName
        'code_metric': '6032-20',
        'code_letter': 'AVX-F',
        'param_nominal': Params( # kemet Tantalum C 6032 H28
            # Dimensions per http://partbuilder.avx.com/p/pb/pdf/TAJ_LOW_PROFILE.pdf
            # This is not the actual AVX-F serie but the TAJ, becaouse 6032-20 in serie AVX-F seems nowhere to find
            # Length, width, height of the tantalum cap
            L = 6.0,
            W = 3.2,
            H = 2.0,
            F = 2.2,
            S = 2.9,
            B = 0.0,
            P = 0.0,
            R = 1.0,
            T = 0.13,
            G = 2.8,
            E = 2.4,
            pml = 0.6
            ),
        'param_max': None
    },
    'EIA-6032-28':{
        'modelName_old': 'CP_Tantalum_Case-C_EIA-6032-28', #modelName
        'modelName_maui': 'Tantalum_C_6032H28', #modelName
        'code_metric': '6032-28',
        'code_letter': 'Kemet-C',
        'param_nominal': Params( # kemet Tantalum C 6032 H28
            # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
            # Length, width, height of the tantalum cap
            L = 6.0,
            W = 3.2,
            H = 2.8,
            F = 2.2,
            S = 1.3,
            B = 0.5,
            P = 0.9,
            R = 1.0,
            T = 0.13,
            G = 2.8,
            E = 2.4,
            pml = 0.6
            ),
        'param_max': Params( # kemet Tantalum C 6032 H28
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
            pml = 0.6
            )
    },
    'EIA-7343-15':{
        'modelName_old': 'CP_Tantalum_Case-W_EIA-7343-15', #modelName
        'modelName_maui': 'Tantalum_W_7343H15', #modelName
        'code_metric': '7343-15',
        'code_letter': 'Kemet-W',
        'param_nominal': None,
        'param_max': Params( # kemet Tantalum W 7343 H15
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
            pml = 1.2
            )
    },
    'EIA-7343-20':{
        'modelName_old': 'CP_Tantalum_Case-V_EIA-7343-20', #modelName
        'modelName_maui': 'Tantalum_V_7343H20', #modelName
        'code_metric': '7343-20',
        'code_letter': 'Kemet-V',
        'param_nominal': Params( # kemet Tantalum W 7343 H20
            # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
            # Length, width, height of the tantalum cap
            L = 7.5,
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
            pml = 1.2
            ),
        'param_max': Params( # kemet Tantalum W 7443 H20
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
            pml = 1.2
            )
    },
    'EIA-7343-30':{
        'modelName_old': 'CP_Tantalum_Case-N_EIA-7343-30', #modelName
        'modelName_maui': 'Tantalum_N_7343H30', #modelName
        'code_metric': '7343-30',
        'code_letter': 'AVX-N',
        'param_nominal': Params(
            # Dimensions per http://catalogs.avx.com/TantalumNiobium.pdf
            # serie F93
            # Length, width, height of the tantalum cap
            L = 7.30,
            W = 4.30,
            H = 2.80,
            F = 2.40,
            S = 1.30,
            B = 0.0, # not beveling
            P = 0.9,
            R = 1.0,
            T = 0.13,
            G = 2.8,
            E = 2.4,
            pml = 0.6
            ),
        'param_max': None
    },
    'EIA-7343-31':{
        'modelName_old': 'CP_Tantalum_Case-D_EIA-7343-31', #modelName
        'modelName_maui': 'Tantalum_D_7343H31', #modelName
        'code_metric': '7343-31',
        'code_letter': 'Kemet-D',
        'param_nominal': Params( # kemet Tantalum D 7343 H31
            # Dimensions per http://www.kemet.com/Lists/ProductCatalog/Attachments/253/KEM_TC101_STD.pdf
            # Length, width, height of the tantalum cap
            L = 7.3,
            W = 4.3,
            H = 3.1,
            F = 2.4,
            S = 1.3,
            B = 0.5,
            P = 0.9,
            R = 1.0,
            T = 0.13,
            G = 3.5,
            E = 3.5,
            pml = 1.2
            ),
        'param_max': Params( # kemet Tantalum D 7343 H31
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
            pml = 1.2
            )
    },
    'EIA-7343-40':{
        'modelName_old': 'CP_Tantalum_Case-Y_EIA-7343-43', #modelName
        'modelName_maui': 'Tantalum_X_7343H43', #modelName
        'code_metric': '7343-40',
        'code_letter': 'Kemet-Y',
        'param_nominal': Params( # kemet Tantalum Y
            # Dimensions per https://content.kemet.com/datasheets/KEM_T2076_T52X-530.pdf
            # Length, width, height of the tantalum cap
            L = 7.3,
            W = 4.3,
            H = 3.8,
            F = 2.4,
            S = 1.3,
            B = 0.5,
            P = 1.5,
            R = 1.0,
            T = 0.13,
            G = 3.5,
            E = 3.5,
            pml = 1.2
            ),
        'param_max': None
    },
    'EIA-7343-43':{
        'modelName_old': 'CP_Tantalum_Case-X_EIA-7343-43', #modelName
        'modelName_maui': 'Tantalum_X_7343H43', #modelName
        'code_metric': '7343-43',
        'code_letter': 'Kemet-X',
        'param_nominal': Params( # kemet Tantalum X 7343 H43
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
            pml = 1.2
            ),
        'param_max': Params( # kemet Tantalum X 7343 H43
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
            pml = 1.2
            )
    },
    'EIA-7360-38':{
        'modelName_old': 'CP_Tantalum_Case-E_EIA-7360-38', #modelName
        'modelName_maui': 'Tantalum_E_7360H38', #modelName
        'code_metric': '7360-38',
        'code_letter': 'Kemet-E',
        'param_nominal': None,
        'param_max': Params( # kemet Tantalum E 7360 H38
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
            pml = 1.2
            )
    },
    'EIA-7361-38':{
        'modelName_old': 'CP_Tantalum_Case-V_EIA-7343-38', #modelName
        'modelName_maui': 'Tantalum_V_7343H38', #modelName
        'code_metric': '7361-38',
        'code_letter': 'AVX-V',
        'param_nominal': Params(
            # Dimensions per http://catalogs.avx.com/TantalumNiobium.pdf
            # serie TAJ
            # Length, width, height of the tantalum cap
            L = 7.3,
            W = 6.10,
            H = 3.55,
            F = 3.10,
            S = 1.30,
            B = 0.0,  #not beveling
            P = 1.0,
            R = 2.0,
            T = 0.10,
            G = 4.40,
            E = 4.40,
            pml = 2.0
            ),
        'param_max': None
    },
    'EIA-7361-438':{
        'modelName_old': 'CP_Tantalum_Case-U_EIA-7343-438', #modelName
        'modelName_maui': 'Tantalum_U_7343H438', #modelName
        'code_metric': '7361-438',
        'code_letter': 'AVX-U',
        'param_nominal': Params(
            # Dimensions per http://catalogs.avx.com/TantalumNiobium.pdf
            # serie TAJ 
            # the foot print 7361-438 exist but the casing does not, so the 7361-43 is used
            # Length, width, height of the tantalum cap
            L = 7.3,
            W = 6.10,
            H = 4.10,
            F = 3.10,
            S = 1.30,
            B = 0.0,  #not beveling
            P = 1.0,
            R = 2.0,
            T = 0.10,
            G = 4.40,
            E = 4.40,
            pml = 2.0
            ),
        'param_max': None
    },
}

from collections import namedtuple

destination_dir = "/generated_diode/"
# destination_dir="./"

# body color
case_color = (26,  26,  26)
# case_color = (50,  50,  50)
# pins_color = (230,  230,  230)
pins_color = (205,  205,  192)
# mark_color = (255, 255, 255)  #white
# mark_color = (255, 250, 250)  #snow
# mark_color = (255, 255, 240)  #ivory
mark_color = (248,  248,  255)  # ghost white


Params = namedtuple("Params", [
    'pml',
    'c',
    'the',
    'tb_s',
    'ef',
    'cc1',
    'fp_r',
    'fp_d',
    'fp_z',
    'R1',
    'R2',
    'S',
    'D1',
    'E1',
    'E',
    'A1',
    'A2',
    'b',
    'e',
    'npx',
    'npy',
    'mN',
    'rot',
    'dest_dir_pref'
])

all_params_diode = {
    'A_3216_18': Params(  # kemet Tantalum A 3216 H18
        pml=0.1,
        c=0.1,  # pin thickness, body center part height
        the=8,  # body angle in degrees
        tb_s=0.15, # top part of body is that much smaller
        ef=0.05,  # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        cc1=0,  # 0.45 chamfer of the 1st pin corner
        fp_r=0,  # first pin indicator radius
        fp_d=0,  # first pin indicator distance from edge
        fp_z=0,   # first pin indicator depth
        R1=0.1,  # pin upper corner, inner radius
        R2=0.1,  # pin lower corner, inner radius
        S=0.2,   # pin top flat part length (excluding corner arc)
        # automatically calculated    L  = params.L
        D1=3,  # body length
        E1=1.5,  # body width
        E=1.5,  # body overall width  E=E1+2*(S+L+c)
        A1=0.1,  # body-board separation
        A2=1.5,  # body height
        b=0.5,  # pin width
        e=0,  # pin (center-to-center) distance
        npx=1,
        npy=0,
        mN='Name',
        rot=0,
        dest_dir_pref='diode'
        ),
  }
from collections import namedtuple

Params = namedtuple("Params",[
    'series_name',
    'file_name',
    'angled',
    'flanged',
    'num_pins',
    'pin_pitch',
    'mount_hole',
    'mount_hole_to_pin',
    'side_to_pin'
])

def generate_params(num_pins, series_name, pin_pitch, angled, flanged, mount_hole=False, mount_hole_to_pin=None, side_to_pin=None):

    return Params(
        series_name=series_name,
        file_name="PhoenixContact_" + series_name + "_01x" + ('%02d' % num_pins) + "_"\
        + ('%.2f' % pin_pitch) + "mm_" + ('Angled' if angled else 'Vertical')\
        + ('_ThreadedFlange' + ('_MountHole' if mount_hole else '') if flanged else ''),
        angled=angled,
        flanged=flanged,
        num_pins=num_pins,
        pin_pitch=pin_pitch,
        mount_hole=mount_hole,
        mount_hole_to_pin=pin_pitch if mount_hole_to_pin is None else mount_hole_to_pin,
        side_to_pin=(3*pin_pitch if flanged else pin_pitch+2)/2.0 if side_to_pin is None else side_to_pin
    )


all_params = {
    ##################################################################################################################
    # Pin Pitch 5.00mm
    ##################################################################################################################
    'MSTBA_01x02_5.00mm' : generate_params( 2, "MSTBA", 5.0, True, False),
    'MSTBA_01x03_5.00mm' : generate_params( 3, "MSTBA", 5.0, True, False),
    'MSTBA_01x04_5.00mm' : generate_params( 4, "MSTBA", 5.0, True, False),
    'MSTBA_01x05_5.00mm' : generate_params( 5, "MSTBA", 5.0, True, False),
    'MSTBA_01x06_5.00mm' : generate_params( 6, "MSTBA", 5.0, True, False),
    'MSTBA_01x07_5.00mm' : generate_params( 7, "MSTBA", 5.0, True, False),
    'MSTBA_01x08_5.00mm' : generate_params( 8, "MSTBA", 5.0, True, False),
    'MSTBA_01x09_5.00mm' : generate_params( 9, "MSTBA", 5.0, True, False),
    'MSTBA_01x10_5.00mm' : generate_params(10, "MSTBA", 5.0, True, False),
    'MSTBA_01x11_5.00mm' : generate_params(11, "MSTBA", 5.0, True, False),
    'MSTBA_01x12_5.00mm' : generate_params(12, "MSTBA", 5.0, True, False),
    'MSTBA_01x13_5.00mm' : generate_params(13, "MSTBA", 5.0, True, False),
    'MSTBA_01x14_5.00mm' : generate_params(14, "MSTBA", 5.0, True, False),
    'MSTBA_01x15_5.00mm' : generate_params(15, "MSTBA", 5.0, True, False),
    'MSTBA_01x16_5.00mm' : generate_params(16, "MSTBA", 5.0, True, False),
    ###################################################################################################################
    'MSTB_01x02_5.00mm' : generate_params( 2, "MSTB", 5.0, True, True),
    'MSTB_01x03_5.00mm' : generate_params( 3, "MSTB", 5.0, True, True),
    'MSTB_01x04_5.00mm' : generate_params( 4, "MSTB", 5.0, True, True),
    'MSTB_01x05_5.00mm' : generate_params( 5, "MSTB", 5.0, True, True),
    'MSTB_01x06_5.00mm' : generate_params( 6, "MSTB", 5.0, True, True),
    'MSTB_01x07_5.00mm' : generate_params( 7, "MSTB", 5.0, True, True),
    'MSTB_01x08_5.00mm' : generate_params( 8, "MSTB", 5.0, True, True),
    'MSTB_01x09_5.00mm' : generate_params( 9, "MSTB", 5.0, True, True),
    'MSTB_01x10_5.00mm' : generate_params(10, "MSTB", 5.0, True, True),
    'MSTB_01x11_5.00mm' : generate_params(11, "MSTB", 5.0, True, True),
    'MSTB_01x12_5.00mm' : generate_params(12, "MSTB", 5.0, True, True),
    'MSTB_01x13_5.00mm' : generate_params(13, "MSTB", 5.0, True, True),
    'MSTB_01x14_5.00mm' : generate_params(14, "MSTB", 5.0, True, True),
    'MSTB_01x15_5.00mm' : generate_params(15, "MSTB", 5.0, True, True),
    'MSTB_01x16_5.00mm' : generate_params(16, "MSTB", 5.0, True, True),
    ###################################################################################################################
    'MSTB_01x02_5.00mm_MH' : generate_params( 2, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x03_5.00mm_MH' : generate_params( 3, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x04_5.00mm_MH' : generate_params( 4, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x05_5.00mm_MH' : generate_params( 5, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x06_5.00mm_MH' : generate_params( 6, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x07_5.00mm_MH' : generate_params( 7, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x08_5.00mm_MH' : generate_params( 8, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x09_5.00mm_MH' : generate_params( 9, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x10_5.00mm_MH' : generate_params(10, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x11_5.00mm_MH' : generate_params(11, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x12_5.00mm_MH' : generate_params(12, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x13_5.00mm_MH' : generate_params(13, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x14_5.00mm_MH' : generate_params(14, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x15_5.00mm_MH' : generate_params(15, "MSTB", 5.0, True, True, mount_hole=True),
    'MSTB_01x16_5.00mm_MH' : generate_params(16, "MSTB", 5.0, True, True, mount_hole=True),
    ###################################################################################################################
    'MSTBVA_01x02_5.00mm' : generate_params( 2, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x03_5.00mm' : generate_params( 3, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x04_5.00mm' : generate_params( 4, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x05_5.00mm' : generate_params( 5, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x06_5.00mm' : generate_params( 6, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x07_5.00mm' : generate_params( 7, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x08_5.00mm' : generate_params( 8, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x09_5.00mm' : generate_params( 9, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x10_5.00mm' : generate_params(10, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x11_5.00mm' : generate_params(11, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x12_5.00mm' : generate_params(12, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x13_5.00mm' : generate_params(13, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x14_5.00mm' : generate_params(14, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x15_5.00mm' : generate_params(15, "MSTBVA", 5.0, False, False),
    'MSTBVA_01x16_5.00mm' : generate_params(16, "MSTBVA", 5.0, False, False),
    ###################################################################################################################
    'MSTBV_01x02_5.00mm' : generate_params( 2, "MSTBV", 5.0, False, True),
    'MSTBV_01x03_5.00mm' : generate_params( 3, "MSTBV", 5.0, False, True),
    'MSTBV_01x04_5.00mm' : generate_params( 4, "MSTBV", 5.0, False, True),
    'MSTBV_01x05_5.00mm' : generate_params( 5, "MSTBV", 5.0, False, True),
    'MSTBV_01x06_5.00mm' : generate_params( 6, "MSTBV", 5.0, False, True),
    'MSTBV_01x07_5.00mm' : generate_params( 7, "MSTBV", 5.0, False, True),
    'MSTBV_01x08_5.00mm' : generate_params( 8, "MSTBV", 5.0, False, True),
    'MSTBV_01x09_5.00mm' : generate_params( 9, "MSTBV", 5.0, False, True),
    'MSTBV_01x10_5.00mm' : generate_params(10, "MSTBV", 5.0, False, True),
    'MSTBV_01x11_5.00mm' : generate_params(11, "MSTBV", 5.0, False, True),
    'MSTBV_01x12_5.00mm' : generate_params(12, "MSTBV", 5.0, False, True),
    'MSTBV_01x13_5.00mm' : generate_params(13, "MSTBV", 5.0, False, True),
    'MSTBV_01x14_5.00mm' : generate_params(14, "MSTBV", 5.0, False, True),
    'MSTBV_01x15_5.00mm' : generate_params(15, "MSTBV", 5.0, False, True),
    'MSTBV_01x16_5.00mm' : generate_params(16, "MSTBV", 5.0, False, True),
    ###################################################################################################################
    'MSTBV_01x02_5.00mm_MH' : generate_params( 2, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x03_5.00mm_MH' : generate_params( 3, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x04_5.00mm_MH' : generate_params( 4, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x05_5.00mm_MH' : generate_params( 5, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x06_5.00mm_MH' : generate_params( 6, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x07_5.00mm_MH' : generate_params( 7, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x08_5.00mm_MH' : generate_params( 8, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x09_5.00mm_MH' : generate_params( 9, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x10_5.00mm_MH' : generate_params(10, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x11_5.00mm_MH' : generate_params(11, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x12_5.00mm_MH' : generate_params(12, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x13_5.00mm_MH' : generate_params(13, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x14_5.00mm_MH' : generate_params(14, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x15_5.00mm_MH' : generate_params(15, "MSTBV", 5.0, False, True, mount_hole=True),
    'MSTBV_01x16_5.00mm_MH' : generate_params(16, "MSTBV", 5.0, False, True, mount_hole=True),
    ##################################################################################################################
    # Pin Pitch 5.08mm
    ##################################################################################################################
    'MSTBA_01x02_5.08mm' : generate_params( 2, "MSTBA", 5.08, True, False),
    'MSTBA_01x03_5.08mm' : generate_params( 3, "MSTBA", 5.08, True, False),
    'MSTBA_01x04_5.08mm' : generate_params( 4, "MSTBA", 5.08, True, False),
    'MSTBA_01x05_5.08mm' : generate_params( 5, "MSTBA", 5.08, True, False),
    'MSTBA_01x06_5.08mm' : generate_params( 6, "MSTBA", 5.08, True, False),
    'MSTBA_01x07_5.08mm' : generate_params( 7, "MSTBA", 5.08, True, False),
    'MSTBA_01x08_5.08mm' : generate_params( 8, "MSTBA", 5.08, True, False),
    'MSTBA_01x09_5.08mm' : generate_params( 9, "MSTBA", 5.08, True, False),
    'MSTBA_01x10_5.08mm' : generate_params(10, "MSTBA", 5.08, True, False),
    'MSTBA_01x11_5.08mm' : generate_params(11, "MSTBA", 5.08, True, False),
    'MSTBA_01x12_5.08mm' : generate_params(12, "MSTBA", 5.08, True, False),
    'MSTBA_01x13_5.08mm' : generate_params(13, "MSTBA", 5.08, True, False),
    'MSTBA_01x14_5.08mm' : generate_params(14, "MSTBA", 5.08, True, False),
    'MSTBA_01x15_5.08mm' : generate_params(15, "MSTBA", 5.08, True, False),
    'MSTBA_01x16_5.08mm' : generate_params(16, "MSTBA", 5.08, True, False),
    ###################################################################################################################
    'MSTB_01x02_5.08mm' : generate_params( 2, "MSTB", 5.08, True, True),
    'MSTB_01x03_5.08mm' : generate_params( 3, "MSTB", 5.08, True, True),
    'MSTB_01x04_5.08mm' : generate_params( 4, "MSTB", 5.08, True, True),
    'MSTB_01x05_5.08mm' : generate_params( 5, "MSTB", 5.08, True, True),
    'MSTB_01x06_5.08mm' : generate_params( 6, "MSTB", 5.08, True, True),
    'MSTB_01x07_5.08mm' : generate_params( 7, "MSTB", 5.08, True, True),
    'MSTB_01x08_5.08mm' : generate_params( 8, "MSTB", 5.08, True, True),
    'MSTB_01x09_5.08mm' : generate_params( 9, "MSTB", 5.08, True, True),
    'MSTB_01x10_5.08mm' : generate_params(10, "MSTB", 5.08, True, True),
    'MSTB_01x11_5.08mm' : generate_params(11, "MSTB", 5.08, True, True),
    'MSTB_01x12_5.08mm' : generate_params(12, "MSTB", 5.08, True, True),
    'MSTB_01x13_5.08mm' : generate_params(13, "MSTB", 5.08, True, True),
    'MSTB_01x14_5.08mm' : generate_params(14, "MSTB", 5.08, True, True),
    'MSTB_01x15_5.08mm' : generate_params(15, "MSTB", 5.08, True, True),
    'MSTB_01x16_5.08mm' : generate_params(16, "MSTB", 5.08, True, True),
    ###################################################################################################################
    'MSTB_01x02_5.08mm_MH' : generate_params( 2, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x03_5.08mm_MH' : generate_params( 3, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x04_5.08mm_MH' : generate_params( 4, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x05_5.08mm_MH' : generate_params( 5, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x06_5.08mm_MH' : generate_params( 6, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x07_5.08mm_MH' : generate_params( 7, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x08_5.08mm_MH' : generate_params( 8, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x09_5.08mm_MH' : generate_params( 9, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x10_5.08mm_MH' : generate_params(10, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x11_5.08mm_MH' : generate_params(11, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x12_5.08mm_MH' : generate_params(12, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x13_5.08mm_MH' : generate_params(13, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x14_5.08mm_MH' : generate_params(14, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x15_5.08mm_MH' : generate_params(15, "MSTB", 5.08, True, True, mount_hole=True),
    'MSTB_01x16_5.08mm_MH' : generate_params(16, "MSTB", 5.08, True, True, mount_hole=True),
    ###################################################################################################################
    'MSTBVA_01x02_5.08mm' : generate_params( 2, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x03_5.08mm' : generate_params( 3, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x04_5.08mm' : generate_params( 4, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x05_5.08mm' : generate_params( 5, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x06_5.08mm' : generate_params( 6, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x07_5.08mm' : generate_params( 7, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x08_5.08mm' : generate_params( 8, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x09_5.08mm' : generate_params( 9, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x10_5.08mm' : generate_params(10, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x11_5.08mm' : generate_params(11, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x12_5.08mm' : generate_params(12, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x13_5.08mm' : generate_params(13, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x14_5.08mm' : generate_params(14, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x15_5.08mm' : generate_params(15, "MSTBVA", 5.08, False, False),
    'MSTBVA_01x16_5.08mm' : generate_params(16, "MSTBVA", 5.08, False, False),
    ###################################################################################################################
    'MSTBV_01x02_5.08mm' : generate_params( 2, "MSTBV", 5.08, False, True),
    'MSTBV_01x03_5.08mm' : generate_params( 3, "MSTBV", 5.08, False, True),
    'MSTBV_01x04_5.08mm' : generate_params( 4, "MSTBV", 5.08, False, True),
    'MSTBV_01x05_5.08mm' : generate_params( 5, "MSTBV", 5.08, False, True),
    'MSTBV_01x06_5.08mm' : generate_params( 6, "MSTBV", 5.08, False, True),
    'MSTBV_01x07_5.08mm' : generate_params( 7, "MSTBV", 5.08, False, True),
    'MSTBV_01x08_5.08mm' : generate_params( 8, "MSTBV", 5.08, False, True),
    'MSTBV_01x09_5.08mm' : generate_params( 9, "MSTBV", 5.08, False, True),
    'MSTBV_01x10_5.08mm' : generate_params(10, "MSTBV", 5.08, False, True),
    'MSTBV_01x11_5.08mm' : generate_params(11, "MSTBV", 5.08, False, True),
    'MSTBV_01x12_5.08mm' : generate_params(12, "MSTBV", 5.08, False, True),
    'MSTBV_01x13_5.08mm' : generate_params(13, "MSTBV", 5.08, False, True),
    'MSTBV_01x14_5.08mm' : generate_params(14, "MSTBV", 5.08, False, True),
    'MSTBV_01x15_5.08mm' : generate_params(15, "MSTBV", 5.08, False, True),
    'MSTBV_01x16_5.08mm' : generate_params(16, "MSTBV", 5.08, False, True),
    ###################################################################################################################
    'MSTBV_01x02_5.08mm_MH' : generate_params( 2, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x03_5.08mm_MH' : generate_params( 3, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x04_5.08mm_MH' : generate_params( 4, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x05_5.08mm_MH' : generate_params( 5, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x06_5.08mm_MH' : generate_params( 6, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x07_5.08mm_MH' : generate_params( 7, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x08_5.08mm_MH' : generate_params( 8, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x09_5.08mm_MH' : generate_params( 9, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x10_5.08mm_MH' : generate_params(10, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x11_5.08mm_MH' : generate_params(11, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x12_5.08mm_MH' : generate_params(12, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x13_5.08mm_MH' : generate_params(13, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x14_5.08mm_MH' : generate_params(14, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x15_5.08mm_MH' : generate_params(15, "MSTBV", 5.08, False, True, mount_hole=True),
    'MSTBV_01x16_5.08mm_MH' : generate_params(16, "MSTBV", 5.08, False, True, mount_hole=True),
    ##################################################################################################################
    # High Voltage Versions (pin pitch 7.5mm)
    ##################################################################################################################
    'GMSTBA_01x02_7.50mm' : generate_params( 2, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x03_7.50mm' : generate_params( 3, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x04_7.50mm' : generate_params( 4, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x05_7.50mm' : generate_params( 5, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x06_7.50mm' : generate_params( 6, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x07_7.50mm' : generate_params( 7, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x08_7.50mm' : generate_params( 8, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x09_7.50mm' : generate_params( 9, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x10_7.50mm' : generate_params(10, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x11_7.50mm' : generate_params(11, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    'GMSTBA_01x12_7.50mm' : generate_params(12, "GMSTBA", 7.50, True, False, side_to_pin=3.75),
    ##################################################################################################################
    'GMSTBVA_01x02_7.50mm' : generate_params( 2, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x03_7.50mm' : generate_params( 3, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x04_7.50mm' : generate_params( 4, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x05_7.50mm' : generate_params( 5, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x06_7.50mm' : generate_params( 6, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x07_7.50mm' : generate_params( 7, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x08_7.50mm' : generate_params( 8, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x09_7.50mm' : generate_params( 9, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x10_7.50mm' : generate_params(10, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x11_7.50mm' : generate_params(11, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    'GMSTBVA_01x12_7.50mm' : generate_params(12, "GMSTBVA", 7.50, False, False, side_to_pin=3.75),
    ##################################################################################################################
    # High Voltage Versions (pin pitch 7.62mm)
    ##################################################################################################################
    'GMSTBA_01x02_7.62mm' : generate_params( 2, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x03_7.62mm' : generate_params( 3, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x04_7.62mm' : generate_params( 4, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x05_7.62mm' : generate_params( 5, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x06_7.62mm' : generate_params( 6, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x07_7.62mm' : generate_params( 7, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x08_7.62mm' : generate_params( 8, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x09_7.62mm' : generate_params( 9, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x10_7.62mm' : generate_params(10, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x11_7.62mm' : generate_params(11, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    'GMSTBA_01x12_7.62mm' : generate_params(12, "GMSTBA", 7.62, True, False, side_to_pin=3.81),
    ###################################################################################################################
    'GMSTB_01x02_7.62mm' : generate_params( 2, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x03_7.62mm' : generate_params( 3, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x04_7.62mm' : generate_params( 4, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x05_7.62mm' : generate_params( 5, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x06_7.62mm' : generate_params( 6, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x07_7.62mm' : generate_params( 7, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x08_7.62mm' : generate_params( 8, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x09_7.62mm' : generate_params( 9, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x10_7.62mm' : generate_params(10, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x11_7.62mm' : generate_params(11, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x12_7.62mm' : generate_params(12, "GMSTB", 7.62, True, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    ###################################################################################################################
    'GMSTB_01x02_7.62mm_MH' : generate_params( 2, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x03_7.62mm_MH' : generate_params( 3, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x04_7.62mm_MH' : generate_params( 4, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x05_7.62mm_MH' : generate_params( 5, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x06_7.62mm_MH' : generate_params( 6, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x07_7.62mm_MH' : generate_params( 7, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x08_7.62mm_MH' : generate_params( 8, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x09_7.62mm_MH' : generate_params( 9, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x10_7.62mm_MH' : generate_params(10, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x11_7.62mm_MH' : generate_params(11, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTB_01x12_7.62mm_MH' : generate_params(12, "GMSTB", 7.62, True, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    ###################################################################################################################
    'GMSTBVA_01x02_7.62mm' : generate_params( 2, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x03_7.62mm' : generate_params( 3, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x04_7.62mm' : generate_params( 4, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x05_7.62mm' : generate_params( 5, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x06_7.62mm' : generate_params( 6, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x07_7.62mm' : generate_params( 7, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x08_7.62mm' : generate_params( 8, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x09_7.62mm' : generate_params( 9, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x10_7.62mm' : generate_params(10, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x11_7.62mm' : generate_params(11, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    'GMSTBVA_01x12_7.62mm' : generate_params(12, "GMSTBVA", 7.62, False, False, side_to_pin=3.81),
    ###################################################################################################################
    'GMSTBV_01x02_7.62mm' : generate_params( 2, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x03_7.62mm' : generate_params( 3, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x04_7.62mm' : generate_params( 4, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x05_7.62mm' : generate_params( 5, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x06_7.62mm' : generate_params( 6, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x07_7.62mm' : generate_params( 7, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x08_7.62mm' : generate_params( 8, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x09_7.62mm' : generate_params( 9, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x10_7.62mm' : generate_params(10, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x11_7.62mm' : generate_params(11, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x12_7.62mm' : generate_params(12, "GMSTBV", 7.62, False, True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    ###################################################################################################################
    'GMSTBV_01x02_7.62mm_MH' : generate_params( 2, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x03_7.62mm_MH' : generate_params( 3, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x04_7.62mm_MH' : generate_params( 4, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x05_7.62mm_MH' : generate_params( 5, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x06_7.62mm_MH' : generate_params( 6, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x07_7.62mm_MH' : generate_params( 7, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x08_7.62mm_MH' : generate_params( 8, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x09_7.62mm_MH' : generate_params( 9, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x10_7.62mm_MH' : generate_params(10, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x11_7.62mm_MH' : generate_params(11, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1),
    'GMSTBV_01x12_7.62mm_MH' : generate_params(12, "GMSTBV", 7.62, False, True, mount_hole=True, mount_hole_to_pin=6.1, side_to_pin=9.1)
}

class globalParams():
    pin_width = 1.0
    pin_depth = 4.0
    pin_inside_distance = 2.0
    pin_from_front_bottom = 3.8
    pin_bend_radius = 0.1
    pin_chamfer_long = 0.6
    pin_chamfer_short = 0.2
    pin_angled_from_back = 2.0

    body_width = 8.6
    body_height = 12.0


    plug_width = 5.3
    plug_arc_width = 5.9
    plug_arc_len = 4.0
    plug_front = pin_from_front_bottom-1.6
    plug_depth = 8.5

    body_lock_prodrudion = 1.0
    body_lock_height = 3.0
    body_lock_chamfer_h = 1.5
    body_lock_chamfer_d = 0.6
    body_lock_cutout_top_l = 2.0
    body_lock_cutout_bottom_l = 1.5

    thread_insert_r = 2.0
    thread_r = 1.0
    thread_depth = 5.0 # estimated


    pcb_thickness=1.5
    mount_screw_head_radius=2.0
    mount_screw_head_heigth=1.5
    mount_screw_fillet = 0.5
    mount_screw_slot_width = 0.6
    mount_screw_slot_depth = 0.8

#lock_cutout=

calcDim = namedtuple( 'calcDim',[
    'lenght', 'cutout_len', 'mount_hole_y', 'plug_left_side'
])

def dimensions(params):
    mount_hole_y = 2.5 if params.angled else 0.0
    lenght = (params.num_pins-1)*params.pin_pitch + 2*params.side_to_pin
    cutout_len = params.num_pins*params.pin_pitch-1.6 + (0 if params.pin_pitch>5.08 else 2)
    return calcDim(
        lenght = lenght
        ,mount_hole_y = 2.5 if params.angled else 0.0
        ,cutout_len = cutout_len
        ,plug_left_side = (lenght-cutout_len)/2.0-params.side_to_pin
    )

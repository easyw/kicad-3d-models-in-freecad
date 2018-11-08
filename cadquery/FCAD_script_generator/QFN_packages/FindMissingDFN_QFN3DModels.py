#
#
# Auto create DFN_QFN 3D models     version 1.0
#
# Script to scan SOIC foot print files and create 3D model paramters for those 3D models that 
# is missing in \Package_DFN_QFN.3dshapes
#
# This script scan all the foot print files , extract the 3D models file name 
# and check if the specified 3D model exists, if not, the script will create 
# the paramters for the 3D model in a cq_paramter.py file style.
# 
# It will assume different height of the package depedning on the body size
# It will assume the distance between the PCB and the body to 0.1 mm
#
# The script will use two different list, ExcludeModels and SpecialModels
#
# ExcludeModels list
# If a foot print file name is in the ExcludeModels list it will be ignored 
# For example the model is to complicated and need to be hand made or missing information 
# so the data sheet nmust be consulted manually 
#
# SpecialModels list
# If a 3D model name is in the SpecialModels list it will created with the paramters given 
# in the list regardless what it says in the foot print file
# For example the model is to complicated and need to be hand made or missing information 
# so the data sheet nmust be consulted manually 
#
# It will scan the FP file to find the desired name of the 3D model name
# It will scan the foot print file name to exctract body size, pad distance and, if present, 
# the epad size.
#
# The script will create two files MakeFindMissingXXX3DModels.sh and MissingXXX3DModels.txt
#
# MissingXXX3DModels.txt
# This file contain the content that should be appended to the ordinary cq_paramets.py file
#
# MakeFindMissingXXX3DModels.sh
# This batch file contain one line for each missing model, it will start FreeCad 
# with main_generator.py and the missing model as an argument.
#
# How to use this script
# 1)
# Execute this script like this 
# python FindMissingXXX3DModels.py
# 
# 2)
# append the content in MissingXXX3DModels.txt to cq_paramets.py
#
# 3)
# execute the MakeFindMissingXXXDModels.sh so all the 3D models is created with help of FreeCad
# ./MakeFindMissingXXX3DModels.sh
#

import sys
import math
import os
import subprocess 
import time
import datetime
from datetime import datetime as dt
import re
from pathlib import Path

DefaultA1 = 0.025
DefaultA2 = 0.75
DefaultA =  1.0
Defaultm =  0.0
Defaultb =  0.2


SkippingModelCnt = 0

#
# The path to foot print file directory in relation to where this script is placed
#
FPDir = '../../../../kicad-footprints/Package_DFN_QFN.pretty'
KISYS3DMOD = '../../../../kicad-packages3D'

#
# The name of the result files
#
ResultFile = 'MissingDFN_QFN3DModels.txt'
MakeAllfile = 'MakeFindMissingDFN_QFN3DModels.sh'
#
# The path to FreeCad, this path will be used in the MakeFindMissingXXX3DModels.sh script
#
FreeCadExe = '/c/users/stefan/Downloads/FreeCAD_0.17.11223_x64_dev_win/FreeCAD_0.17.11223_x64_dev_win/bin/FreeCAD.exe'
MainGenerator = 'main_generator.py '


MissingModels = []

#
# If a foot print file name is in the ExcludeModels list it will not be created
#
ExcludeModels =[
                    
                    'Mini-Circuits_FG873-4_3x3mm.kicad_mod',
                    'Infineon_PQFN-22-15-4EP_6x5mm_P0.65mm.kicad_mod',
                    'Infineon_PQFN-44-31-5EP_7x7mm_P0.5mm.kicad_mod',    
                    'Texas_MOF0009A.kicad_mod',
                    'Texas_RWH0032A.kicad_mod',
                    'Texas_RWH0032A_ThermalVias.kicad_mod',
                    'Texas_VQFN-RHL-20_ThermalVias',
                ]

#
# If a foot print file contian a model name (xxxx.wrl) that is in the SpecialModels list 
# it will will be created with those parameters given in the list
#
# model, D, E, e, b, L, m, npy, npx, excluded_pins
#
SpecialModels =[
                ['Nordic_AQFN-73-1EP_7x7mm_P0.5mm',     7.0,  7.0,    0.50,     0.200,   0.20,  0.0,   12,  12, "(3, 11, 12, 33, 35, 46, 47, 48)"],
                ['Mini-Circuits_DL805',                 3.25, 3.25,   0.66,     0.300,   0.20,  0.0,    1,  4,  "None"],
                ['ROHM_DFN0604-3',                      0.6,  0.4,    0.150,    0.050,   0.20,  0.0,    0,  3,  "(2,4,6)"],
                ['Diodes_DFN1006-3',                    1.0,  0.6,    0.225,    0.050,   0.20,  0.0,    0,  3,  "(2,4,6)"],
                ['DFN-14-1EP_3x4mm_Pitch0.5mm',         3.0,  4.0,    0.5,      0.200,   0.20,  0.0,    0,  7,  "None"],
                ['Linear_UGK52_QFN-46-52',              7.0,  8.0,    0.5,      0.200,   0.20,  0.0,   12, 14,  "(3, 37, 41, 45, 49, 51)"],
                ['QFN-16-1EP_4x4mm_Pitch0.65mm',        4.0,  4.0,    0.65,     0.250,   0.20,  0.0,    4,  4,  "None"],
                ['Qorvo_DFN-8-1EP_2x2mm_P0.5mm',        2.0,  2.0,    0.50,     0.200,   0.20,  0.0,    0,  4,     "None"],
                ['ST_UFQFPN-20_3x3mm_P0.5mm',           3.0,  3.0,    0.50,     0.200,   0.20,  0.0,    5,  5,     "None"],
                ['ST_UQFN-6L_1.5x1.7mm_Pitch0.5mm',     1.5,  1.7,    0.50,     0.200,   0.20,  0.0,    0,  3,     "None"],
                ['QFN-28_4x4mm_P0.5mm',                 4.0,  4.0,    0.50,     0.200,   0.20,  0.0,    7,  7,     "None"],
                ['DFN-8-1EP_6x5mm_Pitch1.27mm',         6.0,  5.0,    1.27,     0.450,   0.20,  0.0,    0,  4,     "None"],
                ['UDFN-4_1x1mm_P0.65mm',                1.0,  1.0,    0.65,     0.20,    0.20,  0.0,    0,  2,     "None"],
                ['WDFN-8_2.2x2mm_P0.5mm_1EP',           2.0,  2.0,    0.50,     0.20,    0.20,  0.0,    0,  4,     "None"],

                ['Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm',                    6.0, 8.0, 0.50,     0.20,  0.0,   0.20,    8, 12,     "(4, 9, 15, 18, 24, 29, 35, 38)"],
                ['Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.8x1.3mm_ThermalVias',   2.0, 2.0, 0.50,     0.15,  0.0,   0.20,    0,  4,     "None"],
                ['Microchip_DRQFN-44-1EP_5x5mm_P0.7mm_EP2.65x2.65mm',       5.0, 5.0, 0.70,     0.25,  0.0,   0.20,   6,  6,     "None"],
                ['Microchip_DRQFN-64-1EP_7x7mm_P0.65mm_EP4.1x4.1mm',        7.0, 7.0, 0.65,     0.25,  0.0,   0.20,   8,  8,     "None"],
                ['QFN-56-1EP_8x8mm_P0.5mm_EP6.22x6.22mm_ThermalVias',       8.0, 8.0, 0.50,     0.20,  0.0,   0.20,   14,  14,   "None"],
                ['WDFN-8-1EP_2x2.2mm_P0.5mm_EP0.80x0.54',                   2.0, 2.2, 0.50,     0.20,  0.0,   0.20,    0,  4,     "None"],
                ['WQFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm',                   4.0, 4.0, 0.65,     0.20,  0.0,   0.20,    4,  4,     "None"],
                ['WQFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm_ThermalVias',       4.0, 4.0, 0.65,     0.20,  0.0,   0.20,    4,  4,     "None"],
                ['Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm',         4.0, 4.0, 0.65,     0.20,  0.0,   0.20,    4,  4,     "None"],
                ['Infineon_MLPQ-40-32-1EP_7x7mm_P0.5mm',                    7.0, 7.0, 0.50,     0.15,  0.0,   0.20,   10, 10,     "(13, 14, 15, 35,36, 37)"],
                ['Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.15x5.15mm',        7.0, 7.0, 0.50,     0.15,  0.0,   0.20,   12, 12,     "None"],

                ['DFN-8-1EP_6x5mm_P1.27mm_EP2x2mm',                         6.0,    5.0,    1.270,   0.4,    0.20,  0.0,     0,   4,  "None"],
                ['MLF-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm',                     4.0,    4.0,    0.500,   0.2,    0.20,  0.0,     5,   5,  "None"],
                ['OnSemi_VCT-28_3.5x3.5mm_P0.4mm',                          3.5,    3.5,    0.400,   0.18,   0.20,  0.0,    7,   7,   "None"],
                ['Panasonic_HSON-8_8x8mm_P2.00mm',                          8.0,    8.0,    2.000,   1.00,   0.20,  0.0,    0,   4,   "None"],
                ['Infineon_MLPQ-16-14-1EP_4x4mm_P0.5mm',                    4.00,   4.00,   0.500,   0.15,   0.20,  0.0,    4,   4,   "(10, 15)"],
                ['Infineon_MLPQ-48-1EP_7x7mm_P0.5mm_Pad5.55x5.55mm',        7.00,   7.00,   0.500,   0.20,   0.20,  0.0,   12,  12,   "None"],
                ['Texas_RUM0016A',                                          4.00,   4.00,   0.325,   0.10,   0.20,  0.0,    3,   3,   "None"],
                ['Texas_R-PWQFN-N28_EP2.1x3.1mm',                           3.50,   4.50,   0.400,   0.20,   0.20,  0.0,    5,   9,   "None"],
                ['Texas_RGE0024H_EP2.7x2.7mm',                              4.00,   4.00,   0.500,   0.20,   0.20,  0.0,    6,   6,   "None"],
                ['Texas_VQFN-RGR-20-1EP_3.5x3.5mm_Pitch0.5mm',              3.50,   3.50,   0.500,   0.20,   0.20,  0.0,    5,   5,   "None"],
                ['Texas_VQFN-RGW-20-1EP_5x5mm_Pitch0.65mm',                 5.00,   5.00,   0.650,   0.30,   0.20,  0.0,    5,   5,   "None"],
                ['Texas_WQFN-MR-100',                                       9.00,   9.00,   0.600,   0.20,   0.20,  0.0,   13,  13,   "None"],
                ['Texas_S-PWQFN-N20',                                       3.00,   3.00,   0.400,   0.15,   0.20,  0.0,    5,   5,   "None"],
                ['Texas_S-PWSON-N6',                                        2.00,   2.00,   0.650,   0.25,   0.20,  0.0,    0,   3,   "None"],
                ['Texas_S-PWSON-N6',                                        9.00,   9.00,   0.500,   0.25,   0.20,  0.0,   10,  10,   "None"],
                ['QFN-40-1EP_6x6mm_P0.5mm',                                 6.00,   6.00,   0.500,   0.25,   0.20,  0.0,   10,  10,   "None"],
                ['Texas_S-PVQFN-N48_EP5.15x5.15mm',                         7.00,   7.00,   0.500,   0.20,   0.20,  0.0,   12,  12,   "None"],
                ['Texas_S-PVQFN-N64_EP4.25x4.25mm',                         9.00,   9.00,   0.500,   0.20,   0.20,  0.0,   16,  16,   "None"],
                ['Texas_S-PVQFN-N36',                                       6.00,   6.00,   0.500,   0.20,   0.20,  0.0,    9,   9,   "None"],
                ['Texas_S-PVQFN-N16_EP2.7x2.7mm',                           4.00,   4.00,   0.650,   0.25,   0.20,  0.0,    4,   4,   "None"],
                ['Texas_S-PVQFN-N20_EP2.4x2.4mm',                           4.00,   4.00,   0.500,   0.20,   0.20,  0.0,    5,   5,   "None"],
                ['QFN-20-1EP_4x4mm_P0.5mm',                                 4.00,   4.00,   0.500,   0.20,   0.20,  0.0,    5,   5,   "None"],
                ['Texas_S-PVQFN-N24_EP2.1x2.1mm',                           4.00,   4.00,   0.500,   0.20,   0.20,  0.0,    6,   6,   "None"],
                ['Texas_S-PVQFN-N32_EP3.45x3.45mm',                         5.00,   5.00,   0.500,   0.20,   0.20,  0.0,    8,   8,   "None"],

                
                ]
                
class A3Dmodel:

    def __init__(self, subf, currfile):
    
        self.subf = subf
        self.currfile = currfile

        self.the = 12.0      # body angle in degrees
        self.tb_s = 0.15     # top part of body is that much smaller
        self.K = 0.2         # Fillet radius for pin edges
        self.c = 0.1         # pin thickness, body center part height
        self.R1 = 0.1        # pin upper corner, inner radius
        self.R2 = 0.1        # pin lower corner, inner radius
        self.S = 0.10        # pin top flat part length (excluding corner arc)
        self.L = 0.30        # pin bottom flat part length (including corner arc)
        self.fp_s = True     # True for circular pinmark, False for square pinmark (useful for diodes)
        self.fp_r = 0.5      # first pin indicator radius
        self.fp_d = 0.20     # first pin indicator distance from edge
        self.fp_z = 0.02     # first pin indicator depth
        self.ef = 0.0        # fillet of edges  Note: bigger bytes model with fillet
        self.cc1 = 0.25      # 0.45 chamfer of the 1st pin corner
        self.cce = 0.20      # 0.45 chamfer of the epad 1st pin corner
        self.D1 = 0.0        # body length
        self.E1 = 0.0        # body width
        self.E =  0.0        # body overall width
        self.A1 = DefaultA1  # body-board separation
        self.A2 = DefaultA2  # body height
        self.b = 0.0         # pin width
        self.e = 0.0         # pin (center-to-center) distance
        self.m = 0.1         # margin between pins and body 
        self.ps = 'square'   # rounded, square pads
        self.npx = 0         # number of pins along X axis (width)
        self.npy = 0         # number of pins along y axis (length)
        self.epad = 'None'   # e Pad
        self.excluded_pins = 'None' # no pin excluded
        self.old_modelName = ''     # modelName
        self.modelName = ''         # modelName
        self.rotation = -90         # rotation if required
        self.numpin = 0
        self.dest_dir_prefix = ''
        self.descr = ''
        
        
    #
    # Clean up, this function is executed right before it is added to the list
    #
    def CleanUp(self):


        if self.D < 4.0 or self.E < 4.0:
            if self.D < 2.0 or self.E < 2.0:
                self.fp_r = 0.1
                self.fp_d = 0.05
            else:
                self.fp_r = 0.2
                self.fp_d = 0.3
        else:
            self.fp_r = 0.4
            self.fp_d = 0.5
        
        
    #
    # Print the module on stdout, for debuging purpose
    #
    def Print(self):
        print("self.subf          " + self.subf)
        print("self.currfile      " + self.currfile)
        print("self.D1              " + self.D1)
        print("self.E1              " + self.E1)
        print("self.E               " + self.E)
        print("self.A1              " + self.A1)
        print("self.A2              " + self.A2)
        print("self.b               " + self.b)
        print("self.e               " + self.e)
        print("self.npx             " + self.npx)
        print("self.npy             " + self.npy)
        print("self.epad            " + self.epad)
        print("self.excluded_pins   " + self.excluded_pins)
        
    #
    # Scan and extract information from the foot print file
    #
    def ReadFile(self):
        

        #
        # Extract what is possible from the model name
        #
        li0 = self.subf.replace("_Pad", "_XXX")
        li2 = li0.replace("_PullBack", "_XXX")
        li3 = li2.replace("_PQFN", "_XXX")
        li1 = li3.replace("_Pitch", "_P")
        
        #
        # Extract pitch
        #
        FoundPitch = False
        if '_P' in li1:
            spline = li1.split('_P')
            spline2 = spline[1].split('mm')
            try:
                self.e = float(spline2[0])
                FoundPitch = True
            except ValueError:
                print("_P in file name is wrong, skipping " + self.subf)
                return False
        else:
            print("_P dont exist in file name, skipping add to exclude or special list " + self.subf)
            return False
        
        #
        # Extract body size
        #
        FoundSize = False
        if '_P' in li1:
            spline = li1.split('_P')
            spline2 = spline[0].split('_')
            li2 = spline2[len(spline2) - 1]
            spline3 = li2.split('mm')
            spline4 = spline3[0].split('x')
            if len(spline4) == 2:
                try:
                    self.E = float(spline4[0])
                except ValueError:
                    print("First parameter in body size parameter in file name is wrong, skipping " + self.subf)
                    return False
                try:
                    self.D = float(spline4[1])
                    FoundSize = True
                except ValueError:
                    print("Second parameter in body size parameter in file name is wrong, skipping " + self.subf)
                    return False
                
            else:
                print("_Layout is 1 or more than 2 parameters, skipping, add to exclude or special list " + self.subf)
                return False
            
        #
        # Extract epad size
        #
        FoundEPad = False
        if '_EP' in li1:
            spline = li1.split('_EP')
            spline2 = spline[1].split('mm')
            spline3 = spline2[0].split('x')
            EPadx = 0.0
            if len(spline3) == 2:
                try:
                    EPady = float(spline3[0])
                except ValueError:
                    print("first EPad parameter in file name is wrong, skipping " + self.subf)
                    return False
                try:
                    EPadx = float(spline3[1])
                    self.epad = '(' + str(EPadx) + ', ' + str(EPady) + ')'
                    FoundEPad = True
                except ValueError:
                    print("Second EPad parameter in file name is wrong, skipping " + self.subf)
                    return False
                
            else:
                print("EPad parameter is 1 or more than 2 parameters, skipping, add to exclude or special list " + self.subf)
                return False
            
        #
        # Extract number of pins
        #
        FoundPinNum = False
        self.numpin = 0
        spline = li1.split('-')
        try:
            self.numpin = int(spline[1])
        except ValueError:
            try:
                if len(spline) > 2:
                    self.numpin = int(spline[2])
                    FoundPinNum = True
                else:
                    spline1 = spline[1].split('_')
                    self.numpin = int(spline1[0])
                    FoundPinNum = True
            except ValueError:
                print("Pin number is missing in file name, skipping, add to exclude or special list " + self.subf)
                return False

        PinPos = []
        #
        # Collect all pads to calculte npx and npy
        #
        with open(self.currfile) as currf:
            for line in currf:
                #
                if 'pad' in line and ('layers F.Cu F.Paste F.Mask' in line or 'layers F.Cu F.Mask F.Paste' in line) and 'at' in line:
                    spline = line.split('at ')
                    spline2 = spline[1].split(')')
                    spline3 = spline2[0].split(' ')
                    x = float(spline3[0])
                    y = float(spline3[1])
                    PinMissing = True
                    for i in range(len(PinPos)):
                        if math.fabs(PinPos[i][0] - x) < 0.0001:
                            PinMissing = False
                            PinPos[i][2] = PinPos[i][2] + 1
                    if PinMissing:
                        PinPos.append([x, y, 1])

                    spline = line.split('size ')
                    spline2 = spline[1].split(')')
                    spline3 = spline2[0].split(' ')
                    self.b = round(float(spline3[1]) * 0.70, 2)
                    if self.b > (self.e / 2.0):
                        #
                        # Pad is probably rotated
                        #
                        self.b = round(float(spline3[0]) * 0.70, 2)
                        if self.b > (self.e / 2.0):
                            self.b = self.e / 3.0

#        for i in range(len(PinPos)):
#            print("PinPos[" + str(i) + "] = " + str(PinPos[i][0]) + ", " + str(PinPos[i][1]) + ", " + str(PinPos[i][2]))

        if len(PinPos) == 2:
            #
            # Only got pins along y-axis
            #
            if PinPos[0][2] == PinPos[1][2]:
                self.npx = 0
                self.npy = PinPos[0][2]
            else:
                print("Pads are unequal on left and right side, skipping, add to exclude or special list " + self.subf)
                return False
        else:
            ssum = 0
            hnum = 0
            for i in range(len(PinPos)):
                ssum = ssum + PinPos[i][2]
                if PinPos[i][2] > hnum:
                    hnum = PinPos[i][2]
            #
            if ssum == self.numpin:
                #
                # number of pads is equal to the number of found
                #
                self.npy = hnum
                self.npx = int((self.numpin - (hnum + hnum)) / 2)
            else:
                print("Pads are missing, skipping, add to exclude or special list " + self.subf)
                return False
            
            
        if self.npx == 0 and self.npy == 0:
            print("Could not calculte number of pads, skipping, add to exclude or special list " + self.subf)
            sys.exit()
            return False
        
        return True
            
    #
    # Add a finnished 3D model to the ResultFile and MakeAllfile
    #
    def PrintMissingModels(self, datafile, commandfile):


        
        datafile.write("    '" + self.model + "': Params(\n")
        datafile.write("        #\n")
        datafile.write("        # " + self.descr + "\n")
        datafile.write("        # This model have been auto generated based on the foot print file\n")
        datafile.write("        # A number of paramters have been fixed or guessed, such as A2\n")
        datafile.write("        # \n")
        datafile.write("        # The foot print that uses this 3D model is " + self.subf + "\n")
        datafile.write("        # \n")
        datafile.write('        c = ' + str(round(self.c, 2)) + ',           # pin thickness, body center part height\n')
        datafile.write('#        K = ' + str(round(self.K, 2)) + ',         # Fillet radius for pin edges\n')
        datafile.write('        L = ' + str(round(self.L, 2)) + ',         # pin bottom flat part length (including corner arc)\n')
        datafile.write('        fp_s = ' + str(round(self.fp_s, 2)) + ',          # True for circular pinmark, False for square pinmark (useful for diodes)\n')
        datafile.write('        fp_r = ' + str(round(self.fp_r, 2)) + ',          # First pin indicator radius\n')
        datafile.write('        fp_d = ' + str(round(self.fp_d, 2)) + ',          # First pin indicator distance from edge\n')
        datafile.write('        fp_z = ' + str(round(self.fp_z , 2)) + ',       # first pin indicator depth\n')
        datafile.write('        ef = ' + str(round(self.ef, 2)) + ',          # fillet of edges  Note: bigger bytes model with fillet\n')
        datafile.write('#        cc1 = ' + str(round(self.cc1, 2)) + ',        # 0.45 chamfer of the 1st pin corner\n')
        datafile.write('        cce = ' + str(round(self.cc1, 2)) + ',        # 0.45 chamfer of the epad 1st pin corner\n')
        datafile.write('        D = ' + str(round(self.D, 3)) + ',         # body length\n')
        datafile.write('        E = ' + str(round(self.E, 3)) + ',          # body overall width\n')
        datafile.write('        A1 = ' + str(round(self.A1 , 2)) + ',          # body-board separation\n')
        datafile.write('        A2 = ' + str(round(self.A2 , 2)) + ',          # body-board separation\n')
        datafile.write('        b = ' + str(round(self.b, 3)) + ',          # pin width\n')
        datafile.write('        e = ' + str(round(self.e, 3)) + ',          # pin (center-to-center) distance\n')
        datafile.write('        m = ' + str(round(self.m, 3)) + ',          # margin between pins and body \n')
        datafile.write("        ps = '" + self.ps + "',          # rounded, square pads\n")
        datafile.write('        npx = ' + str(round(self.npx, 2)) + ',           # number of pins along X axis (width)\n')
        datafile.write('        npy = ' + str(round(self.npy, 2)) + ',           # number of pins along y axis (length)\n')
        datafile.write('        epad = ' + self.epad + ',       # e Pad\n')
        datafile.write('        excluded_pins = ' + str(self.excluded_pins) + ',          # pin excluded\n')
        datafile.write("        modelName = '" + self.modelName + "',            # modelName\n")
        datafile.write('        rotation = ' + str(self.rotation) + ',      # rotation if required\n')
        datafile.write("        dest_dir_prefix = '../" + self.dest_dir_prefix + "',      # destination directory\n")

        datafile.write('        ),\n\n')

        #
        # Create the FreeCad command line
        #
        commandfile.write(FreeCadExe + ' ' + MainGenerator + self.model + '\n')

#
# Check if a foot print file should be excluded form being scanned
#
def DoNotExcludeModel(subf):

    global SkippingModelCnt

    #
    # Shall the model be excluded based on it's name
    #
    for n in ExcludeModels:
        if n == subf:
            #
            # Exclude this 3D model from creation
            #
#            print("Is in exclude list " + subf);
            SkippingModelCnt = SkippingModelCnt - 1
            return False
    
    return True

        
#
# Check if a 3D model given in the foot print file is misisng in the 3D model directory
#
def ModelDoNotExist(subf, currfile, NewA3Dmodel):

    global SkippingModelCnt
    #
    # Shall the model be excluded becaouse it already exist
    #
    with open(currfile) as currf:
        for line in currf:
            #
            if 'descr' in line:
                spline = line. split('"')
                if len(spline) > 1:
                    if len(spline[1]) > 2:
                        NewA3Dmodel.descr = spline[1]
            #
            if 'model' in line:
                line2 = line.replace("\\", "/")
                line3 = line2.replace("\r", "/")
                line4 = line3.replace("\n", "/")
                line2 = line4.replace("\t", "/")
                spline = line2.split('/')
                if len(spline) > 2:
                    NewA3Dmodel.dest_dir_prefix = spline[1]
                    NewA3Dmodel.filename = spline[2]
                    spline2 = spline[2].split('.wrl')
                    NewA3Dmodel.model = spline2[0]
                    NewA3Dmodel.modelName = NewA3Dmodel.model
                    NewA3Dmodel.old_modelName = NewA3Dmodel.model
                    #
                    line2 = spline[1] + '/' + spline[2]
                    Model3DFile = KISYS3DMOD + '/' + line2
#                    print("Model3DFile " + Model3DFile);
                    Model3DFilePath = Path(Model3DFile)
                    if Model3DFilePath.exists():
                        #
                        # 3D model already exist
                        #
#                        print("3D model exist, skipping it    " + subf);
                        SkippingModelCnt = SkippingModelCnt - 1
                        return False
#                    print("3D model do not exist  " + NewA3Dmodel.model)
                else:
                    print("Exclude  " + subf + "   Something fuzzy about 3D model name")
                    return False
    
    return True

        
#
# Check if a 3D model should be created from the SpecialModel list
#
def IsNotSpecialModel(NewA3Dmodel):
    #
    # Is it a special model that do not require parsing
    #
    for n in SpecialModels:
        if n[0] == NewA3Dmodel.model:
            #
            # This model is special setup
            # model, D, E, e, b, L, npy, npx, exluded pins
            #
            # ['Infineon_MLPQ-16-14-1EP_4x4mm_P0.5mm',                    4.00,   4.00,   0.50,   0.15,   0.20,    4,  4,     "(10, 15)"],
            # 
            
            NewA3Dmodel.E = n[1]
            NewA3Dmodel.D = n[2]
            NewA3Dmodel.e = n[3]
            NewA3Dmodel.b = n[4]
            NewA3Dmodel.L = n[5]
            NewA3Dmodel.m = n[6]
            NewA3Dmodel.npy = n[7]
            NewA3Dmodel.npx = n[8]
            NewA3Dmodel.excluded_pins = n[9]
#            print("Special  " + NewA3Dmodel.subf)
            return False

    return True
    

#
# Find all missing models
#
def FindMissingModels():

    global SkippingModelCnt
    #
    print("Checking dir: " + FPDir)
    currdir = FPDir
    #
    for subpath, subdirs, subfiles in os.walk(currdir):
        for subf in subfiles:
            if subf.endswith('.kicad_mod'):
                currfile = os.path.join(subpath, subf)
                #
                NewA3Dmodel = A3Dmodel(subf, currfile)
                #
                # Shall the model be excluded based on it's name
                #
                AddMissing = DoNotExcludeModel(subf)

                if AddMissing:
                    #
                    # Shall the model be excluded because it already exist
                    #
                    AddMissing = ModelDoNotExist(subf, currfile, NewA3Dmodel)
                    
                if AddMissing:
                    #
                    # Is it a special model
                    #
                    if IsNotSpecialModel(NewA3Dmodel):
                        #
                        # Parse the data file
                        #
                        AddMissing = NewA3Dmodel.ReadFile()
                        
                        
                if AddMissing:
                    for n in MissingModels:
                        if n.model == NewA3Dmodel.model:
                            AddMissing = False
                    #
                    if AddMissing:
                        print("Creating " + NewA3Dmodel.model);
                        NewA3Dmodel.CleanUp()
                        MissingModels.append(NewA3Dmodel)
                else:
                    SkippingModelCnt = SkippingModelCnt + 1
#                    NewA3Dmodel.Print()


def SaveMissingModels():


    if os.path.isfile(ResultFile):
        os.remove(ResultFile)

    if os.path.isfile(MakeAllfile):
        os.remove(MakeAllfile)
    
    if len(MissingModels) > 0:
        datafile = open(ResultFile, "w") 
        commandfile = open(MakeAllfile, "w") 
        
        commandfile.write('#!/bin/sh\n\n')
        
        for n in MissingModels:
            n.PrintMissingModels(datafile, commandfile)

        datafile.close()
        commandfile.close()
        
        print(" ")
    

def main(argv):

    global MissingModels
    global SkippingModelCnt

    SkippingModelCnt = 0

    MissingModels = []
    FindMissingModels()
    SaveMissingModels()
    
    if len(MissingModels) == 0 and SkippingModelCnt == 0:
        print("No missing 3D models was found")
        
    if len(MissingModels) > 0:
        print(str(len(MissingModels)) + " 3D models was missing")
        print("Add paramters in " + ResultFile + " to file cq_parameters.py")
        print("And execute batch file " + MakeAllfile)
    
    if SkippingModelCnt > 0:
        print(str(SkippingModelCnt) + " Foot prints was skipped, add them to the ExcludeModels list or SpecialModels list")

        
if __name__ == "__main__":
    main(sys.argv[1:])

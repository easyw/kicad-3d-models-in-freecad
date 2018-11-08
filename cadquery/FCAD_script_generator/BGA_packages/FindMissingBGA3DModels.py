#
#
# Auto create BGA 3D models     version 1.0
#
# Script to scan SOIC foot print files and create 3D model paramters for those 3D models that 
# is missing in \Package_BGA.3dshapes
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
ModelExist = False

#
# The path to foot print file directory in relation to where this script is placed
#
FPDir = '../../../../kicad-footprints/Package_BGA.pretty'
KISYS3DMOD = '../../../../kicad-packages3D'

#
# The name of the result files
#
ResultFile = 'MissingBGA3DModels.txt'
MakeAllfile = 'MakeFindMissingBGA3DModels.sh'
#
# The path to FreeCad, this path will be used in the MakeFindMissingXXX3DModels.sh script
#
FreeCadExe = '/c/users/stefan/Downloads/FreeCAD_0.17.11223_x64_dev_win/FreeCAD_0.17.11223_x64_dev_win/bin/FreeCAD.exe'
MainGenerator = 'main_generator.py '
Parameters_Py = 'cq_parameters.py'

#
# this list contain the foot print that is missing it's 3D model but the 3D model is specified in the parameter file
#
MissingModelsInParameters = []

#
# This list will hold the missing 3D models
#
MissingModels = []

#
# If a foot print file name is in the ExcludeModels list it will not be created
#
ExcludeModels =[
                'Texas_SIL0010A_MicroSiP-10-1EP_3.8x3mm_P0.6mm_EP0.7x2.9mm.kicad_mod', 
                'BGA-132_12x18mm_Layout11x17_P0.5mm.kicad_mod', 
                'BGA-152_14x18mm_Layout13x17_P0.5mm.kicad_mod',
                'LFBGA-169_16x12mm_Layout28x14_P0.5mm_Ball0.3_Pad0.3mm_NSMD.kicad_mod', 
                'Texas_DSBGA-5_0.822x1.116mm_Layout2x1x2_P0.4mm.kicad_mod',
                'BGA-152_14x18mm_Layout13x17_P0.5mm.kicad_mod'
                ]

#
# If a foot print file contian a model name (xxxx.wrl) that is in the SpecialModels list 
# it will will be created with those parameters given in the list
#
# model, D, E, e, b, L, m, npy, npx, excluded_pins
#
SpecialModels =[
#                    ['Linear_LGA-133_15.0x15.0_Layout12x12_P1.27mm',           15.00,  15.00,   1.27,   0.50,   0.50,   0.10,   12,   12, 'None'],
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
        self.D =  0.0        # body overall width
        self.E =  0.0        # body overall width
        self.A1 = DefaultA1  # body-board separation
        self.A2 = DefaultA2  # body height
        self.A = DefaultA2   # body height
        self.b = 0.0         # pin width
        self.e = 0.0         # pin (center-to-center) distance
        self.m = 0.1         # margin between pins and body 
        self.ps = 'square'   # rounded, square pads
        self.npx = 0         # number of pins along X axis (width)
        self.npy = 0         # number of pins along y axis (length)
        self.epad = 'None'   # e Pad
        self.excluded_pins = 'None' # no pin excluded
        self.model = ''             # modelName
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

        if self.D < 2.0 or self.E < 2.0:
            self.fp_r = 0.2
            self.fp_d = 0.1
        else:
            self.fp_r = 0.4
            self.fp_d = 0.3
        
        
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
        sizesx = 0.0
        sizesy = 0.0
        sizeex = 0.0
        sizeey = 0.0
        self.b = 0.0
        self.e = 0.0
        self.npx = 0
        self.npy = 0
        #
        with open(self.currfile) as currf:
            for line in currf:
                if line.startswith('  (fp_line') and 'F.Fab' in line:
                    line2 = line.replace("(", " ")
                    line = line2.replace(")", " ")
                    spline = line.split(' ')
                    sizesx = min(sizesx, float(spline[7]))
                    sizesx = min(sizesx, float(spline[12]))
                    sizeex = max(sizeex, float(spline[7]))
                    sizeex = max(sizeex, float(spline[12]))
                    #
                    sizesy = min(sizesy, float(spline[6]))
                    sizesy = min(sizesy, float(spline[11]))
                    sizeey = max(sizeey, float(spline[6]))
                    sizeey = max(sizeey, float(spline[11]))
                    #
        #
        self.D = (0.0 - sizesx) + sizeex
        self.E = (0.0 - sizesy) + sizeey
        #
        #
        spline = self.subf.split('-')
        if spline[0] == "Maxim_WLP":
            spline2 = spline[1].split('.')
            li1 = spline2[0]                
        elif "_" in spline[0] or "BGA" in spline[0] or "WLP" in spline[0]:
            spline2 = spline[1].split('_')
            li1 = spline2[0]
        else:
            spline2 = spline[2].split('_')
            li1 = spline2[0]
            
        fnp = float(li1)
        fnp = math.sqrt(fnp)
        fnp = round(fnp)
        self.npx = int(fnp)
        self.npy = self.npx

        #
        #
        if '_P' in self.subf:
            spline = self.subf.split('_P')
            li1 = spline[1]
            spline = li1.split('mm')
            self.e = float(spline[0])
            self.b = self.e / 2.0
        if '_Ball' in self.subf:
            spline1 = self.subf.split('_Ball')
            spline2 = spline1[1].split('_')
            spline3 = spline2[0].split('mm')
            self.b = float(spline3[0])
        if '_Layout' in self.subf:
            spline1 = self.subf.split('_Layout')
            spline2 = spline1[1].split('_')
            spline3 = spline2[0].split('x')
            self.npy = int(spline3[0])
            self.npx = int(spline3[1])
        #
        
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
        datafile.write("        # A number of paramters have been fixed or guessed, such as A and A1\n")
        datafile.write("        # \n")
        datafile.write("        # The foot print that uses this 3D model is " + self.subf + "\n")
        datafile.write("        # \n")
        datafile.write("        fp_z = 0.1,     # first pin indicator depth\n")
        datafile.write('        fp_r = ' + str(round(self.fp_r, 2)) + ',          # First pin indicator radius\n')
        datafile.write('        fp_d = ' + str(round(self.fp_d, 2)) + ',          # First pin indicator distance from edge\n')
        datafile.write("        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet\n")
        datafile.write("        D = " + str(self.D) + ",      # body overall length\n")
        datafile.write("        E = " + str(self.E) + ",      # body overall width\n")
        datafile.write("        A1 = " + str(self.A1) + ",      # body-board separation\n")
        datafile.write("        A = " + str(self.A) + ",       # body overall height\n")
        datafile.write("        b = " + str(self.b) + ",      # ball pin width diameter with a small extra to obtain a union of balls and case\n")
        datafile.write("        e = " + str(self.e) + ",       # pin (center-to-center) distance\n")

        datafile.write("        sp = 0.0,       # seating plane (pcb penetration)\n")
        datafile.write("        npx = " + str(self.npx) + ",      # number of pins along X axis (width)\n")
        datafile.write("        npy = " + str(self.npy) + ",      # number of pins along y axis (length)\n")
        datafile.write('        excluded_pins = ("internals",), # pins to exclude -> None or "internals"\n')
        datafile.write("        old_modelName = '" + self.old_modelName + "', # Old_modelName\n")
        datafile.write("        modelName = '" + self.modelName + "',\n")
        datafile.write("        rotation = -90, # rotation if required\n")
        datafile.write("        dest_dir_prefix = '../" + self.dest_dir_prefix + "',\n")
        datafile.write('        ),\n\n')

        #
        # Create the FreeCad command line
        #
        commandfile.write(FreeCadExe + ' ' + MainGenerator + self.model + '\n')

#
# Check if a foot print file should be excluded form being scanned
#
def DoNotExcludeModel(subf):
    #
    # Shall the model be excluded based on it's name
    #
    for n in ExcludeModels:
        if n == subf:
            #
            # Exclude this 3D model from creation
            #
            print("Is in exclude list " + subf);
            return False
    
    return True

        
#
# Check if a 3D model given in the foot print file is misisng in the 3D model directory
#
def ModelDoNotExist(subf, currfile, NewA3Dmodel):

    global ModelExist
    
    #
    # Shall the model be excluded becaouse it already exist
    #
    ModelExist = False
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
                        ModelExist = True
#                        print("3D model already exist  " + NewA3Dmodel.model)
                        return False
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
            
            NewA3Dmodel.E = n[1]
            NewA3Dmodel.D = n[2]
            NewA3Dmodel.e = n[3]
            NewA3Dmodel.b = n[4]
            NewA3Dmodel.L = n[5]
            NewA3Dmodel.m = n[6]
            NewA3Dmodel.npy = n[7]
            NewA3Dmodel.npx = n[8]
            NewA3Dmodel.excluded_pins = n[8]
#            print("Special  " + NewA3Dmodel.subf)
            return False

    return True
        
#
# Check if a 3D model should be created from the SpecialModel list
#
def ModelNotAlreadyCreated(NewA3Dmodel):
    #
    # Have it already been created
    #
    for n in MissingModels:
        if n.model == NewA3Dmodel.model:
            # Remove duplicates
            return False

    #
    # Do a foot print have a missing 3D model but the 3D model have not been created
    #
    with open(Parameters_Py) as currf:
        for line in currf:
            if "'" + NewA3Dmodel.model + "'" in line:
                MissingModelsInParameters.append(NewA3Dmodel.model)
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
                    AddMissing = ModelNotAlreadyCreated(NewA3Dmodel)
                    #
                    if AddMissing:
                        print("Creating " + NewA3Dmodel.model);
                        NewA3Dmodel.CleanUp()
                        MissingModels.append(NewA3Dmodel)
                else:
                    if not ModelExist:
                        print("Discard  " + NewA3Dmodel.subf);
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

        if len(MissingModelsInParameters) > 0:
            for n in MissingModelsInParameters:
                commandfile.write(FreeCadExe + ' ' + MainGenerator + n + '\n')
    
        commandfile.close()
        datafile.close()
    else:
        if len(MissingModelsInParameters) > 0:
            commandfile = open(MakeAllfile, "w") 
            #
            commandfile.write('#!/bin/sh\n\n')
            #
            for n in MissingModelsInParameters:
                commandfile.write(FreeCadExe + ' ' + MainGenerator + n + '\n')
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
    else:
        if len(MissingModelsInParameters) > 0:
            print(str(len(MissingModelsInParameters)) + " 3D models was missing but is included in the " + Parameters_Py)
            print("Execute batch file " + MakeAllfile)
    
    
    if SkippingModelCnt > 0:
        print(str(SkippingModelCnt) + " Foot prints was skipped, add them to the ExcludeModels list or SpecialModels list")

        
if __name__ == "__main__":
    main(sys.argv[1:])

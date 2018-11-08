#
#
# Auto create DIP 3D models     version 1.0
#
# Script to scan DIP foot print files and create 3D model paramters for those 3D models that 
# is missing in \Package_DIP.3dshapes
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

DefaultA1 = 0.38
DefaultA2 =  3.3
Defaultm =  0.0
Defaultb =  0.46
Defaultb1 =  1.52


SkippingModelCnt = 0

#
# The path to foot print file directory in relation to where this script is placed
#
FPDir = '../../../../kicad-footprints/Package_DIP.pretty'
KISYS3DMOD = '../../../../kicad-packages3D'

#
# The name of the result files
#
ResultFile = 'MissingDIP3DModels.txt'
MakeAllfile = 'MakeFindMissingDIP3DModels.sh'
#
# The path to FreeCad, this path will be used in the MakeFindMissingDIP3DModels.sh script
#
FreeCadExe = '/c/users/stefan/Downloads/FreeCAD_0.17.11223_x64_dev_win/FreeCAD_0.17.11223_x64_dev_win/bin/FreeCAD.exe'
MainGenerator = 'main_generator.py '

#
# This list will hold the missing 3D models
#
MissingModels = []

#
# If a foot print file name is in the ExcludeModels list it will not be created
#
ExcludeModels =[
                'PowerIntegrations_eDIP-12B.kicad_mod', 
               ]

#
# If a foot print file contian a model name (xxxx.wrl) that is in the SpecialModels list 
# it will will be created with those parameters given in the list
#
# model, D, E, E1, e, b, numpin, SMDSocket, excluded_pins
#
SpecialModels =[
                ['PowerIntegrations_PDIP-8B',               10.28,  7.62,  4.50, 2.54, 0.46, 8,   'tht', '[6]'], 
                ['PowerIntegrations_PDIP-8C',               10.28,  7.62,  4.50, 2.54, 0.46, 8,   'tht', '[3]'], 
                ['PowerIntegrations_SDIP-10C',              12.82,  7.62,  4.50, 2.54, 0.46, 10,  'tht', '[4]'], 
                ['PowerIntegrations_SMD-8',                 10.24,  7.62,  4.90, 2.54, 0.46,  8,  'smd', '[0]'], 
                ['PowerIntegrations_SMD-8B',                10.24,  7.62,  4.90, 2.54, 0.46,  8,  'smd', '[6]'], 
                ['PowerIntegrations_SMD-8C',                10.24,  7.62,  4.90, 2.54, 0.46,  8,  'smd', '[3]'], 
                ['PowerIntegrations_SMD-8C',                10.24,  7.62,  4.90, 2.54, 0.46,  8,  'smd', '[3]'], 
                ['Toshiba_11-7A9',                           7.86,  7.86,  5.54, 2.54, 0.46,  6,  'tht', '[5]'], 
                ['DIP-6_W8.89mm_SMDSocket_LongPads',         7.74,  8.89,  5.07, 2.54, 1.30,  6,  'tht', '[0]'], 
               ]

                
                    
                
class A3Dmodel:

    def __init__(self, subf, currfile):
        self.subf = subf
        self.currfile = currfile
        self.numpin = 0
        self.model = ""
        self.descr = ""
        self.D = 1.0
        self.E = 1.0
        self.E1 = 1.0
        self.A = 0.0
        self.A1 = DefaultA1
        self.A2 = DefaultA2
        self.npx = 0
        self.npy = 0
        self.e = 0.5
        self.b = Defaultb
        self.b1 = Defaultb1
        self.m = Defaultm
        self.epad = "None"
        self.excluded_pins = '[0]'
        self.SMDSocket = 'tht'
        self.PinDist = 0.0
        self.corner = 'fillet'
        self.dest_dir_prefix = ''
        self.filename = ''
        self.rotation = 90
    
    #
    # Print the module on stdout, for debuging purpose
    #
    def Print(self):
        print("self.subf            " + self.subf)
        print("self.currfile        " + self.currfile)
        print("self.numpin          " + str(self.numpin))
        print("self.model           " + self.model)
        print("self.descr           " + self.descr)
        print("self.D               " + str(self.D))
        print("self.E               " + str(self.E))
        print("self.E1              " + str(self.E1))
        print("self.A               " + str(self.A))
        print("self.A1              " + str(self.A1))
        print("self.A2              " + str(self.A2))
        print("self.npx             " + str(self.npx))
        print("self.npy             " + str(self.npy))
        print("self.e               " + str(self.e))
        print("self.b               " + str(self.b))
        print("self.m               " + str(self.m))
        print("self.epad            " + str(self.epad))
        print("self.SMDSocket       " + self.SMDSocket)
        print("self.corner          " + self.corner)
        print("self.excluded_pins   " + self.excluded_pins)
        print("self.dest_dir_prefix " + self.dest_dir_prefix)
    
        
    #
    # Scan and extract information from the foot print file
    #
    def ReadFile(self):
        

        #
        # Extract what is possible from the model name
        #
#        print("subf " + self.subf)
        li0 = self.subf.replace("_Pad", "_XXX")
        li1 = li0.replace("_PullBack", "_XXX")
        li2 = li1.replace("_PQFN", "_XXX")
        li1 = li2.replace("_Pitch", "_P")

#        print("li1  " + li1)
        #
        # Extract pitch
        #
        FoundPitch = False
        self.e = 2.54
        FoundPitch = True

        #
        # Extract width
        #
        FoundPitch = False
        self.e = 2.54
        FoundPitch = True

        try:
            spline = li1.split('_W')
            spline2 = spline[0].split('-')
            if len(spline2) == 2:
                # Normal
                self.numpin = int(spline2[1])
            elif len(spline2) == 3:
                # Missing pin
                if 'N' in spline2[2]:
                    li2 = spline2[2].replace("N", "")
                    self.numpin = int(spline2[1])
                    self.excluded_pins = '[' + li2 + ']'
                else:
                    self.numpin = int(spline2[2])
                    self.excluded_pins = '[' + spline2[1] + ']'
            else:
                print("Fuzzy file name1 " + self.subf);
                return False
            #
            # Extract body size
            #
            spline = li1.split('_W')
            spline2 = spline[1].split('mm')
            
            self.E = float(spline2[0])
            #
            # Extract number of pins
            #
            self.npx = 0
            self.npy = int(self.numpin / 2)
            #
            # Pin or smd
            #
            if 'SMDSocket' in li1 or li1.startswith('SMDIP'):
                self.SMDSocket = 'smd'
        except ValueError:
                print("Fuzzy file name2 " + self.subf);
                return False
        #
        # Check for missing
        #
        
            
        minx = 0.0
        maxx = 0.0
        miny = 0.0
        maxy = 0.0
        #
        with open(self.currfile) as currf:
            for line in currf:
                #
                if 'fp_line' in line and '(layer F.Fab)' in line:
                    spline = line.split('start ')
                    spline2 = spline[1].split(')')
                    spline3 = spline2[0].split(' ')
                    x = float(spline3[0])
                    y = float(spline3[1])
                    minx = min(minx, x)
                    maxx = max(maxx, x)
                    #
                    miny = min(miny, y)
                    maxy = max(maxy, y)
                    #
                if 'pad' in line and ('layers F.Cu F.Paste F.Mask' in line or 'layers F.Cu F.Mask F.Paste' in line) and 'at' in line:
                    if ' smd ' in line:
                        self.SMDSocket = 'smd'
                        
        self.E1 = (maxx + math.fabs(minx))
        self.D = (maxy + math.fabs(miny))
        
        if self.E1 > (self.E - 1.5):
            #
            # Foot print is messed up with extra F.Fabs
            #
            self.E1 = self.E - 1.5
        
        
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
        datafile.write('        D  = ' + str(round(self.D, 2)) + ',         # body length\n')
        datafile.write('        E1 = ' + str(round(self.E1, 2)) + ',         # body width\n')
        datafile.write('        E  = ' + str(round(self.E, 2)) + ',         # body overall width\n')
        datafile.write('        A1 = ' + str(round(self.A1 , 2)) + ',          # body-board separation\n')
        datafile.write('        A2 = ' + str(round(self.A2 , 2)) + ',          # body height\n')
        datafile.write('        b1 = ' + str(round(self.b1 , 2)) + ',         # pin width\n')
        datafile.write('        b  = ' + str(round(self.b , 2)) + ',         # pin tip width\n')
        datafile.write('        e  = ' + str(round(self.e , 2)) + ',         # body-board separation\n')
        datafile.write('        npins = ' + str(self.numpin) + ',         # number of pins\n')
        datafile.write("        modelName = '" + self.model + "',            # modelName\n")
        datafile.write('        rotation = ' + str(self.rotation) + ',      # rotation if required\n')
        datafile.write("        type = '" + self.SMDSocket + "',       # tht, smd or thtsmd\n")
        datafile.write("        corner = '" + self.corner + "',   # chamfer or fillet\n")
        datafile.write('        excludepins = ' + self.excluded_pins + ',  # pin excluded\n')
        datafile.write("#        dest_dir_prefix = '../" + self.dest_dir_prefix + "',  # destination directory\n")
        
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
            print("Excluded " + subf);
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
#    print(" ")
    with open(currfile) as currf:
#        print("currfile  " + currfile)
        for line in currf:
            #
            if 'descr' in line:
                spline = line. split('"')
                if len(spline) > 1:
                    if len(spline[1]) > 2:
                        NewA3Dmodel.descr = spline[1]
#                        print("NewA3Dmodel.descr  " + NewA3Dmodel.descr)
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
#            print("Special  " + n[0])
            #
            # This mdel is special setup
            #
            NewA3Dmodel.D = n[1]
            NewA3Dmodel.E = n[2]
            NewA3Dmodel.E1 = n[3]
            NewA3Dmodel.e = n[4]
            NewA3Dmodel.b = n[5]
            NewA3Dmodel.numpin = n[6]
            NewA3Dmodel.SMDSocket = n[7]
            NewA3Dmodel.excluded_pins = n[8]
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
        
        
# -*- coding: utf8 -*-
'''
Script for inserting licensing information into an existing step file.

Original Script Automatic STEP to VRML converter for KiCAD with thumbnail creation in Povray
from https://github.com/JoanTheSpark/KiCAD
Rene Poeschl removed everything that is not needed to insert licensing information into step files.

 Copyright (c) 2015 Maurice easyw@katamail.com
 Copyright (c) 2015 Hasan Yavuz Özderya
 Copyright Nico
 Copyright (c) 2016 marmni (FreeCAD forums user)
 overall arrangement and snippets came from all over the internet and have been pushed into place by Joan Sparky (c) 2016
'''

import sys, os, shutil
import hashlib, pyparsing
import datetime
from datetime import datetime

import FreeCAD
import Import
import FreeCADGui
import ImportGui
import Draft

# additionally needed for new VRML export script
import FreeCADGui,Part,Mesh
import PySide
from PySide import QtGui, QtCore
from collections import namedtuple
from os.path import expanduser

# additionally needed for POVray export script
try:
    import __builtin__ as builtin #py2
except:
    import builtins as builtin  #py3

import subprocess
from subprocess import call

#FNME_hashfile = "_StepFileHashes.txt" # stored in STEP folder above

STR_int_licAuthor = "your name"
STR_int_licEmail = "your email"
STR_int_licOrgSys = ""
STR_int_licPreProc = ""
STR_int_licOrg = "FreeCAD"

LIST_int_license = ["Copyright (C) "+datetime.now().strftime("%Y")+", " + STR_int_licAuthor,
                "",
                "This work is licensed under the [Creative Commons CC-BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/legalcode), ",
                "with the following exception:",
                "To the extent that the creation of electronic designs that use \'Licensed Material\' can be considered to be \'Adapted Material\', ",
                "then the copyright holder waives article 3 of the license with respect to these designs and any generated files which use data provided ",
                "as part of the \'Licensed Material\'.",
                "You are free to use the library data in your own projects without the obligation to share your project files under this or any other license agreement.",
                "However, if you wish to redistribute these libraries, or parts thereof (including in modified form) as a collection then the exception above does not apply. ",
                "Please refer to https://github.com/KiCad/kicad-packages3D/blob/master/LICENSE.md for further clarification of the exception.",
                "Disclaimer of Warranties and Limitation of Liability.",
                "These libraries are provided in the hope that they will be useful, but are provided without warranty of any kind, express or implied.",
                "*USE 3D CAD DATA AT YOUR OWN RISK*",
                "*DO NOT RELY UPON ANY INFORMATION FOUND HERE WITHOUT INDEPENDENT VERIFICATION.*",
                ]

# points: [Vector, Vector, ...]
# faces: [(pi, pi, pi), ], pi: point index
# color: (Red, Green, Blue), values range from 0 to 1.0



def say(*arg):
    FreeCAD.Console.PrintMessage(" ".join(map(str,arg)) + "\n")

def FNCT_modify_step(PMBL_stepfile,
                     DICT_positions,
                     LIST_license,
                     FNME_stepfile,
                     STR_licAuthor,
                     STR_licEmail,
                     STR_licOrgSys,
                     STR_licPreProc,
                     STR_licOrg,
                     ):
    """
    - add license right after HEADER
    - modification of DESCR
    - total replace of NAME
    - copy of SCHEMA
    - space after ENDSEC

    DICT_positions:
    H .. HEADER
    D .. DESCRIPTION
    N .. NAME
    S .. SCHEMA
    E .. ENDSEC
    """
    PMBL_modstepfile = []
    FLAG_addlicense = True
    STR_description = ""
    STR_schema = ""
    fname, ext=os.path.splitext(FNME_stepfile)
    for line in range(DICT_positions["E"]):
        if line < DICT_positions["H"]: # leave ISO/HEADER alone
            PMBL_modstepfile.append(PMBL_stepfile[line].strip())
        if line == DICT_positions["H"] and FLAG_addlicense: # add license
            PMBL_modstepfile.append("/* " + str(FNME_stepfile) + " 3D STEP model for use in ECAD systems")
            for licline in LIST_license:
                PMBL_modstepfile.append(" * " + licline)
            PMBL_modstepfile.append(" */")
            PMBL_modstepfile.append("")
            FLAG_addLicense = False
        if line >= DICT_positions["D"] and line < (DICT_positions["N"] - 1): # get DESCR part
            STR_description += PMBL_stepfile[line].strip()
        if line == (DICT_positions["S"] - 1): # add modded DESCR and NAME
            # DESCRIPTION
            PMBL_modstepfile.append("FILE_DESCRIPTION(")
            #PMBL_modstepfile.append("/* description */ ('model of " + str(FNME_stepfile) + "'),")
            PMBL_modstepfile.append("/* description */ ('model of " + str(fname) + "'),")
            STR_description = pyparsing.nestedExpr("/*", "*/").suppress().transformString(STR_description)
            #PMBL_modstepfile.append("/* implementation_level */ " + STR_description[-len("'2;1');"):])
            PMBL_modstepfile.append("/* implementation_level */ " + "'2;1');")
            PMBL_modstepfile.append("")
            #NAME
            PMBL_modstepfile.append("FILE_NAME(")
            PMBL_modstepfile.append("/* name */ '" + str(FNME_stepfile) + "',")
            STR_TS = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            PMBL_modstepfile.append("/* time_stamp */ '" + STR_TS + "',")
            PMBL_modstepfile.append("/* author */ ('" + STR_licAuthor + "','" + STR_licEmail + "'),"),
            PMBL_modstepfile.append("/* organization */ ('" + STR_licOrg + "'),")
            PMBL_modstepfile.append("/* preprocessor_version */ '" + STR_licPreProc + "',")
            PMBL_modstepfile.append("/* originating_system */ '" + STR_licOrgSys + "',")
            PMBL_modstepfile.append("/* authorisation */ '');")
            PMBL_modstepfile.append("")
        if line >= (DICT_positions["S"] - 1) and line <= (DICT_positions["E"] - 1): # get DESCR part
            STR_schema += PMBL_stepfile[line].strip()
        if line == (DICT_positions["E"] - 1): # add cleaned SCHEMA/ENDSEC
            STR_schema = pyparsing.nestedExpr("/*", "*/").suppress().transformString(STR_schema)
            for item in STR_schema.split(";")[:-1]:
                PMBL_modstepfile.append(item + ";")
    PMBL_modstepfile.append("")
    return(PMBL_modstepfile)



def addLicenseToStep(FLDR_toStepFiles, FNME_stepfile, LIST_license, STR_licAuthor, STR_licEmail="", STR_licOrgSys="", STR_licOrg="",STR_licPreProc=""):
    filepath = FLDR_toStepFiles + os.sep + FNME_stepfile
    if os.path.isfile(filepath): # test if folder or file..
        fname, ext=os.path.splitext(FNME_stepfile)
        if LIST_license[0] == "":
            LIST_license=list(LIST_int_license)
        LIST_license[0] = "Copyright (C) "+datetime.now().strftime("%Y")+", " + STR_licAuthor
        if ext == ".stp" or ext == ".step": # test if step file
            #say("Starting of licensing\n")
            try:
                HDLR_stepfile = open(filepath, 'r') # open
            except Exception as exception:
                FreeCAD.Console.PrintError("Add License: Can't open step file for read access\n")
                FreeCAD.Console.PrintError("{:s}\n".format(exception))
                return

            HDLR_stepfile.seek(0)
            PMBL_stepfile = HDLR_stepfile.readlines()
            HDLR_stepfile.close()
            CNT_cutoff = 0
            DICT_positions = {}
            for line in PMBL_stepfile:
                CNT_cutoff += 1
                if line[:6] == "HEADER":
                    DICT_positions["H"] = CNT_cutoff
                elif line[:6] == "ENDSEC":
                    DICT_positions["E"] = CNT_cutoff
                elif line[:4] == "DATA":
                    DICT_positions["A"] = CNT_cutoff
                    break
                if line[:5] == "FILE_":
                    if line[5:9] == "DESC":
                        DICT_positions["D"] = CNT_cutoff
                    elif line[5:9] == "NAME":
                        DICT_positions["N"] = CNT_cutoff
                    elif line[5:9] == "SCHE":
                        DICT_positions["S"] = CNT_cutoff

            LIST_PMBL = FNCT_modify_step(PMBL_stepfile[:DICT_positions["E"]],
                                         DICT_positions,
                                         LIST_license,
                                         FNME_stepfile,
                                         STR_licAuthor,
                                         STR_licEmail,
                                         STR_licOrgSys,
                                         STR_licPreProc,
                                         STR_licOrg,
                                         )

            # overwrite step file
            try:
                HDLR_stepfile_w = open(filepath, 'w') # open
            except Exception as exception:
                FreeCAD.Console.PrintError("Add License: Can't open step file for write access\n")
                FreeCAD.Console.PrintError("{:s}\n".format(exception))
                return

            # overwrite with new preamble
            for line in LIST_PMBL:
                HDLR_stepfile_w.write(line + "\n")
            # add old data section
            for line in PMBL_stepfile[(DICT_positions["A"]-1):]:
                HDLR_stepfile_w.write(line.strip() + "\n")
            HDLR_stepfile_w.close()
            say ("License addition successful")
        else:
            FreeCAD.Console.PrintWarning("Add License: File has wrong file extension: {:s}".format(FNME_stepfile))
    else:
        FreeCAD.Console.PrintWarning("Add License: Path does not exist: {:s}".format(filepath))
###

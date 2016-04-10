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

PATH_FREECADBIN = "C:\Program Files\FreeCAD 0.16\bin"
sys.path.append(PATH_FREECADBIN)

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
import __builtin__
import subprocess
from subprocess import call

PATH_POVrayExecutable = "C:/Program Files/POV-Ray/v3.7/bin/pvengine64.exe" # install povray 3.7, under options there deactivate restrictions for I/O
IMG_W = "150"
IMG_H = "150"

FLDR_toStepFiles = "E:/Data_Inventor/ElectronicDevices/STEP/"
FLDR_toVrmlFiles = "E:/Data_Inventor/ElectronicDevices/VRML/"
FLDR_toPOVrayFiles = "E:/Data_Inventor/ElectronicDevices/POVray/" # this folder will contain the thumbnails

FNME_hashfile = "_StepFileHashes.txt" # stored in STEP folder above

STR_licAuthor = "your name"
STR_licEmail = "your email"
STR_licOrgSys = ""
STR_licPreProc = ""

LIST_license = ["Copyright (C) "+datetime.now().strftime("%Y")+", " + STR_licAuthor,
                "",
                "This program is free software: you can redistribute it and/or modify",
                "it under the terms of the GNU General Public License as published by",
                "the Free Software Foundation, either version 3 of the License, or",
                "any later version.",
                "",
                "This program is distributed in the hope that it will be useful,",
                "but WITHOUT ANY WARRANTY; without even the implied warranty of",
                "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the",
                "GNU General Public License for more details.",
                "",
                "You should have received a copy of the GNU General Public License",
                "along with this program.  If not, see http://www.gnu.org/licenses/.",
                ]

# points: [Vector, Vector, ...]
# faces: [(pi, pi, pi), ], pi: point index
# color: (Red, Green, Blue), values range from 0 to 1.0
MeshVRML = namedtuple('Mesh', ['points', 'faces', 'color', 'transp'])


def shapeToMesh(shape, color, transp, scale=None):
    mesh_deviation=0.03 #the smaller the best quality, 1 coarse; 0.03 good compromise :)
    mesh_data = shape.tessellate(mesh_deviation)
    points = mesh_data[0]
    if scale != None:
        points = map(lambda p: p*scale, points)
    newMesh= MeshVRML(points = points,
                      faces = mesh_data[1],
                      color = color, transp=transp)
    return newMesh

def writeVRML(objects, filepath):
    """Export given list of Mesh objects to a VRML file.
    `Mesh` structure is defined at root.
    """

    #print "writing: ",filepath
    with open(filepath, 'w') as f:
        # write the standard VRML header
        f.write("#VRML V2.0 utf8\n\n")
        for obj in objects:
            f.write("Shape { geometry IndexedFaceSet \n{ coordIndex [")
            # write coordinate indexes for each face
            f.write(','.join("%d,%d,%d,-1" % f for f in obj.faces))
            f.write("]\n") # closes coordIndex
            f.write("coord Coordinate { point [")
            # write coordinate points for each vertex
            #f.write(','.join('%.3f %.3f %.3f' % (p.x, p.y, p.z) for p in obj.points))
            f.write(','.join('%.3f %.3f %.3f' % (p.x, p.y, p.z) for p in obj.points))
            f.write("]\n}") # closes Coordinate
            #shape_col=(1.0, 0.0, 0.0)#, 0.0)
            f.write("}\n") # closes points
            #say(obj.color)
            shape_col=obj.color[:-1] #remove last item
            #say(shape_col)
            shape_transparency=obj.transp
            f.write("appearance Appearance{material Material{diffuseColor %f %f %f\n" % shape_col)
            f.write("transparency %f}}" % shape_transparency)
            f.write("}\n") # closes Shape
        #say(filepath+' written')
        #print filepath," ..written"

def exportToVRML(componentObjs, FLDR_toVrmlFile, scale=None):
    """ Exports given ComponentModel object using FreeCAD.

    `componentObjs` : a ComponentObjs list
    `fullfilePathName` : name of the FC file, extension is important
    """
    #print FLDR_toVrmlFile
    exp_name=componentObjs[0].Label

    color=[]
    Diffuse_color=[]
    transparency=[]
    for obj in componentObjs:
        color.append(Gui.ActiveDocument.getObject(obj.Name).ShapeColor)
        transparency.append(Gui.ActiveDocument.getObject(obj.Name).Transparency/100.0)
        Diffuse_color.append(Gui.ActiveDocument.getObject(obj.Name).DiffuseColor)
    i=0
    meshes=[]
    indexColor=0;
    color_vector=[]
    applyDiffuse=0
    for obj in componentObjs:
        shape1=obj.Shape
        single_color=Diffuse_color[i];
        #check lenght color
        #colors less then faces
        if(len(single_color)!=len(shape1.Faces)):
            applyDiffuse=0;
            #copy color to all faces
        #else copy singolar colors for faces
        else:
            applyDiffuse=1;
            for color in single_color:
                color_vector.append(color)
        for index in range(len(shape1.Faces)):
            singleFace=shape1.Faces[index]
            if(applyDiffuse):
                meshes.append(shapeToMesh(singleFace, color_vector[indexColor], transparency[i], scale))
            else:
                meshes.append(shapeToMesh(singleFace, single_color[0], transparency[i], scale))
            indexColor=indexColor+1
            #meshes.append(shapeToMesh(face, Diffuse_color[i], transparency[i], scale))
        color_vector=[]
        indexColor=0;
        i=i+1
    writeVRML(meshes, FLDR_toVrmlFile)
    return


def meshFace(shape, scale=None):
    faces = []
    mesh_data = shape.tessellate(0.03) # the number represents the precision of the tessellation

    for tri in mesh_data[1]:
        face = []
        for i in range(3):
            vindex = tri[i]
            face.append(mesh_data[0][vindex])
        faces.append(face)
    m = Mesh.Mesh(faces)

    if scale != None:
        mat = App.Matrix()
        mat.scale(scale,scale,scale)
        m.transform(mat)
    return m


def exportToPOVRAY(projectObjects,FLDR_toPOVrayFile, scale=None):
    outPutString = ""
    #
    for i in projectObjects:  # objects in document
        try:
            objectColors = i.ViewObject.DiffuseColor
            shape = i.Shape.Faces
        except:
            continue

        if len(i.Shape.Faces) == 0:
            continue

        outPutString += "mesh2 {\n"
        ##################
        indexList = []
        vertexList = []
        colorsDeclaration = {}
        nr = 0
        for j in range(len(i.Shape.Faces)):
            # get face color
            if len(objectColors) == len(i.Shape.Faces):
                modelType = objectColors[j]
            else:
                modelType = objectColors[0]

            if not modelType in colorsDeclaration:
                colorsDeclaration[modelType] = []
            ######
            mesh = meshFace(i.Shape.Faces[j],scale)

            for pp in mesh.Facets:
                colorsDeclaration[modelType].append(nr)
                nr += 1

                num = len(vertexList)
                for kk in pp.Points:
                    vertexList.append("\t<{0}, {1}, {2}>".format(kk[0], kk[1], -kk[2]))
                indexList.append([num, num + 1, num + 2])
        #
        outPutString += "vertex_vectors {\n"
        outPutString += "\t{0},\n".format(len(vertexList))
        outPutString += (',\n').join(vertexList)
        outPutString += "\n}\n\n"
        ##################
        outPutString += "texture_list {\n"
        outPutString += "\t{0},\n".format(len(colorsDeclaration.keys()))

        for j in colorsDeclaration.keys():
            outPutString += "\ttexture{pigment{rgb <%.2f, %.2f, %.2f>}}\n" % (j[0], j[1], j[2])

        outPutString += "}\n"
        ##################
        outPutString += "face_indices {\n"
        outPutString += "\t{0},\n".format(len(vertexList) / 3)
        for i in range(len(indexList)):
            faceColor = [k for k, l in colorsDeclaration.items() if i in l]
            faceColor = colorsDeclaration.keys().index(faceColor[0])
            outPutString += "\t<{0}, {1}, {2}>, {3}, \n".format(indexList[i][0], indexList[i][1], indexList[i][2], faceColor)

        outPutString += "}\n"
        ##################
        outPutString += "\n}\n"

    plik = __builtin__.open(FLDR_toPOVrayFile, "w")
    plik.write('''
    // Persistence of Vision Ray Tracer Scene Description File
    // for FreeCAD (http://www.freecadweb.org)

    #version 3.6;

    #include "colors.inc"
    #include "metals.inc"
    #include "rad_def.inc"

    global_settings {
        radiosity {
            Rad_Settings(Radiosity_Normal,off,off)
        }

        //ambient_light <0.2,0.2,0.2>
        assumed_gamma 1.4
    }

    #default {finish{ambient 0}}
    background { color rgb <0.75, 0.8, 0.8> }

    // Standard finish
    #declare StdFinish = finish { crand 0.01 diffuse 0.8 };

    // declares positon and view direction
    // Generated by FreeCAD (http://www.freecadweb.org/)
    #declare cam_location =  <15,-15,-15>;
    #declare cam_look_at  = <0.0,0.0,1.0>;
    #declare cam_sky      = <-1,1,0>;
    #declare cam_angle    = 35;
    camera {
        location  cam_location
        sky       cam_sky
        look_at   cam_look_at
        angle     cam_angle
        rotate <0, 0, 0>
        right x*600/600
        blur_samples 10
        aperture 1
        focal_point <0,0,0>
    }

    //yellowish front/side light
    light_source {
        <12, -6, -12>//cam_location
        color <1,0.9,0.6>
        area_light <5, 0, 0>, <0, 5, 0>, 4, 4
        adaptive 1
        jitter
    }

    //blue backlight
    light_source {
        <-12, -6, -18>//cam_location
        color <0.4,0.5,0.9>
        area_light <3, 0, 0>, <0, 3, 0>, 4, 4
        adaptive 1
        jitter
    }
    ''')
#    plik.write( RaytracingGui.povViewCamera() + "\n")
    plik.write(outPutString + "\n")
    plik.close()




def FNCT_modify_step(PMBL_stepfile,
                     DICT_positions,
                     LIST_license,
                     FNME_stepfile,
                     STR_licAuthor,
                     STR_licEmail,
                     STR_licOrgSys,
                     STR_licPreProc,
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
            PMBL_modstepfile.append("/* description */ ('model of " + str(FNME_stepfile) + "'),")
            STR_description = pyparsing.nestedExpr("/*", "*/").suppress().transformString(STR_description)
            PMBL_modstepfile.append("/* implementation_level */ " + STR_description[-len("'2;1');"):])
            PMBL_modstepfile.append("")
            #NAME
            PMBL_modstepfile.append("FILE_NAME(")
            PMBL_modstepfile.append("/* name */ '" + str(FNME_stepfile) + ".stp',")
            STR_TS = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            PMBL_modstepfile.append("/* time_stamp */ '" + STR_TS + "',")
            PMBL_modstepfile.append("/* author */ ('" + STR_licAuthor + "','" + STR_licEmail + "'),"),
            PMBL_modstepfile.append("/* organization */ (''),")
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


def FNCT_modify_vrml(PMBL_vrmlfile,
                     DICT_positions,
                     LIST_license,
                     FNME_vrmlfile,
                     STR_licAuthor,
                     STR_licEmail,
                     STR_licOrgSys,
                     STR_licPreProc,
                     ):
    """
    DICT_positions:
    V .. VRML line
    GS .. Group/Shape start
    """
    PMBL_modvrmlfile = []
    STR_description = ""
    STR_schema = ""
    for line in range(DICT_positions["GS"]):
        if line < DICT_positions["V"]: # leave ISO/HEADER alone
            PMBL_modvrmlfile.append(PMBL_vrmlfile[line].strip())
        if line == DICT_positions["V"]: # add license
            PMBL_modvrmlfile.append("")
            PMBL_modvrmlfile.append("# LICENSE")
            PMBL_modvrmlfile.append("# " + str(FNME_vrmlfile) + " 3D VRML model for use in ECAD systems")
            for licline in LIST_license:
                PMBL_modvrmlfile.append("# " + licline)
            PMBL_modvrmlfile.append("#")
            # DESCRIPTION
            PMBL_modvrmlfile.append("# METADATA")
            PMBL_modvrmlfile.append("# description 'model of " + str(FNME_vrmlfile) + "'")
            PMBL_modvrmlfile.append("# filename '" + str(FNME_vrmlfile) + ".wrl'")
            STR_TS = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            PMBL_modvrmlfile.append("# time_stamp '" + STR_TS + "'")
            PMBL_modvrmlfile.append("# author ('" + STR_licAuthor + "','" + STR_licEmail + "')"),
            PMBL_modvrmlfile.append("# organization ('')")
            PMBL_modvrmlfile.append("# preprocessor_version '" + STR_licPreProc + "'")
            PMBL_modvrmlfile.append("# originating_system '" + STR_licOrgSys + "'")
            PMBL_modvrmlfile.append("# authorisation ''")
    PMBL_modvrmlfile.append("")
    return(PMBL_modvrmlfile)


def FNCT_md5_for_file(FNME_file, NMBR_block_size=8192):
    md5 = hashlib.md5()
    while True:
        data = FNME_file.read(NMBR_block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()



if __name__=='__main__':

    # if exist, read old md5 hash file in list for comparison
    # so we don't work on already good files
    try:
        HDLR_hashfile = open(FLDR_toStepFiles + FNME_hashfile, 'r') # open
        HDLR_hashfile.seek(0)
        LIST_md5Hashes = HDLR_hashfile.readlines()
        HDLR_hashfile.close()
    except:
        # no file there, start from scratch
        LIST_md5Hashes = []
        print "broken_1, no hashfile there"
    DICT_md5Hashes = {}
    for item in LIST_md5Hashes:
        DICT_md5Hashes[item.split(";")[0]] = item.split(";")[1].strip()

    # modify STEP files if needed
    LIST_stepfiles = os.listdir(FLDR_toStepFiles)
    LIST_stepfiles_clean = []
    for FNME_stepfile in LIST_stepfiles:
        if os.path.isfile(FLDR_toStepFiles + FNME_stepfile) == 1: # test if folder or file..
            if FNME_stepfile[-3:] == "stp": # test if step file
                FLAG_makeTransparent = False
                if FNME_stepfile[-6:-4] != "_T": # test if transparency manipulation is needed
                    FLAG_makeTransparent = True
                LIST_stepfiles_clean.append(FNME_stepfile[:-4])
                try:
                    HDLR_stepfile = open(FLDR_toStepFiles + FNME_stepfile, 'r') # open
                except:
                    print "broken_2"
                STR_md5Hash = str(FNCT_md5_for_file(HDLR_stepfile))

                #search for stepfile in old md5 hash list, compare hashes
                FLAG_workFile = False
                if FNME_stepfile[:-4] in DICT_md5Hashes.keys():
                    if DICT_md5Hashes.get(FNME_stepfile[:-4]) != STR_md5Hash:
                        FLAG_workFile = True #got changed step file here
                else:
                    FLAG_workFile = True #new step file here

                if FLAG_workFile == True:
                    print "=======================================================================================\nworking on: ",FNME_stepfile
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
                                                 FNME_stepfile[:-4],
                                                 STR_licAuthor,
                                                 STR_licEmail,
                                                 STR_licOrgSys,
                                                 STR_licPreProc,
                                                 )

                    # overwrite step file
                    try:
                        HDLR_stepfile_w = open(FLDR_toStepFiles + FNME_stepfile, 'w') # open
                    except:
                        print "broken_3"
                    else:
                        # overwrite with new preamble
                        for line in LIST_PMBL:
                            HDLR_stepfile_w.write(line + "\n")
                        # add old data section
                        for line in PMBL_stepfile[(DICT_positions["A"]-1):]:
                            HDLR_stepfile_w.write(line.strip() + "\n")
                        HDLR_stepfile_w.close()

                    # load STEP model, manipulate and save as VRML
                    FreeCAD.newDocument("Unnamed")
                    FreeCAD.setActiveDocument("Unnamed")
                    ImportGui.insert(FLDR_toStepFiles + FNME_stepfile,"Unnamed")
                    FNME_vrmlfile = FNME_stepfile[:-4] + ".wrl"
                    FNME_povfile = FNME_stepfile[:-4] + ".pov"
                    # change display mode
                    for part in FreeCAD.ActiveDocument.Objects:
                        part.ViewObject.DisplayMode = 1 #Shaded
                    if FLAG_makeTransparent: # if transparency is needed
#                        from PySide import QtGui
#                        QtGui.QInputDialog.getText(None, "Get text", "Input:")[0]
                        pass
                    objs=[] # select all parts
                    for part in FreeCAD.ActiveDocument.Objects:
                        objs.append(part)

                    exportToVRML(objs,(FLDR_toVrmlFiles + FNME_vrmlfile), 0.3937)

                    # before exporting to POVray, scale and move to fit standard camera view & light setup
                    bb = App.BoundBox();
                    for part in objs:
                        bb.add( part.Shape.BoundBox )
                    # calculate scale
                    newScale = 10.0/(max(bb.XLength,bb.YLength,bb.ZLength))
                    # calculate transformation
                    newCentre = FreeCAD.Vector(-(bb.XMin + bb.XMax)/2,-(bb.YMin + bb.YMax)/2,-(bb.ZMin + bb.ZMax)/2)
                    for part in objs:
                        part.Placement.Base = newCentre

                    PATH_ToPOVrayFile = FLDR_toPOVrayFiles + FNME_povfile
                    exportToPOVRAY(objs,PATH_ToPOVrayFile, newScale)
                    # start povray and render scene
                    subprocess.call([PATH_POVrayExecutable,"/EXIT","+I"+PATH_ToPOVrayFile,"+W"+IMG_W,"+H"+IMG_H])

                    del objs
                    FreeCAD.closeDocument("Unnamed")

                    # add license stuff to fresh VRML file
                    print "saved VRML, now adding license: ",FNME_vrmlfile
                    try:
                        HDLR_vrmlfile = open(FLDR_toVrmlFiles + FNME_vrmlfile, 'r') # open
                    except:
                        print "broken_4"
                    else:
                        HDLR_vrmlfile.seek(0)
                        PMBL_vrmlfile = HDLR_vrmlfile.readlines()
                        HDLR_vrmlfile.close()
                        CNT_cutoff = 0
                        DICT_positions = {}
                        for line in PMBL_vrmlfile:
                            CNT_cutoff += 1
                            if line[:15] == "#VRML V2.0 utf8":
                                DICT_positions["V"] = CNT_cutoff
                            elif line[:7] == "Group {":
                                DICT_positions["GS"] = CNT_cutoff
                            elif line[:7] == "Shape {":
                                DICT_positions["GS"] = CNT_cutoff
                                break

                        LIST_PMBL = FNCT_modify_vrml(PMBL_vrmlfile[:DICT_positions["GS"]],
                                                     DICT_positions,
                                                     LIST_license,
                                                     FNME_vrmlfile[:-4],
                                                     STR_licAuthor,
                                                     STR_licEmail,
                                                     STR_licOrgSys,
                                                     STR_licPreProc,
                                                     )

                        # overwrite vrml file
                        try:
                            HDLR_vrmlfile_w = open(FLDR_toVrmlFiles + FNME_vrmlfile, 'w') # open
                        except:
                            print "broken_5"
                        else:
                            # overwrite with new preamble
                            for line in LIST_PMBL:
                                HDLR_vrmlfile_w.write(line + "\n")
                            # add old data section
                            for line in PMBL_vrmlfile[(DICT_positions["GS"]-1):]:
                                HDLR_vrmlfile_w.write(line)
                            HDLR_vrmlfile_w.close()

                else:
                    HDLR_stepfile.close()

    # rewrite hash file when done
    if LIST_stepfiles_clean:
        LIST_stepfiles_clean.sort()
        try:
            HDLR_hashfile_w = open(FLDR_toStepFiles + FNME_hashfile, 'w') # open
        except:
            print "broken_6"
        else:
            print "writing new hashfile"
            for FNME_stepfile_clean in LIST_stepfiles_clean:
                try:
                    HDLR_stepfile_r = open(FLDR_toStepFiles + FNME_stepfile_clean + ".stp", 'r') # open
                except:
                    print "broken_7"
                else:
                    HDLR_hashfile_w.write(FNME_stepfile_clean + ";" + str(FNCT_md5_for_file(HDLR_stepfile_r)) + "\n")
                    HDLR_stepfile_r.close()
            HDLR_hashfile_w.close()

    print "done"

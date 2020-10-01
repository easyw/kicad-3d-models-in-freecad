#!/bin/sh

# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
cd $SCRIPTPATH
echo Best using FC 0.18
#freecad  main_generator.py  R_Axial_Power_L60.0mm_W14.0mm_P66.04mm
FreeCAD  main_generator.py $1

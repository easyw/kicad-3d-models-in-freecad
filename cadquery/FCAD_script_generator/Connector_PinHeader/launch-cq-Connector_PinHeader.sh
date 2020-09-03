#!/bin/sh

# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
cd $SCRIPTPATH
#FreeCAD  main_generator.py
FreeCAD main_generator.py PinHeader_1xyy_P2.54mm_Vertical 10,17


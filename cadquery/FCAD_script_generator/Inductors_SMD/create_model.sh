#!/bin/sh

echo "Working example with FreeCAD_0.19-16854-Linux-Conda_Py3Qt5_glibc2.12-x86_64.AppImage"
# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
cd $SCRIPTPATH
echo "Best using FC >= 0.18"
#freecad  main_generator.py 0402
## freecad  main_generator.py $1

if [ -z $1 ]; #missing parameter
then ~/Downloads/FreeCAD_0.19-16854-Linux-Conda_Py3Qt5_glibc2.12-x86_64.AppImage  main_generator.py L_Vishay_IHSM-7832 # echo Ciao
else ~/Downloads/FreeCAD_0.19-16854-Linux-Conda_Py3Qt5_glibc2.12-x86_64.AppImage  main_generator.py $1 # echo bao
fi

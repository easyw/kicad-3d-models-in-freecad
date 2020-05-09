#!/bin/sh

# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
cd $SCRIPTPATH
echo Best using FC 0.19
#freecad  main_generator.py QFN-28-1EP_6x6mm_Pitch0.65mm
freecad main_generator.py $1

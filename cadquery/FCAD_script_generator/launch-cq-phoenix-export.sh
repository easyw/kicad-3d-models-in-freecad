#!/bin/sh

# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
echo $SCRIPTPATH
cd $SCRIPTPATH
#FreeCAD export_conn_phoenix.py MSTB_01x02_GF_5.00mm_MH
FreeCAD export_conn_phoenix.py all
#FreeCAD export_conn_phoenix.py MC_01x04_GF_3.5mm_MH

#!/bin/bash

if [ $# -ne 2 ]
then 
 echo "Usage: ./extract.sh <videofile> <directoryslug>"
 exit -1
fi

mkdir $2
pushd $2
mplayer -vo png:5 -vf framestep=96,scale=64:48 -nosound $1
popd

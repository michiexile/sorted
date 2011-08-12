#!/bin/bash

if [ $# -ne 2 ]
then 
 echo "Usage: ./extract.sh <videofile> <directoryslug>"
 exit -1
fi

mkdir $2
pushd $2
mplayer -vo png:z=5 -vf frameskip=96,scale=64x48 $1
popd

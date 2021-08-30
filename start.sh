#!/bin/bash

test=`cat /home/twitter/ecnitoctoc/launch.status`
if [ $test = "0" ]
then
    python /home/twitter/ecnitoctoc/launch.py
else
    echo "programe en cours"
fi
exit

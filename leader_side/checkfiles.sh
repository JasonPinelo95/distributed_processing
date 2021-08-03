#!/bin/bash

echo "Waiting for files..."

FLAG=0
FILE=processedFiles/node_2.csv

while [ $FLAG -eq 0 ]
do
        if test -e "$FILE"; then
                sleep 30
                FLAG=1
                python unifyNodes.py
        fi
done

MAP_CA=django_files/Covid_Map/Covid_Map/templates/map_ca.html
MAP_DEF=django_files/Covid_Map/Covid_Map/templates/map_def.html

echo "Removing old maps"

if test -e "$MAP_CA"; then
        rm $MAP_CA
fi

if test -e "$MAP_DEF"; then
        rm $MAP_DEF
fi

python genMaps.py
docker-compose restart web


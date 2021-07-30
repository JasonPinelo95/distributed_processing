#!/bin/bash

echo "Waiting for files..."

FLAG=0
FILE=processedFiles/node_2.csv

while [ $FLAG -eq 0 ]
do
        if test -e "$FILE"; then
                sleep 7
                FLAG=1
                python unifyNodes.py
        fi
done


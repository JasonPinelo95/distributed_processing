#!/bin/bash
  
# This script helps to check if a file existe in remote server through ssh
# Change user and ssh path as corresponding

FLAG=0
while [ $FLAG -eq 0 ]
do
        if ssh -i ~/.ssh/node0 node0@34.122.137.68 "test -e covid_project/files/ready"; then
                FLAG=1
                python processFiles.py
        fi
done

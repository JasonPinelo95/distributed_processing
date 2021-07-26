#!/bin/bash
# USER AND FILE ARE PASSED AS ARGUMENTS
USER=$1
DOWN_FILE=$2

scp -i ~/.ssh/$USER $USER@34.133.161.216:covid_project/files/$DOWN_FILE ./partition
cd ./partition
unzip $DOWN_FILE
rm $DOWN_FILE

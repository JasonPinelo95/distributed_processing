#!/bin/bash
# USER AND FILE ARE PASSED AS ARGUMENTS
USER=$1
DOWN_FILE=$2

mkdir partition
mkdir processed

scp -i ~/.ssh/$USER $USER@34.122.137.68:covid_project/files/$DOWN_FILE ./partition
cd ./partition
unzip $DOWN_FILE
rm $DOWN_FILE

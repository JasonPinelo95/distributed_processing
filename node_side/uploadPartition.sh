#!/bin/bash

USER=$1
DOWN_FILE=$2
UP_FILE=$3


scp -i ~/.ssh/$USER ./processed/$UP_FILE $USER@34.122.137.68:covid_project/processedFiles
rm ./partition/$DOWN_FILE
rm ./processed/$UP_FILE
rm -rf partition
rm -rf processed



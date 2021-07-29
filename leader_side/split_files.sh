#!/bin/bash

# Making directory to save splitted files
mkdir files
mkdir processedFiles
echo "Splitting file..."

# Moving to that directory and split big file
cd files

NUMBER=$(wc -l < ../covid.csv)
DIVISION=$(echo $((NUMBER/3+1)))

split -dl $DIVISION --additional-suffix=.csv ../covid.csv covid_
echo "Done"

FILES="*.csv"

# Getting header
cat ../covid.csv | head -n 1 > header.csv

# Adding header to splitted and zippping generated files
COUNTER=0
for f in $FILES
do
        if [[ "header.csv" = "$f" ]]; then
                continue
        fi

        if [[ "covid_00.csv" = "$f" ]]; then
                echo "Processing $f file..."
                zip covid_${COUNTER}.zip $f
                rm $f
                let COUNTER++
                continue
        fi
        echo "Processing $f file..."
        cat header.csv $f > tmp
        mv tmp $f
        zip covid_${COUNTER}.zip $f
        rm $f
        let COUNTER++

done

# Remove temporal header

rm header.csv
rm ../covid.csv
touch ready


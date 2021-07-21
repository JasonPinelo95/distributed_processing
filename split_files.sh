#!/bin/bash

# Making directory to save splitted files
mkdir files
echo "Splitting file..."

# Moving to that directory and split big file
cd files
split -dn 3 --additional-suffix=.csv ../covid.csv covid_
echo "Done"

FILES="*.csv"

# Getting header
cat ../covid.csv | head -n 1 > header.csv

# Adding header to splitted files

for f in $FILES
do	
	if [[ "covid_00.csv" = "$f" ]]; then
		continue
	fi
	echo "Processing $f file..."
	cat header.csv $f > tmp 
	mv tmp $f
	
done

# Remove temporal header

rm header.csv

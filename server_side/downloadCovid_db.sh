#!/bin/bash

#This script helps to download the official covid database

wget http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip
unzip datos_abiertos_covid19.zip
mv *COVID19* covid.csv
rm datos_abiertos_covid19.zip

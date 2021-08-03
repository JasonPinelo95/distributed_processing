#!/usr/bin/env python
# coding: utf-8

# # Version for Django

# In[1]:


# Importing Modules
from plotly.graph_objs import Choropleth
from plotly import graph_objs as go
from urllib.request import urlopen
import json
import pandas as pd
from datetime import datetime


# In[2]:
print("Generating Maps...")

# Function to get current Date 
def current_date_format():
    date = datetime.now()
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "el {} de {} del {}".format(day, month, year)

    return messsage


# In[3]:


# Load GeoJson
with urlopen('https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json') as response:
    mx_regions_geo = json.load(response)

# Make Data Frame from CSV File
df = pd.read_csv('./processedFiles/covid_data.csv')

# Get Current Date
date = current_date_format()


# ---
# ## Defunciones Map 

# In[4]:


# Make Choropleth Figure
fig = go.Figure(Choropleth(geojson = mx_regions_geo, locations = df.Estados, z=df.Defunciones,
                              colorscale="OrRd",featureidkey='properties.name'))

# Update Geo
fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

# Update Layout
fig.update_layout(
    title_text = 'Defunciones por COVID-19 en México ' + date,
    font=dict(
        family="Ubuntu",
        size=18,
        color="#7f7f7f"
        ),
        annotations = [dict(
            x=0.55,
            y=-0.1,
            xref='paper',
            yref='paper',
            text='Fuente Oficial: <a href="https://www.gob.mx/salud/documentos/datos-abiertos-152127">\
                Datos Abiertos Dirección General de Epidemiología </a>',
            showarrow = False
    )]
)

# Show Figure
fig.show()

# Save Figure has HTML File
fig.write_html("django_files/Covid_Map/Covid_Map/templates/map_def.html")


# ---
# ## Casos Activos Map

# In[5]:


# Make Choropleth Figure
Fig = go.Figure(Choropleth(geojson = mx_regions_geo, locations = df.Estados, z=df.Casos_activos_covid,
                              colorscale="PuBuGn",featureidkey='properties.name'))

# Update Geo
Fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

# Update Layout
Fig.update_layout(
    title_text = 'Casos Activos COVID-19 en México ' + date,
    font=dict(
        family="Ubuntu",
        size=18,
        color="#7f7f7f"
        ),
        annotations = [dict(
            x=0.55,
            y=-0.1,
            xref='paper',
            yref='paper',
            text='Fuente Oficial: <a href="https://www.gob.mx/salud/documentos/datos-abiertos-152127">\
                Datos Abiertos Dirección General de Epidemiología </a>',
            showarrow = False
    )]
)

# Show Figure
Fig.show()

# Save Figure has HTML File
Fig.write_html("django_files/Covid_Map/Covid_Map/templates/map_ca.html")


# In[ ]:





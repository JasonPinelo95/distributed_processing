from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter, Choropleth
from plotly import graph_objs as go
from urllib.request import urlopen
import json
import pandas as pd

# Vista Home
def home(request):
     return render(request,'home.html')
     # url = http://localhost:8000/home/

# Vista Test (plot de plotly en django)
def index(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "index.html", context={'plot_div': plot_div})
    # url = http://localhost:8000/test/

# Vista Mapa Covid Defunciones
def map_defuciones(request):
     return render (request,'defunciones.html')
     # url = http://localhost:8000/defunciones/

# Vista Mapa Casos Covid
def map_casos(request):
     return render (request,'casos.html')
     # url = http://localhost:8000/casos/
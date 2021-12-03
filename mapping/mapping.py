import folium
import pandas

map = folium.Map(location=[38.58, -99.09],zoom_start=5,tiles="Stamen Terrain")

def getElevationColor(elevation):
    if elevation < 1000:
        return 'blue'
    elif 999 < elevation < 2000:
        return 'green'
    elif 1999 < elevation < 3000:
        return 'orange'
    else:
        return 'red'

## Add elements from a file using pandas
data = pandas.read_csv("Volcanoes.txt",sep=',')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

## As above, but using HTML in the popup...
html = """<h4>Volcano information:</h4>
Height: %s m
Height: %s m
"""

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % (str(el), str(el)), width=200, height=100)
    
    ## Enhancement to call color-setting function based on elevation...
    fgv.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(icon='fire',radius=6,color=getElevationColor(el))))

#use 'GeoJson' to add an extra layer that makes polygons from the input file specifying all countries of world
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000001 < x['properties']['POP2005'] < 20000000 else 'red'}))

#note - can add both layers to single feature group. But for control, may be better to add to sepatate groups

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) #add option to control each layer
map.save("Map1.html")
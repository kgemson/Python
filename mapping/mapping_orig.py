import folium
import pandas

map = folium.Map(location=[38.58, -99.09],zoom_start=5,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

def getElevationColor(elevation):
    if elevation < 1000:
        return 'blue'
    elif elevation < 2000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

## Add elements individually
#fg.add_child(folium.Marker(location=[54.1,-6.19], popup="Bollocks", icon=folium.Icon(color='green')))
#fg.add_child(folium.Marker(location=[54.0,-6.21], popup="Bollocks", icon=folium.Icon(color='green')))

## Add elements through a loop
#for coords in [[54.1,-6.19],[54.0,-6.21],[54.05,-6.20]]:
#    fg.add_child(folium.Marker(location=coords, popup="Marker", icon=folium.Icon(color='green')))

## Add elements from a file using pandas
data = pandas.read_csv("Volcanoes.txt",sep=',')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

## Use 'zip' function to pair up elements of list and display ...
#for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location=[lt,ln], popup="Elevation: "+str(el)+" m", icon=folium.Icon(color='green')))

## As above, but using HTML in the popup...
html = """<h4>Volcano information:</h4>
Height: %s m
Height: %s m
"""
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % (str(el), str(el)), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

    ## Enhancement to call color-setting function based on elevation...
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(icon='fire',radius=6,color=getElevationColor(el))))

map.add_child(fg)
map.save("Map1.html")
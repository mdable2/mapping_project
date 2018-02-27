import folium
import pandas

# Read in data file with coordinates of USA volcanoes
data = pandas.read_csv("Volcanoes_USA.txt")

# Calculate what color the marker should be based on elevation
def what_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# Create a list of latitudes, longitudes, and elevation from data
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location = [42.001377, -114.117143], zoom_start = 5)

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " m",
                    fill_color = what_color(el), color = 'grey', fill_opacity = 0.7, fill = True))

fgp = folium.FeatureGroup(name = "Population")

# Read in population and line coordinates of each country in the world
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Add layers to map object
map.add_child(fgv)
map.add_child(fgp)

# Add layer control to map
map.add_child(folium.LayerControl())

map.save("Map1.html")

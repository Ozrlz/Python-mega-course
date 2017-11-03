# -*- coding: utf-8 -*-

import folium, pandas

data = pandas.read_csv('volcanoes.csv')
names = list(data['NAME'])
lats = list(data['LAT'])
lons = list(data['LON'])
alts = list(data['ELEV'])


def getColorPerElevation(elevation):
	if elevation < 1000:
		return 'green'
	elif elevation <3000:
		return 'orange'
	else:
		return 'red'

house_coords = [20.666954, -103.284624]

map_object = folium.Map(location=[lats[0],lons[0]], zoom_start=7, tiles="OpenStreetMap")

folium_feature_group = folium.FeatureGroup(name='FeatureGroup1')

for name, la, lo, alt in zip(names, lats, lons, alts):
	#folium_feature_group.add_child(folium.Marker(location=[la, lo],popup=folium.Popup(name, parse_html=True) , icon=folium.Icon(color='red')))
	folium_feature_group.add_child(folium.Circle(location=[la, lo], radius=10000, 
		color='gray', fill=True, fill_color=getColorPerElevation(alt), fill_opacity=0.7,popup=folium.Popup(name, parse_html=True)))
	print (name, type(name))

map_object.add_child(folium_feature_group)


map_object.save('Map01.html')
#map_object.add_child(folium.Marker([20.666954, -103.284624], 'Marcador, paps :v', folium.Icon('blue')))
#map_object.add_child(folium.Marker(location=[20.669383, -103.282448], popup='Este es un marcador, papu :v', icon=folium.Icon('Red')))

# -*- coding: utf-8 -*-

import folium

class DrawableMap():
	"""
	This class stores a folium.Map object, some folium.FeatureGroup's 
	and its childs (circles, markers and so on).
	"""

	def __init__(self, lat=20.666954, lon=-103.284624, zoom_start=10, tiles="OpenStreetMap"):
		"""
		Initialize the map with some initial position, zoom and type
		"""
		self.map = folium.Map(location=[lat, lon], zoom_start=zoom_start, tiles=tiles)
		self.markers = folium.FeatureGroup(name='Volcanoes')
		self.population = folium.FeatureGroup(name='Population')


	def addAllFeatureGroups(self):
		self.map.add_child(self.markers)
		self.map.add_child(self.population)
		self.map.add_child(folium.LayerControl())
		return True

	def addCircle(self, location=[20.666954, -103.284624], radius=10000, 
		color='gray', fill=True, fill_color='green', fill_opacity=0.7, 
		popup=''):
		self.markers.add_child(folium.Circle(location=location, radius=radius, color=color,
			fill=fill, fill_color=fill_color, fill_opacity=fill_opacity, popup=popup))
		return True

	def addGeoJson(self):
		self.population.add_child(folium.GeoJson( open('../files/world.json', 'r', encoding='utf-8-sig').read(), 
		style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 100000000
		else 'orange' if 1000000000 <= x['properties']['POP2005'] < 2000000000 else 'red'} ))

	def saveMap(self, filename='map.html'):
		#Check whether the filename has extension or not, if not then add it
		if filename[-5:] != '.html':
			filename = filename+'.html'

		self.map.save(filename)
		return True

if __name__ == '__main__':
	mapa = DrawableMap()
	mapa.addCircle(radius=1000)
	mapa.addAllFeatureGroups()
	mapa.saveMap('mapene')
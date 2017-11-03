# -*- coding: utf-8 -*-

from volcanoes import Volcanoes
from drawable_map import DrawableMap
import folium

class Manager():
	"""
	This class manages the interaction between the volcanoes and the map
	"""

	def __init__(self, lat=20.666954, lon=-103.284624, zoom_start=10, tiles="OpenStreetMap"):
		self.volcanoes = Volcanoes('../files/volcanoes.csv')
		self.volcanoes.printVolcanoes() # --debug
		self.map = DrawableMap(lat=lat, lon=lon, zoom_start=zoom_start, tiles=tiles)

	def addCircleMarkers(self, radius=1000, color='gray'):
		for volcano in self.volcanoes.volcanoes:
			self.map.addCircle(location=[volcano.latitude, volcano.longitude], radius=radius, color=color,
				fill=True, fill_color=volcano.getElevationColor(), fill_opacity=0.77, 
				popup=folium.Popup(volcano.name, parse_html=True))

	def closeMap(self, filename='map.html'):
		self.map.addAllFeatureGroups()
		self.map.saveMap(filename)

if __name__ == '__main__':
	manager = Manager()
	manager.addCircleMarkers(10000, 'blue')
	manager.map.addGeoJson()
	manager.closeMap()


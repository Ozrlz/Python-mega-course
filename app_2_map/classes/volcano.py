# -*- coding: utf-8 -*-

class Volcano():
	"""
		This class represents an abstraction of a volcano, with the latitude and longitude, its name
		and its elevation


	"""
	def __init__(self, lat, lon, name, elev):
		self.latitude = lat
		self.longitude = lon
		self.name = name
		self.elevation = elev

	def getElevationColor(self):
		if self.elevation < 1000:
			return 'green'
		elif self.elevation <3000:
			return 'orange'
		else:
			return 'red'

	def printInfo(self):
		print ("Name: ",self.name)
		print ("Longitude: ",self.longitude)
		print ("Latitude: ",self.latitude)
		print ("Elevation: ",self.elevation)

if __name__ == '__main__':
	pass
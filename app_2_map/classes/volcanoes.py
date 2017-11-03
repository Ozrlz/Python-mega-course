# -*- coding: utf-8 -*-

import pandas
from volcano import Volcano

class Volcanoes():
	"""
		This class represents an array of volcanoes with all the methods for fetching the info from 
		a csv file and create the array of volcanoes.

		['NAME', 'ELEV', 'LAT', 'LON']
	"""
	def __init__(self, filename=''):
		# Fetch columns of the csv into a pandas dataframe, then convert the dataframe into a python list
		df_names = pandas.read_csv(filepath_or_buffer=filename, usecols=['NAME'])['NAME'].values
		df_elevs = pandas.read_csv(filepath_or_buffer=filename, usecols=['ELEV'])['ELEV'].values
		df_lats = pandas.read_csv(filepath_or_buffer=filename, usecols=['LAT'])['LAT'].values
		df_lons = pandas.read_csv(filepath_or_buffer=filename, usecols=['LON'])['LON'].values

		#Create an empty list of volcanoes, for appending later the new volcanoes
		self.volcanoes = []

		#Iterate over the lists fetched to create the array of volcanoes
		for index in range(len(df_names)):
			self.volcanoes.append(Volcano(lat=df_lats[index], lon=df_lons[index], name=df_names[index], elev=df_elevs[index]))

	def printVolcanoes(self):
		for volcano in self.volcanoes:
			volcano.printInfo()
			print ('_'*50)

if __name__ == '__main__':
	test = Volcanoes('/home/oscar/Documentos/Python/app_2_map/zip_file/volcanoes.csv')
	test.printVolcanoes()
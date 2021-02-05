#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import pandas as pd
from geopy.geocoders import Nominatim
import sqlite3


#Obtiene la ubicacion dadas las cooredenadas 
def geolocaliza(coordenadas):
	geolocator = Nominatim(user_agent="prueba")
	location = geolocator.reverse(coordenadas)
	try:
		ubica = location[0]
	except:
		ubica = 'N/A'
	return ubica

#Creacion de la Base de datos
def crea_base(data):
	print("Creando Base de Datos...")
	conn = sqlite3.connect('TestDB.db')
	c = conn.cursor()
	c.execute('CREATE TABLE MBUS (id number, date_updated timestamp, vehicle_id number, vehicle_label number, vehicle_current_status number, position_latitude number, position_longitude number, geographic_point number, position_speed number, position_odometer number, trip_schedule_relationship number, trip_id number, trip_start_date number, trip_route_id number, alcaldia text, ubicacion text)')
	conn.commit()
	data.to_sql('MBUS', conn, if_exists='replace', index = False)
	return

if __name__ == '__main__':
	
	#Lectura de archivo csv 
	data = pd.read_csv('prueba_fetchdata_metrobus2801.csv')
	#Generamos una lista para los valore de ls coordenadas geograficas
	list_aux = list(data['geographic_point'])
	#Se forman dos listas con los valores de ubicacion y alcaldia
	print("Generacion ubicaciones...")
	ubicacion = [geolocaliza(i) for i in list_aux]
	alcaldia = []
	print("Generacion alcaldias...")
	for location in ubicacion:
		try:
			alcaldia.append(location.split(',')[-4])
		except:
			alcaldia.append('N/A')
			pass

	#Anexamos las dos nuevas columnas al dataframe 
	data['alcaldia'] = alcaldia
	data['ubicacion'] = ubicacion
	#Creamos la base de datos a partir del dataset construido
	crea_base(data)


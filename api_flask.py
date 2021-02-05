#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from time import time 
import json
import requests
import sqlite3


app = Flask(__name__)

#Conexion a base de datos 
def conec():
	conn = sqlite3.connect('TestDB.db')
	cur = conn.cursor()
	return cur

#Obtiene una lista de unidades disponibles
@app.route('/api/unidades', methods=['GET'])
def get_unidades():
	cur = conec()
	cur.execute("SELECT DISTINCT vehicle_id FROM MBUS")
	list_2 = cur.fetchall()
	unidades = [i[0] for i in list_2]
	info ={
			'unidades': unidades
	}
	cur.close()
	return jsonify(info)

#Consultar los el historial de ubicaciones/fechas de una unidad dado su ID
@app.route('/api/historial/<ids>', methods=['GET'])
def get_historial(ids):
	cur = conec()
	cur.execute("SELECT date_updated, ubicacion FROM MBUS WHERE vehicle_id LIKE '%"+ids+"%'")#"+applc)
	list_2 = cur.fetchall()
	historial = [i[0] for i in list_2]
	ubicacion = [i[1] for i in list_2]
	info ={
			'historial': historial,
			'ubicacion': ubicacion

	}
	cur.close()
	return jsonify(info)

#Obtiene una lista de alcaldías disponibles
@app.route('/api/alcaldias', methods=['GET'])
def get_alcaldias():
	cur = conec()
	cur.execute("SELECT DISTINCT alcaldia FROM MBUS")
	list_2 = cur.fetchall()
	alcaldia = [i[0] for i in list_2]
	info ={
			'alcaldias': alcaldia
	}
	cur.close()
	return jsonify(info)

#Obtiene una lista de unidades que hayan estado dentro de una alcaldía
@app.route('/api/uni_alc/<name>', methods=['GET'])
def get_uni_alc(name):
	cur = conec()
	cur.execute("SELECT vehicle_id FROM MBUS WHERE alcaldia LIKE '%"+name+"%'")#"+alc)
	list_2 = cur.fetchall()
	uni_alc = [i[0] for i in list_2]
	info ={
			'unidades_alcaldia': uni_alc
	}
	cur.close()
	return jsonify(info)


if __name__ == '__main__':
	
	app.run(debug=True,port=8000)


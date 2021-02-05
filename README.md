
Ambos codigos estan desarrollados con python3.6 

Para la ejecucion de los programas es necesario instalar las siguientes bibliotecas:

	- sqlite3    
	- pandas
	- flask      
	- geopy			


Una vez instaladas el primer paso sera la creacion de la base de datos, nos posicionamos em el directorio donde guardamos
los scripts y ejecutamos lo siguiente:

	- python3 creacion_bd.py


Despues de crear la base de datos ejecutamos la api hecha con flask con el siguente comando:

	- python3  api_flask.py 


Una vez que la api se encuentre n ejecucion podemos empezar a probar de varias maneras con postman por ejemplo, desde el navegador o en una terminal. Para visualizarlo en una terminal ejecutamos los siguientes comandos:

	1.- Obtener una lista de unidades disponibles
		
		- curl -X GET http://127.0.0.1:8000/api/unidades

	2.- Consultar los el historial de ubicaciones/fechas de una unidad dado su ID
		
		- curl -X GET http://127.0.0.1:8000/api/historial/4

	3.- Obtener una lista de alcaldías disponibles
		
		- curl -X GET http://127.0.0.1:8000/api/alcaldias

	4.- Obtener una lista de unidades que hayan estado dentro de una alcaldía
		
		- curl -X GET http://127.0.0.1:8000/api/uni_alc/Miguel Hidalgo
-






 






	




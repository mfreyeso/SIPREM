# -*- coding: utf-8 -*-
import macaron
import models

class EstacionDao(object):
	"""docstring for EstacionDao"""
	def __init__(self):
		super(EstacionDao, self).__init__()
	
	def obtenerEstacion(self, estacionId):
		try:
			macaron.macaronage("siprem.db")
			estacionObtenida = models.Estacion.get(estacionId)
			return estacionObtenida
		except Exception, e:
			print e

	def cargarEstaciones(self):
		try:
			macaron.macaronage("siprem.db")
			estaciones= models.Estacion.select("estado = ?", [1])
			return estaciones
		except Exception, e:
			print e
		

	def desactivarEstacion(self, idEstacionP):
		try:
			macaron.macaronage("siprem.db")
			estacion = models.Estacion.get(idEstacionP)
			estacion.estado = 0
			macaron.bake()
		except Exception, e:
			raise e

	def crearEstacion(self, nombreEstacionP, ubicacionP, fechaOperacionP):
		response = False
		try:
			macaron.macaronage("siprem.db")
			models.Estacion.create(
				nombre = nombreEstacionP,
				ubicacion = ubicacionP,
				fechaoperacion = fechaOperacionP,
				estado = 1)
			macaron.bake()
			response = True
			return response
		except Exception, e:
			print e
			return response

	def modificarEstacion(self, estacionDaoP, nombreEstacionP, ubicacionP, fechaOperacionP):
		response = False
		try:
			macaron.macaronage("siprem.db")
			if estacionDaoP.nombre != nombreEstacionP:
				estacionDaoP.nombre = nombreEstacionP
			if estacionDaoP.ubicacion != ubicacionP:
				estacion.ubicacion = ubicacionP
			if estacionDaoP.fecha != fechaOperacionP:
				estacion.fecha != fechaOperacionP
			macaron.bake()
			response = True
			return response
		except Exception, e:
			print e
			return response

	def obtenerEstaciones(self):
		try:
			estaciones = []
			macaron.macaronage("siprem.db")
			estacionesDao = models.Estacion.all()
			for estacion in estacionesDao:
				estacionV = []
				estacionV.append(estacion)
				registros = models.Registro.select("estacion_id =?", [estacion.id]).order_by("fecha")
				if registros.count() == 0:
					cadena = "No existen registros de precipitacion de la estacion."
					print cadena
				else:
					primerRegistro = registros[0]
					ultimoRegistro = registros[registros.count()-1]
					print primerRegistro.fecha, ultimoRegistro.fecha
					cadena = "La estacion tiene registros de precipitación desde la fecha " + str(primerRegistro.fecha) + " hasta " + str(ultimoRegistro.fecha)
				estacionV.append(cadena)
				estaciones.append(estacionV)
			return estaciones
		except Exception, e:
			print e
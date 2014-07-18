import models
import macaron
import registro as reg
import datetime

class RegistroDao(object):
	"""docstring for RegistroDao"""
	def __init__(self):
		super(RegistroDao, self).__init__()

	def almacenarRegistros(self, kernelRegistrosP, estacionId):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionId)
			for registroP in kernelRegistrosP:
				if registroP.entregarPrecipitacion() != 0 and registroP.entregarPrecipitacion() != "-":
					estacionDaoP.estacionreg.append(
					fecha = str(registroP.entregarFecha()),
					hora = str(registroP.entregarHora()),
					vprec = registroP.entregarPrecipitacion()
					)
			macaron.bake()
		except Exception, e:
			print e

	def buscarRegistros(self, fechaInicialP, fechaFinalP, estacionIdP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionId)
			registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicialP, fechaFinalP])
			registros = self.transformarRegistros(registrosDao)
			return registros
		except Exception, e:
			raise e

	def transformarRegistros(self, coleccionRegistrosDaoP):
		registrosTransformados = []
		for registroD  in coleccionRegistrosDaoP:
			objRegistro = reg.registro(
				registroD.fecha,
				registroD.hora,
				registroD.vprec)
			registrosTransformados.append(objRegistro)
		return registrosTransformados

	def busquedaParametrizada(self, opcionBusquedaP, parametrosP, estacionIdP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionIdP)
			if opcionBusquedaP == 1:
				registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [parametrosP])
				registros = self.transformarRegistros(registrosDao)
				return registros
			elif opcionBusquedaP == 2:
				registrosDao = estacionDaoP.estacionreg.select("strftime('%Y-%d', fecha) = ?", [parametrosP])
				registros = self.transformarRegistros(registrosDao)
				return registros
			elif opcionBusquedaP == 3:
				registrosDao = estacionDaoP.estacionreg.select("strftime('%Y', fecha) = ?", [parametrosP])
				registros = self.transformarRegistros(registrosDao)
				return registros
			elif opcionBusquedaP == 4:
				if parametrosP[0] == 1:
					fechaInicial = datetime.date(parametrosP[1], 1, 1)
					fechaFinal = datetime.date(parametrosP[1], 6, 30)
				else:
					fechaInicial = datetime.date(parametrosP[1], 7, 1)
					fechaFinal = datetime.date(parametrosP[1], 12, 31)
				registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
				registros = self.transformarRegistros(registrosDao)
				return registros
			elif opcionBusquedaP == 5:
				#Trimestre Bimodal
				if parametrosP[0] == 1:
					fechaInicial = datetime.date((parametrosP[1]-1), 12, 1)
					fechaFinal = datetime.date(parametrosP[1], 2, self.febreroBisiesto())
				elif parametrosP[1] == 2:
					fechaInicial = datetime.date(parametrosP[1], 3, 1)
					fechaFinal = datetime.date(parametrosP[1], 5, 31)
				elif parametrosP[1] == 3:
					fechaInicial = datetime.date(parametrosP[1], 6, 1)
					fechaFinal = datetime.date(parametrosP[1], 8, 31)
				else:
					fechaInicial = datetime.date(parametrosP[1], 9, 1)
					fechaFinal = datetime.date(parametrosP[1], 11, 30)
				registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
				registros = self.transformarRegistros(registrosDao)
				return registros
			elif opcionBusquedaP == 6:
				#Trimestre Estandar
				if parametrosP[0] == 1:
					fechaInicial = datetime.date(parametrosP[1], 1, 1)
					fechaFinal = datetime.date(parametrosP[1], 3, 31)
				elif parametrosP[1] == 2:
					fechaInicial = datetime.date(parametrosP[1], 4, 1)
					fechaFinal = datetime.date(parametrosP[1], 6, 30)
				elif parametrosP[1] == 3:
					fechaInicial = datetime.date(parametrosP[1], 7, 1)
					fechaFinal = datetime.date(parametrosP[1], 9, 30)
				else:
					fechaInicial = datetime.date(parametrosP[1], 10, 1)
					fechaFinal = datetime.date(parametrosP[1], 12, 31)
				registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
				registros = self.transformarRegistros(registrosDao)
				return registros
			else:
				registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [parametrosP[0], parametrosP[1]])
				registros = self.transformarRegistros(registrosDao)
				return registros		
		except Exception, e:
			print e

	def febreroBisiesto(self, anoP):
		if( anoP % 4 == 0 and anoP % 100 != 0 or anoP % 400 == 0):
			#Ano Bisiesto
			return 29
		else:
			return 28





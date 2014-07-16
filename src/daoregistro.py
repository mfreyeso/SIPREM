import models
import macaron
import registro as reg

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

	def busquedaParametrizada(self, opcionBusquedaP, parametrosP):
		try:
			macaron.macaronage("siprem.db")
			if opcionBusquedaP == 2:

		except Exception, e:
			print e
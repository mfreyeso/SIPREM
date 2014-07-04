import models
import macaron

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
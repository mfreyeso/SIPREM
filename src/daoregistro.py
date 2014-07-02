import models
import macaron

class RegistroDao(object):
	"""docstring for RegistroDao"""
	def __init__(self):
		super(RegistroDao, self).__init__()

	def almacenarRegistros(self, kernelRegistrosP, estacionId):
		macaron.macaronage("siprem.db")
		estacionDao = models.Estacion.get(estacionId)
		for registro in kernelRegistrosP:
			if registro.entregarPrecipitacion() != 0 and registro.entregarPrecipitacion() != "-":
				self.insertarRegistro(registro, estacionDao)

	def insertarRegistro(self, registroP, estacionDaoP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP.estacionreg.append(
				fecha = registroP.entregarFecha(),
				hora = registroP.entregarHora(),
				vprec = registro.entregarPrecipitacion()
			)
			macaron.bake()
			return True
		except Exception, e:
			print e
			return False
		


		
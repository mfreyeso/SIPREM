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

		
import macaron
import models
import sqlite3 as lite
import cPickle as pickle

class EventoDao(object):
	"""docstring for EventoDao"""
	def __init__(self):
		super(EventoDao, self).__init__()

	def almacenarEventos(self, coleccionP, estacionId):
		macaron.macaronage("siprem.db")
		estacionDao = models.Estacion.get(estacionId)
		for evento in coleccionP:
			self.insertarEvento(evento, estacionDao)

	def insertarEvento(self, eventoP, estacionDaoP):
		try:
			macaron.macaronage("siprem.db")
			vectorMagnitudes = eventoP.entregarVectorMagnitudes()
			vectorSerializado = self.serializarObjeto(vectorMagnitudes)
			vectorBinario = self.conversorBinario(vectorSerializado)

			estacionDaoP.eventos.append(
				fecha= str(eventoP.entregarFecha()),
				horainicio= str(eventoP.entregarHoraInicio()),
				horafin= str(eventoP.entregarHoraFin()),
				magnitud= eventoP.entregarMagnitud(),
				duracion= eventoP.entregarDuracion(),
				intmedia= eventoP.entregarIntensidadMedia(),
				intmaxima= eventoP.entregarIntensidadMaxima(),
				tipoprec= eventoP.entregarTipoLluvia(),
				observ= eventoP.entregarObservaciones(),
				jorprec= eventoP.entregarJornadaEvento(),
				vmagn= vectorBinario
			)
			macaron.bake()
			return
		except Exception, e:
			print e
			return

	def serializarObjeto(self, objetoP):
		objetoSerializado = pickle.dumps(objetoP, 2)
		return objetoSerializado

	def conversorBinario(self, objetoSerializadoP):
		nuevoBinario = lite.Binary(objetoSerializadoP)
		return nuevoBinario

	def deserializarObjeto(self, objetoResultado):
		cadenaObjeto = str(objetoResultado)
		objetoDeserializado = pickle.loads(cadenaObjeto)
		return objetoDeserializado
		


		
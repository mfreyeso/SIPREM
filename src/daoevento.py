import macaron
import models
import evento as evm
import sqlite3 as lite
import cPickle as pickle

class EventoDao(object):
	"""docstring for EventoDao"""
	def __init__(self):
		super(EventoDao, self).__init__()

	def almacenarEventos(self, coleccionP, estacionId):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionId)
			for eventoP in coleccionP:
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
		except Exception, e:
			print e

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
		
	def buscarEventos(self, fechaInicialP, fechaFinalP, estacionIdP):
		try:
			macaron.macaronage("siprem.db")
			estacionDao = models.Estacion.get(estacionIdP)
			eventosDao = estacionDao.eventos.select("fecha between ? and ?", [fechaInicialP, fechaFinalP])
			eventos = self.transformarEventosModelo(eventosDao)
			return eventos	
		except Exception, e:
			print e

	def buscarEventosAvanzado(self, fechaInicialP, fechaFinalP, estacionIdP, categoriaP, jornadaP):
		try:
			macaron.macaronage("siprem.db")
			estacionDao = models.Estacion.get(estacionIdP)
			eventosDao = estacionDao.eventos.select("fecha between ? and ? and tipoprec = ? and jorprec = ?", [fechaInicialP, fechaFinalP, categoriaP, jornadaP])
			eventos = self.transformarEventosModelo(eventosDao)
			return eventos	
		except Exception, e:
			print e


	def transformarEventosModelo(self, coleccionEventosDaoP):
		eventosTransformados = []
		for eventoD in coleccionEventosDaoP:
			vmagn = self.deserializarObjeto(eventoD.vmagn)
			objEvento = evm.evento(
				eventoD.fecha,
				eventoD.horainicio,
				eventoD.horafin,
				eventoD.magnitud,
				eventoD.duracion,
				eventoD.intmedia,
				eventoD.intmaxima,
				eventoD.tipoprec,
				eventoD.jorprec,
				eventoD.observ,
				vmagn
				)
			eventosTransformados.append(objEvento)

		return eventosTransformados
import datetime
import sqlite3 as lite
import cPickle as pickle
import macaron
import models

class PrsEvento(object):
	"""docstring for PrsEvento"""
	def __init__(self):
		super(PrsEvento, self).__init__()
		
	def persistenciaColeccionEventos(self, coleccionP, idEstacionP):
		response = False
		coleccion = coleccionP
		fechaInicial = coleccion[0].entregarFecha()
		fechaFinal = coleccion[len(coleccion)-1].entregarFecha()
		objetoASerializar = models.AlmacenSerializado(coleccion)
		objetoSerializado = self.serializarObjeto(objetoASerializar)
		serializadoBinario = self.conversorBinario(objetoSerializado)
		macaron.macaronage("siprem.db")
		try:
			estacionRelacionada= models.Cevento.create(
				idestacion=idEstacionP,
				fechainicio=fechaInicial,
				fechafin=fechaFinal,
				binario=serializadoBinario
				)
			response=True
			return response			
		except Exception, e:
			print e
			return response

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

	def pruebaDeserializacion(self):
		try:
			fechaInicio = datetime.date(2007, 8, 20)
			fechaFin =  datetime.date(2007, 10, 20)
			macaron.macaronage('siprem.db')
			result = models.Cevento.select("fechainicio < ? and fechafin > ?", [fechaInicio, fechaFin])
			encapsulado = result[0].binario
			deserializado = self.deserializarObjeto(encapsulado)
			eventos = deserializado.coleccionEventos
			print len(eventos)
			for evento in eventos:
				print evento.entregarHoraInicio()
		except Exception, e:
			print e		

	def buscarEventos(self, opcionBusquedaP, diaP, mesP, anoP):
		fechaFin = datetime.date(anoP, 12, 31)
		if opcionBusquedaP == 1:
			fechaBusqueda = datetime.date(anoP, mesP, diaP)
		elif opcionBusquedaP == 2:
			fechaBusqueda = datetime.date(anoP, mesP, 1)
		else:
			fechaBusqueda = datetime.date(anoP, 1, 1)
		macaron.macaronage('siprem.db')
		print fechaBusqueda, fechaFin
		result = models.Cevento.select("fechainicio between ? and ?", [fechaBusqueda, fechaFin])
		coleccionEventos = []
		if result.count() > 0:
			for idx, o in enumerate(result):
				coleccionEventos.append(o)

	def filtroBusqueda(self, fechaBusquedaP, coleccionEventosP, opcionBusquedaP):
		objetoDeserializado = self.deserializarObjeto(coleccionEventosP)
		eventosEncontrados = []
		if opcionBusquedaP == 1:
			for evento in eventos:
				fechaEvento = evento.entregarFecha()
				if fechaEvento == fechaBusqueda:
					eventosEncontrados.append(evento)
		elif opcionBusquedaP == 2:
			for evento in eventos:
				fechaEvento = evento.entregarFecha()
				fechaInicial = datetime.date(fechaBusqueda.year, fechaBusqueda.month, 1)
				fechaFinal = datetime.date(fechaBusqueda.year, fechaBusqueda.month, 31)
				if (fechaEvento >= fechaInicial) and (fechaEvento <= fechaFinal):
					eventosEncontrados.append(evento)

		else:
			for evento in eventos:
				fechaEvento = evento.entregarFecha()
				fechaInicial = datetime.date(fechaBusqueda.year, 1, 1)
				fechaFinal = datetime.date(fechaBusqueda.year, 12, 31)
				if (fechaEvento >= fechaInicial) and (fechaEvento <= fechaFinal):
					eventosEncontrados.append(evento)
		return eventosEncontrados
				
			









		
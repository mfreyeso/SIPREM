import macaron
import models
import evento as evm
import sqlite3 as lite
import cPickle as pickle
import datetime

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
			objEvento.calcularTiempoNeto()
			eventosTransformados.append(objEvento)

		return eventosTransformados

	def busquedaParametrizada(self, opcionBusquedaP, parametrosP, estacionIdP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionIdP)
			if opcionBusquedaP == 1:
				eventosDao = estacionDaoP.eventos.select("fecha = ?", [parametrosP])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos
			elif opcionBusquedaP == 2:
				eventosDao = estacionDaoP.eventos.select("strftime('%Y-%m', fecha) = ?", [parametrosP])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos
			elif opcionBusquedaP == 3:
				eventosDao = estacionDaoP.eventos.select("strftime('%Y', fecha) = ?", [parametrosP])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos
			elif opcionBusquedaP == 4:
				if parametrosP[0] == 1:
					fechaInicial = datetime.date(parametrosP[1], 1, 1)
					fechaFinal = datetime.date(parametrosP[1], 6, 30)
				else:
					fechaInicial = datetime.date(parametrosP[1], 7, 1)
					fechaFinal = datetime.date(parametrosP[1], 12, 31)
				eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos
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
				eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos
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
				eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos
			else:
				eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [parametrosP[0], parametrosP[1]])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos		
		except Exception, e:
			print e

	def febreroBisiesto(self, anoP):
		if( anoP % 4 == 0 and anoP % 100 != 0 or anoP % 400 == 0):
			#Ano Bisiesto
			return 29
		else:
			return 28

	def validarEventos(self, eventosP, estacionId):
		eventosValidos = []
		try:
			macaron.macaronage("siprem.db")
			estacion = models.Estacion.get(estacionId)
			for evento in eventosP:
				fecha = evento.entregarFecha() 
				horaInicio = evento.entregarHoraInicio()
				horaFin = evento.entregarHoraFin()
				eventoQ = estacion.eventos.select("fecha = ? and horainicio = ? and horafin = ?", [str(fecha), str(horaInicio), str(horaFin)])
				if eventoQ.count() == 0:
					eventosValidos.append(evento)
			return eventosValidos
		except Exception, e:
			print e
			return None

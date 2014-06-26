import random


class evento(object):
	
	def __init__(self, fechaP, horaInicioP, horaFinP,
	magnitudP, duracionP, intensidadMediaP, intensidadMaximaP, tipoLluviaP, 
	jornadaEventoP, observacionesP, vectorMagnitudesP):
		super(evento, self).__init__()
		self.fecha = fechaP
		self.horaInicio = horaInicioP
		self.horaFin = horaFinP
		self.magnitud = magnitudP
		self.duracion = duracionP
		self.intensidadMedia = intensidadMediaP
		self.intensidadMaxima = intensidadMaximaP
		self.tipoLluvia = tipoLluviaP
		self.jornadaEvento = jornadaEventoP
		self.observaciones = observacionesP
		self.vectorMagnitudes = vectorMagnitudesP

	"""Metodos Acceso a Atributos......................................"""

	def __str__(self):
		return self.horaInicio

	def entregarFecha(self):
		return self.fecha

	def entregarHoraInicio(self):
		return self.horaInicio

	def entregarHoraFin(self):
		return self.horaFin

	def entregarMagnitud(self):
		return self.magnitud

	def entregarDuracion(self):
		return self.duracion

	def entregarIntensidadMedia(self):
		return self.intensidadMedia

	def entregarIntensidadMaxima(self):
		return self.intensidadMaxima

	def entregarTipoLluvia(self):
		return self.tipoLluvia

	def entregarJornadaEvento(self):
		return self.jornadaEvento

	def entregarObservaciones(self):
		return self.observaciones

	def entregarDuracionNeta(self):
		return self.duracionNeta

	def entregarVectorMagnitudes(self):
		return self.vectorMagnitudes

	"""Metodos Modificadores......................................"""

	def modificarFecha(self, fechaP):
		self.fecha = fechaP

	def modificarHoraInicio(self, horaInicioP):
		self.horaInicio = horaInicioP

	def modificarHoraFin(self, horaFinP):
		self.horaFin = horaFinP

	def modificarMagnitud(self, magnitudP):
		self.magnitud = magnitudP

	def modificarIntensidadMedia(self, intensidadMediaP):
		self.intensidadMedia = intensidadMediaP

	def modificarIntensidadMaxima(self, intensidadMaximaP):
		self.intensidadMaxima = intensidadMaximaP

	def modificarTipoLluvia(self, tipoLluviaP):
		self.tipoLluvia = tipoLluviaP

	def modificarJornadaEvento(self, jornadaEventoP):
		self.jornadaEvento = jornadaEventoP

	def modificarObservaciones(self, observacionesP):
		self.observaciones = observacionesP

	def modificarDuracionNeta(self, duracionNetaP):
		self.duracionNeta = duracionNetaP

	def modificarVectorMagnitudes(self, vectorMagnitudesP):
		self.vectorMagnitudes = vectorMagnitudesP

	def modificarIdentificador(self, codigoHash):
		self.identificador = codigoHash

	"""Calcula el tiempo neto de la precipitacion"""

	def calcularTiempoNeto(self):
		tiempoNulo = 0
		for iMagnitud in self.vectorMagnitudes:
			if iMagnitud == 0:
				tiempoNulo = tiempoNulo + 1
		duracionNetaCalculada = self.entregarDuracion() - (tiempoNulo * 5)
		self.modificarDuracionNeta(duracionNetaCalculada)



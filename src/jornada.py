class jornada(object):
	def __init__(self, etiquetaJornadaP, horaInicioP, horaFinP, identificacionP):
		super (jornada, self).__init__()
		self.etiquetaJornada = etiquetaJornadaP
		self.horaInicio = horaInicioP
		self.horaFin = horaFinP
		self.identificacion = identificacionP

	def entregarEtiquetaJornada(self):
		return self.etiquetaJornada

	def entregarHoraInicio(self):
		return self.horaInicio

	def entregarHoraFin(self):
		return self.horaFin

	def entregarIdentificacion(self):
		return self.identificacion

	def modificarEtiquetaJornada(self, etiquetaJornadaP):
		self.etiquetaJornada = etiquetaJornadaP

	def modificarHoraInicio(self, horaInicioP):
		self.horaInicio = horaInicioP

	def modificarHoraFin(self, horaFinP):
		self.horaFin = horaFinP

	def __str__(self):
		print self.etiquetaJornada
class registro(object):
	"""Metodo constructor a futuro"""
	"""
	def __init__(self, fechaP, horaP, temperaturaAireP, velocidadVientoP, 
		direccionVientoP, presionBarometricaP, precipitacionP, humedadRelativaP):
		super(registro, self).__init__()
		self.fecha = fechaP
		self.hora = horaP
		self.temperaturaAire = temperaturaAireP
		self.velocidadViento = velocidadVientoP
		self.direccionViento = direccionVientoP
		self.presionBarometrica = presionBarometricaP
		self.precipitacion = precipitacionP
		self.humedadRelativa = humedadRelativaP
	"""

	"""Metodo constructor temporal"""
	def __init__(self, fechaP, horaP, precipitacionP):
		super(registro, self).__init__()
		self.fecha = fechaP
		self.hora = horaP
		self.precipitacion = precipitacionP
		
	def __str__(self):
		return self.hora

	def entregarFecha(self):
		return self.fecha

	def entregarHora(self):
		return self.hora

	def entregarTemperaturaAire(self):
		return self.temperaturaAire

	def entregarVelocidadViento(self):
		return self.velocidadViento

	def entregarDireccionViento(self):
		return self.direccionViento

	def entregarPresionBarometrica(self):
		return self.presionBarometrica

	def entregarPrecipitacion(self):
		return self.precipitacion

	def entregarHumedadRelativa(self):
		return self.humedadRelativa

	"""Metodos Modificadores de los Atributos de la clase Registro"""

	def modificarFecha(self, fechaP):
		self.fecha = fechaP

	def modificarHora(self, horaP):
		self.hora = horaP

	def modificarTemperaturaAire(self, temperaturaAireP):
		self.temperaturaAire = temperaturaAireP

	def modificarVelocidadViento(self, velocidadVientoP):
		self.velocidadViento = velocidadVientoP

	def modificarDireccionViento(self, direccionVientoP):
		self.direccionViento = direccionVientoP

	def modificarPresionBarometrica(self, presionBarometricaP):
		self.presionBarometrica = presionBarometricaP

	def modificarPrecipitacion(self, precipitacionP):
		self.precipitacion = precipitacionP

	def modificarHumedadRelativa(self, humedadRelativaP):
		self.humedadRelativa = humedadRelativaP

		
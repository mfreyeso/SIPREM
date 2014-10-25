class categoria(object):
	
	def __init__(self, etiquetaCategoriaP, medidaMagnitudP, identificacionP):
		super(categoria, self).__init__()
		self.etiquetaCategoria = etiquetaCategoriaP
		self.medidaMagnitud = medidaMagnitudP
		self.identificacion = identificacionP

	def entregarEtiqueta(self):
		return self.etiquetaCategoria

	def entregarMagnitud(self):
		return self.medidaMagnitud

	def entregarIdentificacion(self):
		return self.identificacion

	def modificarEtiqueta(self, etiquetaCategoriaP):
		self.etiquetaCategoria = etiquetaCategoriaP

	def modificarMagnitud(self, medidaMagnitudP):
		self.medidaMagnitud = medidaMagnitudP

	def __str__(self):
		print self.etiquetaCategoria
	
		
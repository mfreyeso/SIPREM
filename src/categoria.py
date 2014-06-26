class categoria(object):
	
	def __init__(self, etiquetaCategoriaP, medidaMagnitudP):
		super(categoria, self).__init__()
		self.etiquetaCategoria = etiquetaCategoriaP
		self.medidaMagnitud = medidaMagnitudP

	def entregarEtiqueta(self):
		return self.etiquetaCategoria

	def entregarMagnitud(self):
		return self.medidaMagnitud

	def modificarEtiqueta(self, etiquetaCategoriaP):
		self.etiquetaCategoria = etiquetaCategoriaP

	def modificarMagnitud(self, medidaMagnitudP):
		self.medidaMagnitud = medidaMagnitudP

	
		
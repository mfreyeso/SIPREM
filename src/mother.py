class Mother(object):
	
	def __init__(self):
		super(Mother, self).__init__()
	
	def modificarEstructuraMain(self, objEstMain):
		self.estructuraMain = objEstMain

	def entregarEstructuraMain(self):
		return self.estructuraMain

	def modificarResumen(self, objResumen):
		self.resumen= objResumen

	def entregarResumen(self):
		return self.resumen



	
		
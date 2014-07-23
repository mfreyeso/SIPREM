class acumulado(object):
	
	def __init__(self):
		super(acumulado, self).__init__()
		self.etiquetasTrimestresEstandar = ["Enero - Marzo", "Abril - Junio", "Julio - Septiembre", "Octubre - Diciembre"]
		self.etiquetasTrimestresBimodal = ["Diciembre - Febrero", "Marzo - Mayo", "Junio - Agosto", "Septiembre - Noviembre"]
		self.etiquetasSemestres = ["Enero - Junio", "Julio - Diciembre"]
		self.etiquetasMeses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


	def entregarEtiquetasTrimestresEstandar(self):
		return self.etiquetasTrimestresEstandar

	def entregarEtiquetasTrimestresBimodal(self):
		return self.etiquetasTrimestresBimodal
	
	def entregarEtiquetasSemestres(self):
		return self.etiquetasSemestres

	def entregarEtiquetasMeses(self):
		return self.etiquetasMeses

	def entregarSemestre(self, idSemestre):
		return self.entregarEtiquetasSemestres()[idSemestre -1]

	def entregarTrimestre(self, tipoP, idTrimestre):
		if tipoP == 1:
			return self.entregarEtiquetasTrimestresBimodal()[idTrimestre -1]
		else:
			return self.entregarEtiquetasTrimestresEstandar()[idTrimestre -1]

	def entregarMes(self, idMes):
		return self.entregarEtiquetasMeses()[idMes - 1]

	def calcularAcumuladoMagnitudRegistros(self, coleccionRegistrosP):
		acumulado = 0
		for registro in coleccionRegistrosP:
			acumulado += registro.entregarPrecipitacion()
		return acumulado

	def calcularAcumuladoMagnitudEventos(self, coleccionEventosP):
		acumulado = 0
		for evento in coleccionEventosP:
			acumulado += evento.entregarMagnitud()
		return acumulado

	def calcularAcumuladoIntensidadMediaEventos(self, coleccionEventosP):
		acumulado = 0
		for evento in coleccionEventosP:
			acumulado += evento.entregarIntensidadMedia()
		return acumulado

	def calcularAcumuladoIntensidadMaximaEventos(self, coleccionEventosP):
		acumulado = 0
		for evento in coleccionEventosP:
			acumulado += evento.entregarIntensidadMaxima()
		return acumulado

	def calcularAcumuladoDuracionEventos(self, coleccionEventosP):
		acumulado = 0
		for evento in coleccionEventosP:
			acumulado += evento.entregarDuracion()
		return acumulado

	def calcularAcumuladoDuracionMaxEventos(self, coleccionEventosP):
		maximo = 0
		for evento in coleccionEventosP:
			if evento.entregarDuracion() > maximo:
				maximo = evento.entregarDuracion()
		return maximo

	def calcularAcumuladoDuracionNetaEventos(self, coleccionEventosP):
		acumulado = 0
		for evento in coleccionEventosP:
			acumulado+=evento.entregarDuracionNeta()
		return acumulado

	def calculoGeneralAcumuladoEventos(self, coleccionEventosP):
		resultados = [self.calcularAcumuladoMagnitudEventos(coleccionEventosP),
		self.calcularAcumuladoIntensidadMediaEventos(coleccionEventosP),
		self.calcularAcumuladoIntensidadMaximaEventos(coleccionEventosP),
		self.calcularAcumuladoDuracionEventos(coleccionEventosP),
		self.calcularAcumuladoDuracionMaxEventos(coleccionEventosP),
		self.calcularAcumuladoDuracionNetaEventos(coleccionEventosP)]
		return resultados

	
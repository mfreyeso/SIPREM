class acumulado(object):
	
	def __init__(self):
		super(acumulado, self).__init__()
		self.etiquetasTrimestresEstandar = ["Enero - Marzo", "Abril - Junio", "Julio - Septiembre", "Octubre - Diciembre"]
		self.etiquetasTrimestresBimodal = ["Diciembre - Febrero", "Marzo - Mayo", "Junio - Agosto", "Septiembre - Noviembre"]
		self.etiquetasSemestres = ["Enero - Junio", "Julio - Diciembre"]
		self.etiquetasMeses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


	def entregarColeccionEventos(self):
		return self.coleccionEventos

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

	def acumuladoParametrizado(self, modoTrabajoP, diaAcumuladoP, mesP, anoP, semestreP, trimestreP):
		resultado = None
		if modoTrabajoP == 1:
			resultado = self.acumuladoDiario(diaAcumuladoP, mesP)
		elif modoTrabajoP == 2:
			resultado = self.acumuladoMensual(mesP)
		elif modoTrabajoP == 3:
			resultado = self.acumuladoAnual(anoP)
		elif modoTrabajoP == 4:
			resultado = self.acumuladoSemestral(semestreP)
		else:
			resultado = self.acumuladoTrimestral(trimestreP)
		return resultado

	def acumuladoDiario(self, diaAcumuladoP, mesP):
		magnitudDia = 0
		intensidadMediaDiariaMax = 0
		intensidadMaximaDiariaMax = 0
		duracion = 0
		duracionMax = 0
		duracionNeta = 0

		coleccionEventos = self.entregarColeccionEventos()
		c=1
		for evento in coleccionEventos:
			fechaEvento = evento.entregarFecha()
			diaEvento = fechaEvento.day
			mesEvento = fechaEvento.month
			if mesEvento == mesP and diaEvento == diaAcumuladoP:
				print "Evento..." + str(c)
				c+=1
				print evento.entregarDuracion()

				magnitudDia+=evento.entregarMagnitud()
				duracion+=evento.entregarDuracion()
				print duracion
				duracionNeta+=evento.entregarDuracionNeta()

				if evento.entregarIntensidadMedia() > intensidadMediaDiariaMax:
					intensidadMediaDiariaMax = evento.entregarIntensidadMedia()

				if evento.entregarIntensidadMaxima() > intensidadMaximaDiariaMax:
					intensidadMaximaDiariaMax = evento.entregarIntensidadMaxima()

				if evento.entregarDuracion() > duracionMax:
					duracionMax = evento.entregarDuracion()
			else:
				if diaEvento == (diaAcumuladoP + 1) and mesEvento == mesP:
					break

		resultados = [magnitudDia, intensidadMediaDiariaMax, intensidadMaximaDiariaMax, duracion, duracionMax, duracionNeta]
		return resultados

	def acumuladoMensual(self, mesP):
		magnitudMensual = 0
		intensidadMediaMensualMax = 0
		intensidadMaximaMensualMax = 0
		duracionMensual = 0
		duracionMaximaMensual = 0
		duracionNetaMensual = 0

		coleccionEventos = self.entregarColeccionEventos()
		for evento in coleccionEventos:
			fechaEvento = evento.entregarFecha()
			mesEvento = fechaEvento.month

			if mesEvento == mesP:
				magnitudMensual+=evento.entregarMagnitud()
				duracionMensual+=evento.entregarDuracion()
				duracionNetaMensual+=evento.entregarDuracionNeta()

				if evento.entregarIntensidadMedia() > intensidadMediaMensualMax:
					intensidadMediaMensualMax = evento.entregarIntensidadMedia()

				if evento.entregarIntensidadMaxima() > intensidadMaximaMensualMax:
					intensidadMaximaMensualMax = evento.entregarIntensidadMaxima()

				if evento.entregarDuracion() > duracionMaximaMensual:
					duracionMaximaMensual = evento.entregarDuracion()
			elif mesEvento > mesP:
				break

		resultados = [magnitudMensual, intensidadMediaMensualMax, intensidadMaximaMensualMax, duracionMensual, duracionMaximaMensual, duracionNetaMensual]
		return resultados


	def acumuladoAnual(self, anoP):
		magnitudAnual = 0
		intensidadMediaAnualMax = 0
		intensidadMaximaAnualMax = 0
		duracionAnual = 0
		duracionAnualMax = 0
		duracionNetaAnual = 0

		coleccionEventos = self.entregarColeccionEventos()
		for evento in coleccionEventos:

			fechaEvento = evento.entregarFecha()
			anoEvento = fechaEvento.year

			if anoEvento == anoP:
				magnitudAnual+=evento.entregarMagnitud()
				duracionAnual+= evento.entregarDuracion()
				duracionNetaAnual+= evento.entregarDuracionNeta()

				if evento.entregarIntensidadMedia() > intensidadMediaAnualMax:
					intensidadMediaAnualMax = evento.entregarIntensidadMedia()

				if evento.entregarIntensidadMaxima() > intensidadMaximaAnualMax:
					intensidadMaximaAnualMax = evento.entregarIntensidadMaxima()

				if evento.entregarDuracion() > duracionAnualMax:
					duracionAnualMax = evento.entregarDuracion()

			elif anoEvento > anoP:
				break

		resultados = [magnitudAnual, intensidadMediaAnualMax, intensidadMaximaAnualMax, duracionAnual, duracionAnualMax, duracionNetaAnual]
		return resultados

	def acumuladoSemestral(self, semestreP):
		magnitudSemestral = 0
		intensidadMediaSemestralMax = 0
		intensidadMaximaSemestralMax = 0
		duracionSemestral = 0
		duracionMaximaSemestral = 0
		duracionNetaSemestral = 0

		coleccionEventos = self.entregarColeccionEventos()

		if semestreP == 1:
			for evento in coleccionEventos:
				fechaEvento = evento.entregarFecha()
				mesEvento = fechaEvento.month

				if mesEvento <= 6:
					magnitudSemestral+= evento.entregarMagnitud()
					duracionSemestral+= evento.entregarDuracion()
					duracionNetaSemestral+= evento.entregarDuracionNeta()

					if evento.entregarIntensidadMedia() > intensidadMediaSemestralMax:
						intensidadMediaSemestralMax = evento.entregarIntensidadMedia()

					if evento.entregarIntensidadMaxima() > intensidadMaximaSemestralMax:
						intensidadMaximaSemestralMax = evento.entregarIntensidadMaxima()

					if evento.entregarDuracion() > duracionMaximaSemestral:
						duracionMaximaSemestral = evento.entregarDuracion()
		else:
			for evento in coleccionEventos:
				fechaEvento = evento.entregarFecha()
				mesEvento = fechaEvento.month

				if mesEvento > 6:
					magnitudSemestral+= evento.entregarMagnitud()
					duracionSemestral+= evento.entregarDuracion()
					duracionNetaSemestral+= evento.entregarDuracionNeta()

					if evento.entregarIntensidadMedia() > intensidadMediaSemestralMax:
						intensidadMediaSemestralMax = evento.entregarIntensidadMedia()

					if evento.entregarIntensidadMaxima() > intensidadMaximaSemestralMax:
						intensidadMaximaSemestralMax = evento.entregarIntensidadMaxima()

					if evento.entregarDuracion() > duracionMaximaSemestral:
						duracionMaximaSemestral = evento.entregarDuracion()

		resultados = [magnitudSemestral, intensidadMediaSemestralMax, intensidadMaximaSemestralMax, duracionSemestral, duracionMaximaSemestral, duracionNetaSemestral]
		return resultados



	def acumuladoTrimestral(self, trimestreP):
		magnitudTrimestral = 0
		intensidadMediaTrimestralMax = 0
		intensidadMaximaTrimestralMaxima = 0
		duracionTrimestral = 0
		duracionMaximaTrimestral = 0
		duracionNetaTrimestral = 0

		coleccionEventos = self.entregarColeccionEventos()
		if trimestreP == 1:
			for evento in coleccionEventos:
				fechaEvento = evento.entregarFecha()
				mesEvento = fechaEvento.month

				if mesEvento == 12 or mesEvento <= 2:
					magnitudTrimestral+=evento.entregarMagnitud()
					duracionTrimestral+=evento.entregarDuracion()
					duracionNetaTrimestral+=evento.entregarDuracionNeta()

					if evento.entregarIntensidadMedia() > intensidadMediaTrimestralMax:
						intensidadMediaTrimestralMax = evento.entregarIntensidadMedia()

					if evento.entregarIntensidadMaxima() > intensidadMaximaTrimestralMaxima:
						intensidadMaximaTrimestralMaxima = evento.entregarIntensidadMaxima()

					if evento.entregarDuracion() > duracionMaximaTrimestral:
						duracionMaximaTrimestral = evento.entregarDuracion()

		elif trimestreP == 2:
			for evento in coleccionEventos:
				fechaEvento = evento.entregarFecha()
				mesEvento = fechaEvento.month

				if mesEvento >= 3 and mesEvento < 6:
					magnitudTrimestral+=evento.entregarMagnitud()
					duracionTrimestral+=evento.entregarDuracion()
					duracionNetaTrimestral+=evento.entregarDuracionNeta()

					if evento.entregarIntensidadMedia() > intensidadMediaTrimestralMax:
						intensidadMediaTrimestralMax = evento.entregarIntensidadMedia()

					if evento.entregarIntensidadMaxima() > intensidadMaximaTrimestralMaxima:
						intensidadMaximaTrimestralMaxima = evento.entregarIntensidadMaxima()

					if evento.entregarDuracion() > duracionMaximaTrimestral:
						duracionMaximaTrimestral = evento.entregarDuracion()

		elif trimestreP == 3:
			for evento in coleccionEventos:
				fechaEvento = evento.entregarFecha()
				mesEvento = fechaEvento.month

				if mesEvento >= 6 and mesEvento < 9:
					magnitudTrimestral+=evento.entregarMagnitud()
					duracionTrimestral+=evento.entregarDuracion()
					duracionNetaTrimestral+=evento.entregarDuracionNeta()

					if evento.entregarIntensidadMedia() > intensidadMediaTrimestralMax:
						intensidadMediaTrimestralMax = evento.entregarIntensidadMedia()

					if evento.entregarIntensidadMaxima() > intensidadMaximaTrimestralMaxima:
						intensidadMaximaTrimestralMaxima = evento.entregarIntensidadMaxima()

					if evento.entregarDuracion() > duracionMaximaTrimestral:
						duracionMaximaTrimestral = evento.entregarDuracion()

		else:
			for evento in coleccionEventos:
				fechaEvento = evento.entregarFecha()
				mesEvento = fechaEvento.month

				if mesEvento >= 9 and mesEvento < 12:
					magnitudTrimestral+=evento.entregarMagnitud()
					duracionTrimestral+=evento.entregarDuracion()
					duracionNetaTrimestral+=evento.entregarDuracionNeta()

					if evento.entregarIntensidadMedia() > intensidadMediaTrimestralMax:
						intensidadMediaTrimestralMax = evento.entregarIntensidadMedia()

					if evento.entregarIntensidadMaxima() > intensidadMaximaTrimestralMaxima:
						intensidadMaximaTrimestralMaxima = evento.entregarIntensidadMaxima()

					if evento.entregarDuracion() > duracionMaximaTrimestral:
						duracionMaximaTrimestral = evento.entregarDuracion()

		resultados = [magnitudTrimestral, intensidadMediaTrimestralMax, intensidadMaximaTrimestralMaxima, duracionTrimestral, duracionMaximaTrimestral, duracionNetaTrimestral]
		return resultados


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

	
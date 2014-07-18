class resumen(object):
	
	def __init__(self):
		super(resumen, self).__init__()
		

	def entregarColeccionEventos(self):
		return self.coleccionEventos

	def entregarVocCategoria(self):
		return self.vectorOcurCategoria

	def entregarVocJornada(self):
		return self.vectorOcurJornada

	def entregarListaCategorias(self):
		return self.listaCategorias

	def entregarListaJornadas(self):
		return self.listaJornadas

	def entregarNumeroRegistros(self):
		return len(self.entregarColeccionEventos())

	"""Entrega la precipitacion de mayor duracion"""
	def entregarMaximaDuracion(self, casoUso, parametroP):
		coleccionEventos = self.entregarColeccionEventos()
		maximaDuracion = None
		#"""Caso General"""
		if casoUso == 0:
			duracion = 0
			for evento in coleccionEventos:
				if evento.entregarDuracion() > duracion:
					maximaDuracion = evento
					duracion = maximaDuracion.entregarDuracion()

		elif casoUso == 1:
			duracion = 0
			mesParametro = parametroP
			for evento in coleccionEventos:
				mesEvento = evento.entregarFecha().month
				if (evento.entregarDuracion() > duracion) and (mesEvento == mesParametro):
					maximaDuracion = evento
					duracion = maximaDuracion.entregarDuracion()

				elif mesEvento > mesParametro:
					break

		#"""Caso Semestral"""			
		elif casoUso == 2:
			duracion = 0
			#"""Semestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarDuracion() > duracion) and (mesEvento>=1 and mesEvento<=6):
						maximaDuracion = evento
						duracion = maximaDuracion.entregarDuracion()
					elif mesEvento > 6:
						break
			#"""Semestre 2"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarDuracion() > duracion) and (mesEvento>=7 and mesEvento<=12):
						maximaDuracion = evento
						duracion = maximaDuracion.entregarDuracion()
					
		#"""Caso Trimestral"""
		elif casoUso == 3:
			duracion = 0
			#"""Trimestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarDuracion() > duracion) and (mesEvento==12 or mesEvento<=2):
						maximaDuracion = evento
						duracion = maximaDuracion.entregarDuracion()
					elif mesEvento > 2:
						break

			#"""Trimestre 2"""
			elif parametroP == 2:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarDuracion() > duracion) and (mesEvento>=3 and mesEvento<6):
						maximaDuracion = evento
						duracion = maximaDuracion.entregarDuracion()
					elif mesEvento > 5:
						break

			#"""Trimestre 3"""			
			elif parametroP == 3:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarDuracion() > duracion) and (mesEvento>=6 and mesEvento<9):
						maximaDuracion = evento
						duracion = maximaDuracion.entregarDuracion()
					elif mesEvento > 8:
						break

			#"""Trimestre 4"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarDuracion() > duracion) and (mesEvento>=9 and mesEvento<12):
						maximaDuracion = evento
						duracion = maximaDuracion.entregarDuracion()
					elif mesEvento > 11:
						break
		
		return maximaDuracion


	"""Entrega la precipitacion de mayor Magnitud"""
	def entregarMaximaMagnitud(self, casoUso, parametroP):
		coleccionEventos = self.entregarColeccionEventos()
		maximaMagnitud =None		
		#"""Caso General"""
		if casoUso == 0:
			duracion = 0
			for evento in coleccionEventos:
				if evento.entregarMagnitud() > duracion:
					maximaMagnitud = evento
					duracion = maximaMagnitud.entregarMagnitud()
		#"""Caso Mensual"""
		elif casoUso == 1:
			duracion = 0
			mesParametro = parametroP
			for evento in coleccionEventos:
				mesEvento = evento.entregarFecha().month
				if (evento.entregarMagnitud() > duracion) and mesEvento == mesParametro:
					maximaMagnitud = evento
					duracion = maximaMagnitud.entregarMagnitud()
				elif mesEvento > mesParametro:
					break
		#"""Caso Semestral"""			
		elif casoUso == 2:
			duracion = 0
			"""Semestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarMagnitud() > duracion) and (mesEvento>=1 and mesEvento<=6):
						maximaMagnitud = evento
						duracion = maximaMagnitud.entregarMagnitud()
					elif mesEvento > 6:
						break
			#"""Semestre 2"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarMagnitud() > duracion) and (mesEvento>=7 and mesEvento<=12):
						maximaMagnitud = evento
						duracion = maximaMagnitud.entregarMagnitud()
		#"""Caso Trimestral"""
		else:
			duracion = 0
			#"""Trimestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarMagnitud() > duracion) and (mesEvento==12 or mesEvento<=2):
						maximaMagnitud = evento
						duracion = maximaMagnitud.entregarMagnitud()
					elif mesEvento > 2:
						break

			#"""Trimestre 2"""
			elif parametroP == 2:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarMagnitud() > duracion) and (mesEvento>=3 and mesEvento<6):
						maximaMagnitud = evento
						duracion = maximaMagnitud.entregarMagnitud()
					elif mesEvento > 5:
						break

			#"""Trimestre 3"""			
			elif parametroP == 3:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarMagnitud() > duracion) and (mesEvento>=6 and mesEvento<9):
						maximaMagnitud = evento
						duracion = maximaMagnitud.entregarMagnitud()
					elif mesEvento > 8:
						break
			#"""Trimestre 4"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarMagnitud() > duracion) and (mesEvento>=9 and mesEvento<12):
						maximaMagnitud = evento
						duracion = maximaMagnitud.entregarMagnitud()
					elif mesEvento > 11:
						break
		return maximaMagnitud


	"""Entrega la precipitacion de mayor Intensidad Media"""
	def entregarMaximaIntensidadMedia(self, casoUso, parametroP):
		coleccionEventos = self.entregarColeccionEventos()
		maximaIntensidadMedia = None
		#"""Caso General"""
		if casoUso == 0:
			duracion = 0
			for evento in coleccionEventos:
				if evento.entregarIntensidadMedia() > duracion:
					maximaIntensidadMedia = evento
					duracion = maximaIntensidadMedia.entregarIntensidadMedia()
		#"""Caso Mensual"""
		elif casoUso == 1:
			duracion = 0
			mesParametro = parametroP
			for evento in coleccionEventos:
				mesEvento = evento.entregarFecha().month
				if (evento.entregarIntensidadMedia() > duracion) and (mesEvento == mesParametro):
					maximaIntensidadMedia = evento
					duracion = maximaIntensidadMedia.entregarIntensidadMedia()
				elif mesEvento > mesParametro:
					break			
		#"""Caso Semestral"""			
		elif casoUso == 2:
			duracion = 0
			"""Semestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMedia() > duracion) and (mesEvento>=1 and mesEvento<=6):
						maximaIntensidadMedia = evento
						duracion = maximaIntensidadMedia.entregarIntensidadMedia()
					elif mesEvento > 6:
						break
			#"""Semestre 2"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMedia() > duracion) and (mesEvento>=7 and mesEvento<=12):
						maximaIntensidadMedia = evento
						duracion = maximaIntensidadMedia.entregarIntensidadMedia()
		#"""Caso Trimestral"""
		else:
			duracion = 0
			#"""Trimestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMedia() > duracion) and (mesEvento==12 or mesEvento<=2):
						maximaIntensidadMedia = evento
						duracion = maximaIntensidadMedia.entregarIntensidadMedia()
					elif mesEvento > 2:
						break
			#"""Trimestre 2"""
			elif parametroP == 2:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMedia() > duracion) and (mesEvento>=3 and mesEvento<6):
						maximaIntensidadMedia = evento
						duracion = maximaIntensidadMedia.entregarIntensidadMedia()
					elif mesEvento > 5:
						break
			#"""Trimestre 3"""			
			elif parametroP == 3:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMedia() > duracion) and (mesEvento>=6 and mesEvento<9):
						maximaIntensidadMedia = evento
						duracion = maximaIntensidadMedia.entregarIntensidadMedia()
					elif mesEvento > 8:
						break
			#"""Trimestre 4"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMedia() > duracion) and (mesEvento>=9 and mesEvento<12):
						maximaIntensidadMedia = evento
						duracion = maximaIntensidadMedia.entregarIntensidadMedia()
					elif mesEvento > 11:
						break

		return maximaIntensidadMedia


	"""Entrega la precipitacion de mayor Intensidad Maxima"""
	def entregarMaximaIntensidadMaxima(self, casoUso, parametroP):
		coleccionEventos = self.entregarColeccionEventos()
		maximaIntensidadMaxima = None
		
		"""Caso General"""
		if casoUso == 0:
			duracion = 0
			for evento in coleccionEventos:
				if evento.entregarIntensidadMaxima() > duracion:
					maximaIntensidadMaxima = evento
					duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
		#"""Caso Mensual"""
		elif casoUso == 1:
			duracion = 0
			mesParametro = parametroP
			for evento in coleccionEventos:
				mesEvento = evento.entregarFecha().month
				if (evento.entregarIntensidadMaxima() > duracion) and mesEvento == mesParametro:
					maximaIntensidadMaxima = evento
					duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
				elif mesEvento > mesParametro:
					break
		#"""Caso Semestral"""			
		elif casoUso == 2:
			duracion = 0
			#"""Semestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMaxima() > duracion) and (mesEvento>=1 and mesEvento<=6):
						maximaIntensidadMaxima = evento
						duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
					elif mesEvento > 6:
						break
			#"""Semestre 2"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMaxima() > duracion) and (mesEvento>=7 and mesEvento<=12):
						maximaIntensidadMaxima = evento
						duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
		#"""Caso Trimestral"""
		else:
			duracion = 0
			#"""Trimestre 1"""
			if parametroP == 1:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMaxima() > duracion) and (mesEvento==12 or mesEvento<=2):
						maximaIntensidadMaxima = evento
						duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
					elif mesEvento > 2:
						break
			#"""Trimestre 2"""
			elif parametroP == 2:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMaxima() > duracion) and (mesEvento>=3 and mesEvento<6):
						maximaIntensidadMaxima = evento
						duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
					elif mesEvento > 5:
						break
			#"""Trimestre 3"""			
			elif parametroP == 3:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMaxima() > duracion) and (mesEvento>=6 and mesEvento<9):
						maximaIntensidadMaxima = evento
						duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
					elif mesEvento > 8:
						break
			#"""Trimestre 4"""
			else:
				for evento in coleccionEventos:
					mesEvento = evento.entregarFecha().month
					if (evento.entregarIntensidadMaxima() > duracion) and (mesEvento>=9 and mesEvento<12):
						maximaIntensidadMaxima = evento
						duracion = maximaIntensidadMaxima.entregarIntensidadMaxima()
					elif mesEvento > 11:
						break

		return maximaIntensidadMaxima


	def periodoEventos(self):
		periodo = None
		primerEvento = self.entregarColeccionEventos()[0]
		ultimoEvento = self.entregarColeccionEventos()[len(self.entregarColeccionEventos()) - 1]
		
		periodo = str(primerEvento.entregarFecha()) + " - " + str(ultimoEvento.entregarFecha())
		return periodo

	def entregarMaximos(self, casoUsoP, parametroP):
		maximos = []
		maximos.append(self.entregarMaximaDuracion(casoUsoP, parametroP).entregarDuracion())
		maximos.append(self.entregarMaximaMagnitud(casoUsoP, parametroP).entregarMagnitud())
		maximos.append(self.entregarMaximaIntensidadMedia(casoUsoP, parametroP).entregarIntensidadMedia())
		maximos.append(self.entregarMaximaIntensidadMaxima(casoUsoP, parametroP).entregarIntensidadMaxima())

		return maximos

	def validarCompletitudResumen(self):	
		coleccionEventos = self.entregarColeccionEventos()
		for i in range(1, 13):
			response = False
			for evento in coleccionEventos:
				mesEvento = evento.entregarFecha().month
				if mesEvento == i:
					response = True
					break
			if response == False:
				return response
		return response


	def resumenMensualAnual(self):
		eventos = self.entregarColeccionEventos()
		matrizJornadas=[]
		matrizCategorias=[]
		listaMaximos=[]
		jornadasE = self.entregarListaJornadas()
		categoriasE = self.entregarListaCategorias()

		for i in range(0, len(jornadasE)):
			jornada = jornadasE[i].entregarEtiquetaJornada()
			horaInicio = jornadasE[i].entregarHoraInicio()
			horaFin = jornadasE[i].entregarHoraFin()
			listaOcurrenciaMensual = [0]
			for i in range(1, 13):
				ocurrenciaMes = 0
				for evento in eventos:
					mesEvento = evento.entregarFecha().month
					horaInicioE = evento.entregarHoraInicio().hour
					horaFinE = evento.entregarHoraFin().hour
					if mesEvento <= i:
						if mesEvento == i:
							if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
								ocurrenciaMes+=1
					else:
						break
				listaOcurrenciaMensual.append(ocurrenciaMes)			
			dicJornada=[jornada, listaOcurrenciaMensual]
			matrizJornadas.append(dicJornada)

		#"""Clasificador de Categorias"""
		for i in range(0, len(categoriasE)):
			categoria = categoriasE[i].entregarEtiqueta()
			metrica= categoriasE[i].entregarMagnitud()
			metricaPrevia= categoriasE[i-1].entregarMagnitud()			
			listaOcurrenciaMensual = [0]
			for j in range(1, 13):
				ocurrenciaMes = 0
				for evento in eventos:
					mesEvento = evento.entregarFecha().month
					intensidadMediaEvento = evento.entregarIntensidadMedia()
					if mesEvento <= j:
						if mesEvento == j:
							if i == 0:
								if intensidadMediaEvento <= metrica:
									ocurrenciaMes+=1
							else:
								if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
									ocurrenciaMes+=1
					else:
						break
				listaOcurrenciaMensual.append(ocurrenciaMes)			
			dicCategoria=[categoria, listaOcurrenciaMensual]
			matrizCategorias.append(dicCategoria)


		#"""Clasificador de Maximos"""
		for i in range (1, 13):
			resultadoMes = self.entregarMaximos(1, i)
			listaMaximos.append(resultadoMes)

		resumenMensualAnual = [matrizJornadas, matrizCategorias, listaMaximos]
		totales = self.cacularTotales(resumenMensualAnual)
		resumenMensualAnual.append(totales)
		return resumenMensualAnual


	def resumenSemestral(self):
		eventos = self.entregarColeccionEventos()
		matrizJornadas=[]
		matrizCategorias=[]
		listaMaximos=[]
		jornadasE = self.entregarListaJornadas()
		categoriasE = self.entregarListaCategorias()
		#"""Clasificador de Jornadas"""
		for i in range(0, len(jornadasE)):
			jornada = jornadasE[i].entregarEtiquetaJornada()
			horaInicio = jornadasE[i].entregarHoraInicio()
			horaFin = jornadasE[i].entregarHoraFin()
			listaOcurrenciaSemestral = [0]
			for i in range(1, 3):
				if i == 1:
					ocurrenciaSemestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=1 and mesEvento<=6 :							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaSemestre+=1
						else:
							listaOcurrenciaSemestral.append(ocurrenciaSemestre)
							break
				else:
					ocurrenciaSemestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=7 and mesEvento<=12 :							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaSemestre+=1
					
					listaOcurrenciaSemestral.append(ocurrenciaSemestre)					
			dicJornada=[jornada, listaOcurrenciaSemestral]
			matrizJornadas.append(dicJornada)
		#"""Clasificador de Categorias"""
		for i in range(0, len(categoriasE)):
			categoria = categoriasE[i].entregarEtiqueta()
			metrica= categoriasE[i].entregarMagnitud()
			metricaPrevia  = categoriasE[i-1].entregarMagnitud()
			listaOcurrenciaSemestral = [0]
			for j in range(1, 3):
				ocurrenciaSemestre = 0
				if j == 1:					
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=1 and mesEvento<=6 :							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaSemestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaSemestre+=1
						else:
							listaOcurrenciaSemestral.append(ocurrenciaSemestre)
							break
				else:
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=7 and mesEvento<=12 :							
								if intensidadMediaEvento <= metrica:
									if i == 0:
										if intensidadMediaEvento <= metrica:
											ocurrenciaSemestre+=1
									else:
										if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
											ocurrenciaSemestre+=1
					listaOcurrenciaSemestral.append(ocurrenciaSemestre)			
			dicCategoria=[categoria, listaOcurrenciaSemestral]
			matrizCategorias.append(dicCategoria)
		#"""Clasificador de Maximos"""
		for i in range (1, 3):
			resultadoMes = self.entregarMaximos(2, i)
			listaMaximos.append(resultadoMes)

		resumenSemestral = [matrizJornadas, matrizCategorias, listaMaximos]
		totales = self.cacularTotales(resumenSemestral)
		resumenSemestral.append(totales)
		return resumenSemestral


	def resumenTrimestral(self):
		eventos = self.entregarColeccionEventos()
		matrizJornadas=[]
		matrizCategorias=[]
		listaMaximos=[]
		jornadasE = self.entregarListaJornadas()
		categoriasE = self.entregarListaCategorias()

		#"""Clasificador de Jornadas"""
		for i in range(0, len(jornadasE)):
			jornada = jornadasE[i].entregarEtiquetaJornada()
			horaInicio = jornadasE[i].entregarHoraInicio()
			horaFin = jornadasE[i].entregarHoraFin()
			listaOcurrenciaTrimestral = [0]
			for i in range(1, 5):
				if i == 1:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento<=3:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				elif i == 2:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=4 and mesEvento<=6:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				elif i == 3:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=7 and mesEvento<=9:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
				else:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=10 and mesEvento<=12:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
			dicJornada=[jornada, listaOcurrenciaTrimestral]
			matrizJornadas.append(dicJornada)

		#"""Clasificador de Categorias"""
		for i in range(0, len(categoriasE)):
			categoria = categoriasE[i].entregarEtiqueta()
			metrica= categoriasE[i].entregarMagnitud()	
			metricaPrevia = categoriasE[i-1].entregarMagnitud() 		
			listaOcurrenciaTrimestral = [0]
			for j in range(1, 5):
				if j == 1:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento<=3:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				elif j == 2:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=4 and mesEvento <=6:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
				elif j == 3:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=7 and mesEvento<=9:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				else:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=10 and mesEvento<=12:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
			dicCategoria=[categoria, listaOcurrenciaTrimestral]
			matrizCategorias.append(dicCategoria)
		#"""Clasificador de Maximos"""
		for i in range (1, 5):
			resultadoMes = self.entregarMaximos(3, i)
			listaMaximos.append(resultadoMes)

		resumenTrimestral = [matrizJornadas, matrizCategorias, listaMaximos]
		totales = self.cacularTotales(resumenTrimestral)
		resumenTrimestral.append(totales)
		return resumenTrimestral


	"""Resumen Trimestral Bimodal"""
	def resumenTrimestralBimodal(self):
		eventos = self.entregarColeccionEventos()
		matrizJornadas=[]
		matrizCategorias=[]
		listaMaximos=[]
		jornadasE = self.entregarListaJornadas()
		categoriasE = self.entregarListaCategorias()

		#"""Clasificador de Jornadas"""
		for i in range(0, len(jornadasE)):
			jornada = jornadasE[i].entregarEtiquetaJornada()
			horaInicio = jornadasE[i].entregarHoraInicio()
			horaFin = jornadasE[i].entregarHoraFin()
			listaOcurrenciaTrimestral = [0]
			for i in range(1, 5):
				if i == 1:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento<=2:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				elif i == 2:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=3 and mesEvento<6:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				elif i == 3:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=6 and mesEvento<9:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
				else:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						horaInicioE = evento.entregarHoraInicio().hour
						horaFinE = evento.entregarHoraFin().hour
						if mesEvento>=9 and mesEvento<12:							
								if (horaInicioE >= horaInicio) and (horaInicioE < horaFin):
									ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
			dicJornada=[jornada, listaOcurrenciaTrimestral]
			matrizJornadas.append(dicJornada)

		#"""Clasificador de Categorias"""
		for i in range(0, len(categoriasE)):
			categoria = categoriasE[i].entregarEtiqueta()
			metrica= categoriasE[i].entregarMagnitud()	
			metricaPrevia = categoriasE[i-1].entregarMagnitud() 		
			listaOcurrenciaTrimestral = [0]
			for j in range(1, 5):
				if j == 1:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento<=2:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				elif j == 2:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=3 and mesEvento <6:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
				elif j == 3:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=6 and mesEvento<9:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
					
				else:
					ocurrenciaTrimestre = 0
					for evento in eventos:
						mesEvento = evento.entregarFecha().month
						intensidadMediaEvento = evento.entregarIntensidadMedia()
						if mesEvento>=9 and mesEvento<12:							
								if i == 0:
									if intensidadMediaEvento <= metrica:
										ocurrenciaTrimestre+=1
								else:
									if intensidadMediaEvento> metricaPrevia and intensidadMediaEvento<=metrica:
										ocurrenciaTrimestre+=1
					listaOcurrenciaTrimestral.append(ocurrenciaTrimestre)
			dicCategoria=[categoria, listaOcurrenciaTrimestral]
			matrizCategorias.append(dicCategoria)
		#"""Clasificador de Maximos"""
		for i in range (1, 5):
			resultadoMes = self.entregarMaximos(3, i)
			listaMaximos.append(resultadoMes)

		resumenTrimestral = [matrizJornadas, matrizCategorias, listaMaximos]
		totales = self.cacularTotales(resumenTrimestral)
		resumenTrimestral.append(totales)
		return resumenTrimestral


	def cacularTotales(self, colecciones):
		jornadas = colecciones[0]
		categorias = colecciones[1]
		maximos = colecciones[2]
		totalesJornadas = [0]
		totalesCategorias = [0]
		totalesMaximos = []

		listaPeriodosJ = jornadas[0][1]
		for i in range(1, len(listaPeriodosJ)):
			totalPeriodo=0
			for j in range(0, len(jornadas)):
				totalPeriodo+=jornadas[j][1][i]
			totalesJornadas.append(totalPeriodo)

		listaPeriodosC = categorias[0][1]
		for i in range(1, len(listaPeriodosC)):
			totalPeriodo=0
			for j in range(0, len(categorias)):
				totalPeriodo+=categorias[j][1][i]
			totalesCategorias.append(totalPeriodo)

		listaPeriodosM = len(maximos)
		for i in range(0, 4):
			totalPeriodo = 0
			for j in range(0, listaPeriodosM):
				totalPeriodo+=maximos[j][i]
			totalesMaximos.append(totalPeriodo)

		totalesCompletos = [totalesJornadas, totalesCategorias, totalesMaximos]
		return totalesCompletos


	def generarResumenEventos(self, opcionResumenP, parametrosP, estacionIdP, jornadasP, categoriasP):


	def crearResumenJornadas		


	def crearResumenCategorias(self, opcionResumenP, parametrosP, estacionIdP, categoriasP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionIdP)
			if opcionBusquedaP == 1:
				#Aqui deberia definir la estructura que manejaria para cada caso
				# y Aqui iniciaria la iteracion sobre cada Categoria en este caso...
				# El contenido de la iteracion consiste en ejecutar las sentencias en busca de eventos con la categoria semjante
				#Recordar que se obtienen los dao eventos que cumplen pero tan solo interesa cuantos son y ese sera el numero que
				#interesara
				#Teniedo en cuenta que si obtengo todos los datos en una variable la deberia enviar para sacar los maximos....
				eventosDao = estacionDaoP.eventos.select("fecha = ?", [parametrosP])
				eventos = self.transformarEventosModelo(eventosDao)
				return eventos
			elif opcionBusquedaP == 2:
				eventosDao = estacionDaoP.eventos.select("strftime('%Y-%d', fecha) = ?", [parametrosP])
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

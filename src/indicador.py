from datetime import date

class indicadorA(object):
	
	def __init__(self, cEventosP, indicadorP):
		super(indicadorA, self).__init__()
		self.coleccionEventos = cEventosP
		self.indicador = indicadorP
		self.indicadorCalculado = 0
	
	def entregarIndicadorParametrizado(self):
		return self.indicador

	def modificarIndicarCalculado(self, caluloIndicador):
		return self.indicadorCalculado

	def entregarColeccionEventos(self):
		return self.coleccionEventos

	def calcularIndicador(self, diaP, mesP, anoP):
		limiteMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		conteoIndicador = self.entregarIndicadorParametrizado()
		coleccionEventos = self.entregarColeccionEventos()

		indicadorCalculadoTemp = 0

		if mesP == 1:
			if diaP < conteoIndicador:
				diasFaltantes = conteoIndicador - diaP
				diaInicio = (31 - diasFaltantes) + 1
				fechaInicio = date((anoP - 1), 12, diaInicio)

			else:
				if diaInicio == conteoIndicador:
					diaInicio = 1
				else:
					diasFaltantes = (conteoIndicador - diaP) + 1
					diaInicio = diasFaltantes

				fechaInicio = date(anoP, 1, diaInicio)

		elif mes == 3:
			if anoP % 4 == 0:
				#Ano Bisiesto
				if diaP < conteoIndicador:
					if diaP < conteoIndicador:
						diasFaltantes = conteoIndicador - diaP
						diaInicio = (29 - diasFaltantes) + 1
						fechaInicio = date(anoP, 2, diaInicio)
				else:
					if diaP == conteoIndicador:
						diaInicio = 1
					else:
						diasFaltantes = (conteoIndicador - diaP) + 1
						diaInicio = diasFaltantes
				fechaInicio = date(anoP, 3, diaInicio)
			else:
				if diaP < conteoIndicador:
					if diaP < conteoIndicador:
						diasFaltantes = conteoIndicador - diaP
						diaInicio = (28 - diasFaltantes) + 1
						fechaInicio = date(anoP, 2, diaInicio)
				else:
					if diaP == conteoIndicador:
						diaInicio = 1
					else:
						diasFaltantes = (conteoIndicador - diaP) + 1
						diaInicio = diasFaltantes

				fechaInicio = date(anoP, 3, diaInicio)
		else:
			if diaP < conteoIndicador:
				diasFaltantes = conteoIndicador - diaP
				diaInicio = limiteMes[(mesP - 1)] - diasFaltantes
				fechaInicio = date(anoP, (mesP - 1), diaInicio)
			
			else:
				if diaP == conteoIndicador:
					diaInicio = 1
				else:
					diasFaltantes = (conteoIndicador - diaP	) + 1
					diaInicio = diasFaltantes

				fechaInicio = date(anoP, mesP, diaInicio)

		fechaFin = date(anoP, mesP, diaP)
		cantidadEventosEncontrados = 0
		for evento in coleccionEventos:
			if evento.entregarFecha() >= fechaInicio:
				if evento.entregarFecha <= fechaFin:
					cantidadEventosEncontrados+=1
					indicadorCalculadoTemp += evento.entregarIntensidadMedia()
				else:
					break

		self.modificarIndicarCalculado(indicadorCalculadoTemp)
		


				









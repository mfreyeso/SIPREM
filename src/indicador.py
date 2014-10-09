import models
import macaron
import registro as reg
import datetime
import acumulado as acm

class indicadorA(object):
	
	def __init__(self, cEventosP, indicadorP):
		super(indicadorA, self).__init__()
		self.indicador = indicadorP
			
	def entregarIndicadorParametrizado(self):
		return self.indicador

	def modificarIndicarCalculado(self, caluloIndicador):
		return self.indicadorCalculado

	def entregarDiasMes(self, fechaP):
		dias = ["-", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		mes = int(fechaP.split("-")[1])
		ano = int(fechaP.split("-")[0])
		if mes == 2:
			if( ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
				#Bisiesto
				return 29
		return dias[mes]

	def entregarFechaInicialIndicador(self, diaP, mesP, anoP):
		if diaP > self.entregarIndicadorParametrizado():
			diaInicial = self.entregarIndicadorParametrizado() - diaP
			mesInicial = mesP
			anoInicial = anoP			
		elif diaP < self.entregarIndicadorParametrizado():
			if mesP == 1:
				diaInicial = self.entregarDiasMes(12) + (diaP - self.entregarIndicadorParametrizado())
				mesInicial = 12
				anoInicial = anoP - 1
			else:
				diaInicial = self.entregarDiasMes(mesP - 1) + (diaP - self.entregarIndicadorParametrizado())
				mesInicial = mesP - 1
				anoInicial = anoP
		else:
			diaInicial = 1
			mesInicial = mesP
			anoInicial = anoP
		fechaInicial = datetime.date(anoInicial, mesInicial, diaInicial) 
		return fechaInicial

	def calcularIndicador(self, opcionBusquedaP, parametrosP, estacionIdP):
		try:
			objetoAcumulador = acm.acumulado()
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionIdP)
			resultados = ["X"]
			if opcionBusquedaP == 1:
				#Diario - Anual
				for m in range(1, 13):
					datosMes = []
					if m < 10:
						mes = "0" + str(m)
					else:
						mes = str(m)
					diasMes = [0]
					for d in range(1, (self.entregardiasMes(m, int(parametrosP)) + 1)):
						if d < 10:
							dia = "0" + str(d)
						else:
							dia = str(d)
						fechaInicial = str(self.entregarFechaInicialIndicador(d, m, int(parametrosP)))
						fechaFinal = parametrosP + "-" + mes + "-" + dia
						registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
						registros = self.transformarRegistros(registrosDao)
						diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
					datosMes.append(diasMes)
					objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
					datosMes.append(objEstadistico)
					resultados.append(datosMes)					
			elif opcionBusquedaP == 2:
				#Semestral
				if parametrosP[0] == 1:
					for m in range(1, 7):
						datosSemestre = []
						mes = "0" + str(m)
						diasMes = [0]
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)							
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosSemestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosSemestre.append(objEstadistico)
						resultados.append(datosSemestre)
				else:
					for m in range(7, 13):
						datosSemestre = []
						if m < 10:
							mes = "0" + str(m)
						else:
							mes = str(m)
						diasMes = [0]
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosSemestre.append(diasMes)					
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosSemestre.append(objEstadistico)
						resultados.append(datosSemestre)
			elif opcionBusquedaP == 3:
				#Trimestre Bimodal
				resultados = ["X"]				
				if parametrosP[0] == 1:
					datosTrimestre = []
					#Mes Diciembre Ano Anterior
					diasMes = [0]
					mes = str(12)
					for d in range(1, (self.entregardiasMes(12, (parametrosP[1] - 1)) + 1)):
						if d < 10:
							dia = "0" + str(d)
						else:
							dia = str(d)
						fechaInicial = str(self.entregarFechaInicialIndicador(d, m, (parametrosP[1] - 1)))
						fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
						registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
						registros = self.transformarRegistros(registrosDao)
						diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
					datosTrimestre.append(diasMes)
					objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
					datosTrimestre.append(objEstadistico)
					resultados.append(datosTrimestre)

					for m in range(1, 3):
						datosTrimestre = []
						diasMes = [0]
						mes = "0" + str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
				elif parametrosP[0] == 2:
					for m in range (3, 6):
						datosTrimestre = []
						diasMes = [0]
						mes = "0" + str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1])) + 1):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
				elif parametrosP[0] == 3:
					for m in range(6, 9):
						datosTrimestre = []
						diasMes = [0]
						mes = "0" + str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
				else:
					for m in range(9, 12):
						datosTrimestre = []
						diasMes = [0]
						if m < 10:
							mes = "0" + str(m)
						else:
							mes = str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
			else:
				#Trimestre Estandar
				resultados = ["X"]
				if parametrosP[0] == 1:
					for m in range(1, 4):
						datosTrimestre = []
						diasMes = [0]
						mes = "0" + str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
				elif parametrosP[0] == 2:
					for m in range (4, 7):
						datosTrimestre = []
						diasMes = [0]
						mes = "0" + str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
				elif parametrosP[0] == 3:
					for m in range(7, 10):
						datosTrimestre = []
						diasMes = [0]
						mes = "0" + str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) +1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
				else:
					for m in range(10, 13):
						datosTrimestre = []
						diasMes = [0]
						if m < 10:
							mes = "0" + str(m)
						else:
							mes = str(m)
						for d in range(1, (self.entregardiasMes(m, parametrosP[1]) + 1)):
							if d < 10:
								dia = "0" + str(d)
							else:
								dia = str(d)
							fechaInicial = str(self.entregarFechaInicialIndicador(d, m, parametrosP[1]))
							fechaFinal = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicial, fechaFinal])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
			return resultados	
		except Exception, e:
			print e

	def entregardiasMes(self, mesP, anoP):
		dias = ["-", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		mes = mesP
		ano = anoP
		if mes == 2:
			if( ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
				#Bisiesto
				return 29
		return dias[mes]



				









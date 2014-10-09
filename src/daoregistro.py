import models
import macaron
import registro as reg
import datetime
import acumulado as acm

class RegistroDao(object):
	"""docstring for RegistroDao"""
	def __init__(self):
		super(RegistroDao, self).__init__()

	def almacenarRegistros(self, kernelRegistrosP, estacionId):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionId)
			for registroP in kernelRegistrosP:
				if registroP.entregarPrecipitacion() != 0 and registroP.entregarPrecipitacion() != "-":
					estacionDaoP.estacionreg.append(
					fecha = str(registroP.entregarFecha()),
					hora = str(registroP.entregarHora()),
					vprec = registroP.entregarPrecipitacion()
					)
			macaron.bake()
		except Exception, e:
			print e

	def buscarRegistros(self, fechaInicialP, fechaFinalP, estacionIdP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionId)
			registrosDao = estacionDaoP.estacionreg.select("fecha between ? and ?", [fechaInicialP, fechaFinalP])
			registros = self.transformarRegistros(registrosDao)
			return registros
		except Exception, e:
			raise e

	def transformarRegistros(self, coleccionRegistrosDaoP):
		registrosTransformados = []
		for registroD  in coleccionRegistrosDaoP:
			objRegistro = reg.registro(
				registroD.fecha,
				registroD.hora,
				registroD.vprec)
			registrosTransformados.append(objRegistro)
		return registrosTransformados

	def busquedaParametrizada(self, opcionBusquedaP, parametrosP, estacionIdP):
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
						fechaBusqueda = parametrosP +"-"+mes+"-"+dia
						registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
						fechaBusqueda = str((parametrosP[1] - 1)) + "-" + mes + "-" + dia 
						registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?",  [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" +  dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
			elif opcionBusquedaP == 4:
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" + dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?",  [fechaBusqueda])
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
							fechaBusqueda = str(parametrosP[1]) + "-" + mes + "-" +  dia
							registrosDao = estacionDaoP.estacionreg.select("fecha = ?", [fechaBusqueda])
							registros = self.transformarRegistros(registrosDao)
							diasMes.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
						datosTrimestre.append(diasMes)
						objEstadistico = objetoAcumulador.calcularEstadisticos(diasMes)
						datosTrimestre.append(objEstadistico)
						resultados.append(datosTrimestre)
			else:
				#Multianual
				resultados = ["X"]
				anoInicial = parametrosP[0]
				anoFinal = parametrosP [1]
				for a in range(anoInicial, (anoFinal + 1)):
					datosAno = []
					meses = [0]
					for m in range(1, 13):
						if m < 10:
							mes = "0" + str(m)
						else:
							mes = str(m)
						fechaBusqueda = str(a) + "-" + mes
						registrosDao = estacionDaoP.estacionreg.select("strftime('%Y-%m', fecha) = ?", [fechaBusqueda])
						registros = self.transformarRegistros(registrosDao)
						meses.append(objetoAcumulador.calcularAcumuladoMagnitudRegistros(registros))
					datosAno.append(meses)
					objEstadistico = objetoAcumulador.calcularEstadisticos(meses)
					datosAno.append(objEstadistico)
					resultados.append(datosAno)
			return resultados	
		except Exception, e:
			print e

	def febreroBisiesto(self, anoP):
		if( anoP % 4 == 0 and anoP % 100 != 0 or anoP % 400 == 0):
			#Ano Bisiesto
			return 29
		else:
			return 28

	def validarRegistros(self, kernelRegistrosP, estacionId):
		registrosValidos = []
		try:
			macaron.macaronage("siprem.db")
			estacion = models.Estacion.get(estacionId)
			for registro in kernelRegistrosP:
				if registro.entregarPrecipitacion() != 0 and registro.entregarPrecipitacion() != "-":
					fecha = registro.entregarFecha()
					hora = registro.entregarHora()
					registroQ = estacion.estacionreg.select("fecha = ? and hora =?", [str(fecha), str(hora)])
					if registroQ.count() == 0:
						registrosValidos.append(registro)
			return registrosValidos
		except Exception, e:
			print e
			return None
	
	def entregardiasMes(self, mesP, anoP):
		dias = ["-", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		mes = mesP
		ano = anoP
		if mes == 2:
			if( ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
				#Bisiesto
				return 29
		return dias[mes]

import daoevento as dev
import datetime
import macaron
import models



class resumen(object):	
	def __init__(self):
		super(resumen, self).__init__()
	
	def generarResumenEventos(self, opcionResumenP, parametrosP, estacionIdP, jornadasP, categoriasP):
		resCategorias = self.crearResumenCategorias(opcionResumenP, parametrosP, estacionIdP, categoriasP)
		resJornadas = self.crearResumenJornadas(opcionResumenP, parametrosP, estacionIdP, jornadasP)
		resMaximos = self.crearResumenMaximos(opcionResumenP, parametrosP, estacionIdP)
		resumen = [resCategorias, resJornadas, resMaximos]
		return resumen

	def crearResumenCategorias(self, opcionResumenP, parametrosP, estacionIdP, categoriasP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionIdP)
			if opcionResumenP == 1:
				resultados = []
				for categoria in categoriasP:
					nombreCategoria = categoria.entregarEtiqueta()
					eventosDao = estacionDaoP.eventos.select("fecha = ? and tipoprec = ?", [parametrosP, nombreCategoria])
					resultados.append(eventosDao.count())
				return resultados
			elif opcionResumenP == 2:
				resultados = []
				for categoria in categoriasP:
					nombreCategoria = categoria.entregarEtiqueta()
					dias = ["-"]
					for i in range(1, (self.diasMes(parametrosP) + 1)):
						eventosDao = estacionDaoP.eventos.select("strftime('%Y-%m', fecha) = ? and strftime('%d', fecha) = ? and tipoprec = ?", [parametrosP, str(i), nombreCategoria])
						dias.append(eventosDao.count())
					resultados.append(dias)
				return resultados
			elif opcionResumenP == 3:
				resultados = []
				for categoria in categoriasP:
					nombreCategoria = categoria.entregarEtiqueta()
					meses =["-"]
					for i in range(1, 13):
						if i != 10 and i != 11 and i != 12:
							mesc = "0"+str(i)
						else:
							mesc = i
						eventosDao = estacionDaoP.eventos.select("strftime('%Y', fecha) = ? and strftime('%m', fecha) = ? and tipoprec = ?", [parametrosP, str(mesc), nombreCategoria])
						meses.append(eventosDao.count())
					resultados.append(meses)
				return resultados
			elif opcionResumenP == 4:
				resultados = []
				for i in range(1, 3):
					if i == 1:
						fechaInicial = datetime.date(parametrosP[1], 1, 1)
						fechaFinal = datetime.date(parametrosP[1], 6, 30)
					else:
						fechaInicial = datetime.date(parametrosP[1], 7, 1)
						fechaFinal = datetime.date(parametrosP[1], 12, 31)
					semestre = []
					for categoria  in categoriasP:
						nombreCategoria = categoria.entregarEtiqueta()
						eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and tipoprec = ?", [str(fechaInicial), str(fechaFinal), nombreCategoria])
						semestre.append(eventosDao.count())
					resultados.append(semestre)
				return resultados
			elif opcionResumenP == 5:
				#Trimestre Bimodal
				resultados = []
				for i in range(1, 5):
					if i == 1:
						fechaInicial = datetime.date((parametrosP[1]-1), 12, 1)
						fechaFinal = datetime.date(parametrosP[1], 2, self.febreroBisiesto(parametrosP[1]))
					elif i == 2:
						fechaInicial = datetime.date(parametrosP[1], 3, 1)
						fechaFinal = datetime.date(parametrosP[1], 5, 31)
					elif i == 3:
						fechaInicial = datetime.date(parametrosP[1], 6, 1)
						fechaFinal = datetime.date(parametrosP[1], 8, 31)
					else:
						fechaInicial = datetime.date(parametrosP[1], 9, 1)
						fechaFinal = datetime.date(parametrosP[1], 11, 30)
					trimestre =[]
					for categoria in categoriasP:
						nombreCategoria = categoria.entregarEtiqueta()
						eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and tipoprec = ?", [str(fechaInicial), str(fechaFinal), nombreCategoria])
						trimestre.append(eventosDao.count())
					resultados.append(trimestre)
				return resultados
			elif opcionResumenP == 6:
				#Trimestre Estandar
				resultados = []
				for i in range(1, 5):					
					if i == 1:
						fechaInicial = datetime.date(parametrosP[1], 1, 1)
						fechaFinal = datetime.date(parametrosP[1], 3, 31)
					elif i == 2:
						fechaInicial = datetime.date(parametrosP[1], 4, 1)
						fechaFinal = datetime.date(parametrosP[1], 6, 30)
					elif i == 3:
						fechaInicial = datetime.date(parametrosP[1], 7, 1)
						fechaFinal = datetime.date(parametrosP[1], 9, 30)
					else:
						fechaInicial = datetime.date(parametrosP[1], 10, 1)
						fechaFinal = datetime.date(parametrosP[1], 12, 31)
					trimestre = []
					for categoria in categoriasP:
						nombreCategoria = categoria.entregarEtiqueta()
						eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and tipoprec = ?", [str(fechaInicial), str(fechaFinal), nombreCategoria])
						trimestre.append(eventosDao.count())
					resultados.append(trimestre)
				return resultados
			elif opcionResumenP == 7:
				#Multianual
				resultados = []
				for i in range(parametrosP[0], (parametrosP[1] + 1)):
					ano = []
					for categoria in categoriasP:
						nombreCategoria = categoria.entregarEtiqueta()
						eventosDao = estacionDaoP.eventos.select("strftime('%Y', fecha) = ? and tipoprec = ?", [str(i), nombreCategoria])
						ano.append(eventosDao.count())
					resultados.append(ano)
				return resultados 
			else:
				resultados = []
				for categoria in categoriasP:
					nombreCategoria = categoria.entregarEtiqueta()
					eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and tipoprec = ?", [parametrosP[0], parametrosP[1], nombreCategoria])
					resultados.append(eventosDao.count())
				return resultados		
		except Exception, e:
			print e

	def crearResumenJornadas(self, opcionResumenP, parametrosP, estacionIdP, jornadasP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionIdP)
			if opcionResumenP == 1:
				resultados = []
				for jornada in jornadasP:
					nombreJornada = jornada.entregarEtiquetaJornada()
					eventosDao = estacionDaoP.eventos.select("fecha = ? and jorprec = ?", [parametrosP, nombreJornada])
					resultados.append(eventosDao.count())
				return resultados
			elif opcionResumenP == 2:
				resultados = []
				for jornada in jornadasP:
					nombreJornada = jornada.entregarEtiquetaJornada()
					dias = ["-"]
					for i in range(1, (self.diasMes(parametrosP) + 1)):
						eventosDao = estacionDaoP.eventos.select("strftime('%Y-%m', fecha) = ? and strftime('%d', fecha) = ? and jorprec = ?", [parametrosP, str(i), nombreJornada])
						dias.append(eventosDao.count())
					resultados.append(dias)
				return resultados
			elif opcionResumenP == 3:
				resultados = []
				for jornada in jornadasP:
					nombreJornada = jornada.entregarEtiquetaJornada()
					meses =["-"]
					for i in range(1, 13):
						if i != 10 and i != 11 and i != 12:
							mesc = "0"+str(i)
						else:
							mesc = i
						eventosDao = estacionDaoP.eventos.select("strftime('%Y', fecha) = ? and strftime('%m', fecha) = ? and jorprec = ?", [parametrosP, str(mesc), nombreJornada])
						meses.append(eventosDao.count())
					resultados.append(meses)
				return resultados
			elif opcionResumenP == 4:
				resultados = []
				for i in range(1, 3):
					if i == 1:
						fechaInicial = datetime.date(parametrosP[1], 1, 1)
						fechaFinal = datetime.date(parametrosP[1], 6, 30)
					else:
						fechaInicial = datetime.date(parametrosP[1], 7, 1)
						fechaFinal = datetime.date(parametrosP[1], 12, 31)
					semestre = []
					for jornada  in jornadasP:
						nombreJornada = jornada.entregarEtiquetaJornada()
						eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and jorprec = ?", [str(fechaInicial), str(fechaFinal), nombreJornada])
						semestre.append(eventosDao.count())
					resultados.append(semestre)
				return resultados
			elif opcionResumenP == 5:
				#Trimestre Bimodal
				resultados = []
				for i in range(1, 5):
					if i == 1:
						fechaInicial = datetime.date((parametrosP[1]-1), 12, 1)
						fechaFinal = datetime.date(parametrosP[1], 2, self.febreroBisiesto(parametrosP[1]))
					elif i == 2:
						fechaInicial = datetime.date(parametrosP[1], 3, 1)
						fechaFinal = datetime.date(parametrosP[1], 5, 31)
					elif i == 3:
						fechaInicial = datetime.date(parametrosP[1], 6, 1)
						fechaFinal = datetime.date(parametrosP[1], 8, 31)
					else:
						fechaInicial = datetime.date(parametrosP[1], 9, 1)
						fechaFinal = datetime.date(parametrosP[1], 11, 30)
					trimestre =[]
					for jornada in jornadasP:
						nombreJornada = jornada.entregarEtiquetaJornada()
						eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and jorprec = ?", [str(fechaInicial), str(fechaFinal), nombreJornada])
						trimestre.append(eventosDao.count())
					resultados.append(trimestre)
				return resultados
			elif opcionResumenP == 6:
				#Trimestre Estandar
				resultados = []
				for i in range(1, 5):					
					if i == 1:
						fechaInicial = datetime.date(parametrosP[1], 1, 1)
						fechaFinal = datetime.date(parametrosP[1], 3, 31)
					elif i == 2:
						fechaInicial = datetime.date(parametrosP[1], 4, 1)
						fechaFinal = datetime.date(parametrosP[1], 6, 30)
					elif i == 3:
						fechaInicial = datetime.date(parametrosP[1], 7, 1)
						fechaFinal = datetime.date(parametrosP[1], 9, 30)
					else:
						fechaInicial = datetime.date(parametrosP[1], 10, 1)
						fechaFinal = datetime.date(parametrosP[1], 12, 31)
					trimestre = []
					for jornada in jornadasP:
						nombreJornada = jornada.entregarEtiquetaJornada()
						eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and jorprec = ?", [str(fechaInicial), str(fechaFinal), nombreJornada])
						trimestre.append(eventosDao.count())
					resultados.append(trimestre)
				return resultados
			elif opcionResumenP == 7:
				#Multianual
				resultados = []
				for i in range(parametrosP[0], (parametrosP[1] + 1)):
					ano = []
					for jornada in jornadasP:
						nombreJornada = jornada.entregarEtiquetaJornada()
						eventosDao = estacionDaoP.eventos.select("strftime('%Y', fecha) = ? and jorprec = ?", [str(i), nombreJornada])
						ano.append(eventosDao.count())
					resultados.append(ano)
				return resultados 
			else:
				resultados = []
				for jornada in jornadasP:
					nombreJornada = jornada.entregarEtiquetaJornada()
					eventosDao = estacionDaoP.eventos.select("fecha between ? and ? and jorprec = ?", [parametrosP[0], parametrosP[1], nombreJornada])
					resultados.append(eventosDao.count())
				return resultados		
		except Exception, e:
			print e

	def crearResumenMaximos(self, opcionResumenP, parametrosP, estacionIdP):
		try:
			macaron.macaronage("siprem.db")
			estacionDaoP = models.Estacion.get(estacionIdP)
			if opcionResumenP == 1:
				eventosDao = estacionDaoP.eventos.select("fecha = ?", [parametrosP])
				resultados = self.determinarMaximos(eventosDao)
				return resultados
			elif opcionResumenP == 2:
				dias = ["-"]
				for i in range(1, (self.diasMes(parametrosP) + 1)):
					eventosDao = estacionDaoP.eventos.select("strftime('%Y-%m', fecha) = ? and strftime('%d', fecha) = ?", [parametrosP, str(i)])
					dias.append(self.determinarMaximos(eventosDao))
				resultados = dias
				return resultados
			elif opcionResumenP == 3:
				meses =["-"]
				for i in range(1, 13):
					if i != 10 and i != 11 and i != 12:
						mesc = "0"+str(i)
					else:
						mesc = i
					eventosDao = estacionDaoP.eventos.select("strftime('%Y', fecha) = ? and strftime('%m', fecha) = ?", [parametrosP, str(mesc)])
					meses.append(self.determinarMaximos(eventosDao))
				resultados = meses
				return resultados
			elif opcionResumenP == 4:
				semestres = []
				for i in range(1, 3):
					if i == 1:
						fechaInicial = datetime.date(parametrosP[1], 1, 1)
						fechaFinal = datetime.date(parametrosP[1], 6, 30)
					else:
						fechaInicial = datetime.date(parametrosP[1], 7, 1)
						fechaFinal = datetime.date(parametrosP[1], 12, 31)
					eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
					semestres.append(self.determinarMaximos(eventosDao))
				resultados = semestres
				return resultados
			elif opcionResumenP == 5:
				#Trimestre Bimodal
				trimestres = []
				for i in range(1, 5):
					if i == 1:
						fechaInicial = datetime.date((parametrosP[1]-1), 12, 1)
						fechaFinal = datetime.date(parametrosP[1], 2, self.febreroBisiesto(parametrosP[1]))
					elif i == 2:
						fechaInicial = datetime.date(parametrosP[1], 3, 1)
						fechaFinal = datetime.date(parametrosP[1], 5, 31)
					elif i == 3:
						fechaInicial = datetime.date(parametrosP[1], 6, 1)
						fechaFinal = datetime.date(parametrosP[1], 8, 31)
					else:
						fechaInicial = datetime.date(parametrosP[1], 9, 1)
						fechaFinal = datetime.date(parametrosP[1], 11, 30)
					eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
					trimestres.append(self.determinarMaximos(eventosDao))
				resultados = trimestres
				return resultados
			elif opcionResumenP == 6:
				#Trimestre Estandar
				trimestres = []
				for i in range(1, 5):					
					if i == 1:
						fechaInicial = datetime.date(parametrosP[1], 1, 1)
						fechaFinal = datetime.date(parametrosP[1], 3, 31)
					elif i == 2:
						fechaInicial = datetime.date(parametrosP[1], 4, 1)
						fechaFinal = datetime.date(parametrosP[1], 6, 30)
					elif i == 3:
						fechaInicial = datetime.date(parametrosP[1], 7, 1)
						fechaFinal = datetime.date(parametrosP[1], 9, 30)
					else:
						fechaInicial = datetime.date(parametrosP[1], 10, 1)
						fechaFinal = datetime.date(parametrosP[1], 12, 31)
					eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [str(fechaInicial), str(fechaFinal)])
					trimestres.append(self.determinarMaximos(eventosDao))
				resultados = trimestres
				return resultados
			elif opcionResumenP == 7:
				#Multianual
				anos = []
				for i in range(parametrosP[0], (parametrosP[1] + 1)):
					eventosDao = estacionDaoP.eventos.select("strftime('%Y', fecha) = ?", [str(i)])
					anos.append(self.determinarMaximos(eventosDao))
				resultados = anos
				return resultados 
			else:
				resultados = []
				eventosDao = estacionDaoP.eventos.select("fecha between ? and ?", [parametrosP[0], parametrosP[1]])
				resultados = self.determinarMaximos(eventosDao)
				return resultados		
		except Exception, e:
			print e

	def determinarMaximos(self, coleccionEventosP):
		objDao = dev.EventoDao()
		eventos = objDao.transformarEventosModelo(coleccionEventosP)
		resultados = [self.maximaDuracion(eventos),
		self.maximaMagnitud(eventos),
		self.maximaIntensidadMedia(eventos),
		self.maximaIntensidadMaxima(eventos)]
		return resultados

	def maximaDuracion(self, coleccionEventosP):
		duracion = 0
		for evento in coleccionEventosP:
			if evento.entregarDuracion() > duracion:
				duracion = evento.entregarDuracion()
		return duracion

	def maximaMagnitud(self, coleccionEventosP):
		magnitud = 0
		for evento in coleccionEventosP:
			if evento.entregarMagnitud() > magnitud:
				magnitud = evento.entregarMagnitud()
		return magnitud

	def maximaIntensidadMedia(self, coleccionEventosP):
		imedia = 0
		for evento in coleccionEventosP:
			if evento.entregarIntensidadMedia() > imedia:
				imedia = evento.entregarIntensidadMedia()
		return imedia

	def maximaIntensidadMaxima(self, coleccionEventosP):
		imaxima = 0
		for evento in coleccionEventosP:
			if evento.entregarIntensidadMaxima() > imaxima:
				imaxima = evento.entregarIntensidadMaxima()
		return imaxima

	def diasMes(self, fechaP):
		dias = ["-", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		mes = int(fechaP.split("-")[1])
		ano = int(fechaP.split("-")[0])
		if mes == 2:
			if( ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
				#Bisiesto
				return 29
		return dias[mes]

	def febreroBisiesto(self, anoP):
		if( anoP % 4 == 0 and anoP % 100 != 0 or anoP % 400 == 0):
			#Ano Bisiesto
			return 29
		else:
			return 28




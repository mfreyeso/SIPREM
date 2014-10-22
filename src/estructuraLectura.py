import jornada as jor
import evento 
import categoria as cat
import registro as rg
import csv
import datetime


class estructuraLectura(object):
	def __init__(self, posicionPrecipitacionP, tiempoDifEventosP):
		super(estructuraLectura, self).__init__()
		self.posicionPrecipitacion = posicionPrecipitacionP
		self.tiempoDifEventos = int(tiempoDifEventosP)
		self.coleccionEventos = []
		self.estructuraKernel = []
		"""Vectores para la administracion de la estructura y datos del archivo a leer"""
		self.etiquetaVariables = []
		self.jornadaEventos = []
		self.categoriaEventos = []
		self.ocurrenciaCategoriaEventos = []
		self.ocurrenciaJornadaEventos = []

	"""Metodos de acceso a los atributos del archivo  a leer"""

	def entregarOcurrenciaCategoriaEventos(self):
		return self.ocurrenciaCategoriaEventos

	def entregarOcurrenciaJornadaEventos(self):
		return self.ocurrenciaJornadaEventos

	def entregarTiempoDifEventos(self):
		return self.tiempoDifEventos

	def entregarColeccionEventos(self):
		return self.coleccionEventos

	def entregarEstructuraKernel(self):
		return self.estructuraKernel

	def entregarEtiquetaVariables(self):
		return self.etiquetaVariables

	def entregarJornadaEventos(self):
		return self.jornadaEventos

	def entregarCategoriaEventos(self):
		return self.categoriaEventos

	def entregarPosicionPrecipitacion(self):
		return self.posicionPrecipitacion


	"""Metodos modificadores de los atributos de la clase"""

	def modificarTiempoDifEventos(self, tiempoDifEventosP):
		self.tiempoDifEventos = tiempoDifEventosP

	def modificarEtiquetaVariables(self, etiquetaVariablesP):
		self.etiquetaVariables = etiquetaVariablesP

	def modificarCategoriaEventos(self, categoriasP):
		self.categoriaEventos = categoriasP
		for i in range(len(categoriasP)): self.entregarOcurrenciaCategoriaEventos().append(0)

	def modificarJornadaEventos(self, jornadasP):
		self.jornadaEventos = jornadasP
		for i in range(len(jornadasP)): self.entregarOcurrenciaJornadaEventos().append(0)


	"""Metodo que inicializa las jornadas y las categorias por defecto de los archivos de configuraciones"""
	def inicializarMetricas(self, jornadaEventosP, categoriaEventosP):
		self.modificarJornadaEventos(jornadaEventosP)
		self.modificarCategoriaEventos(categoriaEventosP)	

	def definirCategoriaEvento(self, intensidadMediaP):
		intensidadMediaEvento = intensidadMediaP
		categoriasEvento = self.entregarCategoriaEventos()
		for i in range(len(categoriasEvento)):
			if intensidadMediaEvento <= categoriasEvento[i].entregarMagnitud():
				self.entregarOcurrenciaCategoriaEventos()[i]+=1
				return categoriasEvento[i].entregarEtiqueta()


	def definirJornadaEvento(self, horaInicioP):
		horaInicioEvento = horaInicioP
		jornadasEvento = self.entregarJornadaEventos()
		for i in range(len(jornadasEvento)):
			if horaInicioEvento >= jornadasEvento[i].entregarHoraInicio() and horaInicioEvento < jornadasEvento[i].entregarHoraFin():
				self.entregarOcurrenciaJornadaEventos()[i]+=1
				return jornadasEvento[i].entregarEtiquetaJornada()

	def leerArchivo(self, archivoDatosP):
		respuesta = False
		reader = csv.reader(archivoDatosP, dialect=csv.excel_tab)
		banderaCabecera = 0
		precipitacionUbicacion = self.entregarPosicionPrecipitacion() - 1

		for registro in reader:
			if banderaCabecera == 0:
				if registro[0].split()[0].lower() == "fecha":
					print "la encontre"
					cabecera = registro
					self.modificarEtiquetaVariables(cabecera)
					banderaCabecera = 1
			else:
				if (not self.validarContenido(registro[2]))  and (not self.validarContenido(registro[3])):
					fechaFormateada = registro[0].split("-")
					horaFormateada = registro[1].split(":")
					try:
						precipitacion = float(registro[precipitacionUbicacion])
					except Exception:
						precipitacion = "-"			

					dia = int(fechaFormateada[2])
					mes = int(fechaFormateada[1])
					ano = int(fechaFormateada[0])
					hora = int(horaFormateada[0])
					minuto = int(horaFormateada[1])

					fecha = datetime.date(ano, mes, dia)
					hora = datetime.time(hora, minuto, 0)

					nuevoRegistro = rg.registro(fecha, hora, precipitacion)
					self.entregarEstructuraKernel().append(nuevoRegistro)
		respuesta =True
		return respuesta	


	def validarContenido(self, contenidoP):
		listaContenidosInvalidos = ["-", " ", "*"]
		if contenidoP in listaContenidosInvalidos:
			return True
		else:
			return False
			
	def identificadorEventos(self):
		unidadDiferencia = (self.entregarTiempoDifEventos() / 5) -1
		kernelRegistros = self.entregarEstructuraKernel()
		i=0
		while i < len(kernelRegistros):
			cDiferencia = 0
			posFinal = 0
			posFinalTemp = 0
		
			if kernelRegistros[i].entregarPrecipitacion() > 0.00 and (not self.validarContenido(kernelRegistros[i].entregarPrecipitacion())):
				begin = i
				for j in range(begin, len(kernelRegistros)):
					if kernelRegistros[j].entregarPrecipitacion() > 0.00 and (not self.validarContenido(kernelRegistros[i].entregarPrecipitacion())):
						cDiferencia = 0
						posFinalTemp = j
					else:
						if cDiferencia == unidadDiferencia:
							posFinal = posFinalTemp
							self.creadorEventos(i, posFinal)
							i=j
							break
						else:
							cDiferencia+=1				
			else:
				i+=1
				

	"""Metodo encargado de crear eventos de precipitacion a partir de la posicion inicial y
	final de los registros que representa un evento, devuelve una respuesta booleana del proceso"""					
	def creadorEventos(self, posInicialP, posFinalP):
		respuesta = False
		registrosKernel = self.entregarEstructuraKernel()
		numeroRegistros = (posFinalP - posInicialP) + 1
		vectorMagnitudes = []
		magnitudEvento = 0
		maximaMagnitud = 0		
		posicionMaximo = 0

		for i in range(posInicialP, (posFinalP + 1)):
			if self.validarContenido(registrosKernel[i].entregarPrecipitacion()):
				vectorMagnitudes.append(0)
			else:
				vectorMagnitudes.append(registrosKernel[i].entregarPrecipitacion())
			try:
				if vectorMagnitudes[len(vectorMagnitudes) - 1] > maximaMagnitud:
					maximaMagnitud = registrosKernel[i].entregarPrecipitacion()
					posicionMaximo = i
				magnitudEvento += registrosKernel[i].entregarPrecipitacion()
			except TypeError:
				magnitudEvento += 0	

		registroInicioEvento = registrosKernel[posInicialP]
		registroFinEvento = registrosKernel[posFinalP + 1]
		fechaEvento = registroInicioEvento.entregarFecha()
		horaInicioEvento = registroInicioEvento.entregarHora()
		horaFinEvento = registroFinEvento.entregarHora()

		horaInicioEventoEntero = int(horaInicioEvento.hour)
		horaFinEventoEntero = int(horaFinEvento.hour)

		duracionEvento = float(numeroRegistros * 5)
		intensidadMedia = round(magnitudEvento /(duracionEvento/60), 1)

		if self.validarContenido(registrosKernel[posicionMaximo-1].entregarPrecipitacion()):
			intensidadMaxima = "*"		
		else:
			intensidadMaxima = maximaMagnitud * 12

		"""Definiendo categoria y jornada para el evento"""

		categoriaEvento = self.definirCategoriaEvento(intensidadMedia)
		jornadaEvento = self.definirJornadaEvento(horaInicioEventoEntero)

		"""Observacion ::: Si el evento transcurre en dos dias distintos"""
		parametroObservacion = "La precipitacion termino en el dia siguiente: "
		observaciones = " "
		if horaFinEventoEntero < horaInicioEventoEntero:
			finEvento = str(registroFinEvento.entregarFecha()) +" "+ str(registroFinEvento.entregarHora())
			observaciones = parametroObservacion + finEvento

		"""Caso : Intensidad Maxima no determinada"""
		if self.validarContenido(intensidadMaxima):
			observaciones = observaciones + "La magnitud del evento es incompleta para determinar la intensidad maxima."
		
		#Creando instancia de un nuevo evento
		nuevoEvento = evento.evento(fechaEvento, horaInicioEvento, horaFinEvento, magnitudEvento, duracionEvento, intensidadMedia, intensidadMaxima, categoriaEvento, jornadaEvento, observaciones, vectorMagnitudes)
		nuevoEvento.calcularTiempoNeto()
		self.adicionarEventoColeccion(nuevoEvento)
				
	def adicionarEventoColeccion(self, eventoP):
		self.entregarColeccionEventos().append(eventoP)







		

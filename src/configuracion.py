import macaron
import models
import jornada as jor
import categoria as cat



class ConfiguracionMother(object):
	"""docstring for Configuracion"""
	def __init__(self):
		super(ConfiguracionMother, self).__init__()
		self.listaJornadas = []
		self.listaCategorias = []
		self.tiempoDiferencia = 0
		self.ubicacionVarPrecipitacion = 0
		self.usuarioActivo = None

	"""Metodos getter y setter de atributos"""

	def entregarJornadas(self):
		return self.listaJornadas

	def entregarCategorias(self):
		return self.listaCategorias

	def entregarTiempoDiferencia(self):
		return self.tiempoDiferencia

	def entregarUbicacionVarP(self):
		return self.ubicacionVarPrecipitacion

	def modificarJornadas(self, jornadasP):
		self.listaJornadas = jornadasP

	def modificarCategorias(self, categoriasP):
		self.listaCategorias =categoriasP

	def modificarTiempoDiferencia(self, tiempoDifP):
		self.tiempoDiferencia = tiempoDifP

	def modificarUbicacionVarP(self, posicionP):
		self.ubicacionVarPrecipitacion = posicionP

	"""Entrega las configuraciones actualizadas"""
	def actualizarConfiguracion(self):
		configuraciones = [self.obtenerConfiguraciones(), self.obtenerCategorias(), self.obtenerJornadas()]
		return configuraciones
	"""Metodos de manipulacion de datos sobre la Base de Datos"""

	def adicionarJornadabd(self, etiquetaJornada, horaInicioP, horaFinP):
		response = False
		try:
			macaron.macaronage("siprem.db")
			#consultar si existe una jornada con hora de inicios semejante antes de adicionarla
			jornadasRelacionadas = models.Jornada.select("hinicio=?", [horaInicioP])
			if jornadasRelacionadas.count() == 0:
				models.Jornada.create(nombre=etiquetaJornada, horainicio=horaInicioP, horafin=horaFinP)
				macaron.bake()
				response = True
			return response
		except Exception, e:
			print e
			return response

	def adicionarCategoriabd(self, etiquetaCategoria, metrica):
		response = False
		try:
			macaron.macaronage("siprem.db")
			#Consultar si existe una metrica igual antes de adicionarla
			metricasRelacionadas = models.Categoria.select("metrica=?", [metrica])
			if metricasRelacionadas.count() == 0:
				nuevaCategoria = models.Categoria.create(etiqueta=etiquetaCategoria, metrica=float(metrica))
				macaron.bake()
				response = True
			return response
		except Exception, e:
			print e
			return response		

	def adicionarUsuario(self, nombreP, pApellidoP, sApellidoP, telefonoP, emailP, identificacionP, idTipoUsuarioP):
		response = False
		try:
			if self.buscarUsuario(identificacionP) != None:
				return response
			else:
				tipousuarioSet = models.TipoUsuario.select("tipo=?", [idTipoUsuarioP])
				tipoO = tipousuarioSet[0]
				tipoO.tipousuario.append(
					nombre=nombreP,
					primerapellido=pApellidoP,
					segundoapellido=sApellidoP,
					telefono=telefonoP,
					email=emailP,
					docidentificacion=identificacion,
					idtipou=tipoO.pk)
				response = True
				return response
		except Exception, e:
			print e
			return False		

	def obtenerConfiguraciones(self):
		macaron.macaronage("siprem.db")
		configuraciones = models.Configuracion.all()
		return configuraciones

	def obtenerCategorias(self):
		return self.entregarCategorias()

	def obtenerJornadas(self):
		return self.entregarJornadas()
	
	def buscarUsuario(self, identificacionP):
		busquedaUsuario = models.Usuario.select("name=?", [identificacionP])
		if busquedaUsuario.count():
			usuario = busquedaUsuario[0]
			return usuario

	def adicionarConfiguracion(self, idUsuarioP, nombreConfP, tDiferenciaP, ubicacionPrecipitacionP):
		response = False
		macaron.macaronage("siprem.db")
		"""response = False
		tipoUsuario = usuario.tipousuario
		if tipousuario == 1:
			models.Configuracion.create(
				nombre=nombreConfP,
				tiempodiferencia = tDiferenciaP,
				ubicacionprecip = ubicacionPrecipitacionP,
				idusuario=idUsuarioP)
			response = True
			return response
		else:
			return response"""
		try:
			models.Configuracion.create(
				nombre=nombreConfP,
				tiempodiferencia = tDiferenciaP,
				ubicacionprecip = ubicacionPrecipitacionP,
				idusuario=idUsuarioP)
			macaron.bake()	
			response = True
			return response
		except Exception, e:
			print e
			macaron.bake()
			return response
		

	def adicionarCategoriaConfiguracion(self, idCategoriaP, idConfiguracionP):
		try:
			models.ConfCategoria.create(
				idconf=idConfiguracionP,
				idcategoria=idCategoriaP
				)
			return True
		except Exception, e:
			print e
			return False

	def adicionarJornadaEvento(self, idJornadaP, idConfiguracionP):
		try:
			models.ConfJornada.create(
				idconf=idConfiguracionP,
				idJornada=idJornadaP
				)
			return True
		except Exception, e:
			print e
			return False

	def cargarConfiguracion(self, opcionCarga, identificacionP):
		if opcionCarga == 0:
			identificacionDefecto = 1
			return self.cargarConfiguracionIdentificacion(identificacionDefecto)
		else:
			return self.cargarConfiguracionIdentificacion(identificacionP)

	def cargarConfiguracionIdentificacion(self, identificacionP):
		response =False
		try:
			jornadas =[]
			categorias =[]
			configuracionRelacionada = models.Configuracion.get(identificacionP)
			setConfJornadas = models.ConfJornada.select("configuracion_id=?", [identificacionP])
			for i, o in enumerate(setConfJornadas):
				jornadaOb = models.Jornada.get(o.jornada_id)
				jornadas.append(jornadaOb)
			jornadas.sort()
			setConfCategorias = models.ConfCategoria.select("configuracion_id=?", [identificacionP])
			for i, o in enumerate(setConfCategorias):
				categoriaOb = models.Categoria.get(o.categoria_id)
				categorias.append(categoriaOb)
			categorias.sort()
			self.preparacionFinalConfiguracion(categorias, jornadas)
			tiempoDif = configuracionRelacionada.tiempodiferencia
			ubcPrecipitacion = configuracionRelacionada.ubicacionprecip
			self.modificarTiempoDiferencia(tiempoDif)
			self.modificarUbicacionVarP(ubcPrecipitacion)
			response = True
			return response
		except Exception, e:
			print e
			return response

	def preparacionFinalConfiguracion(self, categoriasP, jornadasP):
		for jorn in jornadasP:
			etiqueta = jorn.nombre
			horaInicio = jorn.horainicio
			horaFin = jorn.horafin 
			objJornada = jor.jornada(etiqueta, horaInicio, horaFin)
			self.entregarJornadas().append(objJornada)

		for catg in categoriasP:
			etiqueta = catg.etiqueta
			metrica = catg.metrica
			objCategoria = cat.categoria(etiqueta, metrica)
			self.entregarCategorias().append(objCategoria)

	def cargarEstaciones(self):
		macaron.macaronage("siprem.db")
		estaciones= models.Estacion.all()
		return estaciones
			

	
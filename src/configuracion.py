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

	def obtenerConfiguraciones(self):
		macaron.macaronage("siprem.db")
		configuraciones = models.Configuracion.all()
		return configuraciones

	def obtenerCategorias(self):
		return self.entregarCategorias()

	def obtenerJornadas(self):
		return self.entregarJornadas()

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

			usuarioActivo = models.Usuario.get(identificacionP)
			configuracionAsociada = usuarioActivo.configuracionesu.select("predt=?", [1])[0]
			pkConfiguracion = configuracionAsociada.pk

			setConfJornadas = models.ConfJornada.select("configuracion_id=?", [pkConfiguracion])
			for i, o in enumerate(setConfJornadas):
				jornadaOb = models.Jornada.get(o.jornada_id)
				jornadas.append(jornadaOb)
			jornadas.sort()
			
			setConfCategorias = models.ConfCategoria.select("configuracion_id=?", [pkConfiguracion])
			for i, o in enumerate(setConfCategorias):
				categoriaOb = models.Categoria.get(o.categoria_id)
				categorias.append(categoriaOb)
			categorias.sort()
			
			self.preparacionFinalConfiguracion(categorias, jornadas)

			tiempoDif = configuracionAsociada.tiempodiferencia
			ubcPrecipitacion = configuracionAsociada.ubicacionprecip
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

	"""Metodos de manipulacion de datos sobre la Base de Datos"""

	def adicionarJornadabd(self, etiquetaJornada, horaInicioP, horaFinP):
		response = False
		try:
			macaron.macaronage("siprem.db")
			#Se valida que no haya en la bd una jornada con hora de inicio semejante
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
			#Se valida que no exista en la bd una categoria con metrica semejante
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
			#Se valida que no exista en la bd el usuario
			if self.buscarUsuario(identificacionP) != None:
				return response
			else:
				tipousuarioSet = models.TipoUsuario.select("tipo=?", [idTipoUsuarioP])
				tipoObject = tipousuarioSet[0]
				tipoObject.tipousuario.append(
					nombre=nombreP,
					primerapellido=pApellidoP,
					segundoapellido=sApellidoP,
					telefono=telefonoP,
					email=emailP,
					docidentificacion=identificacion,
					idtipou=tipoObject.pk)
				response = True
				return response
		except Exception, e:
			print e
			return False	
	
	def buscarUsuario(self, identificacionP):
		busquedaUsuario = models.Usuario.select("name=?", [identificacionP])
		if busquedaUsuario.count():
			usuario = busquedaUsuario[0]
			return usuario
		else:
			return None

	def adicionarConfiguracion(self, idUsuarioP, nombreConfP, tDiferenciaP, ubicacionPrecipitacionP):
		response = False
		try:
			models.Configuracion.create(
				nombre=nombreConfP,
				tiempodiferencia = tDiferenciaP,
				ubicacionprecip = ubicacionPrecipitacionP,
				usuario_id=idUsuarioP,
				predt = 0)
			macaron.bake()	
			response = True
			return response
		except Exception, e:
			print e
			macaron.bake()
			return response
		

	def adicionarCategoriaConfiguracion(self, idCategoriaP, idConfiguracionP):
		try:
			macaron.macaronage("siprem.db")
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
			macaron.macaronage("siprem.db")
			models.ConfJornada.create(
				idconf=idConfiguracionP,
				idJornada=idJornadaP
				)
			return True
		except Exception, e:
			print e
			return False

	def obtenerConfiguracion(self, idConfiguracionP):
		try:
			macaron.macaronage("siprem.db")
			configuracion = models.Configuracion.get(idConfiguracionP)
			return configuracion  
		except Exception, e:
			raise e

	

	
			

	
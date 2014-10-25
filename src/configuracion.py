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

	def entregarUsuarioActivo(self):
		return self.usuarioActivo

	def modificarJornadas(self, jornadasP):
		self.listaJornadas = jornadasP

	def modificarCategorias(self, categoriasP):
		self.listaCategorias =categoriasP

	def modificarTiempoDiferencia(self, tiempoDifP):
		self.tiempoDiferencia = tiempoDifP

	def modificarUbicacionVarP(self, posicionP):
		self.ubicacionVarPrecipitacion = posicionP

	def modificarUsuarioActivo(self, usuarioP):
		self.usuarioActivo = usuarioP

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

			#usuarioActivo = models.Usuario.get(identificacionP)
			#configuracionAsociada = usuarioActivo.configuracionesu.select("predt=?", [1])[0]
			#pkConfiguracion = configuracionAsociada.pk
			
			configuracionAsociada = models.Configuracion.get(identificacionP)
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

	#Transformacion de las categorias y jornadas obtenidas como DAO a las clases originales
	def preparacionFinalConfiguracion(self, categoriasP, jornadasP):
		for jorn in jornadasP:
			etiqueta = jorn.nombre
			horaInicio = jorn.horainicio
			horaFin = jorn.horafin
			identificacion = jorn.id 
			objJornada = jor.jornada(etiqueta, horaInicio, horaFin, identificacion)
			self.entregarJornadas().append(objJornada)

		for catg in categoriasP:
			etiqueta = catg.etiqueta
			metrica = catg.metrica
			identificacion = catg.id
			objCategoria = cat.categoria(etiqueta, metrica, identificacion)
			self.entregarCategorias().append(objCategoria)

	"""Metodos de manipulacion de datos sobre la Base de Datos"""

	def adicionarJornadabd(self, etiquetaJornada, horaInicioP, horaFinP):
		response = False
		try:
			macaron.macaronage("siprem.db")
			#Se valida que no haya en la bd una jornada con hora de inicio semejante
			jornadasRelacionadas = models.Jornada.select("horainicio=?", [horaInicioP])
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
			return response	
	
	def buscarUsuario(self, identificacionP):
		try:
			macaron.macaronage("siprem.db")
			usuario = models.Usuario.get(identificacionP)
			if usuario != None:
				return usuario
			else:
				return None
		except Exception, e:
			print e
			return None

	def validarUsuario(self, usernameP, passwordP):
		try:
			macaron.macaronage("siprem.db")
			busquedaUsuario = models.Usuario.select(" usuariosistema=? and clave=? ", [usernameP,  passwordP])
			if busquedaUsuario.count() > 0:
				usuarioEncontrado = busquedaUsuario[0]
				return usuarioEncontrado
			else:
				return None
		except Exception, e:
			print e
			return None

	def obtenerTipoUsuario(self, idTipoUsuario):
		try:
			macaron.macaronage("siprem.db")
			tipoUsuario = models.TipoUsuario.get(idTipoUsuario)
			return tipoUsuario.tipo
		except Exception, e:
			print e
			return None

	def obtenerTiposUsuario(self):
		try:
			macaron.macaronage("siprem.db")
			tiposUsuarios = models.TipoUsuario.all()
			return tiposUsuarios
		except Exception, e:
			print e
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
			response = False
			models.ConfCategoria.create(
				configuracion_id=idConfiguracionP,
				categoria_id=idCategoriaP
				)
			macaron.bake()
			response = True
		except AttributeError, e:
			print e
			response = True			
		return response

	def adicionarJornadaEvento(self, idJornadaP, idConfiguracionP):
		try:
			response = False
			models.ConfJornada.create(
				configuracion_id=idConfiguracionP,
				jornada_id=idJornadaP
				)
			macaron.bake()
			response = True
		except AttributeError, e:
			print e
			response = True 
		return response

	def obtenerConfiguracion(self, idConfiguracionP):
		try:
			macaron.macaronage("siprem.db")
			configuracion = models.Configuracion.get(idConfiguracionP)
			return configuracion  
		except Exception, e:
			raise e

	def obtenerCategoria(self, idCategoriaP):
		try:
			macaron.macaronage("siprem.db")
			categoriaDao = models.Categoria.get(idCategoriaP)
			etiqueta = categoriaDao.etiqueta
			metrica = categoriaDao.metrica
			identificacion = categoriaDao.id
			categoriaObtenida = cat.categoria(etiqueta, metrica, identificacion)
			return categoriaObtenida
		except Exception, e:
			print e

	def obtenerJornada(self, idJornadaP):
		try:
			macaron.macaronage("siprem.db")
			jornadaDao = models.Jornada.get(idJornadaP)
			etiqueta = jornadaDao.nombre
			horaInicio = jornadaDao.horainicio
			horaFin = jornadaDao.horafin
			identificacion = jornadaDao.id 
			jornadaObtenida = jor.jornada(etiqueta, horaInicio, horaFin, identificacion)
			return jornadaObtenida
		except Exception, e:
			print e

	def editarCategoria(self, idCategoriaP, etiquetaCategoriaP, metricaP):
		try:
			macaron.macaronage("siprem.db")
			categoriaDao = models.Categoria.get(idCategoriaP)
			categoriaDao.etiqueta = etiquetaCategoriaP
			categoriaDao.metrica = metricaP
			categoriaDao.save()
			return True
		except Exception, e:
			print e

	def editarJornada(self, idJornadaP, etiquetaJornadaP, horaInicioP, horaFinP):
		try:
			macaron.macaronage("siprem.db")
			jornadaDao = models.Jornada.get(idJornadaP)
			jornadaDao.nombre = etiquetaJornadaP
			jornadaDao.horainicio = horaInicioP
			jornadaDao.horafin = horaFinP
			jornadaDao.save()
			return True
		except Exception, e:
			print e

	def eliminarCategoria(self, idCategoriaP):
		try:
			macaron.macaronage("siprem.db")
			categoriaDao = models.Categoria.get(idCategoriaP)
			categoriaDao.delete()
			return True
		except Exception, e:
			print e

	def eliminarJornada(self, idJornadaP):
		try:
			macaron.macaronage("siprem.db")
			jornadaDao = models.Jornada.get(idJornadaP)
			jornadaDao.delete()
			return True
		except Exception, e:
			print e

	def obtenerCategoriasExistentes(self):
		try:
			categoriasEncontradas = []
			macaron.macaronage("siprem.db")
			categoriasExistentes = models.Categoria.all()
			for categoria in categoriasExistentes:
				etiqueta = categoria.etiqueta
				metrica = categoria.metrica
				identificacion = categoria.id
				objCategoria = cat.categoria(etiqueta, metrica, identificacion)
				categoriasEncontradas.append(objCategoria)
			return categoriasEncontradas
		except Exception, e:
			print e

	def obtenerJornadasExistentes(self):
		try:
			jornadasEncontradas = []
			macaron.macaronage("siprem.db")
			jornadasExistentes = models.Jornada.all()
			for jornada in jornadasExistentes:
				etiqueta = jornada.nombre
				horaInicio = jornada.horainicio
				horaFin = jornada.horafin
				identificacion = jornada.id 
				objJornada = jor.jornada(etiqueta, horaInicio, horaFin, identificacion)
				jornadasEncontradas.append(objJornada)
			return jornadasEncontradas
		except Exception, e:
			print e

	def obtenerCategoriasConfiguracion(self, idConfiguracionP):
		try:
			macaron.macaronage("siprem.db")
			categorias = []
			confcategorias = models.ConfCategoria.select("configuracion_id=?", [idConfiguracionP])
			for i, o in enumerate(confcategorias):
				categoriaOb = models.Categoria.get(o.categoria_id)
				categorias.append(categoriaOb)
			categorias.sort()
		except Exception, e:
			print e
		return categorias

	def obtenerJornadasConfiguracion(self, idConfiguracionP):
		try:
			macaron.macaronage("siprem.db")
			jornadas = []
			confjornadas = models.ConfJornada.select("configuracion_id=?", [idConfiguracionP])
			for i, o in enumerate(confjornadas):
				jornadaOb = models.Jornada.get(o.jornada_id)
				jornadas.append(jornadaOb)
			jornadas.sort()			
		except Exception, e:
			print e
		return jornadas



	
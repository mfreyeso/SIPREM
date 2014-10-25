#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import *
import os, inspect, json
import jsonparsers as jsp

import estructuraLectura as esl

#import resumen as rev
import resumenred as rev
import acumulado as acu
import categoria as cat
import jornada as jor
import mother as mot
import configuracion
import indicador as indx

import reportePrueba as rpb
import reporteVertical as rv

#Se importan las clases de acceso a datos
import daoevento as dtev
import daoregistro as dtreg
import daoestacion as des

import macaron

#Controlador de MacaronPlugin
install(macaron.MacaronPlugin("siprem.db"))

#Interfaz Mother
mother = mot.Mother()
fileRead = None

#Creacion de objeto de Configuracion del Sistema
configuracionP = configuracion.ConfiguracionMother()

#Inicializacion de Configuracion por Defecto
configuracionP.cargarConfiguracion(0, 0)

#Objeto de Acceso a Datos de Evento,Registro y Estacion
dtaevento = dtev.EventoDao()
dtaregistro = dtreg.RegistroDao()
dtaestacion = des.EstacionDao()

#Objeto Acumulador
objAcumulador = acu.acumulado()
#Objeto Indicador
objIndicador = indx.indicadorA(25)


@route('/')
def indexApp():
	return template('indexCambios.tpl')

@route('/index')
def indexAppTwo():
	return template('indexCambios.tpl')

@route('/menuinicio')
def inicio():
	return template('menuinicio.tpl')


"""---------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------ROUTES LECTURA ARCHIVO----------------------------------------------------------------------"""


@route('/cargarArchivo', method='POST')
def loadFile():
	fileRead = request.files.get('fileIn').file
	estacionSeleccionada = int(request.forms.estacionselect)
	nombreEstacion = dtaestacion.obtenerNombreEstacion(estacionSeleccionada)
	estructuraMain = esl.estructuraLectura(int(configuracionP.entregarUbicacionVarP()), int(configuracionP.entregarTiempoDiferencia()))
	estructuraMain.inicializarMetricas(configuracionP.entregarJornadas(), configuracionP.entregarCategorias())
	if estructuraMain.leerArchivo(fileRead):
		estructuraMain.identificadorEventos()
		listEventos = estructuraMain.entregarColeccionEventos()
		listRegistros = estructuraMain.entregarEstructuraKernel()
		registrosValidos = dtaregistro.validarRegistros(listRegistros, estacionSeleccionada)
		if len(registrosValidos) != 0:
			dtaregistro.almacenarRegistros(registrosValidos, estacionSeleccionada)
			eventosValidos = dtaevento.validarEventos(listEventos, estacionSeleccionada)
			if eventosValidos != None:
				dtaevento.almacenarEventos(eventosValidos, estacionSeleccionada)
				cadenaParametrizadaP = nombreEstacion + " "+ str(listRegistros[0].entregarFecha()) + " " + str(listRegistros[(len(listRegistros)-1)].entregarFecha())
				return template('eventos.tpl', coleccionEventos=eventosValidos, cadenaParametrizada=cadenaParametrizadaP)
			else:
				return template('errorCargaArchivo.tpl', opcion=1)
		else:
			return template('errorCargaArchivo.tpl', opcion=1)
	else:		
		return template('errorCargaArchivo.tpl', opcion=2)

@route('/archivoPlano')
def cargaArchivoPlano():
	vectorEstaciones = dtaestacion.cargarEstaciones()
	return template('cargaArchivo.tpl', estaciones=vectorEstaciones)


"""---------------------------------------------------------------------------------------------------------------------------"""



"""---------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------ROUTES EVENTOS--------------------------------------------------------------------------------"""

@route('/cargarEventos', method='GET')
def loadEvents():
	try:
		estructuraMain = mother.entregarEstructuraMain()
		objetosEventos = estructuraMain.entregarColeccionEventos()
		return template('eventos.tpl', coleccionEventos=objetosEventos)
	except Exception:
		vectorEstaciones = dtaestacion.cargarEstaciones()
		return template('buscarEventosv2.tpl', estaciones=vectorEstaciones)

@route('/eventos', method='GET')
def eventos():
	vectorEstaciones = dtaestacion.cargarEstaciones()
	return template('buscarEventosv2.tpl', estaciones=vectorEstaciones)

@route('/eventosFiltro', method='GET')
def eventos():
	vectorEstaciones = dtaestacion.cargarEstaciones()
	vectorJornadas = configuracionP.entregarJornadas() 
	vectorCategorias = configuracionP.entregarCategorias()
	return template('buscarEventosAvanzado.tpl', estaciones=vectorEstaciones, jornadas=vectorJornadas, categorias=vectorCategorias)

@route('/buscarEventos', method='POST')
def buscarEventos():
	idEstacion = int(request.forms.estacionselect)
	fechaInicial = str(request.forms.fechainicial)
	fechaFinal = str(request.forms.fechafinal)
	nombreEstacion = dtaestacion.obtenerNombreEstacion(idEstacion)
	cadenaParametrizadaP = str(nombreEstacion) + " " + fechaInicial + " - " + fechaFinal
	eventosEncontrados = dtaevento.buscarEventos(fechaInicial, fechaFinal, idEstacion)
	return template('eventos.tpl', coleccionEventos=eventosEncontrados, cadenaParametrizada=cadenaParametrizadaP)


@route('/buscarEventosAvanzado', method='POST')
def buscarEventos():
	idEstacion = int(request.forms.estacionselect)
	fechaInicial = str(request.forms.fechainicial)
	fechaFinal = str(request.forms.fechafinal)
	jornada = str(request.forms.jornada)
	categoria = str(request.forms.categoria)
	nombreEstacion = str(dtaestacion.obtenerNombreEstacion(idEstacion))
	cadenaParametrizadaP = nombreEstacion + " " + fechaInicial + " - " + fechaFinal
	eventosEncontrados = dtaevento.buscarEventosAvanzado(fechaInicial, fechaFinal, idEstacion, categoria, jornada)
	return template('eventos.tpl', coleccionEventos=eventosEncontrados, cadenaParametrizada=cadenaParametrizadaP)


"""REPORTES DE EVENTOS"""

@route('/reporteEventos', method='POST')
def crearReporteEventos():
	data = request.json
	dirArchivo = str(data['dir'])
	nombreArchivo = str(data['namefile'])
	operador = configuracionP.entregarUsuarioActivo().nombre + " " + configuracionP.entregarUsuarioActivo().primerapellido 
	try:
		nuevoReporte = rv.ReporteVertical(nombreArchivo, dirArchivo, operador)
		nuevoReporte.crearReporteVertical()		
		return json.dumps({'efect': "El reporte fue creado con exito."})
	except Exception, e:
		print e
		print "Error de Ind"
		return json.dumps({'efect': "Existieron problemas en la construcción del reporte, intente de nuevo."})	


"""---------------------------------------------------------------------------------------------------------------------------"""



"""---------------------------------------------------------------------------------------------------------------------------"""
"""ROUTES DEL MODULO DE RESUMEN"""

@route('/crearResumen', method='POST')
def crearResumen():
	objresumen = rev.resumen()
	vJornadas = configuracionP.obtenerJornadas()
	vCategorias = configuracionP.obtenerCategorias()

	#Se crea esta variable vacia si no es utiliza el caso para renderizar resultados
	dias = 0

	estacionSeleccionada = int(request.forms.estacionselect)
	daoEstacion = des.EstacionDao()
	nombreEstacionP = str(daoEstacion.obtenerEstacion(int(estacionSeleccionada)).nombre)

	opcionSeleccionada = int(request.forms.opcionselect)
	if opcionSeleccionada ==1:
		parametro = str(request.forms.fecha)
		cadenaParametrizadaP = "Diario " + parametro
	elif opcionSeleccionada == 2:
		parametro = str(request.forms.mes)
		deriv = parametro.split("-")
		dias = objresumen.diasMes(parametro)
		cadenaParametrizadaP = objAcumulador.entregarMes(int(deriv[1])) + " " + deriv[0]
	elif opcionSeleccionada == 3:
		parametro = str(request.forms.ano)
		cadenaParametrizadaP = "Año " + parametro
	elif opcionSeleccionada == 4:
		parametro = ["-", int(request.forms.ano)]
		cadenaParametrizadaP = "Semestral " + str(parametro[1])
	elif opcionSeleccionada == 5:
		#Trimestre Bimodal
		parametro = ["-", int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestral Bimodal " + str(parametro[1])
	elif opcionSeleccionada == 6:
		#Trimestre Estandar
		parametro = ["-", int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestral Estandar " + str(parametro[1])
	elif opcionSeleccionada == 7:
		parametro = [int(request.forms.anoi), int(request.forms.anof)]
		cadenaParametrizadaP = "Multianual " + str(request.forms.anoi) + " - " + str(request.forms.anof)
	else:
		parametro = [str(request.forms.fechainicial), str(request.forms.fechafinal)]
		cadenaParametrizadaP = "Personalizada: Fecha Inicial: " + str(request.forms.fechainicial) + " Fecha Final: " + str(request.forms.fechafinal)
	resumenObtenido = objresumen.generarResumenEventos(opcionSeleccionada, parametro, estacionSeleccionada, vJornadas, vCategorias)
	return template('resultadoresumen.tpl', opcionrs = opcionSeleccionada, resultados = resumenObtenido, cadenaParametrizada = cadenaParametrizadaP, categorias=vCategorias, jornadas = vJornadas, nombreEstacion = nombreEstacionP, diasMes = dias, vAnual = parametro)

@route('/topcresumen')
def vistaResumenOpciones():
	vectorEstaciones = dtaestacion.cargarEstaciones()
	return template('presumeneventos.tpl', estaciones=vectorEstaciones)


"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


"""--------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------ROUTES DE CONFIGURACION DE APP-------------------------------------------------"""



@route('/static/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static/')

"""--------------------------------------------------------------------------------------------------------------------------------"""





"""---------------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------ROUTES DEL MODULO DE INDICADOR AX--------------------------------------------------"""

@route('/tsindicador')
def vistaIndicador():
	vectorEstaciones = dtaestacion.cargarEstaciones()
	return template('sindicadorx.tpl', valorIndicador =objIndicador.entregarIndicadorParametrizado(), estaciones=vectorEstaciones)

@route('/calcularIndicador', method="POST")
def calcularIndicador():
	valIndicadorP = objIndicador.entregarIndicadorParametrizado()
	estacionSeleccionada = int(request.forms.estacionselect)
	nombreEstacion = dtaestacion.obtenerNombreEstacion(estacionSeleccionada)
	opcionSeleccionada = int(request.forms.opcionselect)
	if opcionSeleccionada ==1:
		parametro = str(request.forms.ano)
		cadenaParametrizadaP = "Año " + parametro
	elif opcionSeleccionada == 2:
		parametro = [int(request.forms.semestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Semestre: " + objAcumulador.entregarSemestre(parametro[0]) + " " + str(parametro[1])
	elif opcionSeleccionada == 3:
		#Trimestre Bimodal
		parametro = [int(request.forms.trimestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestre: " + objAcumulador.entregarTrimestre(1, parametro[0]) + " " + str(parametro[1])
	else:
		#Trimestre Estandar
		parametro = [int(request.forms.trimestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestre: " + objAcumulador.entregarTrimestre(0, parametro[0]) + " " + str(parametro[1])
	indicadorObtenido = objIndicador.calcularIndicador(opcionSeleccionada, parametro, estacionSeleccionada)
	cadenaParametrizadaP = nombreEstacion + " " + cadenaParametrizadaP
	return template('indicadorObtenido.tpl', indicador = indicadorObtenido, cadenaParametrizada = cadenaParametrizadaP, opcion=opcionSeleccionada, periodos = parametro, valIndicador = valIndicadorP)

@route('/configurarindicador')
def configurarIndicador():
	return template('formindicador.tpl', valindicador = objIndicador.entregarIndicadorParametrizado())

@route('/transformarIndicador', method="POST")
def transformarIndicador():
	data = request.json
	valorIndicador = int(data['valindicador'])
	objIndicador.modificarIndicadorParametrizado(valorIndicador)
	if valorIndicador == objIndicador.entregarIndicadorParametrizado():
		return json.dumps({'efect': "El indicador fue modificado con exito."})
	else:
		return json.dumps({'efect': "El indicador no fue modificado, intente de nuevo."})


"""---------------------------------------------------------------------------------------------------------------------------"""


"""---------------------------------------------------------------------------------------------------------------------------"""

"""ROUTES DEL MODULO DE ACUMULADOS"""

@route('/tacumulado')
def vistaAcumulado():
	vectorEstaciones = dtaestacion.cargarEstaciones()
	return template('sacumuladod.tpl', estaciones=vectorEstaciones)

@route('/tacumuladoeventos')
def vistaAcumulado():
	vectorEstaciones = dtaestacion.cargarEstaciones()
	return template('sacumuladodeventos.tpl', estaciones=vectorEstaciones)

@route('/buscarAcumulado', method='POST')
def busquedaAcumulado():
	estacionSeleccionada = int(request.forms.estacionselect)
	nombreEstacion = str(dtaestacion.obtenerNombreEstacion(estacionSeleccionada))
	opcionSeleccionada = int(request.forms.opcionselect)
	if opcionSeleccionada ==1:
		parametro = str(request.forms.ano)
		cadenaParametrizadaP = "Año " + parametro
	elif opcionSeleccionada == 2:
		parametro = [int(request.forms.semestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Semestre " + objAcumulador.entregarSemestre(parametro[0]) + " " + str(parametro[1])
	elif opcionSeleccionada == 3:
		#Trimestre Bimodal
		parametro = [int(request.forms.trimestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestre " + objAcumulador.entregarTrimestre(1, parametro[0]) + " " + str(parametro[1])
	elif opcionSeleccionada == 4:
		#Trimestre Estandar
		parametro = [int(request.forms.trimestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestre " + objAcumulador.entregarTrimestre(0, parametro[0]) + " " + str(parametro[1])
	else:
		#Multianual
		parametro = [int(request.forms.anoinicial), int(request.forms.anofinal)]
		cadenaParametrizadaP = "Personalizada: " + str(request.forms.anoinicial) + " " + str(request.forms.anofinal)
	acumuladoObtenido = dtaregistro.busquedaParametrizada(opcionSeleccionada, parametro, estacionSeleccionada)
	cadenaParametrizadaP = nombreEstacion + " " + cadenaParametrizadaP
	return template('acumuladoObtenido.tpl', acumulado=acumuladoObtenido, cadenaParametrizada=cadenaParametrizadaP, opcion=opcionSeleccionada, periodos = parametro)


@route('/buscarAcumuladoEventos', method='POST')
def busquedaAcumulado():
	estacionSeleccionada = int(request.forms.estacionselect)
	nombreEstacion = str(dtaestacion.obtenerNombreEstacion(estacionSeleccionada))
	opcionSeleccionada = int(request.forms.opcionselect)
	if opcionSeleccionada ==1:
		parametro = str(request.forms.fecha)
		cadenaParametrizadaP = "Diario " + parametro
	elif opcionSeleccionada == 2:
		parametro = str(request.forms.mes)
		deriv = parametro.split("-")
		cadenaParametrizadaP = objAcumulador.entregarMes(int(deriv[1])) + " " +deriv[0]
	elif opcionSeleccionada == 3:
		parametro = str(request.forms.ano)
		cadenaParametrizadaP = "Año " + parametro
	elif opcionSeleccionada == 4:
		parametro = [int(request.forms.semestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Semestre " + objAcumulador.entregarSemestre(parametro[0]) + " " + str(parametro[1])
	elif opcionSeleccionada == 5:
		#Trimestre Bimodal
		parametro = [int(request.forms.trimestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestre " + objAcumulador.entregarTrimestre(1, parametro[0]) + " " + str(parametro[1])
	elif opcionSeleccionada == 6:
		#Trimestre Estandar
		parametro = [int(request.forms.trimestre), int(request.forms.ano)]
		cadenaParametrizadaP = "Trimestre " + objAcumulador.entregarTrimestre(0, parametro[0]) + " " + str(parametro[1])
	else:
		parametro = [str(request.forms.fechainicial), str(request.forms.fechafinal)]
		cadenaParametrizadaP = "Personalizada: Fecha Inicial: " + str(request.forms.fechainicial) + " Fecha Final: " + str(request.forms.fechafinal)
	eventosEncontrados = dtaevento.busquedaParametrizada(opcionSeleccionada, parametro, estacionSeleccionada)
	resultadosObtenidos = objAcumulador.calculoGeneralAcumuladoEventos(eventosEncontrados)
	cadenaParametrizadaP = nombreEstacion + " " + cadenaParametrizadaP
	return template('acumuladoObtenidoEventos.tpl', resultados=resultadosObtenidos, cadenaParametrizada=cadenaParametrizadaP)

"""-----------------------------------------------------------------------------------------------------------------------------------------------------"""


"""---------------------------------------------------------------------------------------------------------------------------"""

"""ROUTES DEL MODULO DE ESTACIONES"""

@route('/estaciones')
def estacionesSIPREM():
	estacionesObtenidas = dtaestacion.obtenerEstaciones()
	return template('estaciones.tpl', estaciones = estacionesObtenidas)


@route('/crearEstacion', method="POST")
def crearEstacion():
	data = request.json
	nombreEstacion = str(data['nombre'])
	ubicacionEstacion = str(data['ubicacion'])
	fechaEstacion = str(data['fecha'])
	if dtaestacion.crearEstacion(nombreEstacion, ubicacionEstacion, fechaEstacion):
		return json.dumps({'efect':"La estación fue creada con exito."})
	else:
		return json.dumps({'efect':"La estación no pudo ser creada en el sistema."})

@route('/modificarEstacion', method="POST")
def modificarEstacion():
	data = request.json
	nombreEstacion = str(data['nombre'])
	ubicacionEstacion = str(data['ubicacion'])
	fechaEstacion = str(data['fecha'])
	ideEstacion = str(data['ide'])
	estacionD = dtaestacion.obtenerEstacion(ideEstacion)
	if dtaestacion.modificarEstacion(estacionD, nombreEstacion, ubicacionEstacion, fechaEstacion):
		return json.dumps({'efect':"La estación fue actualizada con exito."})
	else:
		return json.dumps({'efect':"La estación no pudo ser actualizada."})

@route('/desactivarEstacion', method="POST")
def desactivarEstacion():
	data = request.json
	ideEstacion = str(data['ide'])
	if dtaestacion.desactivarEstacion(ideEstacion):
		return json.dumps({'efect':"La estación fue desactivada con exito."})
	else:
		return json.dumps({'efect':"La estación no pudo ser desactivada."})

@route('/activarEstacion', method="POST")
def activarEstacion():
	data = request.json
	ideEstacion = str(data['ide'])
	if dtaestacion.activarEstacion(ideEstacion):
		return json.dumps({'efect':"La estación fue reactivada con exito."})
	else:
		return json.dumps({'efect':"La estación no pudo ser reactivada."})

@route('/estacionesDesactivadas', method="GET")
def estacionesDesactivadas():
	estacionesDesactivadas = dtaestacion.obtenerEstacionesDesactivadas()
	if estacionesDesactivadas != None:
		resultado = {}
		coleccionEstaciones=[]
		for i in range(0, estacionesDesactivadas.count()):
			dicestacion =  {'nombre': str(estacionesDesactivadas[i].nombre), 'ide': str(estacionesDesactivadas[i].id)}
			coleccionEstaciones.append(dicestacion)
		resultado['coleccion']=coleccionEstaciones
		resultado['efect']="1"
		return json.dumps(resultado)
	else:
		return json.dumps({'efect':"0"})

@route('/obtenerEstacion', method="POST")
def obtenerEstacion():
	data = request.json
	idEstacion = int(data['estacion'])
	estacionEncontrada = dtaestacion.obtenerEstacion(idEstacion)
	if estacionEncontrada != None:
		return json.dumps({'efect': '1', 'estacion': {'nombre': str(estacionEncontrada.nombre), 'ubicacion': str(estacionEncontrada.ubicacion), 'fecha': str(estacionEncontrada.fechaoperacion)}})
	else:
		return json.dumps({'efect': '0'})

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""ROUTES DEL MODULO DE CONFIGURACION"""

@route('/tconfiguracion')
def vistaConfiguracion():
	setConfiguraciones = configuracionP.obtenerConfiguraciones()
	setJornadas = configuracionP.obtenerJornadasExistentes()
	setCategorias = configuracionP.obtenerCategoriasExistentes()
	return template('configuracion.tpl', configuraciones=setConfiguraciones, categorias=setCategorias, jornadas=setJornadas)

@route('/tconfiguracionjc')
def vistaConfiguracion():
	setJornadas = configuracionP.obtenerJornadasExistentes()
	setCategorias = configuracionP.obtenerCategoriasExistentes()
	return template('configuracionjorncat.tpl', categorias=setCategorias, jornadas=setJornadas)


@route('/cargarConfiguracion', method="POST")
def cargarConfiguracion():
	data = request.json
	ideConfiguracion = data['ideconf']
	if configuracionP.cargarConfiguracion(1, ideConfiguracion):
		return json.dumps({'efect':"La configuración fue cargada sobre el sistema."})
	else:
		return json.dumps({'efect':"La configuracion no fue cargada en el sistema, Por favor intente de nuevo."})


@route('/crearConfiguracion', method="POST")
def crearConfiguracion():
	data = request.json
	nombreConfiguracion = data['nombre']
	posicionPrecipitacion = int(data['posicion'])
	diferencialTiempo = int(data['diferencial'])
	if configuracionP.adicionarConfiguracion(1, nombreConfiguracion, diferencialTiempo, posicionPrecipitacion):
		return json.dumps({'efect':"La configuración fue creada sobre el sistema."})
	else:
		return json.dumps({'efect':"La configuración no pudo ser creada en el sistema, Intente de Nuevo."})

@route('/obtenerConfiguracion', method="POST")
def obtenerConfiguracion():
	data = request.json
	ideConfiguracion = int(data['ideconf'])
	configuracionObtenida = configuracionP.obtenerConfiguracion(ideConfiguracion)
	categoriasConfiguracion = configuracionP.obtenerCategoriasConfiguracion(ideConfiguracion)
	jornadasConfiguracion =  configuracionP.obtenerJornadasConfiguracion(ideConfiguracion)
	nombreConfiguracion = configuracionObtenida.nombre
	posicionPrecipitacion = configuracionObtenida.ubicacionprecip
	diferencialTiempo = configuracionObtenida.tiempodiferencia

	if configuracionObtenida != None and categoriasConfiguracion != None and jornadasConfiguracion != None:
		resultado = {}
		coleccionCategorias = []
		for categoria in categoriasConfiguracion:
			dicategoria = {'etcategoria': str(categoria.etiqueta) , 'metrica': str(categoria.metrica)}
			coleccionCategorias.append(dicategoria)
		resultado['categorias'] = coleccionCategorias

		coleccionJornadas = []
		for jornada in jornadasConfiguracion:
			dicjornada = {'etjornada': str(jornada.nombre)  , 'hinicio': str(jornada.horainicio) , 'hfin': str(jornada.horafin)}
			coleccionJornadas.append(dicjornada)
		resultado['jornadas'] = coleccionJornadas
		resultado['efect'] = 1
		resultado['configuracion'] = {'nombre': str(nombreConfiguracion), 'posicion': str(posicionPrecipitacion), 'diferencial': str(diferencialTiempo)}
		return json.dumps(resultado)
	else:
		return json.dumps({'efect': '0'})

@route('/adicionarCategoria', method="POST")
def adicionarCategoria():
	data = request.json
	identificacionCategoria = int(data['idcat'])
	identificacionConfiguracion = int(data['idconf'])
	if configuracionP.adicionarCategoriaConfiguracion(identificacionCategoria, identificacionConfiguracion):
		return json.dumps({'efect':"La categoria fue añadida a la configuración."})
	else:
		return json.dumps({'efect':"La categoria no fue añadida, asegurese que la configuración no incluye ya esta categoria."})

@route('/adicionarJornada', method="POST")
def adicionarJornada():
	data = request.json
	identificacionJornada = int(data['idjor'])
	identificacionConfiguracion = int(data['idconf'])
	if configuracionP.adicionarJornadaEvento(identificacionJornada, identificacionConfiguracion) == True:
		return json.dumps({'efect':"La jornada fue añadida a la configuración."})
	else:
		return json.dumps({'efect':"La jornada no fue añadida, asegurese que la configuración no incluye ya esta jornada."})

@route('/obtenerCategoria', method="POST")
def obtenerCategoria():
	data = request.json
	idCategoria = int(data['idcat'])
	categoriaObtenida = configuracionP.obtenerCategoria(idCategoria)
	if categoriaObtenida != None:
		return json.dumps({'efect': '1', 'categoria': {'etiqueta': str(categoriaObtenida.entregarEtiqueta()), 'metrica': str(categoriaObtenida.entregarMagnitud())}})
	else:
		return json.dumps({'efect': '0'})

@route('/obtenerJornada', method="POST")
def obtenerJornada():
	data = request.json
	idJornada = int(data['idjor'])
	jornadaObtenida = configuracionP.obtenerJornada(idJornada)
	if jornadaObtenida != None:
		return json.dumps({'efect': '1', 'jornada' :{'etiqueta': str(jornadaObtenida.entregarEtiquetaJornada()), 'hinicio': str(jornadaObtenida.entregarHoraInicio()), 'hfin': str(jornadaObtenida.entregarHoraFin())}})
	else:
		return json.dumps({'efect': '0'})

@route('/crearCategoria', method="POST")
def crearCategoria():
	data = request.json
	etiquetaCategoria = str(data['etiqueta'])
	metricaCategoria = float(data['metrica'])
	if configuracionP.adicionarCategoriabd(etiquetaCategoria, metricaCategoria):
		return json.dumps({'efect':"La categoria fue creada en el sistema."})
	else:
		return json.dumps({'efect':"La categoria no pudo ser creada en el sistema, Intente de Nuevo."})


@route('/crearJornada', method="POST")
def crearJornada():
	data = request.json
	etiquetaJornada = str(data['etiqueta'])
	horaInicio = int(data['hinicio'])
	horaFin = int(data['hfin'])
	if configuracionP.adicionarJornadabd(etiquetaJornada, horaInicio, horaFin):
		return json.dumps({'efect':"La jornada fue creada en el sistema."})
	else:
		return json.dumps({'efect':"La jornada no pudo ser creada en el sistema, Intente de Nuevo."})

@route('/eliminarCategoria', method="POST")
def eliminarCategoria():
	data = request.json
	idCategoria = int(data['idcat'])
	if configuracionP.eliminarCategoria(idCategoria):
		return json.dumps({'efect':"La categoria fue eliminada del sistema."})
	else:
		return json.dumps({'efect':"La categoria no fue eliminada del sistema, Intente de Nuevo."})

@route('/eliminarJornada', method="POST")
def eliminarJornada():
	data = request.json
	idJornada = int(data['idjor'])
	if configuracionP.eliminarJornada(idJornada):
		return json.dumps({'efect':"La jornada fue eliminada del sistema."})
	else:
		return json.dumps({'efect':"La jornada no fue eliminada del sistema, Intente de Nuevo."})

@route('/editarCategoria', method='POST')
def editarCategoria():
	data = request.json
	idCategoria = int(data['idcat'])
	etiquetaCategoria = str(data['etiqueta'])
	metricaCategoria = float(data['metrica'])
	if configuracionP.editarCategoria(idCategoria, etiquetaCategoria, metricaCategoria):
		return json.dumps({'efect':"La categoria fue modificada con exito."})
	else:
		return json.dumps({'efect':"La categoria no fue modificada, Intente de Nuevo."})

@route('/editarJornada', method="POST")
def editarJornada():
	data = request.json
	idJornada = int(data['idjor'])
	etiquetaJornada = str(data['etiqueta'])
	horaInicio = int(data['hinicio'])
	horaFin = int(data['hfin'])
	if configuracionP.editarJornada(idJornada, etiquetaJornada, horaInicio, horaFin):
		return json.dumps({'efect':"La jornada fue modificada con exito."})
	else:
		return json.dumps({'efect':"La categoria no fue modificada, Intente de Nuevo."})

"""---------------------------------------------------------------------------------------------------------------------------------"""


"""---------------------------------------------------------------------------------------------------------------------------------"""
""".....................................ROUTES DE USUARIOS.........................................................................."""


@route('/loginuser', method="POST")
def loginSIPREM():
	data = request.json
	username = str(data['nameuser'])
	password = str(data['passuser'])
	if configuracionP.validarUsuario(username, password) != None:
		usuarioEncontrado = configuracionP.validarUsuario(username, password)
		configuracionP.modificarUsuarioActivo(usuarioEncontrado)
		return json.dumps({'efect': "1"})
	else:
		return json.dumps({'efect': "0"})

@route('/usuariodetalles')
def detallesUsuario():
	usuarioActivo = configuracionP.entregarUsuarioActivo()
	nombreUsuario = usuarioActivo.nombre
	primerApellido = usuarioActivo.primerapellido
	segundoApellido = usuarioActivo.segundoapellido
	telefono = usuarioActivo.telefono
	email = usuarioActivo.email
	docidentificacion = usuarioActivo.docidentificacion
	rol = configuracionP.obtenerTipoUsuario(usuarioActivo.tipousuario_id)
	usuariosistema = usuarioActivo.usuariosistema
	rolesEncontrados = configuracionP.obtenerTiposUsuario()
	if rol == "Administrador":
		rolId = 1
	else:
		rolId = 0
	return template('detallesUsuario.tpl', nombre=nombreUsuario, papellido=primerApellido, sapellido=segundoApellido, mail=email, rolusuario=rol,
	 identificacion=docidentificacion, accuser=usuariosistema, rolid=rolId, roles=rolesEncontrados)



@route('/teditusuario')
def vistaEditarUsuario():
	usuarioActivo = configuracionP.entregarUsuarioActivo()
	nombreUsuario = usuarioActivo.nombre
	primerApellido = usuarioActivo.primerapellido
	segundoApellido = usuarioActivo.segundoapellido
	telefono = usuarioActivo.telefono
	email = usuarioActivo.email
	docidentificacion = usuarioActivo.docidentificacion
	
	roles = configuracionP.obtenerTipoUsuario(usuarioActivo.tipousuario_id)
	
	usuariosistema = usuarioActivo.usuariosistema
	claveaccess = usuarioActivo.clave

	return template('editarUsuario.tpl', nombre=nombreUsuario, papellido=primerApellido, sapellido=segundoApellido, mail=email, rolusuario=roles,
	 identificacion=docidentificacion, accuser=usuariosistema, rolesdisponibles=roles, accpassword=claveaccess)








"""---------------------------------------------------------------------------------------------------------------------------------"""


run(host='localhost', port=8080)

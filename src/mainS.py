# -*- coding: utf-8 -*-
from bottle import *

import estructuraLectura as esl
#import resumen as rev
import resumenred as rev
import acumulado as acu
import categoria as cat
import jornada as jor
import mother as mot
import configuracion

#Se importan las clases de acceso a datos
import daoevento as dtev
import daoregistro as dtreg

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

#Objeto de Acceso a Datos de Evento
dtaevento = dtev.EventoDao()
dtaregistro = dtreg.RegistroDao()

#Objeto Acumulador
objAcumulador = acu.acumulado()

@route('/')
def indexApp():
	return template('indexCambios.tpl')
	#return template('index.tpl')

@route('/index')
def indexAppTwo():
	return template('indexCambios.tpl')
	#return template('index.tpl')

@route('/cargarArchivo', method='POST')
def loadFile():
	fileRead = request.files.get('fileIn').file
	estacionSeleccionada = int(request.forms.estacionselect)
	estructuraMain = esl.estructuraLectura(int(configuracionP.entregarUbicacionVarP()), int(configuracionP.entregarTiempoDiferencia()))
	estructuraMain.inicializarMetricas(configuracionP.entregarJornadas(), configuracionP.entregarCategorias())
	if estructuraMain.leerArchivo(fileRead):
		estructuraMain.identificadorEventos()
		listEventos = estructuraMain.entregarColeccionEventos()
		listRegistros = estructuraMain.entregarEstructuraKernel()
		mother.modificarEstructuraMain(estructuraMain)
		dtaevento.almacenarEventos(listEventos, estacionSeleccionada)
		dtaregistro.almacenarRegistros(listRegistros, estacionSeleccionada)
		return template('eventos.tpl', coleccionEventos=listEventos)
	else:
		return template('errorCargaArchivo.tpl')

@route('/cargarEventos', method='GET')
def loadEvents():
	try:
		estructuraMain = mother.entregarEstructuraMain()
		objetosEventos = estructuraMain.entregarColeccionEventos()
		return template('eventos.tpl', coleccionEventos=objetosEventos)
	except Exception:
		vectorEstaciones = configuracionP.cargarEstaciones()
		return template('buscarEventosv2.tpl', estaciones=vectorEstaciones)

@route('/archivoPlano')
def cargaArchivoPlano():
	vectorEstaciones = configuracionP.cargarEstaciones()
	return template('cargaArchivo.tpl', estaciones=vectorEstaciones)

@route('/eventos', method='GET')
def eventos():
	vectorEstaciones = configuracionP.cargarEstaciones()
	return template('buscarEventosv2.tpl', estaciones=vectorEstaciones)

@route('/eventosFiltro', method='GET')
def eventos():
	vectorEstaciones = configuracionP.cargarEstaciones()
	vectorJornadas = configuracionP.entregarJornadas() 
	vectorCategorias = configuracionP.entregarCategorias()
	return template('buscarEventosAvanzado.tpl', estaciones=vectorEstaciones, jornadas=vectorJornadas, categorias=vectorCategorias)

@route('/buscarEventos', method='POST')
def buscarEventos():
	idEstacion = int(request.forms.estacionselect)
	fechaInicial = str(request.forms.fechainicial)
	fechaFinal = str(request.forms.fechafinal)
	eventosEncontrados = dtaevento.buscarEventos(fechaInicial, fechaFinal, idEstacion)
	return template('eventos.tpl', coleccionEventos=eventosEncontrados)


@route('/buscarEventosAvanzado', method='POST')
def buscarEventos():
	idEstacion = int(request.forms.estacionselect)
	fechaInicial = str(request.forms.fechainicial)
	fechaFinal = str(request.forms.fechafinal)
	jornada = str(request.forms.jornada)
	categoria = str(request.forms.categoria)
	eventosEncontrados = dtaevento.buscarEventosAvanzado(fechaInicial, fechaFinal, idEstacion, categoria, jornada)
	return template('eventos.tpl', coleccionEventos=eventosEncontrados)



@route('/tresumen')
def resumen():
	estructuraMain = mother.entregarEstructuraMain()
	objetosEventos = estructuraMain.entregarColeccionEventos()
	listaOcurrenciaJornadas = estructuraMain.entregarOcurrenciaJornadaEventos()
	listaOcurrenciaCategorias = estructuraMain.entregarOcurrenciaCategoriaEventos()
	objetosCategoria = estructuraMain.entregarCategoriaEventos()
	objetosJornada = estructuraMain.entregarJornadaEventos()
	objResumenP = rev.resumen(objetosEventos, objetosJornada, objetosCategoria)
	mother.modificarResumen(objResumenP)
	if not objResumenP.validarCompletitudResumen():
		return template('resumen.tpl', objResumen=objResumenP, objMain=estructuraMain)
	else:
		return template('opcionResumen.tpl')

@route('/resumenParametrizado', method='POST')
def resumenParametrizado():
	objResumenP = mother.entregarResumen()
	resumenSeleccionado = int(request.forms.opcionResumen)
	if resumenSeleccionado == 1:
		response = objResumenP.resumenMensualAnual()
		return template('resumenParametrizadoAnual.tpl', resource=response)

	elif resumenSeleccionado == 2:
		response = objResumenP.resumenSemestral()
		return template('resumenParametrizadoSemestral.tpl', resource=response)

	elif resumenSeleccionado == 3:
		response = objResumenP.resumenTrimestral()
		return template('resumenParametrizadoTrimestral.tpl', resource=response)

	elif resumenSeleccionado == 4:
		response = objResumenP.resumenTrimestralBimodal()
		return template('resumenParametrizadoTrimestralBimodal.tpl', resource=response)

@route('/acumuladoParametrizado', method='POST')
def prepareAcumulate():	
	seleccion = int(request.forms.opcionselect)
	estructuraMain = mother.entregarEstructuraMain()
	objetosEventos = estructuraMain.entregarColeccionEventos()
	objAcumulador = acu.acumulado(objetosEventos)
	if seleccion == 1:
		opSelec = "Diario"
		diaSeleccionado = int(request.forms.dia)
		mesSeleccionado = int(request.forms.mes)
		anoSeleccionado = int(request.forms.ano)		
		cadenaParametrizadaP = str(diaSeleccionado) + " " + objAcumulador.entregarMes(mesSeleccionado -1) + " " + str(anoSeleccionado) 
		resultadoP = objAcumulador.acumuladoParametrizado(seleccion, diaSeleccionado, mesSeleccionado, anoSeleccionado, 0, 0)
	elif seleccion == 2:
		mesSeleccionado = int(request.forms.mes)
		anoSeleccionado = int(request.forms.ano)
		opSelec = "Mensual"
		cadenaParametrizadaP = objAcumulador.entregarMes(mesSeleccionado -1) + " " + str(anoSeleccionado)
		resultadoP = objAcumulador.acumuladoParametrizado(seleccion, 0, mesSeleccionado, anoSeleccionado, 0, 0)
	elif seleccion == 3:
		anoSeleccionado = int(request.forms.ano)
		opSelec = "Anual"
		cadenaParametrizadaP = str(anoSeleccionado)
		resultadoP = objAcumulador.acumuladoParametrizado(seleccion, 0, 0, anoSeleccionado, 0, 0)
	elif seleccion == 4:
		opSelec = "Semestral"
		semestreSeleccionado = int(request.forms.semestre)
		cadenaParametrizadaP = objAcumulador.entregarSemestre(semestreSeleccionado -1)
		resultadoP = objAcumulador.acumuladoParametrizado(seleccion, 0, 0, 0, semestreSeleccionado, 0)

	else:
		opSelec = "Trimestral"
		trimestreSeleccionado = int(request.forms.trimestre)
		cadenaParametrizadaP = objAcumulador.entregarTrimestre(trimestreSeleccionado - 1)
		resultadoP = objAcumulador.acumuladoParametrizado(seleccion, 0, 0, 0, 0, trimestreSeleccionado)		
	return template('resacumulado.tpl', resultado=resultadoP, opseleccion=opSelec, cadenaParametrizada=cadenaParametrizadaP)


@route('/buscarAcumulado', method='POST')
def busquedaAcumulado():
	estacionSeleccionada = int(request.forms.estacionselect)
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
		cadenaParametrizadaP = "Personalizada: " + str(request.forms.fechainicial) + " " + str(request.forms.fechafinal)
		
	registrosEncontrados = dtaregistro.busquedaParametrizada(opcionSeleccionada, parametro, estacionSeleccionada)
	acumuladoObtenido = objAcumulador.calcularAcumuladoMagnitudRegistros(registrosEncontrados)
	return template('acumuladoObtenido.tpl', acumulado=acumuladoObtenido, cadenaParametrizada=cadenaParametrizadaP)


@route('/buscarAcumuladoEventos', method='POST')
def busquedaAcumulado():
	estacionSeleccionada = int(request.forms.estacionselect)
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
	return template('acumuladoObtenidoEventos.tpl', resultados=resultadosObtenidos, cadenaParametrizada=cadenaParametrizadaP)

@route('/crearResumen', method='POST')
def crearResumen():
	objresumen = rev.resumen()
	vJornadas = configuracionP.obtenerJornadas()
	vCategorias = configuracionP.obtenerCategorias()

	estacionSeleccionada = int(request.forms.estacionselect)
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
		cadenaParametrizadaP = "Multianual " + str(request.forms.anoi) + "-" + str(request.forms.anof)
	else:
		parametro = [str(request.forms.fechainicial), str(request.forms.fechafinal)]
		cadenaParametrizadaP = "Personalizada: Fecha Inicial: " + str(request.forms.fechainicial) + " Fecha Final: " + str(request.forms.fechafinal)
	resumenObtenido = objresumen.generarResumenEventos(opcionSeleccionada, parametro, estacionSeleccionada, vJornadas, vCategorias)
	print resumenObtenido


@route('/tacumulado')
def vistaAcumulado():
	vectorEstaciones = configuracionP.cargarEstaciones()
	return template('sacumuladod.tpl', estaciones=vectorEstaciones)

@route('/tacumuladoeventos')
def vistaAcumulado():
	vectorEstaciones = configuracionP.cargarEstaciones()
	return template('sacumuladodeventos.tpl', estaciones=vectorEstaciones)

@route('/topcresumen')
def vistaResumenOpciones():
	vectorEstaciones = configuracionP.cargarEstaciones()
	return template('presumeneventos.tpl', estaciones=vectorEstaciones)

@route('/tconfiguracion')
def vistaConfiguracion():
	setConfiguraciones = configuracionP.obtenerConfiguraciones()
	setJornadas = configuracionP.obtenerJornadas()
	setCategorias = configuracionP.obtenerCategorias()
	return template('configuracion.tpl', configuraciones=setConfiguraciones, categorias=setCategorias, jornadas=setJornadas)

@route('/ajustarConfiguracion/<idconfiguracion>', method="GET")
def cargarConfiguracion(idconfiguracion):
	if configuracionP.cargarConfiguracion(1, idconfiguracion):
		setConfiguraciones = configuracionP.obtenerConfiguraciones()
		setJornadas = configuracionP.obtenerJornadas()
		setCategorias = configuracionP.obtenerCategorias()
		return template('index.tpl')
	else:
		print "Existieron Problemas"


@route('/crearconfiguracion', method="POST")
def adicionarConfiguracion():
	nombreConfiguracion = request.forms.nombreC
	tiempoDifEventos = int(request.forms.dfprec) / 5
	posicionPrecipitacion = int(request.forms.psprec)
	if configuracionP.adicionarConfiguracion(1, nombreConfiguracion, tiempoDifEventos, posicionPrecipitacion):
		print "Adicione la Configuracion"
		actualizacion = configuracionP.actualizarConfiguracion()
		return template('configuracion.tpl', configuraciones=actualizacion[0], categorias=actualizacion[1], jornadas=actualizacion[2])
	else:
		print "Problema en insercion"

@route('/crearCategoria', method="POST")
def adicionarCategoria():
	nombreCategoria = request.forms.nombrecat
	metricaCategoria = float(request.forms.metricac)
	if configuracionP.adicionarCategoriabd(nombreCategoria, metricaCategoria):
		actualizacion = configuracionP.actualizarConfiguracion()
		return template('configuracion.tpl', configuraciones=actualizacion[0], categorias=actualizacion[1], jornadas=actualizacion[2])
	else:
		print "Existieron problemas"

@route('/crearJornada', method="POST")
def adicionarJornada():
	nombreJornada = request.forms.nombrejor
	hInicio = int(request.forms.hinicio)
	hFin = int(request.forms.hfin)
	print hInicio, hFin
	if configuracionP.adicionarJornadabd(nombreJornada, hInicio, hFin):
		actualizacion = configuracionP.actualizarConfiguracion()
		return template('configuracion.tpl', configuraciones=actualizacion[0], categorias=actualizacion[1], jornadas=actualizacion[2])
	else:
		print "Existieron problemas"


@route('/tcarga')
def vistaAcumulado():
	vectorEstaciones = configuracionP.cargarEstaciones()
	return template('cargaArchivo.tpl', estaciones=vectorEstaciones)

@route('/static/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/reporteResumen', method="POST")
def construirReporteResumen():
	estructuraMain = mother.entregarEstructuraMain()
	objetosEventos = estructuraMain.entregarColeccionEventos()
	objetosCategoria = estructuraMain.entregarCategoriaEventos()
	objetosJornada = estructuraMain.entregarJornadaEventos()
	objResumenP = rev.resumen(objetosEventos, objetosCategoria, objetosJornada)
	datosNecesarios = [estructuraMain, objResumenP]
	reporteResumen = rpa.MakerResumen(datosNecesarios)
	if reporteResumen.makerReporte():
		"Revisar el Directorio"
	else:
		"Falla"

@route('/estaciones')
def estacionesSIPREM():
	return template('estaciones.tpl')


run(host='localhost', port=8080)

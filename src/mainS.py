from bottle import *

import estructuraLectura as esl
import resumen as rev
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


@route('/')
def indexApp():
	return template('index.tpl')

@route('/index')
def indexAppTwo():
	return template('index.tpl')

@route('/cargarArchivoS', method='POST')
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
		return template('buscarEventos.tpl', estaciones=vectorEstaciones)

@route('/buscarEventos', method='POST')
def buscarEventos():
	opcionSeleccionada = int(request.forms.opcionselect)
	if opcionSeleccionada == 1:
		ano = int(request.forms.anoUno)
		mes = int(request.forms.mesUno)
		dia = int(request.forms.dia)
	elif opcionSeleccionada == 2:
		ano = int(request.forms.anoDos)
		mes = int(request.forms.mesDos)
	else:
		ano = int(request.forms.anoTres)
	persistencia.buscarEventos(opcionSeleccionada, dia, mes, ano)

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

@route('/tacumulado')
def vistaAcumulado():
	return template('sacumuladod.tpl')

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
	nombreConfiguracion = request.forms.nombreconf
	tiempoDifEventos = int(request.forms.tiempodif) / 5
	posicionPrecipitacion = int(request.forms.pospre)
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


run(host='localhost', port=8080)

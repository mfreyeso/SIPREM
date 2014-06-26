#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4



class MakerResumen(object):
	"""docstring for MakerAcumulados"""
	def __init__(self, datosTablaP):
		super(MakerResumen, self).__init__()
		self.objectStory = []
		self.datosTabla = datosTablaP
		self.hojaEstilos = getSampleStyleSheet()

	def entregarStory(self):
		return self.objectStory

	def modificadorStory(self, nuevoStoryP):
		self.objectStory.append(nuevoStoryP)

	def entregarDatosReporte(self):
		return self.datosTabla

	def entregarHojaEstilos(self):
		return self.hojaEstilos

	def preparador(self):
		self.documento = SimpleDocTemplate(str(self.entregarCadenaDetalle()))

	def entregarDocumentoTemplate(self):
		return self.documento

	def makerReporte(self):
		try:
			docum = self.entregarDocumentoTemplate()
			self.makerCabecera()
			self.formatearDatos()
			storyP = self.entregarStory()
			docum.build(storyP)
			return True
		except Exception, e:
			print e
			return False

	def makerCabecera(self):
		titulo = Paragraph("Instituto de Estudios Ambientales IDEA", self.entregarHojaEstilos()['Heading1'])
		subtitulo = Paragraph("Sistema de Informacion Meteorologíco de Precipitaciones Red de Estaciones Manizales", self.entregarHojaEstilos()['Heading2'])
		resumen = Paragraph("Resumen de Resultados", self.entregarHojaEstilos()['Normal'])

		storyParcial = [titulo, subtitulo, informe, resumen]
		storyParcial.append(Spacer(0, 20))
		self.modificadorStory(storyParcial)

	def makerTablaDatos(self, tCat, tJor, tMax):
		tablaCategoriasFinal = Table(tCat)
		tablaCategoriasFinal.setStyle([('GRID', (0, 0), (-1, -1), 0.2, colors.silver)])
		tablaJornadasFinal = Table(tJor)
		tablaJornadasFinal.setStyle([('GRID', (0, 0), (-1, -1), 0.2, colors.silver)])
		tablaMaximosFinal = Table(tMax)
		tablaMaximosFinal.setStyle([('GRID', (0, 0), (-1, -1), 0.2, colors.silver)])
		subtUno=Paragraph("Numero de Eventos según Categoria", self.entregarHojaEstilos()['Normal'])
		subtDos=Paragraph("Numero de Eventos según Jornada", self.entregarHojaEstilos()['Normal'])
		subtTres = Paragraph("Maximos Obtenidos", self.entregarHojaEstilos()['Normal'])

		storyParcial =[subtUno, Spacer(0, 10), tablaCategoriasFinal, Spacer(0, 20), subtDos, Spacer(0, 10), tablaJornadasFinal, Spacer(0, 20), subtTres, Spacer(0, 10), tablaMaximosFinal, Spacer(0,20)]
		self.modificadorStory(storyParcial)

	def formatearDatos(self):
		#Objetos Estructura Main 0,  Resumen 1
		datosObtenidos = self.entregarDatosReporte()
		estructuraMain = datosObtenidos[0]
		objResumen = datosObtenidos[1]
		maximos = objResumen.entregarMaximos()
		etiquetasMaximos =["Duración (min.)", "Magnitud(mm)", "Intensidad Media (mm/h)", "Intensidad Maxima (mm/h)"]
		vCategorias = objMain.entregarCategoriaEventos()
		vJornadas = objMain.entregarJornadaEventos()
		voCategorias = objMain.entregarOcurrenciaCategoriaEventos()
		voJornadas = objMain.entregarOcurrenciaJornadaEventos()

		#Tabla de Categorias

		tablaCategorias = []
		cabezal = ["Categoria", "Resultado"]
		tablaMaximos.append(cabezal)
		for i in range(0,len(vCategorias)):
			fila = [vCategorias[i], voCategorias[i]]
			tablaCategorias.append(fila)

		#Tabla de Jornadas

		tablaJornadas = []
		cabezal = ["Jornada", "Resultado"]
		tablaMaximos.append(cabezal)
		for i in range(0,len(vJornadas)):
			fila = [vJornadas[i], voJornadas[i]]
			tablaJornadas.append(fila)

		#Tabla de Maximos

		tablaMaximos = []
		cabezal = ["Metrica", "Resultado"]
		tablaMaximos.append(cabezal)
		for i in range(0,len(maximos)):
			fila = [etiquetasMaximos[i], maximos[i]]
			tablaMaximos.append(fila)

		self.makerTablaDatos(tablaCategorias, tablaJornadas, tablaMaximos)





		
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



class MakerAcumulados(object):
	"""docstring for MakerAcumulados"""
	def __init__(self, cadenaInformacionP, tipoAcumuladoP, datosTablaP):
		super(MakerAcumulados, self).__init__()
		self.objectStory = []
		self.cadenaInformacion = cadenaInformacionP
		self.tipoAcumulado = tipoAcumuladoP
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

	def entregarTipoAcumuladoGenerado(self):
		return self.tipoAcumulado

	def entregarCadenaDetalle(self):
		return self.cadenaInformacion

	def preparador(self):
		self.documento = SimpleDocTemplate(str(self.entregarCadenaDetalle()))

	def entregarDocumentoTemplate(self):
		return self.documento

	def makerReporte(self, storyP):
		docum = self.entregarDocumentoTemplate()
		docum.build(storyP)


	def makerCabecera(self):
		titulo = Paragraph("Instituto de Estudios Ambientales IDEA", self.entregarHojaEstilos()['Heading1'])
		subtitulo = Paragraph("Sistema de Informacion Meteorologíco de Precipitaciones Red de Estaciones Manizales", self.entregarHojaEstilos()['Heading2'])
		informe = Paragraph(str(self.definirTipo(self.entregarTipoAcumuladoGenerado())), self.entregarHojaEstilos()['Normal'])
		detalle = Paragraph(str(self.entregarCadenaDetalle()), self.entregarHojaEstilos()['Normal'])

		storyParcial = [titulo, subtitulo, informe, detalle]
		storyParcial.append(Spacer(0, 20))
		self.modificadorStory(storyParcial)

	def definirTipo(self, casoR):
		informe = "Reporte de Acumulados" + str(casoR)
		return informe 

		
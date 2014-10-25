#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, PageTemplate, 
NextPageTemplate, PageBreak, Frame, FrameBreak, Flowable, Paragraph, 
Image, Spacer)
from reportlab.rl_config import defaultPageSize

imagenes = ['static/image/universidad.jpg', 'static/image/alcaldia.png']
operador = "Mario Reyes"

class ReporteVertical(object):
	"""docstring for ReporteVertical"""
	def __init__(self, nombreReporteP, directorioArchivoP, operadorP):
		super(ReporteVertical, self).__init__()
		self.PAGE_HEIGHT = letter[1]
		self.PAGE_WIDTH = letter[0]
		self.story = []
		self.styles = getSampleStyleSheet()
		self.nombreReporte = str(nombreReporteP)
		self.dirArchivo = str(directorioArchivoP)
		self.tipoArchivo = ".pdf"
		global operador
		global imagenes
		operador = str(operadorP)
		imagenes = ['static/image/universidad.jpg', 'static/image/alcaldia.png']

	def inicializarReporte(self, nombreReporteP):
		self.doc = BaseDocTemplate(nombreReporteP, pagesize=letter)

	def contenidoFrame(self):
		self.contenidoFrame = Frame(self.doc.leftMargin, (self.doc.height - self.doc.topMargin), self.doc.width, self.doc.height / 6, showBoundary=1)

	def constructorPaginas(self):
		self.doc.addPageTemplates([PageTemplate(id='reporte', frames=self.contenidoFrame, onPage =encabezado, onPageEnd=piePagina)])

	def crearReporteVertical(self):
		try:
			self.inicializarReporte(os.path.join(self.dirArchivo, self.nombreReporte + self.tipoArchivo))
			self.contenidoFrame()
			self.constructorPaginas()
			self.story.append(Paragraph("El viaje del navegante. Blog de Python", self.styles['Normal']))
			self.doc.build(self.story)
			os.system(os.path.join(self.dirArchivo, self.nombreReporte + self.tipoArchivo))
		except Exception, e:
			print e

def encabezado(canvas,doc):
	canvas.saveState()
	canvas.drawImage(os.path.realpath(imagenes[1]), (inch-32), (letter[1] - 80), 50, 65)
	canvas.drawImage(os.path.realpath(imagenes[0]), (letter[0]-(inch + 20)), (letter[1] - 80), 50, 65)
	canvas.setFont('Helvetica-Bold', 12)
	canvas.drawCentredString((letter[0] / 2.0), letter[1] - 50, "Universidad Nacional de Colombia Sede Manizales")
	canvas.setFont('Helvetica', 11)
	canvas.drawCentredString((letter[0] / 2.0), letter[1] - 60, "Observatorios Ambientales para el Desarrollo Urbano Sostenible en Manizales")
	canvas.setFont('Helvetica', 10)
	canvas.drawCentredString((letter[0] / 2.0), letter[1] - 70, "Contrato Municipio de Manizales/UGR - Universidad Nacional de Colombia")
	canvas.restoreState()

def piePagina(canvas,doc):
	canvas.saveState()
	canvas.setFont('Helvetica',7)
	canvas.drawString(inch, 0.75 * inch, "G.T.A en Ingeniería Hidráulica y Ambiental")
	canvas.drawCentredString((letter[0] / 2.0), 0.75 * inch, "Elaborado por: %s" %operador)
	canvas.drawString(((letter[0] / 6.0) * 4), 0.75 * inch, "Instituto de Estudios Ambientales IDEA")
	canvas.restoreState()
		

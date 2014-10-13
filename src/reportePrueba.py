from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class Reporte(object):
	"""docstring for Reporte"""
	def __init__(self):
		super(Reporte, self).__init__()

	def crearReporte(self):
		c = canvas.Canvas("canvas_draw.pdf", pagesize=letter)
		c.setFont("Helvetica", 18)
		c.line(50,50,50,350)
		c.line(50,50,350,50)
		c.setStrokeColorRGB(1,1,0,0)
		c.setFillColorRGB(0,0.,0,0.5)

		c.roundRect(75,75,275,275,20,stroke=0,fill=1)
		c.setFillColorRGB(0.8,0.,0.2)
		c.circle(205,205,100,stroke=1, fill=1)

		c.setFillColorRGB(0.75,0.75,0)
		c.drawString(125, 80, "Cuadrado")
		c.setFillColorRGB(0,1,0.2)
		c.drawString(155,200, "Circulo")
		c.setFillColorRGB(0,0,0.5)
		c.drawString(150, 375, "Elipse")
		c.showPage()
		c.save()

		
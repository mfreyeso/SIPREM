# -*- coding: utf-8 -*-
import cPickle as pickle
import sqlite3 as lite


class jornada(object):
	def __init__(self, etiquetaJornadaP, horaInicioP, horaFinP):
		super (jornada, self).__init__()
		self.etiquetaJornada = etiquetaJornadaP
		self.horaInicio = horaInicioP
		self.horaFin = horaFinP

	def entregarEtiquetaJornada(self):
		return self.etiquetaJornada

	def entregarHoraInicio(self):
		return self.horaInicio

	def entregarHoraFin(self):
		return self.horaFin

	def modificarEtiquetaJornada(self, etiquetaJornadaP):
		self.etiquetaJornada = etiquetaJornadaP

	def modificarHoraInicio(self, horaInicioP):
		self.horaInicio = horaInicioP

	def modificarHoraFin(self, horaFinP):
		self.horaFin = horaFinP


objetoJornada = jornada("Lluvia", 8, 10)


s = pickle.dumps(objetoJornada, 2)
#print "Este es normal"
#print s

#desformato = pickle.loads(formato)
#print desformato.etiquetaJornada
#suno = lite.Binary(s)
#print "Este es codificado"
#print suno

db = lite.connect("prueba.db")
cursor = db.cursor()
#cursor.execute("INSERT INTO frames VALUES(?);", (lite.Binary(s)))
cursor.execute('''
    insert into frames values (null, ?)''',
    (lite.Binary(s),))
db.commit()
for row in cursor.execute("select * from frames"):
    cadena = str(row[1])
    objectN = pickle.loads(cadena)
    print objectN.horaInicio
cursor.close()
db.close()




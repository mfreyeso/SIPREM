#!/usr/bin/env python
# -*- coding: utf-8 -*-
import macaron

class Estacion(macaron.Model):
	nombre = macaron.CharField(max_length=56, null=True)
	ubicacion = macaron.CharField(max_length=56, null=True)

class Configuracion(macaron.Model):
	tiempodiferencia = macaron.IntegerField()
	ubicacionprecipitacion = macaron.IntegerField()
	nombre = macaron.CharField(max_length=48)

class TipoUsuario(macaron.Model):pass

class Usuario(macaron.Model):
	nombre = macaron.CharField(max_length=32, null=False)
	primerapellido = macaron.CharField(max_length=32, null=False)
	segundoapellido = macaron.CharField(max_length=32, null=False)
	telefono = macaron.CharField(max_length=32, null=True)
	email = macaron.CharField(max_length=48, null=False)
	docidentificacion = macaron.CharField(max_length=18, null=False)
	tipousuario = macaron.ManyToOne(TipoUsuario, related_name="tipousuario")

class Jornada(macaron.Model):
	nombre = macaron.CharField(max_length=32)
	horainicio = macaron.IntegerField(null=True)
	horafin = macaron.IntegerField(null=True)

	def __cmp__(self, other):
		if self.horainicio < other.horainicio:
			rst = -1
		elif self.horainicio > other.horainicio:
			rst = 1
		else:
			rst = 0
		return rst

class Categoria(macaron.Model):
	etiqueta = macaron.CharField(max_length=32)
	metrica = macaron.FloatField(min=0, max=600)

	def __cmp__(self, other):
		if self.metrica < other.metrica:
			rst = -1
		elif self.metrica > other.metrica:
			rst = 1
		else:
			rst = 0
		return rst

class TipoResumen(macaron.Model):
	etiquetaTipoR = macaron.CharField(max_length=48)
	def __str__(self):
		return self.etiquetaTipo

class TipoAcumulado(macaron.Model):
	etiquetaTipoA = macaron.CharField(max_length=48)
	def __str__(self):
		return self.etiquetaTipoA

class Resumen(macaron.Model):
	infoDetalle = macaron.CharField(max_length=64)
	tipoResumen = macaron.ManyToOne(TipoResumen, related_name="clasificacionR")

class Acumulado(macaron.Model):
	infoDetalle = macaron.CharField(max_length=64)
	TipoAcumulado = macaron.ManyToOne(TipoAcumulado, related_name="clasificacionA")

class ConfCategoria(macaron.Model):
	configuracion = macaron.ManyToOne(Configuracion, related_name="configuracionC")
	categoriaC = macaron.ManyToOne(Categoria, related_name="categoriaC")

class ConfJornada(macaron.Model):
	configuracion = macaron.ManyToOne(Configuracion, related_name="configuracionCj")
	jornadaC = macaron.ManyToOne(Jornada, related_name="jornadaC")

class AlmacenSerializado(object):
		"""docstring for AlmacenSerializado"""
		def __init__(self, coleccionP):
			super(AlmacenSerializado, self).__init__()
			self.coleccionEventos = coleccionP

class Cevento(macaron.Model): pass


import macaron

class Estacion(macaron.Model):
	nombre = macaron.CharField(maxlength=56, null=True)
	ubicacion = macaron.CharField(maxlength=56, null=True)

class Usuario(macaron.Model):
	nombre = macaron.CharField(maxlength=32, null=False)
	primerapellido = macaron.CharField(maxlength=32, null=False)
	segundoapellido = macaron.CharField(maxlength=32, null=False)
	telefono = macaron.CharField(maxlength=32, null=True)
	email = macaron.CharField(maxlength=48, null=False)
	configuracion = macaron.ManyToOne(Configuracion, related_name="confusuario")
	docidentificacion = macaron.CharField(maxlength=18, null=False)

class Jornada(macaron.Model):
	nombre = macaron.CharField(maxlength=32)
	horainicio = macaron.IntegerField(null=True)
	horaFin = macaron.IntegerField(null=True)

class Categoria(macaron.Model):
	etiqueta = macaron.CharField(maxlength=32)
	metrica = macaron.FloatField(min=0, max=300)

class Resumen(macaron.Model):
	infoDetalle = macaron.CharField(maxlength=64)
	tipoResumen = macaron.ManyToOne(TipoResumen, related_name="clasificacionR")

class Acumulado(macaron.Model):
	infoDetalle = macaron.CharField(maxlength=64)
	TipoAcumulado = macaron.ManyToOne(TipoAcumulado, related_name="clasificacionA")

class TipoResumen(macaron.Model):
	etiquetaTipoR = macaron.CharField(maxlength=48)
	def __str__(self):
		return self.etiquetaTipo

class TipoAcumulado(macaron.Model):
	etiquetaTipoA = macaron.CharField(maxlength=48)
	def __str__(self):
		return self.etiquetaTipoA

class Configuracion(macaron.Model):pass

class ConfCategoria(macaron.Model):
	configuracion = macaron.ManyToOne(Configuracion, related_name="configuracionC")
	categoria = macaron.ManyToOne(Categoria, related_name="categoriaC")

class ConfJornada(macaron.Model):
	configuracion = macaron.ManyToOne(Configuracion, related_name="configuracionCj")
	jornada = macaron.ManyToOne(Jornada, related_name="jornadaC")

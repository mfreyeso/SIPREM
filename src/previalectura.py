def leerArchivo(self, archivoDatosP):
		respuesta = False
		reader = csv.reader(archivoDatosP, dialect=csv.excel_tab)
		banderaCabecera = 0
		precipitacionUbicacion = self.entregarPosicionPrecipitacion() - 1
		for registro in reader:
			if banderaCabecera == 0:
				cabecera = registro
				self.modificarEtiquetaVariables(cabecera)
				banderaCabecera = 1
			else:

				fechaFormateada = registro[0].split("-")
				horaFormateada = registro[1].split(":")
				try:
					precipitacion = float(registro[precipitacionUbicacion])
				except Exception:
					precipitacion = "-"				

				dia = int(fechaFormateada[2])
				mes = int(fechaFormateada[1])
				ano = int(fechaFormateada[0])
				hora = int(horaFormateada[0])
				minuto = int(horaFormateada[1])

				fecha = datetime.date(ano, mes, dia)
				hora = datetime.time(hora, minuto, 0)

				nuevoRegistro = rg.registro(fecha, hora, precipitacion)
				self.entregarEstructuraKernel().append(nuevoRegistro)
		respuesta =True
		return respuesta
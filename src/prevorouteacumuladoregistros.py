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
		
	acumuladoObtenido = dtaregistro.busquedaParametrizada(opcionSeleccionada, parametro, estacionSeleccionada)
	return template('acumuladoObtenido.tpl', acumulado=acumuladoObtenido, cadenaParametrizada=cadenaParametrizadaP, opcion=opcionSeleccionada)
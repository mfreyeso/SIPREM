/*
Autor:: Mario Reyes Ojeda
*/
 

/* # Validando Formulario
============================================*/
$(document).ready(function(){

	jQuery.validator.addMethod("diariocheck", function(value, element){
		var fechaRegistradaDiaria = new Date(value);
		var vAnoIngresado = fechaRegistradaDiaria.getFullYear();
		if (vAnoIngresado < 2002){
			var errors = {};
			errors[element.name] = "El año de la fecha ingresada no puede ser inferior al 2002";
			this.showErrors(errors);
		}
		else{
			this.hideErrors();
			return true;
		}
	});

	jQuery.validator.addMethod("mescheck", function(value, element){
		var vAnoIngresado = value.split("-")[0];
		if(vAnoIngresado < 2002)
		{
			var errors = {};
			errors[element.name] = "El año de la fecha ingresada no puede ser inferior al 2002";
			this.showErrors(errors);
		}
		else{
			this.hideErrors();
			return true;
		}
	});

	jQuery.validator.addMethod("personalizadocheck", function(value, element)
	{
		var fechaFinal = new Date(value);
		var fechaInicial = new Date(document.getElementById("fechainicial").value);
		var anoFinal = value.split("-")[0];
		var anoInicial = document.getElementById("fechainicial").value.split("-")[0];
		if (fechaInicial > fechaFinal){
			var errors = {};
			errors[element.name] = "La Fecha Inicial no puede ser posterior a la Fecha Final";
			this.showErrors(errors);
		}	
		else if(anoFinal < 2002 || anoInicial < 2002){
			var errors = {};
			errors[element.name] = "La Fecha Inicial y Fecha Final deben corresponder al año 2002 o posteriores";
			this.showErrors(errors);
		}
		else{
			this.hideErrors();
			return true;
		}
	});

	$('#formacueventos').validate({
		errorElement: "span",
		rules: {
			estacionselect:{
				required: true
			},

			opcionselect:{
				required: true
			},
			fecha : "diariocheck",
			mes : "mescheck",
			fechafinal : "personalizadocheck"
		},
		messages:{
			fecha : "El año de la fecha ingresada no puede ser inferior al 2002",
			mes : "El año de la fecha ingresada no puede ser inferior al 2002",
			fechafinal : "La fecha inicial y fecha final deben corresponder al año 2002 o posteriores, la fecha inicial no puede ser posterior a la final"
		},
		highlight: function(element) {
			$(element).closest('.control-group')
			.removeClass('success').addClass('error');
		},
		success: function(element) {
			element
			.closest('.control-group')
			.removeClass('error').addClass('success');
		}
	});
});
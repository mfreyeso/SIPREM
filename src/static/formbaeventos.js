/*
Autor:: Mario Reyes Ojeda
*/
 

/* # Validando Formulario
============================================*/
$(document).ready(function(){

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

	$('#formbaeventos').validate({
		errorElement: "span",
		rules: {
			estacionselect:{
				required: true
			},
			jornada:{
				required: true
			},
			categoria:{
				required: true
			},
			fechafinal : "personalizadocheck"
		},
		messages:{
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
<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">

			<h4>SIPREM es capaz de entregarle a usted los acumulados de las precipitaciones según su necesidad, seleccione el tipo de acumulado que desea conocer y llene los datos necesarios para poder realizar su solicitud.</h4>

			<form role="form" action="/acumuladoParametrizado" method="post" enctype="multipart/form-data">
			   	<div class="form-group">
                    <label for="tipoacumulado">Tipo de Acumulado</label>
	                <select class="form-control" id="opcionselect" name="opcionselect">
	                  <option value="1">Diario</option>
	                  <option value="2">Mensual</option>
	                  <option value="3">Anual</option>
	                  <option value="4">Semestral</option>
	                  <option value="5">Trimestral</option>
	                </select>
	            </div>
	            <button type="button" class="btn btn-primary" valign="middle" id="butT">Preparar</button><br><br>

				<div id="divDinamico">

				<script>
					$("#butT").on("click",
    				function(){
    					var seleccion = $("#opcionselect").val();
    					var intSeleccion = parseInt(seleccion)
    					switch(intSeleccion)
				    	{
				    		case 1:
				    			var inputsDi = "<div class='form-group'>\
				    			<label for='diasel'>Día</label>\
				    			<input class='form-control' value='1' type='number' name='dia' min='1' max='31'></div>\
				    			<div class='form-group'>\
				                	<label for='diasel'>Mes</label>\
				                	<select class='form-control' name='mes'>\
					                  <option value='1'>Enero</option>\
					                  <option value='2'>Febrero</option>\
					                  <option value='3'>Marzo</option>\
					                  <option value='4'>Abril</option>\
					                  <option value='5'>Mayo</option>\
					                  <option value='6'>Junio</option>\
					                  <option value='7'>Julio</option>\
					                  <option value='8'>Agosto</option>\
					                  <option value='9'>Septiembre</option>\
					                  <option value='10'>Octubre</option>\
					                  <option value='11'>Noviembre</option>\
					                  <option value='12'>Diciembre</option>\
					                </select>\
				                </div>\
				                <div class='form-group'>\
				                	<label for='diasel'>Año</label>\
				                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
				                </div><br>";
				                $("#divDinamico").append($(inputsDi));
				    			break;

				    		case 2:
				    			var inputsDi = "<div class='form-group'>\
				                	<label for='diasel'>Mes</label>\
				                	<select class='form-control' name='mes'>\
					                <option value='1'>Enero</option>\
					                <option value='2'>Febrero</option>\
					                <option value='3'>Marzo</option>\
					                <option value='4'>Abril</option>\
					                <option value='5'>Mayo</option>\
					                <option value='6'>Junio</option>\
					                <option value='7'>Julio</option>\
					                <option value='8'>Agosto</option>\
					                <option value='9'>Septiembre</option>\
					                <option value='10'>Octubre</option>\
					                <option value='11'>Noviembre</option>\
					                <option value='12'>Diciembre</option>\
					                </select>\
				                	</div>\
				                	<div class='form-group'>\
				                	<label for='diasel'>Año</label>\
				                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
				                	</div><br>";
				                
				                $("#divDinamico").append($(inputsDi));
				    			break;

				    		case 3:
				    			var inputsDi = "<div class='form-group'>\
				                <label for='diasel'>Año</label>\
				                <input class='form-control' value='2002' type='number' name='ano' min='2002'>\
				                </div><br>";
				                $("#divDinamico").append($(inputsDi));
				    			break;

				    		case 4:
				    			var inputsDi =" <div class='form-group'>\
				                    <label for='tipoacumulado'>Semestre</label>\
					                <select class='form-control' name='semestre'>\
					                  <option value='1'>Enero - Junio</option>\
					                  <option value='2'>Julio - Diciembre</option>\
					                </select>\
					            </div><br>";
				                $("#divDinamico").append($(inputsDi));
				    			break;

				    		case 5:
				    			var inputsDi ="<div class='form-group'>\
				                    <label for='tipoacumulado'>Trimestre</label>\
					                <select class='form-control' name='trimestre'>\
					                <option value='1'>Diciembre - Febrero</option>\
					                <option value='2'>Marzo - Mayo</option>\
					                <option value='3'>Junio - Agosto</option>\
					                <option value='2'>Septiembre - Noviembre</option>\
					                </select>\
					            </div><br>";
				                $("#divDinamico").append($(inputsDi));
				    			break;
						}});
				</script>
					
				</div>
				<div class="form-group">
               <input name="butAcumulado" type="submit" value="Consultar" class="btn btn-primary">
               </div>
        	</form>

		</div>
		
	</div>
		

</body>
<!--
<footer class="bs-docs-footer" role="contentinfo">
	<div class="row">
		<div class="container">
			<p>Derechos reservados</p>
	     	<p>Instituto de Estudios Ambientales IDEA</p>
		</div>	
	</div>
	
</footer>
-->
</html>
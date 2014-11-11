<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3>Indicador A{{valorIndicador}}</h3><br>
			
			<h4>SIPREM.</h4><br>

			<form role="form" action="/calcularIndicador" method="post" id="formindicador">
				<div class="row">
					<div class="col-md-6">
						<div class="form-group">
							<label for="estacion">Estacion</label>
							<select class="form-control" name="estacionselect">
			                  %for estacion in estaciones:
			                  	<option value="{{estacion.pk}}">{{estacion.nombre}}</option>
			                  %end
			                </select>
						</div>

						<div class="form-group">
		                    <label for="tipoacumulado">Periodo de Tiempo</label>
			                <select class="form-control" id="opcionselect" name="opcionselect">
			                  <option value="1">Diario - Anual</option>
			                  <option value="2">Semestral</option>
			                  <option value="3">Trimestral Bimodal</option>
			                  <option value="4">Trimestral Estandar</option>
			                </select>
			            </div>
	            		<button type="button" class="btn btn-primary" valign="middle" id="butT">Preparar</button>
					</div>
					
					<div class="col-md-6">
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
							                <label for='diasel'>Año</label>\
							                <input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                </div><br>";
							                $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 2:
							    			var inputsDi ="<div class='form-group'>\
							                    <label for='tipoacumulado'>Semestre</label>\
								                <select class='form-control' name='semestre'>\
								                  <option value='1'>Enero - Junio</option>\
								                  <option value='2'>Julio - Diciembre</option>\
								                </select>\
								                </div>\
								            	<div class='form-group'>\
							                	<label for='diasel'>Año</label>\
							                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                	</div><br>";
								            $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 3:
							    			var inputsDi ="<div class='form-group'>\
							                    <label for='tipoacumulado'>Trimestre</label>\
								                <select class='form-control' name='trimestre'>\
								                <option value='1'>Diciembre - Febrero</option>\
								                <option value='2'>Marzo - Mayo</option>\
								                <option value='3'>Junio - Agosto</option>\
								                <option value='4'>Septiembre - Noviembre</option>\
								                </select>\
								            	</div>\
								            	<div class='form-group'>\
							                	<label for='diasel'>Año</label>\
							                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                	</div><br>";
								            $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 4:
							    			var inputsDi ="<div class='form-group'>\
							                    <label for='tipoacumulado'>Trimestre</label>\
								                <select class='form-control' name='trimestre'>\
								                <option value='1'>Enero - Marzo</option>\
								                <option value='2'>Abril - Junio</option>\
								                <option value='3'>Julio - Septiembre</option>\
								                <option value='4'>Octubre - Diciembre</option>\
								                </select>\
								            	</div>\
								            	<div class='form-group'>\
							                	<label for='diasel'>Año</label>\
							                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                	</div><br>";
								            $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;							    		
									}});
							</script>
						</div>
					</div>
				</div>
				<div class="row" align="center">
					<div class="form-group">
		               <input name="butAcumulado" type="submit" value="Consultar" class="btn btn-primary">
		            </div>
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
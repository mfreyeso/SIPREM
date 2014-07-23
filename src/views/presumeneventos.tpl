<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3>Resumen de Eventos</h3><br>
			
			<h4>SIPREM es capaz de crear resumenes de eventos clasificados según su jornada de ocurrencia
			y el tipo de precipitación segun metricas definidas anteriormente. Utilice las opciones dispuestas
			para personalizar el resumen de eventos deseado.</h4><br>

			<form role="form" action="/crearResumen" method="post">
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
		                    <label for="tipoacumulado">Tipo de Resumen</label>
			                <select class="form-control" id="opcionselect" name="opcionselect">
			                  <option value="1">Diario</option>
			                  <option value="2">Mensual</option>
			                  <option value="3">Anual</option>
			                  <option value="4">Semestral</option>
			                  <option value="5">Trimestral Bimodal</option>
			                  <option value="6">Trimestral Estandar</option>
			                  <option value="7">Multianual</option>
			                  <option value="8">Personalizado</option>
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
							    			<label for='diasel'>Fecha</label>\
							    			<input class='form-control' type='date' name='fecha'/>\
							    			</div><br>";							    			
											$("#divDinamico").empty();							                
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 2:
							    			var inputsDi = "<div class='form-group'>\
							                	<label for='diasel'>Mes</label>\
							                	<input class='form-control' type='month' name='mes'/>\
							                	</div><br>";
							                $("#divDinamico").empty();							                
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 3:
							    			var inputsDi = "<div class='form-group'>\
							                <label for='diasel'>Año</label>\
							                <input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                </div><br>";
							                $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 4:
							    			var inputsDi ="<div class='form-group'>\
							                   	<label for='diasel'>Año</label>\
							                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                	</div><br>";
								            $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 5:
							    			var inputsDi ="<div class='form-group'>\
							                    <label for='diasel'>Año</label>\
							                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                	</div><br>";
								            $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 6:
							    			var inputsDi ="<div class='form-group'>\
							                    <label for='diasel'>Año</label>\
							                	<input class='form-control' value='2002' type='number' name='ano' min='2002'>\
							                	</div><br>";
								            $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 7:
							    			var inputsDi ="<div class='form-group'>\
							                    <label for='diasel'>Año Inicial</label>\
							                	<input class='form-control' value='2002' type='number' name='anoi' min='2002'>\
							                	</div>\
							                	<div class='form-group'>\
							                    <label for='diasel'>Año Final</label>\
							                	<input class='form-control' value='2002' type='number' name='anof' min='2002'>\
							                	</div><br>";
								            $("#divDinamico").empty();
							                $("#divDinamico").append($(inputsDi));
							                break;

							    		case 8:
							    			var inputsDi = "<div class='form-group'>\
							    				<label for='tipoacumulado'>Fecha Inicial</label>\
							    				<input class='form-control' type='date' name='fechainicial'/><br>\
							    				<label for='tipoacumulado'>Fecha Final</label>\
							    				<input class='form-control' type='date' name='fechafinal'/>\
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
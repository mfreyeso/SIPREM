<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>	
	%include('header.tpl')
	%include('aside.tpl')
	<div class="row">
		<div class="col-xs-10 col-md-8">
			<div class="panel-heading">
				<h3><b>Parametrización</b></h3>
			</div>
			<div class="panel-body">
				<p align="justify">
					<h4>Realice los ajustes necesarios para usar SIPREM. Tenga en cuenta
			  		que solo podra utilizar las configuraciones que con su rol de usuario quedaron
			  		registradas en el sistema.</h4>				
				</p><br>

				<div class="panel panel-success">
					<div class="panel-heading">
						<h4><b>Configuraciones Existentes</b></h4>
					</div>

					<p></p><br>

					<div id="configExistentes">
						<table class="table table-hover" margin="auto">
					    	<tr>
					    		<td align="center"><strong>Nombre</strong></td>
					    		<td align="center"><strong>Tiempo de Diferencia</strong></td>
					    		<td align="center"><strong>Posición Precipitación</strong></td>
					    	</tr>
					    	%for configuracion in configuraciones:
					    		<tr>
					    		<td align="center">{{configuracion.nombre}}</td>
					    		<td align="center">{{configuracion.tiempodiferencia}}</td>
					    		<td align="center">{{configuracion.ubicacionprecip}}</td>
					    		</tr>
	                		%end
	                	</table>
					</div>				
				</div>

				<div class="panel panel-success">
					<div class="panel-heading">
						<h4><b>Administrar Configuraciones</b></h4>
					</div>
					<br>
					<div id="admconfiguraciones" class="panel-body">
						%include('formsconfiguracion.tpl')
					</div>				
				</div>				
			</div>				
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
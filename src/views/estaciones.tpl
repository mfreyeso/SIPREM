<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>
	%include('header.tpl')
	%include('aside.tpl')
	<div class="row">
		<h3>Estaciones Existentes</h3>
		<br>
		%if len(estaciones) % 2 == 0:
			%include('estacionespares.tpl')
		%else:
			%include('estacionesimpares.tpl')
		%end
		<br>

		<div class="col-xs-12 col-md-8">
			<div class="panel panel-default">
			   <div class="panel-heading">
			      <h2 class="panel-title">
			         <b>Administración de Estaciones</b>
			      </h2><br>
			   </div>
			   <div class="panel-body">
			   		<br>
			      	%include('formsestaciones.tpl')
			   </div>
			</div>
		</div>
	</div>
</body>
</html>
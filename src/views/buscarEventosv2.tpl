<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">

			<h4>Seleccione la estacion y defina un intervalo de fechas para poder realizar la busqueda de eventos
			dentro de SIPREM.</h4><br>

			<form role="form" action="/buscarEventos" method="post" id="formbeventos">
				<div class="row">
           			<div class="col-md-4">
           				<div class="form-group">
			                <label for="estacion">Estacion</label>
			                <select class="form-control" name="estacionselect">
			                  %for estacion in estaciones:
			                  	<option value="{{estacion.pk}}">{{estacion.nombre}}</option>
			                  %end
			                </select>
			           	</div>
					</div>
					<div class="col-md-4">
           				<div class="form-group">
			                <label for="estacion">Fecha Inicial</label><br>
			                <input type="date" name="fechainicial" class="form-control" id="fechainicial"/>
			           	</div>
					</div>
					<div class="col-md-4">
           				<div class="form-group">
			                <label for="estacion">Fecha Final</label><br>
			                <input type="date" name="fechafinal" class="form-control"/>			                
			           	</div>
					</div>					           			
           		</div>
           		<div class="row">
           			<div class="form-group" align="center">
			            <input name="butBuscar" type="submit" value="Buscar Eventos" class="btn btn-primary">
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
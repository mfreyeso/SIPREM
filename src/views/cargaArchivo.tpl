<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">

			<h4>Seleccione el archivo que contiene los datos que desea ingresar en el sistema, recuerde que si los datos ya han sido utilizados en alguna anterior ocasion, no se debera realizar de nuevo.</h4><br>

			<form role="form" action="/cargarArchivo" method="post" enctype="multipart/form-data">
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
					</div>

					<div class="col-md-6">
						<div class="form-group">
		                  <label for="exampleFile">Archivo de Registros</label>
		                  <input type="file" class="form-control"  name="fileIn" >
		                </div><br>
					</div>					
				</div>

				<div class="row" align="center">
					<div class="form-group">
		               <input name="butCargar" type="submit" value="Cargar Archivo" class="btn btn-primary">
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
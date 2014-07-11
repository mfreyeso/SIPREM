<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">

			<h4>Seleccione la estacion y defina parametros de busqueda para poder recuperar eventos
			cargados anteriormente en el sistema.</h4><br>

			<form role="form" action="/buscarEventos" method="post" enctype="multipart/form-data">
				<div class="form-group">
                <label for="estacion">Estacion</label>
                <select class="form-control" name="estacionselect">
                  %for estacion in estaciones:
                  	<option value="{{estacion.pk}}">{{estacion.nombre}}</option>
                  %end
                </select>
           		</div><br>

           		<div class="form-group">
                    <label for="tipoacumulado">Parametros de Busqueda</label>
	                <select class="form-control" id="opcionselect" name="opcionselect">
	                  <option value="1">Diario</option>
	                  <option value="2">Mensual</option>
	                  <option value="3">Anual</option>
	                </select>
	            </div>
	            <button type="button" class="btn btn-primary" valign="middle" id="butBusquedaD">Preparar</button><br><br>
				<div>				
					<div id="opcion1" style="display: none">
						<div class="form-group">
					    			<label for="diasel">Día</label>
					    			<input class="form-control" value="1" type="number" name="dia" min="1" max="31">
					 	</div>
					    <div class="form-group">
					          	<label for="diasel">Mes</label>
					               	<select class="form-control" name="mesUno">
						                <option value="1">Enero</option>
						                <option value="2">Febrero</option>
						                <option value="3">Marzo</option>
						 	            <option value="4">Abril</option>
						                <option value="5">Mayo</option>
						                <option value="6">Junio</option>
						                <option value="7">Julio</option>
						                <option value="8">Agosto</option>
						                <option value="9">Septiembre</option>
						                <option value="10">Octubre</option>
						                <option value="11">Noviembre</option>
						                <option value="12">Diciembre</option>
						            </select>
					    </div>
					    <div class="form-group">
					          	<label for="diasel">Año</label>
					           	<input class="form-control" type="number" name="anoUno" min="2002">
					    </div><br>
					</div>
					<div id="opcion2" style="display: none">						
						
					    <div class="form-group">
					          	<label for="diasel">Mes</label>
					               	<select class="form-control" name="mesDos">
						                <option value="1">Enero</option>
						                <option value="2">Febrero</option>
						                <option value="3">Marzo</option>
						 	            <option value="4">Abril</option>
						                <option value="5">Mayo</option>
						                <option value="6">Junio</option>
						                <option value="7">Julio</option>
						                <option value="8">Agosto</option>
						                <option value="9">Septiembre</option>
						                <option value="10">Octubre</option>
						                <option value="11">Noviembre</option>
						                <option value="12">Diciembre</option>
						            </select>
					    </div>
					    <div class="form-group">
					          	<label for="diasel">Año</label>
					           	<input class="form-control" type="number" name="anoDos" min="2002">
					    </div><br>
					</div>
					<div id="opcion3" style="display: none">
						<div class="form-group">
					          	<label for="diasel">Año</label>
					           	<input class="form-control" type="number" name="anoTres" min="2002">
					    </div><br>
					</div>
				<script>
					$("#butBusquedaD").on("click",
						function(){
							var seleccion = $("#opcionselect").val();
    						var intSeleccion = parseInt(seleccion);
    						switch(intSeleccion)
    						{
    							case 1:
    								$("#opcion1").css({display: "block"});
    								break;

    							case 2:
    								$("#opcion2").css({display: "block"});
    								break;

    							case 3:
    								$("#opcion3").css({display: "block"});
    								break;
    						}
						}
					);
				</script>
				</div>				                               
	               <div class="form-group">
	               <input name="butBuscar" type="submit" value="Buscar Eventos" class="btn btn-primary">
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
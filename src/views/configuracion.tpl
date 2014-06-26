<!DOCTYPE html>
<html lang="es">
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CSS de Bootstrap -->
    <link href="static/bootstrap.min.css" rel="stylesheet" media="screen">
    <meta charset="utf-8">
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="static/bootstrap.min.js"></script>
	<title>Instituto de Estudios Ambientales IDEA</title>
</head>

<body>	
	<header>
		<nav class="navbar navbar-default" role="navigation">
		  <div class="container-fluid">
		    <!-- Brand and toggle get grouped for better mobile display -->
		    <div class="navbar-header">
		      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
		        <span class="sr-only">Toggle navigation</span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		      </button>
		      <a class="navbar-brand" href="#">SIPREM</a>
		    </div>

		    <!-- Collect the nav links, forms, and other content for toggling -->
		    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
		      <ul class="nav navbar-nav">
		        <li class="active"><a href="#">Link</a></li>
		        <li><a href="#">Link</a></li>
		        <li class="dropdown">
		          <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
		          <ul class="dropdown-menu">
		            <li><a href="#">Action</a></li>
		            <li><a href="#">Another action</a></li>
		            <li><a href="#">Something else here</a></li>
		            <li class="divider"></li>
		            <li><a href="#">Separated link</a></li>
		            <li class="divider"></li>
		            <li><a href="#">One more separated link</a></li>
		          </ul>
		        </li>
		      </ul>
		     
		      <ul class="nav navbar-nav navbar-right">

		      <form class="navbar-form navbar-left" role="search">
		        <div class="form-group">
		          <input type="text" class="form-control" placeholder="Search">
		        </div>
		        <button type="submit" class="btn btn-default">Submit</button>
		      </form>



		        <li><a href="#">Link</a></li>
		        <li class="dropdown">
		          <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
		          <ul class="dropdown-menu">
		            <li><a href="#">Action</a></li>
		            <li><a href="#">Another action</a></li>
		            <li><a href="#">Something else here</a></li>
		            <li class="divider"></li>
		            <li><a href="#">Separated link</a></li>
		          </ul>
		        </li>
		      </ul>
		    </div><!-- /.navbar-collapse -->
		  </div><!-- /.container-fluid -->
		</nav>
		<!--HEADER INFORMATIVO DE LA APLICACION -->

		<div class="page-header">
			<h1>Universidad Nacional de Colombia <small>Sede Manizales</small></h1>
			<h2>Instituto de Estudios Ambientaltes IDEA <small>Sistema de Informacion Meteorologíco de Precipitaciones Red de Estaciones Manizales</small></h2>
		</div>
	</header>

	<aside>
		<div class="col-xs-4 col-md-2">
			<ul class="nav nav-pills nav-stacked">
	 			<li><a href="/index">Home</a></li>
	  			<li><a href="#">Perfil</a></li>
	  			<li><a href="#">Estaciones</a></li>
	  			<li><a href="/cargarEventos">Eventos</a></li>
	  			<li class="active"><a href="/tconfiguracion">Configuración</a></li>
	  			<li><a href="/tcarga">Carga de Datos</a></li>
	  			<li><a href="/tacumulado">Acumulado</a></li>
	  			<li><a href="/tresumen">Resumen</a></li>
			</ul>
		</div>
	</aside>

	<div class="row">
		<div class="col-xs-12 col-md-8">
			<div class="panel-heading"><h3>Parametrización</h3></div>
	  		<div class="panel-body">
	  		<p align="justify"><h4>Realice los ajustes necesarios para usar SIPREM. Tenga en cuenta
	  		que solo podra utilizar las configuraciones que con su rol de usuario quedaron
	  		registradas en el sistema.</h4></p><br>
				<!--Panel Configuraciones-->	  		
	  			<div class="panel panel-info">
				  <div class="panel-heading"><h4>Configuraciones</h4></div>
				  	<div class="panel-body">
				    <h5>Configuraciones Existentes</h5><br>
				    <div class="btn-group">
					  <button type="button" class="btn btn-info" id="butA">Adicionar</button>
					  <button type="button" class="btn btn-info" id="butE">Modificar</button>
					  <button type="button" class="btn btn-info" id="butD">Eliminar</button>
					</div><br><br>
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
				    			<td align="center"><form action="/ajustarConfiguracion/{{configuracion.pk}}"><input  type="submit" value="Utilizar" class="btn btn-info btn-sm"/></form>
                			</tr>
                			%end
                		</table><br>
						</div>				    	
                		<div id="dinAdicionarConf">
                			<script>
                				$("#butA").on("click", 
                					function(){
                						$("#configExistentes").hide();
                						var inputsDi = "<form role='form' action='/crearconfiguracion' method='post' enctype='multipart/form-data'>\
                							<div class='form-group'>\
				                			<label for='nombreconf'>Etiqueta Configuración</label>\
				                			<input type='text' class='form-control' name='nombreconf' id='nombreconf'\
				                			placeholder='nombre de configuracion'>\
				                			</div><br>\
				                			<div class='form-group'>\
				                			<label for='tiempodif'>Tiempo de Diferencia entre Eventos</label>\
				                			<input type='number' min='5' class='form-control'  name='tiempodif' id='tiempodif'\
				                			placeholder='Numero expresado en minutos'>\
				                			</div><br>\
				                			<div class='form-group'>\
				                			<label for='posipre'>Posición Precipitación</label>\
				                			<input type='number' class='form-control'  name='pospre' id='pospre'\
				                			placeholder='8'>\
				                			</div><br>\
				                			<input name='butAdicionar' type='submit' value='Adicionar' class='btn btn-info'>\
				                			</form>";
				                		$("#dinAdicionarConf").append($(inputsDi));
                					});
                			</script>          
                		</div>
                	</div>

                	<div id="eliminarConf">
                		<script>
                		$("#butD").on("click", 
                					function(){
                						$("#configExistentes").hide();
                						var inputsDi ="<table class='table table-hover'\
                						margin='auto'><tr>\
										<td align='center'><strong>Nombre</strong></td>\
										<td align='center'><strong>Tiempo de Diferencia</strong></td>\
										<td align='center'><strong>Posición Precipitación</strong></td>\
										</tr>\
										%for configuracion in configuraciones:\
											<tr>\
											<td align='center'>{{configuracion.nombre}}</td>\
											<td align='center'>{{configuracion.tiempodiferencia}}</td>\
											<td align='center'>{{configuracion.ubicacionprecip}}</td>\
											<td align='center'><form action='/ajustarConfiguracion/{{configuracion.pk}}'><input  type='submit' value='Eliminar'\class='btn btn-danger btn-sm'/></form>\
											</tr>\
										%end\
										</table><br>";               						
				                		$("#eliminarConf").append($(inputsDi));
                					});
                		</script>                		
                	</div>
			  	<!-- Panel Jornadas y Categorias-->
				  <div>
				   	<div class="panel panel-info">
						<div class="panel-heading"><h4>Jornadas y Categorias</h4></div>
							<div class="panel-body">
								<div class="row">
									<div class="col-xs-12 col-md-6">
										<div class="panel panel-info">
										  <div class="panel-heading">Categorias</div>
										  <div class="panel-body">
										   		<h5>Categorias Existentes</h5><br>
										    	<table class="table table-hover" margin="auto">
										    		<tr>
										    			<td align="center"><strong>Categoria</strong></td>
										    			<td align="center"><strong>Medida</strong></td>
										    		</tr>
										    		%for categoria in categorias:
										    		<tr>
										    			<td align="center">{{categoria.etiquetaCategoria}}</td>
										    			<td align="center">{{categoria.medidaMagnitud}}</td>
						                			</tr>
						                			%end
						                		</table><br>
						                		<button type="button" class="btn btn-info" valign="middle" id="butAddC">Adicionar Categoria</button><br><br>
							                	<div id="addCategoria">
							                		<script>
							                			$("#butAddC").on("click", 
						                					function(){
						                						var inputsDi = "<form role='form' action='/crearCategoria' method='post' enctype='multipart/form-data'>\
						                							<div class='form-group'>\
										                			<label for='nombrecat'>Nombre Categoria</label>\
										                			<input type='text' class='form-control' name='nombrecat' id='nombrecat'\
										                			placeholder='Ejemplo: Llovizna'>\
										                			</div><br>\
										                			<div class='form-group'>\
										                			<label for='hinicio'>Valor de Referencia</label>\
										                			<input type='text' class='form-control'  name='metricac' id='metricat'\
										                			placeholder='2'>\
										                			</div><br>\
										                			<input name='butAdicionar' type='submit' value='Adicionar' class='btn btn-info'>\
										                			</form>";
										                		$("#addCategoria").append($(inputsDi));
						                					});
							                		</script>

							                		
							                	</div>
									  	  </div>
								  		</div>
									</div>
										
									<div class="col-xs-12 col-md-6">
										<div class="panel panel-info">
											  <div class="panel-heading">Jornadas</div>
											  <div class="panel-body">
											  	<h5>Jornadas Existentes</h5><br>
										    	<table class="table table-hover" margin="auto">
										    		<tr>
										    			<td align="center"><strong>Jornada</strong></td>
										    			<td align="center"><strong>Hora Inicio</strong></td>
										    			<td align="center"><strong>Hora Fin</strong></td>
										    		</tr>
										    		%for jornada in jornadas:
										    		<tr>
										    			<td align="center">{{jornada.etiquetaJornada}}</td>
										    			<td align="center">{{jornada.horaInicio}}</td>
										    			<td align="center">{{jornada.horaFin}}</td>
						                			</tr>
						                			%end
						                		</table><br>
						                		<button type="button" class="btn btn-info" valign="middle" id="butAddJ">Adicionar Jornada</button><br><br>

							                	<div id="addJornada">
							                		<script>
							                			$("#butAddJ").on("click", 
						                					function(){
						                						var inputsDi = "<form role='form' action='/crearJornada' method='post' enctype='multipart/form-data'>\
						                							<div class='form-group'>\
										                			<label for='nombreconf'>Etiqueta</label>\
										                			<input type='text' class='form-control' name='nombrejor' id='nombrejor'\
										                			placeholder='Ejemplo: Mañana'>\
										                			</div><br>\
										                			<div class='form-group'>\
										                			<label for='hinicio'>Hora Inicio</label>\
										                			<input type='number' min='0' max='23' class='form-control'  name='hinicio' id='hinicio'\
										                			placeholder='2'>\
										                			</div><br>\
										                			<div class='form-group'>\
										                			<label for='hfin'>Hora Fin</label>\
										                			<input type='number' class='form-control' min='0' max='23' name='hfin' id='hfin' placeholder='8'>\
										                			</div><br>\
										                			<input name='butAdicionar' type='submit' value='Adicionar' class='btn btn-info'>\
										                			</form>";
										                		$("#addJornada").append($(inputsDi));
						                					});
							                		</script>
							                	</div>
											</div>
								  		</div>
									</div>
								</div>				    
							</div>
						</div>
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
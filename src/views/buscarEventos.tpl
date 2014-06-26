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
	  			<li><a href="/tconfiguracion">Configuración</a></li>
	  			<li class="active"><a href="/tcarga">Carga de Datos</a></li>
	  			<li><a href="/tacumulado">Acumulado</a></li>
	  			<li><a href="/tresumen">Resumen</a></li>
			</ul>
		</div>
	</aside>

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
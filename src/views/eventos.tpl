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
	  			<li class="active"><a href="/cargarEventos">Eventos</a></li>
	  			<li><a href="/tconfiguracion">Configuración</a></li>
	  			<li><a href="/tcarga">Carga de Datos</a></li>
	  			<li><a href="/tacumulado">Acumulado</a></li>
	  			<li><a href="/tresumen">Resumen</a></li>
			</ul>
		</div>
	</aside>

	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3>Eventos Encontrados</h3>
    
	  	     <table class="table table-hover">
		        <tr>
		    	  	<td><strong>Evento</strong></td>
		            <td><strong>Fecha</strong></td>
		            <td><strong>Hora de Inicio</strong></td>
		            <td><strong>Hora de Fin</strong></td>
		            <td><strong>Magnitud</strong></td>
		            <td><strong>Duración (min)</strong></td>
		            <td><strong>Intensidad Media (mm/h)</strong></td>
		            <td><strong>Intensidad Maxima</strong></td>
		            <td><strong>Categoria Evento</strong></td>
		            <td><strong>Jornada Evento</strong></td>
		            <td><strong>Observaciones</strong></td>
		        </tr>
		        	%cont=1
		           %for evento in coleccionEventos:
		        	<tr>
			            <td>{{cont}}</td>
			            <td>{{evento.entregarFecha()}}</td>
			            <td>{{evento.entregarHoraInicio()}}</td>
			            <td>{{evento.entregarHoraFin()}}</td>
			            <td>{{evento.entregarMagnitud()}}</td>
			            <td>{{evento.entregarDuracion()}}</td>
			            %b = '%.2f' %evento.entregarIntensidadMedia()
			            <td>{{b}}</td>
			            <td>{{evento.entregarIntensidadMaxima()}}</td>
			            <td>{{evento.entregarTipoLluvia()}}</td>
			            <td>{{evento.entregarJornadaEvento()}}</td>
			            <td>{{evento.entregarObservaciones()}}</td>
			            %cont+=1			            	
		          	</tr>
		          	%end
	  		 </table>
			

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
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
	 			<li class="active"><a href="/index">Home</a></li>
	  			<li><a href="#">Perfil</a></li>
	  			<li><a href="#">Estaciones</a></li>
	  			<li><a href="/cargarEventos">Eventos</a></li>
	  			<li><a href="/tconfiguracion">Configuración</a></li>
	  			<li><a href="/tcarga">Carga de Datos</a></li>
	  			<li><a href="/tacumulado">Acumulado</a></li>
	  			<li><a href="/tresumen">Resumen</a></li>
			</ul>
		</div>
	</aside>

	<div class="row">
		<div class="col-xs-12 col-md-8">
		<!--Me encargo de sacar todo lo que necesito de los objetos-->
			
				%listaMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
				%listaMetricas = ["Duración(min)", "Magnitud(mm)", "Intensidad Media(mm/h)", "Intensidad Maxima(mm/h)"]
				%listaSemestres = ["Enero - Junio", "Julio - Diciembre"]
				%listaTrimestres = ["Diciembre - Febrero", "Marzo - Mayo", "Junio - Agosto", "Septiembre - Noviembre"]

				%maximos= resource[2]
				%rJornadas = resource[0]
				%rCategorias = resource[1]

			<h2>Resumen</h2><br>

			<h3>Precipitaciones según Categoria</h3><br>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Categoria</strong></td>
		             %for i in range(0, len(listaMeses)):
		        		<td><strong>{{listaMeses[i]}}</strong></td>
			        %end	            
		        </tr>

		        %for i in range(0, len(rCategorias)):
		        %categoria = rCategorias[i][0]
		        %listaMes = rCategorias[i][1]
		        <tr>
		    	  	<td><strong>{{categoria}}</strong></td>
		             %for j in range(1, len(listaMes)):
		        		<td>{{listaMes[j]}}</td>
			        %end	            
		        </tr>		        
		        %end	        
		        </table><br>

		        <h3>Precipitaciones según Jornada</h3><br>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Jornada</strong></td>
		             %for i in range(0, len(listaMeses)):
		        		<td><strong>{{listaMeses[i]}}</strong></td>
			        %end	            
		        </tr>

		        %for i in range(0, len(rJornadas)):
		        %jornada = rJornadas[i][0]
		        %listaMesJ = rJornadas[i][1]
		        <tr>
		    	  	<td><strong>{{jornada}}</strong></td>
		             %for j in range(1, len(listaMesJ)):
		        		<td>{{listaMesJ[j]}}</td>
			        %end	            
		        </tr>		        
		        %end	        
		        </table><br>


		        <h3>Maximos Obtenidos</h3><br>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Metrica</strong></td>
		             %for i in range(0, len(listaMeses)):
		        		<td><strong>{{listaMeses[i]}}</strong></td>
			        %end	            
		        </tr>

		        %for i in range(0, len(listaMetricas)):
		        %metrica = listaMetricas[i]
		        <tr>
		    	  	<td><strong>{{metrica}}</strong></td>
		             %for j in range(0, len(maximos)):
		             	%b = '%.2f' %maximos[j][i]
		        		<td>{{b}}</td>
			        %end	            
		        </tr>		        
		        %end	        
		        </table><br>

	  		 <form role="form" action="/reporteResumen" method="post" enctype="multipart/form-data">
				<div class="form-group">
               <input name="butCargar" type="submit" value="Generar Reporte" class="btn btn-primary">
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
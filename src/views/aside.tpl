<aside data-spy="scroll" id="navi">
		<div class="col-xs-4 col-md-2">
			<ul class="nav nav-pills nav-stacked" id="navaside">
	 			<li><a href="/index">Inicio</a></li>
	  			<li><a href="#">Perfil</a></li>
	  			<li id="estaciones"><a href="/estaciones">Estaciones</a></li>
	  			<li><a href="/eventos" class="dropdown-toggle" data-toggle="dropdown">Eventos<span class="caret"></span></a>
		          <ul class="dropdown-menu">
		          	<li><a href="/eventos">Eventos(Busqueda Basica)</a></li>
		          	<li><a href="/eventosFiltro">Eventos(Busqueda Avanzada)</a></li>
		          </ul>
		        </li>
	  			<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Configuración<span class="caret"></span></a>
		          <ul class="dropdown-menu">
		          	<li><a href="/tconfiguracion">Administrar Configuraciones</a></li>
		            <li><a href="/tconfiguracionjc">Administrar Jornadas y Categorias</a></li>
		         </ul>
		        </li>
		        <li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Administración de Datos<span class="caret"></span></a>
		          <ul class="dropdown-menu">
		          	<li><a href="/archivoPlano">Carga de Archivos Planos</a></li>
		            <li><a href="#">Bodega de Datos</a></li>
		          </ul>
		        </li>

		        <li><a href="#" class="dropdown-toggle" data-toggle="dropdown">Acumulados<span class="caret"></span></a>
		          <ul class="dropdown-menu">
		          	<li><a href="/tacumulado">Acumulados de Registros</a></li>
		          	<li><a href="/tacumuladoeventos">Acumulados de Eventos</a></li>
		          </ul>
		        </li>
	  			<li><a href="/topcresumen">Resumen de Eventos</a></li>
	  			<li><a class="dropdown-toggle" data-toggle="dropdown">Indicador AX<span class="caret"></span></a>
		          <ul class="dropdown-menu">
		          	<li><a href="/configurarindicador">Configuración de Indicador</a></li>
		            <li><a href="/tsindicador">Utilizar Indicador</a></li>
		          </ul>
		        </li>
	  			<li><a href="/tresumen">Representaciones Graficas</a></li>
			</ul>
		</div>
</aside>
<script>
	var x;
	x = $(document);
	x.ready(asideDinamico);

	function asideDinamico() {
		var url = window.location.pathname,
	        urlRegExp = new RegExp(url.replace(/\/$/, '') + "$");
	    $('#navaside a').each(function () {
	        if (urlRegExp.test(this.href.replace(/\/$/, ''))) {
	            var liPadre = $(this).parent();
	            liPadre.addClass('active');
	        }
	    });    
	}
</script>


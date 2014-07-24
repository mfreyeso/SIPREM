<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3><strong>Resumen de Eventos</strong></h3>
			<h4><strong>Estacion: </strong>{{nombreEstacion}}</h4>
			<h4>{{cadenaParametrizada}}</h4><br>

			%listaMeses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
			%listaMetricas = ["Duración(min)", "Magnitud(mm)", "Intensidad Media(mm/h)", "Intensidad Maxima(mm/h)"]
			%listaSemestres = ["Enero - Junio", "Julio - Diciembre"]
			%listaTrimestresEstandar = ["Ene-Feb-Mar", "Abr-May-Jun", "Jul-Ago-Sep", "Oct-Nov-Dic"]
			%listaTrimestresBimodal = ["Dic-Ene-Feb", "Mar-Abr-May", "Jun-Jul-Ago", "Sep-Oct-Nov"]

			%resultadosCategoria = resultados[0]
			%resultadosJornada = resultados[1]
			%resultadosMaximos = resultados[2]
			
			<div>
				<h3>Precipitaciones según Categoria</h3><br>
					%include('rescategoria.tpl', opcionr = opcionrs, resultados = resultadosCategoria, categoriasP = categorias, diasMesF = diasMes, vAnualF = vAnual)				
			</div>

			<div>
				<h3>Precipitaciones según Jornada</h3><br>
					
			</div>
			<div>
				<h3>Máximos Obtenidos</h3><br>
				
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
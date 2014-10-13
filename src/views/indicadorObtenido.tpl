<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')

	%listaMeses = ["Dic","Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3>Indicador A{{valIndicador}}</h3>
			<h4>{{cadenaParametrizada}}</h4><br>
			%if opcion == 1:
				%include('tablaIndicadorAnual.tpl')
			%elif opcion == 2:
				%include('tablaIndicadorSemestral.tpl')
			%elif opcion == 3:
				%include('tablaIndicadorTrimestralB.tpl')
			%else:
				%include('tablaAcumuladosTrimestral.tpl')
			%end
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
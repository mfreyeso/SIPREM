<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')

	%listaMeses = ["Dic","Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

	<div class="row">
		<div class="col-xs-12 col-md-8">
			<div id="indicador">
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
			<div align="center" style="padding-top:0.3cm">
				<p>
					<button type="button" class="btn btn-default"><a download="indA{{valIndicador}}{{cadenaParametrizada}}.xls" href="#" onclick="return ExcellentExport.excel(this, 'indicador', 'indicador');">Reporte Excel</a></button>
					<button type="button" class="btn btn-default" id="btnreportevent">Reporte PDF</button>					
				</p>																
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
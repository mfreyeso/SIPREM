<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')

	%listaMeses = ["Dic","Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

	<div class="row">
		<div class="col-xs-12 col-md-8">
			<div id="acumulados">
				<h3>Acumulado de Registros Obtenido</h3>
				<h4>{{cadenaParametrizada}}</h4><br>
				%if opcion == 1:
					%include('tablaAcumulados.tpl')
				%elif opcion == 2:
					%include('tablaAcumuladosSemestral.tpl')
				%elif opcion == 3:
					%include('tablaAcumuladosTrimestralB.tpl')
				%elif opcion == 4:
					%include('tablaAcumuladosTrimestral.tpl')
				%else:
					%include('tablaAcumuladosMultianual.tpl')				
				%end			
			</div>
			<div align="center" style="padding-top:0.3cm">
				<p>
					<button type="button" class="btn btn-default"><a download="acum{{cadenaParametrizada}}.xls" href="#" onclick="return ExcellentExport.excel(this, 'acumulados', 'acumulado');">Reporte Excel</a></button>
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
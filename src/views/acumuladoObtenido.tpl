<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3>Acumulado de Registros Obtenido</h3>
			<h4>{{cadenaParametrizada}}</h4><br>
			<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Magnitud Acumulada (mm.)</strong></td>
		    	  	%b = '%.2f' %acumulado
		            <td align="center">{{b}}</td>		            
		        </tr>
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
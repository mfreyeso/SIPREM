<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<div id="acumulados">
				<h3>Acumulado Obtenido</h3>
				<h4>{{cadenaParametrizada}}</h4><br>

				<table class="table table-hover">
			        <tr>
			    	  	<td><strong>Metrica</strong></td>
			            <td align="center"><strong>Resultado</strong></td>		            
			        </tr>
			        
			        <tr>
			    	  	<td><strong>Magnitud (mm)</strong></td>
			            <td align="center">{{resultados[0]}}</td>		            
			        </tr>

			        <tr>
			    	  	<td><strong>Intensidad Media Maxima (mm/h)</strong></td>
			    	  	%b = '%.1f' %resultados[1]
			            <td align="center">{{b}}</td>		            
			        </tr>

			        <tr>
			    	  	<td><strong>Intensidad Maxima (mm/h)</strong></td>
			            <td align="center">{{resultados[2]}}</td>		            
			        </tr>
			        <tr>
			    	  	<td><strong>Duración (min.)</strong></td>
			            %rTres = int(resultados[3])
			            <td align="center">{{rTres}}</td>
			        </tr>

			        <tr>
			    	  	<td><strong>Duración Maxima (min.)</strong></td>
			            %rCuatro = int(resultados[4])	
			            <td align="center">{{rCuatro}}</td>
			        </tr>
			        <tr>
			    	  	<td><strong>Duración Neta (min.)</strong></td>
			            %rCinco = int(resultados[5])
			            <td align="center">{{rCinco}}</td>
			        </tr>
		  		 </table>				
			</div>
			<div align="center" style="padding-top:0.3cm">
				<p>
					<button type="button" class="btn btn-default"><a download="acumeventos{{cadenaParametrizada}}.xls" href="#" onclick="return ExcellentExport.excel(this, 'acumulados', 'acumulado');">Reporte Excel</a></button>
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
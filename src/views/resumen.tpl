<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	<div class="row">
		<div class="col-xs-12 col-md-8">
		<!--Me encargo de sacar todo lo que necesito de los objetos de forma MAGICA-->
			
				%cadenaPeriodo = objResumen.periodoEventos()
				%maximos = objResumen.entregarMaximos(0,0)

				%vCategorias = objMain.entregarCategoriaEventos()
				%vJornadas = objMain.entregarJornadaEventos()

				%voCategorias = objMain.entregarOcurrenciaCategoriaEventos()
				%voJornadas = objMain.entregarOcurrenciaJornadaEventos()
			
			<h2>Resumen</h2><br>

			<p><h4>El resumen presentado es un esquema general de metricas debido a que los datos que fueron
			suministrados por el usuario se encuentran incompletos.</h4></p><br>

			<h3>Precipitaciones según Categoria</h3>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Categoria</strong></td>
		            <td><strong>Resultado</strong></td>		            
		        </tr>
		        %lim = len(vCategorias)
		        %for i in range(0, lim):
		        	<tr>
			    	  	<td><strong>{{vCategorias[i].entregarEtiqueta()}}</strong></td>
			            <td>{{voCategorias[i]}}</td>		            
		        	</tr>
		        %end
		        </table>


			<h3>Precipitaciones según Jornada de Ocurrencia</h3>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Jornada</strong></td>
		            <td><strong>Resultado</strong></td>		            
		        </tr>
		        %lim = len(vJornadas)
		        %for i in range(0, lim):
		        	<tr>
			    	  	<td><strong>{{vJornadas[i].entregarEtiquetaJornada()}}</strong></td>
			            <td>{{voJornadas[i]}}</td>		            
		        	</tr>
		        %end
		        </table>


			<h3>Maximos en Precipitaciones</h3>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Metrica</strong></td>
		            <td><strong>Resultado</strong></td>		            
		        </tr>
		        
		        <tr>
		    	  	<td><strong>Duración (min)</strong></td>
		            <td>{{maximos[0]}}</td>		            
		        </tr>

		        <tr>
		    	  	<td><strong>Magnitud (mm)</strong></td>
		            <td>{{maximos[1]}}</td>		            
		        </tr>

		        <tr>
		    	  	<td><strong>Intensidad Media (mm/h)</strong></td>
		    	  	%b = '%.2f' %maximos[2]
		            <td>{{b}}</td>		            
		        </tr>

		        <tr>
		    	  	<td><strong>Intensidad Maxima (mm/h)</strong></td>
		            <td>{{maximos[3]}}</td>		            
		        </tr>
		        


	  		 </table>

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
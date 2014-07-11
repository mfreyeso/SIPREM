<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')

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
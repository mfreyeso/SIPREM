<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
		<!--Me encargo de sacar todo lo que necesito de los objetos-->
			
				%listaMetricas = ["Duración(min)", "Magnitud(mm)", "Intensidad Media(mm/h)", "Intensidad Maxima(mm/h)"]
				%listaSemestres = ["Semestre 1", "Semestre 2"]
				
				%maximos= resource[2]
				%rJornadas = resource[0]
				%rCategorias = resource[1]
				%totalesJ = resource[3][0]
				%totalesC = resource[3][1]
				%totalesM = resource[3][2]

			<h2>Resumen</h2><br>

			<h3>Precipitaciones según Categoria</h3><br>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Categoria</strong></td>
		             %for i in range(0, len(listaSemestres)):
		        		<td align="center"><strong>{{listaSemestres[i]}}</strong></td>
			        %end
			        <td align="center"><strong>Totales</strong></td>	            
		        </tr>

		        %for i in range(0, len(rCategorias)):
		        %categoria = rCategorias[i][0]
		        %listaMes = rCategorias[i][1]
		        %sum=0
		        <tr>
		    	  	<td><strong>{{categoria}}</strong></td>
		             %for j in range(1, len(listaMes)):
		             	%sum = sum + listaMes[j]
		        		<td align="center">{{listaMes[j]}}</td>
			        %end
			        <td align="center"><strong>{{sum}}</strong></td>
			        	            
		        </tr>		        
		        %end
		        <tr>
		    	  	<td><strong>Totales</strong></td>
		    	  	%totalGlobal = 0
		             %for j in range(1, len(listaMes)):
		             	%totalGlobal = totalGlobal + totalesC[j]             	
		        		<td align="center"><strong>{{totalesC[j]}}</strong></td>
			        %end
			        <td align="center"><strong>{{totalGlobal}}</strong></td>
			        	            
		        </tr>	        
		        </table><br>

		        <h3>Precipitaciones según Jornada</h3><br>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Jornada</strong></td>
		             %for i in range(0, len(listaSemestres)):
		        		<td align="center"><strong>{{listaSemestres[i]}}</strong></td>
			        %end
			        <td align="center"><strong>Totales</strong></td>	            
		        </tr>

		        %for i in range(0, len(rJornadas)):
		        %jornada = rJornadas[i][0]
		        %listaMesJ = rJornadas[i][1]
		        %sum=0
		        <tr>
		    	  	<td><strong>{{jornada}}</strong></td>
		             %for j in range(1, len(listaMesJ)):
		             	%sum = sum + listaMesJ[j]
		        		<td align="center">{{listaMesJ[j]}}</td>
			        %end
			        <td align="center"><strong>{{sum}}</strong></td>
		        </tr>		        
		        %end
		        <tr>
		    	  	<td><strong>Totales</strong></td>
		    	  	%totalGlobal = 0
		             %for j in range(1, len(listaMes)):
		             	%totalGlobal = totalGlobal + totalesJ[j]
		             	<td align="center"><strong>{{totalesJ[j]}}</strong></td>
			        %end
			        <td align="center"><strong>{{totalGlobal}}</strong></td>
			    </tr>	        
		        </table><br>


		        <h3>Máximos Obtenidos</h3><br>
				<table class="table table-hover">
		        <tr>
		    	  	<td><strong>Metrica</strong></td>
		             %for i in range(0, len(listaSemestres)):
		        		<td align="center"><strong>{{listaSemestres[i]}}</strong></td>
			        %end         
		        </tr>

		        %for i in range(0, len(listaMetricas)):
		        %metrica = listaMetricas[i]
		        <tr>
		    	  	<td><strong>{{metrica}}</strong></td>
		             %for j in range(0, len(maximos)):
		             	%if i == 0:
		             		%b = int(maximos[j][i])
		             		<td align="center">{{b}}</td>
		             	%end
		             	%if i != 0:
		             	   	%b = '%.1f' %maximos[j][i]
		        			<td align="center">{{b}}</td>
		        		%end
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
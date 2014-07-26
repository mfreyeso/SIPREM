<div>
	%if opcionr == 1:
		<!--<h3>Diario</h3> -->
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        <td align="center"><strong>Valor Obtenido</strong></td>      
			</tr>
			%for i in range(0, len(listaMetricas)):
				%metrica = listaMetricas[i]
				<tr>
					<td><strong>{{metrica}}</strong></td>
					<td align="center">{{resultados[i]}}</td>
				</tr>					
			%end			
		</table><br>
	%elif opcionr == 2:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        %for i in range(1, (diasMesF + 1)):
		       		<td align="center"><strong>{{i}}</strong></td>
		        %end	            
			</tr>
			%for i in range(0, len(listaMetricas)):
				%metrica = listaMetricas[i]
				<tr>
					<td><strong>{{metrica}}</strong></td>
					%for j in range(1, (diasMesF + 1)):
						<td align="center">{{resultados[j][i]}}</td>
					%end
				</tr>
			%end	    
		</table><br>
	%elif opcionr == 3:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        %for i in range(0, len(listaMeses)):
		       		<td align="center"><strong>{{listaMeses[i]}}</strong></td>
		        %end	            
			</tr>

			%for i in range(0, len(listaMetricas)):
				%metrica = listaMetricas[i]
				<tr>
					<td><strong>{{metrica}}</strong></td>
					%for j in range(1, 13):
						<td align="center">{{resultados[j][i]}}</td>
					%end
				</tr>
			%end    
		</table><br>
	%elif opcionr == 4:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        %for i in range(0, len(listaSemestres)):
		       		<td align="center"><strong>{{listaSemestres[i]}}</strong></td>
		        %end		                    
			</tr>

			%for i in range(0, len(listaMetricas)):
				%jornada = listaMetricas[i]
				<tr>
					<td><strong>{{jornada}}</strong></td>
					%for j in range(0, 2):
						<td align="center">{{resultados[j][i]}}</td>
					%end					
				</tr>
			%end 
		</table><br>
	%elif opcionr == 5:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        %for i in range(0, len(listaTrimestresBimodal)):
		       		<td align="center"><strong>{{listaTrimestresBimodal[i]}}</strong></td>
		        %end		                 
			</tr>

			%for i in range(0, len(listaMetricas)):
				%metrica = listaMetricas[i]
				<tr>
					<td><strong>{{metrica}}</strong></td>
					%for j in range(0, 4):
						<td align="center">{{resultados[j][i]}}</td>
					%end
				</tr>
			%end			    
		</table><br>
	%elif opcionr == 6:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        %for i in range(0, len(listaTrimestresEstandar)):
		       		<td align="center"><strong>{{listaTrimestresEstandar[i]}}</strong></td>
		        %end         
			</tr>

			%for i in range(0, len(listaMetricas)):
				%metrica = listaMetricas[i]
				<tr>
					<td><strong>{{metrica}}</strong></td>
					%for j in range(0, 4):
						<td align="center">{{resultados[j][i]}}</td>
					%end
				</tr>
			%end	    
		</table><br>
	%elif opcionr == 7:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        %for i in range(vAnualF[0], (vAnualF[1]+ 1)):
		       		<td align="center"><strong>{{i}}</strong></td>
		        %end
		    </tr>

			%for i in range(0, len(listaMetricas)):
				%metrica = listaMetricas[i]
				<tr>
					<td><strong>{{metrica}}</strong></td>
					%for j in range(0, len(vAnualF)):
						<td align="center">{{resultados[j][i]}}</td>
					%end
				</tr>
			%end	    
		</table><br>
	%else:
		<!--<h3>Personalizada</h3> -->
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Métrica</strong></td>
		        <td align="center"><strong>Valor Máximo</strong></td>  
		    </tr>
			%for i in range(0, len(listaMetricas)):
				%metrica = listaMetricas[i]
				<tr>
					<td><strong>{{metrica}}</strong></td>
					<td align="center">{{resultados[i]}}</td>
				</tr>					
			%end			
		</table><br>
	%end
</div>
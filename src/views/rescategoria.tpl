<div>
	%if opcionr == 1:
		<!--<h3>Diario</h3> -->
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        <td align="center"><strong>Ocurrencias</strong></td>      
			</tr>
			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				<tr>
					<td><strong>{{categoria}}</strong></td>
					<td align="center">{{resultados[i]}}</td>
				</tr>					
			%end			
		</table><br>
	%elif opcionr == 2:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        %for i in range(1, (diasMesF + 1)):
		       		<td align="center"><strong>{{i}}</strong></td>
		        %end
		        <td align="center"><strong>Totales</strong></td>	            
			</tr>

			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				%eventosCategoria = resultados[i]
				<tr>
					<td><strong>{{categoria}}</strong></td>
					%sum = 0
					%for j in range(1, (diasMesF + 1)):
						%sum = sum + eventosCategoria[j]
						<td align="center">{{eventosCategoria[j]}}</td>
					%end
					<td align="center"><strong>{{sum}}</strong></td>
				</tr>
			%end
			<tr>
				<td><strong>Totales</strong></td>
				%totalFinal = 0
				%for i in range(1, (diasMesF + 1)):
					%totalDia = 0
					%for j in range(0, len(categoriasP)):
						%totalDia = totalDia + resultados[j][i]
					%end
					<td align="center"><strong>{{totalDia}}</strong></td>
					%totalFinal = totalFinal + totalDia
				%end
				<td align="center"><strong>{{totalFinal}}</strong></td>
			</tr>	    
		</table><br>
	%elif opcionr == 3:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        %for i in range(0, len(listaMeses)):
		       		<td align="center"><strong>{{listaMeses[i]}}</strong></td>
		        %end
		        <td align="center"><strong>Totales</strong></td>	            
			</tr>

			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				%eventosCategoria = resultados[i]
				<tr>
					<td><strong>{{categoria}}</strong></td>
					%sum = 0
					%for j in range(1, 13):
						%sum = sum + eventosCategoria[j]
						<td align="center">{{eventosCategoria[j]}}</td>
					%end
					<td align="center"><strong>{{sum}}</strong></td>
				</tr>
			%end
			<tr>
				<td><strong>Totales</strong></td>
				%totalFinal = 0
				%for i in range(1, 13):
					%totalMes = 0
					%for j in range(0, len(categoriasP)):
						%totalMes = totalMes + resultados[j][i]
					%end
					<td align="center"><strong>{{totalMes}}</strong></td>
					%totalFinal = totalFinal + totalMes
				%end
				<td align="center"><strong>{{totalFinal}}</strong></td>
			</tr>	    
		</table><br>
	%elif opcionr == 4:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        %for i in range(0, len(listaSemestres)):
		       		<td align="center"><strong>{{listaSemestres[i]}}</strong></td>
		        %end
		        <td align="center"><strong>Totales</strong></td>	            
			</tr>

			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				<tr>
					<td><strong>{{categoria}}</strong></td>
					%sum = 0
					%for j in range(0, 2):
						%sum = sum + resultados[j][i]
						<td align="center">{{resultados[j][i]}}</td>
					%end
					<td align="center"><strong>{{sum}}</strong></td>
				</tr>
			%end
			<tr>
				<td><strong>Totales</strong></td>
				%totalFinal = 0
				%for i in range(0, 2):
					%totalSemestre = 0
					%for j in range(0, len(categoriasP)):
						%totalSemestre = totalSemestre + resultados[i][j]
					%end
					<td align="center"><strong>{{totalSemestre}}</strong></td>
					%totalFinal = totalFinal + totalSemestre
				%end
				<td align="center"><strong>{{totalFinal}}</strong></td>
			</tr>	    
		</table><br>
	%elif opcionr == 5:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        %for i in range(0, len(listaTrimestresBimodal)):
		       		<td align="center"><strong>{{listaTrimestresBimodal[i]}}</strong></td>
		        %end
		        <td align="center"><strong>Totales</strong></td>         
			</tr>

			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				<tr>
					<td><strong>{{categoria}}</strong></td>
					%sum = 0
					%for j in range(0, 4):
						%sum = sum + resultados[j][i]
						<td align="center">{{resultados[j][i]}}</td>
					%end
					<td align="center"><strong>{{sum}}</strong></td>
				</tr>
			%end
			<tr>
				<td><strong>Totales</strong></td>
				%totalFinal = 0
				%for i in range(0, 4):
					%totalTrimestre = 0
					%for j in range(0, len(categoriasP)):
						%totalTrimestre = totalTrimestre + resultados[i][j]
					%end
					<td align="center"><strong>{{totalTrimestre}}</strong></td>
					%totalFinal = totalFinal + totalTrimestre
				%end
				<td align="center"><strong>{{totalFinal}}</strong></td>
			</tr>	    
		</table><br>
	%elif opcionr == 6:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        %for i in range(0, len(listaTrimestresEstandar)):
		       		<td align="center"><strong>{{listaTrimestresEstandar[i]}}</strong></td>
		        %end
		        <td align="center"><strong>Totales</strong></td>         
			</tr>

			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				<tr>
					<td><strong>{{categoria}}</strong></td>
					%sum = 0
					%for j in range(0, 4):
						%sum = sum + resultados[j][i]
						<td align="center">{{resultados[j][i]}}</td>
					%end
					<td align="center"><strong>{{sum}}</strong></td>
				</tr>
			%end
			<tr>
				<td><strong>Totales</strong></td>
				%totalFinal = 0
				%for i in range(0, 4):
					%totalTrimestre = 0
					%for j in range(0, len(categoriasP)):
						%totalTrimestre = totalTrimestre + resultados[i][j]
					%end
					<td align="center"><strong>{{totalTrimestre}}</strong></td>
					%totalFinal = totalFinal + totalTrimestre
				%end
				<td align="center"><strong>{{totalFinal}}</strong></td>
			</tr>	    
		</table><br>
	%elif opcionr == 7:
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        %for i in range(vAnualF[0], (vAnualF[1]+ 1)):
		       		<td align="center"><strong>{{i}}</strong></td>
		        %end
		        <td align="center"><strong>Totales</strong></td>	            
			</tr>

			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				<tr>
					<td><strong>{{categoria}}</strong></td>
					%sum = 0
					%for j in range(0, len(vAnualF)):
						%sum = sum + resultados[j][i]
						<td align="center">{{resultados[j][i]}}</td>
					%end
					<td align="center"><strong>{{sum}}</strong></td>
				</tr>
			%end
			<tr>
				<td><strong>Totales</strong></td>
				%totalFinal = 0
				%for i in range(0, len(vAnualF)):
					%totalAno = 0
					%for j in range(0, len(categoriasP)):
						%totalAno = totalAno + resultados[i][j]
					%end
					<td align="center"><strong>{{totalAno}}</strong></td>
					%totalFinal = totalFinal + totalAno
				%end
				<td align="center"><strong>{{totalFinal}}</strong></td>
			</tr>	    
		</table><br>
	%else:
		<!--<h3>Personalizada</h3> -->
		<table class="table table-hover" margin="auto">
		    <tr>
		   	  	<td><strong>Categoria</strong></td>
		        <td align="center"><strong>Ocurrencias</strong></td>  
		    </tr>
			%for i in range(0, len(categoriasP)):
				%categoria = categoriasP[i].entregarEtiqueta()
				<tr>
					<td><strong>{{categoria}}</strong></td>
					<td align="center">{{resultados[i]}}</td>
				</tr>					
			%end			
		</table><br>
	%end
</div>



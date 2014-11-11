%if periodos[0] == 1:
	<table class="table table-hover">
	<tr>
		<td align=" center"><strong>Día</strong></td>
	    %for i in range(1, ((len(listaMeses) / 2) + 1)):
	  		<td align="center"><strong>{{listaMeses[i]}}</strong></td>
	    %end
	    <td align="center"><strong>Totales</strong></td>	    
	</tr>
	%for i in range(1, 32):
		<tr>
		<td align="center"><strong>{{i}}</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			%try:
				<td align="center">{{acumulado[j][0][i]}}</td>
			%except IndexError:
				<td align="center">-</td>
			%end
		%end			
		</tr>		
	%end
	<tr>
		<td align="center"><strong>Total</strong></td>
		%total = 0
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			%total = total + acumulado[j][1].entregarSumatoria()
			<td align="center">{{acumulado[j][1].entregarSumatoria()}}</td>
		%end
	</tr>

	<tr>
		<td align="center"><strong>Total Anual:</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			<td align="center">-</td>
		%end
		<td align="center"><strong>{{total}}</strong></td>
	</tr>

	<tr>
		<td align="center"><strong>Máximo</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			<td align="center">{{acumulado[j][1].entregarMaximo()}}</td>
		%end
	</tr>
	<tr>
		<td align="center"><strong>Mínimo</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			<td align="center">{{acumulado[j][1].entregarMinimo()}}</td>
		%end
	</tr>
	<tr>
		<td align="center"><strong>Promedio</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			%b = '%.1f' %acumulado[j][1].entregarPromedio()
			<td align="center">{{b}}</td>
		%end
	</tr>    
	</table>
%else:
	<table class="table table-hover">
	<tr>
		<td align=" center"><strong>Día</strong></td>
	    %for i in range(7, len(listaMeses)):
	  		<td align="center"><strong>{{listaMeses[i]}}</strong></td>
	    %end
	    <td align="center"><strong>Totales</strong></td>	    
	</tr>
	%for i in range(1, 32):
		<tr>
		<td align="center"><strong>{{i}}</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			%try:
				<td align="center">{{acumulado[j][0][i]}}</td>
			%except IndexError:
				<td align="center">-</td>
			%end
		%end			
		</tr>		
	%end
	<tr>
		<td align="center"><strong>Total</strong></td>
		%total = 0
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			%total = total + acumulado[j][1].entregarSumatoria()
			<td align="center">{{acumulado[j][1].entregarSumatoria()}}</td>
		%end
	</tr>

	<tr>
		<td align="center"><strong>Total Anual:</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			<td align="center">-</td>
		%end
		<td align="center"><strong>{{total}}</strong></td>
	</tr>

	<tr>
		<td align="center"><strong>Máximo</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			<td align="center">{{acumulado[j][1].entregarMaximo()}}</td>
		%end
	</tr>
	<tr>
		<td align="center"><strong>Mínimo</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			<td align="center">{{acumulado[j][1].entregarMinimo()}}</td>
		%end
	</tr>
	<tr>
		<td align="center"><strong>Promedio</strong></td>
		%for j in range(1, ((len(listaMeses) / 2) + 1)):
			%b = '%.1f' %acumulado[j][1].entregarPromedio()
			<td align="center">{{b}}</td>
		%end
	</tr>    
	</table>
%end
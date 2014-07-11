<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3>Eventos Encontrados</h3>
    
	  	     <table class="table table-hover">
		        <tr align="center">
		    	  	<td><strong>Evento</strong></td>
		            <td><strong>Fecha</strong></td>
		            <td><strong>Hora de Inicio</strong></td>
		            <td><strong>Hora de Fin</strong></td>
		            <td><strong>Magnitud (mm)</strong></td>
		            <td><strong>Duración (min)</strong></td>
		            <td><strong>Intensidad Media (mm/h)</strong></td>
		            <td><strong>Intensidad Maxima</strong></td>
		            <td><strong>Categoria Evento</strong></td>
		            <td><strong>Jornada Evento</strong></td>
		            <td><strong>Observaciones</strong></td>
		        </tr>
		        	%cont=1
		           %for evento in coleccionEventos:
		        	<tr align="center">
			            <td>{{cont}}</td>
			            <td>{{evento.entregarFecha()}}</td>
			            <td>{{evento.entregarHoraInicio()}}</td>
			            <td>{{evento.entregarHoraFin()}}</td>
			            <td>{{evento.entregarMagnitud()}}</td>
			            <td>{{int(evento.entregarDuracion())}}</td>
			            %b = '%.1f' %evento.entregarIntensidadMedia()
			            <td>{{b}}</td>
			            <td>{{evento.entregarIntensidadMaxima()}}</td>
			            <td>{{evento.entregarTipoLluvia()}}</td>
			            <td>{{evento.entregarJornadaEvento()}}</td>
			            <td>{{evento.entregarObservaciones()}}</td>
			            %cont+=1			            	
		          	</tr>
		          	%end
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
<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	
	<div class="row">
		<div class="col-xs-12 col-md-8">			
			<div id="eventos">
				<h3>Eventos Encontrados</h3>
				<h4>{{cadenaParametrizada}}</h4>
				<br>
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
			<div align="center" style="padding-top:0.3cm">
				<p>
					<button type="button" class="btn btn-default"><a download="Eventos{{cadenaParametrizada}}.xls" href="#" onclick="return ExcellentExport.excel(this, 'eventos', 'eventos');">Reporte Excel</a></button>
					<button type="button" class="btn btn-default" id="btnreportevent"><a href="#">Reporte PDF</a></button>					
				</p>																
			</div>		
	  	</div>	  	
	</div>

	<script>
	$("#btnreportevent").click(function(){
		var direccion = prompt("Por favor Ingrese la direccion donde se guardara el reporte");
		var nombreArchivo = prompt("Ingrese el nombre que desea asginarle al reporte");
		var post_data = {'dir': direccion, 'namefile': nombreArchivo};
		$.ajax
      	({
	        type: 'POST',
	        url : 'reporteEventos',
	        data: JSON.stringify(post_data),
	        contentType: "application/json; charset=utf-8",
	        dataType: 'json',
	        success: function(data){
	       	    $.each(data, function(index,  value){
	        	    alert(value);
	            	$(location).attr('href', '/menuinicio')
	            });
	        }
	    });
	});
	</script>

</body>
</html>
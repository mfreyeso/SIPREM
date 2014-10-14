<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>	
	%include('header.tpl')
	%include('aside.tpl')
	<div class="row">
		<div class="col-xs-10 col-md-8">
			<div class="panel-heading">
				<h3><b>Administración de Jornadas y Categorias</b></h3>
			</div>
			<div class="panel-body">
				<p align="justify">
					<h4>Cree, modifique y elimine jornadas y categorias que luego podra asociar
					a una configuración de ejecución del sistema.</h4>				
				</p><br>

				<div class="panel panel-success">
					<div class="panel-heading">
						<h4><b>Categorias y Jornadas Existentes</b></h4>
					</div>

					<p></p><br>

					<div id="configExistentes">
						<table class="table table-hover" margin="auto">
							<tr>
								<td align="center"><strong>Categorias</strong></td>
								<td align="center"><strong>Jornadas</strong></td>
							</tr>
							<tr>
								<td>
									<table class="table table-hover" margin="auto">
								    	<tr>
								    		<td align="center"><strong>Categoria</strong></td>
								    		<td align="center"><strong>Metrica</strong></td>					    		
								    	</tr>
								    	%for categoria in categorias:
								    		<tr>
									    		<td align="center">{{categoria.entregarEtiqueta()}}</td>
									    		<td align="center">{{categoria.entregarMagnitud()}}</td>		    		
								    		</tr>
				                		%end
				                	</table>									
								</td>
								<td>
									<table class="table table-hover" margin="auto">
								    	<tr>
								    		<td align="center"><strong>Jornada</strong></td>
								    		<td align="center"><strong>Hora Inicio</strong></td>
								    		<td align="center"><strong>Hora Fin</strong></td>					    		
								    	</tr>
								    	%for jornada in jornadas:
								    		<tr>
									    		<td align="center">{{jornada.entregarEtiquetaJornada()}}</td>
									    		<td align="center">{{jornada.entregarHoraInicio()}}</td>
									    		<td align="center">{{jornada.entregarHoraFin()}}</td>		    		
								    		</tr>
				                		%end
				                	</table>
								</td>
							</tr>
						</table>						
					</div>				
				</div>

				<div class="panel panel-default">
					<div class="panel-heading">
						<h3>Categorias y Jornadas</h3>
					</div>
					<br>
					<div id="admjc" class="panel-body">
						%include('formsconfiguracionjc.tpl')
					</div>				
				</div>				
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
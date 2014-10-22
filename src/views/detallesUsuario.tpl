<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>
	%include('header.tpl')
	%include('aside.tpl')	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<div class="panel panel-primary">
					<div class="panel-heading">
						<h4><b>Información de Usuario</b></h4>
					</div>
					<br>
					<div class="panel-body">
						<div class="col-md-6">
							<table class="table table-striped">
								<tr>
									<td><h5>Documento Identificación:</h5></td>
									<td><h5>{{identificacion}}</h5></td>
								</tr>
								<tr>
									<td><h5>Nombre:</h5></td>
									<td><h5>{{nombre}}</h5></td>
								</tr>
								<tr>
									<td><h5>Apellidos:</h5></td>
									<td><h5>{{papellido}} {{sapellido}}</h5></td>
								</tr>
								<tr>
									<td><h5>Email:</h5></td>
									<td><h5>{{mail}}</h5></td>
								</tr>				
							</table>				
						</div>
						<div class="col-md-6">
							<table class="table table-striped">					
								<tr>
									<td><h5>Tipo de Usuario:</h5></td>
									<td><h5>{{rolusuario}}</h5></td>
								</tr>
								<tr>
									<td><h5>Usuario de Acceso:</h5></td>
									<td><h5>{{accuser}}</h5></td>
								</tr>
							</table>
						</div>
					</div>				
			</div>
		</div>
		%if rolid == 1:
		<div class="row">
			<div class="col-xs-12 col-md-8">
				<h3>Administrar Usuarios</h3><br>
				<ul id="myTab" class="nav nav-tabs">
				   <li class="active">
				      <a href="#addu" data-toggle="tab" class="btn btn-primary">Añadir Usuario</a></li>
				   <li><a href="#editu" data-toggle="tab" class="btn btn-primary">Editar Usuario</a></li>
				   <li><a href="#desu" data-toggle="tab" class="btn btn-primary">Desactivar Usuario</a></li>			   
				</ul>
				<div id="myTabContent" class="tab-content">
				   <div class="tab-pane fade in active" id="addu">
				      <div class="col-md-6">
				         <form role="form" style="padding:0.5cm" action="/crearconfiguracion" method="POST">
				            <div class="form-group" style="padding-right:2cm">
				               <label for="nombre">Nombre Configuración</label>
				               <input type="text" class="form-control" id="cnombrec" name="cnombrec" 
				                  placeholder="Ejemplo: Configuracion Dos">
				            </div>
				            <div class="form-group" style="padding-right:2cm">
				               <label for="tiempo">Diferencial de Tiempo Precipitación (min.)</label>
				               <input class="form-control" type="number" id="cdfprec" name="cdfprec" min="5">
				            </div>
				            <div class="form-group" style="padding-right:2cm">
				               <label for="tiempo">Posición Precipitación (Archivo Plano)</label>
				               <input class="form-control" type="number" id="cpsprec" name="cpsprec" min="0">
				            </div>                     
				         </form>         
				      </div>
				      <div class="col-md-6">
				         <div class="form-group" align="center" style="padding:2.5cm" align="center">
				            <!--<button type="button" id="btncrearco" class="btn btn-success btn-lg">Crear</button>-->
				            <button id="btncrearconfiguracion" class="btn btn-success btn-lg">Crear</button>
				         </div>   
				      </div>
				   </div>

				   <div class="tab-pane fade" id="editu">
				      <div class="col-md-6">
				      </div>
				      <div class="col-md-6">
				      </div>   
				   </div>

				   <div class="tab-pane fade" id="desu">
				      <div class="col-md-6">
				      </div>
				      <div class="col-md-6">
				      </div>      
				   </div>
				</div>
			</div>			
		</div>
		%end
	</div>	
</body>
</html>
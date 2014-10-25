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
						<h4>Información de Usuario</h4>
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
				         <form role="form" style="padding:0.5cm">
				            <div class="form-group" style="padding-right:2cm">
				               <label for="nombre">Nombres</label>
				               <input type="text" class="form-control" id="unombres" name="unombres" 
				                  placeholder="Ejemplo: Alexander">
				            </div>
				            <div class="form-group" style="padding-right:2cm">
				               <label for="papellido">Primer Apellido</label>
				               <input class="form-control" type="text" id="upapellido" name="usapellido">
				            </div>
				            <div class="form-group" style="padding-right:2cm">
				               <label for="sapellido">Segundo Apellido</label>
				               <input class="form-control" type="text" id="usapellido" name="usapellido">
				            </div>
				            <div class="form-group" style="padding-right:2cm">
				               <label for="sapellido">Numero Identificación</label>
				               <input class="form-control" type="text" id="uidentificacion" name="uidentificacion">
				            </div>
				            <div class="form-group" style="padding-right:2cm">
				               <label for="urol">Tipo Usuario</label>
								<select class="form-control" name="urol" id="urol">
									%for rol in roles:
										<option value="{{rol.id}}">{{rol.tipo}}</option>
									%end
								</select>
							</div>
				         </form>         
				      </div>
				      <div class="col-md-6">
				      		<form role="form" style="padding:0.5cm">
				      			<div class="form-group" style="padding-right:2cm">
				                <label for="sapellido">Email</label>
				                <input class="form-control" type="email" id="uemail" name="uemail">
					            </div>
					            <div class="form-group" style="padding-right:2cm">
					               <label for="sapellido">Telefono</label>
					               <input class="form-control" type="text" id="utelefono" name="utelefono">
					            </div>
					            <div class="form-group" style="padding-right:2cm">
					               <label for="sapellido">Usuario de Acceso</label>
					               <input class="form-control" type="text" id="unameuser" name="unameuser">
					            </div>
					            <div class="form-group" style="padding-right:2cm">
					               <label for="sapellido">Contraseña</label>
					               <input class="form-control" type="text" id="upassword" name="upassword">
					            </div>
					            <div class="form-group" style="padding-right:2cm">
					               <label for="sapellido">Confirmar Contraseña</label>
					               <input class="form-control" type="text" id="urpassword" name="urpassword">
					            </div>

					         <div class="form-group" align="center" style="padding:0.5cm" align="center">
					            <button id="btncrearusu" class="btn btn-primary">Añadir</button>
					         </div>
				      		</form>				      	  	   
				      	</div>
				 	</div>
				   	<div class="tab-pane fade" id="editu">
				      <div class="col-md-6">
				      	<div>
				      		
				      	</div>
				      	<div id="eformuser" style="display:none">
				      		
				      	</div>
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
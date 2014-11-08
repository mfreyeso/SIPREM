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
				   		<div class="row">
				   			<div class="col-md-6">
						      	<div>
						      		<div class="form-group" align="center" style="padding:1.3cm" align="center">
							            <button id="btnloadusu" class="btn btn-primary">Cargar Usuarios</button>
							        </div>
						      	</div>
						      	<div id="loadusers" style="display:none">					      		
						      	</div>
					      	</div>				   			
				   		</div>
				   		<div class="row">
				   			<div id="formedituser" style="display:none">
				   				<div class="col-md-6">
							         <form role="form" style="padding:0.5cm">
							            <div class="form-group" style="padding-right:2cm">
							               <label for="nombre">Nombres</label>
							               <input type="text" class="form-control" id="eunombres" name="unombres" 
							                  placeholder="Ejemplo: Alexander">
							            </div>
							            <div class="form-group" style="padding-right:2cm">
							               <label for="papellido">Primer Apellido</label>
							               <input class="form-control" type="text" id="eupapellido" name="usapellido">
							            </div>
							            <div class="form-group" style="padding-right:2cm">
							               <label for="sapellido">Segundo Apellido</label>
							               <input class="form-control" type="text" id="eusapellido" name="usapellido">
							            </div>
							            <div class="form-group" style="padding-right:2cm">
							               <label for="sapellido">Numero Identificación</label>
							               <input class="form-control" type="text" id="euidentificacion" name="uidentificacion">
							            </div>
							            <div class="form-group" style="padding-right:2cm">
							               <label for="urol">Tipo Usuario</label>
											<select class="form-control" name="urol" id="eurol">
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
							                <input class="form-control" type="email" id="euemail" name="uemail">
								            </div>
								            <div class="form-group" style="padding-right:2cm">
								               <label for="sapellido">Telefono</label>
								               <input class="form-control" type="text" id="eutelefono" name="utelefono">
								            </div>
								            <div class="form-group" style="padding-right:2cm">
								               <label for="sapellido">Usuario de Acceso</label>
								               <input class="form-control" type="text" id="eunameuser" name="unameuser">
								            </div>
								            <div class="form-group" style="padding-right:2cm">
								               <label for="sapellido">Contraseña</label>
								               <input class="form-control" type="text" id="eupassword" name="upassword">
								            </div>
								            <div class="form-group" style="padding-right:2cm">
								               <label for="sapellido">Confirmar Contraseña</label>
								               <input class="form-control" type="text" id="eurpassword" name="urpassword">
								            </div>

								         <div class="form-group" align="center" style="padding:0.5cm" align="center">
								            <button id="btneditusu" class="btn btn-primary">Editar</button>
								         </div>
							      		</form>				      	  	   
							    </div>	
				   			</div>
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
	<script>
		$("#btncrearusu").click(function(){
			var nombresUsuario = $("#unombres").val();
			var primerApellidoUsuario = $("#upapellido").val();
			var segundoApellidoUsuario = $("#usapellido").val();
			var identificacionUsuario = $("#uidentificacion").val();
			var rolUsuario = $("#urol").val();
			var utelefono = $("#utelefono").val();
			var email = $("#uemail").val();
			var unameUser = $("#unameuser").val();
			var upasswordUsuario = $("#upassword").val();
			var urpasswordUsuario = $("#urpassword").val();			
			if(upasswordUsuario == urpasswordUsuario){
				alert("Las constraseñas ingresadas no coinciden. Intente de Nuevo.");
				$(location).attr('href', '/usuariodetalles');
			}
			else{
				var post_data = {"identificacion": identificacionUsuario};
				$.ajax(
					{
						type : 'POST',
					    url : 'validarUsuario',
					    data : JSON.stringify(post_data),
					    contentType : "application/json; charset=utf-8",
					    dataType: 'json',
					    success : function(data){
					    	if (parseInt(data['efect']) == 0){
					    		alert("El usuario ya existe en el sistema.");
					    	}
					    	else{
					    		var post_dataIn = {'nombres': nombresUsuario, 'papellido': primerApellidoUsuario, 'sapellido': segundoApellidoUsuario, 'identificacion': identificacionUsuario, 'rol': rolUsuario, 'telefono': utelefono, 'email': email, 'nameuser': unameUser, 'password': upasswordUsuario};
					    		$.ajax(
					    			{
					    				type : 'POST',
									    url : 'crearUsuario',
									    data : JSON.stringify(post_dataIn),
									    contentType : "application/json; charset=utf-8",
									    dataType: 'json',
									    success : function(data){
									    	$.each(data, function(index, value){
								               alert(value);
								            });
								            $(location).attr('href', '/usuariodetalles');
									    }
					    			});					    			
					    	}
					    }
					});
			}
		});

		$("#loadusers").click(function(){
			var activos = 1;
			var post_data = {'estado': activos};
			$.ajax({
				type : 'POST',
		        url : 'obtenerUsuarios',
		        data : JSON.stringify(post_data),
		        contentType : "application/json; charset=utf-8",
		        dataType : 'json',
		        success : function(data){
		        	if (parseInt(data['efect']) == 1){
		        		var cadenaInicial ="<form role='form'><div class='form-group'>\
			            <label for='estacion'>Estación</label>\
			            <select class='form-control' name='ususedit' id='ususedit'>";
			            var cadenaFinal = "</select></div></form>";
			            var cadenaCentro = " ";
			            $(data.usuarios).each(function(index, value){
			              var opcion = "<option value='"+value['identificacion']+"'>"+value['nombres']+value['apellidos']+"</option>";
			              cadenaCentro+=opcion;
			            });
			            var cadena = cadenaInicial + cadenaCentro + cadenaFinal;
			            $("#loadusers").append(cadena);
			            var btneditarusuarios = "<div class='form-group' align='center' style='padding:0.5cm'\
			            align='center'><button id='btnformeditusu' class='btn btn-primary'>Cargar Formulario</button>\
			            </div>";
			            $("#loadusers").append(btneditarusuarios);
			            $("#loadusers").show();
		        	}
		        	else{
		        		alert("No exiten otros usuarios activos.");
		        	}		        	
		        }
			});
		});
		
		$("#btnformeditusu").click(function(){
			var usuarioSeleccionado = $("ususedit").val();
			var post_data = {'identificacion': usuarioSeleccionado};
			$.ajax({
				type : 'POST',
		        url : 'obtenerUsuarios',
		        data : JSON.stringify(post_data),
		        contentType : "application/json; charset=utf-8",
		        dataType : 'json',
		        success : function(data){
		        	if (parseInt(data['efect']) == 1){
		        		usuario = data['usuario'];
		        		nombres = usuario['nombre'];
		        		papellido = usuario['papellido'];
		        		sapellido = usuario['sapellido'];
		        		telefono = usuario['telefono'];
		        		email = usuario['email'];
		        		nameuser = usuario['nameuser'];
		        		clave = usuario['clave'];

		        		$("#eunombres").attr("value", nombres);
		        		$("#eupapellido").attr("value", papellido);
		        		$("#eusapellido").attr("value", sapellido);
		        		$("#eutelefono").attr("value", telefono);
		        		$("#euemail").attr("value", email);
		        		$("#eunameuser").attr("value", nameuser);
		        		$("#eupassword").attr("value", clave);
		        		$("#eurpassword").attr("value", clave);
		        		$("#formedituser").show();
		        	}
		        	else{
		        		alert("Ocurrio un error en el sistema, Intente de nuevo.");
		        	}		        	
		        }
			});			
		});

		$("#btneditusu").click(function(){


		});
	</script>	
</body>
</html>
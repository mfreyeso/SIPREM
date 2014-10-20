<ul id="myTab" class="nav nav-tabs">
   <li class="active">
      <a href="#creatc" data-toggle="tab" class="btn btn-success">Añadir Configuración</a></li>
   <li><a href="#editc" data-toggle="tab" class="btn btn-success">Editar Configuración</a></li>
   <li><a href="#actc" data-toggle="tab" class="btn btn-success">Activar Configuración</a></li>
   
</ul>
<div id="myTabContent" class="tab-content">
   <div class="tab-pane fade in active" id="creatc">
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

   <div class="tab-pane fade" id="editc">
      <div class="col-md-6">
         <div class="form-group" style="padding-top:0.9cm; padding-right:1.5cm">
            <select name="editconfiguracion" id="editconfiguracion" class="form-control">
               %for configuracion in configuraciones:
               <option value="{{configuracion.id}}">{{configuracion.nombre}}</option>
               %end
            </select>            
         </div>

         <div class="form-group" style="padding-top:0.2cm">
            <button type="button" id="btncargarconfiguracion" class="btn btn-success">Cargar</button>
         </div>

         <div id="catjors">

            
         </div>

         <div id="formeditconf" style="display:none">
            <form role="form">
               <div class="form-group" style="padding-right:1cm">
                  <label for="nombre">Nombre Configuración</label>
                  <input type="text" class="form-control" id="enombrec" name="enombrec" 
                     placeholder="Ejemplo: Configuracion Dos">
               </div>
               <div class="form-group" style="padding-right:1cm">
                  <label for="tiempo">Diferencial de Tiempo Precipitación (min.)</label>
                  <input class="form-control" type="number" id="edfprec" name="edfprec" min="5">
               </div>
               <div class="form-group" style="padding-right:1cm">
                  <label for="tiempo">Posición Precipitación (Archivo Plano)</label>
                  <input class="form-control" type="number" id="epsprec" name="epsprec" min="0">
               </div>                     
            </form>
         </div>         
      </div>
      <div class="col-md-6">
         <div class="row" style="padding-top:0.5cm; padding-left:0.2cm; padding-right:0.2cm">
            <h4>Añadir Categorias</h4>
            <form role="form">
               <div class="form-group">
                  <label for="nombre">Categoria</label>
                  <select name="addcat" id="addcat" class="form-control">
                     %for cat in categorias:
                     <option value="{{cat.entregarIdentificacion()}}">{{cat.entregarEtiqueta()}}</option>
                     %end
               </select>
               </div>
               <div class="form-group" style="padding-top:0.2cm" align="center">
                  <button type="button" id="btnaddcat" class="btn btn-success">Añadir</button>
               </div>                   
            </form>
         </div>
         <div class="row" style="padding-top:0.1cm; padding-left:0.2cm; padding-right:0.2cm">
            <h4>Añadir Jornadas</h4>
               <form role="form">
               <div class="form-group">
                  <label for="nombre">Jornadas</label>
                  <select name="addjor" id="addjor" class="form-control">
                     %for jor in jornadas:
                     <option value="{{jor.entregarIdentificacion()}}">{{jor.entregarEtiquetaJornada()}}</option>
                     %end
               </select>
               </div>
               <div class="form-group" style="padding-top:0.2cm" align="center">
                  <button type="button" id="btnaddjor" class="btn btn-success">Añadir</button>
               </div>                   
            </form>
         </div>                  
      </div>   
   </div>
   <div class="tab-pane fade" id="actc">
      <div class="col-md-6">
         <div class="form-group" style="padding:1cm">
            <select name="actconfiguracion" id="actconfiguracion" class="form-control">
               %for configuracion in configuraciones:
               <option value="{{configuracion.id}}">{{configuracion.nombre}}</option>
               %end
            </select>            
         </div>         
      </div>
      <div class="col-md-6">
         <div class="form-group" style="padding: 1cm" align="center">
            <button class="btn btn-success" id="btnactconfiguracion">
               Activar Configuración
            </button>            
         </div>
      </div>      
   </div>   
</div>

<script>
   $("#btnactconfiguracion").click(function(){
      var configuracion = $("#actconfiguracion").val();
      var post_data = {'ideconf': configuracion};
      $.ajax
      ({
         type: 'POST',
         url : 'cargarConfiguracion',
         data: JSON.stringify(post_data),
         contentType: "application/json; charset=utf-8",
         dataType: 'json',
         success: function(data){
            $.each(data, function(index,  value){
               alert(value);
               $(location).attr('href', '/tconfiguracion')
            });
         }
      });
   });

   $("#btncrearconfiguracion").click(function(){
      var nombreConfiguracion = $("#cnombrec").val();
      var posPrecipitacion = $("#cpsprec").val();
      var dfPrecipitacion = $("#cdfprec").val();
      var post_data = {'nombre': nombreConfiguracion, 'posicion': posPrecipitacion, 'diferencial': dfPrecipitacion};
      $.ajax
      ({
         type : 'POST',
         url : 'crearConfiguracion',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success :  function(data){
            $.each(data, function(index, value){
               alert(value);
            });
            $(location).attr('href', '/tconfiguracion');
         }
      });
   });

   $("#btncargarconfiguracion").click(function(){
      var configuracion = $("#editconfiguracion").val();
      var post_data = {'ideconf': configuracion};
      $.ajax
      ({
         type : 'POST',
         url : 'obtenerConfiguracion',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success: function(data){
          if(parseInt(data['efect']) == 1){
            var configuracionObtenida = data['configuracion'];
            var nombreConfiguracion = configuracionObtenida['nombre'];
            var posicion = configuracionObtenida['posicion'];
            var diferencial = configuracionObtenida['diferencial'];
            $("#enombrec").attr("placeholder", nombreConfiguracion);
            $("#epsprec").attr("value", posicion);
            $("#edfprec").attr("value", diferencial);
            $("#formeditconf").show();

            var tablaJornadasCategoriasInicio = "<table class='table table-hover' margin='auto'>\
                     <tr>\
                        <td align='center'><strong>Categorias</strong></td>\
                        <td align='center'><strong>Jornadas</strong></td>\
                     </tr>\
                     <tr>\
                     <td>";
           var tablaCategoriasInicio =" <table class='table table-hover' margin='auto'>\
                                 <tr>\
                                 <td align='center'><strong>Categoria</strong></td>\
                                 <td align='center'><strong>Metrica</strong></td>\
                                 </tr>";

            var tablaCategoriasFin = "</table></td>";

            var tablaJornadasInicio = "<td><table class='table table-hover' margin='auto'>\
                                 <tr>\
                                 <td align='center'><strong>Jornada</strong></td>\
                                 <td align='center'><strong>Hora Inicio</strong></td>\
                                 <td align='center'><strong>Hora Fin</strong></td>\
                                 </tr>";

            var tablaJornadasFin = "</table>";
            var tablaJornadasCategoriasFin = "</td></tr></table>";


                          
                              %for categoria in categorias:
                                 <tr>
                                    <td align='center'>{{categoria.entregarEtiqueta()}}</td>
                                    <td align='center'>{{categoria.entregarMagnitud()}}</td>             
                                 </tr>
                                 %end
                                                       
                        
                              %for jornada in jornadas:
                                 <tr>
                                    <td align='center'>{{jornada.entregarEtiquetaJornada()}}</td>
                                    <td align='center'>{{jornada.entregarHoraInicio()}}</td>
                                    <td align='center'>{{jornada.entregarHoraFin()}}</td>             
                                 </tr>
                                 %end
                              
              

            
         }
          else{
            alert("La configuracion no pudo ser cargada en el sistema, Intente de Nuevo.");
          }
         }
      });
   });

   $("#btnaddcat").click(function(){
      var identificacionConfiguracion = $("#editconfiguracion").val();
      var identificacionCategoria = $("#addcat").val();
      var post_data = {'idcat': identificacionCategoria, 'idconf': identificacionConfiguracion};
      $.ajax
      ({
         type : 'POST',
         url : 'adicionarCategoria',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success :  function(data){
            $.each(data, function(index, value){
               alert(value);
            });
            //$(location).attr('href', '/tconfiguracion');
         }
      });
   });

   $("#btnaddjor").click(function(){
      var identificacionConfiguracion = $("#editconfiguracion").val();
      var identificacionJornada = $("#addjor").val();
      var post_data = {'idjor': identificacionJornada, 'idconf': identificacionConfiguracion};
      $.ajax
      ({
         type : 'POST',
         url : 'adicionarJornada',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success :  function(data){
            $.each(data, function(index, value){
               alert(value);
            });
            //$(location).attr('href', '/tconfiguracion');
         }
      });
   });   
</script>


<!--Administración de Categorias -->
<div class="row">
   <div class="col-md-8">
   <h3>Administración de Categorias</h3>
   <br>
      <ul id="myTab" class="nav nav-tabs">
         <li class="active">
            <a href="#creatcat" data-toggle="tab" class="btn btn-info">Añadir Categoria</a></li>
         <li><a href="#editcat" data-toggle="tab" class="btn btn-info">Editar Categoria</a></li>
         <li><a href="#delcat" data-toggle="tab" class="btn btn-info">Eliminar Categoria</a></li>      
      </ul>

      <div id="myTabContent" class="tab-content">
         <div class="tab-pane fade in active" id="creatcat">
            <div class="col-md-6">
               <form role="form" style="padding-top:0.5cm" action="/crearconfiguracion" method="POST">
                  <div class="form-group" style="padding-right:2cm">
                     <label for="nombre">Etiqueta Categoria</label>
                     <input type="text" class="form-control" id="cetiquetacat" name="cetiquetacat" 
                        placeholder="Lluvia Semifuerte">
                  </div>
                  <div class="form-group" style="padding-right:2cm">
                     <label for="tiempo">Métrica</label>
                     <input class="form-control" type="text" id="cmcat" name="cmcat">
                  </div>                                   
               </form>
               <div class="form-group" style="padding-top:0.2cm">
                  <!--<button type="button" id="btncrearco" class="btn btn-success btn-lg">Crear</button>-->
                  <button id="btncreatecat" class="btn btn-info">Crear</button>
               </div>
            </div>         
         </div>
         <div class="tab-pane fade" id="editcat">
            <div class="col-md-6">

               <div class="form-group" style="padding-top:1cm">
                  <select name="editidcat" id="editidcat" class="form-control">
                     %for categoria in categorias:
                     <option value="{{categoria.entregarIdentificacion()}}">{{categoria.entregarEtiqueta()}}</option>
                     %end
                  </select>            
               </div>

               <div class="form-group" style="padding-top:0.2cm">
                  <button type="button" id="btnloadcat" class="btn btn-info">Cargar</button>
               </div>

               <div id="formeditcat" style="display:none">
                  <form role="form">
                     <div class="form-group" style="padding-right:1cm">
                        <label for="nombre">Etiqueta Categoria</label>
                        <input type="text" class="form-control" id="edetiquetacat" name="edetiquetacat" 
                           placeholder="Ejemplo: Lluvia Semifuerte">
                     </div>
                     <div class="form-group" style="padding-right:1cm">
                        <label for="tiempo">Métrica</label>
                        <input class="form-control" type="text" id="edmetricat" name="edmetricat">
                     </div>                                      
                  </form>
                  <div class="form-group" style="padding-top:0.2cm">
                     <!--<button type="button" id="btncrearco" class="btn btn-success btn-lg">Crear</button>-->
                     <button id="btneditcat" class="btn btn-success btn-info">Editar</button>
                  </div>
               </div>         
            </div>         
         </div>
         <div class="tab-pane fade" id="delcat">
            <div class="col-md-6">
               <div class="form-group" style="padding-top:1cm">
                  <select name="deletecat" id="deletecat" class="form-control">
                     %for categoria in categorias:
                     <option value="{{categoria.entregarIdentificacion()}}">{{categoria.entregarEtiqueta()}}</option>
                     %end
                  </select>            
               </div>
               <div class="form-group" style="padding-top: 0.2cm">
                  <button class="btn btn-info" id="btndelcat">
                     Eliminar
                  </button>            
               </div>            
            </div>               
         </div>   
      </div>   
   </div>   
</div>
<!--Administración de Jornadas -->
<div class="row">
   <div class="col-md-8">
   <h3>Administración de Jornadas</h3>
   <br>
      <ul id="myTab" class="nav nav-tabs">
         <li class="active">
            <a href="#creatjor" data-toggle="tab" class="btn btn-warning">Añadir Jornada</a></li>
         <li><a href="#editjor" data-toggle="tab" class="btn btn-warning">Editar Jornada</a></li>
         <li><a href="#deljor" data-toggle="tab" class="btn btn-warning">Eliminar Jornada</a></li>      
      </ul>

      <div id="myTabContent" class="tab-content">
         <div class="tab-pane fade in active" id="creatjor">
            <div class="col-md-6">
               <form role="form" style="padding-top:0.5cm" action="/crearconfiguracion" method="POST">
                  <div class="form-group" style="padding-right:2cm">
                     <label for="nombre">Etiqueta Jornada</label>
                     <input type="text" class="form-control" id="cetiquetajor" name="cetiquetajor" 
                        placeholder="Media Tarde">
                  </div>
                  <div class="form-group" style="padding-right:2cm">
                     <label for="tiempo">Hora Inicio</label>
                     <input class="form-control" type="number" id="hiniciojor" name="hiniciojor" min="0" max="24">
                  </div>
                  <div class="form-group" style="padding-right:2cm">
                     <label for="tiempo">Hora Fin</label>
                     <input class="form-control" type="number" id="hfinjor" name="hfinjor" min="0" max="24">
                  </div>                                  
               </form>
               <div class="form-group" style="padding-top:0.2cm">
                  <!--<button type="button" id="btncrearco" class="btn btn-success btn-lg">Crear</button>-->
                  <button id="btncreatejor" class="btn btn-warning">Crear</button>
               </div>
            </div>         
         </div>
         <div class="tab-pane fade" id="editjor">
            <div class="col-md-6">

               <div class="form-group" style="padding-top:1cm">
                  <select name="editidjor" id="editidjor" class="form-control">
                     %for jornada in jornadas:
                     <option value="{{jornada.entregarIdentificacion()}}">{{jornada.entregarEtiquetaJornada()}}</option>
                     %end
                  </select>            
               </div>

               <div class="form-group" style="padding-top:0.2cm">
                  <button type="button" id="btnloadjor" class="btn btn-warning">Cargar</button>
               </div>

               <div id="formeditjor" style="display:none">
                  <form role="form">
                     <div class="form-group" style="padding-right:2cm">
                        <label for="nombre">Etiqueta Jornada</label>
                        <input type="text" class="form-control" id="edetiquetajor" name="edetiquetajor" 
                           placeholder="Media Tarde">
                     </div>
                     <div class="form-group" style="padding-right:2cm">
                        <label for="tiempo">Hora Inicio</label>
                        <input class="form-control" type="number" id="edhiniciojor" name="edhiniciojor" min="0" max="24">
                     </div>
                     <div class="form-group" style="padding-right:2cm">
                        <label for="tiempo">Hora Fin</label>
                        <input class="form-control" type="number" id="edhfinjor" name="edhfinjor" min="0" max="24">
                     </div>                                                          
                  </form>
                  <div class="form-group" style="padding-top:0.2cm">
                     <!--<button type="button" id="btncrearco" class="btn btn-success btn-lg">Crear</button>-->
                     <button id="btneditjor" class="btn btn-warning">Editar</button>
                  </div>
               </div>         
            </div>         
         </div>
         <div class="tab-pane fade" id="deljor">
            <div class="col-md-6">
               <div class="form-group" style="padding-top:1cm">
                  <select name="deletejor" id="deletejor" class="form-control">
                     %for jornada in jornadas:
                     <option value="{{jornada.entregarIdentificacion()}}">{{jornada.entregarEtiquetaJornada()}}</option>
                     %end
                  </select>            
               </div>
               <div class="form-group" style="padding-top: 0.2cm">
                  <button class="btn btn-warning" id="btndeljor">
                     Eliminar
                  </button>            
               </div>            
            </div>               
         </div>   
      </div>   
   </div>   
</div>

<script>
   $("#btndelcat").click(function(){
      var identificacionCategoria = $("#deletecat").val();
      var post_data = {'idcat': identificacionCategoria};
      $.ajax
      ({
         type: 'POST',
         url : 'eliminarCategoria',
         data: JSON.stringify(post_data),
         contentType: "application/json; charset=utf-8",
         dataType: 'json',
         success: function(data){
            $.each(data, function(index,  value){
               alert(value);
               $(location).attr('href', '/tconfiguracionjc')
            });
         }
      });
   });

   $("#btncreatecat").click(function(){
      var etiquetaCategoria = $("#cetiquetacat").val();
      var metricaCategoria = $("#cmcat").val();
      var post_data = {'etiqueta': etiquetaCategoria, 'metrica': metricaCategoria};
      $.ajax
      ({
         type : 'POST',
         url : 'crearCategoria',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success :  function(data){
            $.each(data, function(index, value){
               alert(value);
            });
            $(location).attr('href', '/tconfiguracionjc');
         }
      });
   });

   $("#btneditcat").click(function(){
      var identificacionCategoria = $("#editidcat").val();
      var etiquetaCategoria = $("#edetiquetacat").val();
      var metricaCategoria = $("#edmetricat").val();
      var post_data = {'idcat': identificacionCategoria, 'etiqueta': etiquetaCategoria, 'metrica': metricaCategoria};
      $.ajax
      ({
         type : 'POST',
         url : 'editarCategoria',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success :  function(data){
            $.each(data, function(index, value){
               alert(value);
            });
            $(location).attr('href', '/tconfiguracionjc');
         }
      });
   });

   $("#btnloadcat").click(function(){
      var identificacionCategoria = $("#editidcat").val();
      var post_data = {'idcat': identificacionCategoria};
      $.ajax
      ({
         type : 'POST',
         url : 'obtenerCategoria',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success: function(data){
          if(parseInt(data['efect']) == 1){
            var categoriaObtenida = data['categoria'];
            var etiquetaCategoria = categoriaObtenida['etiqueta'];
            var metricaCategoria = categoriaObtenida['metrica'];
            $("#edetiquetacat").attr("value", etiquetaCategoria);
            $("#edmetricat").attr("value", metricaCategoria);
            $("#formeditcat").show();
          }
          else{
            alert("La configuracion no pudo ser cargada en el sistema, Intente de Nuevo.");
          }
         }
      });
   });

   $("#btndeljor").click(function(){
      var identificacionJornada = $("#deletejor").val();
      var post_data = {'idjor': identificacionJornada};
      $.ajax
      ({
         type: 'POST',
         url : 'eliminarJornada',
         data: JSON.stringify(post_data),
         contentType: "application/json; charset=utf-8",
         dataType: 'json',
         success: function(data){
            $.each(data, function(index,  value){
               alert(value);
               $(location).attr('href', '/tconfiguracionjc')
            });
         }
      });
   });

   $("#btncreatejor").click(function(){
      var etiquetaJornada = $("#cetiquetajor").val();
      var horaInicio = $("#hiniciojor").val();
      var horaFin = $("#hfinjor").val();
      var post_data = {'etiqueta': etiquetaJornada, 'hinicio': horaInicio, 'hfin': horaFin};
      $.ajax
      ({
         type : 'POST',
         url : 'crearJornada',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success :  function(data){
            $.each(data, function(index, value){
               alert(value);
            });
            $(location).attr('href', '/tconfiguracionjc');
         }
      });
   });

   $("#btnloadjor").click(function(){
      var identificacionJornada = $("#editidjor").val();
      var post_data = {'idjor': identificacionJornada};
      $.ajax
      ({
         type : 'POST',
         url : 'obtenerJornada',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success: function(data){
          if(parseInt(data['efect']) == 1){
            var jornadaObtenida = data['jornada'];
            var etiquetaJornada = jornadaObtenida['etiqueta'];
            var horaInicio = jornadaObtenida['hinicio'];
            var horaFin = jornadaObtenida['hfin'];
            $("#edetiquetajor").attr("value", etiquetaJornada);
            $("#edhiniciojor").attr("value", horaInicio);
            $("#edhfinjor").attr("value", horaFin);
            $("#formeditjor").show();
          }
          else{
            alert("La configuracion no pudo ser cargada en el sistema, Intente de Nuevo.");
          }
         }
      });
   });

   $("#btneditjor").click(function(){
      var identificacionJornada = $("#editidjor").val();
      var etiquetaJornada = $("#edetiquetajor").val();
      var horaInicio = $("#edhiniciojor").val();
      var horaFin = $("#edhfinjor").val();
      var post_data = {'idjor': identificacionJornada, 'etiqueta': etiquetaJornada, 'hinicio': horaInicio, 'hfin': horaFin};
      $.ajax
      ({
         type : 'POST',
         url : 'editarJornada',
         data : JSON.stringify(post_data),
         contentType : "application/json; charset=utf-8",
         dataType : 'json',
         success :  function(data){
            $.each(data, function(index, value){
               alert(value);
            });
            $(location).attr('href', '/tconfiguracionjc');
         }
      });
   });   
</script>


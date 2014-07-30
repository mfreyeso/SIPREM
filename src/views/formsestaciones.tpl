<ul id="myTab" class="nav nav-tabs">
   <li class="active">
      <a href="#create" data-toggle="tab" class="btn btn-primary">Añadir Estación</a>
    </li>
   <li><a href="#edite" data-toggle="tab" class="btn btn-primary">Editar Estación</a></li>
   <li><a href="#acte" data-toggle="tab" class="btn btn-primary">Activar Estación</a></li>
   <li><a href="#dese" data-toggle="tab" class="btn btn-primary">Desactivar Estación</a></li>   
</ul>
<div id="myTabContent" class="tab-content">
  <div class="tab-pane fade in active" id="create">
         <div class="col-md-8">
            <form role="form" style="padding:0.5cm" action="/crearEstacion" method="POST">
               <div class="form-group" style="padding-right:7cm">
                  <label for="nombre">Nombre:</label>
                  <input type="text" class="form-control" id="nombreE" name="nombreE" 
                     placeholder="Ejemplo: EMAS">
               </div>

               <div class="form-group" style="padding-right:7cm">
                  <label for="nombre">Ubicación:</label>
                  <input type="text" class="form-control" id="ubicacionE" name="ubicacionE" 
                     placeholder="Ejemplo: Posgrados">
               </div>

               <div class="form-group" style="padding-right:7cm">
                  <label for="nombre">Fecha Inicial de Operación:</label>
                  <input type="date" class="form-control" id="fechaE" name="fechaE" 
                     placeholder="Ejemplo: 2002-12-01">
               </div>            
               <div class="form-group">
                  <button type="button" class="btn btn-primary" id="btncrearestacion">Crear</button>
               </div>           
            </form>
            <br>           
         </div>       
  </div>

  <div class="tab-pane fade" id="edite">
    <div class="col-md-6">
      <form action="/modificarEstacion" method="POST">
        <div class="form-group" style="padding:0.5cm">
          <label for="estacion">Estación</label>
          <select class="form-control" name="estacionselect" id="estacionselect">
          %for estacion in estaciones:
            <option value="{{estacion[0].pk}}">{{estacion[0].nombre}}</option>
          %end
          </select>
        </div>
        <div class="form-group">
          <button type="button" class="btn btn-primary" id="btneditestacion">Preparar</button>
        </div>
      </form>
    </div>
    
    <div class="col-md-6" id="atrcambios">
          <form role='form' style ='padding:0.5cm'>
            <div id="formmodestacion" style="display:none">
              <div class='form-group'>
                <label for='nombre'>Nombre:</label>
                <input type='text' class='form-control' id='nombreEstacion' name='nombreEstacion' placeholder='"+nombreEstacion+"'>
                </div>
                <div class='form-group'>
                <label for='ubicacion'>Ubicación:</label>
                <input type='text' class='form-control' id='ubicacionEstacion' name='ubicacionEstacion' placeholder='"+ubicacionEstacion+"'>
                </div>
                <div class='form-group'>
                <label for='fecha'>Fecha Inicial de Operación:</label>
                <input type='date' class='form-control' id='fechaEstacion' name='fechaEstacion'>
                </div>
                <div class='form-group'>
                <button type='button' class='btn btn-primary' id="btneditfestacion">Actualizar</button>
                </div>              
            </div>            
          </form>
          <br>        
    </div>
    <br>
  </div>

  <div class="tab-pane fade" id="dese">
    <div class="col-md-6">
      <form role="form">
        <div class="form-group" style="padding:0.5cm">
          <label for="estacion">Estación</label>
          <select class="form-control" name="destacionselect" id="destacionselect">
          %for estacion in estaciones:
            <option value="{{estacion[0].pk}}">{{estacion[0].nombre}}</option>
          %end
          </select>
        </div>
        <div class="form-group" style="padding:0.5cm">
          <button type="button" class="btn btn-primary" id="btndesestacion">Desactivar</button>
        </div>        
      </form>
      <br>     
    </div>    
  </div>

  <div class="tab-pane fade" id="acte">
    <div class="col-md-6">
      <div class="form-group" style="padding:2.0cm">
         <button type="button" id="btncargarestdes" class="btn btn-primary">Cargar Estaciones Desactivadas</button>        
      </div>     
    </div>
    <div class="col-md-6">
      <div id="activestacion" style="padding: 0.5cm">
        
      </div>
      <div style="padding: 0.5cm" align="center">
        <button class="btn btn-primary" type="button" id="btnactivar" style="display:none">Activar</button>        
      </div>
  </div>
</div>

<script>

   $("#btncrearestacion").click(function(){
         var nombreEstacion = $("#nombreE").val();
         var ubicacionEstacion = $("#ubicacionE").val();
         var fechaEstacion = $("#fechaE").val();
         var post_data = {"nombre":nombreEstacion, "ubicacion": ubicacionEstacion, "fecha": fechaEstacion};
        $.ajax
        ({
            type: 'POST',
            url: 'crearEstacion',
            data:JSON.stringify(post_data),
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(data){
                $.each(data, function(index, value){
                     alert(value);
                     $(location).attr('href', '/estaciones'); 
                });
            }
        });
    });
  
  $("#btneditestacion").click(function(){
    var estacion = $("#estacionselect").val();
    var post_data = {"estacion": estacion};
    $.ajax(
    {
      type : 'POST',
      url : 'obtenerEstacion',
      data : JSON.stringify(post_data),
      contentType : "application/json; charset=utf-8",
      dataType: 'json',
      success: function(data){
        if(parseInt(data['efect']) == 1){
          var estacionObtenida = data['estacion'];
          var nombreEstacion = estacionObtenida['nombre'];
          var ubicacionEstacion = estacionObtenida['ubicacion'];
          $('#nombreEstacion').attr("placeholder", nombreEstacion);
          $('#ubicacionEstacion').attr("placeholder", ubicacionEstacion);
          $("#formmodestacion").show();
                 
        }
      }
    });
  });

  $("#btneditfestacion").click(function(){
    var nombreEstacion = $("#nombreEstacion").val();
    var ubicacionEstacion = $("#ubicacionEstacion").val();
    var fechaEstacion = $("#fechaEstacion").val();
    var estacionSeleccionada = $("#estacionselect").val();
    var post_data = {"ide": estacionSeleccionada, "ubicacion": ubicacionEstacion, "nombre": nombreEstacion, "fecha": fechaEstacion};
    $.ajax(
    {
      type : 'POST',
      url : 'modificarEstacion',
      data : JSON.stringify(post_data),
      contentType : "application/json; charset=utf-8",
      dataType: 'json',
      success : function(data){
        $.each(data, function(index, value){
          alert(value);
          $(location).attr('href', '/estaciones'); 
        });
      }
    });
  });

  $("#btndesestacion").click(function(){
    var estacionSeleccionada = $("#destacionselect").val();
    var post_data = {"ide": estacionSeleccionada};
    $.ajax(
    {
      type : 'POST',
      url : 'desactivarEstacion',
      data : JSON.stringify(post_data),
      contentType : "application/json; charset=utf-8",
      dataType: 'json',
      success : function(data){
        $.each(data, function(index, value){
          alert(value);
          $(location).attr('href', '/estaciones'); 
        });
      }
    });
  });

  $("#btncargarestdes").click(function(){
    $.ajax
    ({
        url : 'estacionesDesactivadas',
        success: function(data){
          if (parseInt(data['efect']) == 1){
            var cadenaInicial ="<form role='form'><div class='form-group'>\
            <label for='estacion'>Estación</label>\
            <select class='form-control' name='estacionselect' id='aestacionselect'>";
            var cadenaFinal = "</select></div></form>";
            var cadenaCentro = " ";
            $(data.coleccion).each(function(index, value){
              var opcion = "<option value='"+value['ide']+"'>"+value['nombre']+"</option>";
              cadenaCentro+=opcion;
            });
            var cadena = cadenaInicial + cadenaCentro + cadenaFinal;
            $("#activestacion").append(cadena);
            $("#btnactivar").show();
          }
          else{
            alert("En el momento no hay estaciones desactivadas.");
            $(location).attr('href', '/estaciones');
          }
        },
        dataType: 'json'
    });
  });
  
  $("#btnactivar").click(function(){
    var estacionSeleccionada = $("#aestacionselect").val();
    var post_data = {'ide': estacionSeleccionada};
    $.ajax(
    {
      type: 'POST',
      url : 'activarEstacion',
      data : JSON.stringify(post_data),
      contentType : "application/json; charset=utf-8",
      dataType : 'json',
      success : function(data){
        $.each(data, function(index, value){
          alert(value);
          $(location).attr('href', '/estaciones');
        });
      }
    });
  });
</script>
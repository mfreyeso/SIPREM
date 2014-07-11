<ul id="myTab" class="nav nav-tabs">
   <li class="active">
      <a href="#creatc" data-toggle="tab" class="btn btn-success">Añadir Configuración</a></li>
   <li><a href="#editc" data-toggle="tab" class="btn btn-success">Editar Configuración</a></li>
   <li><a href="#delc" data-toggle="tab" class="btn btn-success">Eliminar Configuración</a></li>
   
</ul>
<div id="myTabContent" class="tab-content">
   <div class="tab-pane fade in active" id="creatc">
     <form role="form" style="padding:0.5cm" action="/crearconfiguracion" method="POST">
            <div class="form-group" style="padding-right:7cm">
               <label for="nombre">Nombre Configuración</label>
               <input type="text" class="form-control" id="nombreC" name="nombreC" 
                  placeholder="Ejemplo: Configuracion Dos">
            </div>
            <div class="form-group">
               <label for="tiempo">Diferencial de Tiempo Precipitación (min.)</label>
               <input type="number" id="dfprec" name="dfprec" min="5">
            </div>
            <div class="form-group">
               <label for="tiempo">Posición Precipitación (Archivo Plano)</label>
               <input type="number" id="psprec" name="psprec" min="0">
            </div>
            <div class="form-group">
               <button type="submit" class="btn btn-success">Crear</button>
            </div>           
         </form>
      <p></p><br>
   </div>
   <div class="tab-pane fade" id="editc">
      <p></p><br>
   </div>
   <div class="tab-pane fade" id="delc">
      <p></p><br>
   </div>   
</div>
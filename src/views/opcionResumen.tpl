<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>	
	%include('header.tpl')
	%include('aside.tpl')

	<div class="row">
		<div class="col-xs-12 col-md-8">
				
			<h2>Opciones de Resumen</h2><br>

			<p><h4>Seleccione el tipo de resumen que desea generar de los eventos encontrados</h4></p><br>

			<form role="form" action="/resumenParametrizado" method="post" enctype="multipart/form-data">
				<div class="form-group">
                    <label for="tiporesumen">Tipo de Resumen</label>
	                <select class="form-control" name="opcionResumen">
	                  <option value="1">Mensual Anual</option>
	                  <option value="2">Semestral</option>
	                  <option value="3">Trimestral</option>
	                  <option value="4">Trimestral según régimen bimodal</option>
	                </select>
	            </div>

				<div class="form-group">
               <input name="butEjecutar" type="submit" value="Generar Resumen" class="btn btn-primary">
                </div>
        	</form>
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
<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			<h3>Configuración de Indicador A{{valindicador}}</h3><br>
			
			<h4>SIPREM permite parametrizar el calculo del Indicador A{{valindicador}}....</h4><br>

			<form role="form" action="/transformarIndicador" method="post">
				<div class="row">
					<div class="col-md-6">
						<div class="form-group">
							<label for="indicador">Numero de Dias</label>
							<input class='form-control' id='valindicador' type='number' name='numdias' value='25' min='5' max='31'/>
						</div>
					</div>
					
					<div class="col-md-6" align="center">
						<div class="form-group" style="padding-top:0.5cm">
			               <button type="button" class="btn btn-primary" id="btncambioind">Guardar Cambios</button>
			            </div>
					</div>
				</div>				
			</form>
		</div>
	</div>
	<script>
		$("#btncambioind").click(function(){
         var valIndicador = $("#valindicador").val();
         var post_data = {"valindicador":valIndicador};
        $.ajax
        ({
            type: 'POST',
            url: 'transformarIndicador',
            data:JSON.stringify(post_data),
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(data){
                $.each(data, function(index, value){
                     alert(value);
                     $(location).attr('href', '/configurarindicador'); 
                });
            }
        });
    	});
	</script>
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
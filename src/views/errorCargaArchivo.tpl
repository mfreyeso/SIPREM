<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	%if opcion == 1:	
		<div class="row">
			<div class="col-xs-12 col-md-8">			
	    		<div class="jumbotron">
	  				<h1>Advertencia</h1>
	  				<p>El archivo seleccionado contiene registros y eventos de precipitación que ya se encuentran almacenados en el sistema.</p>
	            </div>		
			</div>
		</div>
	%else:
		<div class="row">
				<div class="col-xs-12 col-md-8">			
		    		<div class="jumbotron">
		  				<h1>Advertencia</h1>
		  				<p>Se produjo un problema en la carga del archivo que fue seleccionado.</p>
					</div>		
				</div>
		</div>
	%end


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
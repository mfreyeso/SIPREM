<!DOCTYPE html>
<html lang="es">
%include('head.tpl')
<body>
	%include('headerOut.tpl')	
	<div class="row">
		<div class="col-xs-12 col-md-8">
			
		</div>
	</div>

<script>
	$("#btnlogin").click(function(){
		var username = $("#nameuser").val();
		var password = $("#passuser").val();
		var post_data = {'nameuser': username, 'passuser': password};
		$.ajax
		({
			type: 'POST',
	        url : 'loginuser',
	        data: JSON.stringify(post_data),
	        contentType: "application/json; charset=utf-8",
	        dataType: 'json',
	        success: function(data){
	        	if (parseInt(data['efect']) == 1){
	        		alert("Ingreso Satisfactorio");
	        		$(location).attr('href', '/menuinicio')
	        	}
	        	else{
	        		alert("Ingreso incorrecto, revise que su usuario y contraseña sean correctos e intente nuevamente.");
	        	}
	        }	        
		});
	});
</script>
</body>
</html>
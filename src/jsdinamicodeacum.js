case 1:
							    			var inputsDi = "<div class='form-group'>\
							    			<label for='diasel'>Fecha</label>\
							    			<input class='form-control' type='date' name='fecha'/>\
							    			</div><br>";							    			
											$("#divDinamico").empty();							                
							                $("#divDinamico").append($(inputsDi));
							    			break;

							    		case 2:
							    			var inputsDi = "<div class='form-group'>\
							                	<label for='diasel'>Mes</label>\
							                	<input class='form-control' type='month' name='mes'/>\
							                	</div><br>";
							                $("#divDinamico").empty();							                
							                $("#divDinamico").append($(inputsDi));
							    			break;
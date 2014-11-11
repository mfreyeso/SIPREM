<!DOCTYPE html>
<html lang="es">
%include('head.tpl')

<body>	
	%include('header.tpl')
	%include('aside.tpl')
	
	<div class="row">
		<div class="col-xs-12 col-md-8">			
			<div id="resumen">
				<h3><strong>Resumen de Eventos</strong></h3>
				<h4><strong>Estacion: </strong>{{nombreEstacion}}</h4>
				<h4>{{cadenaParametrizada}}</h4><br>

				%listaMeses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
				%listaMetricas = ["Duración(min)", "Magnitud(mm)", "Intensidad Media(mm/h)", "Intensidad Maxima(mm/h)"]
				%listaSemestres = ["Enero - Junio", "Julio - Diciembre"]
				%listaTrimestresEstandar = ["Ene-Feb-Mar", "Abr-May-Jun", "Jul-Ago-Sep", "Oct-Nov-Dic"]
				%listaTrimestresBimodal = ["Dic-Ene-Feb", "Mar-Abr-May", "Jun-Jul-Ago", "Sep-Oct-Nov"]

				%resultadosCategoria = resultados[0]
				%resultadosJornada = resultados[1]
				%resultadosMaximos = resultados[2]
				
				<div>
					<h3>Precipitaciones según Categoria</h3>
						%include('rescategoria.tpl', opcionr = opcionrs, resultados = resultadosCategoria, categoriasP = categorias, diasMesF = diasMes, vAnualF = vAnual)				
				</div>

				<div>
					<h3>Precipitaciones según Jornada</h3>
						%include('resjornada.tpl', opcionr = opcionrs, resultados = resultadosJornada, jornadasP = jornadas, diasMesF = diasMes, vAnualF = vAnual)					
				</div>
				<div>
					<h3>Máximos Obtenidos</h3>
					%include('resmaximo.tpl', opcionr = opcionrs, resultados = resultadosMaximos, diasMesF = diasMes, vAnualF = vAnual)				
				</div>
			</div>
			<div align="center" style="padding-top:0.3cm">
				<p>
					<button type="button" class="btn btn-default"><a download="resumeneventos_{{nombreEstacion}}_{{cadenaParametrizada}}.xls" href="#" onclick="return ExcellentExport.excel(this, 'resumen', 'hoja');">Reporte Excel</a></button>
					<button type="button" class="btn btn-default" id="btnreportevent">Reporte PDF</button>					
				</p>																
			</div>						
		</div>
	</div>
	<script>
		$("#btnreportevent").click(function(){
			var pdf = new jsPDF('p', 'pt', 'letter')
			//var pdf = new jsPDF('p', 'pt', 'letter', 'landscape')
		// source can be HTML-formatted string, or a reference
		// to an actual DOM element from which the text will be scraped.
		, source = $('#resumen')[0]

		// we support special element handlers. Register them with jQuery-style 
		// ID selector for either ID or node name. ("#iAmID", "div", "span" etc.)
		// There is no support for any other type of selectors 
		// (class, of compound) at this time.
		, specialElementHandlers = {
			// element with id of "bypass" - jQuery style selector
			'#bypassme': function(element, renderer){
				// true = "handled elsewhere, bypass text extraction"
				return true
			}
		}

		margins = {
	      top: 80,
	      bottom: 60,
	      left: 40,
	      width: 522
	    };
	    // all coords and widths are in jsPDF instance's declared units
	    // 'inches' in this case
	    pdf.text(20, 20, 'Universidad Nacional de Colombia Sede Manizales');
		pdf.text(20, 40, 'Instituto de Estudios Ambientaltes IDEA');
		pdf.text(20, 60, 'Sistema de Informacion Meteorologíco de Precipitaciones Red de Estaciones Manizales');
	    pdf.fromHTML(
	    	source // HTML string or DOM elem ref.
	    	, margins.left // x coord
	    	, margins.top // y coord
	    	, {
	    		'width': margins.width // max width of content on PDF
	    		, 'elementHandlers': specialElementHandlers
	    	},
	    	function (dispose) {
	    	  // dispose: object with X, Y of the last line add to the PDF 
	    	  //          this allow the insertion of new lines after html
	          pdf.save('Test.pdf');
	        },
	    	margins
	    )
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
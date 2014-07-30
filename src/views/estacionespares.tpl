		<div class="col-xs-8 col-md-4">
			<div class="list-group">
				%for i in range(0, (len(estaciones)/2)):
					<a href="/infoestacion/{{estaciones[i][0].id}}" class="list-group-item" data-toggle="tab">
				    	<h4 class="list-group-item-heading">{{estaciones[i][0].nombre}}</h4>
				    	<p class="list-group-item-text">{{estaciones[i][1]}}</p>
			  		</a>
			  	%end
			</div>
		</div>
		<div class="col-xs-8 col-md-4">
			<div class="list-group">
				%for i in range((len(estaciones)/2), len(estaciones)):
					<a href="/infoestacion/{{estaciones[i][0].id}}" class="list-group-item" data-toggle="tab">
				    	<h4 class="list-group-item-heading">{{estaciones[i][0].nombre}}</h4>
				    	<p class="list-group-item-text">{{estaciones[i][1]}}</p>
			  		</a>
			  	%end
			</div>
		</div>
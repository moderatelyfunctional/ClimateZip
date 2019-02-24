$(document).ready(function() {
	createChart(
		$('#currentConditions'), 
		curr_city, 
		curr_city_vector,
		'#75cff8',
		curr_closest_city,
		curr_closest_vector,
		'#55e585'
	);

	createChart(
		$('#futureConditions'),
		curr_city,
		future_city_vector,
		'#ffa759',
		future_closest_city,
		future_closest_vector,
		'#f84b47'
	);

	$('#selectYears').on('change', ajaxUpdateFutureConditions);
})

const month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const createChart = function(ctx, first_city, first_city_vector, first_color, second_city, second_city_vector, second_color) {
	var chart = new Chart(ctx, {
	    type: 'line',
	    data: {
	        labels: month_labels,
	        datasets: [
		        {
		            label: first_city,
		            backgroundColor: 'transparent',
		            borderColor: first_color,
		            data: first_city_vector,
		        },
		        {
		        	label: second_city,
		        	backgroundColor: 'transparent',
		        	borderColor: second_color,
		        	data: second_city_vector
		        }
	        ]
	    },
	    options: {
            responsive: true,
	    }
	});
}

const ajaxUpdateFutureConditions = function() {
	const value = $(this).val();
	





}




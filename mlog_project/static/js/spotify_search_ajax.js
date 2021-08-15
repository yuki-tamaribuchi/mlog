var search_url = document.currentScript.getAttribute('search_url');
function search(){
	$.ajax({
		'url':search_url,
		'type':'POST',
		'data':{
			'search_keywords':$('#search_keywords').val()
		},
		'dataType':'json'
	})
	.done(function(response){
		console.log(response['results']);
		results = response['results'];
		let html_data = '<option value="">--------</option>';
		results.forEach(function(result){
			html_data += `<option value="{&quot;spotify_link&quot;:&quot;${result.spotify_link}&quot;, &quot;preview_url&quot;:&quot;${result.preview_url}&quot;, &quot;artwork_url&quot;:&quot;${result.artwork_url}&quot;}">${result.track_name}/${result.artists}</option>`
		});
		$("#spotify_track_select").html(html_data);
	});
}
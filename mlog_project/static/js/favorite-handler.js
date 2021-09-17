var favorite_url = document.currentScript.getAttribute('favorite_url');
var artist_slug = document.currentScript.getAttribute('artist_slug');
var favorite_btn = document.getElementById('favorite-btn');
var is_loggedin = document.currentScript.getAttribute('is_loggedin');

favorite_btn.addEventListener('click', favorite_process, false);

function favorite_process(){
	if (is_loggedin==='True'){
		$.ajax({
			'url':favorite_url,
			'type':'POST',
			'data':{
				'favorited_artist':artist_slug
			},
			'dataType':'json'
		})
		.done(function(response){
			fav_status = response['fav_status'];
			if (fav_status){
				favorite_btn.value = "お気に入り解除";
			}else{
				favorite_btn.value = "お気に入り登録";
			}
		});
	}else{
		$.ajax({
			'url':favorite_url,
			'type':'GET',
			'data':{
				'artist_slug':artist_slug
			},
			'dataType':'json'
		})
		.done(function(response){
			window.location.replace(response['login_url']);
		});
	}
	
}
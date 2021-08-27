var favorite_url = document.currentScript.getAttribute('favorite_url');
var favorited_artist = document.currentScript.getAttribute('favorited_artist');
var favorite_btn = document.getElementById('favorite-btn');

favorite_btn.addEventListener('click', favorite_process, false);

function favorite_process(){
	$.ajax({
		'url':favorite_url,
		'type':'POST',
		'data':{
			'favorited_artist':favorited_artist
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
}
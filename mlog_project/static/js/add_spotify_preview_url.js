var add_spotify_preview_url_url = document.currentScript.getAttribute('add_spotify_preview_url_url');

function open_add_spotify_preview_url_window(){
	window.open(add_spotify_preview_url_url, 'subwin_spotify');
}

var add_spotify_preview_url_link = document.getElementById('add_spotify_preview_url_link');
add_spotify_preview_url_link.addEventListener('click', open_add_spotify_preview_url_window, false);

function add_spotify_preview_url(spotify_link, preview_url, artwork_url){
	var id_spotify_link_field = document.getElementById('id_spotify_link');
	var id_spotify_preview_url_field = document.getElementById('id_spotify_preview_url');
	var id_artwork_url_field = document.getElementById('id_artwork_url')
	id_spotify_link_field.value = spotify_link;
	if (preview_url !== "null"){
		id_spotify_preview_url_field.value = preview_url;
	}
	id_artwork_url_field.value = artwork_url;
}
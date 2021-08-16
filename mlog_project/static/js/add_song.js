var song_create_popup_url = document.currentScript.getAttribute('song_create_popup_url');

function add_song_window_open(){
	window.open(song_create_popup_url, 'subwin_song', 'width=500,height=500');
}

var add_song_link = document.getElementById('add_song_link');
add_song_link.addEventListener('click', add_song_window_open, false);

function add_song(name, pk){
	var select = document.getElementById('id_song');
	var option = document.createElement('option');
	option.setAttribute('value', pk);
	option.innerHTML = name;

	select.add(option, 0);
	select.options[0].selected = true;
}
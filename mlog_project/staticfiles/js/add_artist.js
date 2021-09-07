var add_artist_link_url = document.currentScript.getAttribute('add_artist_link_url');

function open_add_artist_window(){
	window.open(add_artist_link_url,'subwin_artist');
}

var add_artist_link = document.getElementById('add_artist_link');
add_artist_link.addEventListener('click', open_add_artist_window, false);

function add_artist(name, pk){
	var select=document.getElementById('id_artist');
	var option=document.createElement('option');
	option.setAttribute('value', pk);
	option.innerHTML = name;

	select.add(option, 0);
	select.options[0].selected = true;
}
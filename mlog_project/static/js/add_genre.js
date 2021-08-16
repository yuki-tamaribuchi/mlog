var genre_create_popup_url = document.currentScript.getAttribute('genre_create_popup_url');
console.log(genre_create_popup_url);

function open_add_genre_window(){
	console.log('called');
	window.open(genre_create_popup_url, 'subwin_genre');
	console.log('finished');
}

var add_genre_link = document.getElementById('add_genre_link');
add_genre_link.addEventListener('click', open_add_genre_window, false);

function add_genre(name, pk){
	var select=document.getElementById('id_genre');
	var option=document.createElement('option');
	option.setAttribute('value',pk);
	option.innerHTML = name;

	select.add(option, 0);
	select.options[0].selected=true;
}
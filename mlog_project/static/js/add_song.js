function add_song(name, pk){
	var select = document.getElementById('id_song');
	var option = document.createElement('option');
	option.setAttribute('value', pk);
	option.innerHTML = name;

	select.add(option, 0);
	select.options[0].selected = true;
}
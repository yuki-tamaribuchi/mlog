var like_url = document.currentScript.getAttribute('like_url');
var entry_id = document.currentScript.getAttribute('entry_id');
var like_btn = document.getElementById('like-btn');
var is_loggedin = document.currentScript.getAttribute('is_loggedin');
var liked_user_list_link = document.getElementById('liked_user_list_link');

like_btn.addEventListener('click', like_process, false);

function like_process(){
	if(is_loggedin==='True'){
		$.ajax({
			'url':like_url,
			'type':'POST',
			'data':{
				'entry_id':entry_id
			},
			'dataType':'json'
		})
		.done(function(response){
			like_status = response['like_status'];
			like_count = response['like_count'];
			if (like_status){
				like_btn.innerHTML = '<i class="fa fa-heart like-true"></i>';
			}else{
				like_btn.innerHTML = '<i class="fa fa-heart like-false"></i>';
			}
			liked_user_list_link.innerHTML = "Like:"+like_count;
		});
	}else{
		$.ajax({
			'url':like_url,
			'type':'GET',
			'data':{
				'entry_id':entry_id
			},
			'dataType':'json'
		})
		.done(function(response){
			window.location.replace(response['login_url']);
		});
	}
}
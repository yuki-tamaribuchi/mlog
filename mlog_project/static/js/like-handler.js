var like_url = document.currentScript.getAttribute('like_url');
var liked_entry = document.currentScript.getAttribute('liked_entry');
var like_btn = document.getElementById('like-btn');

like_btn.addEventListener('click', like_process, false);

function like_process(){
	$.ajax({
		'url':like_url,
		'type':'POST',
		'data':{
			'liked_entry':liked_entry
		},
		'dataType':'json'
	})
	.done(function(response){
		like_status = response['like_status'];
		if (like_status){
			like_btn.innerHTML = '<i class="fa fa-heart like-true"></i>';
		}else{
			like_btn.innerHTML = '<i class="fa fa-heart like-false"></i>';
		}
	});
}
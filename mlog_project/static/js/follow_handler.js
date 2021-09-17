var follow_url = document.currentScript.getAttribute('follow_url');
var follower_user = document.currentScript.getAttribute('follower_user');
var follow_btn = document.getElementById('follow_btn');
var follower_count_span = document.getElementById('follower_count');

follow_btn.addEventListener('click', follow_process, false);

function follow_process(){
	$.ajax({
		'url':follow_url,
		'type':'POST',
		'data':{
			'follower_user':follower_user
		},
		'dataType':'json'
	})
	.done(function(response){
		follow_status = response['follow_status'];
		follower_count = response['follower_count'];
		if (follow_status){
			follow_btn.value='フォローをやめる';
		}else{
			follow_btn.value='フォローする';
		}
		follower_count_span.innerHTML = follower_count;
	});
}
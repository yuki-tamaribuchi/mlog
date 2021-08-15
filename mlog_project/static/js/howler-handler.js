spotify_preview_url = document.currentScript.getAttribute('spotify_preview_url');

var sound = new Howl({
	src: [spotify_preview_url],
	format:['mp3']
});

function play_pause(sound){
	if (sound.playing()){
		$('#id_artwork_for_preview_in_entry_detail').removeClass('artwork_circle');
		sound.pause();
		$('.circle-wrap .circle .mask.full, .circle-wrap .circle .fill').css("animation-play-state", "paused");
		$('.pause_icon').remove();
		$('.inside-circle').append('<i class="fas fa-play fa-2x play_icon"></i>');
	}else{
		$('#id_artwork_for_preview_in_entry_detail').addClass('artwork_circle');
		sound.play();
		$('.circle-wrap .circle .mask.full, .circle-wrap .circle .fill').css("animation-play-state", "running");
		$('.play_icon').remove();
		$('.inside-circle').append('<i class="fas fa-pause fa-2x pause_icon"></i>');

	}

	sound.on('end', function(){
		$('.circle-wrap .circle .mask.full, .circle-wrap .circle .fill').css("animation-play-state", "paused");
		$('.pause_icon').remove();
		$('.inside-circle').append('<i class="fas fa-play fa-2x play_icon"></i>');
		$('#id_artwork_for_preview_in_entry_detail').removeClass('artwork_circle');
	})
}
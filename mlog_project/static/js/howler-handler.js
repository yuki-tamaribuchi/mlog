spotify_preview_url = document.currentScript.getAttribute('spotify_preview_url');

var sound = new Howl({
	src: [spotify_preview_url],
	format:['mp3']
});

var play_preview_element = document.getElementById('id_play_preview');
play_preview_element.addEventListener('click', play_pause, false);

function play_pause(){
	if (sound.playing()){
		$('#id-artwork-for-preview-in-entry-detail').removeClass('artwork-circle');
		sound.pause();
		$('.circle-wrap .circle .mask.full, .circle-wrap .circle .fill').css("animation-play-state", "paused");
		$('.pause-icon').remove();
		$('.inside-circle').append('<i class="fas fa-play fa-2x play-icon"></i>');
	}else{
		$('#id-artwork-for-preview-in-entry-detail').addClass('artwork-circle');
		sound.play();
		$('.circle-wrap .circle .mask.full, .circle-wrap .circle .fill').css("animation-play-state", "running");
		$('.play-icon').remove();
		$('.inside-circle').append('<i class="fas fa-pause fa-2x pause-icon"></i>');

	}

	sound.on('end', function(){
		$('.circle-wrap .circle .mask.full, .circle-wrap .circle .fill').css("animation-play-state", "paused");
		$('.pause-icon').remove();
		$('.inside-circle').append('<i class="fas fa-play fa-2x play-icon"></i>');
		$('#id-artwork-for-preview-in-entry-detail').removeClass('artwork-circle');
	})
}
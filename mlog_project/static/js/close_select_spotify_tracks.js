var spotify_link = document.currentScript.getAttribute('spotify_link');
var preview_url = document.currentScript.getAttribute('preview_url');
var artwork_url = document.currentScript.getAttribute('artwork_url');

window.opener.add_spotify_preview_url(spotify_link, preview_url, artwork_url);
window.close();
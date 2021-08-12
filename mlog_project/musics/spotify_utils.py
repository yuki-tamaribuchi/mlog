import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from mlog_project.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

class GetSpotifyData:
	def __init__(self):
		#SPOTIFY_CLIENT_ID = os.environ.get('MLOG_SPOTIFY_CLIENT_ID')
		#SPOTIFY_CLIENT_SECRET = os.environ.get('MLOG_SPOTIFY_CLIENT_SECRET')
		client_credentials_manager = SpotifyClientCredentials(
		client_id=SPOTIFY_CLIENT_ID,
		client_secret=SPOTIFY_CLIENT_SECRET,
		)
		self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


	def search_track(self, search_keywords):
		artists = []
		item_list = []

		result = self.spotify.search(
			q=search_keywords,
			limit=30,
		)
		items = result['tracks']['items']

		for item in items:
			if item['preview_url']:
				artists = [artist['name'] for artist in item['artists']]
				item_list.append(
					{
						'track_name':item['name'],
						'artists':artists,
						'link':item['external_urls']['spotify'],
						'preview_url':item['preview_url'],
					}
				)

		return item_list
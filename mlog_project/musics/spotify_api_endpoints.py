import base64
import requests
import json

from mlog_project.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


client_id = SPOTIFY_CLIENT_ID
client_secret = SPOTIFY_CLIENT_SECRET
BASE64 = base64.b64encode(bytes(client_id+':'+client_secret, 'ascii'))
BASE64 = BASE64.decode('ascii')

SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
API_VERSION = 'v1'

CLIENT_SIDE_URL  = 'http://127.0.0.1'
PORT = '8000'
REDIRECT_URI = '{}:{}/callback/q'.format(CLIENT_SIDE_URL, PORT)
SCOPE = ''
STATE = ''
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
	'response_type':'code',
	'redirect_uri':REDIRECT_URI,
	'scope':SCOPE,
	'client_id':client_id,
}

url_args = '&'.join(['{}={}'.format(key, val) for key, val in auth_query_parameters.items()])
auth_url = '{}/?{}'.format(SPOTIFY_AUTH_URL, url_args)

def save_access_token_to_client_session(request):
	auth_token = request.GET.get('code')

	code_payload = {
		'grant_type':'authorization_code',
		'code':auth_token,
		'redirect_url':REDIRECT_URI,
	}
	headers = {'Authorization':'Basic {}'.format(BASE64)}
	post_request = requests.post(
		SPOTIFY_TOKEN_URL, data=code_payload, headers=headers
	)
	response_data = json.loads(post_request.text)

	request.session['access_token'] = response_data['access_token']
	request.session['refresh_token'] = response_data['refresh_token']
	request.session.set_expiry(response_data['expires_in'])

SPOTIFY_API_URL = '{}/{}'.format(SPOTIFY_API_BASE_URL, API_VERSION)
USER_PROFILE_ENDPOINT = '{}/{}'.format(SPOTIFY_API_URL, 'me')

def requests_url(request, url):
	access_token = request.session.get('access_token')
	authorization_header = {'Authorization':'Bearer {}'.format(access_token)}
	resp = requests.get(url, headers=authorization_header)
	return resp.json()

def get_album(request, album_id):
	url = '{}/{}/'.format(SPOTIFY_API_URL, 'albums')+album_id
	print(url)
	return requests_url(request, url)
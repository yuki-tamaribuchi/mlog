import base64
from os import POSIX_FADV_DONTNEED
from mlog_project.mlog_project.settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


client_id = SPOTIFY_CLIENT_ID
client_secret = SPOTIFY_CLIENT_SECRET
BASE64 = base64.b64encode(bytes(client_id+':'+client_secret, 'ascii'))

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
def create_test_genre(genre_name):
	from musics.models import Genre
	genre_instance = Genre.objects.create(genre_name = genre_name)
	return genre_instance

def get_test_genre(gerne_name):
	from musics.models import Genre
	genre_instance = Genre.objects.get(gerne_name=gerne_name)
	return genre_instance

def create_test_artist(artist_name, artist_name_id, genre_name):
	from musics.models import Artist
	aritst_instance = Artist.objects.create(
		artist_name = artist_name,
		artist_name_id = artist_name_id
	)
	aritst_instance.genre.add(create_test_genre(genre_name))
	return aritst_instance

def create_test_song(song_name, artist_name, artist_name_id, genre_name):
	from musics.models import Song
	song_instance = Song.objects.create(
		song_name = song_name
	)
	song_instance.artist.add(create_test_artist(artist_name, artist_name_id ,genre_name))
	song_instance.genre.add(get_test_genre(genre_name))
	return song_instance

def create_test_user(username, handle, biograph):
	from accounts.models import User
	user_instance = User.objects.create(
		username = username,
		handle = handle,
		biograph = biograph
	)
	return user_instance


def create_test_entry(title, content, username, handle, biograph, song_name, artist_name, artist_name_id, genre_name):
	from entry.models import Entry
	entry_instance = Entry.objects.create(
		title = title,
		content = content,
		writer = create_test_user(username, handle, biograph),
		song = create_test_song(song_name, artist_name, artist_name_id, genre_name)
	)
	return entry_instance
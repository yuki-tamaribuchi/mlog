def create_test_genre(genre_name):
	from musics.models import Genre
	genre_instance = Genre.objects.create(genre_name = genre_name)
	return genre_instance

def get_test_genre(genre_name):
	from musics.models import Genre
	genre_instance = Genre.objects.get(genre_name=genre_name)
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

def create_test_comment(comment, username_for_comment, handle_for_comment, biograph_for_comment, title, content, username_for_entry, handle_for_entry, biograph_for_entry, song_name, artist_name, artist_name_id, genre_name):
	from comments.models import Comment
	comment_instance = Comment.objects.create(
		comment=comment,
		user=create_test_user(
			username=username_for_comment,
			handle=handle_for_comment,
			biograph=biograph_for_comment
		),
		entry=create_test_entry(
			title=title,
			content=content,
			username=username_for_entry,
			handle=handle_for_entry,
			biograph=biograph_for_entry,
			song_name=song_name,
			artist_name=artist_name,
			artist_name_id=artist_name_id,
			genre_name=genre_name
		)
	)
	return comment_instance
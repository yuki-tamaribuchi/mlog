# Generated by Django 3.2.4 on 2021-08-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0016_song_spotify_preview_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artwork_url',
            field=models.URLField(blank=True),
        ),
    ]

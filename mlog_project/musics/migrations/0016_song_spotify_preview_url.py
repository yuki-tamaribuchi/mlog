# Generated by Django 3.2.4 on 2021-08-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0015_alter_artist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='spotify_preview_url',
            field=models.URLField(blank=True),
        ),
    ]

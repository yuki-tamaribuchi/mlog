# Generated by Django 3.2.4 on 2021-08-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0012_remove_artist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]

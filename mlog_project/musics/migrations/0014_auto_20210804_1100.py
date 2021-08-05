# Generated by Django 3.2.4 on 2021-08-04 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0013_artist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artist_name_id',
        ),
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Unique Artist ID'),
        ),
    ]

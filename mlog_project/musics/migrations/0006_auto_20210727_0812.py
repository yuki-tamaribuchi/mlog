# Generated by Django 3.2.4 on 2021-07-26 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0005_auto_20210726_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='belong_to',
        ),
        migrations.AddField(
            model_name='artist',
            name='belong_to',
            field=models.ManyToManyField(blank=True, related_name='_musics_artist_belong_to_+', to='musics.Artist'),
        ),
    ]
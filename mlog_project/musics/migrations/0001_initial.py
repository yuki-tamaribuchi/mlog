# Generated by Django 3.2.4 on 2021-06-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=30)),
                ('artist_name_id', models.CharField(max_length=30, unique=True)),
                ('artist_biograph', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=30)),
                ('artist', models.ManyToManyField(to='musics.Artist')),
                ('genre', models.ManyToManyField(to='musics.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ManyToManyField(to='musics.Genre'),
        ),
    ]

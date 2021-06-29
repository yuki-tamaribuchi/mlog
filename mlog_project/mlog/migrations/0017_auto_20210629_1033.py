# Generated by Django 3.2.4 on 2021-06-29 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20210629_1033'),
        ('favorite_artists', '0002_alter_favoriteartist_artist'),
        ('musics', '0007_auto_20210629_1000'),
        ('mlog', '0016_auto_20210628_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.AlterField(
            model_name='entry',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='musics.song'),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]

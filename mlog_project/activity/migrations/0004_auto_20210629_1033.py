# Generated by Django 3.2.4 on 2021-06-29 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0007_auto_20210629_1000'),
        ('activity', '0003_userdetailcheckedactivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistcheckedactivity',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics.artist'),
        ),
        migrations.AlterField(
            model_name='songcheckedactivity',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics.song'),
        ),
    ]
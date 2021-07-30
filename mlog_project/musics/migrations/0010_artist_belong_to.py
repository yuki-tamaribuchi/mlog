# Generated by Django 3.2.4 on 2021-07-28 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0009_delete_belongto'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='musics.artist'),
        ),
    ]
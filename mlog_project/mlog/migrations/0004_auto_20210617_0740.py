# Generated by Django 3.2.4 on 2021-06-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlog', '0003_auto_20210614_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_biograph',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_name_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

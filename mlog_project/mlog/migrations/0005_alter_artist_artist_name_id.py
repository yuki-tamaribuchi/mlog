# Generated by Django 3.2.4 on 2021-06-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlog', '0004_auto_20210617_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artist_name_id',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
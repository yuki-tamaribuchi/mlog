# Generated by Django 3.2.4 on 2021-08-04 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0014_auto_20210804_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.SlugField(verbose_name='Unique Artist ID'),
        ),
    ]
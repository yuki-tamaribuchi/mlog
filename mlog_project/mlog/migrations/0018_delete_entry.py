# Generated by Django 3.2.4 on 2021-06-29 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_alter_like_entry'),
        ('comments', '0002_alter_comment_entry'),
        ('mlog', '0017_auto_20210629_1033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]

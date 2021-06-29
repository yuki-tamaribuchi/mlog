# Generated by Django 3.2.4 on 2021-06-29 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_auto_20210629_0921'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO musics_song (
            id,
            song_name
        )
        SELECT
            id,
            song_name
        FROM
            mlog_song;
        """,reverse_sql="""
        INSERT INTO mlog_song (
            id,
            song_name
        )
        SELECT
            id,
            song_name
        FROM
            musics_song;
        """)
    ]

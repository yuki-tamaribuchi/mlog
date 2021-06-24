# Generated by Django 3.2.4 on 2021-06-24 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mlog', '0006_readhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readhistory',
            name='entry',
        ),
        migrations.AddField(
            model_name='readhistory',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mlog.entry'),
        ),
        migrations.AlterField(
            model_name='readhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-29 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20210629_1321'),
        ('activity', '0004_auto_20210629_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryreadactivity',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.entry'),
        ),
    ]

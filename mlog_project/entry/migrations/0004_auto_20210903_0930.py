# Generated by Django 3.2.4 on 2021-09-03 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_auto_20210903_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
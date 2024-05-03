# Generated by Django 5.0.4 on 2024-05-03 22:31

import signature.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='filename',
            field=models.CharField(default=signature.utils.generate_filename, max_length=200),
        ),
        migrations.AlterField(
            model_name='key',
            name='token',
            field=models.CharField(default=signature.utils.generate_key, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='jshshr',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
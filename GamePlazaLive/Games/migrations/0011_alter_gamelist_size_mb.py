# Generated by Django 4.2.6 on 2023-11-13 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0010_gamelist_size_mb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelist',
            name='size_mb',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=10, validators=[django.core.validators.MaxValueValidator(100000000.0), django.core.validators.MinValueValidator(0.01)]),
        ),
    ]

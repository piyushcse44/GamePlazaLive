# Generated by Django 4.2.6 on 2023-11-12 16:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0002_alter_gamelist_description_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Unknown', max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Unknown', max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='reviews',
            name='Rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.0)]),
        ),
    ]

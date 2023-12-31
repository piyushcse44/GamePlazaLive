# Generated by Django 4.2.6 on 2023-11-13 05:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Games', '0011_alter_gamelist_size_mb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone_no', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='assets/images/userimages')),
                ('gamelist', models.ManyToManyField(to='Games.gamelist')),
            ],
        ),
    ]

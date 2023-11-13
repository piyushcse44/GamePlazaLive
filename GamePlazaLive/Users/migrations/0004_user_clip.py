# Generated by Django 4.2.6 on 2023-11-13 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_profile_options_profile_userid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_clip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clip_title', models.CharField(max_length=200)),
                ('user_clip', models.FileField(upload_to='assests/videos/clip_video')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.profile')),
            ],
        ),
    ]

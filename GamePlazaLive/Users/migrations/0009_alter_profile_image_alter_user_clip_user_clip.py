# Generated by Django 4.2.6 on 2023-11-13 11:35

import Users.default
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_user_clip_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=Users.default.default_profile_image, upload_to='assets/images/userimages'),
        ),
        migrations.AlterField(
            model_name='user_clip',
            name='user_clip',
            field=models.FileField(default=Users.default.default_clip_video, upload_to='assests/videos/clip_video'),
        ),
    ]
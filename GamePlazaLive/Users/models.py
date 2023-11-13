from django.db import models
import uuid
from Games.models import GameList
from django.contrib.auth.models import User
from autoslug.fields import AutoSlugField
from .default import default_clip_video,default_profile_image

# Create your models here.

# it contain all information about user for profile section
class Profile(models.Model):

    profile_id = models.UUIDField(unique=True,primary_key=True,editable=False,default=uuid.uuid4)
    userid = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=False,blank=False)
    email = models.EmailField(max_length=200,null=False,blank=False)
    phone_no = models.CharField(max_length=20,null=False,blank=False)
    image = models.ImageField(upload_to='assets/images/userimages',default=default_profile_image)
    gamelist = models.ManyToManyField(GameList)
    friend = models.ManyToManyField('Profile',symmetrical=True)

    class Meta:
        ordering=['name']
    
    def __str__(self):
        return self.name
    

#this contain all clip of every profile
class User_clip(models.Model):

    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False,blank=False)
    clip_title = models.CharField(max_length=200,null=False,blank=False)
    slug = AutoSlugField(populate_from='clip_title', unique=True)
    user_clip = models.FileField(upload_to='assests/videos/clip_video',null=False,blank=False,default=default_clip_video)
    views = models.PositiveBigIntegerField(default=0)
    likes = models.PositiveBigIntegerField(default=0)
    dislikes = models.PositiveBigIntegerField(default=0)

    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clip_title
   
    class Meta:
        ordering = ['upload_date']



    


    




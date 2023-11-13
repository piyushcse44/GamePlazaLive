from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .constants import DevicesChoice
import uuid
from django.contrib.auth.models import User

# this class includes the basic information about games
class GameList(models.Model):

   
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    name = models.CharField(max_length=200,unique=True,null=False,blank=False)
    developer = models.CharField(max_length=200,null=False,blank=False,default="Unknown")
    company_name = models.CharField(max_length=200,null=False,blank=False,default="Unknown")
    size_mb =  models.DecimalField(
        max_digits=10,decimal_places=2, 
        default=0.01,validators=[MaxValueValidator(100000000.0), MinValueValidator(0.01)])
    language = models.CharField(max_length=200,null=False,blank=False,default="Unknown")
    genera = models.ManyToManyField('Genera')
 #  live_streaming = models.BooleanField(default=False)  
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False,default=0.00)
    feature_image = models.ImageField(upload_to='assets/images/gameimages',default='assets/images/gameimages/default.png')
    about = models.CharField(max_length=200,null=False,blank=True,default="Nothing")
    description = models.TextField(null=True,blank=True)
    download_link = models.URLField(max_length=200,null=True,blank=True)
    pros = models.ManyToManyField('Pros')
    cons = models.ManyToManyField('Cons')
    device = models.CharField(max_length=10,choices=DevicesChoice)
    total_downloads = models.IntegerField( validators=[MaxValueValidator(10000000000000), MinValueValidator(0)],default=0)
    Rating = models.DecimalField(
        max_digits=2,decimal_places=1, 
        default=0,validators=[MaxValueValidator(5.0), MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-total_downloads']
    

# this class include reviews of games by any user
class Reviews(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    game_list = models.ForeignKey(GameList,on_delete=models.CASCADE)
    Rating = models.DecimalField(
        max_digits=2,decimal_places=1, 
        default=0,validators=[MaxValueValidator(5.0), MinValueValidator(0.0)])
    body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.game_list.name
    


#this class contain all possible  pros  of a game present in gamelist
class Pros(models.Model):
   
    title = models.CharField(max_length=200,null=False,blank=False,default="Unknown")
    body = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.title
    


#this class contain all possible  cons  of a game present in gamelist
class Cons(models.Model):
   
    title = models.CharField(max_length=200,null=False,blank=False,default="Unknown")
    body = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.title    

#this class contains all categry of each game  present  in gamelist 
class Genera(models.Model):

    title = models.CharField(max_length=200,null=False,blank=False,unique=True)

    def __str__(self):
        return self.title
    

# this class contains all Additional images of each game in gamelist    
class AdditionalImages(models.Model):

    game_list = models.ForeignKey(GameList,on_delete=models.CASCADE)
    game_list_image = models.ImageField(upload_to='assets/images/gameimages',default='assets/images/gameimages/default.png')


    def __str__(self):
        return self.game_list.name

 





    


    


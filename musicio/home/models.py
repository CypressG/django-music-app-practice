from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class User(AbstractUser):
    PUBLISHER = 1
    MODERATOR = 2
    USER = 3
    ROLE_CHOICES = (
        (PUBLISHER, 'Publisher'), (MODERATOR, 'Moderator'),(USER,'User')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=ROLE_CHOICES[2][0])
    pass

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    FK_user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,default=None)

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    FK_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default=None)
    description = models.CharField(max_length=100)

class Moderator(models.Model):
    id = models.AutoField(primary_key=True)
    FK_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default=None)

class SongInfo(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=5)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,default="Unknown")
    description = models.TextField(max_length=400)
    author = models.CharField(max_length=300,default="Unknown")
    composer = models.CharField(max_length=300,default="Unknown")
    song_url = models.TextField(max_length=1000,default="Not have")
    FK_moderator = models.ForeignKey(Moderator,on_delete=models.CASCADE,blank=True,null=True,default=None)
    FK_genre = models.ForeignKey(Genre,on_delete=models.CASCADE,blank=True,null=True,default=None)
    FK_publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,blank=True,null=True,default=None)
    FK_song_info = models.ForeignKey(SongInfo,on_delete=models.CASCADE,blank=True,null=True,default=None)
    published = models.BooleanField(default=False)
    DOR = models.DateTimeField(blank=True,auto_now=True)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=0)

class OrderHistory(models.Model):
    id = models.AutoField(primary_key=True)
    FK_order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    FK_song = models.ForeignKey(Song,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    FK_user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,default=None)

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_payment = models.CharField(max_length=200)
    FK_user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,default=None)

class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    FK_song = models.ForeignKey(Song,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    FK_user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    FK_order =  models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    

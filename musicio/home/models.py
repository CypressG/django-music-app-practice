from django.db import models

# Create your models here.

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Account(models.Model):
    username = models.CharField(primary_key=True,max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Adress(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    FK_account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)

class Publisher(models.Model):
    id = models.IntegerField(primary_key=True)
    FK_account = models.ForeignKey(Account,on_delete=models.CASCADE)
    publisher_label = models.CharField(max_length=100)

class Library(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.FloatField(max_length=8)
    quantity = models.IntegerField()
    rating = models.IntegerField()

class Moderator(models.Model):
    id = models.IntegerField(primary_key=True)
    FK_account = models.ForeignKey(Account,on_delete=models.CASCADE)

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    last_price = models.FloatField()
    price_date = models.DateTimeField()

class Inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    FK_account = models.ForeignKey(Account,on_delete=models.CASCADE)
    FK_order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)

class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=400)
    FK_moderator = models.ForeignKey(Moderator,on_delete=models.CASCADE)
    FK_library = models.ForeignKey(Library,on_delete=models.CASCADE)
    FK_genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    FK_publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)

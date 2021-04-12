from django.contrib import admin
from .models import Genre, Account,Adress,Publisher,Library,Moderator,Order,Inventory,Song
# Register your models here.
admin.site.register(Genre)
admin.site.register(Account)
admin.site.register(Adress)
admin.site.register(Publisher)
admin.site.register(Library)
admin.site.register(Moderator)
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(Song)
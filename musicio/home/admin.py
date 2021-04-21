from django.contrib import admin
from .models import Genre, User,Address,Publisher,Song,Moderator,Basket,SongInfo,Order,OrderHistory
# Register your models here.
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Publisher)
admin.site.register(Order)
admin.site.register(Moderator)
admin.site.register(Basket)
admin.site.register(Song)
admin.site.register(OrderHistory)
admin.site.register(SongInfo)

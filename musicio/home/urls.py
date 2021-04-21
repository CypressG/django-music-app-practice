from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name="register"),
    path('login/',views.login_view,name="login"),
    path('add/',views.add_wish,name='add'),
    path('delete/',views.delete_wish,name='delete'),
    path('logout/',views.logout_profile,name='logout'),
    path('basket/',views.basket,name="basket"),
    path('basket/delete',views.delete_wish_from_basket,name="basket_delete"),
    path('order/',views.order, name="order"),
    path('history/',views.history,name="history"),
    path('publish/',views.publish, name='publish'),
    path('add/song/',views.add_song, name='add_song'),
    path('delete/song/',views.delete_song, name='delete_song'),
    path('publisher/',views.publisher, name='publisher'),
    path('moderator/delete',views.moderator_delete_song,name="mod_delete")
]
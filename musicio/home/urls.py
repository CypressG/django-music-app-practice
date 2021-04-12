from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('pavyzdys', views.example, name="example"),
    path('pavyzdys/<int:test>',views.deeper,name="deeper")
]
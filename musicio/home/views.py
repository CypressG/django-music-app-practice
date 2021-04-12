from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Account
from django.apps import apps

def index(request):
    accounts = Account.objects.all()   
    models = apps.all_models['home']
    
    return render(request,'home/index.html',{
        'accounts': accounts,
        'models':models,
    })

def example(request):
    return HttpResponse("Example")

def deeper(request):
    return render(request,'home/index.html')
    
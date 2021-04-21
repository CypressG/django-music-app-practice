from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User, Song, Basket, Order, OrderHistory, Publisher,Genre
from django.apps import apps
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from .forms import AddSong,SongInfo, Search

@xframe_options_exempt
def index(request):
    current_user = request.user
    id = current_user.id
    if current_user.is_anonymous:
        render(request,'home/index.html',{
            "search": Search()

        })

    elif current_user.role == 1:
        return render(request, 'home/publisher.html', {
            "search": Search()

        })
    elif current_user.role == 2:
        songs = Song.objects.filter(published=0)

        return render(request, 'home/moderator.html', {
            "songs":songs,
            "search": Search()

        })
    baskets = Basket.objects.filter(FK_user=id)
    basket_songs = []
    for basket in baskets:
        basket_songs.append(basket.FK_song.id)
    songs = Song.objects.filter(published=1)
    models = apps.all_models['home']
    return render(request, 'home/index.html', {
            'user': current_user,
            'models': models,
            'songs': songs,
            'baskets': baskets,
            'basket_songs': basket_songs,
            'idd': id,
            "search": Search()
            })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if (username == "" or email == "" or
            password == "" or confirmation ==""):
            return render(request, "home/register.html", {
                "message": "You have to input all the fields."
            })        
        if password != confirmation:
            return render(request, "home/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()   
        except IntegrityError:
            return render(request, "home/register.html", {
                "message": "Username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("home:index"))
    else:
        return render(request, "home/register.html")


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home:index"))
        else:
            return render(request, "home/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")


def add_wish(request):
    if (request.method == 'POST' and
            request.user.is_authenticated):
        user = User.objects.get(id=request.POST.get('user'))
        song = Song.objects.get(id=request.POST.get('song'))
        try:
            Basket.objects.get(FK_user=user, FK_song=song)
            return HttpResponseRedirect(reverse('home:index'))
        except Basket.DoesNotExist:
            Basket.objects.create(FK_user=user, FK_song=song).save()
            return HttpResponseRedirect(reverse('home:index'))
    return HttpResponse("You're not logged in")


def delete_wish(request):
    if (request.method == 'POST' and
            request.user.is_authenticated):
        user = User.objects.get(id=request.POST.get('user'))
        song = Song.objects.get(id=request.POST.get('song'))
        Basket.objects.filter(FK_user=user, FK_song=song).delete()
        return HttpResponseRedirect(reverse('home:index'))
    return HttpResponse("You're not logged in")


def delete_wish_from_basket(request):
    if (request.method == 'POST' and
            request.user.is_authenticated):
        user = User.objects.get(id=request.POST.get('user'))
        song = Song.objects.get(id=request.POST.get('song'))
        Basket.objects.filter(FK_user=user, FK_song=song).delete()
        return HttpResponseRedirect(reverse('home:basket'))
    return HttpResponse("You're not logged in")


def logout_profile(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))


def basket(request):
    sum = 0
    basket_items = Basket.objects.filter(FK_user=request.user)
    for basket_item in basket_items:
        sum += basket_item.FK_song.FK_song_info.price
    return render(request, 'home/basket.html', {
        "basket_items": basket_items,
        "sum": sum,
    })


def order(request):
    if (request.method == 'POST' and
            request.user.is_authenticated):
        order_item = Order.objects.create()
        order_item.status = 1
        order_item.save()
        basket_items = Basket.objects.filter(FK_user=request.user)
        basket_items.update(FK_order=order_item)
        for basket_item in basket_items:
            order = OrderHistory.objects.create(
                FK_user=request.user, FK_order=order_item, FK_song=basket_item.FK_song)
        basket_items.delete()
        return HttpResponseRedirect(reverse('home:basket'))
    return HttpResponse("works")


def history(request):
    orders = OrderHistory.objects.filter(FK_user=request.user)
    return render(request, 'home/history.html', {
        "orders": orders,
    })


def publish(request):
    if (request.method == "POST" and 
        request.user.is_authenticated):
        song = Song.objects.get(id=request.POST.get('song'))
        song.published = True
        song.save()
        return HttpResponseRedirect(reverse('home:index'))
    return HttpResponse("Yra")

def add_song(request):
    if (request.method == "POST" and
        request.user.role == 1):
            form = AddSong(request.POST)
            if form.is_valid():
                begin = "src= "
                end = " width=700 height=90 frameborder=0 allowtransparency=true allow=encrypted-media"
                url_link = form.cleaned_data["song_url"]
                name = form.cleaned_data["name"]
                composer = form.cleaned_data["composer"]
                author = form.cleaned_data['author']
                description = form.cleaned_data['description']
                genre = form.cleaned_data['genre']
                song_url = begin + url_link + end
                publisher = request.user.id
                publisher = Publisher.objects.get(FK_user=User.objects.get(id=request.user.id))
                Song.objects.create(name=name,description=description,author=author, composer=composer,song_url=song_url,FK_publisher=publisher).save()
                return HttpResponseRedirect(reverse('home:index'))
            else:
                return HttpResponse(form.is_valid())
    return render(request,'home/add.html',{
        "form": AddSong(),
        "form_price": SongInfo(),

    })

def publisher(request):
    user = User.objects.get(id=request.user.id)
    publisher = Publisher.objects.get(FK_user=user)
    songs = Song.objects.filter(FK_publisher=publisher)
    return render(request,'home/publisher.html',{
        "songs" : songs,
        "user":user,
        "publisher":publisher
    })

def delete_song(request):
    if (request.user.role == 1 or
    request.user.role == 2):
        if request.method == "POST":
            song = Song.objects.filter(id=request.POST.get('song')).delete()
            return HttpResponseRedirect(reverse('home:index'))
        else:
            user = User.objects.get(id=request.user.id)
            list_of_songs = Song.objects.filter(FK_publisher=Publisher.objects.get(FK_user=user))
            return render(request, 'home/delete.html', {
                "songs":list_of_songs,
            }) 
def search(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Search(request.POST)
        # check whether it's valid:
        if form.is_valid():
            genre = form.cleaned_data['genre']
            item = form.cleaned_data['item']
            if genre == "Any":
                return render(request,'home/search.html',{
                    "songs":Song.objects.filter(name__contains=item)
                })
            else:
                exact = Genre.objects.filter(id=genre)
                return render(request,'home/search.html',{
                    "songs": Song.objects.filter(FK_genre=exact[0])
                })
            return render(request,'home/search.html',{
            "genre":genre,
            "item":item
    })
    return HttpResponseRedirect(reverse('home:index'))


def moderator_delete_song(request):
    if request.user.role == 2:
        if request.method == "POST":
            Song.objects.filter(id=request.POST.get('song')).delete()
        else:
            songs = Song.objects.all()
            return render(request, 'home/delete.html',{
                "songs":songs
            })
    pass
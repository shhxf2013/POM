from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
# from datetime import datetime
from .models import City, Continente, Place, Photo
from .forms import CityForm, PlaceForm

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username and password does not match.')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')
            
    return render(request, 'base/login_register.html', {'form':form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    cities = City.objects.filter(
        Q(continente__name__icontains=q) |
        Q(name__icontains=q) |
        Q(country__icontains=q)
        )
    continentes = Continente.objects.all()
    city_count = cities.count()
    context = {
        'cities':cities,
        'continentes': continentes
    }
    return render(request, 'base/home.html', context)

def city(request, pk):
    city = City.objects.get(id=pk)
    city_places = city.place_set.all().order_by('-created')
    context = {
        'city':city,
        'places': city_places,
    }
    return render(request, 'base/cityPage.html', context)

@login_required(login_url='login')
def addCity(request):
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.user = request.user
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/city_form.html', context)

@login_required(login_url='login')
def updateCity(request, pk):
    city = City.objects.get(id=pk)
    form = CityForm(instance=city)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/city_form.html', context)

@login_required(login_url='login')
def deleteCity(request, pk):
    city = City.objects.get(id=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':city})

def place(request,pk):
    place = Place.objects.get(id=pk)
    context = {'place': place}
    return render(request, 'base/placePage.html')

@login_required(login_url='login')
def addPlace(request):
    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/place_form.html', context)

@login_required(login_url='login')
def updatePlace(request, pk):
    place = Place.objects.get(id=pk)
    form = PlaceForm(instance=place)
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/place_form.html', context)

@login_required(login_url='login')
def deletePlace(request,pk):
    place = Place.objects.get(id=pk)
    if request.user != place.user:
        return HttpResponse('You do not have the right to make this operation')

    if request.method == 'POST':
        place.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':place})

@login_required(login_url='login')
def addPhoto(request):
    context = {}
    return render(request, '', context)

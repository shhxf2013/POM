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
from .models import City, Continente, Place
from .forms import CityForm

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
    # city_locOfInts = city.locOfInt_set.all()
    # tags = city.tags.all()
   
    context = {
        'city':city,
        # 'city_locOfInts': city_locOfInts,
        # 'tags': tags
    }
    return render(request, 'base/cityPage.html', context)

@login_required(login_url='login')
def addCity(request):
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
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

@login_required(login_url='login')
def deletePlace(request,pk):
    place = Place.objects.get(id=pk)
    if request.user != place.user:
        return HttpResponse('You do not have the right to make this operation')

    if request.method == 'POST':
        place.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':place})

def detail(request):
    
    return render(request, 'base/detailPage.html')
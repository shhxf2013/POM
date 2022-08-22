from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    path('', views.home, name="home"),
    path('city/<str:pk>/', views.city, name="city"),
    path('add-city/', views.addCity, name='add-city'),
    path('update-city/<str:pk>/', views.updateCity, name='update-city'),
    path('delete-city/<str:pk>/', views.deleteCity, name='delete-city'),
    path('place/<str:pk>/', views.place, name="place"),
    path('add-place/', views.addPlace, name='add-place'),
    path('update-place/<str:pk>/', views.updatePlace, name='update-place'),
    path('delete-place/<str:pk>/', views.deletePlace, name='delete-place'),

]
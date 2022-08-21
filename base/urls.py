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

]
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Continente(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True)
    continente = models.ForeignKey(Continente, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class LocOfInt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    # latLong =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # comment =

    def __str__(self):
        return self.name

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    price = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=50, null=True)
    # latLong =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
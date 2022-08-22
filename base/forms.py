from django.forms import ModelForm
from .models import City, Place

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        exclude = ['user']

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        exclude = ['user']


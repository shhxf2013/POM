from django.urls import path
from myMap.views import MapView

app_name = 'myMap'
urlpatterns = [
    path('map/', MapView.as_view()),

]
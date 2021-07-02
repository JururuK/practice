from django.urls import path

from countapp.views import hello_world
app_name = 'countapp'
urlpatterns = [
    path('hello_world/', hello_world, name='Hello world')
]
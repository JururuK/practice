from django.urls import path

from myself.views import introduce

app_name = 'myself'
urlpatterns = [
    path('intro/', introduce, name='introduce')
]
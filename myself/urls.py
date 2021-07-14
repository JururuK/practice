from django.urls import path

from myself.views import introduce, AccountCreateView

app_name = 'myself'
urlpatterns = [
    path('intro/', introduce, name='introduce'),
    path('create/', AccountCreateView.as_view(), name = 'create')
]
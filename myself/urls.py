from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from myself.views import introduce, AccountCreateView

app_name = 'myself'
urlpatterns = [
    path('intro/', introduce, name='introduce'),
    path('login/', LoginView.as_view(template_name='myself/login.html'),
         name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create')
]
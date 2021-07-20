from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from myself.views import introduce, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'myself'
urlpatterns = [
    path('intro/', introduce, name='introduce'),
    path('login/', LoginView.as_view(template_name='myself/login.html'),
         name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), #숫자를 받을것. primary key
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
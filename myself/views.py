from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from myself.decorators import account_ownership_required
from myself.forms import AccountCreationForm
from myself.models import NewModel

#view 간단히.

class AccountCreateView(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list') #함수에서는 reverse, class 에서는 reverse_lazy
    template_name = 'myself/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin) :
    model = User
    context_object_name = 'target_user'
    template_name = 'myself/detail.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,**kwargs)
has_ownership = [login_required,account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')

class AccountUpdateView(UpdateView) : #수정할 객체를 찾고, 저장하는 과정
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'myself/update.html'

    def get_success_url(self):
        return reverse('myself:detail',kwargs={'pk':self.object.pk})

has_ownership = [login_required,account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('myself:login')
    template_name = 'myself/delete.html'


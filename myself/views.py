from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from myself.models import NewModel


def introduce(myself) :
    if myself.method == "POST": #추후에 경로를 특정하기 위해(헷갈림방지) myself(앱이름)폴더를 하나더 만들고 html파일을 넣어줌

        temp = myself.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save() #사용자가 입력한 값을 db에 저장

        # post 만들어주고나서 get 으로 재연결. 안그러면 새로고침할때 입력안해도 추가됨.

        return HttpResponseRedirect(reverse('myself:introduce')) #urls.py 안에 있는 내용

    else :
        data_list = NewModel.objects.all()
        return render(myself, 'myself/intro.html',
                      context={'data_list': data_list})



#view 간단히.

class AccountCreateView(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('myself:introduce') #함수에서는 reverse, class 에서는 reverse_lazy
    template_name = 'myself/create.html'
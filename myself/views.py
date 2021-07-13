from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myself.models import NewModel


def introduce(myself) :
    if myself.method == "POST": #추후에 경로를 특정하기 위해(헷갈림방지) myself(앱이름)폴더를 하나더 만들고 html파일을 넣어줌

        temp = myself.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save() #사용자가 입력한 값을 db에 저장

        data_list = NewModel.objects.all()

        return render(myself, 'myself/intro.html',
                      context={'data_list': data_list})
    else :
        data_list = NewModel.objects.all()
        return render(myself, 'myself/intro.html',
                      context={'data_list': data_list})
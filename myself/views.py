from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def introduce(myself) :
    return render(myself, 'myself/intro.html') #추후에 경로를 특정하기 위해(헷갈림방지) myself(앱이름)폴더를 하나더 만들고 html파일을 넣어줌
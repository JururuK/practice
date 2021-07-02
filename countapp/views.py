from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!!!!!') #빨간줄 위에 알트 엔터 누르면 관련된 라이브러리 추천
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def introduce(myself) :
    return render(myself, 'index.html')
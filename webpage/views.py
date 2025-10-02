from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

#AQUI TIENEN QUE DEFINIR LAS URLS DE LAS PAGINAS Y Eso
def index(request):
    return render(request, 'index.html')
# Create your views here.
def historia(request):
    return render(request, 'historia.html')
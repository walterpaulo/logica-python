from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import request

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def tamplate(resques):
    return render(request, 'index.html')

def html_bruto(request):
    resposta = {}
    resposta["conteudo"] = "Agora com API JSON"
    return HttpResponse("<h1>respondendo por html</h1>")

def json(request):
    resposta = {}
    resposta["conteudo"] = "Agora com API JSON"
    return JsonResponse(resposta)
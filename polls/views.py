from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world</h1>")

def meme(request):
    return HttpResponse("https://upload.wikimedia.org/wikipedia/ru/4/4d/Wojak.png")
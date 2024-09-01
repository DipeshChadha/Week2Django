from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("Hello, world. 5e5d15a4 is the polls index.")

from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the Generic Types index.")

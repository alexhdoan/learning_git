from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import ConsumableRequest

def index(request):
    request_list = ConsumableRequest.objects.filter(status = "R")
    template = loader.get_template('transactions/index.html')
    context = {
        'request_list': request_list,
    }
    return HttpResponse(template.render(context, request))

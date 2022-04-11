from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def hello_world (request):
    now = datetime.now()
    return (HttpResponse('Hi, Current server time is {now}'.format(now=str(now))))

def hi(request,name,age):
    if (age >= 18):
        return (HttpResponse(f'Bienvenido, {name}' ))
    else: 
        return (HttpResponse('Acceso denegado'))


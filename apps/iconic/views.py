from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Iconic

def index(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        iconic = Iconic.objects.all()
        template = loader.get_template('nehal/iconic.html')
        context = {'iconic_places': iconic}
        return HttpResponse(template.render(context,request))


def about(request):
    template = loader.get_template('nehal/icon.html')
    return HttpResponse(template.render({},request))

def festival(request):
    template = loader.get_template('nehal/festival.html')
    return HttpResponse(template.render({},request))

def events(request):
    template = loader.get_template('nehal/events.html')
    return HttpResponse(template.render({},request))

def experience(request):
    template = loader.get_template('nehal/experience.html')
    return HttpResponse(template.render({},request))

def nearby(request):
    template = loader.get_template('nehal/nearby.html')
    return HttpResponse(template.render({},request))
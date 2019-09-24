from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template("nehal/experience.html")
    """View function for home page of site."""
    return HttpResponse(template.render({}, request))

def iconic(request):
    template = loader.get_template('nehal/iconic.html')
    return HttpResponse(template.render({},request))

def events(request):
    template = loader.get_template('nehal/events.html')
    return HttpResponse(template.render({},request))

def festival(request):
    template = loader.get_template('nehal/festival.html')
    return HttpResponse(template.render({},request))

def nearby(request):
    template = loader.get_template('nehal/nearby.html')
    return HttpResponse(template.render({},request))


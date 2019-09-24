from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Events

def index(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Event = Events.objects.all()
        template = loader.get_template('nehal/events.html')
        context = {'hotel_images': Event}
        return HttpResponse(template.render(context,request))


def eventExplore(request):
    template = loader.get_template('nehal/eventExplore.html')
    return HttpResponse(template.render({},request))

def iconic(request):
    template = loader.get_template('nehal/iconic.html')
    return HttpResponse(template.render({},request))

def festival(request):
    template = loader.get_template('nehal/festival.html')
    return HttpResponse(template.render({},request))

def experience(request):
    template = loader.get_template('nehal/experience.html')
    return HttpResponse(template.render({},request))

def nearby(request):
    template = loader.get_template('nehal/nearby.html')
    return HttpResponse(template.render({},request))


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Icon

def index(request,name):
    if request.method == 'GET':
        # getting all the objects of hotel.
        icon = Icon.objects.all().filter(name=name)
        template = loader.get_template('nehal/icon.html')
        context = {'icon_places': icon}
        return HttpResponse(template.render(context,request))
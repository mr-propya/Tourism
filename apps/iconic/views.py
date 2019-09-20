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
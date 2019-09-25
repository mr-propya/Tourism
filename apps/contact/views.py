from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template("musu/contact-us.html")
    """View function for home page of site."""
    return HttpResponse(template.render({}, request))
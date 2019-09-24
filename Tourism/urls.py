"""Tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('icon/',include('apps.icon.urls')),
    path('about/', include('apps.iconic.urls')),
    path('eventExplore/',include('apps.events.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('iconic/', include('apps.iconic.urls')),
    path('nearby/', include('apps.nearby.urls')),
    path('home/', include('apps.home.urls')),
    path('events/', include('apps.events.urls')),
    path('experience/', include('apps.experience.urls')),
    path('festival/', include('apps.festival.urls'))
]

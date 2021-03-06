from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('iconic/', views.iconic, name="iconic"),
    path('events/', views.events, name="events"),
    path('festival/', views.festival, name="festival"),
    path('nearby/', views.nearby, name="nearby"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
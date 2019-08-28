from django.db import models


class GalleryImage(models.Model):
    displayText = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=500)


class GalleryVideo(models.Model):
    displayText = models.CharField(max_length=100)
    videoUrl = models.CharField(max_length=500)

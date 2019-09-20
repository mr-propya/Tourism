from django.db import models

class Iconic(models.Model):
    name = models.CharField(max_length=50)
    directUrl = models.CharField(max_length=100,default="asdadsd")
    description = models.CharField(max_length=500,default="abc")

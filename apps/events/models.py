from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=50)
    directUrl = models.CharField(max_length=100,default="asdadsd")
    startDate = models.CharField(max_length=50,default="5/5/2019")
    endDate = models.CharField(max_length=50,default="6/5/2019")
    startTime = models.CharField(max_length=50,default="15:00pm")
    endTime = models.CharField(max_length=50,default="15:00pm")
    description = models.CharField(max_length=500,default="abc")
    venue = models.CharField(max_length=100,default="bcd")
    address = models.CharField(max_length=100,default="cde")
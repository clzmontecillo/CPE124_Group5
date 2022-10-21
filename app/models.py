from django.db import models


class Sensor(models.Model):
    temperature = models.CharField(max_length=200)
    humidity = models.CharField(max_length=200)
    
class Thresh(models.Model):
    thresh_temp = models.CharField(max_length=200)
    thresh_humidity = models.CharField(max_length=200)
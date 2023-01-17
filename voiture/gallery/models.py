from django.contrib import admin
from django.db import models


class cars(models.Model):
    energie =[("diesel","diesel"),("essance","essance")]
    model= models.CharField(max_length=200)
    prix= models.IntegerField()
    carburant= models.CharField(max_length=200,choices=energie)
    marque = models.CharField(max_length=200)
    image =models.ImageField(null=True)
from django.contrib import admin
from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=200)
    prénom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mot_de_passe = models.CharField(max_length=200)
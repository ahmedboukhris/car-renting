from django.urls import path
from .views import formulaire,connexion
urlpatterns=[
    path('',formulaire,name='formulaire'),
    path('client',connexion,name='connexion'),
]
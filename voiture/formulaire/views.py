from django.shortcuts import render,redirect
from .models import Contact
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.
def formulaire(request):
    if request.method =="POST":
        nom=request.POST.get('nom')
        prénom=request.POST.get('prénom')
        email=request.POST.get('email')
        password=request.POST.get('password')
        data=Contact(nom=nom,prénom=prénom,email=email,mot_de_passe=password)
        data.save()
    return render(request,'formulaire.html')
def connexion(request):
     if request.method =="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        data=Contact.objects.all ()
        for i in data:
            if email == i.email and password == i.mot_de_passe:
             return redirect('gallery')
            else:
             message='cette compte n existe pas'
            return render(request,'connexion.html',{'message':message})
     return render(request,'connexion.html')
            

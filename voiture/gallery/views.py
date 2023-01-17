from django.shortcuts import render
from .models import cars

# Create your views here.
def gallery(request):
    return render(request,'gallery.html',{'product':cars.objects.all()})


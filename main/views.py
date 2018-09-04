from django.shortcuts import render

from .models import Catagory


def splash_page(request):
    catagories = Catagory.objects.all()
    return render(request, 'main/splash.html', {'catagories': catagories})

from django.shortcuts import render
from . models import Place
from . models import Person


# Create your views here.
def demo(request):
    s = Place.objects.all()
    return render(request, "index.html", {'result1': s})


def demo1(request):
    x = Person.objects.all()
    return render(request, "index.html", {'result': x})

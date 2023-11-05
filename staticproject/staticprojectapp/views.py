from django.shortcuts import render
from . models import Place
from . models import Person


# Create your views here.
def demo(request):
    Places = Place.objects.all()
    Persons= Person.objects.all()
    result={
        'Places':Places,
        'Persons':Persons,
    }
    return render(request, "index.html", result)

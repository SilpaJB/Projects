from django.shortcuts import render, redirect

from .forms import icecreamForm
from .models import icecream
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    ice = icecream.objects.all()
    context = {'icecream_list': ice}
    return render(request, 'index.html', context)


def detail(request, icecream_id):
    ice = icecream.objects.get(id=icecream_id)
    return render(request, "detail.html", {'icecream': ice})


def add_icecream(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        details = request.POST.get('details', )
        flavours = request.POST.get('flavours', )
        image = request.FILES['image']
        ice = icecream(name=name, details=details, flavours=flavours, image=image)
        ice.save()

    return render(request, "add.html")


def update(request, id):
    ice = icecream.objects.get(id=id)
    form = icecreamForm(request.POST or None, request.FILES, instance=ice)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'ice': ice})


def delete(request, id):
    if request.method == 'POST':
        ice = icecream.objects.get(id=id)
        ice.delete()
        return redirect('/')
    return render(request, 'delete.html')

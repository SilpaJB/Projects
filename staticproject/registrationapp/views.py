import django as django
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        x = request.POST['Username']
        y = request.POST['Password']
        user = auth.authenticate(username=x, password=y)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        x = request.POST['Username']
        y = request.POST['firstname']
        z = request.POST['lastname']
        s = request.POST['Email']
        m = request.POST['Password']
        a = request.POST['Confirm Password']

        if m == a:
            if User.objects.filter(username=x).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=s).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=x, first_name=y, last_name=z, email=s, password=m)

                user.save();
                print("user created")
                return redirect('login')



        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

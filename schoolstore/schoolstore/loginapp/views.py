from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        x = request.POST['Username']
        y = request.POST['Password']
        user = auth.authenticate(username=x, password=y)

        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        x = request.POST['Username']
        m = request.POST['Password']
        a = request.POST['Confirm Password']

        if x and m and a:
            if m == a:
                if User.objects.filter(username=x).exists():
                    messages.info(request, "Username Taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=x, password=m)
                    user.save();
                    print("user created")
                    return redirect('login')
            else:
                messages.info(request, "password not matching")
                return redirect('register')
        else:

            return redirect('register')

        return redirect('/')
    return render(request, "register.html")



def form(request):
    if request.method == "POST":
        name = request.POST.get('Name', '')
        dob = request.POST.get('DOB', '')
        age = request.POST.get('Age', '')
        gender = request.POST.get('Gender', '')
        phoneno = request.POST.get('Phone Number', '')
        mail_id = request.POST.get('Mail Id', '')
        address = request.POST.get('Address', '')
        department = request.POST.get('Department', '')
        courses = request.POST.get('Courses', '')
        purpose = request.POST.get('Purpose', '')
        materials = request.POST.getlist('Materials Provide', [])


        if name and dob and age and gender and phoneno and mail_id and address and department and courses and purpose and materials:

            messages.success(request, "Form submitted successfully")

            return redirect('form')  # Redirect back to the form page
        else:
            messages.error(request, "Please fill in all required fields")
            return redirect('form')

    return render(request, "form.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

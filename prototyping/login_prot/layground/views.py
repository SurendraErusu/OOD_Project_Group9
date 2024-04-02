from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm as UCF
from .forms import NewUserForm
from django.contrib.auth import authenticate, logout, login


# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'forms/register.html',context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Login succesful")
        else:
            print("Login Failed")
    return render(request,"forms/login.html")

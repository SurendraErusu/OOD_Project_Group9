from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from corpcconnect.models import NewUser, CustomUser, AdminUser
from Login.forms import NewUserRegistrationForm, CustomUserLoginForm
from django.http import HttpResponseForbidden

def register(request):
    if request.method == 'POST':
        form = NewUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = NewUserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Login succesful")
        else:
            print("Login Failed")
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

#@staff_member_required
def approve_user(request, new_user_id):
    ##if not isinstance(request.user, AdminUser):
        #print("here")
        #return HttpResponseForbidden("You do not have permission to approve users.")
    #print("JODJO:", new_user_id)
    new_user = NewUser.objects.get(pk=new_user_id)
    admin_user = AdminUser.objects.get(pk=request.user.id)
    admin_user.approve_request(new_user_id)
    return redirect('pending_users')


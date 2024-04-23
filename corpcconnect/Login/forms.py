from django import forms
from django.contrib.auth.forms import UserCreationForm as UCF
from corpcconnect.models import NewUser, CustomUser
from django.contrib.auth import authenticate


class NewUserRegistrationForm(UCF):
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ['username', 'email', 'password', 'company', 'position']
    
class CustomUserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    

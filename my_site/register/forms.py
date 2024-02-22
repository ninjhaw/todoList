from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    # can add fields here dpends on the requirements
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
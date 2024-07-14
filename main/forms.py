from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Habit

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class AddHabitForm(forms.ModelForm):
    class Meta:
        model=Habit
        fields = ['habit']
        
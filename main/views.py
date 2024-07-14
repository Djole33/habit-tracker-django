from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Habit

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'main/register.html', {'form':form})

def my_login(request):
    form = LoginForm(request, data=request.POST)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

    return render(request, 'main/my-login.html', {'form':form})

def user_logout(request):
    auth.logout(request)

    return redirect("my-login")

@login_required(login_url='my-login')
def dashboard(request):
    my_habits = Habit.objects.all()
    
    return render(request, 'main/dashboard.html', {'habits': my_habits})

@login_required(login_url='my-login')
def create_habit(request):
    form = AddHabitForm()
    if request.method == "POST":
        form = AddHabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    return render(request, 'main/create-habit.html', {'form':form})

@login_required(login_url='my-login')
def singular_habit(request, pk):
    all_habits = Habit.objects.get(id=pk)

    return render(request, 'main/view-habit.html', {'habit':all_habits})

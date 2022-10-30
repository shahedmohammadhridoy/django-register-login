from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

def registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created successfully '+ user)
                return redirect('login')


        context = {
            'form':form
        }
        return render(request, 'registration.html', context)
    
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Logged In Success")
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Invalid credential')
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out")
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')
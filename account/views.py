from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import CreateUserForm

def registration(request):
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Logged In Success")
            auth_login(request, user)
            return redirect('dashboard')
        
        
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
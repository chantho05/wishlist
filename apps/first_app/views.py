from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from .forms import RegistrationForm, SignInForm

def index(request):
    registration_form = RegistrationForm()
    signin_form = SignInForm()
    context = { 'registration_form': registration_form,
            'signin_form': signin_form}
    return render(request, 'index.html', context)

def submit_registration(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('/')
        else:
            form.add_error('password_confirm', 'Passwords do not match')
            return render(request, 'index.html', { 'form': form })
    return redirect('/')

def submit_signin(request):
    form = SignInForm(request.POST)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return redirect('/travels')
        else:
            return redirect('/')
    return redirect('/')

def submit_logout(request):
    logout(request)
    return redirect('/')

def travels(request):
    return render(request, "travels.html")

def destination(request):
    return render(request, "destination.html")

def add(request):
    return render(request, 'add.html')


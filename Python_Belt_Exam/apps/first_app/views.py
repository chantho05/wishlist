from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from .forms import RegistrationForm, SignInForm

def main(request):
    registration_form = RegistrationForm()
    signin_form = SignInForm()
    context = { 'registration_form': registration_form,
            'signin_form': signin_form}
    return render(request, 'main.html', context)

def submit_registration(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['password'])
            user.name = form.cleaned_data['name']
            user.save()
            return redirect('/')
        else:
            form.add_error('password_confirm', 'Passwords do not match')
            return render(request, 'dashboard.html', { 'form': form })
    return redirect('/')

def submit_signin(request):
    form = SignInForm(request.POST)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data['name'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    return redirect('/dashboard')

def submit_logout(request):
    logout(request)
    return redirect('/')

def index(request):
    current_user = User.objects.get(id = 1)
    return render(request, 'main.html', {'current_user': current_user, 'user_items': current_user.all_items.all(), 'other_items': Item.objects.all().exclude(all_users = current_user)})

def add(request):    
    if 'current_user' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['user'])
    item = Trip.objects.get(id = id)
    item.all_users.add(user)
    item.save()
    return redirect("/")

def show(request, id):
    if 'current_user' not in request.session:
        return redirect('/')
    item = Item.objects.get(id = id)
    return render(request, 'dashboard.html', {'item': item})

def create(request):
    if 'current_user' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['current_user'])
    item = Trip.objects.create(name = request.POST['name'], added_by = user)
    item.all_users.add(user)
    return redirect('/main')

def logout(request):
    request.session.flush()
    return redirect('/')
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    user_id = users.first().id
    request.session['user_id'] = user_id
    request.session['name'] = users.first().first_name
    if users.count() == 0:
        messages.error(request, 'Unknown email', extra_tags='email')
        return redirect('/')
    if not bcrypt.checkpw(request.POST['password'].encode(), users.first().password.encode()):
        messages.error(request, 'Password invalid', extra_tags='password')
        return redirect('/')
    return redirect('/success')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/')
    User.objects.create(first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], 
        email=request.POST['email'], 
        password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
    return redirect('/success')

def success(request):
    return render(request, 'success.html')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect

def index(request):
    users = User.objects.all()
    context = {
        'all_users': users
    }
    return render(request, 'restful_users/index.html', context)

def new(request):
    return render (request, 'restful_users/new.html')

def add(request):
    User.objects.create(name=request.POST['name'], email=request.POST['email'])
    return redirect('/users')

def show(request, user_id):
    if request.method =='POST':
        user = User.objects.get(id = user_id)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()
        print(request.POST)
        return redirect('/users/{}'.format(user_id))
    else:
        user = User.objects.get(id = user_id)
        context = {
            'user': user
        }
        return render(request, 'restful_users/show.html', context)

def edit(request, user_id):
    user = User.objects.get(id = user_id)
    context = {
        'user': user
    }
    return render(request, 'restful_users/edit.html', context)

def delete(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('/users')
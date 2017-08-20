# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    request.session.flush()
    try:
        request.session['loggedIn']
    except KeyError:
        request.session['loggedIn'] = False
    if request.session['loggedIn']:
        return redirect('/dashboard')
    return render(request, "dashboard_app/index.html")

def signinPage(request):
    return render(request, "dashboard_app/login.html")

def registerPage(request):
    return render(request, "dashboard_app/register.html")

def signin(request):
    errors = User.objects.validateLogin(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect("/signinPage")
    else:
        loggedIn(request)
        return redirect("/dashboard")

def register(request):
    errors = User.objects.validateReg(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect("/registerPage")
    else:
        User.objects.createNew(request.POST)
        loggedIn(request)
        return redirect("/dashboard")

def displayUsers(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "dashboard_app/allUsers.html", context)

def editUserPage(request, id):
    context = {
        "user": User.objects.get(id = id)
    }
    return render(request, "dashboard_app/edit.html", context)

def editUserInfo(request, id):
    errors = User.objects.validateEditInfo(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect("/users/{}/edit".format(id))
    else:
        User.objects.editInfo(request.POST, id)
        return redirect("/dashboard")

def editUserPass(request, id):
    errors = User.objects.validateEditPass(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect("/users/{}/edit".format(id))
    else:
        User.objects.editPass(request.POST, id)
        return redirect("/dashboard")

def displayWall(request, id):
    context = {
        "pageOwner": User.objects.get(id = id),
        "messages": Message.objects.all(),
        "comments": Comment.objects.all()
    }

    return render(request, "dashboard_app/dashboard.html", context)

def newComment(request, user_id, message_id, owner_id):
    Comment.objects.create(
        comment = request.POST["comment"],
        message_id = message_id,
        user_id = user_id
    )
    return redirect('/dashboard/{}'.format(owner_id))

def newMessage(request, user_id, owner_id):
    Message.objects.create(
        message = request.POST["message"],
        created_for_id = owner_id,
        user_id = user_id
    )
    return redirect('/dashboard/{}'.format(owner_id))

def loggedIn(request):
    try:
        request.session['loggedIn'] = True
    except KeyError:
        request.session['loggedIn']
    user = User.objects.get(email = request.POST["email"])
    try:
        request.session["id"] = user.id
    except:
        request.session["id"]

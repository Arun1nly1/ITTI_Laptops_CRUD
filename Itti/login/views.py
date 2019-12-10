# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from .forms import SignupForm
from django.contrib.auth import login as auth_login, authenticate

# Create your views here.
@csrf_protect
def signup(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            user = signup.save()
            # For encryting password
            user.set_password(user.password)
            user.save()
            # username = user.username
            # pw = user.password ya encrypted pw hunxa
            # for getting password from form
             # username = signup.cleaned_data.get('username')'''
            raw_password = signup.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
               auth_login(request, user)
               return redirect('/show')

    if request.method == 'GET':
        csrfContext = RequestContext(request)
        signup_form = SignupForm()
        return render(request,'register.html',{'form':signup_form},csrfContext)

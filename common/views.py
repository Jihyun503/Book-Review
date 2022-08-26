from django.shortcuts import render, redirect

from .models import User
from .forms import *
from .decorators import *

# Create your views here.
def signup(request):
    signup_form = SignupForm()
    context = {'forms' : signup_form}

    if request.method == 'GET':
        return render(request, "signup.html", context)
    
    elif request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = User(
                id = signup_form.id,
                pwd = signup_form.pwd,
                name = signup_form.name,
                email = signup_form.email,
                nickname = signup_form.nickname
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = signup_form
            if signup_form.errors:
                for value in signup_form.errors.values():
                    context['error'] = value
        return render(request, "signup.html", context)

def login(request):
    login_form = LoginForm()
    context = {'forms' : login_form}

    if request.method == 'GET':
        return render(request, "login.html", context)

    elif request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            request.session['user'] = login_form.id
            return redirect('/')
        else:
            '''
            context['forms'] = join_form
            if join_form.errors:
                for value in join_form.errors.values():
                    context['error'] = value
            '''
            context['forms'] = login_form
        return render(request, "login.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')

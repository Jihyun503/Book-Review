from django.shortcuts import render, redirect

from reviews.models import User
from .forms import *

# Create your views here.
def login(request):
    login_form = LoginForm()
    context = {'forms' : login_form}

    if request.method == 'GET':
        return render(request, "login.html", context)

    elif request.method == 'POST':
        print("들어옴")
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

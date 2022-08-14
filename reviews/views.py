import imp
from django.shortcuts import render, redirect

from .models import User
from .forms import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def reviewList(request):
    return render(request, "reviews.html")

def writeReview(request):
    return render(request, "write.html")

def join(request):
    join_form = joinForm()
    context = {'forms' : join_form}

    if request.method == 'GET':
        return render(request, "join.html", context)
    
    elif request.method == 'POST':
        join_form = joinForm(request.POST)
        if join_form.is_valid():
            user = User(
                id = join_form.id,
                pwd = join_form.pwd,
                name = join_form.name,
                email = join_form.email,
                nickname = join_form.nickname
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = join_form
            if join_form.errors:
                for value in join_form.errors.values():
                    context['error'] = value
        return render(request, "join.html", context)

    '''
    elif request.method == 'POST':
        id = request.POST.get('id', '')
        pwd = request.POST.get('pwd', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        nickname = request.POST.get('nickname', '')

        if (id or pwd or name or email or nickname) == '':
            return redirect('join')
        else:
            user = User(
                id = id,
                pwd = pwd,
                name = name,
                email = email,
                nickname = nickname
            )
            user.save()

        return redirect('/')
    '''

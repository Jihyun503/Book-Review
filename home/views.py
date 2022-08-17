from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}

    login_session = request.session.get("user", "")
    
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True


    return render(request, "index.html", context)

from django.shortcuts import redirect
from .models import User

def login_required(func):
    def wapper(request, *arg, **kwargs):
        login_session = request.session.get("user", "")
        '''
        if login_session == '':
            return redirect('/login/')
        '''
        if login_session == '':
            return func(request, *arg, login_session=False)
        else:
            return func(request, *arg, login_session=True)

        #return func(request, *arg, **kwargs)

    return wapper


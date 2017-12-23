from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from django.core.urlresolvers import reverse

from models import User

def index(request):
    return render(request, "users/index.html")

def register(request):
    result = User.objects.validate(request.POST)
    
    if result[0]:
        request.session['username'] = request.POST['username']
        request.session['user_id'] = result[1].id
        return redirect('two:dashboard')
    else:
        for tag, error in result[1].iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

def login(request):
    print request.POST
    result = User.objects.login(request.POST)

    if result == False:
        messages.error(request, "wrong password!")
        return redirect('/')
    else:
        request.session['username'] = request.POST['username']
        request.session['user_id'] = result[1].id
        return redirect('two:dashboard')
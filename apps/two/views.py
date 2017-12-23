from django.shortcuts import render, redirect , HttpResponse
from . models import *
from django.contrib import messages
from ..users.models import User

def dashboard(request):
    post_person = User.objects.get(id=request.session['user_id'])
    context = {
        'my_quotes' : Cite.objects.filter(shared_with=post_person),
        'other_quotes' : Cite.objects.exclude(shared_with=post_person)
    }
    return render (request, 'two/dashboard.html', context)
    

def create(request):
    if "user_id" not in request.session:
        return redirect("/")
    result = Cite.objects.citation(request.POST, request.session['user_id'])

    if result [0]:
        return redirect ('two:dashboard')
    else: 
        for error in result[1]:
            messages.error(request,error)
        return redirect ('two:dashboard')

def share(request, quote_id):
    if "user_id" not in request.session:
        return redirect("/")
    Cite.objects.join(request.session['user_id'], quote_id)
    return redirect ('two:dashboard')

def summary(request, poster_id):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        'posts': Cite.objects.get(id=poster_id)
    }
    return render(request, 'two/summary.html', context)

def remove (request, quote_id):
    if "user_id" not in request.session:
        return redirect("/")
    Cite.objects.leave(request.session['user_id'], quote_id)
    return redirect ('two:dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def count(request, poster_id):
    count = Cite.objects.filter(id=poster_id).count()
    context = {
        'count': count
    }
    return render(request, 'two/summary.html', context)
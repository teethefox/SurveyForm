from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
from django.db.models.functions import Length




def index(request):
    return render(request,'index.html')
def process(request):
    
    
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['tries'] += 1
    return redirect('/result')
    

def result(request):
    return render(request,'result.html')

# Create your views here.

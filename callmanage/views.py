from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.

def home(request):
    return render_to_response('home1.html')



def test(request):
    return render_to_response('home.html')


def test2(request):
    return render_to_response('navbar.html')

def test3(request):
    return render_to_response('aside.html')

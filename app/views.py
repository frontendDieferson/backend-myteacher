from django.shortcuts import render
from app.views import render
# Create your views here.

def AppHome():
    return render('Olá Django')

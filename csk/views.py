from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def csk (request):
    return render(request,'csk.html')


def kohli (request):
    return render(request,'kohli.html')


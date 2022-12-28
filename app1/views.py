from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string1(request):
    return HttpResponse('this is string1 function of app1')


def string2(request):
    return HttpResponse('This is String2 function of app1')
    
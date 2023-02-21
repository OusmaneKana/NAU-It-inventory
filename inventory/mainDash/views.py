from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
   
    context = {
        'latest_question_list': "Test Context",
    }
    return render(request, 'mainDash/index.html', context)
def assigne_retrive(request):
    context = {
        'latest_question_list': "Test Context",
    }
    return render(request, 'mainDash/assigne_retrieve.html', context)

def add_device(request):
    context = {
        'latest_question_list': "Test Context",
    }
    return render(request, 'mainDash/add_device.html', context)

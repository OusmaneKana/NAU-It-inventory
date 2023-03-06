from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import DeviceRegistrationForm
from .forms import RecordForm


def index(request):
   
    context = {}

    return render(request, 'mainDash/index.html', context)


    
def assigne_retrieve(request):

    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'form': RecordForm()
        }

    return render(request, 'mainDash/assigne_retrieve.html', context)

def add_device(request):

    if request.method == "POST":
        form = DeviceRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'form': DeviceRegistrationForm()
        }

    return render(request, 'mainDash/add_device.html', context)

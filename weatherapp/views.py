from django.shortcuts import render
from django.http import HttpResponse
from .gweather import get_weather
from .forms import contactform
from django.contrib import messages


def search_view(request):
    if request.method == 'GET':
        if city_name:=request.GET.get('s'):
            return city_name

def index_view(request):
    if city:=search_view(request):
        info=get_weather(city)
    else:
        info = get_weather(city='Tehran')
    if info[0]=='404':
        return render(request, 'error/error_404.html',{'error_type':info[0],'rmessage':info[1]})
    else:
        return render(request, 'website/index.html',{'city':info[0],'temp':info[1],'hum':info[2],'wspeed':info[3],'date':info[4],'day':info[5]})



def contact_view(request):
    if request.method == 'POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submit successfully')
    form=contactform()

    return render(request, 'website/contact.html',{'form':form})
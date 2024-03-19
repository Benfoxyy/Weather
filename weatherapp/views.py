from django.shortcuts import render,redirect
from .gweather import get_weather
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
        return redirect('/')
    else:
        return render(request, 'website/index.html',{'city':info[0],'temp':info[1],'hum':info[2],'wspeed':info[3],'date':info[4],'day':info[5],'weather':info[6]})
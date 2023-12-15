from django.shortcuts import render,get_object_or_404
from .models import *

def news_view(request):
    posts=Post.objects.all()
    return render(request, 'news/news.html',{'posts':posts})

def single_view(request,pid):
    post=get_object_or_404(Post,pk=pid)
    return render(request,'news/single.html',{'post':post})
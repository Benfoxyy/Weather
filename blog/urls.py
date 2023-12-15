from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',news_view,name='news'),
    path('post/<int:pid>',single_view,name='single'),
]

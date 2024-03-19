from django.urls import path
from .views import *

app_name = 'weather'

urlpatterns = [
    path('',index_view,name='home'),
]
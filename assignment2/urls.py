from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from assignment2 import views

urlpatterns =[
    path('',views.home,name='home'),
]
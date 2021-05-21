from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('result', views.result, name='result'), 
    path('about', views.about, name='about' )  
]
"""Educative URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include 


urlpatterns = [
    
    path('',views.index , name='index'),
    path('login_data',views.login_data , name='login_data'),
    path('login',views.login , name='login'),
    path('logout_handeler',views.logout_handeler , name='logout_handeler'),
    path('teacher',views.teacher,name='teacher'),
    path('quizes',views.quizes,name='quizes'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('lecture_authentication',views.lecture_authentication,name='lecture_authentication'),
    path('thumnail_',views.thumnail_,name='thumnail_'),
    path('lectur_Upload',views.lectur_Upload,name='lectur_Upload'),
    path('Quize_thum',views.Quize_thum,name='Quize_thum'),
    
]

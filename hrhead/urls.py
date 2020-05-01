"""HR_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView
from hrhead import views
urlpatterns = [
    path('hr_login/',views.hr_login.as_view(),name='hr_login'),
    path('h_logincheck/',views.h_logincheck,name='h_logincheck'),
    path('h_logout/',views.h_logout,name='h_logout'),
    path('listed/',views.listed,name='listed'),
    path('selected/',views.selected,name='selected'),
    path('deselected/',views.deselected,name='deselected')


]


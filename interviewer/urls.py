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
from interviewer import views
from django.conf.urls.static import static
from HR_management import settings
urlpatterns = [
    path('i_login/',views.i_login.as_view(),name='i_login'),
    path('i_logincheck/',views.i_logincheck,name='i_logincheck'),
    path('i_logout/',views.i_logout,name='i_logout'),
    path('add_interview/',views.add_interview.as_view(),name='add_interview')

]


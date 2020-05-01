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
from django.urls import path
from django.views.generic import TemplateView
from m_app import views
from django.contrib import  admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('m_login/',TemplateView.as_view(template_name='manager/manager_login.html'),name='m_login'),
    path('logincheck/',views.logincheck,name='logincheck'),
    path('again/',views.again,name='again'),
    path('m_logout/',views.m_logout,name='m_logout'),
    path('manager_login/',views.manager_login.as_view(),name='manager_login'),
    path('recruit/',views.manager_recruit.as_view(),name='recruit'),
    path('new_recruit/',views.new_recruit.as_view(),name='new_recruit'),
    path('update_recruit/',views.update_recruit.as_view(),name='update_recruit'),
    path('delete_recruit/',views.delete_recruit.as_view(),name='delete_recruit'),
    path('inter/',views.inter.as_view(),name='inter')



]

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
from adminapp import views
from m_app import urls as manage
from applicant import urls as app
from interviewer import urls as inter
from hrhead import urls as head
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin_login/',views.admin_login.as_view(),name='admin_login'),
    path('checklogin/',views.checklogin,name='checklogin'),
    path('logout/',views.logout, name='logout'),
    path('add_employee/',views.add_employee.as_view(),name='add_employee'),
    path('view_employee/',views.view_employee.as_view(),name='view_employee'),
    path('update_employee/',views.update_employee.as_view(),name='update_employee'),
    path('update_page/<int:pk>',views.update_page.as_view(),name='update_page'),
    path('delete_employee/',views.delete_employee.as_view(), name='delete_employee'),
    path('deleted/',views.deleted,name='deleted'),
    path('',include(manage),),
    path('',include(app),),
    path('',include(inter),),
    path('',include(head),)



]

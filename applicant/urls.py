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
from applicant import views
from django.conf.urls.static import static
from HR_management import settings
urlpatterns = [
    path('a_login/',views.a_login.as_view(),name='a_login'),
    path('a_logincheck/',views.logincheck,name='a_logincheck'),
    path('a_logout/',views.logout,name='a_logout'),
    path('a_register/',views.a_register.as_view(),name='a_register'),
    path('a_post/',views.a_post.as_view(),name='a_post'),
    # path('save_post/',views.save_post,name='save_post'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
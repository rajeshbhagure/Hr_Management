from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from applicant.models import Application, Applicant
from interviewer.models import InterView


class hr_login(View):
    def get(self,request):
        return render(request,"head/login.html")
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=="rajesh" and password=="1234":
            request.session['user_id']=username
            return redirect('h_logincheck')
        else:
            messages.error(request,"Username and password Not valid...")
            return redirect('hr_login')
def h_logincheck(request):
    res=request.session.get('user_id',None)
    if res:
        return render(request, "head/hr_home.html")
    else:
        return redirect('hr_login')
def h_logout(request):
    del request.session['user_id']
    return redirect('hr_login')

def listed(request):
    return render(request,"head/listed.html",{"data":Application.objects.all()})


def selected(request):
        im=InterView.objects.filter(result='selected')
        return render(request,"head/selected.html",{"data":im})


def deselected(request):
    im = InterView.objects.filter(result='deselected')
    return render(request, "head/deselected.html", {"data": im})
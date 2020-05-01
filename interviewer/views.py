from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from interviewer.models import InterView
from  interviewer.forms import InterForm
# Create your views here.

class i_login(View):
    def get(self,request):
        return  render(request,"interviewer/login.html")
    def post(self,request):
        if request.method=='POST':
            user=request.POST.get('username')
            pas=request.POST.get('password')
            if user=='rajesh' and pas=='1234':
                request.session['user_id']=user
                return redirect('i_logincheck')
            else:
                messages.error(request,"Usename & Password Wrong...")
                return redirect('i_login')
def i_logincheck(request):
    res=request.session.get('user_id',None)
    if res:
        return render(request, "interviewer/inter_home.html", {"data": InterForm()})
    else:
        return redirect('i_login')
def i_logout(request):
    del request.session['user_id']
    return redirect('i_login')

class add_interview(View):
    def get(self,request):
        pass
    def post(self,request):
        qs=InterForm(request.POST)
        if qs.is_valid():
            qs.save()
            messages.success(request,"Data Is Saved...")
            return render(request,"interviewer/inter_home.html",)
        else:
            messages.error(request,"Provide Valid data")
            return render(request, "interviewer/inter_home.html", )


from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,UpdateView,ListView
from .models import RecruitPost
from .forms import AppForm, RecruitForm
from django.contrib import messages
from applicant.models import Applicant
# Create your views here.
class manager_login(View):
    def post(self,request):
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                if username == "manager" and password == "manager":
                    request.session["m_id"]=username
                    # request.session.set_expiry(30)
                    return redirect('logincheck')
                else:
                    return redirect('m_login')

    def get(self,request):
        return redirect('logincheck')

def logincheck(request):
    res=request.session.get('m_id',None)
    if res:
        return render(request,"manager/manager_homepage.html")
    else:
        return redirect('m_login')
def again(request):
    res = request.session.get('m_id',None)
    if res:
        return render(request,"manager/manager_homepage.html")
    else:
        return render(request,"manager/manager_login.html")

class manager_recruit(View):
    def post(self,request):
        pass
    def get(self,request):
        return render(request,"manager/recruit.html")

class new_recruit(CreateView):
    template_name = "manager/new_recruit.html"
    form_class = RecruitForm
    success_url = "/recruit/"


class update_recruit(View):
    def get(self,request):
        res=RecruitPost.objects.all()
        return render(request,"manager/update_recruit.html",{"data":res})
    def post(self,request):
        if request.method=="POST":
            opp=request.POST.get('id')
            print(opp)
            qs=RecruitPost.objects.filter(oppcode=opp)
            print(qs)
            return render(request,"manager/update_info.html",{"qs":qs})


class delete_recruit(View):
    def get(self,request):
        qs=RecruitPost.objects.all()
        return render(request,"manager/r_delete.html",{"qs":qs})
    def post(self,request):
        if request.method=="POST":
            oppo=request.POST.getlist('id')
            for id in oppo:
                RecruitPost.objects.filter(oppcode=id).delete()
            return redirect('delete_recruit')


class inter(View):
    def get(self,request):
        return render(request,"manager/inter.html",{"data":AppForm()})
    def post(self,request):
        rf=AppForm(request.POST)
        print(rf)
        if rf.is_valid():
            print("hello")
            rf.save()
            return redirect('manager_login')
        else:
            return redirect('inter')

def m_logout(request):
    del request.session['m_id']
    return redirect('m_login')



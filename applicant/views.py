from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import View
from applicant.forms import Applicant_Form,ApplicationForm
from applicant.models import Applicant
# Create your views here.
class a_login(View):
    def get(self,request):
        return render(request,"applicant/a_login.html")

    def post(self,request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            try:
                res=Applicant.objects.get(username=username,password=password)
                request.session['user_id']=res.id
                return redirect('a_logincheck')

            except Applicant.DoesNotExist:
                return render(request,"applicant/a_login.html",{"data":"Username and password are Wrong...."})


def logincheck(request):
    res=request.session.get('user_id',None)
    if res:
        return redirect('a_post')
    else:
        return redirect('a_login')
def logout(request):
    del request.session['user_id']
    return redirect('a_login')

class a_register(View):
    def get(self,request):
        return render(request,"applicant/a_register.html",{"form":Applicant_Form()})
    def post(self,request):
        af = Applicant_Form(request.POST)
        if af.is_valid():
            af.save()
            return redirect('a_login')
        else:
            messages.error(request,"Provide valid deatails")
            return redirect('a_register')

class a_post(View):

    def get(self,request):
        return render(request, "applicant/a_homepage.html",{"form":ApplicationForm()} )

    def post(self,request):
        af = ApplicationForm(request.POST, request.FILES)
        if af.is_valid():
            af.save()
            messages.success(request, "Your Application is Applied Successfully...")
            return redirect('a_post')
        else:
            messages.success(request, "Provide Valid Details...Try Again...")
            return render(request, "applicant/a_homepage.html",)









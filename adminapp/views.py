from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView
from adminapp.forms import EmpoyeeForm
from adminapp.models import EmployeeModel
# Create your views here.
class admin_login(View):
    def post(self,request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username=="admin" and password=="admin":
                request.session["admin_id"]=username
                # request.session.set_expiry(60)
                return redirect('checklogin')
            else:
                messages.error(request,"username and password wrong")
                return redirect('admin_login')

    def get(self,request):
        return render(request,"login.html")

def checklogin(request):
    res=request.session.get("admin_id",None)
    if res:
        return render(request,"admin_homepage.html")
    else:
        return redirect('admin_login')
def logout(request):
    del request.session["admin_id"]
    return redirect('admin_login')

class add_employee(View):
    def post(self,request):
        if request.method=="POST":
            ef = EmpoyeeForm(request.POST)
            if ef.is_valid():
                ef.save()
        return render(request,"add_employee.html",{"form":EmpoyeeForm(),"msg":"Employee Added..."})

    def get(self,request):
        return render(request,"add_employee.html",{"form":EmpoyeeForm()})

class view_employee(View):
    def post(self,request):
        pass
    def get(self,request):
        return render(request,"view_employee.html",{"qs":EmployeeModel.objects.all()})

class update_employee(View):
    def post(self,request):
        pass
    def get(self,request):
        return render(request, "update_view.html", {"qs": EmployeeModel.objects.all()})

class update_page(UpdateView):
    template_name = "update.html"
    model = EmployeeModel
    fields =("Emp_name","Emp_name","address","address","contactno","contactno","Designation","Designation","email","email","password","password")
    success_url = "/update_employee/"

class delete_employee(View):
    def post(self,request):
        pass
    def get(self,request):
        qs=EmployeeModel.objects.all()
        return render(request, "delete_view.html",{"qs":qs})

def deleted(request):
    id=request.GET.get('id')
    em=EmployeeModel.objects.filter(id=id)
    em.delete()
    return redirect('delete_employee')



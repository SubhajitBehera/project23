from django.shortcuts import render,redirect
from app23.models import Employee,AccountInfo
from django.contrib import messages

def showIndex(request):
    return render(request,"index.html")

def add_emp(request):
    return render(request,'add_emp.html')

def save_emp(request):
    eno=request.POST.get("e1")
    ena=request.POST.get("e2")
    Employee(idno=eno,name=ena).save()
    messages.success(request,"Employee is Saved")
    return redirect("main")

def view_emp(request):
    return render(request,'view_emp.html',{"data":Employee.objects.all()})

def add_acc(request):
    return render(request,'add_acc.html',{"data":Employee.objects.all()})

def save_account(request):
    acno=request.POST.get("t1")
    bn=request.POST.get("t2")
    code=request.POST.get("t3")
    eid=request.POST.get("t4")
    AccountInfo(acno=acno,branch=bn,ifsc=code,emp_id=eid).save()
    messages.success(request,"Account is Saved")
    return redirect("main")

def view_acc(request):
    return render(request,"view_acc.html",{"data":AccountInfo.objects.all()})

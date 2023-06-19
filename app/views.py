from django.shortcuts import render
from . models import *
from .forms import *
from django.http.response import HttpResponse
from django.contrib import messages


def index(request):
    D = Doctor.objects.all()
    return render(request, 'index.html', {"D": D})


def appoinment(request):
    if request.method=='POST':
        name = request.POST['name']
        email =request.POST['email']
        address =request.POST['add']
        id= request.POST['doctor']
        d=Doctor.objects.get(id=id)
        apoinment = request.POST.getlist('appoinment')
        date=request.POST['date']
        issue = request.POST['message']
        P=Patient.objects.create(name=name,email=email,address=address,Doctor=d,apoinment=apoinment,date=date,issue=issue)
        P.save()
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def confirm(request, id):
    activity.objects.all()
    f = activityform()
    return render(request, 'update.html', {'f': f})


def delete(request, id):
    id = Patient.objects.get(id=id)
    id.delete()
    p = Patient.objects.all()
    return render(request, 'activity.html', {"p": p})


def Dlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['pwd']
        if Doctor.objects.filter(email=email).exists() and Doctor.objects.filter(pwd=pwd).exists():

            #     # D=Doctor.objects.get(email=email)
            #       return render(request,'activity.html',{'m','YOU HAVE NO PATIENT'})
            #     else:
            p = Patient.objects.all()
            return render(request, 'activity.html', {"p": p})
            # except:
            #    return render(request,'activity.html',{'m','YOU HAVE NO PATIENT'})
        else:
            return render(request, 'index.html', {'messages': "EMAIL OR PASSWORD WROGN CHECK IT"})
    else:
        return render(request, 'index.html')

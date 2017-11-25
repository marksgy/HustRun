from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import session

from .models import Student


# Create your views here.

@csrf_exempt
def signUp(request):
    name=request.POST.get("name","")
    psd=request.POST.get("psd","")
    studentId=request.POST.get("studentId","")
    students=Student.objects.filter(name=name)
    msg={}
    if students:
        msg["status"]=2
    else:
        msg["status"]=1
        Student.objects.create(name=name,psd=psd,studentId=studentId)
        request.session["name"]=name

    return JsonResponse(msg)


@csrf_exempt
def login(request):
    name = request.POST.get("name", "")
    psd = request.POST.get("psd", "")
    students = Student.objects.filter(name=name)
    msg={}
    if students:
        student=students[0]
        if psd==student.psd:
            msg["status"]=1
            request.session["name"]=name
        else:
            msg["status"]=0
    else:
        msg["status"]=0

    return JsonResponse(msg)
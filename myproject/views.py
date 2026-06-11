from django.http import HttpResponseBadRequest,request,HttpRequest
from django.shortcuts import render
from new.models import New
def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Subject = request.POST.get('Subject')
        Message = request.POST.get('Message')
        en = New(Name=Name,Email=Email,Subject=Subject,Message=Message)
        en.save()
    return render(request,'contact.html')

def skills(request):
    return render(request,'skills.html')

def work(request):
    return render(request,'work.html')
def about(request):
    return render(request,'about.html')

def booknow(request):
    # if request.method == "POST":
    #     Name = request.POST.get('Name')
    #     Email = request.POST.get('Email')
    #     Subject = request.POST.get('Subject')
    #     Message = request.POST.get('Message')
    #     en = New(Name=Name,Email=Email,Subject=Subject,Message=Message)
    #     en.save()
    return render(request,'booknow.html')

    
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')

def services_welcome(request):
    return render(request,'services_welcome.html')

def about_welcome(request):
    return render(request,'about_welcome.html')

def articles_welcome(request):
    return render(request,'articles_welcome.html')

def articles(request):
    return render(request,'articles.html')

def about(request):
    return render(request,'about.html')

def diet(request):
    return render(request,'diet.html')

def immune(request):
    return render(request,'immune.html')

def kidney(request):
    return render(request,'kidney.html')


def getstarted(request):
    return render(request,'getstarted.html')

def logo(request):
    return render(request,'logo.html')

def lungs(request):
    return render(request,'lungs.html')

def physical(request):
    return render(request,'physical.html')

def heart(request):
    return render(request,'heart.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def welcome(request):
    return render(request,'welcome.html')

def lab_locator(request):
    return render(request,'lab_locator.html')

def med_locator(request):
    return render(request,'med_locator.html')

def labsample(request):
    return render(request,'labsample.html')

def search_results(request):
    return render(request,'search_results.html')

def labgui(request):
    return render(request,'labgui.html')

def dashboard(request):
    return render(request,'dashboard.html')

def appointments(request):
    return render(request,'appointments.html')

def appointment_success(request):
    return render(request, 'appointment_success.html')

def medicines(request):
    return render(request, 'medicines.html')

from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')


def logout(request):
    return render(request,'home.html')


def signup(request):
    return render(request,'signup.html')


def profile(request):
    return render(request,'profile.html')




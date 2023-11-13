from django.shortcuts import render

# Create your views here.

# this is a view or logic for Homepage of website
def homepage(request):
    return render(request,'home.html')



def browse(request):
    return render(request,'browse.html')



def streams(request):
    return render(request,'streams.html')
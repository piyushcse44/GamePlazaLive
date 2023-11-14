from django.shortcuts import render
from .models import GameList
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .constants import get_name,compress_download
from .pagination import paginate
# Create your views here.


# this is a view or logic for Homepage of website
def homepage(request):
    queryset = GameList.objects.all()[:8]
  #compress download
    compress_download(queryset)
    data = {'results':queryset}
    return render(request,'home.html',data)


# this is a view or logic for browser of website
def browse(request):
    return render(request,'browse.html')


# this is a view or logic for stream section of website
def streams(request):
    return render(request,'streams.html')


# this is a view or logic if someone search somehing from search bar
def search(request):

    # retriev search keyword which is send from frontend
    search_keyword =  get_name(request,'search_keyword')  
    
    # search for games on the basic of their name or company name
    queryset = GameList.objects.filter(
        Q(name__icontains = search_keyword)  
        |                                   
        Q(company_name__icontains = search_keyword) 
     )
    # paginate to page number given by forntend and result are the count of item in one page
    queryset = paginate(request,queryset)

    # compress downloads
    compress_download(queryset)
    
    data ={
        'search_keyword':search_keyword,
        'results':queryset,
    }

    
    
    
   

    return render(request,'all_items.html',data)
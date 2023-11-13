from django.shortcuts import render
from .models import GameList
from django.db.models import Q
from .constants import compress_number
# Create your views here.




# this is a view or logic for Homepage of website
def homepage(request):
    return render(request,'home.html')


# this is a view or logic for browser of website
def browse(request):
    return render(request,'browse.html')


# this is a view or logic for stream section of website
def streams(request):
    return render(request,'streams.html')


# this is a view or logic if someone search somehing from search bar
def search(request):

    search_keyword = ""
    if request.GET.get("searchKeyword"):
        search_keyword = request.GET.get("searchKeyword")

    
    queryset = GameList.objects.filter(
        Q(name__icontains = search_keyword)
        |
        Q(company_name__icontains = search_keyword)
     )


    data ={
        'search_keyword':search_keyword,
        'results':queryset
    }

    # compress downloads
    for queryobj in data['results']:
        queryobj.total_downloads = compress_number(queryobj.total_downloads)
    
   

    return render(request,'all_items.html',data)
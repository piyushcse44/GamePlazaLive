from .models import GameList
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .constants import get_name


def paginate(request,queryset,result):

    page =1

    p = Paginator(queryset,result)

    try:
        page = request.GET.get('page')
    except PageNotAnInteger:
        page =1
    except EmptyPage:
        page = p.num_pages

    queryset = p.page(page)   

    return queryset 
    






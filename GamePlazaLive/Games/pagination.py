from .models import GameList
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .constants import count_item_in_each_page



def paginate(request, queryset):

    page_number = request.GET.get('page', 1)

    paginator = Paginator(queryset, count_item_in_each_page)

    try:
        paginated_queryset = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        paginated_queryset = paginator.page(paginator.num_pages)

    return paginated_queryset
